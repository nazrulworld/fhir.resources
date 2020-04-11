import os
import pathlib

RESOURCE_TARGET_DIRECTORY = pathlib.Path(os.path.abspath(__file__)).parents[2] / 'fhir' / 'resources'
UNITTEST_TARGET_DIRECTORY = RESOURCE_TARGET_DIRECTORY / 'tests'
FACTORY_TARGET_NAME = RESOURCE_TARGET_DIRECTORY / 'fhirelementfactory.py'
