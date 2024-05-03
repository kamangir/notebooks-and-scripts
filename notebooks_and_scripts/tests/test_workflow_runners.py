import pytest
from abcli.modules.objects import unique_object
from notebooks_and_scripts import env
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.runners.factory import runner_class
from notebooks_and_scripts.workflow.runners.generic import GenericRunner


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
@pytest.mark.parametrize(
    ["command_line"],
    [
        [env.NBS_DEFAULT_WORKFLOW_COMMAND_UQ],
    ],
)
@pytest.mark.parametrize(
    ["runner_type"],
    [[runner_type] for runner_type in RunnerType],
)
def test_workflow_runners(
    pattern: str,
    command_line: str,
    runner_type: str,
):
    job_name = unique_object()

    workflow = Workflow(job_name)

    assert workflow.load_pattern(
        command_line,
        pattern,
    )

    runner = runner_class[RunnerType[runner_type.upper()]]()
    assert isinstance(runner, GenericRunner)

    assert runner.submit(workflow, dryrun=True)
