import argparse
from notebooks_and_scripts import VERSION
from notebooks_and_scripts.sagesemseg.dataset import upload as upload_dataset
from abcli import logging
import logging

logger = logging.getLogger(__name__)

NAME = "notebooks_and_scripts.sagesemseg"

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="upload_dataset",
)
parser.add_argument(
    "--dataset_object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
)
args = parser.parse_args()

success = False
if args.task == "upload_dataset":
    success = upload_dataset(
        dataset_object_name=args.dataset_object_name,
        object_name=args.object_name,
        count=args.count,
    )
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
