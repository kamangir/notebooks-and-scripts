import networkx as nx
from abcli.modules import objects
from abcli.plugins.metadata import post, MetadataSourceType
from notebooks_and_scripts import env
from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.workflow import dot_file
from notebooks_and_scripts.workflow.patterns import load_pattern
from notebooks_and_scripts.workflow.runners import RunnerType


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

        self.runner: RunnerType = RunnerType.PENDING

    def load_file(self, filename: str) -> bool:
        success, self.G = dot_file.load_from_file(filename)
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
        logger.info("not implemented.")
        return False

    def submit(self, dryrun: bool = True) -> bool:
        logger.info("not implemented.")
        return False
