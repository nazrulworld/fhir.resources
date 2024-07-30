# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import claimresponse
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_claimresponse_1(inst):
    assert inst.addItem[0].adjudication[0].amount.currency == "USD"
    assert float(inst.addItem[0].adjudication[0].amount.value) == float(250.0)
    assert inst.addItem[0].adjudication[0].category.coding[0].code == "eligible"
    assert inst.addItem[0].adjudication[1].amount.currency == "USD"
    assert float(inst.addItem[0].adjudication[1].amount.value) == float(10.0)
    assert inst.addItem[0].adjudication[1].category.coding[0].code == "copay"
    assert inst.addItem[0].adjudication[2].category.coding[0].code == "eligpercent"
    assert float(inst.addItem[0].adjudication[2].value) == float(100.0)
    assert inst.addItem[0].adjudication[3].amount.currency == "USD"
    assert float(inst.addItem[0].adjudication[3].amount.value) == float(240.0)
    assert inst.addItem[0].adjudication[3].category.coding[0].code == "benefit"
    assert inst.addItem[0].itemSequence[0] == 1
    assert inst.addItem[0].modifier[0].coding[0].code == "x"
    assert inst.addItem[0].modifier[0].coding[0].display == "None"
    assert (
        inst.addItem[0].modifier[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/fhir/modifiers"}
        ).valueUri
    )
    assert inst.addItem[0].net.currency == "USD"
    assert float(inst.addItem[0].net.value) == float(250.0)
    assert inst.addItem[0].noteNumber[0] == 101
    assert inst.addItem[0].productOrService.coding[0].code == "1101"
    assert (
        inst.addItem[0].productOrService.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/fhir/oralservicecodes"}
        ).valueUri
    )
    assert inst.addItem[1].adjudication[0].amount.currency == "USD"
    assert float(inst.addItem[1].adjudication[0].amount.value) == float(800.0)
    assert inst.addItem[1].adjudication[0].category.coding[0].code == "eligible"
    assert inst.addItem[1].adjudication[1].category.coding[0].code == "eligpercent"
    assert float(inst.addItem[1].adjudication[1].value) == float(100.0)
    assert inst.addItem[1].adjudication[2].amount.currency == "USD"
    assert float(inst.addItem[1].adjudication[2].amount.value) == float(800.0)
    assert inst.addItem[1].adjudication[2].category.coding[0].code == "benefit"
    assert inst.addItem[1].itemSequence[0] == 1
    assert inst.addItem[1].net.currency == "USD"
    assert float(inst.addItem[1].net.value) == float(800.0)
    assert inst.addItem[1].productOrService.coding[0].code == "2101"
    assert (
        inst.addItem[1].productOrService.coding[0].display == "Radiograph, series (12)"
    )
    assert (
        inst.addItem[1].productOrService.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/fhir/oralservicecodes"}
        ).valueUri
    )
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-08-16"}
        ).valueDateTime
    )
    assert inst.disposition == (
        "The enclosed services are authorized for your provision "
        "within 30 days of this notice."
    )
    assert inst.id == "UR3503"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.SocialBenefitsInc.com/fhir/ClaimResponse"}
        ).valueUri
    )
    assert inst.identifier[0].value == "UR3503"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert (
        inst.insurer.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.jurisdiction.org/insurers"}
        ).valueUri
    )
    assert inst.insurer.identifier.value == "444123"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcome == "complete"
    assert inst.patient.reference == "Patient/1"
    assert inst.payeeType.coding[0].code == "provider"
    assert (
        inst.payeeType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/payeetype"}
        ).valueUri
    )
    assert inst.preAuthRef == "18SS12345"
    assert inst.processNote[0].language.coding[0].code == "en-CA"
    assert (
        inst.processNote[0].language.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:bcp:47"}
        ).valueUri
    )
    assert inst.processNote[0].number == 101
    assert inst.processNote[0].text == (
        "Please submit a Pre-Authorization request if a more "
        "extensive examination or urgent services are required."
    )
    assert inst.processNote[0].type == "print"
    assert inst.requestor.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A sample '
        "unsolicited pre-authorization response which authorizes "
        "basic dental services to be performed for a patient.</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total[0].amount.currency == "USD"
    assert float(inst.total[0].amount.value) == float(1050.0)
    assert inst.total[0].category.coding[0].code == "submitted"
    assert inst.total[1].amount.currency == "USD"
    assert float(inst.total[1].amount.value) == float(1040.0)
    assert inst.total[1].category.coding[0].code == "benefit"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/claim-type"}
        ).valueUri
    )
    assert inst.use == "preauthorization"


