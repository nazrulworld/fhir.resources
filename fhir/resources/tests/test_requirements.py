# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Requirements
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import requirements
from .fixtures import ExternalValidatorModel


def impl_requirements_1(inst):
    assert inst.actor[0] == "http://hl7.org/fhir/ActorDefinition/server"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-11-02T14:31:30.239Z"}
        ).valueDateTime
    )
    assert inst.derivedFrom[0] == "http://hl7.org/fhir/Requirements/example2"
    assert inst.description == "Example Requirements Set 2"
    assert inst.id == "example2"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.18.2"
    assert inst.name == "ExampleRequirements2"
    assert inst.statement[0].conformance[0] == "SHOULD"
    assert inst.statement[0].key == "44595579-fa13-42a5-bd24-0515cde96963"
    assert inst.statement[0].label == "requirement-B1"
    assert inst.statement[0].requirement == (
        "Operations based on the SNOMED-CT should use the current "
        "version within 24 hours of each release"
    )
    assert inst.statement[0].source[0].display == "Lloyd Mackenzie"
    assert inst.statement[1].conformance[0] == "SHALL"
    assert inst.statement[1].key == "46f77dcd-d51e-4738-b61f-22506d0cb0ac"
    assert inst.statement[1].label == "requirement-2/a"
    assert inst.statement[1].source[0].display == "Robert Hausam"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Example Requirements Set 2"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Requirements/example2"}
        ).valueUri
    )


def test_requirements_1(base_settings):
    """No. 1 tests collection for Requirements.
    Test File: Requirements-example2.json
    """
    filename = base_settings["unittest_data_dir"] / "Requirements-example2.json"
    inst = requirements.Requirements.model_validate_json(filename.read_bytes())
    assert "Requirements" == inst.get_resource_type()

    impl_requirements_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Requirements" == data["resourceType"]

    inst2 = requirements.Requirements(**data)
    impl_requirements_1(inst2)


def impl_requirements_2(inst):
    assert inst.actor[0] == "http://hl7.org/fhir/ActorDefinition/server"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-11-02T14:31:30.239Z"}
        ).valueDateTime
    )
    assert inst.description == "Example Requirements Set 1"
    assert inst.id == "example1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.18.1"
    assert inst.name == "ExampleRequirements1"
    assert inst.statement[0].conformance[0] == "SHALL"
    assert inst.statement[0].key == "req-1"
    assert (
        inst.statement[0].requirement == "The server SHALL support expanding value sets"
    )
    assert (
        inst.statement[0].satisfiedBy[0]
        == ExternalValidatorModel.model_validate(
            {"valueUrl": "http://hl7.org/fhir/terminology-service.html#expand"}
        ).valueUrl
    )
    assert inst.statement[0].source[0].display == "Grahame Grieve"
    assert inst.statement[1].conformance[0] == "SHALL"
    assert inst.statement[1].key == "46f77dcd-d51e-4738-b61f-22506d0cb0ac"
    assert inst.statement[1].label == "requirement-2"
    assert inst.statement[1].requirement == (
        "Operations based on the codeSystem resource SHALL have the "
        "same result whether or not the relationships are represented"
        " explicitly as properties or implicitly using the CodeSystem"
        " resource hierarchy"
    )
    assert inst.statement[1].source[0].display == "Jose Costa Teixeira"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Example Requirements Set 1"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Requirements/example1"}
        ).valueUri
    )


def test_requirements_2(base_settings):
    """No. 2 tests collection for Requirements.
    Test File: Requirements-example1.json
    """
    filename = base_settings["unittest_data_dir"] / "Requirements-example1.json"
    inst = requirements.Requirements.model_validate_json(filename.read_bytes())
    assert "Requirements" == inst.get_resource_type()

    impl_requirements_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Requirements" == data["resourceType"]

    inst2 = requirements.Requirements(**data)
    impl_requirements_2(inst2)
