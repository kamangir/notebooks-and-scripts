from typing import Dict, Any
import boto3
import glob
from tqdm import tqdm
from abcli import file
from abcli import string
from abcli.modules import objects
from abcli.plugins.graphics.gif import generate_animated_gif
from abcli.plugins.metadata import post, MetadataSourceType
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

    def submit(
        self,
        workflow: Workflow,
        dryrun: bool = True,
    ) -> bool:
        assert super().submit(workflow, dryrun)

        metadata: Dict[str, Any] = {}
        failure_count: int = 0
        round: int = 1
        while not all(
            workflow.G.nodes[node].get("job_id") for node in workflow.G.nodes
        ):
            for node in tqdm(workflow.G.nodes):
                if workflow.G.nodes[node].get("job_id"):
                    continue

                pending_dependencies = [
                    node_
                    for node_ in workflow.G.successors(node)
                    if not workflow.G.nodes[node_].get("job_id")
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

                command_line = workflow.G.nodes[node]["command_line"]
                job_name = f"{workflow.job_name}-{node}"

                if dryrun:
                    workflow.G.nodes[node]["job_id"] = f"dryrun-round-{round}"
                    logger.info(f"{command_line} -> {job_name}")
                    continue

                success, metadata[node] = submit(
                    f"- {command_line}",
                    job_name,
                    SubmissionType.EVAL,
                    dependency_job_id_list=[
                        workflow.G.nodes[node_].get("job_id")
                        for node_ in workflow.G.successors(node)
                    ],
                    verbose=False,
                )
                if not success:
                    failure_count += 1

                workflow.G.nodes[node]["job_id"] = (
                    metadata[node]["jobId"] if success else "failed"
                )

            logger.info(f"end of round {round}")
            round += 1

        if failure_count:
            logger.error(f"{failure_count} failure(s).")

        if not dot_file.save_to_file(
            objects.path_of("workflow.dot", workflow.job_name),
            workflow.G,
        ):
            return False

        if not post(
            "submission",
            {
                "metadata": metadata,
                "failure_count": failure_count,
            },
            source=workflow.job_name,
            source_type=MetadataSourceType.OBJECT,
        ):
            return False

        return failure_count == 0
