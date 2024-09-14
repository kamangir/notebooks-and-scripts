from typing import Dict, Any, Tuple, List
import boto3
import math
from tqdm import tqdm
from blue_options import string
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

    def submit(
        self,
        workflow: Workflow,
        dryrun: bool = True,
        max_dependency: int = 20,
    ) -> bool:
        list_of_nodes = list(workflow.G.nodes.keys())
        for node in list_of_nodes:
            dependency_list = list(workflow.G.successors(node))
            if len(dependency_list) <= max_dependency:
                continue

            proxy_count = math.ceil(len(dependency_list) / (max_dependency - 1)) - 1
            suffix = string.random(length=3, alphabet="0123456789")
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
            for proxy in proxy_list:
                workflow.G.add_node(proxy)
                workflow.G.nodes[proxy]["command_line"] = " ".join(
                    [
                        "workflow monitor",
                        f"node={proxy}",
                        self.job_name,
                    ]
                )

            previous_proxy = node
            for index, node_ in enumerate(dependency_list):
                proxy_index = int(index / (max_dependency - 1))
                if proxy_index < 1:
                    continue

                proxy = proxy_list[proxy_index - 1]

                workflow.G.remove_edge(node, node_)

                if proxy != previous_proxy:
                    workflow.G.add_edge(previous_proxy, proxy)
                    previous_proxy = proxy

                workflow.G.add_edge(proxy, node_)

                logger.info(
                    "{}->{} -> {}->{}->{}".format(
                        node,
                        node_,
                        node,
                        proxy,
                        node_,
                    )
                )

        return workflow.save() and super().submit(workflow, dryrun)

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
