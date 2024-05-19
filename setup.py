from setuptools import setup
import os

from notebooks_and_scripts import NAME, VERSION, DESCRIPTION


with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    long_description = f.read().replace(
        "./",
        "https://github.com/kamangir/notebooks-and-scripts/raw/main/",
    )

setup(
    name=NAME,
    author="arash@kamangir.net",
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        NAME,
        f"{NAME}.sagemaker",
    ],
    package_data={
        NAME: ["config.env"],
    },
)
