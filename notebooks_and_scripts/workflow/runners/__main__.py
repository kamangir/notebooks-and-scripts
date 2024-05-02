import argparse
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow import VERSION, NAME
from notebooks_and_scripts.logger import logger

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="list",
)
parser.add_argument(
    "--delim",
    type=str,
    default="+",
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
)
parser.add_argument(
    "--offset",
    type=int,
    default=0,
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = False
if args.task == "list":
    success = True

    output = sorted([type.name.lower() for type in RunnerType])[args.offset :]

    if args.count != -1:
        output = output[: args.count]

    print(delim.join(output))
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
