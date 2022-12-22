# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import communicationrequest


def impl_communicationrequest_1(inst):
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">To be filled out'
        " at a later time</div>"
    )
    assert inst.text.status == "generated"


def test_communicationrequest_1(base_settings):
    """No. 1 tests collection for CommunicationRequest.
    Test File: communicationrequest-example.json
    """
    filename = base_settings["unittest_data_dir"] / "communicationrequest-example.json"
    inst = communicationrequest.CommunicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CommunicationRequest" == inst.resource_type

    impl_communicationrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CommunicationRequest" == data["resourceType"]

    inst2 = communicationrequest.CommunicationRequest(**data)
    impl_communicationrequest_1(inst2)


def impl_communicationrequest_2(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-06-10T11:01:10-08:00")
    assert inst.basedOn[0].display == "EligibilityRequest"
    assert inst.category[0].coding[0].code == "SolicitedAttachmentRequest"
    assert inst.category[0].coding[0].system == "http://acme.org/messagetypes"
    assert inst.contained[0].id == "provider"
    assert inst.contained[1].id == "payor"
    assert inst.contained[2].id == "requester"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.groupIdentifier.value == "12345"
    assert inst.id == "fm-solicit"
    assert inst.identifier[0].system == "http://www.jurisdiction.com/insurer/123456"
    assert inst.identifier[0].value == "ABC123"
    assert inst.medium[0].coding[0].code == "WRITTEN"
    assert inst.medium[0].coding[0].display == "written"
    assert (
        inst.medium[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ParticipationMode"
    )
    assert inst.medium[0].text == "written"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2016-06-10T11:01:10-08:00"
    )
    assert inst.payload[0].contentString == (
        "Please provide the accident report and any associated "
        "pictures to support your Claim# DEF5647."
    )
    assert inst.priority == "routine"
    assert inst.recipient[0].reference == "#provider"
    assert inst.replaces[0].display == "prior CommunicationRequest"
    assert inst.requester.reference == "#requester"
    assert inst.sender.reference == "#payor"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Request for ' "Accident Report</div>"
    )
    assert inst.text.status == "generated"


def test_communicationrequest_2(base_settings):
    """No. 2 tests collection for CommunicationRequest.
    Test File: communicationrequest-example-fm-solicit-attachment.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "communicationrequest-example-fm-solicit-attachment.json"
    )
    inst = communicationrequest.CommunicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CommunicationRequest" == inst.resource_type

    impl_communicationrequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CommunicationRequest" == data["resourceType"]

    inst2 = communicationrequest.CommunicationRequest(**data)
    impl_communicationrequest_2(inst2)
