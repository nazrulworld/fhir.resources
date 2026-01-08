# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import terminologycapabilities
from .fixtures import ExternalValidatorModel


def impl_terminologycapabilities_1(inst):
    assert inst.codeSystem[0].content == "complete"
    assert inst.codeSystem[0].uri == "http://snomed.info/sct"
    assert (
        inst.codeSystem[0].version[0].code
        == "http://snomed.info/sct/32506021000036107/version/20220831"
    )
    assert inst.codeSystem[1].content == "complete"
    assert inst.codeSystem[1].uri == "http://loinc.org"
    assert inst.codeSystem[1].version[0].code == "2.73"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-09-01"}
        ).valueDateTime
    )
    assert inst.id == "example-terminology-server"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.6.1"
    assert inst.implementation.description == "The ACME FHIR Terminology Server"
    assert inst.kind == "instance"
    assert inst.name == "ACMETerminologyServiceTerminologyCapabilities"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/TerminologyCapabilities/terminology-server"
            }
        ).valueUri
    )


def test_terminologycapabilities_1(base_settings):
    """No. 1 tests collection for TerminologyCapabilities.
    Test File: terminologycapabilities-terminology-server.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "terminologycapabilities-terminology-server.json"
    )
    inst = terminologycapabilities.TerminologyCapabilities.model_validate_json(
        filename.read_bytes()
    )
    assert "TerminologyCapabilities" == inst.get_resource_type()

    impl_terminologycapabilities_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "TerminologyCapabilities" == data["resourceType"]

    inst2 = terminologycapabilities.TerminologyCapabilities(**data)
    impl_terminologycapabilities_1(inst2)


def impl_terminologycapabilities_2(inst):
    assert inst.codeSearch == "in-compose-or-expansion"
    assert inst.contact[0].name == "System Administrator"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "wile@acme.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2012-01-04"}
        ).valueDateTime
    )
    assert inst.description == (
        "This is the FHIR capability statement for the main EHR at "
        "ACME for the private interface - it does not describe the "
        "public interface"
    )
    assert inst.experimental is True
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.6.2"
    assert inst.implementation.description == "Acme Terminology Server"
    assert (
        inst.implementation.url
        == ExternalValidatorModel.model_validate(
            {"valueUrl": "http://example.org/tx"}
        ).valueUrl
    )
    assert inst.kind == "instance"
    assert inst.name == "ACMEEHR"
    assert inst.publisher == "ACME Corporation"
    assert inst.software.name == "TxServer"
    assert inst.software.version == "0.1.2"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "ACME EHR capability statement"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:uuid:68d043b5-9ecf-4559-a57a-396e0d452311"}
        ).valueUri
    )
    assert inst.version == "20130510"


def test_terminologycapabilities_2(base_settings):
    """No. 2 tests collection for TerminologyCapabilities.
    Test File: terminologycapabilities-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "terminologycapabilities-example.json"
    )
    inst = terminologycapabilities.TerminologyCapabilities.model_validate_json(
        filename.read_bytes()
    )
    assert "TerminologyCapabilities" == inst.get_resource_type()

    impl_terminologycapabilities_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "TerminologyCapabilities" == data["resourceType"]

    inst2 = terminologycapabilities.TerminologyCapabilities(**data)
    impl_terminologycapabilities_2(inst2)
