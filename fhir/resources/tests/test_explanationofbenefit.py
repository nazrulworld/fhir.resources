# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import explanationofbenefit


def impl_explanationofbenefit_1(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.claim.reference == "Claim/100150"
    assert inst.claimResponse.reference == "ClaimResponse/R3500"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.disposition == "Claim settled as per contract."
    assert inst.enterer.reference == "Practitioner/1"
    assert inst.facility.reference == "Location/1"
    assert inst.id == "EB3500"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/explanationofbenefit"
    )
    assert inst.identifier[0].value == "987654321"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurer.reference == "Organization/3"
    assert inst.item[0].adjudication[0].amount.currency == "USD"
    assert float(inst.item[0].adjudication[0].amount.value) == float(120.0)
    assert inst.item[0].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[0].adjudication[1].category.coding[0].code == "eligpercent"
    assert float(inst.item[0].adjudication[1].value) == float(0.8)
    assert inst.item[0].adjudication[2].amount.currency == "USD"
    assert float(inst.item[0].adjudication[2].amount.value) == float(96.0)
    assert inst.item[0].adjudication[2].category.coding[0].code == "benefit"
    assert inst.item[0].careTeamSequence[0] == 1
    assert inst.item[0].encounter[0].reference == "Encounter/example"
    assert inst.item[0].net.currency == "USD"
    assert float(inst.item[0].net.value) == float(135.57)
    assert inst.item[0].productOrService.coding[0].code == "1205"
    assert (
        inst.item[0].productOrService.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-USCLS"
    )
    assert inst.item[0].sequence == 1
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].udi[0].reference == "Device/example"
    assert inst.item[0].unitPrice.currency == "USD"
    assert float(inst.item[0].unitPrice.value) == float(135.57)
    assert inst.item[1].adjudication[0].amount.currency == "USD"
    assert float(inst.item[1].adjudication[0].amount.value) == float(180.0)
    assert inst.item[1].adjudication[0].category.coding[0].code == "benefit"
    assert inst.item[1].careTeamSequence[0] == 1
    assert inst.item[1].detail[0].adjudication[0].amount.currency == "USD"
    assert float(inst.item[1].detail[0].adjudication[0].amount.value) == float(180.0)
    assert inst.item[1].detail[0].adjudication[0].category.coding[0].code == "benefit"
    assert inst.item[1].detail[0].net.currency == "USD"
    assert float(inst.item[1].detail[0].net.value) == float(200.0)
    assert inst.item[1].detail[0].productOrService.coding[0].code == "group"
    assert inst.item[1].detail[0].sequence == 1
    assert inst.item[1].detail[0].subDetail[0].adjudication[0].amount.currency == "USD"
    assert float(
        inst.item[1].detail[0].subDetail[0].adjudication[0].amount.value
    ) == float(200.0)
    assert (
        inst.item[1].detail[0].subDetail[0].adjudication[0].category.coding[0].code
        == "eligible"
    )
    assert (
        inst.item[1].detail[0].subDetail[0].adjudication[1].category.coding[0].code
        == "eligpercent"
    )
    assert float(inst.item[1].detail[0].subDetail[0].adjudication[1].value) == float(
        0.9
    )
    assert inst.item[1].detail[0].subDetail[0].adjudication[2].amount.currency == "USD"
    assert float(
        inst.item[1].detail[0].subDetail[0].adjudication[2].amount.value
    ) == float(180.0)
    assert (
        inst.item[1].detail[0].subDetail[0].adjudication[2].category.coding[0].code
        == "benefit"
    )
    assert inst.item[1].detail[0].subDetail[0].net.currency == "USD"
    assert float(inst.item[1].detail[0].subDetail[0].net.value) == float(200.0)
    assert inst.item[1].detail[0].subDetail[0].productOrService.coding[0].code == "1205"
    assert (
        inst.item[1].detail[0].subDetail[0].productOrService.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-USCLS"
    )
    assert inst.item[1].detail[0].subDetail[0].sequence == 1
    assert inst.item[1].detail[0].subDetail[0].udi[0].reference == "Device/example"
    assert inst.item[1].detail[0].subDetail[0].unitPrice.currency == "USD"
    assert float(inst.item[1].detail[0].subDetail[0].unitPrice.value) == float(200.0)
    assert inst.item[1].detail[0].udi[0].reference == "Device/example"
    assert inst.item[1].net.currency == "USD"
    assert float(inst.item[1].net.value) == float(200.0)
    assert inst.item[1].productOrService.coding[0].code == "group"
    assert inst.item[1].sequence == 2
    assert inst.item[1].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "complete"
    assert inst.patient.reference == "Patient/pat1"
    assert inst.payee.party.reference == "Organization/2"
    assert inst.payee.type.coding[0].code == "provider"
    assert (
        inst.payee.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/payeetype"
    )
    assert inst.provider.reference == "Practitioner/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ExplanationOfBenefit</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total[0].amount.currency == "USD"
    assert float(inst.total[0].amount.value) == float(135.57)
    assert inst.total[0].category.coding[0].code == "submitted"
    assert inst.total[1].amount.currency == "USD"
    assert float(inst.total[1].amount.value) == float(96.0)
    assert inst.total[1].category.coding[0].code == "benefit"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_explanationofbenefit_1(base_settings):
    """No. 1 tests collection for ExplanationOfBenefit.
    Test File: explanationofbenefit-example.json
    """
    filename = base_settings["unittest_data_dir"] / "explanationofbenefit-example.json"
    inst = explanationofbenefit.ExplanationOfBenefit.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ExplanationOfBenefit" == inst.resource_type

    impl_explanationofbenefit_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ExplanationOfBenefit" == data["resourceType"]

    inst2 = explanationofbenefit.ExplanationOfBenefit(**data)
    impl_explanationofbenefit_1(inst2)


