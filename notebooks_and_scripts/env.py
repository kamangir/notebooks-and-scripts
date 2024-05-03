import os
import urllib.parse
from abcli.env import load_env, load_config

load_env(__name__)
load_config(__name__)

LOCALFLOW_STATUS_LIST = os.getenv("LOCALFLOW_STATUS_LIST", "")

ABCLI_AWS_BATCH_JOB_STATUS_LIST = os.getenv("ABCLI_AWS_BATCH_JOB_STATUS_LIST", "")

NBS_DEFAULT_WORKFLOW_COMMAND = os.getenv("NBS_DEFAULT_WORKFLOW_COMMAND", "")
NBS_DEFAULT_WORKFLOW_COMMAND_UQ = urllib.parse.unquote(NBS_DEFAULT_WORKFLOW_COMMAND)

NBS_DEFAULT_WORKFLOW_PATTERN = os.getenv("NBS_DEFAULT_WORKFLOW_PATTERN", "")
