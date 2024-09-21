import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from notebooks_and_scripts import NAME
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
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

    output = list_of_patterns()[args.offset :]

    if args.count != -1:
        output = output[: args.count]

    print(delim.join(output))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
