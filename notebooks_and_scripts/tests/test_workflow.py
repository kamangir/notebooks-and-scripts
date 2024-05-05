import pytest
from abcli.modules.objects import unique_object
from notebooks_and_scripts import env
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.patterns import list_of_patterns


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
def test_workflow(pattern: str):
    job_name = unique_object()

    workflow = Workflow(job_name)

    assert workflow.load_pattern(pattern)
