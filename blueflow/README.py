import os

from blue_objects import file, README

from blueflow import NAME, VERSION, ICON, REPO_NAME
from blueflow.workflow.README import items as workflow_items
from blueflow.workflow.patterns import list_of_patterns


def build():
    return README.build(
        items=workflow_items,
        cols=len(list_of_patterns()) + 1,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        MODULE_NAME="blueflow",
        REPO_NAME=REPO_NAME,
    )
