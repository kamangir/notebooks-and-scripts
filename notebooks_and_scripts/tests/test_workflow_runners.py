import pytest
from abcli.modules.objects import unique_object
from notebooks_and_scripts.workflow.runners import list_of_runners
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.runners.factory import runner_class
from notebooks_and_scripts.workflow.runners.generic import GenericRunner


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

    runner = runner_class[runner_type]()
    assert isinstance(runner, GenericRunner)

    assert runner.submit(workflow, dryrun=True)