def test_claimresponse_1(base_settings):
    """No. 1 tests collection for ClaimResponse.
    Test File: claimresponse-example-unsolicited-preauth.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "claimresponse-example-unsolicited-preauth.json"
    )
    inst = claimresponse.ClaimResponse.model_validate_json(filename.read_bytes())
    assert "ClaimResponse" == inst.get_resource_type()

    impl_claimresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ClaimResponse" == data["resourceType"]

    inst2 = claimresponse.ClaimResponse(**data)
    impl_claimresponse_1(inst2)


def impl_claimresponse_2(inst):
    assert inst.addItem[0].adjudication[0].amount.currency == "USD"
    assert float(inst.addItem[0].adjudication[0].amount.value) == float(100.0)
    assert inst.addItem[0].adjudication[0].category.coding[0].code == "eligible"
    assert inst.addItem[0].adjudication[1].amount.currency == "USD"
    assert float(inst.addItem[0].adjudication[1].amount.value) == float(10.0)
    assert inst.addItem[0].adjudication[1].category.coding[0].code == "copay"
    assert inst.addItem[0].adjudication[2].category.coding[0].code == "eligpercent"
    assert float(inst.addItem[0].adjudication[2].value) == float(80.0)
    assert inst.addItem[0].adjudication[3].amount.currency == "USD"
    assert float(inst.addItem[0].adjudication[3].amount.value) == float(72.0)
    assert inst.addItem[0].adjudication[3].category.coding[0].code == "benefit"
    assert inst.addItem[0].adjudication[3].reason.coding[0].code == "ar002"
    assert (
        inst.addItem[0].adjudication[3].reason.coding[0].display == "Plan Limit Reached"
    )
    assert (
        inst.addItem[0].adjudication[3].reason.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/adjudication-reason"}
        ).valueUri
    )
    assert inst.addItem[0].itemSequence[0] == 1
    assert inst.addItem[0].modifier[0].coding[0].code == "x"
    assert inst.addItem[0].modifier[0].coding[0].display == "None"
    assert (
        inst.addItem[0].modifier[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/fhir/modifiers"}
        ).valueUri
    )
    assert inst.addItem[0].net.currency == "USD"
    assert float(inst.addItem[0].net.value) == float(135.57)
    assert inst.addItem[0].noteNumber[0] == 101
    assert inst.addItem[0].productOrService.coding[0].code == "1101"
    assert (
        inst.addItem[0].productOrService.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/fhir/oralservicecodes"}
        ).valueUri
    )
    assert inst.addItem[1].adjudication[0].amount.currency == "USD"
    assert float(inst.addItem[1].adjudication[0].amount.value) == float(35.57)
    assert inst.addItem[1].adjudication[0].category.coding[0].code == "eligible"
    assert inst.addItem[1].adjudication[1].category.coding[0].code == "eligpercent"
    assert float(inst.addItem[1].adjudication[1].value) == float(80.0)
    assert inst.addItem[1].adjudication[2].amount.currency == "USD"
    assert float(inst.addItem[1].adjudication[2].amount.value) == float(28.47)
    assert inst.addItem[1].adjudication[2].category.coding[0].code == "benefit"
    assert inst.addItem[1].itemSequence[0] == 1
    assert inst.addItem[1].net.currency == "USD"
    assert float(inst.addItem[1].net.value) == float(35.57)
    assert inst.addItem[1].productOrService.coding[0].code == "2141"
    assert inst.addItem[1].productOrService.coding[0].display == "Radiograph, bytewing"
    assert (
        inst.addItem[1].productOrService.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/fhir/oralservicecodes"}
        ).valueUri
    )
    assert inst.addItem[2].adjudication[0].amount.currency == "USD"
    assert float(inst.addItem[2].adjudication[0].amount.value) == float(350.0)
    assert inst.addItem[2].adjudication[0].category.coding[0].code == "eligible"
    assert inst.addItem[2].adjudication[1].category.coding[0].code == "eligpercent"
    assert float(inst.addItem[2].adjudication[1].value) == float(80.0)
    assert inst.addItem[2].adjudication[2].amount.currency == "USD"
    assert float(inst.addItem[2].adjudication[2].amount.value) == float(270.0)
    assert inst.addItem[2].adjudication[2].category.coding[0].code == "benefit"
    assert inst.addItem[2].detailSequence[0] == 2
    assert inst.addItem[2].itemSequence[0] == 3
    assert inst.addItem[2].modifier[0].coding[0].code == "x"
    assert inst.addItem[2].modifier[0].coding[0].display == "None"
    assert (
        inst.addItem[2].modifier[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/fhir/modifiers"}
        ).valueUri
    )
    assert inst.addItem[2].net.currency == "USD"
    assert float(inst.addItem[2].net.value) == float(350.0)
    assert inst.addItem[2].noteNumber[0] == 101
    assert inst.addItem[2].productOrService.coding[0].code == "expense"
    assert (
        inst.addItem[2].productOrService.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/fhir/oralservicecodes"}
        ).valueUri
    )
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-08-16"}
        ).valueDateTime
    )
    assert inst.disposition == "Claim settled as per contract."
    assert inst.id == "R3503"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/remittance"}
        ).valueUri
    )
    assert inst.identifier[0].value == "R3503"
    assert (
        inst.insurer.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.jurisdiction.org/insurers"}
        ).valueUri
    )
    assert inst.insurer.identifier.value == "555123"
    assert inst.item[0].adjudication[0].amount.currency == "USD"
    assert float(inst.item[0].adjudication[0].amount.value) == float(0.0)
    assert inst.item[0].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[0].adjudication[1].amount.currency == "USD"
    assert float(inst.item[0].adjudication[1].amount.value) == float(0.0)
    assert inst.item[0].adjudication[1].category.coding[0].code == "benefit"
    assert inst.item[0].itemSequence == 1
    assert inst.item[1].adjudication[0].amount.currency == "USD"
    assert float(inst.item[1].adjudication[0].amount.value) == float(105.0)
    assert inst.item[1].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[1].adjudication[1].category.coding[0].code == "eligpercent"
    assert float(inst.item[1].adjudication[1].value) == float(80.0)
    assert inst.item[1].adjudication[2].amount.currency == "USD"
    assert float(inst.item[1].adjudication[2].amount.value) == float(84.0)
    assert inst.item[1].adjudication[2].category.coding[0].code == "benefit"
    assert inst.item[1].itemSequence == 2
    assert inst.item[2].adjudication[0].amount.currency == "USD"
    assert float(inst.item[2].adjudication[0].amount.value) == float(750.0)
    assert inst.item[2].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[2].adjudication[1].category.coding[0].code == "eligpercent"
    assert float(inst.item[2].adjudication[1].value) == float(80.0)
    assert inst.item[2].adjudication[2].amount.currency == "USD"
    assert float(inst.item[2].adjudication[2].amount.value) == float(600.0)
    assert inst.item[2].adjudication[2].category.coding[0].code == "benefit"
    assert inst.item[2].detail[0].adjudication[0].amount.currency == "USD"
    assert float(inst.item[2].detail[0].adjudication[0].amount.value) == float(750.0)
    assert inst.item[2].detail[0].adjudication[0].category.coding[0].code == "eligible"
    assert (
        inst.item[2].detail[0].adjudication[1].category.coding[0].code == "eligpercent"
    )
    assert float(inst.item[2].detail[0].adjudication[1].value) == float(80.0)
    assert inst.item[2].detail[0].adjudication[2].amount.currency == "USD"
    assert float(inst.item[2].detail[0].adjudication[2].amount.value) == float(600.0)
    assert inst.item[2].detail[0].adjudication[2].category.coding[0].code == "benefit"
    assert inst.item[2].detail[0].detailSequence == 1
    assert inst.item[2].detail[1].adjudication[0].amount.currency == "USD"
    assert float(inst.item[2].detail[1].adjudication[0].amount.value) == float(0.0)
    assert inst.item[2].detail[1].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[2].detail[1].adjudication[1].amount.currency == "USD"
    assert float(inst.item[2].detail[1].adjudication[1].amount.value) == float(0.0)
    assert inst.item[2].detail[1].adjudication[1].category.coding[0].code == "benefit"
    assert inst.item[2].detail[1].detailSequence == 2
    assert inst.item[2].itemSequence == 3
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcome == "complete"
    assert inst.patient.reference == "Patient/1"
    assert inst.payeeType.coding[0].code == "provider"
    assert (
        inst.payeeType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/payeetype"}
        ).valueUri
    )
    assert inst.payment.amount.currency == "USD"
    assert float(inst.payment.amount.value) == float(100.47)
    assert (
        inst.payment.date
        == ExternalValidatorModel.model_validate({"valueDate": "2014-08-31"}).valueDate
    )
    assert (
        inst.payment.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/paymentidentifier"}
        ).valueUri
    )
    assert inst.payment.identifier.value == "201408-2-15507"
    assert inst.payment.type.coding[0].code == "complete"
    assert (
        inst.payment.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-paymenttype"}
        ).valueUri
    )
    assert inst.processNote[0].language.coding[0].code == "en-CA"
    assert (
        inst.processNote[0].language.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:bcp:47"}
        ).valueUri
    )
    assert inst.processNote[0].number == 101
    assert (
        inst.processNote[0].text
        == "Package codes are not permitted. Codes replaced by Insurer."
    )
    assert inst.processNote[0].type == "print"
    assert (
        inst.request.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://happyvalley.com/claim"}
        ).valueUri
    )
    assert inst.request.identifier.value == "12346"
    assert inst.requestor.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ClaimResponse to Claim Oral Average with "
        "additional items</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total[0].amount.currency == "USD"
    assert float(inst.total[0].amount.value) == float(1340.57)
    assert inst.total[0].category.coding[0].code == "submitted"
    assert inst.total[1].amount.currency == "USD"
    assert float(inst.total[1].amount.value) == float(1054.47)
    assert inst.total[1].category.coding[0].code == "benefit"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/claim-type"}
        ).valueUri
    )
    assert inst.use == "claim"


def test_claimresponse_2(base_settings):
    """No. 2 tests collection for ClaimResponse.
    Test File: claimresponse-example-additem.json
    """
    filename = base_settings["unittest_data_dir"] / "claimresponse-example-additem.json"
    inst = claimresponse.ClaimResponse.model_validate_json(filename.read_bytes())
    assert "ClaimResponse" == inst.get_resource_type()

    impl_claimresponse_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ClaimResponse" == data["resourceType"]

    inst2 = claimresponse.ClaimResponse(**data)
    impl_claimresponse_2(inst2)


def impl_claimresponse_3(inst):
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-08-16"}
        ).valueDateTime
    )
    assert inst.disposition == "Claim settled as per contract."
    assert inst.id == "R3500"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/remittance"}
        ).valueUri
    )
    assert inst.identifier[0].value == "R3500"
    assert (
        inst.insurer.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.jurisdiction.org/insurers"}
        ).valueUri
    )
    assert inst.insurer.identifier.value == "555123"
    assert inst.item[0].adjudication[0].amount.currency == "USD"
    assert float(inst.item[0].adjudication[0].amount.value) == float(135.57)
    assert inst.item[0].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[0].adjudication[1].amount.currency == "USD"
    assert float(inst.item[0].adjudication[1].amount.value) == float(10.0)
    assert inst.item[0].adjudication[1].category.coding[0].code == "copay"
    assert inst.item[0].adjudication[2].category.coding[0].code == "eligpercent"
    assert float(inst.item[0].adjudication[2].value) == float(80.0)
    assert inst.item[0].adjudication[3].amount.currency == "USD"
    assert float(inst.item[0].adjudication[3].amount.value) == float(90.47)
    assert inst.item[0].adjudication[3].category.coding[0].code == "benefit"
    assert inst.item[0].adjudication[3].reason.coding[0].code == "ar002"
    assert inst.item[0].adjudication[3].reason.coding[0].display == "Plan Limit Reached"
    assert (
        inst.item[0].adjudication[3].reason.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/adjudication-reason"}
        ).valueUri
    )
    assert inst.item[0].itemSequence == 1
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcome == "complete"
    assert inst.patient.reference == "Patient/1"
    assert inst.payeeType.coding[0].code == "provider"
    assert (
        inst.payeeType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/payeetype"}
        ).valueUri
    )
    assert inst.payment.amount.currency == "USD"
    assert float(inst.payment.amount.value) == float(100.47)
    assert (
        inst.payment.date
        == ExternalValidatorModel.model_validate({"valueDate": "2014-08-31"}).valueDate
    )
    assert (
        inst.payment.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/paymentidentifier"}
        ).valueUri
    )
    assert inst.payment.identifier.value == "201408-2-1569478"
    assert inst.payment.type.coding[0].code == "complete"
    assert (
        inst.payment.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-paymenttype"}
        ).valueUri
    )
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/oralhealthclaim/15476332402"
    )
    assert inst.requestor.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.subType.coding[0].code == "emergency"
    assert (
        inst.subType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-claimsubtype"}
        ).valueUri
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ClaimResponse</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total[0].amount.currency == "USD"
    assert float(inst.total[0].amount.value) == float(135.57)
    assert inst.total[0].category.coding[0].code == "submitted"
    assert inst.total[1].amount.currency == "USD"
    assert float(inst.total[1].amount.value) == float(90.47)
    assert inst.total[1].category.coding[0].code == "benefit"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/claim-type"}
        ).valueUri
    )
    assert inst.use == "claim"


def test_claimresponse_3(base_settings):
    """No. 3 tests collection for ClaimResponse.
    Test File: claimresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "claimresponse-example.json"
    inst = claimresponse.ClaimResponse.model_validate_json(filename.read_bytes())
    assert "ClaimResponse" == inst.get_resource_type()

    impl_claimresponse_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ClaimResponse" == data["resourceType"]

    inst2 = claimresponse.ClaimResponse(**data)
    impl_claimresponse_3(inst2)


