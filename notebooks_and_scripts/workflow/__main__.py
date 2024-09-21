import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from notebooks_and_scripts import NAME
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.logger import logger


NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
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
parser.add_argument(
    "--publish_as",
    type=str,
    default="",
    help="<public-object-name>",
)
args = parser.parse_args()


success = False
if args.task == "create":
    workflow = Workflow(job_name=args.job_name)

    success = workflow.load_pattern(
        pattern=args.pattern,
        publish_as=args.publish_as,
    )

    if success:
        success = workflow.save()
else:
    success = None

sys_exit(logger, NAME, args.task, success)
