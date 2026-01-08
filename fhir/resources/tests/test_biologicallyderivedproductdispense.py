# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProductDispense
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import biologicallyderivedproductdispense
from .fixtures import ExternalValidatorModel


def impl_biologicallyderivedproductdispense_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.patient.display == "Donald Duck"
    assert inst.patient.reference == "Patient/pat1"
    assert inst.product.reference == "BiologicallyDerivedProduct/prod1"
    assert inst.status == "allocated"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_biologicallyderivedproductdispense_1(base_settings):
    """No. 1 tests collection for BiologicallyDerivedProductDispense.
    Test File: biologicallyderivedproductdispense-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "biologicallyderivedproductdispense-example.json"
    )
    inst = biologicallyderivedproductdispense.BiologicallyDerivedProductDispense.model_validate_json(
        filename.read_bytes()
    )
    assert "BiologicallyDerivedProductDispense" == inst.get_resource_type()

    impl_biologicallyderivedproductdispense_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "BiologicallyDerivedProductDispense" == data["resourceType"]

    inst2 = biologicallyderivedproductdispense.BiologicallyDerivedProductDispense(
        **data
    )
    impl_biologicallyderivedproductdispense_1(inst2)
