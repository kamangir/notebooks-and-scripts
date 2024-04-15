from abcli.tests import test_env
from notebooks_and_scripts import env
import pkg_resources


def test_abcli_env():
    test_env.test_abcli_env()


def test_notebooks_and_scripts_env():
    assert env.LOCALFLOW_STATUS_LIST, pkg_resources.resource_listdir(
        "notebooks_and_scripts", ""
    )
