#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["pydantic[email]>=1.7.2"]

setup_requirements = ["pytest-runner"]

orjson_requirements = ["orjson>=3.4.3"]

test_requirements = [
    "coverage",
    "pytest>5.4.0;python_version>='3.6'",
    "pytest-cov>=2.10.0;python_version>='3.6'",
    "flake8==3.8.3",
    "flake8-isort==3.0.0",
    "flake8-bugbear==20.1.4",
    "requests==2.23.0",
    "isort==4.3.21",
    "black",
    "mypy",
]

development_requirements = [
    "Jinja2==2.11.1",
    "MarkupSafe==1.1.1",
    "colorlog==2.10.0",
    "certifi",
    "fhirspec",
    "zest-releaser[recommended]",
]
setup(
    author="Md Nazrul Islam",
    author_email="email2nazrul@gmail.com",
    # Get more from https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    description="FHIR Resources as Model Class",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="fhir, resources, python, hl7, health IT, healthcare",
    name="fhir.resources",
    namespace_packages=["fhir"],
    packages=find_packages(exclude=["ez_setup"]),
    package_data={"fhir.resources": ["py.typed"]},
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={
        "orjson": orjson_requirements,
        "test": (test_requirements + setup_requirements),
        "all": (
            test_requirements
            + setup_requirements
            + development_requirements
            + orjson_requirements
        ),
    },
    url="https://github.com/nazrulworld/fhir.resources",
    version="6.0.0",
    zip_safe=False,
    python_requires=">=3.6",
    project_urls={
        "CI: Travis": "https://travis-ci.org/github/nazrulworld/fhir.resources",
        "Coverage: codecov": "https://codecov.io/gh/nazrulworld/fhir.resources",
        "GitHub: issues": "https://github.com/nazrulworld/fhir.resources/issues",
        "GitHub: repo": "https://github.com/nazrulworld/fhir.resources",
    },
)
