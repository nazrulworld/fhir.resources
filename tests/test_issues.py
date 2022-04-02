# _*_ coding: utf-8 _*_
from pydantic import ValidationError

from fhir.resources.patient import Patient
from fhir.resources.period import Period

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


def test_issue_74():
    """When are Falsy values evaluated as None?"""
    patient = Patient(active=True, address=[])
    assert "address" not in patient.dict()
    assert patient.dict(exclude_none=False)["address"] == []


def test_issue_64():
    """Allow empty string"""
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


def test_issue_96():
    """YAML datetime serialization"""
    from datetime import datetime

    pd = Period(
        end=datetime(2022, 3, 29, 11, 48, 37, 482248),
        start=datetime(2022, 3, 28, 23, 48, 37, 481725),
    )
    assert "2022-03-28T23:48:37.481725" in pd.yaml()
    try:
        "2022-03-28T23:48:37.481725" in Period.parse_raw(
            pd.yaml(), content_type="text/yaml"
        ).json()
    except ValidationError:
        raise AssertionError("Code should not come here")
