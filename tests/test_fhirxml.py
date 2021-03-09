from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from .fixtures import STATIC_PATH
from fhir.resources import fhirxml
__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

def test_xml_node_patient_resource():
    """ """
    patient_fhir = Patient.parse_file(STATIC_PATH / "Patient-with-ext.json")
    patient_node = fhirxml.Node.from_fhir_obj(patient_fhir)
    # with open("output.xml", "wb") as fp:
    #     fp.write(patient_node.to_string(True))
    #
    # with open("output.yml", "wb") as fp:
    #     fp.write(patient_fhir.yaml(return_bytes=True))

