# -*- coding: utf-8 -*-
from .. import fhirtypes  # noqa: F401
from .. import communicationrequest


def test_CommunicationRequest_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "communicationrequest-example.canonical.json"
    )
    inst = communicationrequest.CommunicationRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CommunicationRequest" == inst.resource_type
    impl_CommunicationRequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CommunicationRequest" == data["resourceType"]

    inst2 = communicationrequest.CommunicationRequest(**data)
    impl_CommunicationRequest_1(inst2)


def impl_CommunicationRequest_1(inst):
    assert (
        inst.extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/communicationrequest-orderedBy"
    )
    assert inst.extension[0].valueReference.reference == "Practitioner/example"
    assert (
        inst.extension[1].url
        == "http://hl7.org/fhir/StructureDefinition/communicationrequest-reasonRejected"
    )
    assert inst.extension[1].valueCodeableConcept.coding[0].code == "NON-AVAIL"
    assert (
        inst.extension[1].valueCodeableConcept.coding[0].display
        == "patient not-available"
    )
    assert (
        inst.extension[1].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/v3/ActReason"
    )
    assert inst.id == "communicationrequest-example"
    assert inst.status == "rejected"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == "<div>To be filled out at a later time</div>"
    assert inst.text.status == "generated"
