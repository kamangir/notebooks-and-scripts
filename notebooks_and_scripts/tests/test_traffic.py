import pytest
from notebooks_and_scripts.aws_batch.traffic.classes import Traffic
from notebooks_and_scripts.aws_batch.traffic.patterns import list_of_patterns


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
def test_Traffic(pattern: str):
    assert Traffic().create(pattern)
