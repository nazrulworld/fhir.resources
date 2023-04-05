# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProductDispense
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import biologicallyderivedproductdispense


def impl_biologicallyderivedproductdispense_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
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
    inst = biologicallyderivedproductdispense.BiologicallyDerivedProductDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "BiologicallyDerivedProductDispense" == inst.resource_type

    impl_biologicallyderivedproductdispense_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "BiologicallyDerivedProductDispense" == data["resourceType"]

    inst2 = biologicallyderivedproductdispense.BiologicallyDerivedProductDispense(
        **data
    )
    impl_biologicallyderivedproductdispense_1(inst2)
