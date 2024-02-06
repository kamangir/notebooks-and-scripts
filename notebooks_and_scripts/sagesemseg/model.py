import sagemaker
import json
from abcli.elapsed_timer import ElapsedTimer
from abcli.modules import objects
from abcli import file
from abcli.plugins.storage import instance as storage
from notebooks_and_scripts.sagemaker import role
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class SageSemSegModel(object):
    def __init__(self):
        self.dataset_object_name = ""
        self.dataset_metadata = {}
        self.model_object_name = ""
        self.data_channels = {}

        timer = ElapsedTimer()
        self.session = sagemaker.Session()
        timer.stop()

        self.estimator = None

        self.training_image = sagemaker.image_uris.retrieve(
            "semantic-segmentation", self.session.boto_region_name
        )

        logger.info(
            "{} init ({}), image: {}".format(
                self.__class__.__name__,
                timer.elapsed_pretty(include_ms=True),
                self.training_image,
            )
        )

    def train(
        self,
        dataset_object_name: str,
        model_object_name: str,
        verbose: bool = False,
    ) -> bool:
        self.dataset_object_name = dataset_object_name
        self.model_object_name = model_object_name

        if not storage.download_file(
            f"bolt/{dataset_object_name}/metadata.yaml", "object"
        ):
            return False

        metadata_filename = objects.path_of(
            object_name=dataset_object_name,
            filename="metadata.yaml",
        )
        success, self.dataset_metadata = file.load_yaml(metadata_filename)
        if not success:
            return False

        logger.info(
            "{}.train: {} -> {}".format(
                self.__class__.__name__,
                self.dataset_object_name,
                self.model_object_name,
            )
        )
        if verbose:
            logger.info(
                "{}.metadata: {}".format(
                    self.dataset_object_name,
                    json.dumps(self.dataset_metadata, indent=4),
                )
            )

        self.estimator = sagemaker.estimator.Estimator(
            self.training_image,  # Container image URI
            role,  # Training job execution role with permissions to access our S3 bucket
            instance_count=1,
            instance_type="ml.p3.2xlarge",
            volume_size=50,  # in GB
            max_run=360000,  # in seconds
            output_path=f"s3://kamangir/bolt/{model_object_name}",
            base_job_name=model_object_name,
            sagemaker_session=self.session,
        )

        self.estimator.set_hyperparameters(
            backbone="resnet-50",  # This is the encoder. Other option is resnet-101
            algorithm="fcn",  # This is the decoder. Other options are 'psp' and 'deeplab'
            use_pretrained_model="True",  # Use the pre-trained model.
            crop_size=240,  # Size of image random crop.
            num_classes=21,  # Pascal has 21 classes. This is a mandatory parameter.
            epochs=10,  # Number of epochs to run.
            learning_rate=0.0001,
            optimizer="rmsprop",  # Other options include 'adam', 'rmsprop', 'nag', 'adagrad'.
            lr_scheduler="poly",  # Other options include 'cosine' and 'step'.
            mini_batch_size=16,  # Setup some mini batch size.
            validation_mini_batch_size=16,
            early_stopping=True,  # Turn on early stopping. If OFF, other early stopping parameters are ignored.
            early_stopping_patience=2,  # Tolerate these many epochs if the mIoU doens't increase.
            early_stopping_min_epochs=10,  # No matter what, run these many number of epochs.
            num_training_samples=self.dataset_metadata["num"][
                "train"
            ],  # num_training_samples,  # This is a mandatory parameter, 1464 in this case.
        )

        distribution = "FullyReplicated"
        self.data_channels = {
            "train": sagemaker.inputs.TrainingInput(
                self.dataset_metadata["channel"]["train"],
                distribution=distribution,
            ),
            "validation": sagemaker.inputs.TrainingInput(
                self.dataset_metadata["channel"]["validation"],
                distribution=distribution,
            ),
            "train_annotation": sagemaker.inputs.TrainingInput(
                self.dataset_metadata["channel"]["train_annotation"],
                distribution=distribution,
            ),
            "validation_annotation": sagemaker.inputs.TrainingInput(
                self.dataset_metadata["channel"]["validation_annotation"],
                distribution=distribution,
            ),
            # 'label_map': metadata["channel"]["label_map"], # label_map_channel
        }

        self.estimator.fit(self.data_channels, logs=True)

        return True
