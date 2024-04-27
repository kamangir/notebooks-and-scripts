import sys
import argparse
from notebooks_and_scripts.env import env
from notebooks_and_scripts.aws_batch import VERSION, NAME
from notebooks_and_scripts.aws_batch.submission import (
    submit,
    SubmissionType,
)
from notebooks_and_scripts.aws_batch.traffic import create as create_traffic
from notebooks_and_scripts.logger import logger


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="create_traffic|show_count|submit",
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
    default=env.ABCLI_AWS_BATCH_TRAFFIC_PATTERN_EXAMPLE_SIMPLE,
    help=f"harder example: {env.ABCLI_AWS_BATCH_TRAFFIC_PATTERN_EXAMPLE_HARD}",
)
parser.add_argument(
    "--depth",
    type=int,
    default=5,
)
args = parser.parse_args()

success = False
if args.task == "create_traffic":
    success = create_traffic(
        breadth=args.breadth,
        command_line=args.command_line,
        depth=args.depth,
        job_name=args.job_name,
    )
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
