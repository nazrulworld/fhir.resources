"""Extension.value[x] primitives can carry their own id/extensions in JSON
through the ``_valueX`` sibling property, the same as any other primitive.
https://hl7.org/fhir/R4/json.html#primitive
"""

import importlib
import json

import pytest
from pydantic import ValidationError

RELEASES = ["fhir.resources", "fhir.resources.R4B", "fhir.resources.STU3"]

BIRTHSEX_URL = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex"


def _patient_class(release):
    return importlib.import_module(release + ".patient").Patient


def _extension_class(release):
    return importlib.import_module(release + ".extension").Extension


@pytest.mark.parametrize("release", RELEASES)
def test_extension_accepts_underscore_value_sibling(release):
    Patient = _patient_class(release)
    data = {
        "resourceType": "Patient",
        "extension": [
            {
                "url": BIRTHSEX_URL,
                "valueCode": "F",
                "_valueCode": {"id": "us-core-birthsex1"},
            }
        ],
    }
    patient = Patient.model_validate(data)
    ext = patient.extension[0]
    assert ext.valueCode == "F"
    assert ext.valueCode__ext.id == "us-core-birthsex1"

    dumped = json.loads(patient.model_dump_json())
    assert dumped["extension"][0]["_valueCode"] == {"id": "us-core-birthsex1"}
    assert dumped["extension"][0]["valueCode"] == "F"

    # and it round trips
    again = Patient.model_validate_json(patient.model_dump_json())
    assert again.extension[0].valueCode__ext.id == "us-core-birthsex1"


@pytest.mark.parametrize("release", RELEASES)
def test_extension_underscore_value_with_nested_extension(release):
    Extension = _extension_class(release)
    ext = Extension.model_validate(
        {
            "url": "http://example.org/fhir/StructureDefinition/note",
            "valueString": "hello",
            "_valueString": {
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/translation",
                        "valueString": "hallo",
                    }
                ]
            },
        }
    )
    assert ext.valueString == "hello"
    assert ext.valueString__ext.extension[0].valueString == "hallo"
    dumped = ext.model_dump()
    assert dumped["_valueString"]["extension"][0]["valueString"] == "hallo"


@pytest.mark.parametrize("release", RELEASES)
def test_extension_url_is_still_required(release):
    Extension = _extension_class(release)
    with pytest.raises(ValidationError):
        Extension.model_validate({"valueCode": "F", "_valueCode": {"id": "a"}})


@pytest.mark.parametrize("release", RELEASES)
def test_extension_url_cannot_have_underscore_sibling(release):
    # Extension.url is an XML attribute in FHIR, so it has no _url form.
    Extension = _extension_class(release)
    with pytest.raises(ValidationError):
        Extension.model_validate(
            {"url": "http://example.org/x", "_url": {"id": "a"}, "valueCode": "F"}
        )
