# coding=utf-8

from urllib.parse import urljoin

from setuptools import find_packages
from setuptools import setup

from xargproject.attribute import __author__
from xargproject.attribute import __author_email__
from xargproject.attribute import __description__
from xargproject.attribute import __project__
from xargproject.attribute import __urlhome__
from xargproject.attribute import __version__

__urlcode__ = __urlhome__
__urldocs__ = __urlhome__
__urlbugs__ = urljoin(__urlhome__, "issues")


def all_requirements():
    def read_requirements(path: str):
        with open(path, "r", encoding="utf-8") as rhdl:
            return rhdl.read().splitlines()

    requirements = read_requirements("requirements.txt")
    return requirements


setup(
    name=__project__,
    version=__version__,
    description=__description__,
    url=__urlhome__,
    author=__author__,
    author_email=__author_email__,
    project_urls={"Source Code": __urlcode__,
                  "Bug Tracker": __urlbugs__,
                  "Documentation": __urldocs__},
    packages=find_packages(include=["xargproject*"], exclude=["xargproject.unittest"]),
    install_requires=all_requirements())
