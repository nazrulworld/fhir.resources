# _*_ coding: utf-8 _*_
from fhir.resources.patient import Patient
__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


def test_issue_74():
    """When are Falsy values evaluated as None?"""
    patient = Patient(active=True, address=[])
    assert "address" not in patient.dict()
    assert patient.dict(exclude_none=False)["address"] == []
