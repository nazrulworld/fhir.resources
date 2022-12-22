# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import adverseevent


def impl_adverseevent_1(inst):
    assert inst.actuality == "actual"
    assert inst.category[0].coding[0].code == "product-use-error"
    assert inst.category[0].coding[0].display == "Product Use Error"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/adverse-event-category"
    )
    assert inst.date == fhirtypes.DateTime.validate("2017-01-29T12:34:56+00:00")
    assert inst.event.coding[0].code == "304386008"
    assert inst.event.coding[0].display == "O/E - itchy rash"
    assert inst.event.coding[0].system == "http://snomed.info/sct"
    assert inst.event.text == "This was a mild rash on the left forearm"
    assert inst.id == "example"
    assert inst.identifier.system == "http://acme.com/ids/patients/risks"
    assert inst.identifier.value == "49476534"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.seriousness.coding[0].code == "Non-serious"
    assert inst.seriousness.coding[0].display == "Non-serious"
    assert inst.seriousness.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/adverse-event-" "seriousness"
    )
    assert inst.severity.coding[0].code == "mild"
    assert inst.severity.coding[0].display == "Mild"
    assert (
        inst.severity.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/adverse-event-severity"
    )
    assert inst.subject.reference == "Patient/example"
    assert inst.suspectEntity[0].instance.reference == "Medication/example"
    assert inst.text.status == "generated"


def test_adverseevent_1(base_settings):
    """No. 1 tests collection for AdverseEvent.
    Test File: adverseevent-example.json
    """
    filename = base_settings["unittest_data_dir"] / "adverseevent-example.json"
    inst = adverseevent.AdverseEvent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AdverseEvent" == inst.resource_type

    impl_adverseevent_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AdverseEvent" == data["resourceType"]

    inst2 = adverseevent.AdverseEvent(**data)
    impl_adverseevent_1(inst2)
