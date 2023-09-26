from setuptools import setup

from notebooks_and_scripts import NAME, VERSION, DESCRIPTION

setup(
    name=NAME,
    author="arash@kamangir.net",
    version=VERSION,
    description=DESCRIPTION,
    packages=[NAME.replace(" & ", "_and_")],
)
