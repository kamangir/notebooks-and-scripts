import os

from blue_objects import file, README
from blue_objects.env import ABCLI_PUBLIC_PREFIX

from notebooks_and_scripts import NAME, VERSION, ICON, REPO_NAME
from notebooks_and_scripts.workflow.README import items as workflow_items


features = {
    "workflow": {
        "description": "an abstraction to run mixed-type (cpu/gpu/...) [DAG](https://networkx.org/documentation/stable/reference/classes/digraph.html)s of commands on [aws batch](https://aws.amazon.com/batch/), and a few other compute resources.",
        "icon": ICON,
        "thumbnail": f"{ABCLI_PUBLIC_PREFIX}/hourglass/workflow.gif?raw=true",
        "url": "https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow",
    },
    "scripts": {
        "description": "legacy mechanisms replaced with `@docker eval - <command>` and `@batch eval - <command>`.",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/assets/blob/main/nbs/3x4.jpg?raw=true",
        "url": "https://github.com/kamangir/notebooks-and-scripts/tree/main/scripts",
    },
    "template": {
        "description": "",
        "icon": "",
        "thumbnail": "",
        "url": "",
    },
}

items = [
    "{}[`{}`]({}) [![image]({})]({}) {}".format(
        details["icon"],
        feature,
        details["url"],
        details["thumbnail"],
        details["url"],
        details["description"],
    )
    for feature, details in features.items()
    if feature != "template"
]


def build():
    return README.build(
        items=items,
        cols=2,
        path=os.path.join(file.path(__file__), ".."),
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    ) and README.build(
        items=workflow_items,
        cols=4,
        path=os.path.join(file.path(__file__), "workflow"),
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
