import os
import pytest
import pathlib

PARSER_PATH = pathlib.Path(os.path.abspath(__file__)).parents[3] / 'fhir-parser'


@pytest.fixture(scope='module')
def base_settings():

    settings = dict()
    if 'FHIR_UNITTEST_DATADIR' not in os.environ:
        os.environ.setdefault('FHIR_UNITTEST_DATADIR', str(PARSER_PATH / 'downloads'))

    yield settings
