import os
import glob
from tqdm import tqdm
import shutil
from abcli.modules import objects
from abcli import logging
import logging

logger = logging.getLogger(__name__)


# https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/semantic_segmentation_pascalvoc/semantic_segmentation_pascalvoc.ipynb
def upload(
    dataset_object_name: str,
    object_name,
):
    dataset_object_path = objects.object_path(dataset_object_name)
    object_path = objects.object_path(object_name, create=True)

    logger.info(f"reorg: {dataset_object_path} -> {object_path}")

    """
    Move the images into appropriate directory structure as described in the 
    [documentation](link-to-documentation). This is quite simply, moving the 
    training images to `train` directory and so on. Fortunately, the dataset's 
    annotations are already named in sync with the image names, satisfying one 
    requirement of the Amazon SageMaker Semantic Segmentation algorithm.
    """

    # Create directory structure mimicing the s3 bucket where data is to be dumped.
    VOC2012 = os.path.join(dataset_object_path, "pascal-voc/VOC2012")
    for sub_folder in "train,validation,train_annotation,validation_annotation".split(
        ","
    ):
        os.makedirs(os.path.join(object_path, f"data/{sub_folder}"), exist_ok=True)

    # Create a list of all training images.
    with open(VOC2012 + "/ImageSets/Segmentation/train.txt") as f:
        train_list = f.read().splitlines()

    # Create a list of all validation images.
    with open(VOC2012 + "/ImageSets/Segmentation/val.txt") as f:
        val_list = f.read().splitlines()

    # Move the jpg images in training list to train directory and png images to train_annotation directory.
    for i in tqdm(train_list):
        shutil.copy2(
            VOC2012 + "/JPEGImages/" + i + ".jpg",
            os.path.join(object_path, "data/train/"),
        )
        shutil.copy2(
            VOC2012 + "/SegmentationClass/" + i + ".png",
            os.path.join(object_path, "data/train_annotation/"),
        )

    # Move the jpg images in validation list to validation directory and png images to validation_annotation directory.
    for i in tqdm(val_list):
        shutil.copy2(
            VOC2012 + "/JPEGImages/" + i + ".jpg",
            os.path.join(object_path, "data/validation/"),
        )
        shutil.copy2(
            VOC2012 + "/SegmentationClass/" + i + ".png",
            os.path.join(object_path, "data/validation_annotation/"),
        )

    """
    Let us check if the move was completed correctly. If it was done correctly, the 
    number of jpeg images in `train` and png images in `train_annotation` must be the 
    same, and so in validation as well.
    """

    num_training_samples = len(
        glob.glob1(
            os.path.join(object_path, "data/train"),
            "*.jpg",
        )
    )
    num_validation_samples = len(
        glob.glob1(
            os.path.join(object_path, "data/validation"),
            "*.jpg",
        )
    )
    logger.info("Num Train Images = " + str(num_training_samples))
    assert num_training_samples == len(
        glob.glob1(
            os.path.join(object_path, "data/train_annotation"),
            "*.png",
        )
    )
    logger.info("Num Validation Images = " + str(num_validation_samples))
    assert num_validation_samples == len(
        glob.glob1(
            os.path.join(object_path, "data/validation_annotation"),
            "*.png",
        )
    )

    logger.info("wip 🪄")
    return True
