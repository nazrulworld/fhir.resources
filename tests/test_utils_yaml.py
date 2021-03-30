import sys
from http import client

import lxml.etree  # type: ignore

from fhir.resources import utils
from fhir.resources.observation import Observation
from fhir.resources.patient import Patient

from .fixtures import FHIR_XSD_DIR, IS_TRAVIS, STATIC_PATH
from .utils import has_internet_connection, post_xml_resource

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


def test_yaml_patient_resource():
    """ """
    patient_fhir = Patient.parse_file(STATIC_PATH / "Patient-with-ext.json")
    yaml_str = patient_fhir.yaml(return_bytes=True)
    patient_fhir_2 = Patient.parse_raw(yaml_str, content_type="text/yaml")
    assert patient_fhir_2.dict() == patient_fhir.dict()
