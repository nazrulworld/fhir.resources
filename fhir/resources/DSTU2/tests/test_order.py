# -*- coding: utf-8 -*-
"""
Profile: None
Release: DSTU2
Version: 1.0.2
Revision: None
"""
from .. import fhirtypes, order


def test_Order_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "order-example.json"
    inst = order.Order.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Order" == inst.resource_type
    impl_Order_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Order" == data["resourceType"]

    inst2 = order.Order(**data)
    impl_Order_1(inst2)


def impl_Order_1(inst):
    assert inst.id == "example"
    assert inst.text.status == "generated"
    assert inst.text.div == (
        "<div>Request for Prescription (on patient Donald DUCK @ Acme Healthcare, Inc. MR = 654321)</div>"  # noqa: B950
    )
    assert inst.date == fhirtypes.DateTime.validate("2012-12-28T09:03:04+11:00")
    assert inst.subject.reference == "Patient/pat2"
    assert inst.source.reference == "Practitioner/example"
    assert inst.reasonCodeableConcept.text == "Standard admission testing"
    assert inst.reasonReference is None
    assert inst.when.fhir_comments == [
        '  Institution local code meaning "do this today"  '
    ]
    assert inst.when.code.coding[0].code == "today"
    assert inst.when.code.coding[0].system == "http://acme.com/codes/request-priority"
    assert inst.when.schedule is None
    assert inst.detail[0].reference == "MedicationOrder/example"


def test_Order_2(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "order-example-f201-physiotherapy.json"
    )
    inst = order.Order.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Order" == inst.resource_type
    impl_Order_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Order" == data["resourceType"]

    inst2 = order.Order(**data)
    impl_Order_2(inst2)


def impl_Order_2(inst):
    assert inst.id == "f201"
    assert inst.date == fhirtypes.DateTime.validate("2013-03-05T12:00:00+01:00")
    assert inst.subject.reference == "Patient/f201"
    assert inst.subject.display == "Roel"
    assert inst.source.reference == "Practitioner/f201"
    assert inst.target.reference == "Practitioner/f203"
    assert inst.target.display == "Juri van Gelder"
    assert inst.reasonCodeableConcept.text == (
        "It concerns a one-off order for consultation in order "
        "to evaluate the stairs walking ability of Roel."
    )
    assert inst.reasonReference is None
    assert inst.when.fhir_comments == [
        '  <authority> and <payment> were registered in the EHR as "not applicable"  '
    ]  # noqa: B950
    assert inst.when.code.coding[0].code == "394848005"
    assert inst.when.code.coding[0].display == "Normal priority"
    assert inst.when.code.coding[0].system == "http://snomed.info/sct"
    assert inst.when.schedule is None
    assert inst.detail[0].display == "Consultation, not yet developed"
