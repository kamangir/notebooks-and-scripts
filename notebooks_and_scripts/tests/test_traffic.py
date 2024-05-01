import pytest
from abcli.modules.objects import unique_object
from notebooks_and_scripts import env
from notebooks_and_scripts.aws_batch.traffic.classes import Traffic
from notebooks_and_scripts.aws_batch.traffic.patterns import list_of_patterns


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
@pytest.mark.parametrize(
    ["command_line"],
    [
        [env.ABCLI_AWS_BATCH_DEFAULT_TRAFFIC_COMMAND_UQ],
    ],
)
def test_Traffic(pattern: str, command_line: str):
    job_name = unique_object()

    traffic = Traffic(job_name)

    assert traffic.load_pattern(
        command_line,
        pattern,
    )

    assert traffic.submit(dryrun=True)
