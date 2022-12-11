# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceSpecification
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import substancespecification


def impl_substancespecification_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated '
        "Narrative with Details</b></p><p><b>id</b>: "
        "example</p></div>"
    )
    assert inst.text.status == "generated"


def test_substancespecification_1(base_settings):
    """No. 1 tests collection for SubstanceSpecification.
    Test File: substancesourcematerial-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "substancesourcematerial-example.json"
    )
    inst = substancespecification.SubstanceSpecification.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstanceSpecification" == inst.resource_type

    impl_substancespecification_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstanceSpecification" == data["resourceType"]

    inst2 = substancespecification.SubstanceSpecification(**data)
    impl_substancespecification_1(inst2)


def impl_substancespecification_2(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated '
        "Narrative with Details</b></p><p><b>id</b>: "
        "example</p></div>"
    )
    assert inst.text.status == "generated"


def test_substancespecification_2(base_settings):
    """No. 2 tests collection for SubstanceSpecification.
    Test File: substanceprotein-example.json
    """
    filename = base_settings["unittest_data_dir"] / "substanceprotein-example.json"
    inst = substancespecification.SubstanceSpecification.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstanceSpecification" == inst.resource_type

    impl_substancespecification_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstanceSpecification" == data["resourceType"]

    inst2 = substancespecification.SubstanceSpecification(**data)
    impl_substancespecification_2(inst2)


def impl_substancespecification_3(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated '
        "Narrative with Details</b></p><p><b>id</b>: "
        "example</p></div>"
    )
    assert inst.text.status == "generated"


def test_substancespecification_3(base_settings):
    """No. 3 tests collection for SubstanceSpecification.
    Test File: substancepolymer-example.json
    """
    filename = base_settings["unittest_data_dir"] / "substancepolymer-example.json"
    inst = substancespecification.SubstanceSpecification.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstanceSpecification" == inst.resource_type

    impl_substancespecification_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstanceSpecification" == data["resourceType"]

    inst2 = substancespecification.SubstanceSpecification(**data)
    impl_substancespecification_3(inst2)


def impl_substancespecification_4(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated '
        "Narrative with Details</b></p><p><b>id</b>: "
        "example</p></div>"
    )
    assert inst.text.status == "generated"


def test_substancespecification_4(base_settings):
    """No. 4 tests collection for SubstanceSpecification.
    Test File: substancespecification-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "substancespecification-example.json"
    )
    inst = substancespecification.SubstanceSpecification.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstanceSpecification" == inst.resource_type

    impl_substancespecification_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstanceSpecification" == data["resourceType"]

    inst2 = substancespecification.SubstanceSpecification(**data)
    impl_substancespecification_4(inst2)


def impl_substancespecification_5(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated '
        "Narrative with Details</b></p><p><b>id</b>: "
        "example</p></div>"
    )
    assert inst.text.status == "generated"


def test_substancespecification_5(base_settings):
    """No. 5 tests collection for SubstanceSpecification.
    Test File: substancereferenceinformation-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "substancereferenceinformation-example.json"
    )
    inst = substancespecification.SubstanceSpecification.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstanceSpecification" == inst.resource_type

    impl_substancespecification_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstanceSpecification" == data["resourceType"]

    inst2 = substancespecification.SubstanceSpecification(**data)
    impl_substancespecification_5(inst2)


def impl_substancespecification_6(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated '
        "Narrative with Details</b></p><p><b>id</b>: "
        "example</p></div>"
    )
    assert inst.text.status == "generated"


def test_substancespecification_6(base_settings):
    """No. 6 tests collection for SubstanceSpecification.
    Test File: substancenucleicacid-example.json
    """
    filename = base_settings["unittest_data_dir"] / "substancenucleicacid-example.json"
    inst = substancespecification.SubstanceSpecification.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstanceSpecification" == inst.resource_type

    impl_substancespecification_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstanceSpecification" == data["resourceType"]

    inst2 = substancespecification.SubstanceSpecification(**data)
    impl_substancespecification_6(inst2)
