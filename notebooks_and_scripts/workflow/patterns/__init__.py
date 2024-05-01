from typing import Tuple, List
import os
import glob
import networkx as nx
from abcli import file
from notebooks_and_scripts.workflow.dot_file import load_from_file as load_dot_file


def list_of_patterns() -> List[str]:
    return [
        file.name(filename)
        for filename in glob.glob(
            os.path.join(
                file.path(__file__),
                "*.dot",
            )
        )
    ]


def load_pattern(
    pattern: str,
    **kw_args,
) -> Tuple[bool, nx.DiGraph]:
    return load_dot_file(
        filename=os.path.join(file.path(__file__), f"{pattern}.dot"),
        **kw_args,
    )
