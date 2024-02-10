import argparse
from notebooks_and_scripts import VERSION
from notebooks_and_scripts.sagesemseg.dataset import upload as upload_dataset
from notebooks_and_scripts.sagesemseg.model import SageSemSegModel
from abcli import logging
import logging

logger = logging.getLogger(__name__)

NAME = "notebooks_and_scripts.sagesemseg"

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="train_model|upload_dataset",
)
parser.add_argument(
    "--dataset_object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--model_object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--epochs",
    type=int,
    default=10,
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
)
parser.add_argument(
    "--deploy",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--delete_endpoint",
    type=int,
    default=1,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "train_model":
    success = True

    model = SageSemSegModel()

    if not model.train(
        dataset_object_name=args.dataset_object_name,
        model_object_name=args.model_object_name,
        epochs=args.epochs,
    ):
        success = False
    elif args.deploy:
        model.deploy(
            initial_instance_count=1,
            instance_type="ml.c5.xlarge",
        )

        if args.delete_endpoint:
            model.delete_endpoint()
elif args.task == "upload_dataset":
    upload_dataset(
        dataset_object_name=args.dataset_object_name,
        object_name=args.object_name,
        count=args.count,
    )
    success = True
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
