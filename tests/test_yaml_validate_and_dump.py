from fhir.resources.R4B.patient import Patient

from .fixtures import STATIC_PATH

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


def test_yaml_patient_resource():
    """ """
    patient_fhir = Patient.model_validate_yaml(
        (STATIC_PATH / "R4B" / "Patient-with-ext.json").read_bytes()
    )
    yaml_str = patient_fhir.model_dump_yaml()
    patient_fhir_2 = Patient.model_validate_yaml(yaml_str)
    assert patient_fhir_2.model_dump() == patient_fhir.model_dump()
