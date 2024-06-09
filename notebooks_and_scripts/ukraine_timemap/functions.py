from notebooks_and_scripts.ukraine_timemap import NAME
from notebooks_and_scripts.logger import logger


def ingest(
    object_name: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.ingest -> {object_name}")

    logger.info("🪄")

    return True
