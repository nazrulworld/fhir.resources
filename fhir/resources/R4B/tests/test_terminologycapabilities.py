# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import terminologycapabilities
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_terminologycapabilities_1(inst):
    assert inst.codeSearch == "explicit"
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
    assert inst.implementation.description == "Acme Terminology Server"
    assert (
        inst.implementation.url
        == ExternalValidatorModel.model_validate(
            {"valueUrl": "http://example.org/tx"}
        ).valueUrl
    )
    assert inst.kind == "instance"
    assert inst.name == "ACME-EHR"
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


def test_terminologycapabilities_1(base_settings):
    """No. 1 tests collection for TerminologyCapabilities.
    Test File: terminologycapabilities-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "terminologycapabilities-example.json"
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
