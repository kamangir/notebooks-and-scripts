import pytest
from abcli.modules.objects import unique_object
from notebooks_and_scripts import env
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.workflow.runners import RunnerType


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
@pytest.mark.parametrize(
    ["command_line"],
    [
        [env.ABCLI_AWS_BATCH_DEFAULT_WORKFLOW_COMMAND_UQ],
    ],
)
@pytest.mark.parametrize(
    ["runner_type"],
    [runner_type for runner_type in RunnerType],
)
def test_workflow(
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

    assert workflow.submit(runner_type, dryrun=True)
