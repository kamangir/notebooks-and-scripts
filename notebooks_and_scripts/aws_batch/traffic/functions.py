from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.aws_batch.traffic.patterns import load_pattern


def create(
    command_line: str,
    pattern: str,
    job_name="",
) -> bool:
    logger.info(
        "creating traffic: {} x {} -> {}-*".format(
            pattern,
            command_line,
            job_name,
        )
    )

    success, graph = load_pattern(pattern)
    if not success:
        return success

    logger.info(f"🪄: {graph}")

    return True
