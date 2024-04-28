import pytest
from notebooks_and_scripts import env
from notebooks_and_scripts.aws_batch.traffic.patterns import (
    load_pattern,
    list_of_patterns,
)


def test_list_of_patterns():
    assert list_of_patterns


@pytest.mark.parametrize(
    ["pattern"],
    [list_of_patterns()],
)
def test_load_pattern(pattern: str):
    assert load_pattern(pattern)[0]
