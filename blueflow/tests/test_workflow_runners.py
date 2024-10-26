import pytest
from blue_objects.objects import unique_object

from blueflow.workflow.runners import list_of_runners, RunnerType
from blueflow.workflow.generic import Workflow
from blueflow.workflow.patterns import list_of_patterns
from blueflow.workflow.runners.factory import runner_class
from blueflow.workflow.runners.generic import GenericRunner


def test_list_of_runners():
    assert list_of_runners()


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
@pytest.mark.parametrize(
    ["runner_type"],
    [[runner_type] for runner_type in list_of_runners()],
)
def test_workflow_runners(
    pattern: str,
    runner_type: str,
):
    job_name = unique_object()

    workflow = Workflow(job_name)

    assert workflow.load_pattern(pattern)

    runner = runner_class[RunnerType[runner_type.upper()]]()
    assert isinstance(runner, GenericRunner)

    assert runner.submit(workflow, dryrun=True)
