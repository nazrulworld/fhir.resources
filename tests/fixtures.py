import os
from os.path import dirname
import pathlib
import subprocess

TESTS_ROOT_PATH = pathlib.Path(dirname(os.path.abspath(__file__)))
STATIC_PATH = TESTS_ROOT_PATH / "static"


def has_internet_connection():
    """ """
    try:
        res = subprocess.check_call(["ping", "-c", "1", "8.8.8.8"])
        return res == 0
    except subprocess.CalledProcessError:
        return False
