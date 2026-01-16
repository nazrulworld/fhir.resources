# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from .. import searchparameter
from .conftest import ExternalValidatorModel


def impl_searchparameter_1(inst):
    assert inst.code == "effective"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.id == "valueset-extensions-ValueSet-effective"
    assert inst.name == "effective"
    assert inst.status == "draft"
    assert inst.type == "date"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/valueset-extensions-ValueSet-effective"
            }
        ).valueUri
    )
    assert inst.xpath == (
        "f:ValueSet/f:extension[@url='http://hl7.org/fhir/StructureDe"
        "finition/valueset-effectiveDate'] | /f:#effectiveDate"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_1(base_settings):
    """No. 1 tests collection for SearchParameter.
    Test File: searchparameter-valueset-extensions-ValueSet-effective.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-valueset-extensions-ValueSet-effective.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_1(inst2)


def impl_searchparameter_2(inst):
    assert inst.base[0] == "Observation"
    assert inst.code == "dna-variant"
    assert inst.description == "HGVS DNA variant"
    assert inst.experimental is True
    assert inst.id == "observation-genetic-Observation-dna-variant"
    assert inst.name == "dna-variant"
    assert inst.status == "draft"
    assert inst.type == "string"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/observation-genetic-Observation-dna-variant"
            }
        ).valueUri
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_2(base_settings):
    """No. 2 tests collection for SearchParameter.
    Test File: searchparameter-observation-genetic-Observation-dna-variant.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-observation-genetic-Observation-dna-variant.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_2(inst2)


def impl_searchparameter_3(inst):
    assert inst.base[0] == "Observation"
    assert inst.code == "gene-dnavariant"
    assert inst.description == "HGNC gene symbol and HGVS DNA Variant"
    assert inst.experimental is True
    assert inst.id == "observation-genetic-Observation-gene-dnavariant"
    assert inst.name == "gene-dnavariant"
    assert inst.status == "draft"
    assert inst.type == "string"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/observation-genetic-Observation-gene-dnavariant"
            }
        ).valueUri
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_3(base_settings):
    """No. 3 tests collection for SearchParameter.
    Test File: searchparameter-observation-genetic-Observation-gene-dnavariant.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-observation-genetic-Observation-gene-dnavariant.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_3(inst2)


def impl_searchparameter_4(inst):
    assert inst.code == "alias"
    assert inst.description == "Include Locations that contain the provided alias"
    assert inst.experimental is True
    assert inst.id == "location-extensions-Location-alias"
    assert inst.name == "alias"
    assert inst.status == "draft"
    assert inst.type == "string"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/location-extensions-Location-alias"
            }
        ).valueUri
    )
    assert inst.xpath == (
        "f:Location/f:extension[@url='http://hl7.org/fhir/StructureDe"
        "finition/location-alias'] | /f:#alias"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_4(base_settings):
    """No. 4 tests collection for SearchParameter.
    Test File: searchparameter-location-extensions-Location-alias.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-location-extensions-Location-alias.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_4(inst2)


