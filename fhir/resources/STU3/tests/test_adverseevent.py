# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import adverseevent


def impl_adverseevent_1(inst):
    assert inst.category == "AE"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-29T12:34:56+00:00")
    assert inst.description == "This was a mild rash on the left forearm"
    assert inst.id == "example"
    assert inst.identifier.system == "http://acme.com/ids/patients/risks"
    assert inst.identifier.value == "49476534"
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.seriousness.coding[0].code == "Mild"
    assert inst.seriousness.coding[0].display == "Mild"
    assert (
        inst.seriousness.coding[0].system
        == "http://hl7.org/fhir/adverse-event-seriousness"
    )
    assert inst.subject.reference == "Patient/example"
    assert inst.suspectEntity[0].instance.reference == "Medication/example"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "304386008"
    assert inst.type.coding[0].display == "O/E - itchy rash"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


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
