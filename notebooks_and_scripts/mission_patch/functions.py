from abcli import logging
import logging

logger = logging.getLogger(__name__)


def generate_mission_patches(
    url: str,
    object_name: str,
    count: int,
    height: int = 1024,
    width: int = 1024,
    verbose: bool = False,
):
    logger.info(
        "{} -> {}: {}x{}x{}".format(
            url,
            object_name,
            count,
            height,
            width,
        )
    )
    return True
