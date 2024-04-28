from notebooks_and_scripts.logger import logger


def create(
    command_line: str,
    pattern: str = 5,
    job_name="",
) -> bool:
    logger.info(
        "creating traffic: {} x {} -> {}-*".format(
            pattern,
            command_line,
            job_name,
        )
    )

    logger.info("🪄")

    return True
