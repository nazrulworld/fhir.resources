# _*_ coding: utf-8 _*_
from pydantic import ValidationError
from pydantic.errors import UrlSchemeError
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


def test_issue_97():
    """Test Report HAPI
    1.) if primitive field/value is missing, extension ignored
    2.) List str/str if one string multiple extension it could be list of all
    3.) if more none values in list string, none member removed corosponding number of extension

    """
    from fhir.resources.organization import Organization

    data = {
        "resourceType": "Organization",
        "address": [
            {
                "line": [None],
                "_line": [
                    {
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber",
                                "valueString": "80",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-streetNameType",
                                "valueString": "AV",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-streetNameBase",
                                "valueString": "FOOBAR",
                            },
                        ]
                    },
                    {
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber",
                                "valueString": "180",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-streetNameType",
                                "valueString": "AV9",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-streetNameBase",
                                "valueString": "FOOBAR90",
                            },
                        ]
                    },
                ],
            }
        ],
    }
    org = Organization(**data)

    assert org.dict()["address"][0]["line"] == [None]
    assert '"line":[null]' in org.json()
    assert Organization.parse_raw(org.json(return_bytes=True)).dict() == data
    assert "line:\n  - null\n" in org.yaml()
    assert (
        Organization.parse_raw(
            org.yaml(return_bytes=True), content_type="text/yaml"
        ).dict()
        == data
    )
    org.xml()


def test_issue_100():
    """https://github.com/nazrulworld/fhir.resources/issues/100"""
    from fhir.resources.attachment import Attachment
    from fhir.resources.fhirtypes import Url
    from fhir.resources.STU3.fhirtypes import Url as STU3Url

    Url.validate(
        "https://www.google.dk/main/page.html?6",
        Attachment.__fields__["url"],
        Attachment.__config__,
    )
    try:
        Url.validate(
            "https//www.google.dk/main/page.html?6",
            Attachment.__fields__["url"],
            Attachment.__config__,
        )
        raise AssertionError("Code should not come here.")
    except UrlSchemeError:
        pass

    try:
        Url.validate(
            "//home.saxo/main/page.html?6",
            Attachment.__fields__["url"],
            Attachment.__config__,
        )
        raise AssertionError("Code should not come here.")
    except UrlSchemeError:
        pass

    data = {
        "contentType": "text/plain",
        "url": "/Binary/1-note",
        "title": "Uri where the data can be found: [base]/Binary/1-note",
    }
    try:
        Attachment(**data)
    except ValidationError:
        raise AssertionError("Code should not come here.")


def test_issue101():
    """ """
    from fhir.resources.element import Element
    from fhir.resources.STU3.element import Element as STU3Element
    from fhir.resources.resource import Resource
    from fhir.resources.STU3.resource import Resource as STU3Resource

    data = {
        "id": "001",
        "extension": [
            {
                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber",
                "valueString": "180",
            }
        ],
    }
    data3 = {
        "id": "001",
        "resourceType": "Resource",
        "_language": {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber",
                    "valueString": "180",
                }
            ]
        },
    }
    el = Element(**data)
    assert data == el.dict()

    res = Resource(**data3)
    assert data3 == res.dict()

    el = STU3Element(**data)
    assert data == el.dict()

    data2 = {
        "id": "001",
        "_id": {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber",
                    "valueString": "180",
                }
            ]
        },
    }
    try:
        Element(**data2)
        raise AssertionError("Code should not come here.")
    except ValidationError:
        pass

    try:
        STU3Element(**data2)
        raise AssertionError("Code should not come here.")
    except ValidationError:
        pass

    data4 = {
        "id": "001",
        "resourceType": "Resource",
        "_id": {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber",
                    "valueString": "180",
                }
            ]
        },
    }

    try:
        STU3Resource(**data4)
        raise AssertionError("Code should not come here.")
    except ValidationError:
        pass
