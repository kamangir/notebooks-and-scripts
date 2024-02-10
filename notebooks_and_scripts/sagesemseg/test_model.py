import pytest
from notebooks_and_scripts.sagesemseg.model import SageSemSegModel
from abcli.modules.objects import unique_object


@pytest.mark.parametrize(
    "dataset_object_name",
    [
        ("pascal-voc-v1-debug-v2"),
    ],
)
def test_SageSemSegModel(dataset_object_name):
    model = SageSemSegModel()

    dataset_object_name = unique_object("test_SageSemSegModel")

    assert model.train(
        dataset_object_name=dataset_object_name,
        model_object_name=model_object_name,
    )

    model.deploy(initial_instance_count=1, instance_type="ml.c5.xlarge")

    model.delete_endpoint()
