from abcli.tests import test_env
from notebooks_and_scripts import env


def test_abcli_env():
    test_env.test_abcli_env()


def test_notebooks_and_scripts_env():
    assert env.LOCALFLOW_STATUS_LIST
    assert env.ABCLI_AWS_BATCH_JOB_STATUS_LIST

    assert env.ABCLI_AWS_BATCH_DEFAULT_WORKFLOW_COMMAND
    assert env.ABCLI_AWS_BATCH_DEFAULT_WORKFLOW_COMMAND_UQ

    assert env.ABCLI_AWS_BATCH_DEFAULT_WORKFLOW_PATTERN
