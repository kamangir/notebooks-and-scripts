from setuptools import setup

from notebooks_and_scripts import NAME, VERSION, DESCRIPTION

NAME = NAME.replace(" & ", "_and_")

setup(
    name=NAME,
    author="arash@kamangir.net",
    version=VERSION,
    description=DESCRIPTION,
    packages=[NAME],
)
