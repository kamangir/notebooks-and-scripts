from bs4 import BeautifulSoup
import requests
from tqdm import trange
from typing import List, Tuple
from abcli import logging
import logging

logger = logging.getLogger(__name__)


def read_url(
    url: str,
    verbose: bool = False,
) -> Tuple[bool, str]:
    # https://www.zenrows.com/blog/403-web-scraping#set-fake-user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)
    logger.info(f"response: {response}")

    # https://chat.openai.com/c/6deb94d0-826a-48de-b5ef-f7d8da416c82
    # response.raise_for_status()
    if response.status_code // 100 != 2:  # Check if status code is not in the 2xx range
        logger.info(
            "read_url({}) failed, status_code: {}, reason: {}.".format(
                url,
                response.status_code,
                response.reason,
            )
        )
        return False, ""

    # Check if the content type is text-based (e.g., HTML, plain text)
    if "text" not in response.headers.get("content-type", "").lower():
        logger.error(f"read_url({read_url}): url does not contain text-based content.")
        return False, ""

    soup = BeautifulSoup(response.text, "html.parser")
    description = " ".join([p.get_text() for p in soup.find_all("p")])

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