def impl_claimresponse_4(inst):
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-08-16"}
        ).valueDateTime
    )
    assert inst.disposition == "Claim settled as per contract."
    assert inst.id == "R3502"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://thebenefitcompany.com/claimresponse"}
        ).valueUri
    )
    assert inst.identifier[0].value == "CR6532875367"
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].adjudication[0].amount.currency == "USD"
    assert float(inst.item[0].adjudication[0].amount.value) == float(235.4)
    assert inst.item[0].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[0].adjudication[1].amount.currency == "USD"
    assert float(inst.item[0].adjudication[1].amount.value) == float(20.0)
    assert inst.item[0].adjudication[1].category.coding[0].code == "copay"
    assert inst.item[0].adjudication[2].category.coding[0].code == "eligpercent"
    assert float(inst.item[0].adjudication[2].value) == float(80.0)
    assert inst.item[0].adjudication[3].amount.currency == "USD"
    assert float(inst.item[0].adjudication[3].amount.value) == float(172.32)
    assert inst.item[0].adjudication[3].category.coding[0].code == "benefit"
    assert inst.item[0].detail[0].adjudication[0].amount.currency == "USD"
    assert float(inst.item[0].detail[0].adjudication[0].amount.value) == float(100.0)
    assert inst.item[0].detail[0].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[0].detail[0].adjudication[1].amount.currency == "USD"
    assert float(inst.item[0].detail[0].adjudication[1].amount.value) == float(20.0)
    assert inst.item[0].detail[0].adjudication[1].category.coding[0].code == "copay"
    assert (
        inst.item[0].detail[0].adjudication[2].category.coding[0].code == "eligpercent"
    )
    assert float(inst.item[0].detail[0].adjudication[2].value) == float(80.0)
    assert inst.item[0].detail[0].adjudication[3].amount.currency == "USD"
    assert float(inst.item[0].detail[0].adjudication[3].amount.value) == float(80.0)
    assert inst.item[0].detail[0].adjudication[3].category.coding[0].code == "benefit"
    assert inst.item[0].detail[0].detailSequence == 1
    assert inst.item[0].detail[0].noteNumber[0] == 1
    assert inst.item[0].detail[1].adjudication[0].amount.currency == "USD"
    assert float(inst.item[0].detail[1].adjudication[0].amount.value) == float(110.0)
    assert inst.item[0].detail[1].adjudication[0].category.coding[0].code == "eligible"
    assert (
        inst.item[0].detail[1].adjudication[1].category.coding[0].code == "eligpercent"
    )
    assert float(inst.item[0].detail[1].adjudication[1].value) == float(80.0)
    assert inst.item[0].detail[1].adjudication[2].amount.currency == "USD"
    assert float(inst.item[0].detail[1].adjudication[2].amount.value) == float(88.0)
    assert inst.item[0].detail[1].adjudication[2].category.coding[0].code == "benefit"
    assert inst.item[0].detail[1].detailSequence == 2
    assert inst.item[0].detail[1].noteNumber[0] == 1
    assert inst.item[0].detail[1].subDetail[0].adjudication[0].amount.currency == "USD"
    assert float(
        inst.item[0].detail[1].subDetail[0].adjudication[0].amount.value
    ) == float(60.0)
    assert (
        inst.item[0].detail[1].subDetail[0].adjudication[0].category.coding[0].code
        == "eligible"
    )
    assert (
        inst.item[0].detail[1].subDetail[0].adjudication[1].category.coding[0].code
        == "eligpercent"
    )
    assert float(inst.item[0].detail[1].subDetail[0].adjudication[1].value) == float(
        80.0
    )
    assert inst.item[0].detail[1].subDetail[0].adjudication[2].amount.currency == "USD"
    assert float(
        inst.item[0].detail[1].subDetail[0].adjudication[2].amount.value
    ) == float(48.0)
    assert (
        inst.item[0].detail[1].subDetail[0].adjudication[2].category.coding[0].code
        == "benefit"
    )
    assert inst.item[0].detail[1].subDetail[0].noteNumber[0] == 1
    assert inst.item[0].detail[1].subDetail[0].subDetailSequence == 1
    assert inst.item[0].detail[1].subDetail[1].adjudication[0].amount.currency == "USD"
    assert float(
        inst.item[0].detail[1].subDetail[1].adjudication[0].amount.value
    ) == float(30.0)
    assert (
        inst.item[0].detail[1].subDetail[1].adjudication[0].category.coding[0].code
        == "eligible"
    )
    assert (
        inst.item[0].detail[1].subDetail[1].adjudication[1].category.coding[0].code
        == "eligpercent"
    )
    assert float(inst.item[0].detail[1].subDetail[1].adjudication[1].value) == float(
        80.0
    )
    assert inst.item[0].detail[1].subDetail[1].adjudication[2].amount.currency == "USD"
    assert float(
        inst.item[0].detail[1].subDetail[1].adjudication[2].amount.value
    ) == float(24.0)
    assert (
        inst.item[0].detail[1].subDetail[1].adjudication[2].category.coding[0].code
        == "benefit"
    )
    assert inst.item[0].detail[1].subDetail[1].subDetailSequence == 2
    assert inst.item[0].detail[1].subDetail[2].adjudication[0].amount.currency == "USD"
    assert float(
        inst.item[0].detail[1].subDetail[2].adjudication[0].amount.value
    ) == float(10.0)
    assert (
        inst.item[0].detail[1].subDetail[2].adjudication[0].category.coding[0].code
        == "eligible"
    )
    assert (
        inst.item[0].detail[1].subDetail[2].adjudication[1].category.coding[0].code
        == "eligpercent"
    )
    assert float(inst.item[0].detail[1].subDetail[2].adjudication[1].value) == float(
        80.0
    )
    assert inst.item[0].detail[1].subDetail[2].adjudication[2].amount.currency == "USD"
    assert float(
        inst.item[0].detail[1].subDetail[2].adjudication[2].amount.value
    ) == float(8.0)
    assert (
        inst.item[0].detail[1].subDetail[2].adjudication[2].category.coding[0].code
        == "benefit"
    )
    assert inst.item[0].detail[1].subDetail[2].noteNumber[0] == 1
    assert inst.item[0].detail[1].subDetail[2].subDetailSequence == 3
    assert inst.item[0].detail[2].adjudication[0].amount.currency == "USD"
    assert float(inst.item[0].detail[2].adjudication[0].amount.value) == float(200.0)
    assert inst.item[0].detail[2].adjudication[0].category.coding[0].code == "eligible"
    assert (
        inst.item[0].detail[2].adjudication[1].category.coding[0].code == "eligpercent"
    )
    assert float(inst.item[0].detail[2].adjudication[1].value) == float(80.0)
    assert inst.item[0].detail[2].adjudication[2].amount.currency == "USD"
    assert float(inst.item[0].detail[2].adjudication[2].amount.value) == float(14.0)
    assert inst.item[0].detail[2].adjudication[2].category.coding[0].code == "benefit"
    assert inst.item[0].detail[2].detailSequence == 3
    assert inst.item[0].detail[2].noteNumber[0] == 1
    assert inst.item[0].itemSequence == 1
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcome == "complete"
    assert inst.patient.reference == "Patient/1"
    assert inst.payeeType.coding[0].code == "provider"
    assert (
        inst.payeeType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/payeetype"}
        ).valueUri
    )
    assert inst.payment.adjustment.currency == "USD"
    assert float(inst.payment.adjustment.value) == float(75.0)
    assert inst.payment.adjustmentReason.coding[0].code == "a002"
    assert inst.payment.adjustmentReason.coding[0].display == "Prior Overpayment"
    assert (
        inst.payment.adjustmentReason.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/payment-adjustment-reason"
            }
        ).valueUri
    )
    assert inst.payment.amount.currency == "USD"
    assert float(inst.payment.amount.value) == float(107.0)
    assert (
        inst.payment.date
        == ExternalValidatorModel.model_validate({"valueDate": "2014-08-16"}).valueDate
    )
    assert (
        inst.payment.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://thebenefitcompany.com/paymentidentifier"}
        ).valueUri
    )
    assert inst.payment.identifier.value == "201416-123456"
    assert inst.payment.type.coding[0].code == "complete"
    assert (
        inst.payment.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-paymenttype"}
        ).valueUri
    )
    assert inst.processNote[0].language.coding[0].code == "en-CA"
    assert (
        inst.processNote[0].language.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:bcp:47"}
        ).valueUri
    )
    assert inst.processNote[0].number == 1
    assert inst.processNote[0].text == "After hours surcharge declined"
    assert inst.processNote[0].type == "display"
    assert (
        inst.request.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://happysight.com/claim"}
        ).valueUri
    )
    assert inst.request.identifier.value == "6612346"
    assert inst.requestor.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ClaimResponse</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total[0].amount.currency == "USD"
    assert float(inst.total[0].amount.value) == float(235.4)
    assert inst.total[0].category.coding[0].code == "submitted"
    assert inst.total[1].amount.currency == "USD"
    assert float(inst.total[1].amount.value) == float(182.0)
    assert inst.total[1].category.coding[0].code == "benefit"
    assert inst.type.coding[0].code == "vision"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/claim-type"}
        ).valueUri
    )
    assert inst.use == "claim"


