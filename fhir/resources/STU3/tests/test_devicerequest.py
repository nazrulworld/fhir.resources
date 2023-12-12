# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import devicerequest


def impl_devicerequest_1(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2013-05-08T09:33:27+07:00")
    assert inst.basedOn[0].display == "Homecare - DM follow-up"
    assert inst.codeCodeableConcept.coding[0].code == "43148-6"
    assert inst.codeCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.codeCodeableConcept.text == "Insulin delivery device panel"
    assert inst.context.display == "Encounter 1"
    assert inst.definition[0].display == "DM ambulatory protocol II"
    assert inst.groupIdentifier.value == "ip_request1"
    assert inst.id == "insulinpump"
    assert inst.identifier[0].value == "ip_request1.1"
    assert inst.intent.text == "instance-order"
    assert inst.note[0].text == "this is the right device brand and model"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2013-05-08T09:33:27+07:00"
    )
    assert inst.performer.display == "Nurse Rossignol"
    assert inst.performerType.coding[0].display == "Qualified nurse"
    assert inst.performerType.text == "Nurse"
    assert inst.priorRequest[0].display == "CGM ambulatory"
    assert inst.priority == "routine"
    assert inst.reasonCode[0].text == "gastroparesis"
    assert inst.reasonReference[0].display == "Gastroparesis"
    assert inst.relevantHistory[0].display == "Request for unspecified device"
    assert inst.requester.agent.display == "Dr. Adam Careful"
    assert inst.requester.agent.reference == "Practitioner/example"
    assert inst.requester.onBehalfOf.reference == "Organization/2.16.840.1.113883.19.5"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/dicom"
    assert inst.supportingInfo[0].display == "Previous results"
    assert inst.text.status == "generated"


def test_devicerequest_1(base_settings):
    """No. 1 tests collection for DeviceRequest.
    Test File: devicerequest-example-insulinpump.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "devicerequest-example-insulinpump.json"
    )
    inst = devicerequest.DeviceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceRequest" == inst.resource_type

    impl_devicerequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceRequest" == data["resourceType"]

    inst2 = devicerequest.DeviceRequest(**data)
    impl_devicerequest_1(inst2)


def impl_devicerequest_2(inst):
    assert inst.codeReference.reference == "Device/example"
    assert inst.id == "example"
    assert inst.intent.coding[0].code == "original-order"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_devicerequest_2(base_settings):
    """No. 2 tests collection for DeviceRequest.
    Test File: devicerequest-example.json
    """
    filename = base_settings["unittest_data_dir"] / "devicerequest-example.json"
    inst = devicerequest.DeviceRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceRequest" == inst.resource_type

    impl_devicerequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceRequest" == data["resourceType"]

    inst2 = devicerequest.DeviceRequest(**data)
    impl_devicerequest_2(inst2)
