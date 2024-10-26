from functools import reduce

from blue_options import string
from blue_objects.env import ABCLI_PUBLIC_PREFIX

from blueflow.workflow.patterns import list_of_patterns
from blueflow.workflow.runners import list_of_runners


items = (
    ["📜"]
    + [
        "[`{}`](./patterns/{}.dot)".format(
            pattern,
            pattern,
        )
        for pattern in list_of_patterns()
    ]
    + reduce(
        lambda x, y: x + y,
        [
            (
                [f"[{runner_type}](./runners/{runner_type}.py)"]
                + [
                    f"[![image]({url})]({url})"
                    for url in [
                        "{}/{}-{}/workflow.gif?raw=true&random={}".format(
                            ABCLI_PUBLIC_PREFIX,
                            runner_type,
                            pattern,
                            string.random(),
                        )
                        for pattern in list_of_patterns()
                    ]
                ]
            )
            for runner_type in list_of_runners()
        ],
        [],
    )
)
