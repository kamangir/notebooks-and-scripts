import pytest
from notebooks_and_scripts.workflow.patterns import (
    load_pattern,
    list_of_patterns,
)


def test_list_of_patterns():
    assert list_of_patterns


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
def test_load_pattern(pattern: str):
    assert load_pattern(pattern)[0]
