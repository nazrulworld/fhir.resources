# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Transport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import transport


def impl_transport_1(inst):
    assert inst.basedOn[0].reference == "SupplyRequest/simpleorder"
    assert inst.currentLocation.display == "Current location for item at Lab A"
    assert inst.currentLocation.reference == "Transport/location-labA"
    assert inst.id == "simpledelivery"
    assert inst.identifier[0].value == "Transport1234"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.partOf[0].display == "Central Supply Restock"
    assert (
        inst.requestedLocation.display
        == "Requested location for item at City Hospital Lab"
    )
    assert inst.requestedLocation.reference == "Transport/location-hospitalLab"
    assert inst.status == "completed"
    assert inst.text.status == "generated"


def test_transport_1(base_settings):
    """No. 1 tests collection for Transport.
    Test File: transport-example.json
    """
    filename = base_settings["unittest_data_dir"] / "transport-example.json"
    inst = transport.Transport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Transport" == inst.resource_type

    impl_transport_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Transport" == data["resourceType"]

    inst2 = transport.Transport(**data)
    impl_transport_1(inst2)
