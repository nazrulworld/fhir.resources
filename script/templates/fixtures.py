import hashlib
import io
import os
import shutil
import sys
import tempfile
import zipfile

import pytest
import six

from os.path import dirname


ROOT_PATH = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
PARSER_PATH = os.path.join(ROOT_PATH, 'fhir-parser')
SCRIPT_PATH = os.path.join(ROOT_PATH, 'script')
CACHE_PATH = os.path.join(ROOT_PATH, '.cache')


def force_bytes(string, encoding='utf8', errors='strict'):

    if isinstance(string, bytes):
        if encoding == 'utf8':
            return string
        else:
            return string.decode('utf8', errors).encode(encoding, errors)

    if not isinstance(string, six.string_types):
        return string

    return string.encode(encoding, errors)


def download_and_store(url, path):
    """ """
    import requests
    try:
        sys.stdout.write('Attempting to download from {0}\n'.format(url))
        ret = requests.get(url)
    except requests.HTTPError as exc:
        raise LookupError(
            'Failed to download. Full error: {0!s}'.format(exc)
        )
    else:
        if not ret.ok:
            raise Exception("Failed to download {0}".format(url))
        with io.open(path, 'wb') as handle:
            for chunk in ret.iter_content():
                handle.write(chunk)
            sys.stdout.write(
                'Download has been completed, now saved to {0}\n'.format(path)
            )


def expand(self, local):
    """ Expand the ZIP file at the given path to the cache directory.
    """
    path = os.path.join(self.cache, local)
    assert os.path.exists(path)
    import zipfile  # import here as we can bypass its use with a manual unzip

    with zipfile.ZipFile(path) as z:
        z.extractall(self.cache)


@pytest.fixture(scope='session')
def base_settings():

    if not os.path.exists(CACHE_PATH):
        os.makedirs(CACHE_PATH)

    settings = {}

    with io.open(os.path.join(SCRIPT_PATH, 'settings.py'), 'r') as fp:
        exec(fp.read(), settings)

    example_data_file_uri = '/'.join([settings['base_url'], settings['current_version'], 'examples-json.zip'])

    example_data_file_id = \
            hashlib.md5(example_data_file_uri.encode()).hexdigest()

    example_data_file_location = os.path.join(CACHE_PATH, (example_data_file_id + '.zip'))

    if not os.path.exists(example_data_file_location):
        download_and_store(
            example_data_file_uri,
            example_data_file_location)

    temp_data_dir = tempfile.mkdtemp()
    # extract all files from archive and put into temp dir
    with zipfile.ZipFile(example_data_file_location) as z:
        z.extractall(temp_data_dir)

    if 'FHIR_UNITTEST_DATADIR' not in os.environ:
        os.environ.setdefault('FHIR_UNITTEST_DATADIR', temp_data_dir)

    yield settings

    os.environ.pop('FHIR_UNITTEST_DATADIR')
    shutil.rmtree(temp_data_dir)
