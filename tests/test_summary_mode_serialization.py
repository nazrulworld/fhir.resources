from fhir.resources.R4B.patient import Patient

from .conftest import STATIC_PATH

__author__ = 'Md Nazrul Islam'
__email__ = "email2nazrul@gmail.com"

def test_summary_for_model_serialization():
    """ """
    patient_fhir = Patient.model_validate_json(
        (STATIC_PATH / "R4B" / "Patient-with-ext.json").read_bytes()
    )

    patient_dict = patient_fhir.model_dump(summary_only=True)
    assert "text" not in patient_dict
    assert "contained" not in patient_dict
    assert "extension" not in patient_dict
    assert "identifier" in patient_dict

    patient_dict = patient_fhir.model_dump(summary_only=False)
    assert "text" in patient_dict
    assert "contained" in patient_dict
    assert "extension" in patient_dict

def test_summary_for_json_serialization():
    """ """
    patient_fhir = Patient.model_validate_json(
        (STATIC_PATH / "R4B" / "Patient-with-ext.json").read_bytes()
    )

    json_str = patient_fhir.model_dump_json(summary_only=True)
    assert "\"text\"" not in json_str
    assert "\"contained\"" not in json_str
    assert "\"extension\"" not in json_str
    assert "\"identifier\"" in json_str

    json_str = patient_fhir.model_dump_json(summary_only=False)
    assert "\"text\"" in json_str
    assert "\"contained\"" in json_str
    assert "\"extension\"" in json_str


def test_summary_for_xml_serialization():
    """ """
    patient_fhir = Patient.model_validate_json(
        (STATIC_PATH / "R4B" / "Patient-with-ext.json").read_bytes()
    )

    xml_bytes = patient_fhir.model_dump_xml(summary_only=True)
    assert b"<text>" not in xml_bytes
    assert b"<contained>" not in xml_bytes
    assert b"<extension" not in xml_bytes
    assert b"<identifier>" in xml_bytes

    xml_bytes = patient_fhir.model_dump_xml(summary_only=False)
    assert b"<text>" in xml_bytes
    assert b"<contained>" in xml_bytes
    assert b"<extension" in xml_bytes

def test_summary_for_yaml_serialization():
    """ """
    patient_fhir = Patient.model_validate_json(
        (STATIC_PATH / "R4B" / "Patient-with-ext.json").read_bytes()
    )

    yaml_str = patient_fhir.model_dump_yaml(summary_only=True)

    assert "text:" not in yaml_str
    assert "contained:" not in yaml_str
    assert "extension:" not in yaml_str
    assert "identifier:" in yaml_str

    yaml_str = patient_fhir.model_dump_yaml(summary_only=False)

    assert "text:" in yaml_str
    assert "contained:" in yaml_str
    assert "extension:" in yaml_str
