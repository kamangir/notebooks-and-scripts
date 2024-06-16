import argparse
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow import VERSION, NAME
from notebooks_and_scripts.workflow.runners.factory import runner_class
from notebooks_and_scripts.logger import logger
from blueness.argparse.generic import sys_exit

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="list|monitor|submit",
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
)
parser.add_argument(
    "--delim",
    type=str,
    default="+",
)

parser.add_argument(
    "--dryrun",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--job_name",
    type=str,
    default="",
)
parser.add_argument(
    "--hot_node",
    type=str,
    default="void",
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

    runner = runner_class[RunnerType[workflow.runner_type.upper()]]()

    success = runner.monitor(workflow, args.hot_node)

    if success:
        success = workflow.save()
elif args.task == "submit":
    workflow = Workflow(
        job_name=args.job_name,
        load=True,
    )

    runner = runner_class[RunnerType[args.runner_type.upper()]]()

    success = runner.submit(
        workflow,
        dryrun=args.dryrun == 1,
    )

    if success:
        success = workflow.save()
else:
    success = None

sys_exit(logger, NAME, args.task, success)
