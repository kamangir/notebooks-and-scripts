import argparse
from notebooks_and_scripts import NAME, VERSION, DESCRIPTION, ICON
from notebooks_and_scripts.logger import logger

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="version",
)
parser.add_argument(
    "--show_description",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--show_icon",
    type=int,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "version":
    print(
        "{}{}-{}{}".format(
            f"{ICON} " if args.show_icon else "",
            NAME,
            VERSION,
            "\\n{}".format(DESCRIPTION) if args.show_description else "",
        )
    )
    success = True
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
