import argparse
from notebooks_and_scripts import env
from notebooks_and_scripts.aws_batch import VERSION, NAME
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.logger import logger


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="create",
)
parser.add_argument(
    "--command_line",
    type=str,
    default=env.NBS_DEFAULT_WORKFLOW_COMMAND_UQ,
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

    success = workflow.load_pattern(
        command_line=args.command_line,
        pattern=args.pattern,
    )

    if success:
        success = workflow.save()
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
