import os
import pathlib

RESOURCE_TARGET_DIRECTORY = (
    pathlib.Path(os.path.abspath(__file__)).parents[2] / "fhir" / "resources"
)
UNITTEST_TARGET_DIRECTORY = RESOURCE_TARGET_DIRECTORY / "tests"
FHIR_EXAMPLE_DIRECTORY = (
    pathlib.Path(os.path.abspath(__file__)).parents[2]
    / "script"
    / "static"
    / "examples-json"
    / "R4B"
)
