from typing import Any
import pytest
from notebooks_and_scripts import env
from notebooks_and_scripts.aws_batch.traffic import decode_traffic, encode_traffic


@pytest.mark.parametrize(
    ["pattern"],
    [
        [env.ABCLI_AWS_BATCH_TRAFFIC_PATTERN_EXAMPLE_SIMPLE],
        [env.ABCLI_AWS_BATCH_TRAFFIC_PATTERN_EXAMPLE_HARD],
    ],
)
def test_decode_encode_traffic(
    pattern: str,
):
    assert encode_traffic(decode_traffic(pattern)) == pattern
