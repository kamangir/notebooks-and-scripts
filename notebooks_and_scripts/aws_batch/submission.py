from enum import Enum
import boto3
from abcli import env
from notebooks_and_scripts.logger import logger


class SubmissionType(Enum):
    EVAL = "eval"
    SOURCE = "source"
    SUBMIT = "submit"

    @property
    def runner(self):
        return "abcli_eval" if self == SubmissionType.EVAL else "abcli_scripts source"


def submit(
    command_line: str,
    job_name: str,
    type: SubmissionType,
) -> bool:
    # https://unix.stackexchange.com/questions/243571/how-to-run-source-with-docker-exec/243580#243580
    command = [
        "bash",
        "-c",
        "source /root/git/awesome-bash-cli/bash/abcli.sh mono,install,aws_batch {} {}".format(
            type.runner,
            command_line,
        ),
    ]
    logger.info(
        "{} -> {}: {}".format(
            type.name,
            job_name,
            "\n".join(command),
        )
    )

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html
    client = boto3.client("batch")

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/submit_job.html
    response = client.submit_job(
        jobName=job_name,
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

    return True
