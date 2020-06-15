# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import processresponse


def impl_processresponse_1(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.disposition == (
        "Adjudication processing completed, ClaimResponse and EOB "
        "ready for retrieval."
    )
    assert inst.id == "SR2500"
    assert (
        inst.identifier[0].system == "http://www.BenefitsInc.com/fhir/processresponse"
    )
    assert inst.identifier[0].value == "881234"
    assert inst.organization.reference == "Organization/2"
    assert inst.outcome.coding[0].code == "complete"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/processoutcomecodes"
    assert inst.request.reference == "http://happyvalley.com/fhir/claim/12345"
    assert inst.requestOrganization.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ProcessResponse</div>"
    )
    assert inst.text.status == "generated"


def test_processresponse_1(base_settings):
    """No. 1 tests collection for ProcessResponse.
    Test File: processresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "processresponse-example.json"
    inst = processresponse.ProcessResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessResponse" == inst.resource_type

    impl_processresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessResponse" == data["resourceType"]

    inst2 = processresponse.ProcessResponse(**data)
    impl_processresponse_1(inst2)


def impl_processresponse_2(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-07-14")
    assert inst.disposition == "Referred to claim not found on system."
    assert inst.error[0].coding[0].code == "a001"
    assert inst.error[0].coding[0].system == "http://hl7.org/fhir/adjudication-error"
    assert inst.form.coding[0].code == "PRRESP/2016/01"
    assert inst.form.coding[0].system == "http://ncforms.org/formid"
    assert inst.id == "SR2349"
    assert (
        inst.identifier[0].system == "http://www.BenefitsInc.com/fhir/processresponse"
    )
    assert inst.identifier[0].value == "ER987634"
    assert inst.organization.reference == "Organization/2"
    assert inst.outcome.coding[0].code == "error"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/processoutcomecodes"
    assert inst.processNote[0].text == (
        "Please check the submitted payor identification and local " "claim number."
    )
    assert inst.processNote[0].type.coding[0].code == "print"
    assert inst.processNote[0].type.coding[0].system == "http://hl7.org/fhir/note-type"
    assert inst.request.reference == "http://happyvalley.com/fhir/claim/12204"
    assert inst.requestOrganization.reference == "Organization/1"
    assert inst.requestProvider.identifier.system == "http://npid.org/providerid"
    assert inst.requestProvider.identifier.value == "AZ43258"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ProcessResponse</div>"
    )
    assert inst.text.status == "generated"


def test_processresponse_2(base_settings):
    """No. 2 tests collection for ProcessResponse.
    Test File: processresponse-example-error.json
    """
    filename = base_settings["unittest_data_dir"] / "processresponse-example-error.json"
    inst = processresponse.ProcessResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessResponse" == inst.resource_type

    impl_processresponse_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessResponse" == data["resourceType"]

    inst2 = processresponse.ProcessResponse(**data)
    impl_processresponse_2(inst2)


def impl_processresponse_3(inst):
    assert inst.communicationRequest[0].reference == "#comreq-1"
    assert inst.contained[0].id == "comreq-1"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.disposition == "Additional information required."
    assert inst.id == "SR2499"
    assert (
        inst.identifier[0].system == "http://www.BenefitsInc.com/fhir/processresponse"
    )
    assert inst.identifier[0].value == "881222"
    assert inst.organization.reference == "Organization/2"
    assert inst.outcome.coding[0].code == "pended"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/processoutcomecodes"
    assert inst.request.reference == "http://happyvalley.com/fhir/claim/12345"
    assert inst.requestOrganization.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A '
        "ProcessResponse indicating pended status with a request for "
        "additional information.</div>"
    )
    assert inst.text.status == "generated"


def test_processresponse_3(base_settings):
    """No. 3 tests collection for ProcessResponse.
    Test File: processresponse-example-pended.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "processresponse-example-pended.json"
    )
    inst = processresponse.ProcessResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ProcessResponse" == inst.resource_type

    impl_processresponse_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ProcessResponse" == data["resourceType"]

    inst2 = processresponse.ProcessResponse(**data)
    impl_processresponse_3(inst2)
