# -*- coding: utf-8 -*-
"""
Profile: None
Release: DSTU2
Version: 1.0.2
Revision: None
"""
from .. import fhirtypes, orderresponse


def test_OrderResponse_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "orderresponse-example.json"
    inst = orderresponse.OrderResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OrderResponse" == inst.resource_type
    impl_OrderResponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OrderResponse" == data["resourceType"]

    inst2 = orderresponse.OrderResponse(**data)
    impl_OrderResponse_1(inst2)


def impl_OrderResponse_1(inst):
    assert inst.id == "example"
    assert inst.text.status == "generated"
    assert inst.text.div == "<div>Lab Report completed at 13:10 28-Dec 2012</div>"
    assert inst.request.fhir_comments == [
        "  \n    this should be a response to the example request, \n\tbut we "
        "don't yet have all the resource types in \n\tplace to make this "
        "happen\n\t\n\tSo for now, although the Order message referred to \n\t"
        "here contains a prescription resource, this example\n\tresponse "
        "contains lab reports\n   "
    ]
    assert inst.request.reference == "Order/example"
    assert inst.date == fhirtypes.DateTime.validate("2012-12-28T13:10:56+11:00")
    assert inst.who.fhir_comments == ["  made by the lab  "]
    assert inst.who.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.orderStatus == "completed"
    assert len(inst.fulfillment) == 1
    assert inst.fulfillment[0].fhir_comments == [
        "  \n    the lab report that the lab provides as a token of its \n    "
        "fulfillment for this order \n\n    In the case of a lab order, the "
        "report is usually the real/only\n    outcome. However in a case such "
        "as a medication administration,\n    the actual administration is the"
        " fulfillment - the MedicationAdministration\n    resource is only a "
        "token of the fulfillment of the order\n   "
    ]
    assert inst.fulfillment[0].reference == "DiagnosticReport/101"
