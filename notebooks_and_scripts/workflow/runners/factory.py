from typing import Dict
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.runners.aws_batch import AWSBatchRunner
from notebooks_and_scripts.workflow.runners.local import LocalRunner
from notebooks_and_scripts.workflow.runners.localflow import LocalFlowRunner
from notebooks_and_scripts.workflow.runners.generic import GenericRunner

runner_class: Dict[RunnerType, GenericRunner] = {
    RunnerType.AWS_BATCH: AWSBatchRunner,
    RunnerType.GENERIC: GenericRunner,
    RunnerType.LOCAL: LocalRunner,
    RunnerType.LOCALFLOW: LocalFlowRunner,
}
