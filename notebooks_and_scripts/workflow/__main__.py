import argparse
from notebooks_and_scripts import env
from notebooks_and_scripts.aws_batch import VERSION, NAME
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.workflow.classes import Workflow
from notebooks_and_scripts.workflow.runner import Runner
from notebooks_and_scripts.logger import logger


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="create|monitor|submit",
)
parser.add_argument(
    "--command_line",
    type=str,
    default=env.ABCLI_AWS_BATCH_DEFAULT_WORKFLOW_COMMAND_UQ,
)
parser.add_argument(
    "--job_name",
    type=str,
    default="",
)
parser.add_argument(
    "--runner",
    type=str,
    default="LOCAL",
    help="|".join([str(runner) for runner in list(Runner)]),
)
parser.add_argument(
    "--pattern",
    type=str,
    default=list_of_patterns()[0],
    help="|".join(list_of_patterns()),
)
parser.add_argument(
    "--verbose",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--dryrun",
    type=int,
    default=1,
    help="0|1",
)
args = parser.parse_args()


success = False
if args.task == "create":
    workflow = Workflow(
        job_name=args.job_name,
        verbose=args.verbose == 1,
    )

    success = workflow.load_pattern(
        command_line=args.command_line,
        pattern=args.pattern,
    )

    if success:
        success = workflow.submit(
            runner=Runner[args.runner.upper()],
            dryrun=args.dryrun == 1,
        )
elif args.task == "monitor":
    success = Workflow.monitor(
        job_name=args.job_name,
        runner=Runner[args.runner.upper()],
    )
elif args.task == "submit":
    workflow = Workflow(
        job_name=args.job_name,
        load=True,
        verbose=args.verbose == 1,
    )

    success = workflow.submit(
        runner=Runner[args.runner.upper()],
        dryrun=args.dryrun == 1,
    )
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
