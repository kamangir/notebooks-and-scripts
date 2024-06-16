import argparse
from notebooks_and_scripts import env
from notebooks_and_scripts.aws_batch import VERSION, NAME
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.logger import logger
from blueness.argparse.generic import sys_exit


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="create",
)
parser.add_argument(
    "--job_name",
    type=str,
    default="",
)
parser.add_argument(
    "--pattern",
    type=str,
    default=list_of_patterns()[0],
    help="|".join(list_of_patterns()),
)
args = parser.parse_args()


success = False
if args.task == "create":
    workflow = Workflow(job_name=args.job_name)

    success = workflow.load_pattern(pattern=args.pattern)

    if success:
        success = workflow.save()
else:
    success = None

sys_exit(logger, NAME, args.task, success)
