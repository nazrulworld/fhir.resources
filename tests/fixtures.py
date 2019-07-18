import os
from os.path import dirname

ROOT_PATH = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
PARSER_PATH = os.path.join(ROOT_PATH, 'fhir-parser')
SCRIPT_PATH = os.path.join(ROOT_PATH, 'script')
CACHE_PATH = os.path.join(ROOT_PATH, '.cache')
