from typing import List

from blue_options.terminal import show_usage, xtra

from blueflow.workflow.runners import list_of_runners
from blueflow.workflow.patterns import list_of_patterns


def help_create(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "pattern=<pattern>",
            xtra(",~upload", mono=mono),
        ]
    )

    args = ["[--publish_as <public-object-name>]"]

    return show_usage(
        [
            "workflow",
            "create",
            f"[{options}]",
            "[.|<job-name>]",
        ]
        + args,
        "create a <pattern> workflow.",
        {
            "pattern: {}".format(" | ".join(list_of_patterns())): "",
        },
        mono=mono,
    )


def help_monitor(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "~download,node=<node>,publish_as=<public-object-name>,~upload"

    return show_usage(
        [
            "workflow",
            "monitor",
            f"[{options}]",
            "[.|<job-name>]",
            "[<command-line>]",
        ],
        "monitor <job-name>/workflow and run <command-line>.",
        mono=mono,
    )


def help_submit(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~download,dryrun,", mono=mono),
            "to=<runner>",
            xtra(",~upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "workflow",
            "submit",
            f"[{options}]",
            "[.|<job-name>]",
        ],
        "submit workflow.",
        {
            "runner: {}".format(" | ".join(list_of_runners())): "",
        },
        mono=mono,
    )


help_functions = {
    "create": help_create,
    "monitor": help_monitor,
    "submit": help_submit,
}
