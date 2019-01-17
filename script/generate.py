#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Download and parse FHIR resource definitions
#  Supply "-f" to force a redownload of the spec
#  Supply "-c" to force using the cached spec (incompatible with "-f")
#  Supply "-d" to load and parse but not write resources
#  Supply "-l" to only download the spec
import ast
from distutils.version import StrictVersion
import configparser
import pathlib
import requests
import os
import subprocess
import shutil
import sys

import settings

SRC_BASE_PATH = pathlib.Path(os.path.abspath(__file__)).parents[1] / 'fhir' / 'resources'
PARSER_BASE_PATH = pathlib.Path(os.path.abspath(__file__)).parents[1] / 'fhir-parser'
PARSER_CACHE_DIR = PARSER_BASE_PATH / 'downloads'
SCRIPT_BASE_PATH = pathlib.Path(os.path.abspath(__file__)).parents[1] / 'script'


def get_current_version():
    """ """
    version_file = str(SRC_BASE_PATH / '__init__.py')
    with open(str(SRC_BASE_PATH / '__init__.py'), 'r', encoding='utf-8') as fd:

        for line in fd:
            if '__version__' in line:
                version = StrictVersion(ast.literal_eval(line.split('=')[1].strip()))
                sys.stdout.write(f'Version `{version}` at {version_file}\n')
                return version


def get_cached_version_info():
    """ """
    if not PARSER_CACHE_DIR.exists():
        return
    version_file = PARSER_CACHE_DIR / 'version.info'

    if not version_file.exists():
        return

    config = configparser.ConfigParser()

    with open(str(version_file), 'r') as fp:
        txt = fp.read()
        config.read_string('\n'.join(txt.split('\n')[1:]))

    return config['FHIR']['version'], config['FHIR']['fhirversion']


def get_fhir_version_info():
    """ """
    try:
        response = requests.get(settings.specification_url + '/version.info')
        text = response.text
        config = configparser.ConfigParser()

        config.read_string('\r'.join(text.split('\r')[1:]))

        return config['FHIR']['version'], config['FHIR']['fhirversion']

    except requests.HTTPError as exc:
        sys.stderr.write(str(exc))
        return None


def update_pytest_fixture(version):
    """ """
    lines = list()
    fixture_file = SRC_BASE_PATH / version / 'tests' / 'fixtures.py'
    with open(str(fixture_file), 'r', encoding='utf-8') as fp:
        for line in fp:
            if 'ROOT_PATH =' in line:
                parts = list()
                parts.append(line.split('=')[0])
                parts.append("dirname(dirname(dirname(dirname(dirname(os.path.abspath(__file__))))))\n")
                line = '= '.join(parts)

            elif 'CACHE_PATH =' in line:
                parts = list()
                parts.append(line.split('=')[0])
                parts.append(f"os.path.join(ROOT_PATH, '.cache', '{version}')\n")
                line = '= '.join(parts)

            elif 'example_data_file_uri =' in line:

                parts = list()
                parts.append(line.split('=')[0])
                parts.append(f"'/'.join([settings['base_url'], '{version}', 'examples-json.zip'])\n")
                line = '= '.join(parts)

            lines.append(line)

    # let's write
    fixture_file.write_text(''.join(lines))

    with open(str(SRC_BASE_PATH / version / 'tests' / 'conftest.py'), 'w', encoding='utf-8') as fp:
        fp.write(
            "# _*_ coding: utf-8 _*_\n"
            f"pytest_plugins = ['fhir.resources.{version}.tests.fixtures']\n")


def main():
    """ """
    force_download = len(sys.argv) > 1 and '-f' in sys.argv
    keep_previous_versions = len(sys.argv) > 1 and (
        "-k" in sys.argv or "--keep-previous-versions" in sys.argv
    )

    fhir_v_info = get_fhir_version_info()
    current_version = get_current_version()

    args = [f'{PARSER_BASE_PATH}/generate.py'] + sys.argv[1:]

    shutil.copy(str(SCRIPT_BASE_PATH / 'settings.py'), str(PARSER_BASE_PATH / 'settings.py'))
    try:
        subprocess.check_call(args=args, cwd=str(PARSER_BASE_PATH))
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(str(exc) + '\n')
        return 1

    cached_v_info = get_cached_version_info()

    if (StrictVersion(fhir_v_info[0]) > StrictVersion(cached_v_info[0])) and not force_download:
        sys.stdout.write(
            '==> New FHIR version {0} is available! However resources '
            'are generated from cache.'.format(fhir_v_info[0]))

    if keep_previous_versions and getattr(settings, 'previous_versions', None):

        for version in settings.previous_versions:
            update_pytest_fixture(version)

    return 0


if '__main__' == __name__:
    """ """
    try:
        sys.exit(main())
    except KeyboardInterrupt as exc:
        sys.stdout.write(str(exc))
        sys.exit(0)

