from typing import Dict

from blueflow.workflow.runners import RunnerType
from blueflow.workflow.runners.aws_batch import AWSBatchRunner
from blueflow.workflow.runners.local import LocalRunner
from blueflow.workflow.runners.generic import GenericRunner

runner_class: Dict[RunnerType, GenericRunner] = {
    RunnerType.AWS_BATCH: AWSBatchRunner,
    RunnerType.GENERIC: GenericRunner,
    RunnerType.LOCAL: LocalRunner,
}
