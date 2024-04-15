import os
from abcli.env import load_env, load_config

load_env(__name__)
load_config(__name__)


LOCALFLOW_STATUS_LIST = os.getenv("LOCALFLOW_STATUS_LIST", "")
