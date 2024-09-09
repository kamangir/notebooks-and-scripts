import copy
import textwrap
from typing import Tuple, Dict, List
import numpy as np
import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import read_dot

from blueness import module
from blue_options.logger import crash_report
from blue_options.host import signature as host_signature
from blue_objects import file, path

from notebooks_and_scripts import NAME, VERSION
from notebooks_and_scripts.logger import logger

NAME = module.name(__file__, NAME)


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
    add_legend: bool = True,
    caption: str = "",
    text_width: int = 80,
) -> bool:
    layout_func = layouts.get(layout, None)
    if layout_func is None:
        logger.error(f"unknown layout: {layout}")
        return False

    if add_legend:
        G = copy.deepcopy(G)
        for status in status_color_map:
            G.add_node(status)
            G.nodes[status]["status"] = status

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

    caption_items: List[str] = [caption]
    if hot_node in G.nodes:
        caption_items += [G.nodes[hot_node].get("command_line").replace('"', "")]
    caption_items = [item for item in caption_items if item]

    caption_wrapped = textwrap.fill(
        " | ".join(caption_items),
        width=text_width,
    )

    if caption_items:
        plt.text(
            0.5,
            0.5,
            caption_wrapped,
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
                file.add_extension(filename, export_as_image[1:])
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
) -> bool:
    if not file.prepare_for_saving(filename):
        return False

    try:
        write_dot(G, filename)
    except:
        crash_report(f"save_to_file({filename}) failed.")
        return False

    if log:
        logger.info(f"{G} -> {filename}")

    if not export_as_image:
        return True

    return export_graph_as_image(
        G,
        filename=(
            file.add_extension(filename, export_as_image[1:])
            if export_as_image.startswith(".")
            else export_as_image
        ),
        log=log,
        **kwargs,
    )
