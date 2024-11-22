import pytest

from abcli.env import VANWATCH_TEST_OBJECT
from blue_objects import objects

from blueflow.notebooks import imshow


@pytest.mark.parametrize(
    ["object_name", "filename"],
    [
        [
            VANWATCH_TEST_OBJECT,
            "Victoria41East.jpg",
        ],
    ],
)
def test_imshow(
    object_name: str,
    filename: str,
):
    assert objects.download(
        object_name=object_name,
        filename=filename,
    )

    assert imshow(
        filename,
        dryrun=True,
    )

    assert imshow(
        [filename],
        dryrun=True,
    )

    assert imshow(
        [filename for _ in range(3)],
        dryrun=True,
    )

    assert imshow(
        [[filename for _ in range(3)]],
        dryrun=True,
    )

    assert imshow(
        [[filename for _ in range(3)] for _ in range(4)],
        dryrun=True,
    )
