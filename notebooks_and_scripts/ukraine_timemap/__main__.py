import argparse
from notebooks_and_scripts import VERSION
from notebooks_and_scripts.ukraine_timemap import NAME
from notebooks_and_scripts.ukraine_timemap.functions import ingest
from notebooks_and_scripts.logger import logger
from blueness.argparse.generic import ending

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
    success = None

ending(logger, NAME, args.task, success)
