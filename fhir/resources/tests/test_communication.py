# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Communication
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import communication


def impl_communication_1(inst):
    assert inst.about[0].identifier.system == "http://happyvalley.com/claim"
    assert inst.about[0].identifier.value == "12345"
    assert (
        inst.about[1].identifier.system
        == "http://www.BenefitsInc.com/fhir/claimresponse"
    )
    assert inst.about[1].identifier.value == "R3500"
    assert inst.category[0].coding[0].code == "SolicitedAttachment"
    assert inst.category[0].coding[0].system == "http://acme.org/messagetypes"
    assert inst.id == "fm-attachment"
    assert inst.identifier[0].system == "http://www.providerco.com/communication"
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.payload[0].contentAttachment.contentType == "application/pdf"
    assert inst.payload[0].contentAttachment.creation == fhirtypes.DateTime.validate(
        "2010-02-01T11:50:23-05:00"
    )
    assert inst.payload[0].contentAttachment.data == bytes_validator("SGVsbG8=")
    assert inst.payload[0].contentAttachment.title == "accident notes 20100201.pdf"
    assert inst.payload[1].contentAttachment.contentType == "application/pdf"
    assert inst.payload[1].contentAttachment.creation == fhirtypes.DateTime.validate(
        "2010-02-01T10:57:34+01:00"
    )
    assert inst.payload[1].contentAttachment.hash == bytes_validator("SGVsbG8gdGhlcmU=")
    assert inst.payload[1].contentAttachment.size == 104274
    assert inst.payload[1].contentAttachment.url == "http://example.org/docs/AB12345"
    assert inst.recipient[0].identifier.system == "http://www.jurisdiction.com/insurer"
    assert inst.recipient[0].identifier.value == "123456"
    assert (
        inst.sender.identifier.system == "http://www.jurisdiction.com/provideroffices"
    )
    assert inst.sender.identifier.value == "3456"
    assert inst.sent == fhirtypes.DateTime.validate("2016-06-12T18:01:10-08:00")
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/1"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Attachment which'
        " is unsolicited</div>"
    )
    assert inst.text.status == "generated"


def test_communication_1(base_settings):
    """No. 1 tests collection for Communication.
    Test File: communication-example-fm-attachment.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "communication-example-fm-attachment.json"
    )
    inst = communication.Communication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Communication" == inst.resource_type

    impl_communication_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Communication" == data["resourceType"]

    inst2 = communication.Communication(**data)
    impl_communication_1(inst2)


def impl_communication_2(inst):
    assert inst.basedOn[0].reference == "#request"
    assert inst.category[0].coding[0].code == "SolicitedAttachment"
    assert inst.category[0].coding[0].system == "http://acme.org/messagetypes"
    assert inst.contained[0].id == "provider"
    assert inst.contained[1].id == "payor"
    assert inst.contained[2].id == "request"
    assert inst.id == "fm-solicited"
    assert inst.identifier[0].system == "http://www.providerco.com/communication"
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.payload[0].contentAttachment.contentType == "application/pdf"
    assert inst.payload[0].contentAttachment.creation == fhirtypes.DateTime.validate(
        "2010-02-01T11:50:23-05:00"
    )
    assert inst.payload[0].contentAttachment.data == bytes_validator("SGVsbG8=")
    assert inst.payload[0].contentAttachment.title == "accident notes 20100201.pdf"
    assert inst.payload[1].contentAttachment.contentType == "application/pdf"
    assert inst.payload[1].contentAttachment.creation == fhirtypes.DateTime.validate(
        "2010-02-01T10:57:34+01:00"
    )
    assert inst.payload[1].contentAttachment.hash == bytes_validator("SGVsbG8gdGhlcmU=")
    assert inst.payload[1].contentAttachment.size == 104274
    assert (
        inst.payload[1].contentAttachment.url == "http://happyvalley.com/docs/AB12345"
    )
    assert inst.recipient[0].reference == "#payor"
    assert inst.sender.reference == "#provider"
    assert inst.sent == fhirtypes.DateTime.validate("2016-06-12T18:01:10-08:00")
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/1"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Attachment in '
        "response to a Request</div>"
    )
    assert inst.text.status == "generated"


def test_communication_2(base_settings):
    """No. 2 tests collection for Communication.
    Test File: communication-example-fm-solicited-attachment.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "communication-example-fm-solicited-attachment.json"
    )
    inst = communication.Communication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Communication" == inst.resource_type

    impl_communication_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Communication" == data["resourceType"]

    inst2 = communication.Communication(**data)
    impl_communication_2(inst2)


def impl_communication_3(inst):
    assert inst.category[0].coding[0].code == "Alert"
    assert inst.category[0].coding[0].system == "http://acme.org/messagetypes"
    assert inst.category[0].text == "Alert"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:oid:1.3.4.5.6.7"
    assert inst.identifier[0].type.text == "Paging System"
    assert inst.identifier[0].value == "2345678901"
    assert inst.instantiatesUri[0] == "http://example.org/hyperkalemia"
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
    assert inst.partOf[0].display == "Serum Potassium Observation"
    assert inst.payload[0].contentString == (
        "Patient 1 has a very high serum potassium value (7.2 mmol/L "
        "on 2014-Dec-12 at 5:55 pm)"
    )
    assert inst.payload[1].contentReference.display == "Serum Potassium Observation"
    assert inst.received == fhirtypes.DateTime.validate("2014-12-12T18:01:11-08:00")
    assert inst.recipient[0].reference == "Practitioner/example"
    assert inst.sender.reference == "Device/f001"
    assert inst.sent == fhirtypes.DateTime.validate("2014-12-12T18:01:10-08:00")
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Patient has very'
        " high serum potassium</div>"
    )
    assert inst.text.status == "generated"


def test_communication_3(base_settings):
    """No. 3 tests collection for Communication.
    Test File: communication-example.json
    """
    filename = base_settings["unittest_data_dir"] / "communication-example.json"
    inst = communication.Communication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Communication" == inst.resource_type

    impl_communication_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Communication" == data["resourceType"]

    inst2 = communication.Communication(**data)
    impl_communication_3(inst2)
