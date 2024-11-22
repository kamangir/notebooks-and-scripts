from typing import List, Union
import base64
from IPython.display import display, HTML
import os
from functools import reduce


def get_image_base64(filename):
    with open(filename, "rb") as f:
        data = f.read()
        return "data:image/gif;base64," + base64.b64encode(data).decode("utf-8")


def imshow(
    list_of_files: Union[
        List[List[str]],
        List[str],
        str,
    ],
    dryrun: bool = False,
):
    if not isinstance(list_of_files, list):
        list_of_files = [list_of_files]
    list_of_files = [(row if isinstance(row, list) else [row]) for row in list_of_files]

    html = "".join(
        ["<table>"]
        + reduce(
            lambda x, y: x + y,
            [
                ["<tr>"]
                + [
                    '<td><img src="{}"></td>'.format(get_image_base64(filename))
                    for filename in row
                ]
                + ["</tr>"]
                for row in list_of_files
            ],
            [],
        )
        + ["</table>"]
    )

    if not dryrun:
        display(HTML(html))


for var, value in {
    "abcli_path_bash": "{}/git/awesome-bash-cli/bash".format(os.getenv("HOME")),
    "MLFLOW_TRACKING_URI": "databricks",
}.items():
    os.environ[var] = value
