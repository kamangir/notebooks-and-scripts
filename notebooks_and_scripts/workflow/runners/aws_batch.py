from typing import Dict, Any, Tuple, List
import boto3
import glob
from tqdm import tqdm
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.workflow import dot_file
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.runners.generic import GenericRunner
from notebooks_and_scripts.aws_batch.submission import submit, SubmissionType


class AWSBatchRunner(GenericRunner):
    def __init__(self, **kw_args):
        super().__init__(**kw_args)
        self.type: RunnerType = RunnerType.AWS_BATCH

    def monitor_function(
        self,
        workflow: Workflow,
        hot_node: str,
    ) -> Workflow:
        workflow = super().monitor_function(workflow, hot_node)

        client = boto3.client("batch")

        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_jobs.html
        page_size = 100
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

        return workflow

    def submit_command(
        self,
        command_line: str,
        job_name: str,
        dependencies: List[str],
        verbose: bool = False,
    ) -> Tuple[bool, Any]:
        super().submit_command(command_line, job_name, dependencies, verbose)

        return submit(
            f"- {command_line}",
            job_name,
            SubmissionType.EVAL,
            dependency_job_id_list=dependencies,
            verbose=verbose,
        )
