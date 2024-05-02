from typing import Tuple
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.runners.aws_batch import AWSBatchRunner
from notebooks_and_scripts.workflow.runners.generic import Runner
from notebooks_and_scripts.logger import logger


def create(type: RunnerType) -> Tuple[bool, Runner]:
    if type == RunnerType.AWS_BATCH:
        return True, AWSBatchRunner()

    return False, Runner()
