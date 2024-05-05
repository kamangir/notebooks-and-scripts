import pytest
from abcli.modules.objects import unique_object
from notebooks_and_scripts import env
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.patterns import list_of_patterns


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
def test_workflow(
    pattern: str,
    command_line: str,
):
    job_name = unique_object()

    workflow = Workflow(job_name)

    assert workflow.load_pattern(
        command_line,
        pattern,
    )
