from typing import Tuple, Dict
import numpy as np
import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import read_dot
from abcli import file, path
from abcli.modules.host import signature as host_signature
from abcli.logger import crash_report
from notebooks_and_scripts.workflow import NAME, VERSION
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

status_color_map = {
    "SUBMITTED": "yellow",
    "PENDING": "orange",
    "RUNNABLE": "purple",
    "STARTING": "cyan",
    "RUNNING": "blue",
    "SUCCEEDED": "green",
    "FAILED": "black",
}


def export_graph_as_image(
    G: nx.DiGraph,
    filename: str,
    layout: str = "shell",
    figsize: int = 5,
    log: bool = True,
    colormap: Dict[str, str] = {},
    hot_node: str = "void",
) -> bool:
    layout_func = layouts.get(layout, None)
    if layout_func is None:
        logger.error(f"unknown layout: {layout}")
        return False

    pos = layout_func(G)

    node_color = [
        (
            "red"
            if node == hot_node
            else colormap.get(
                G.nodes[node].get("status"),
                "gray",
            )
        )
        for node in G
    ]

    plt.figure(figsize=(figsize, figsize))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_color,
        edge_color="gray",
        node_size=500,
        font_size=10,
        font_color="darkred",
        # arrowstyle="-|>",
        # arrowsize=5,
    )

    if hot_node in G.nodes:
        plt.text(
            0.5,
            0.5,
            G.nodes[hot_node].get("command_line").replace('"', ""),
            horizontalalignment="center",
            verticalalignment="center",
            transform=plt.gca().transAxes,
            fontsize=12,
            color="green",
        )
    plt.title(
        " | ".join(
            [
                path.name(file.path(filename)),
                file.name(filename),
                f"{G.number_of_nodes()} node(s)",
                f"{G.number_of_edges()} edge(s)",
                f"layout: {layout}",
                f"@{hot_node}",
            ]
        ),
        fontsize=10,
    )
    plt.figtext(
        0.5,
        0.01,
        "\n".join(
            [
                " | ".join(item)
                for item in np.array_split(
                    [f"{NAME}-{VERSION}"] + host_signature(),
                    3,
                )
            ]
        ),
        ha="center",
        fontsize=10,
        color="black",
    )
    return file.save_fig(filename, log=log)


def load_from_file(
    filename: str,
    export_as_image: str = "",
    log: bool = True,
    **kwargs,
) -> Tuple[bool, nx.DiGraph]:
    G = nx.DiGraph()

    try:
        G = read_dot(filename)
    except:
        crash_report(f"-{NAME}: load_from_file({filename}): failed.")
        return False, G

    if log:
        logger.info(f"loaded {G} from {filename}.")

    return (
        not export_as_image
        or export_graph_as_image(
            G,
            filename=(
                file.set_extension(filename, export_as_image[1:])
                if export_as_image.startswith(".")
                else export_as_image
            ),
            log=log,
            **kwargs,
        )
    ), G


def save_to_file(
    filename: str,
    G: nx.DiGraph,
    export_as_image: str = ".png",
    log: bool = True,
    **kwargs,
):
    if not file.prepare_for_saving(filename):
        return False

    try:
        write_dot(G, filename)
    except:
        crash_report(f"save_to_file({filename}) failed.")
        return False

    if log:
        logger.info(f"{G} -> {filename}")

    return (
        not export_as_image
        or export_graph_as_image(
            G,
            filename=(
                file.set_extension(filename, export_as_image[1:])
                if export_as_image.startswith(".")
                else export_as_image
            ),
            log=log,
            **kwargs,
        )
    ), G
