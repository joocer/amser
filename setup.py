from setuptools import setup, find_packages  # type:ignore
from amser.version import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="amser",
    version=version,
    description="Python Timer Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="joocer",
    author_email="justin.joyce@joocer.com",
    packages=find_packages('amser'),
    url="https://github.com/joocer/amser",
    install_requires=[''],
)