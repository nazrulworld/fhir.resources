# _*_ coding: utf-8 _*_
from pydantic import ValidationError

from fhir.resources.patient import Patient

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


def test_issue_74():
    """When are Falsy values evaluated as None?"""
    patient = Patient(active=True, address=[])
    assert "address" not in patient.dict()
    assert patient.dict(exclude_none=False)["address"] == []


def test_issue_64():
    """Allow empty string """
    try:
        Patient(
            active=True,
            address=[
                {
                    "use": "old",
                    "line": ["100 LaSalle St", ""],
                    "city": "Chicago",
                    "district": "Cook",
                    "state": "IL",
                    "postalCode": "60606",
                    "country": "USA",
                }
            ],
        )
        assert 1 == 2, "Code should not come here, because of empty string validation"
    except ValidationError:
        # should raise validation error
        assert 1 == 1
    from fhir.resources.fhirtypes import String

    String.configure_empty_str(allow=True)
    try:
        Patient(
            active=True,
            address=[
                {
                    "use": "old",
                    "line": ["100 LaSalle St", ""],
                    "city": "Chicago",
                    "district": "Cook",
                    "state": "IL",
                    "postalCode": "60606",
                    "country": "USA",
                }
            ],
        )
        assert 1 == 1
    except ValidationError:
        # should not raise validation error
        assert 1 == 2, "Code should not come here, we allow empty string"
    String.configure_empty_str(allow=False)
