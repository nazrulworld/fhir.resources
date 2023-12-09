# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

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
    assert inst.insurance.coverage.reference == "Coverage/9876B1"
    assert inst.item[0].adjudication[0].amount.code == "USD"
    assert inst.item[0].adjudication[0].amount.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].adjudication[0].amount.value) == float(120.0)
    assert inst.item[0].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[0].adjudication[1].category.coding[0].code == "eligpercent"
    assert float(inst.item[0].adjudication[1].value) == float(0.8)
    assert inst.item[0].adjudication[2].amount.code == "USD"
    assert inst.item[0].adjudication[2].amount.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].adjudication[2].amount.value) == float(96.0)
    assert inst.item[0].adjudication[2].category.coding[0].code == "benefit"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].encounter[0].reference == "Encounter/example"
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(135.57)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "1200"
    assert inst.item[0].service.coding[0].system == "http://hl7.org/fhir/service-uscls"
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(135.57)
    assert inst.organization.reference == "Organization/2"
    assert inst.outcome.coding[0].code == "complete"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/remittance-outcome"
    assert inst.patient.reference == "Patient/pat1"
    assert inst.payee.party.reference == "Organization/2"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.payee.type.coding[0].system == "http://hl7.org/fhir/payeetype"
    assert inst.provider.reference == "Practitioner/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ExplanationOfBenefit</div>"
    )
    assert inst.text.status == "generated"
    assert inst.totalBenefit.code == "USD"
    assert inst.totalBenefit.system == "urn:iso:std:iso:4217"
    assert float(inst.totalBenefit.value) == float(96.0)
    assert inst.totalCost.code == "USD"
    assert inst.totalCost.system == "urn:iso:std:iso:4217"
    assert float(inst.totalCost.value) == float(135.57)
    assert inst.type.coding[0].code == "oral"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"


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
