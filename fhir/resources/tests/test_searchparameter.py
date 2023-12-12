# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import searchparameter


def impl_searchparameter_1(inst):
    assert inst.base[0] == "Patient"
    assert inst.code == "part-agree"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == (
        "Search by url for a participation agreement, which is stored"
        " as an extension referencing a DocumentReference"
    )
    assert inst.experimental is True
    assert inst.expression == (
        "Patient.extension('http://example.org/fhir/StructureDefiniti"
        "on/participation-agreement').value"
    )
    assert inst.id == "example-extension"
    assert inst.name == "ExampleSearchParameterOnAnExtension"
    assert inst.processingMode == "normal"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "draft"
    assert inst.target[0] == "DocumentReference"
    assert inst.text.status == "generated"
    assert inst.title == "Example Search Parameter on an extension"
    assert inst.type == "reference"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/example-extension"


def test_searchparameter_1(base_settings):
    """No. 1 tests collection for SearchParameter.
    Test File: searchparameter-example-extension.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "searchparameter-example-extension.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_1(inst2)


def impl_searchparameter_2(inst):
    assert inst.base[0] == "Resource"
    assert inst.code == "_filter"
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2018-07-26")
    assert inst.description == (
        "This is the formal declaration for the _filter parameter, "
        "documented at [http://hl7.org/fhir/search_filter.html](http:"
        "//hl7.org/fhir/search_filter.html)"
    )
    assert inst.experimental is False
    assert inst.id == "filter"
    assert inst.name == "FilterSearchParameter"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.purpose == (
        "Support combination searches when the simple name=value "
        "basis of search cannot express what is required"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Filter Search Parameter"
    assert inst.type == "special"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/filter"
    assert inst.version == "1"


def test_searchparameter_2(base_settings):
    """No. 2 tests collection for SearchParameter.
    Test File: searchparameter-filter.json
    """
    filename = base_settings["unittest_data_dir"] / "searchparameter-filter.json"
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_2(inst2)


def impl_searchparameter_3(inst):
    assert inst.base[0] == "Bundle"
    assert inst.code == "example-constraint"
    assert inst.constraint == (
        "Bundle.type = 'document' and Bundle.entry[0].resource is " "Composition"
    )
    assert inst.description == "Search Composition Bundle"
    assert inst.experimental is True
    assert inst.expression == "Bundle.entry[0].resource"
    assert inst.id == "example-constraint"
    assert inst.name == "Exampleconstraint"
    assert inst.processingMode == "normal"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "draft"
    assert inst.target[0] == "Composition"
    assert inst.text.status == "generated"
    assert inst.title == "example-constraint"
    assert inst.type == "reference"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/example-constraint"


def test_searchparameter_3(base_settings):
    """No. 3 tests collection for SearchParameter.
    Test File: searchparameter-example-constraint.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "searchparameter-example-constraint.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_3(inst2)


def impl_searchparameter_4(inst):
    assert inst.base[0] == "Condition"
    assert inst.chain[0] == "name"
    assert inst.chain[1] == "identifier"
    assert inst.code == "subject"
    assert inst.contact[0].name == "[string]"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2013-10-23")
    assert inst.description == "Search by condition subject"
    assert inst.experimental is True
    assert inst.expression == "Condition.subject"
    assert inst.id == "example-reference"
    assert inst.modifier[0] == "missing"
    assert inst.name == "ExampleSearchParameter"
    assert inst.processingMode == "normal"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.purpose == "Need to search Condition by subject"
    assert inst.status == "draft"
    assert inst.target[0] == "Organization"
    assert inst.text.status == "generated"
    assert inst.title == "Example Search Parameter"
    assert inst.type == "reference"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/example-reference"


def test_searchparameter_4(base_settings):
    """No. 4 tests collection for SearchParameter.
    Test File: searchparameter-example-reference.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "searchparameter-example-reference.json"
    )
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_4(inst2)


def impl_searchparameter_5(inst):
    assert inst.base[0] == "Resource"
    assert inst.code == "_id"
    assert inst.contact[0].name == "[string]"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2013-10-23")
    assert inst.derivedFrom == "http://hl7.org/fhir/SearchParameter/Resource-id"
    assert inst.description == (
        "Search by resource identifier - e.g. same as the read "
        "interaction, but can return included resources"
    )
    assert inst.experimental is True
    assert inst.expression == "id"
    assert inst.id == "example"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.name == "IDSEARCHPARAMETER"
    assert inst.processingMode == "normal"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.purpose == (
        "Need to search by identifier for various infrastructural "
        "cases - mainly retrieving packages, and matching as part of "
        "a chain"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "I D- S E A R C H- P A R A M E T E R"
    assert inst.type == "token"
    assert inst.url == "http://hl7.org/fhir/SearchParameter/example"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "positive"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variant-state"
    )
    assert inst.version == "1"


def test_searchparameter_5(base_settings):
    """No. 5 tests collection for SearchParameter.
    Test File: searchparameter-example.json
    """
    filename = base_settings["unittest_data_dir"] / "searchparameter-example.json"
    inst = searchparameter.SearchParameter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SearchParameter" == inst.resource_type

    impl_searchparameter_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SearchParameter" == data["resourceType"]

    inst2 = searchparameter.SearchParameter(**data)
    impl_searchparameter_5(inst2)
