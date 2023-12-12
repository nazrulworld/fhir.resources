# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceProtein
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import substanceprotein


def impl_substanceprotein_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_substanceprotein_1(base_settings):
    """No. 1 tests collection for SubstanceProtein.
    Test File: substanceprotein-example.json
    """
    filename = base_settings["unittest_data_dir"] / "substanceprotein-example.json"
    inst = substanceprotein.SubstanceProtein.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstanceProtein" == inst.resource_type

    impl_substanceprotein_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstanceProtein" == data["resourceType"]

    inst2 = substanceprotein.SubstanceProtein(**data)
    impl_substanceprotein_1(inst2)
