from typing import Dict, Any
import boto3
import glob
import networkx as nx
from tqdm import tqdm
from abcli import file
from abcli import string
from abcli.modules import objects
from abcli.plugins.metadata import get, post, MetadataSourceType
from abcli.plugins.graphics.gif import generate_animated_gif
from notebooks_and_scripts import env
from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.workflow import dot_file
from notebooks_and_scripts.aws_batch.submission import submit, SubmissionType
from notebooks_and_scripts.workflow.dot_file import (
    load_from_file,
    export_graph_as_image,
    status_color_map,
)
from notebooks_and_scripts.workflow.patterns import load_pattern
from notebooks_and_scripts.workflow.runners import Runner


class Workflow:
    def __init__(
        self,
        job_name: str = "",
        load: bool = False,
        verbose: bool = False,
    ):
        self.job_name = job_name if job_name else objects.unique_object()

        self.verbose = verbose

        self.G: nx.DiGraph = nx.DiGraph()

        if load:
            assert self.load_from(
                objects.path_of(
                    filename="workflow.dot",
                    object_name=self.job_name,
                )
            )

    def load_file(self, filename: str) -> bool:
        success, self.G = load_from_file(filename)
        return success

    def load_pattern(
        self,
        command_line: str = env.ABCLI_AWS_BATCH_DEFAULT_WORKFLOW_COMMAND_UQ,
        pattern: str = env.ABCLI_AWS_BATCH_DEFAULT_WORKFLOW_PATTERN,
    ) -> bool:
        success, self.G = load_pattern(
            pattern=pattern,
            export_as_image=objects.path_of(f"{pattern}.png", self.job_name),
        )
        if not success:
            return success

        for node in self.G.nodes:
            self.G.nodes[node]["command_line"] = command_line.replace(
                "{job_name}",
                self.job_name,
            )

        return post(
            "load_pattern",
            {
                "command_line": command_line,
                "pattern": pattern,
            },
            source=self.job_name,
            source_type=MetadataSourceType.OBJECT,
        )

    @staticmethod
    def monitor(job_name: str) -> bool:
        workflow = Workflow(job_name, load=True)

        # TODO: load runner from metadata and act accordingly.

        logger.info(f"{workflow.__class__.__name__}.monitor: {job_name} @ {workflow.G}")

        client = boto3.client("batch")

        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_jobs.html
        page_size = 100
        summary: Dict[str, str] = {}
        for index in tqdm(range(0, len(workflow.G.nodes), page_size)):
            nodes = list(workflow.G.nodes)[index : index + page_size]

            jobs = [
                workflow.G.nodes[node].get("job_id").replace('"', "") for node in nodes
            ]

            response = client.describe_jobs(jobs=jobs)

            status: Dict[str, str] = {}
            for item in response["jobs"]:
                status[item["jobId"]] = item["status"]

            for node, job_id in zip(nodes, jobs):
                workflow.G.nodes[node]["status"] = status[job_id]

                summary.setdefault(status[job_id], []).append(node)

        for status, nodes in summary.items():
            logger.info("{}: {}".format(status, ", ".join(sorted(nodes))))

        if not export_graph_as_image(
            workflow.G,
            objects.path_of(
                "workflow-{}.png".format(
                    string.pretty_date(as_filename=True, unique=True),
                ),
                job_name,
            ),
            colormap=status_color_map,
        ):
            return False

        return generate_animated_gif(
            [
                filename
                for filename in sorted(
                    glob.glob(objects.path_of("workflow-*.png", job_name))
                )
                if len(file.name(filename)) > 15
            ],
            objects.path_of("workflow.gif", job_name),
            frame_duration=333,
        )

    def submit(
        self,
        runner: Runner,
        dryrun: bool = True,
    ) -> bool:
        logger.info(f"{self.G} -> {runner}")

        metadata: Dict[str, Any] = {}
        failure_count: int = 0
        round: int = 1
        while not all(self.G.nodes[node].get("job_id") for node in self.G.nodes):
            for node in tqdm(self.G.nodes):
                if self.G.nodes[node].get("job_id"):
                    continue

                pending_dependencies = [
                    node_
                    for node_ in self.G.successors(node)
                    if not self.G.nodes[node_].get("job_id")
                ]
                if pending_dependencies:
                    logger.info(
                        "⏳ node {}: {} pending dependenci(es): {}".format(
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
                    dependency_job_id_list=[
                        self.G.nodes[node_].get("job_id")
                        for node_ in self.G.successors(node)
                    ],
                    verbose=False,
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
            objects.path_of("workflow.dot", self.job_name),
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
