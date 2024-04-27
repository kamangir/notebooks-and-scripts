from notebooks_and_scripts.logger import logger


def create(
    command_line: str,
    breadth: int = 5,
    depth: int = 5,
    job_name="",
) -> bool:
    logger.info(
        "creating traffic: {} x {} @ {}-*".format(
            "{"
            + breadth * "j"
            + "} -> "
            + " -> ".join((depth - 2) * ["j"])
            + "-> {"
            + breadth * "j"
            + "}",
            command_line,
            job_name,
        )
    )

    logger.info("🪄")

    return False
