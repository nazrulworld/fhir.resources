# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EventDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import eventdefinition
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_eventdefinition_1(inst):
    assert inst.experimental is True
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.purpose == "Monitor all admissions to Emergency"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.trigger[0].condition.description == (
        "Encounter Location = emergency (active/completed encounters,"
        " current or previous)"
    )
    assert inst.trigger[0].condition.expression == (
        "(this | %previous).location.where(location = "
        "'Location/emergency' and status in {'active', "
        "'completed'}).exists()"
    )
    assert inst.trigger[0].condition.language == "text/fhirpath"
    assert inst.trigger[0].data[0].type == "Encounter"
    assert inst.trigger[0].name == "monitor-emergency-admissions"
    assert inst.trigger[0].type == "named-event"


def test_eventdefinition_1(base_settings):
    """No. 1 tests collection for EventDefinition.
    Test File: eventdefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "eventdefinition-example.json"
    inst = eventdefinition.EventDefinition.model_validate_json(filename.read_bytes())
    assert "EventDefinition" == inst.get_resource_type()

    impl_eventdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EventDefinition" == data["resourceType"]

    inst2 = eventdefinition.EventDefinition(**data)
    impl_eventdefinition_1(inst2)
