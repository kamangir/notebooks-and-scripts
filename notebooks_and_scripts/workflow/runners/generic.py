from typing import Any, List, Tuple
from blueness import module
from notebooks_and_scripts import NAME
from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.runners.factory import RunnerType


NAME = module.name(__file__, NAME)


class GenericRunner:
    def __init__(self):
        self.type: RunnerType = RunnerType.GENERIC

    def monitor(
        self,
        workflow: Workflow,
        hot_node: str = "void",
    ) -> bool:
        logger.info(f"{self.__class__.__name__}.monitor: {workflow.G} @ {hot_node}")

        return True

    def submit(
        self,
        workflow: Workflow,
        dryrun: bool = True,
    ) -> bool:
        workflow.runner_type = self.type.name.lower()

        logger.info(f"{self.__class__.__name__}.submit({workflow.G}, dryrun={dryrun})")

        return True

    def submit_command(
        self,
        command_line: str,
        job_name: str,
        dependencies: List[str],
        verbose: bool = False,
    ) -> Tuple[bool, Any]:
        logger.info(
            "⏳ {}: {}".format(
                job_name,
                command_line,
            )
        )
        return True, {"id": job_name}
