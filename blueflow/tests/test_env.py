from abcli.tests.test_env import test_abcli_env
from blue_objects.tests.test_env import test_blue_objects_env

from blueflow import env


def test_required_env():
    test_abcli_env()
    test_blue_objects_env()


def test_blueflow_env():
    assert env.ABCLI_AWS_BATCH_JOB_STATUS_LIST_WATCH

    assert env.NBS_DEFAULT_WORKFLOW_PATTERN
