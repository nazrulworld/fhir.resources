# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Slot
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import slot
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_slot_1(inst):
    assert inst.comment == (
        "Assessments should be performed before requesting "
        "appointments in this slot."
    )
    assert (
        inst.end
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-25T09:15:00Z"}
        ).valueInstant
    )
    assert inst.id == "1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/identifiers/slots"}
        ).valueUri
    )
    assert inst.identifier[0].value == "123132"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.overbooked is True
    assert inst.schedule.reference == "Schedule/example"
    assert inst.serviceCategory[0].coding[0].code == "17"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert (
        inst.start
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-25T09:00:00Z"}
        ).valueInstant
    )
    assert inst.status == "busy"
    assert inst.text.status == "generated"


def test_slot_1(base_settings):
    """No. 1 tests collection for Slot.
    Test File: slot-example-busy.json
    """
    filename = base_settings["unittest_data_dir"] / "slot-example-busy.json"
    inst = slot.Slot.model_validate_json(filename.read_bytes())
    assert "Slot" == inst.get_resource_type()

    impl_slot_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Slot" == data["resourceType"]

    inst2 = slot.Slot(**data)
    impl_slot_1(inst2)


def impl_slot_2(inst):
    assert inst.appointmentType.coding[0].code == "WALKIN"
    assert (
        inst.appointmentType.coding[0].display
        == "A previously unscheduled walk-in visit"
    )
    assert (
        inst.appointmentType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0276"}
        ).valueUri
    )
    assert inst.comment == (
        "Assessments should be performed before requesting "
        "appointments in this slot."
    )
    assert (
        inst.end
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-25T09:30:00Z"}
        ).valueInstant
    )
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.schedule.reference == "Schedule/example"
    assert inst.serviceCategory[0].coding[0].code == "17"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert inst.serviceType[0].coding[0].code == "57"
    assert inst.serviceType[0].coding[0].display == "Immunization"
    assert inst.specialty[0].coding[0].code == "408480009"
    assert inst.specialty[0].coding[0].display == "Clinical immunology"
    assert (
        inst.start
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-25T09:15:00Z"}
        ).valueInstant
    )
    assert inst.status == "free"
    assert inst.text.status == "generated"


def test_slot_2(base_settings):
    """No. 2 tests collection for Slot.
    Test File: slot-example.json
    """
    filename = base_settings["unittest_data_dir"] / "slot-example.json"
    inst = slot.Slot.model_validate_json(filename.read_bytes())
    assert "Slot" == inst.get_resource_type()

    impl_slot_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Slot" == data["resourceType"]

    inst2 = slot.Slot(**data)
    impl_slot_2(inst2)


def impl_slot_3(inst):
    assert inst.comment == "Dr Careful is out of the office"
    assert (
        inst.end
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-25T09:45:00Z"}
        ).valueInstant
    )
    assert inst.id == "3"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.schedule.reference == "Schedule/example"
    assert inst.serviceCategory[0].coding[0].code == "17"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert (
        inst.start
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-25T09:30:00Z"}
        ).valueInstant
    )
    assert inst.status == "busy-unavailable"
    assert inst.text.status == "generated"


def test_slot_3(base_settings):
    """No. 3 tests collection for Slot.
    Test File: slot-example-unavailable.json
    """
    filename = base_settings["unittest_data_dir"] / "slot-example-unavailable.json"
    inst = slot.Slot.model_validate_json(filename.read_bytes())
    assert "Slot" == inst.get_resource_type()

    impl_slot_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Slot" == data["resourceType"]

    inst2 = slot.Slot(**data)
    impl_slot_3(inst2)


def impl_slot_4(inst):
    assert inst.comment == "Dr Careful is out of the office"
    assert (
        inst.end
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-25T10:00:00Z"}
        ).valueInstant
    )
    assert inst.id == "2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.schedule.reference == "Schedule/example"
    assert inst.serviceCategory[0].coding[0].code == "17"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert (
        inst.start
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2013-12-25T09:45:00Z"}
        ).valueInstant
    )
    assert inst.status == "busy-tentative"
    assert inst.text.status == "generated"


def test_slot_4(base_settings):
    """No. 4 tests collection for Slot.
    Test File: slot-example-tentative.json
    """
    filename = base_settings["unittest_data_dir"] / "slot-example-tentative.json"
    inst = slot.Slot.model_validate_json(filename.read_bytes())
    assert "Slot" == inst.get_resource_type()

    impl_slot_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Slot" == data["resourceType"]

    inst2 = slot.Slot(**data)
    impl_slot_4(inst2)
