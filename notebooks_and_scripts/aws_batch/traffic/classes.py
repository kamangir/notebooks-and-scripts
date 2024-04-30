from typing import Dict, Any
import networkx as nx
from tqdm import tqdm
from abcli.modules import objects
from abcli.plugins.metadata import post, MetadataSourceType
from notebooks_and_scripts import env
from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.aws_batch import dot_file
from notebooks_and_scripts.aws_batch.submission import submit, SubmissionType
from notebooks_and_scripts.aws_batch.traffic import NAME
from notebooks_and_scripts.aws_batch.traffic.patterns import load_pattern


class Traffic:
    def __init__(
        self,
        job_name: str = "",
        verbose: bool = False,
    ):
        self.job_name = job_name if job_name else objects.unique_object()

        self.verbose = verbose

        self.G: nx.DiGraph = nx.DiGraph()

        self.valid: bool = True

    def load_pattern(
        self,
        command_line: str = env.ABCLI_AWS_BATCH_DEFAULT_TRAFFIC_COMMAND_UQ,
        pattern: str = env.ABCLI_AWS_BATCH_DEFAULT_TRAFFIC_PATTERN,
    ) -> bool:
        success, self.G = load_pattern(
            pattern=pattern,
            export_as_image=objects.path_of(f"{pattern}-input.png", self.job_name),
        )
        if not success:
            return success

        for node in self.G.nodes:
            self.G.nodes[node]["command_line"] = command_line.replace(
                "{job_name}",
                self.job_name,
            )

        if not post(
            "load_pattern",
            {
                "command_line": command_line,
                "pattern": pattern,
            },
            source=self.job_name,
            source_type=MetadataSourceType.OBJECT,
        ):
            return False

        return True

    def submit(
        self,
        dryrun: bool = True,
    ) -> bool:
        metadata: Dict[str, Any] = {}
        failure_count: int = 0
        round: int = 1
        while not all(self.G.nodes[node].get("job_id") for node in self.G.nodes):
            for node in tqdm(self.G.nodes):
                if self.G.nodes[node].get("job_id"):
                    continue

                pending_dependencies = [
                    node_
                    for node_ in self.G.predecessors(node)
                    if not self.G.nodes[node_].get("job_id")
                ]
                if pending_dependencies:
                    logger.info(
                        "node {}: {} pending dependenci(es): {}".format(
                            node,
                            len(pending_dependencies),
                            ", ".join(pending_dependencies),
                        )
                    )
                    continue

                command_line = self.G.nodes[node]["command_line"]
                job_name = f"{self.job_name}-{node}"

                if dryrun:
                    self.G.nodes[node]["job_id"] = f"dryrun-round-{round}"
                    logger.info(f"{command_line} -> {job_name}")
                    continue

                success, metadata[node] = submit(
                    f"- {command_line}",
                    job_name,
                    SubmissionType.EVAL,
                )
                if not success:
                    failure_count += 1

                self.G.nodes[node]["job_id"] = (
                    metadata[node]["jobId"] if success else "failed"
                )

            logger.info(f"end of round {round}")
            round += 1

        if failure_count:
            logger.error(f"{failure_count} failure(s).")

        if not dot_file.save_to_file(
            objects.path_of(f"traffic.dot", self.job_name),
            self.G,
            export_as_image=".png",
        ):
            return False

        if not post(
            "submission",
            {
                "metadata": metadata,
                "failure_count": failure_count,
            },
            source=self.job_name,
            source_type=MetadataSourceType.OBJECT,
        ):
            return False

        return failure_count == 0
