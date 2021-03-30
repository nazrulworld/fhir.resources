import os
import pathlib
from os.path import dirname

TESTS_ROOT_PATH = pathlib.Path(dirname(os.path.abspath(__file__)))
STATIC_PATH = TESTS_ROOT_PATH / "static"
FHIR_XSD_DIR = STATIC_PATH / "xsd" / "fhir"
IS_TRAVIS = "TRAVIS" in os.environ
