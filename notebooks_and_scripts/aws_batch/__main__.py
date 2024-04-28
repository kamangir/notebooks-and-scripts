import sys
import argparse
from notebooks_and_scripts import env
from notebooks_and_scripts.aws_batch import VERSION, NAME
from notebooks_and_scripts.aws_batch.submission import (
    submit,
    SubmissionType,
)
from notebooks_and_scripts.aws_batch.traffic.patterns import list_of_patterns
from notebooks_and_scripts.aws_batch.traffic.functions import create as create_traffic
from notebooks_and_scripts.logger import logger


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="create_traffic|list_of_patterns|show_count|submit",
)
parser.add_argument(
    "--command_line",
    type=str,
    default="",
)
parser.add_argument(
    "--job_name",
    type=str,
    default="",
)
parser.add_argument(
    "--type",
    type=str,
    default="source",
    help="eval|source|submit",
)
parser.add_argument(
    "--pattern",
    type=str,
    default=list_of_patterns()[0],
    help="|".join(list_of_patterns()),
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
if args.task == "create_traffic":
    success = create_traffic(
        command_line=args.command_line,
        pattern=args.pattern,
        job_name=args.job_name,
    )
elif args.task == "list_of_patterns":
    success = True

    output = list_of_patterns()[args.offset :]

    if args.count != -1:
        output = output[: args.count]

    print(delim.join(output))
elif args.task == "show_count":
    success = True
    input_string = sys.stdin.read().strip()

    if not input_string.isdigit():
        print(input_string)
    else:
        input_int = int(input_string)
        if input_int:
            print("{} {}".format(input_int, input_int * "🌀"))
elif args.task == "submit":
    success = submit(
        command_line=args.command_line,
        job_name=args.job_name,
        type=SubmissionType[args.type.upper()],
    )
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
