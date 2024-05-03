import argparse
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow import VERSION, NAME
from notebooks_and_scripts.workflow.runners.factory import runner_class
from notebooks_and_scripts.logger import logger

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="list|monitor|submit",
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
parser.add_argument(
    "--runner_type",
    type=str,
    default="local",
    help="|".join([type.name.lower() for type in RunnerType]),
)
parser.add_argument(
    "--dryrun",
    type=int,
    default=0,
    help="0|1",
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
elif args.task == "monitor":
    workflow = Workflow(
        job_name=args.job_name,
        load=True,
    )

    runner = runner_class[workflow.runner_type]

    success = runner.monitor(workflow)

    if success:
        success = workflow.save()
elif args.task == "submit":
    workflow = Workflow(
        job_name=args.job_name,
        load=True,
    )

    runner = runner_class[RunnerType[args.runner_type.upper()]]

    success = runner.submit(
        workflow,
        dryrun=args.dryrun == 1,
    )

    if success:
        success = workflow.save()
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
