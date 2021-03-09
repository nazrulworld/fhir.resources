import os
from os.path import dirname
import pathlib

TESTS_ROOT_PATH = pathlib.Path(dirname(os.path.abspath(__file__)))
STATIC_PATH = TESTS_ROOT_PATH / "static"