def test_claimresponse_4(base_settings):
    """No. 4 tests collection for ClaimResponse.
    Test File: claimresponse-example-vision-3tier.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "claimresponse-example-vision-3tier.json"
    )
    inst = claimresponse.ClaimResponse.model_validate_json(filename.read_bytes())
    assert "ClaimResponse" == inst.get_resource_type()

    impl_claimresponse_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ClaimResponse" == data["resourceType"]

    inst2 = claimresponse.ClaimResponse(**data)
    impl_claimresponse_4(inst2)


def impl_claimresponse_5(inst):
    assert inst.communicationRequest[0].reference == "CommunicationRequest/fm-solicit"
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-08-16"}
        ).valueDateTime
    )
    assert inst.disposition == "Claim could not be processed"
    assert inst.error[0].code.coding[0].code == "a002"
    assert (
        inst.error[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/adjudication-error"}
        ).valueUri
    )
    assert inst.error[0].detailSequence == 2
    assert inst.error[0].itemSequence == 3
    assert inst.formCode.coding[0].code == "2"
    assert (
        inst.formCode.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/forms-codes"}
        ).valueUri
    )
    assert inst.id == "R3501"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/remittance"}
        ).valueUri
    )
    assert inst.identifier[0].value == "R3501"
    assert (
        inst.insurer.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.jurisdiction.org/insurers"}
        ).valueUri
    )
    assert inst.insurer.identifier.value == "555123"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcome == "error"
    assert inst.patient.reference == "Patient/1"
    assert inst.processNote[0].language.coding[0].code == "en-CA"
    assert (
        inst.processNote[0].language.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:bcp:47"}
        ).valueUri
    )
    assert inst.processNote[0].number == 1
    assert inst.processNote[0].text == "Invalid claim"
    assert inst.processNote[0].type == "display"
    assert inst.request.reference == "Claim/100156"
    assert inst.requestor.reference == "Practitioner/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ClaimResponse that demonstrates returning "
        "errors</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/claim-type"}
        ).valueUri
    )
    assert inst.use == "claim"


def test_claimresponse_5(base_settings):
    """No. 5 tests collection for ClaimResponse.
    Test File: claimresponse-example-2.json
    """
    filename = base_settings["unittest_data_dir"] / "claimresponse-example-2.json"
    inst = claimresponse.ClaimResponse.model_validate_json(filename.read_bytes())
    assert "ClaimResponse" == inst.get_resource_type()

    impl_claimresponse_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ClaimResponse" == data["resourceType"]

    inst2 = claimresponse.ClaimResponse(**data)
    impl_claimresponse_5(inst2)
