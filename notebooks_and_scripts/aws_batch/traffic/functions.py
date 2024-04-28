from notebooks_and_scripts.aws_batch.traffic import NAME
from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.aws_batch.traffic.patterns import load_pattern
from abcli.plugins.metadata import post, MetadataSourceType
from abcli.modules import objects


def create(
    command_line: str,
    pattern: str,
    job_name="",
    verbose: bool = False,
) -> bool:
    logger.info(
        "creating traffic: {} x {} -> {}-*".format(
            pattern,
            command_line,
            job_name,
        )
    )

    success, graph = load_pattern(
        pattern=pattern,
        export_as_image=objects.path_of(f"{pattern}.png", job_name),
    )
    if not success:
        return success

    logger.info("🪄")

    return post(
        NAME,
        {
            "command_line": command_line,
            "graph": str(graph),
            "pattern": pattern,
        },
        source=job_name,
        source_type=MetadataSourceType.OBJECT,
        verbose=verbose,
    )
