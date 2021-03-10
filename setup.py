from setuptools import setup, find_packages  # type:ignore

with open("README.md", "r") as fh:
    long_description = fh.read()

version = eval(open("amser/version.py", "r").read())  # nosec

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