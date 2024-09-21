import sys
import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from blue_objects import file

from notebooks_and_scripts import NAME
from notebooks_and_scripts.aws_batch.submission import (
    submit,
    SubmissionType,
)
from notebooks_and_scripts.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="cat_log|get_log_stream_name|show_count|submit",
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
    "--filename",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "cat_log":
    success, content = file.load_json(args.filename, ignore_error=True)

    if success:
        count = 0
        for line in content.get("events", []):
            print(line.get("message", ""))
            count = count + 1

        print(f"📜 {count} line(s).")
elif args.task == "get_log_stream_name":
    success, metadata = file.load_json(args.filename)
    if success:
        print(
            metadata["jobs"][0].get("container", {}).get("logStreamName", "")
            if metadata["jobs"]
            else ""
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
    success, _ = submit(
        command_line=args.command_line,
        job_name=args.job_name,
        type=SubmissionType[args.type.upper()],
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
