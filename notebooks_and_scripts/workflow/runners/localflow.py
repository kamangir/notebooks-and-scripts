from notebooks_and_scripts.workflow.generic import Workflow
from notebooks_and_scripts.workflow.runners import RunnerType
from notebooks_and_scripts.workflow.runners.generic import GenericRunner


class LocalFlowRunner(GenericRunner):
    def __init__(self, **kw_args):
        super().__init__(**kw_args)
        self.type: RunnerType = RunnerType.LOCALFLOW

    def monitor(
        self,
        workflow: Workflow,
        hot_node: str = "void",
    ) -> bool:
        assert super().monitor(workflow, hot_node)

        return True

    def submit(
        self,
        workflow: Workflow,
        dryrun: bool = True,
    ) -> bool:
        assert super().submit(workflow, dryrun)

        return True
