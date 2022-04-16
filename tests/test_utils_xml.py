import sys
from http import client

import lxml.etree  # type: ignore

from fhir.resources.core import utils
from fhir.resources.observation import Observation
from fhir.resources.patient import Patient

from .fixtures import FHIR_XSD_DIR, IS_TRAVIS, STATIC_PATH
from .utils import has_internet_connection, post_xml_resource

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


def test_xml_node_patient_resource():
    """Accept-Charset: utf-8
    Accept: application/fhir+xml;q=1.0, application/xml+fhir;q=0.9
    User-Agent: HAPI-FHIR/5.3.0 (FHIR Client; FHIR 4.0.1/R4; apache)
    Accept-Encoding: gzip
    Content-Type: application/fhir+xml; charset=UTF-8
    """
    patient_fhir = Patient.parse_file(STATIC_PATH / "Patient-with-ext.json")
    patient_node = utils.xml.Node.from_fhir_obj(patient_fhir)

    schema = lxml.etree.XMLSchema(file=str(FHIR_XSD_DIR / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    try:
        patient_node.validate(patient_node, xmlparser=xmlparser)
    except ValueError:
        raise AssertionError("code should not come here!")

    if not (has_internet_connection() and IS_TRAVIS):
        return
    conn = None
    try:
        conn = client.HTTPConnection("hapi.fhir.org", 80)
        response = post_xml_resource(conn, patient_fhir)
        assert response is not None
        assert response.status == 201
    except client.HTTPException as exc:
        sys.stderr.write(f"{exc}\n")
        return
    finally:
        if conn:
            conn.close()


def test_xml_node_observation_resource():
    """ """
    observation_fhir = Observation.parse_file(STATIC_PATH / "Observation.json")
    observation_node = utils.xml.Node.from_fhir_obj(observation_fhir)

    schema = lxml.etree.XMLSchema(file=str(FHIR_XSD_DIR / "observation.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    try:
        observation_node.validate(observation_node, xmlparser=xmlparser)
    except ValueError:
        raise AssertionError("code should not come here!")

    if not (has_internet_connection() and IS_TRAVIS):
        return
    conn = None
    try:
        conn = client.HTTPConnection("hapi.fhir.org", 80)
        response = post_xml_resource(conn, observation_fhir)
        assert response is not None
        assert response.status == 201
    except client.HTTPException as exc:
        sys.stderr.write(f"{exc}\n")
        return
    finally:
        if conn:
            conn.close()


def test_element_to_node():
    """ """
    observation_fhir = Observation.parse_file(STATIC_PATH / "Observation.json")
    observation_node = utils.xml.Node.from_fhir_obj(observation_fhir)

    schema = lxml.etree.XMLSchema(file=str(FHIR_XSD_DIR / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    element = lxml.etree.fromstring(
        (STATIC_PATH / "Patient-with-ext.xml").read_bytes(),
        parser=xmlparser,
    )
    patient_node = utils.xml.Node.from_element(element)
    try:
        patient_node.validate(patient_node.to_xml(), xmlparser=xmlparser)
    except ValueError:
        raise AssertionError("Code should not come here!")


def test_model_obj_xml_file():
    """ """
    patient = Patient.parse_file(STATIC_PATH / "Patient-with-ext.xml")
    # with parser parameter
    schema = lxml.etree.XMLSchema(file=str(FHIR_XSD_DIR / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    patient2 = Patient.parse_file(
        STATIC_PATH / "Patient-with-ext.xml", xmlparser=xmlparser
    )
    patient3 = Patient.parse_file(STATIC_PATH / "Patient-with-ext.json")
    assert patient == patient2
    patient3.text = None
    patient.text = None
    patient.contained[1].text = None
    patient3.contained[1].text = None
    assert patient3 == patient
