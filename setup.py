import os
import io
import pathlib

from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
VERSION = (HERE / "VERSION.txt").read_text()

with open(os.path.join(HERE, "requirements.txt"), encoding="utf-8") as requirements:
    REQUIREMENTS = requirements.read().split("\n")

install_requires = [
    x.strip() for x in REQUIREMENTS if ("git+" not in x) 
    and (not x.startswith("#"))
    and (not x.startswith("-"))
]

dependency_links = [x.strip().replace("git+", "") for x in install_requires if "git+" not in x]

setup(
    name="journal",
    description="Command Line Interface for managing my Journal entries",
    version=VERSION,
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.7",
    entrypoints=""""
        [console_scripts]
        journal=journal.__main__:main
    """,
    author="André de Moraes <amancioandre@gmail.com>",
    keyword="journal manager",
    long_description=README,
    license="MIT",
    dependency_links=dependency_links,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ]
)