def impl_searchparameter_5(inst):
    assert inst.base[0] == "Condition"
    assert inst.code == "definition"
    assert inst.description == "Matches on the definition extension value"
    assert inst.experimental is True
    assert inst.id == "condition-extensions-Condition-definition"
    assert inst.name == "definition"
    assert inst.status == "draft"
    assert inst.type == "reference"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/condition-extensions-Condition-definition"
            }
        ).valueUri
    )
    assert inst.xpath == (
        "f:Condition/f:extension[@url='http://hl7.org/fhir/StructureD"
        "efinition/condition-definition'] | f:Condition/f:extension[@"
        "url='http://hl7.org/fhir/StructureDefinition/condition-"
        "definition']"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_5(base_settings):
    """No. 5 tests collection for SearchParameter.
    Test File: searchparameter-condition-extensions-Condition-definition.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-condition-extensions-Condition-definition.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_5(inst2)


def impl_searchparameter_6(inst):
    assert inst.code == "author"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.id == "codesystem-extensions-CodeSystem-author"
    assert inst.name == "author"
    assert inst.status == "draft"
    assert inst.type == "string"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/codesystem-extensions-CodeSystem-author"
            }
        ).valueUri
    )
    assert inst.xpath == (
        "f:CodeSystem/f:extension[@url='http://hl7.org/fhir/Structure"
        "Definition/codesystem-author'] | /f:#author"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_6(base_settings):
    """No. 6 tests collection for SearchParameter.
    Test File: searchparameter-codesystem-extensions-CodeSystem-author.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-codesystem-extensions-CodeSystem-author.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_6(inst2)


def impl_searchparameter_7(inst):
    assert inst.code == "end"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.id == "codesystem-extensions-CodeSystem-end"
    assert inst.name == "end"
    assert inst.status == "draft"
    assert inst.type == "date"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/codesystem-extensions-CodeSystem-end"
            }
        ).valueUri
    )
    assert inst.xpath == (
        "f:CodeSystem/f:extension[@url='http://hl7.org/fhir/Structure"
        "Definition/codesystem-expirationDate'] | /f:#expirationDate"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_7(base_settings):
    """No. 7 tests collection for SearchParameter.
    Test File: searchparameter-codesystem-extensions-CodeSystem-end.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-codesystem-extensions-CodeSystem-end.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_7(inst2)


def impl_searchparameter_8(inst):
    assert inst.code == "effective"
    assert inst.description == "Optional Extensions Element"
    assert inst.experimental is True
    assert inst.id == "codesystem-extensions-CodeSystem-effective"
    assert inst.name == "effective"
    assert inst.status == "draft"
    assert inst.type == "date"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/codesystem-extensions-CodeSystem-effective"
            }
        ).valueUri
    )
    assert inst.xpath == (
        "f:CodeSystem/f:extension[@url='http://hl7.org/fhir/Structure"
        "Definition/codesystem-effectiveDate'] | /f:#effectiveDate"
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_8(base_settings):
    """No. 8 tests collection for SearchParameter.
    Test File: searchparameter-codesystem-extensions-CodeSystem-effective.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-codesystem-extensions-CodeSystem-effective.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_8(inst2)


def impl_searchparameter_9(inst):
    assert inst.base[0] == "Observation"
    assert inst.code == "amino-acid-change"
    assert inst.description == "HGVS Protein Change"
    assert inst.experimental is True
    assert inst.id == "observation-genetic-Observation-amino-acid-change"
    assert inst.name == "amino-acid-change"
    assert inst.status == "draft"
    assert inst.type == "string"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/observation-genetic-Observation-amino-acid-change"
            }
        ).valueUri
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_9(base_settings):
    """No. 9 tests collection for SearchParameter.
    Test File: searchparameter-observation-genetic-Observation-amino-acid-change.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-observation-genetic-Observation-amino-acid-change.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_9(inst2)


def impl_searchparameter_10(inst):
    assert inst.base[0] == "DiagnosticReport"
    assert inst.code == "assessed-condition"
    assert inst.description == "Condition assessed by genetic test"
    assert inst.experimental is True
    assert inst.id == "diagnosticreport-genetic-DiagnosticReport-assessed-condition"
    assert inst.name == "assessed-condition"
    assert inst.status == "draft"
    assert inst.type == "reference"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/diagnosticreport-genetic-DiagnosticReport-assessed-condition"
            }
        ).valueUri
    )
    assert inst.xpathUsage == "normal"


def test_searchparameter_10(base_settings):
    """No. 10 tests collection for SearchParameter.
    Test File: searchparameter-diagnosticreport-genetic-DiagnosticReport-assessed-condition.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "searchparameter-diagnosticreport-genetic-DiagnosticReport-assessed-condition.json"
    )
    inst = searchparameter.SearchParameter.model_validate_json(filename.read_bytes())
    assert "SearchParameter" == inst.get_resource_type()

    impl_searchparameter_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_10(inst2)
