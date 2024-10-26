import pytest

from blue_objects.objects import unique_object

from blueflow import env
from blueflow.workflow.generic import Workflow
from blueflow.workflow.patterns import list_of_patterns


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
def test_workflow(pattern: str):
    job_name = unique_object()

    workflow = Workflow(job_name)

    assert workflow.load_pattern(pattern)
