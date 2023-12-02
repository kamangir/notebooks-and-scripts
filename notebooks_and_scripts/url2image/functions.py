from tqdm import trange
from typing import List, Tuple
from abcli import logging
import logging

logger = logging.getLogger(__name__)


def read_url(
    url: str,
    verbose: bool = False,
) -> Tuple[bool, str]:
    description = ""

    logger.info("url2image.read_url({}): {}".format(url, description))
    return True, description


def render_url(
    url: str,
    object_name: str,
    count: int,
    height: int = 1024,
    width: int = 1024,
    verbose: bool = False,
) -> bool:
    logger.info(
        "url2image.render_url: {} -> {}: {}x{}x{}".format(
            url, object_name, count, height, width
        )
    )

    success, description = read_url(url, verbose)
    if not success:
        return False

    prompt = "Generate a mission patch for the launch of the constellation described as follows. {}".format(
        description
    )
    logger.info(f"prompt: {prompt}")

    error_count = 0
    for index in trange(count):
        if not render_prompt(
            prompt=prompt,
            object_name=object_name,
            filename="{:05d}.png".format(index),
            height=height,
            width=width,
            verbose=verbose,
        ):
            error_count += 1

    if error_count:
        logger.error(f"{error_count} error(s)")

    return True


def render_prompt(
    prompt: str,
    object_name: str,
    filename: str = "output.png",
    height: int = 1024,
    width: int = 1024,
    verbose: bool = False,
) -> bool:
    logger.info(
        "url2image.render_prompt({} -> {}/{} : {}x{}".format(
            prompt, object_name, filename, height, width
        )
    )

    return True
