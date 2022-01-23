from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="python-lib-template-repository",
    description="GitHub template repository for creating new Python libarries, using the simonw/python-lib cookiecutter template ",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="test-organisation3210",
    url="https://github.com/test-organisation3210/python-lib-template-repository",
    project_urls={
        "Issues": "https://github.com/test-organisation3210/python-lib-template-repository/issues",
        "CI": "https://github.com/test-organisation3210/python-lib-template-repository/actions",
        "Changelog": "https://github.com/test-organisation3210/python-lib-template-repository/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["python_lib_template_repository"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
)
