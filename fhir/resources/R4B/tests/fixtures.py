import decimal
import hashlib
import io
import os
import pathlib
import shutil
import sys
import tempfile
import typing
import zipfile
from os.path import dirname

import pytest  # type: ignore
from fhir_core.types import (
    Base64BinaryType,
    DateTimeType,
    DateType,
    InstantType,
    TimeType,
    UriType,
    UrlType,
)
from pydantic import BaseModel, Field

from tests import patch_r4b_test

patch_r4b_test.apply()
EXAMPLE_RESOURCES_URL = (
    "https://github.com/nazrulworld/hl7-archives/raw/"
    "0.4.0/FHIR/R4B/"
    "4.3.0-examples-json.zip"
)
ROOT_PATH = dirname(dirname(dirname(dirname(dirname(os.path.abspath(__file__))))))
CACHE_PATH = os.path.join(ROOT_PATH, ".cache", "R4B")


def download_and_store(url, path):
    """ """
    import requests

    try:
        sys.stdout.write("Attempting to download from {0}\n".format(url))
        ret = requests.get(url)
    except requests.HTTPError as exc:
        raise LookupError("Failed to download. Full error: {0!s}".format(exc))
    else:
        if not ret.ok:
            raise Exception("Failed to download {0}".format(url))
        with io.open(path, "wb") as handle:
            for chunk in ret.iter_content():
                handle.write(chunk)
            sys.stdout.write(
                "Download has been completed, now saved to {0}\n".format(path)
            )


def expand(self, local):
    """Expand the ZIP file at the given path to the cache directory."""
    path = os.path.join(self.cache, local)
    assert os.path.exists(path)
    import zipfile  # import here as we can bypass its use with a manual unzip

    with zipfile.ZipFile(path) as z:
        z.extractall(self.cache)


@pytest.fixture(scope="session")
def base_settings():
    if not os.path.exists(CACHE_PATH):
        os.makedirs(CACHE_PATH)

    settings = {}

    example_data_file_uri = EXAMPLE_RESOURCES_URL

    example_data_file_id = hashlib.md5(example_data_file_uri.encode()).hexdigest()

    example_data_file_location = os.path.join(
        CACHE_PATH, (example_data_file_id + ".zip")
    )

    if not os.path.exists(example_data_file_location):
        download_and_store(example_data_file_uri, example_data_file_location)

    temp_data_dir = tempfile.mkdtemp()
    # extract all files from archive and put into temp dir
    with zipfile.ZipFile(example_data_file_location) as z:
        z.extractall(temp_data_dir)

    zip_dir_name = pathlib.Path(EXAMPLE_RESOURCES_URL).name[:-4]
    if "FHIR_UNITTEST_DATADIR" not in os.environ:
        os.environ.setdefault(
            "FHIR_UNITTEST_DATADIR", os.path.join(temp_data_dir, zip_dir_name)
        )

    settings["unittest_data_dir"] = pathlib.Path(os.environ["FHIR_UNITTEST_DATADIR"])

    yield settings

    os.environ.pop("FHIR_UNITTEST_DATADIR")
    shutil.rmtree(temp_data_dir)


def bytes_validator(v: typing.Any) -> typing.Union[bytes]:
    if isinstance(v, bytes):
        return v
    elif isinstance(v, bytearray):
        return bytes(v)
    elif isinstance(v, str):
        return v.encode()
    elif isinstance(v, (float, int, decimal.Decimal)):
        return str(v).encode()
    else:
        raise ValueError


class ExternalValidatorModel(BaseModel):
    """This model is used to validate datetime objects against in the tests"""

    valueDate: DateType = Field(None, title="Date")
    valueTime: TimeType = Field(None, title="Time")
    valueDateTime: DateTimeType = Field(None, title="DateTime")
    valueInstant: InstantType = Field(None, title="Instant")
    valueUri: UriType = Field(None, title="Uri")
    valueUrl: UrlType = Field(None, title="Url")
    valueBase64Binary: Base64BinaryType = Field(None, title="Base64Binary")
