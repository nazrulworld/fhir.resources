# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Group
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import group
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_group_1(inst):
    assert inst.actual is True
    assert inst.characteristic[0].code.text == "gender"
    assert inst.characteristic[0].exclude is False
    assert inst.characteristic[0].valueCodeableConcept.text == "mixed"
    assert inst.characteristic[1].code.text == "owner"
    assert inst.characteristic[1].exclude is False
    assert inst.characteristic[1].valueCodeableConcept.text == "John Smith"
    assert inst.code.text == "Horse"
    assert inst.id == "101"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://someveterinarianclinic.org/fhir/NamingSystem/herds"}
        ).valueUri
    )
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "John's herd"
    assert inst.quantity == 25
    assert inst.text.status == "additional"
    assert inst.type == "animal"


def test_group_1(base_settings):
    """No. 1 tests collection for Group.
    Test File: group-example.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example.json"
    inst = group.Group.model_validate_json(filename.read_bytes())
    assert "Group" == inst.get_resource_type()

    impl_group_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_1(inst2)


def impl_group_2(inst):
    assert inst.actual is True
    assert inst.id == "102"
    assert inst.member[0].entity.reference == "Patient/pat1"
    assert (
        inst.member[0].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-10-08"}
        ).valueDateTime
    )
    assert inst.member[1].entity.reference == "Patient/pat2"
    assert inst.member[1].inactive is True
    assert (
        inst.member[1].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-04-02"}
        ).valueDateTime
    )
    assert inst.member[2].entity.reference == "Patient/pat3"
    assert (
        inst.member[2].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-08-06"}
        ).valueDateTime
    )
    assert inst.member[3].entity.reference == "Patient/pat4"
    assert (
        inst.member[3].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-08-06"}
        ).valueDateTime
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.text.status == "additional"
    assert inst.type == "person"


def test_group_2(base_settings):
    """No. 2 tests collection for Group.
    Test File: group-example-member.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example-member.json"
    inst = group.Group.model_validate_json(filename.read_bytes())
    assert "Group" == inst.get_resource_type()

    impl_group_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_2(inst2)


def impl_group_3(inst):
    assert inst.actual is True
    assert inst.characteristic[0].code.coding[0].code == "attributed-to"
    assert (
        inst.characteristic[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org"}
        ).valueUri
    )
    assert inst.characteristic[0].code.text == "Patients primarily attributed to"
    assert inst.characteristic[0].exclude is False
    assert inst.characteristic[0].valueReference.reference == "Practitioner/123"
    assert inst.id == "example-patientlist"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.text.status == "additional"
    assert inst.type == "person"


def test_group_3(base_settings):
    """No. 3 tests collection for Group.
    Test File: group-example-patientlist.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example-patientlist.json"
    inst = group.Group.model_validate_json(filename.read_bytes())
    assert "Group" == inst.get_resource_type()

    impl_group_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_3(inst2)


def impl_group_4(inst):
    assert inst.active is True
    assert inst.actual is True
    assert inst.characteristic[0].code.text == "gender"
    assert inst.characteristic[0].exclude is False
    assert inst.characteristic[0].valueCodeableConcept.text == "female"
    assert inst.code.coding[0].code == "388393002"
    assert inst.code.coding[0].display == "Genus Sus (organism)"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.code.coding[1].code == "POR"
    assert inst.code.coding[1].display == "porcine"
    assert (
        inst.code.coding[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.aphis.usda.gov"}
        ).valueUri
    )
    assert inst.code.text == "Porcine"
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/fhir/StructureDefinition/owner"}
        ).valueUri
    )
    assert inst.extension[0].valueReference.display == "Peter Chalmers"
    assert inst.extension[0].valueReference.reference == "RelatedPerson/peter"
    assert inst.id == "herd1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://vetmed.iastate.edu/vdl"}
        ).valueUri
    )
    assert inst.identifier[0].value == "20171120-1234"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Breeding herd"
    assert inst.quantity == 2500
    assert inst.text.status == "generated"
    assert inst.type == "animal"


def test_group_4(base_settings):
    """No. 4 tests collection for Group.
    Test File: group-example-herd1.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example-herd1.json"
    inst = group.Group.model_validate_json(filename.read_bytes())
    assert "Group" == inst.get_resource_type()

    impl_group_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_4(inst2)
