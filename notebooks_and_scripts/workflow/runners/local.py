from typing import Any, List, Tuple
from tqdm import tqdm
from abcli.modules import objects
from abcli import file
from abcli.modules import objects
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.runners.generic import GenericRunner
from notebooks_and_scripts.logger import logger


class LocalRunner(GenericRunner):
    def __init__(self, **kw_args):
        super().__init__(**kw_args)
        self.type: RunnerType = RunnerType.LOCAL

    def monitor_function(self, workflow: Workflow) -> Workflow:
        workflow = super().monitor_function(workflow)

        for node in tqdm(self.G.notes):
            if file.exists(
                objects.path_of(
                    "metadata.yaml",
                    workflow.node_job_name(node),
                )
            ):
                workflow.G.nodes[node]["status"] = "SUCCEEDED"

        return workflow

    def submit_command(
        self,
        command_line: str,
        job_name: str,
        dependencies: List[str],
        verbose: bool = False,
    ) -> Tuple[bool, Any]:
        super().submit_command(command_line, job_name, dependencies, verbose)

        filename = objects.path_of(f"{job_name}.sh", job_name)
        success, script = file.load_text(filename, civilized=True, log=True)
        if not success:
            script = ["#! /usr/bin/env bash", ""]

        script += [command_line]

        return file.save_text(filename, script), {"job_id": job_name}
