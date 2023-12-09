# -*- coding: utf-8 -*-
from pydantic.v1.datetime_parse import parse_datetime

from .. import fhirtypes  # noqa: F401
from .. import communication


def test_Communication_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "communication-example.canonical.json"
    )
    inst = communication.Communication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Communication" == inst.resource_type
    impl_Communication_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Communication" == data["resourceType"]

    inst2 = communication.Communication(**data)
    impl_Communication_1(inst2)


def impl_Communication_1(inst):
    assert inst.category.coding[0].code == "Alert"
    assert inst.category.coding[0].system == "http://acme.org/messagetypes"
    assert inst.category.text == "Alert"
    assert (
        inst.extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/communication-reasonNotPerformed"
    )
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "EIE"
    assert (
        inst.extension[0].valueCodeableConcept.coding[0].display == "entered in error"
    )
    assert (
        inst.extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/v3/ActReason"
    )
    assert inst.id == "communication-example"
    assert inst.identifier[0].system == "urn:oid:1.3.4.5.6.7"
    assert inst.identifier[0].type.text == "Paging System"
    assert inst.identifier[0].value == "2345678901"
    assert (
        inst.payload[0].contentString
        == "Patient 1 has a very high serum potassium value (7.2 mmol/L on 2014-Dec-12 at 5:55 pm)"
    )
    assert inst.payload[1].contentReference.reference == "Observation/643666aa12f"
    assert inst.recipient[0].reference == "Practitioner/21"
    assert inst.sender.reference == "Device/f001"
    assert inst.sent == parse_datetime("2014-12-12T18:01:10-08:00")
    assert inst.status == "suspended"
    assert inst.subject.reference == "Patient/1"
    assert inst.text.div == "<div>Patient has very high serum potassium</div>"
    assert inst.text.status == "generated"
