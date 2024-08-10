from functools import reduce
from notebooks_and_scripts.workflow.patterns import list_of_patterns
from notebooks_and_scripts.workflow.runners import list_of_runners

items = [
    "[`{}`](./patterns/{}.dot) {}".format(
        pattern,
        pattern,
        " ".join(
            [
                "[🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/{}-{}/workflow.gif?raw=true)".format(
                    runner_type,
                    pattern,
                )
                for runner_type in list_of_runners()
            ]
        ),
    )
    for pattern in list_of_patterns()
] + reduce(
    lambda x, y: x + y,
    [
        [
            "![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/{}-{}/workflow.gif?raw=true)".format(
                runner_type,
                pattern,
            )
            for pattern in list_of_patterns()
        ]
        for runner_type in list_of_runners()
    ],
    [],
)
