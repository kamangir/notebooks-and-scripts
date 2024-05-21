from notebooks_and_scripts import NAME, VERSION, DESCRIPTION
from blueness.pypi import setup


setup(
    filename=__file__,
    repo_name="notebooks-and-scripts",
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.sagemaker",
    ],
    package_data={
        NAME: ["config.env"],
    },
)
