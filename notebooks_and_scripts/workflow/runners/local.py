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

    def monitor_function(
        self,
        workflow: Workflow,
        hot_node: str,
    ) -> Workflow:
        workflow = super().monitor_function(workflow, hot_node)

        for node in tqdm(workflow.G.nodes):
            if file.exist(
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

        filename = objects.path_of(f"{self.job_name}.sh", self.job_name)
        success, script = file.load_text(filename, civilized=True, log=True)
        if not success:
            script = ["#! /usr/bin/env bash", ""]

        script += [f"abcli_eval - {command_line}"]

        return file.save_text(filename, script, log=True), {"job_id": job_name}
