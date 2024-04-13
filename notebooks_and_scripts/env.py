import os
from dotenv import load_dotenv

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(parent_dir, ".env"))
load_dotenv(os.path.join(parent_dir, "config.env"))


LOCALFLOW_STATUS_LIST = os.getenv("LOCALFLOW_STATUS_LIST", "")
