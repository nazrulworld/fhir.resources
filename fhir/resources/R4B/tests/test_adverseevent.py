# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import adverseevent
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_adverseevent_1(inst):
    assert inst.actuality == "actual"
    assert inst.category[0].coding[0].code == "product-use-error"
    assert inst.category[0].coding[0].display == "Product Use Error"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/adverse-event-category"}
        ).valueUri
    )
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2017-01-29T12:34:56+00:00"}
        ).valueDateTime
    )
    assert inst.event.coding[0].code == "304386008"
    assert inst.event.coding[0].display == "O/E - itchy rash"
    assert (
        inst.event.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.event.text == "This was a mild rash on the left forearm"
    assert inst.id == "example"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/ids/patients/risks"}
        ).valueUri
    )
    assert inst.identifier.value == "49476534"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.seriousness.coding[0].code == "Non-serious"
    assert inst.seriousness.coding[0].display == "Non-serious"
    assert (
        inst.seriousness.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/adverse-event-seriousness"
            }
        ).valueUri
    )
    assert inst.severity.coding[0].code == "mild"
    assert inst.severity.coding[0].display == "Mild"
    assert (
        inst.severity.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/adverse-event-severity"}
        ).valueUri
    )
    assert inst.subject.reference == "Patient/example"
    assert inst.suspectEntity[0].instance.reference == "Medication/example"
    assert inst.text.status == "generated"


def test_adverseevent_1(base_settings):
    """No. 1 tests collection for AdverseEvent.
    Test File: adverseevent-example.json
    """
    filename = base_settings["unittest_data_dir"] / "adverseevent-example.json"
    inst = adverseevent.AdverseEvent.model_validate_json(filename.read_bytes())
    assert "AdverseEvent" == inst.get_resource_type()

    impl_adverseevent_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "AdverseEvent" == data["resourceType"]

    inst2 = adverseevent.AdverseEvent(**data)
    impl_adverseevent_1(inst2)
