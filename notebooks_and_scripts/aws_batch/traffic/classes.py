import networkx as nx
from abcli import string
from abcli.modules import objects
from abcli.plugins.metadata import post, MetadataSourceType
from notebooks_and_scripts import env
from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.aws_batch import dot_file
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

    def create(
        self,
        pattern: str = env.ABCLI_AWS_BATCH_DEFAULT_TRAFFIC_PATTERN,
        command_line: str = env.ABCLI_AWS_BATCH_DEFAULT_TRAFFIC_COMMAND_UQ,
        dryrun: bool = True,
    ) -> bool:
        if not self.load_pattern(command_line, pattern):
            return False

        self.assign_status()

        logger.info("🪄")

        if not dot_file.save_to_file(
            objects.path_of(f"{pattern}.dot", self.job_name),
            self.G,
            export_as_image=".png",
        ):
            return False

        return post(
            NAME,
            {
                "command_line": command_line,
                "pattern": pattern,
                "submission": {},
            },
            source=self.job_name,
            source_type=MetadataSourceType.OBJECT,
            verbose=self.verbose,
        )

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

        return True

    def assign_status(self):
        for node in self.G.nodes:
            self.G.nodes[node]["status"] = (
                "RUNNABLE" if self.G.in_degree(node) == 0 else "SUBMITTED"
            )
