from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.runners.generic import GenericRunner


class LocalRunner(GenericRunner):
    def __init__(self, **kw_args):
        super().__init__(**kw_args)
        self.runner: RunnerType = RunnerType.LOCAL

    def monitor(
        self,
        workflow: Workflow,
    ) -> bool:
        assert super().monitor(workflow)

        return True

    def submit(
        self,
        workflow: Workflow,
        dryrun: bool = True,
    ) -> bool:
        assert super().submit(workflow, dryrun)

        return True