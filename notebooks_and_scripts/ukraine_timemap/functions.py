from abcli import file
from abcli.modules import objects
from notebooks_and_scripts.ukraine_timemap import NAME
from notebooks_and_scripts.logger import logger

api_url = "https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json"


def ingest(
    object_name: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.ingest -> {object_name}")
    filename = objects.path_of("api.json", object_name)

    success = file.download(api_url, filename)
    if not success:
        return success

    success, items = file.load_json(filename)
    if not success:
        return success
    logger.info("{:,} item(s) downloaded.".format(len(items)))

    logger.info("🪄")

    return True
