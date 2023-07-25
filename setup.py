from setuptools import setup

from notebooks import NAME, VERSION

setup(
    name=NAME,
    author="arash@kamangir.net",
    version=VERSION,
    description="research notebooks",
    packages=[NAME],
)
