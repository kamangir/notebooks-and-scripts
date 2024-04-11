import sys
import argparse
import boto3
from abcli import env
from notebooks_and_scripts import VERSION, NAME
from notebooks_and_scripts.logger import logger

NAME = f"{NAME}.aws_batch"

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
    # https://unix.stackexchange.com/questions/243571/how-to-run-source-with-docker-exec/243580#243580
    command = [
        "bash",
        "-c",
        "source /root/git/awesome-bash-cli/bash/abcli.sh mono,install,aws_batch {} {}".format(
            "abcli_eval" if args.type == "eval" else "abcli_scripts source",
            args.command_line,
        ),
    ]
    logger.info(
        "{} -> {}: {}".format(
            args.task,
            args.job_name,
            "\n".join(command),
        )
    )

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html
    client = boto3.client("batch")

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/submit_job.html
    response = client.submit_job(
        jobName=args.job_name,
        jobQueue="abcli-v3",
        jobDefinition="abcli-custom-v1",
        containerOverrides={
            "command": command,
        },
    )
    logger.info(f"response: {response}")

    job_id = response["jobId"]
    logger.info(f"job_id: {job_id}")

    logger.info(
        "https://{}.console.aws.amazon.com/batch/home?region={}#jobs/detail/{}".format(
            env.abcli_aws_region,
            env.abcli_aws_region,
            job_id,
        )
    )
    success = True
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
