from blue_objects.objects import unique_object

from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.runners.aws_batch import AWSBatchRunner


def test_workflow_runners_aws_batch():
    job_name = unique_object()

    workflow = Workflow(job_name)
    workflow.G.add_node("root")
    workflow.G.nodes["root"]["command_line"] = " ".join(
        [
            "workflow monitor",
            "node=root",
            job_name,
        ]
    )

    for node in [f"node-{index:04d}" for index in range(100)]:
        workflow.G.add_node(node)
        workflow.G.add_edge("root", node)
        workflow.G.nodes[node]["command_line"] = " ".join(
            [
                "workflow monitor",
                f"node={node}",
                job_name,
            ]
        )

    runner = AWSBatchRunner()

    assert runner.submit(workflow, dryrun=True)
