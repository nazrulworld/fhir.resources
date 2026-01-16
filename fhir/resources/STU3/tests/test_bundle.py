# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from .. import bundle
from .conftest import ExternalValidatorModel


def impl_bundle_1(inst):
    assert (
        inst.entry[0].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-sct"}
        ).valueUri
    )
    assert inst.entry[0].resource.id == "tx-sct"
    assert (
        inst.entry[1].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-rxnorm"}
        ).valueUri
    )
    assert inst.entry[1].resource.id == "tx-rxnorm"
    assert (
        inst.entry[2].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-loinc"}
        ).valueUri
    )
    assert inst.entry[2].resource.id == "tx-loinc"
    assert (
        inst.entry[3].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-ucum"}
        ).valueUri
    )
    assert inst.entry[3].resource.id == "tx-ucum"
    assert (
        inst.entry[4].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-nci"}
        ).valueUri
    )
    assert inst.entry[4].resource.id == "tx-nci"
    assert (
        inst.entry[5].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-cpt"}
        ).valueUri
    )
    assert inst.entry[5].resource.id == "tx-cpt"
    assert (
        inst.entry[6].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-ndf-rt"}
        ).valueUri
    )
    assert inst.entry[6].resource.id == "tx-ndf-rt"
    assert (
        inst.entry[7].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-unii"}
        ).valueUri
    )
    assert inst.entry[7].resource.id == "tx-unii"
    assert (
        inst.entry[8].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-ndc"}
        ).valueUri
    )
    assert inst.entry[8].resource.id == "tx-ndc"
    assert (
        inst.entry[9].fullUrl
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/tx-cvx"}
        ).valueUri
    )
    assert inst.entry[9].resource.id == "tx-cvx"
    assert inst.id == "terminologies"
    assert inst.type == "collection"


def test_bundle_1(base_settings):
    """No. 1 tests collection for Bundle.
    Test File: bundle-namingsystem-terminologies(terminologies).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "bundle-namingsystem-terminologies(terminologies).json"
    )
    inst = bundle.Bundle.model_validate_json(filename.read_bytes())
    assert "Bundle" == inst.get_resource_type()

    impl_bundle_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_1(inst2)
