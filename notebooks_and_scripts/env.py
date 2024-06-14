import os
import urllib.parse
from abcli.env import load_env, load_config

load_env(__name__)
load_config(__name__)

LOCALFLOW_STATUS_LIST = os.getenv("LOCALFLOW_STATUS_LIST", "")

ABCLI_AWS_BATCH_JOB_STATUS_LIST = os.getenv("ABCLI_AWS_BATCH_JOB_STATUS_LIST", "")
ABCLI_AWS_BATCH_JOB_STATUS_LIST_WATCH = os.getenv(
    "ABCLI_AWS_BATCH_JOB_STATUS_LIST_WATCH", ""
)

NBS_DEFAULT_WORKFLOW_PATTERN = os.getenv("NBS_DEFAULT_WORKFLOW_PATTERN", "")

UKRAINE_TIMEMAP_TEMPLATE = os.getenv("UKRAINE_TIMEMAP_TEMPLATE", "")
