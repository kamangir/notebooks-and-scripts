import argparse
from abcli.plugins import aws
from notebooks_and_scripts import VERSION
from abcli import logging
import logging

logger = logging.getLogger(__name__)

NAME = "notebooks_and_scripts.aws_batch"

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="submit",
)
parser.add_argument(
    "--command_line",
    type=str,
    default="",
)
parser.add_argument(
    "--vcpus",
    type=int,
    default=8,
)
parser.add_argument(
    "--job_name",
    type=str,
    default="",
)
parser.add_argument(
    "--memory",
    type=int,
    default=32000,
)
parser.add_argument(
    "--retries",
    type=int,
    default=3,
)
args = parser.parse_args()

success = False
if args.task == "submit":
    # https://unix.stackexchange.com/questions/243571/how-to-run-source-with-docker-exec/243580#243580
    command = [
        "bash",
        "-c",
        f"source /root/git/awesome-bash-cli/bash/abcli.sh install,minimal,aws_batch abcli_scripts source {args.command_line}",
    ]
    logger.info("{}.submit -> {}: {}".format(NAME, args.job_name, " ".join(command)))

    # request = BatchRequest(
    #    command=command,
    #    vcpus=args.vcpus,
    #    mem=args.memory,
    #    retries=args.retries,
    #    job_name=args.job_name,
    # )
    # request.image = "image-name"
    # job_id = request.submit_job_request()

    job_id = None

    aws_region = aws.get_from_json("region", "")
    logger.info(f"job_id: {job_id}")
    logger.info(
        "https://{}.console.aws.amazon.com/batch/home?region={}#jobs/detail/{}".format(
            aws_region,
            aws_region,
            job_id,
        )
    )
    success = True
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