def impl_explanationofbenefit_2(inst):
    assert inst.accident.date == fhirtypes.Date.validate("2014-02-14")
    assert inst.accident.locationReference.reference == "Location/ph"
    assert inst.accident.type.coding[0].code == "SPT"
    assert (
        inst.accident.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.billablePeriod.end == fhirtypes.DateTime.validate("2014-03-01")
    assert inst.billablePeriod.start == fhirtypes.DateTime.validate("2014-02-01")
    assert inst.claim.reference == "Claim/100150"
    assert inst.claimResponse.reference == "ClaimResponse/R3500"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.disposition == "Could not process."
    assert inst.enterer.reference == "Practitioner/1"
    assert inst.facility.reference == "Location/1"
    assert inst.formCode.coding[0].code == "2"
    assert (
        inst.formCode.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/forms-codes"
    )
    assert inst.id == "EB3501"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/explanationofbenefit"
    )
    assert inst.identifier[0].value == "error-1"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurer.reference == "Organization/2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.originalPrescription.reference == "MedicationRequest/medrx0301"
    assert inst.outcome == "error"
    assert inst.patient.reference == "Patient/pat1"
    assert inst.precedence == 2
    assert inst.prescription.reference == "MedicationRequest/medrx002"
    assert inst.procedure[0].date == fhirtypes.DateTime.validate("2014-02-14")
    assert inst.procedure[0].procedureCodeableConcept.coding[0].code == "123001"
    assert (
        inst.procedure[0].procedureCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/sid/ex-icd-10-procedures"
    )
    assert inst.procedure[0].sequence == 1
    assert inst.procedure[0].udi[0].reference == "Device/example"
    assert inst.processNote[0].language.coding[0].code == "en-CA"
    assert inst.processNote[0].language.coding[0].system == "urn:ietf:bcp:47"
    assert inst.processNote[0].number == 1
    assert inst.processNote[0].text == "Invalid claim"
    assert inst.processNote[0].type == "display"
    assert inst.provider.reference == "Organization/2"
    assert inst.related[0].reference.system == "http://www.BenefitsInc.com/case-number"
    assert inst.related[0].reference.value == "23-56Tu-XX-47-20150M14"
    assert inst.status == "active"
    assert inst.subType.coding[0].code == "emergency"
    assert (
        inst.subType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-claimsubtype"
    )
    assert inst.supportingInfo[0].category.coding[0].code == "employmentimpacted"
    assert inst.supportingInfo[0].category.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/claiminformationcatego" "ry"
    )
    assert inst.supportingInfo[0].sequence == 1
    assert inst.supportingInfo[0].timingPeriod.end == fhirtypes.DateTime.validate(
        "2014-02-28"
    )
    assert inst.supportingInfo[0].timingPeriod.start == fhirtypes.DateTime.validate(
        "2014-02-14"
    )
    assert inst.supportingInfo[1].category.coding[0].code == "hospitalized"
    assert inst.supportingInfo[1].category.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/claiminformationcatego" "ry"
    )
    assert inst.supportingInfo[1].sequence == 2
    assert inst.supportingInfo[1].timingPeriod.end == fhirtypes.DateTime.validate(
        "2014-02-16"
    )
    assert inst.supportingInfo[1].timingPeriod.start == fhirtypes.DateTime.validate(
        "2014-02-14"
    )
    assert inst.text.status == "generated"
    assert inst.total[0].amount.currency == "USD"
    assert float(inst.total[0].amount.value) == float(2478.57)
    assert inst.total[0].category.coding[0].code == "submitted"
    assert inst.total[1].amount.currency == "USD"
    assert float(inst.total[1].amount.value) == float(0.0)
    assert inst.total[1].category.coding[0].code == "benefit"
    assert inst.type.coding[0].code == "oral"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/claim-type"
    )
    assert inst.use == "claim"


def test_explanationofbenefit_2(base_settings):
    """No. 2 tests collection for ExplanationOfBenefit.
    Test File: explanationofbenefit-example-2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "explanationofbenefit-example-2.json"
    )
    inst = explanationofbenefit.ExplanationOfBenefit.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ExplanationOfBenefit" == inst.resource_type

    impl_explanationofbenefit_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ExplanationOfBenefit" == data["resourceType"]

    inst2 = explanationofbenefit.ExplanationOfBenefit(**data)
    impl_explanationofbenefit_2(inst2)
