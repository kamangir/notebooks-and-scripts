from typing import Dict, Any, Tuple, List
import boto3
import glob
from tqdm import tqdm
from abcli import file
from abcli import string
from abcli.modules import objects
from abcli.plugins.graphics.gif import generate_animated_gif
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

    def monitor(
        self,
        workflow: Workflow,
        hot_node: str = "void",
    ) -> bool:
        assert super().monitor(workflow)

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

        if not dot_file.export_graph_as_image(
            workflow.G,
            objects.path_of(
                "workflow-{}.png".format(
                    string.pretty_date(as_filename=True, unique=True),
                ),
                workflow.job_name,
            ),
            colormap=dot_file.status_color_map,
            hot_node=hot_node,
        ):
            return False

        return generate_animated_gif(
            [
                filename
                for filename in sorted(
                    glob.glob(objects.path_of("workflow-*.png", workflow.job_name))
                )
                if len(file.name(filename)) > 15
            ],
            objects.path_of("workflow.gif", workflow.job_name),
            frame_duration=333,
        )

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
