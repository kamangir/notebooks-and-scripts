from notebooks_and_scripts.logger import logger
from notebooks_and_scripts.workflow.runners import RunnerType


class Runner:
    def __init__(self):
        self.type: RunnerType = RunnerType.PENDING

    def monitor(self, job_name: str) -> bool:
        return False

    def submit(self, dryrun: bool = True) -> bool:
        return False
