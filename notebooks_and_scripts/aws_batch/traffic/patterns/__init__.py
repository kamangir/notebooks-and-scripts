from typing import Tuple, List
import os
import glob
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import read_dot
from abcli import file, path
from abcli.logger import crash_report
from notebooks_and_scripts.aws_batch import NAME, VERSION
from notebooks_and_scripts.logger import logger

layouts = {
    "spring": nx.spring_layout,
    "circular": nx.circular_layout,
    "random": nx.random_layout,
    "shell": nx.shell_layout,
    "kamada_kawai": nx.kamada_kawai_layout,
    "spectral": nx.spectral_layout,
    "planar": nx.planar_layout,
    "fruchterman_reingold": nx.fruchterman_reingold_layout,
    "spiral": nx.spiral_layout,
}


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


def load_from_file(
    filename: str,
    log: bool = True,
    export_as_image: str = "",
    layout: str = "shell",
    figsize: int = 5,
) -> Tuple[bool, nx.DiGraph]:
    graph = nx.DiGraph()

    try:
        graph = read_dot(filename)
    except:
        crash_report(f"-{NAME}: traffic: load_from_file({filename}): failed.")
        return

    if log:
        logger.info(
            "loaded a {}[{} node(s) X {} edge(s)] from {}.".format(
                graph.__class__.__name__,
                graph.number_of_nodes(),
                graph.number_of_edges(),
                filename,
            )
        )

    if not export_as_image:
        return True, graph

    layout_func = layouts.get(layout, None)
    assert layout_func is not None

    pos = layout_func(graph)

    plt.figure(figsize=(figsize, figsize))
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color="lightblue",
        edge_color="gray",
        node_size=500,
        font_size=10,
        font_color="darkred",
    )
    plt.title(
        " | ".join(
            [
                path.name(file.path(filename)),
                file.name(filename),
                f"{graph.number_of_nodes()} node(s)",
                f"{graph.number_of_edges()} edge(s)",
                f"layout: {layout}",
            ]
        )
    )
    file.save_fig(export_as_image, log=log)

    return True, graph


def load_pattern(
    pattern: str,
    **kw_args,
) -> Tuple[bool, nx.DiGraph]:
    return load_from_file(
        filename=os.path.join(file.path(__file__), f"{pattern}.dot"),
        **kw_args,
    )
