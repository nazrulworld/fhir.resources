#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["isodate"]

setup_requirements = ["pytest-runner"]

test_requirements = ["coverage", "pytest", "pytest-cov"]

setup(
    author="Md Nazrul Islam",
    author_email="email2nazrul@gmail.com",
    # Get more from https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
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
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={"test": test_requirements + setup_requirements},
    url="https://github.com/nazrulworld/fhir.resources",
    version="5.0.0b2",
    zip_safe=False,
)
