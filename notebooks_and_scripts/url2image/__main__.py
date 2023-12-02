import argparse
from notebooks_and_scripts.url2image import NAME, read_url, render_url
from notebooks_and_scripts import VERSION
from abcli import logging
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="read_url|render_url",
)
parser.add_argument(
    "--url",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--count",
    type=int,
    default=1,
)
parser.add_argument(
    "--height",
    type=int,
    default=1024,
)
parser.add_argument(
    "--width",
    type=int,
    default=1024,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "read_url":
    success, description = read_url(
        url=args.url,
        verbose=bool(args.verbose),
    )
elif args.task == "render_url":
    success = render_url(
        url=args.url,
        object_name=args.object_name,
        count=args.count,
        height=args.height,
        width=args.width,
        verbose=bool(args.verbose),
    )
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
