from typing import Dict
import boto3
import glob
from tqdm import tqdm
from abcli import string
from abcli.modules import objects
from abcli.plugins.graphics.gif import generate_animated_gif
from abcli.plugins.metadata import get, MetadataSourceType
from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.aws_batch.dot_file import (
    load_from_file,
    export_graph_as_image,
    status_color_map,
)


def monitor_traffic(
    job_name: str,
) -> bool:
    pattern = get(
        "traffic.pattern",
        "",
        job_name,
        MetadataSourceType.OBJECT,
    )

    success, G = load_from_file(objects.path_of(f"{pattern}.dot", job_name))
    if not success:
        return success

    logger.info(f"monitor_traffic: {job_name} @ {pattern}: {G}")

    client = boto3.client("batch")

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_jobs.html
    page_size = 100
    summary: Dict[str, str] = {}
    for index in tqdm(range(0, len(G.nodes), page_size)):
        nodes = list(G.nodes)[index : index + page_size]

        jobs = [G.nodes[node].get("job_id").replace('"', "") for node in nodes]

        response = client.describe_jobs(jobs=jobs)

        for node, status in zip(
            nodes,
            [item["status"] for item in response["jobs"]],
        ):
            G.nodes[node]["status"] = status

            summary.setdefault(status, []).append(node)

    for status, nodes in summary.items():
        logger.info("{}: {}".format(status, ", ".join(sorted(nodes))))

    if not export_graph_as_image(
        G,
        objects.path_of(
            "{}-{}.png".format(
                pattern,
                string.pretty_date(as_filename=True, unique=True),
            ),
            job_name,
        ),
        colormap=status_color_map,
    ):
        return False

    return generate_animated_gif(
        glob.glob(objects.path_of(f"{pattern}-*.png", job_name)),
        objects.path_of(f"{pattern}.gif", job_name),
        frame_duration=333,
    )
