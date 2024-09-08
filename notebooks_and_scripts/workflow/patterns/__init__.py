from typing import Tuple, List
import os
import glob
import networkx as nx

from blue_objects import file

from notebooks_and_scripts.workflow import dot_file


def list_of_patterns() -> List[str]:
    return sorted(
        [
            file.name(filename)
            for filename in glob.glob(
                os.path.join(
                    file.path(__file__),
                    "*.dot",
                )
            )
        ]
    )


def load_pattern(
    pattern: str,
    **kw_args,
) -> Tuple[bool, nx.DiGraph]:
    return dot_file.load_from_file(
        filename=os.path.join(file.path(__file__), f"{pattern}.dot"),
        **kw_args,
    )
