import sys
import argparse
from notebooks_and_scripts import env
from notebooks_and_scripts.aws_batch import VERSION, NAME
from notebooks_and_scripts.aws_batch.submission import (
    submit,
    SubmissionType,
)
from notebooks_and_scripts.logger import logger
from blueness.argparse.generic import sys_exit


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="show_count|submit",
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
args = parser.parse_args()

success = False
if args.task == "show_count":
    success = True
    input_string = sys.stdin.read().strip()

    if not input_string.isdigit():
        print(input_string)
    else:
        input_int = int(input_string)
        if input_int:
            print("{} {}".format(input_int, input_int * "🌀"))
elif args.task == "submit":
    success, _ = submit(
        command_line=args.command_line,
        job_name=args.job_name,
        type=SubmissionType[args.type.upper()],
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
