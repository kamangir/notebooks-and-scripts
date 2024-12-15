from typing import Dict, Any, Tuple, List
import boto3
import math
from tqdm import tqdm

from blue_options import string
from blueflow.workflow.generic import Workflow
from blueflow.logger import logger
from blueflow.workflow.runners.generic import GenericRunner
from blueflow.aws_batch.submission import submit, SubmissionType


class AWSBatchRunner(GenericRunner):
    def __init__(self, **kw_args):
        super().__init__(**kw_args)
        self.type_name: str = "aws_batch"

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

    def set_max_dependency(
        self,
        workflow: Workflow,
        node: str,
        max_dependency: int = 20,
    ):
        dependency_list = list(workflow.G.successors(node))
        if len(dependency_list) <= max_dependency:
            return

        proxy_count = math.ceil(len(dependency_list) / max_dependency)
        suffix = string.random(length=5)
        logger.info(
            "@ {}: {} dependencies > {} - adding {} proxy(s) @ {}.".format(
                node,
                len(dependency_list),
                max_dependency,
                proxy_count,
                suffix,
            )
        )

        proxy_list = [
            "{}-{}-{:03d}".format(node, suffix, index + 1)
            for index in range(proxy_count)
        ]
        node_index: int = 0
        for proxy in proxy_list:
            workflow.G.add_node(proxy)
            workflow.G.nodes[proxy]["command_line"] = " ".join(
                [
                    "blueflow_workflow monitor",
                    f"node={proxy}",
                    self.job_name,
                    "abcli_log ✅",
                ]
            )
            workflow.G.add_edge(node, proxy)

            for _ in range(max_dependency):
                if node_index >= len(dependency_list):
                    break

                node_ = dependency_list[node_index]

                workflow.G.add_edge(proxy, node_)
                workflow.G.remove_edge(node, node_)

                node_index += 1

                logger.info(
                    "{}->{} => {}->{}->{}".format(
                        node,
                        node_,
                        node,
                        proxy,
                        node_,
                    )
                )

        self.set_max_dependency(
            workflow,
            node,
            max_dependency,
        )

    def submit(
        self,
        workflow: Workflow,
        dryrun: bool = True,
        max_dependency: int = 20,
    ) -> bool:
        self.job_name = workflow.job_name

        list_of_nodes = list(workflow.G.nodes.keys())
        for node in list_of_nodes:
            self.set_max_dependency(
                workflow,
                node,
                max_dependency,
            )

        return workflow.save() and super().submit(workflow, dryrun)

    def submit_command(
        self,
        command_line: str,
        job_name: str,
        dependencies: List[str],
        verbose: bool = False,
        type: str = "cpu",
    ) -> Tuple[bool, Any]:
        assert super().submit_command(
            command_line,
            job_name,
            dependencies,
            verbose,
            type,
        )[0]

        # ignore type - all jobs are cpu.
        return submit(
            f"- {command_line}",
            job_name,
            SubmissionType.EVAL,
            dependency_job_id_list=dependencies,
            verbose=verbose,
        )
