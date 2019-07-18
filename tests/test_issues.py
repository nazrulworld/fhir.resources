# _*_ coding: utf-8 _*_
import pytest

__author__ = "Md Nazrul Islam<nazrul@zitelab.dk>"

def test_issue5():
    """https://github.com/nazrulworld/fhir.resources/issues/5"""
    from fhir.resources.codeableconcept import CodeableConcept
    from fhir.resources.coding import Coding
    coding1 = Coding(jsondict={'system': 'http://www.snomed.org/', 'code': '424144002'})
    coding2 = Coding(jsondict={'system': 'https://loinc.org/', 'code': '30525-0'})

    with pytest.raises(Exception) as e_info:
        CodeableConcept(jsondict={'text': 'Age', 'coding': [coding1, coding2]})
    # Test if already solved the problem
    assert "name 'self' is not defined" not in str(e_info.value)
