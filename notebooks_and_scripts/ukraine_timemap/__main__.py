import argparse
from notebooks_and_scripts import VERSION
from notebooks_and_scripts.ukraine_timemap import NAME
from notebooks_and_scripts.ukraine_timemap.functions import ingest
from notebooks_and_scripts.logger import logger

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="ingest",
)
parser.add_argument(
    "--object_name",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "ingest":
    success, _ = ingest(object_name=args.object_name)
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
