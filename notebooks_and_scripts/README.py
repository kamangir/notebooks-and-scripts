import os
from blueness import module
import abcli
from abcli import file
from abcli.file.functions import build_from_template
from abcli.plugins import markdown
from notebooks_and_scripts import NAME, VERSION, ICON
from notebooks_and_scripts.logger import logger

NAME = module.name(__file__, NAME)

features = {
    "workflow": {
        "description": "an abstraction to run mixed-type (cpu/gpu/...) [DAG](https://networkx.org/documentation/stable/reference/classes/digraph.html)s of commands on [aws batch](https://aws.amazon.com/batch/).",
        "icon": ICON,
        "thumbnail": "https://kamangir-public.s3.ca-central-1.amazonaws.com/hourglass/workflow.gif?raw=true",
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


def build(filename: str = ""):
    if not filename:
        filename = os.path.join(file.path(__file__), "../README.md")

    logger.info(f"{NAME}.build: {filename}")

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

    table = markdown.generate_table(items, cols=2)

    signature = [
        "---",
        "built by [`{}`]({}), based on [`{}-{}`]({}).".format(
            abcli.fullname(),
            "https://github.com/kamangir/awesome-bash-cli",
            NAME,
            VERSION,
            "https://github.com/kamangir/openai-commands",
        ),
    ]

    return file.build_from_template(
        os.path.join(file.path(__file__), "./assets/README.md"),
        {
            "--table--": table,
            "--signature": signature,
        },
        filename,
    )
