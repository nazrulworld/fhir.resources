# _*_ coding: utf-8 _*_
import re

import pytest  # type: ignore
from pydantic.error_wrappers import ValidationError
from pydantic.errors import ConfigError

from fhir.resources.fhirtypes import Id
from fhir.resources.organization import Organization


def test_primitive_type_id():
    """Issue#https://github.com/nazrulworld/fhir.resources/pull/48"""
    original = {
        "min_length": Id.min_length,
        "max_length": Id.max_length,
        "regex": Id.regex,
    }
    # test configuration constraint
    with pytest.raises(ConfigError):
        # default maximum value is 64
        Id.configure_constraints(min_length=65)

    with pytest.raises(ConfigError):
        # default maximum value cannot be less than minimum length
        Id.configure_constraints(min_length=65, max_length=40)

    org_resource = {
        "resourceType": "Organization",
        "id": "hl7",
        "name": "Health Level Seven International",
        "alias": ["HL7 International"],
        "meta": {
            "tag": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActReason",
                    "code": "HTEST",
                    "display": "test health data",
                }
            ]
        },
    }
    org_resource_copy = org_resource.copy()
    org_resource_copy["id"] = "hl7-" + "D" * 124
    with pytest.raises(ValidationError):
        Organization(**org_resource_copy)

    Id.configure_constraints(max_length=128)
    Organization(**org_resource_copy)

    string_pattern = re.compile(r"^[ \r\n\t\S]+$")
    org_resource_copy["id"] = "hl7-#€Åæø"
    with pytest.raises(ValidationError):
        # non ASCII letters are not allowed
        Organization(**org_resource_copy)

    Id.configure_constraints(regex=string_pattern)
    # now should allowed
    Organization(**org_resource_copy)

    # Restore originals
    Id.configure_constraints(**original)
