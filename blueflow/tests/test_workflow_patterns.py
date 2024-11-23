import pytest
import networkx as nx

from blueflow.workflow.patterns import (
    load_pattern,
    list_of_patterns,
)


def test_list_of_patterns():
    assert list_of_patterns()


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
def test_load_pattern(pattern: str):
    success, G = load_pattern(pattern)
    assert success
    assert isinstance(G, nx.DiGraph)
