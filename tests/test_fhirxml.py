from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from http import client
from .fixtures import STATIC_PATH, FHIR_XSD_DIR
from .utils import has_internet_connection, post_xml_resource
from fhir.resources import utils
import pytest
import sys
import pathlib
import lxml.etree

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
    with open("output.xml", "wb") as fp:
        fp.write(patient_fhir.xml(return_bytes=True, pretty_print=True))

    with open("output.json", "wb") as fp:
        fp.write(patient_fhir.json(return_bytes=True, indent=2, exclude_comments=False))

    schema = lxml.etree.XMLSchema(file=str(FHIR_XSD_DIR / "patient.xsd"))
    xmlparser = lxml.etree.XMLParser(schema=schema)
    el = lxml.etree.parse("output.xml", parser=xmlparser)

    patient_node.validate(FHIR_XSD_DIR / "patient.xsd")
    return
    if not has_internet_connection():
        return
    conn = None
    try:
        conn = client.HTTPConnection("hapi.fhir.org", 80)
        response = post_xml_resource(conn, patient_node)
        assert response is not None
        assert response.status == 201
    except client.HTTPException as exc:
        sys.stderr.write(f"{exc}\n")
        return
    finally:
        if conn:
            conn.close()
    # with open("output.yml", "wb") as fp:
    #     fp.write(patient_fhir.yaml(return_bytes=True))
