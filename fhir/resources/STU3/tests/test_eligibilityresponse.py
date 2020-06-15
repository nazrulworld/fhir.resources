# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EligibilityResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import eligibilityresponse


def impl_eligibilityresponse_1(inst):
    assert inst.contained[0].id == "patient-1"
    assert inst.contained[1].id == "coverage-1"
    assert inst.created == fhirtypes.DateTime.validate("2014-09-16")
    assert inst.disposition == "Policy is currently in-force."
    assert inst.form.coding[0].code == "ELRSP/2017/01"
    assert inst.form.coding[0].system == "http://national.org/form"
    assert inst.id == "E2502"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/eligibilityresponse"
    )
    assert inst.identifier[0].value == "8812342"
    assert inst.inforce is True
    assert inst.insurance[0].benefitBalance[0].category.coding[0].code == "medical"
    assert (
        inst.insurance[0].benefitBalance[0].category.coding[0].system
        == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.code == "USD"
    assert (
        inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.value
    ) == float(500000)
    assert (
        inst.insurance[0].benefitBalance[0].financial[0].type.coding[0].code
        == "benefit"
    )
    assert inst.insurance[0].benefitBalance[0].financial[0].usedMoney.code == "USD"
    assert (
        inst.insurance[0].benefitBalance[0].financial[0].usedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[0].financial[0].usedMoney.value
    ) == float(3748.0)
    assert inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.code == "USD"
    assert (
        inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.value
    ) == float(100)
    assert (
        inst.insurance[0].benefitBalance[0].financial[1].type.coding[0].code
        == "copay-maximum"
    )
    assert inst.insurance[0].benefitBalance[0].financial[2].allowedUnsignedInt == 20
    assert (
        inst.insurance[0].benefitBalance[0].financial[2].type.coding[0].code
        == "copay-percent"
    )
    assert inst.insurance[0].benefitBalance[0].network.coding[0].code == "in"
    assert (
        inst.insurance[0].benefitBalance[0].network.coding[0].system
        == "http://hl7.org/fhir/benefit-network"
    )
    assert inst.insurance[0].benefitBalance[0].subCategory.coding[0].code == "30"
    assert (
        inst.insurance[0].benefitBalance[0].subCategory.coding[0].display
        == "Health Benefit Plan Coverage"
    )
    assert (
        inst.insurance[0].benefitBalance[0].subCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.insurance[0].benefitBalance[0].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].benefitBalance[0].term.coding[0].system
        == "http://hl7.org/fhir/benefit-term"
    )
    assert inst.insurance[0].benefitBalance[0].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].benefitBalance[0].unit.coding[0].system
        == "http://hl7.org/fhir/benefit-unit"
    )
    assert inst.insurance[0].benefitBalance[1].category.coding[0].code == "medical"
    assert (
        inst.insurance[0].benefitBalance[1].category.coding[0].system
        == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.code == "USD"
    assert (
        inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.value
    ) == float(15000)
    assert (
        inst.insurance[0].benefitBalance[1].financial[0].type.coding[0].code
        == "benefit"
    )
    assert inst.insurance[0].benefitBalance[1].network.coding[0].code == "in"
    assert (
        inst.insurance[0].benefitBalance[1].network.coding[0].system
        == "http://hl7.org/fhir/benefit-network"
    )
    assert inst.insurance[0].benefitBalance[1].subCategory.coding[0].code == "69"
    assert (
        inst.insurance[0].benefitBalance[1].subCategory.coding[0].display == "Maternity"
    )
    assert (
        inst.insurance[0].benefitBalance[1].subCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.insurance[0].benefitBalance[1].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].benefitBalance[1].term.coding[0].system
        == "http://hl7.org/fhir/benefit-term"
    )
    assert inst.insurance[0].benefitBalance[1].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].benefitBalance[1].unit.coding[0].system
        == "http://hl7.org/fhir/benefit-unit"
    )
    assert inst.insurance[0].benefitBalance[2].category.coding[0].code == "oral"
    assert (
        inst.insurance[0].benefitBalance[2].category.coding[0].system
        == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.code == "USD"
    assert (
        inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.value
    ) == float(2000)
    assert (
        inst.insurance[0].benefitBalance[2].financial[0].type.coding[0].code
        == "benefit"
    )
    assert inst.insurance[0].benefitBalance[2].network.coding[0].code == "in"
    assert (
        inst.insurance[0].benefitBalance[2].network.coding[0].system
        == "http://hl7.org/fhir/benefit-network"
    )
    assert inst.insurance[0].benefitBalance[2].subCategory.coding[0].code == "F3"
    assert (
        inst.insurance[0].benefitBalance[2].subCategory.coding[0].display
        == "Dental Coverage"
    )
    assert (
        inst.insurance[0].benefitBalance[2].subCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.insurance[0].benefitBalance[2].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].benefitBalance[2].term.coding[0].system
        == "http://hl7.org/fhir/benefit-term"
    )
    assert inst.insurance[0].benefitBalance[2].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].benefitBalance[2].unit.coding[0].system
        == "http://hl7.org/fhir/benefit-unit"
    )
    assert inst.insurance[0].benefitBalance[3].category.coding[0].code == "vision"
    assert (
        inst.insurance[0].benefitBalance[3].category.coding[0].system
        == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.insurance[0].benefitBalance[3].description == (
        "Vision products and services such as exams, glasses and " "contatc lenses."
    )
    assert inst.insurance[0].benefitBalance[3].excluded is True
    assert inst.insurance[0].benefitBalance[3].name == "Vision"
    assert inst.insurance[0].benefitBalance[3].subCategory.coding[0].code == "F6"
    assert (
        inst.insurance[0].benefitBalance[3].subCategory.coding[0].display
        == "Vision Coverage"
    )
    assert (
        inst.insurance[0].benefitBalance[3].subCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert (
        inst.insurance[0].contract.reference
        == "http://www.BenefitsInc.com/fhir/contract/NBU22547"
    )
    assert inst.insurance[0].coverage.reference == "#coverage-1"
    assert inst.insurer.reference == "Organization/2"
    assert inst.outcome.coding[0].code == "complete"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/remittance-outcome"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332405"
    )
    assert inst.requestOrganization.identifier.system == "http://national.org/clinic"
    assert inst.requestOrganization.identifier.value == "OR1234"
    assert inst.requestProvider.identifier.system == "http://national.org/provider"
    assert inst.requestProvider.identifier.value == "PR9876"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the EligibilityResponse.</div>"
    )
    assert inst.text.status == "generated"


def test_eligibilityresponse_1(base_settings):
    """No. 1 tests collection for EligibilityResponse.
    Test File: eligibilityresponse-example-benefits-2.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "eligibilityresponse-example-benefits-2.json"
    )
    inst = eligibilityresponse.EligibilityResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EligibilityResponse" == inst.resource_type

    impl_eligibilityresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EligibilityResponse" == data["resourceType"]

    inst2 = eligibilityresponse.EligibilityResponse(**data)
    impl_eligibilityresponse_1(inst2)


def impl_eligibilityresponse_2(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-09-16")
    assert inst.disposition == (
        "Eligibiliy request could not be processed, please address "
        "errors before submitting."
    )
    assert inst.error[0].code.coding[0].code == "a001"
    assert (
        inst.error[0].code.coding[0].system == "http://hl7.org/fhir/adjudication-error"
    )
    assert inst.form.coding[0].code == "ELRSP/2017/01"
    assert inst.form.coding[0].system == "http://national.org/form"
    assert inst.id == "E2503"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/eligibilityresponse"
    )
    assert inst.identifier[0].value == "8812343"
    assert inst.insurer.reference == "Organization/2"
    assert inst.outcome.coding[0].code == "error"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/remittance-outcome"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332406"
    )
    assert inst.requestOrganization.identifier.system == "http://national.org/clinic"
    assert inst.requestOrganization.identifier.value == "OR1234"
    assert inst.requestProvider.identifier.system == "http://national.org/provider"
    assert inst.requestProvider.identifier.value == "PR9876"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the EligibilityResponse.</div>"
    )
    assert inst.text.status == "generated"


def test_eligibilityresponse_2(base_settings):
    """No. 2 tests collection for EligibilityResponse.
    Test File: eligibilityresponse-example-error.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "eligibilityresponse-example-error.json"
    )
    inst = eligibilityresponse.EligibilityResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EligibilityResponse" == inst.resource_type

    impl_eligibilityresponse_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EligibilityResponse" == data["resourceType"]

    inst2 = eligibilityresponse.EligibilityResponse(**data)
    impl_eligibilityresponse_2(inst2)


def impl_eligibilityresponse_3(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.disposition == "Policy is currently in-force."
    assert inst.id == "E2500"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/eligibilityresponse"
    )
    assert inst.identifier[0].value == "881234"
    assert inst.inforce is True
    assert inst.insurer.reference == "Organization/2"
    assert inst.outcome.coding[0].code == "complete"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/remittance-outcome"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332402"
    )
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the EligibilityResponse.</div>"
    )
    assert inst.text.status == "generated"


def test_eligibilityresponse_3(base_settings):
    """No. 3 tests collection for EligibilityResponse.
    Test File: eligibilityresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "eligibilityresponse-example.json"
    inst = eligibilityresponse.EligibilityResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EligibilityResponse" == inst.resource_type

    impl_eligibilityresponse_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EligibilityResponse" == data["resourceType"]

    inst2 = eligibilityresponse.EligibilityResponse(**data)
    impl_eligibilityresponse_3(inst2)


def impl_eligibilityresponse_4(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.disposition == "Policy is currently in-force."
    assert inst.id == "E2501"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/eligibilityresponse"
    )
    assert inst.identifier[0].value == "881234"
    assert inst.inforce is True
    assert inst.insurance[0].benefitBalance[0].category.coding[0].code == "medical"
    assert (
        inst.insurance[0].benefitBalance[0].category.coding[0].system
        == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.code == "SAR"
    assert (
        inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.value
    ) == float(500000)
    assert (
        inst.insurance[0].benefitBalance[0].financial[0].type.coding[0].code
        == "benefit"
    )
    assert inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.code == "SAR"
    assert (
        inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.value
    ) == float(100)
    assert (
        inst.insurance[0].benefitBalance[0].financial[1].type.coding[0].code
        == "copay-maximum"
    )
    assert inst.insurance[0].benefitBalance[0].financial[2].allowedUnsignedInt == 20
    assert (
        inst.insurance[0].benefitBalance[0].financial[2].type.coding[0].code
        == "copay-percent"
    )
    assert inst.insurance[0].benefitBalance[0].network.coding[0].code == "in"
    assert (
        inst.insurance[0].benefitBalance[0].network.coding[0].system
        == "http://hl7.org/fhir/benefit-network"
    )
    assert inst.insurance[0].benefitBalance[0].subCategory.coding[0].code == "30"
    assert (
        inst.insurance[0].benefitBalance[0].subCategory.coding[0].display
        == "Health Benefit Plan Coverage"
    )
    assert (
        inst.insurance[0].benefitBalance[0].subCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.insurance[0].benefitBalance[0].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].benefitBalance[0].term.coding[0].system
        == "http://hl7.org/fhir/benefit-term"
    )
    assert inst.insurance[0].benefitBalance[0].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].benefitBalance[0].unit.coding[0].system
        == "http://hl7.org/fhir/benefit-unit"
    )
    assert inst.insurance[0].benefitBalance[1].category.coding[0].code == "medical"
    assert (
        inst.insurance[0].benefitBalance[1].category.coding[0].system
        == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.code == "SAR"
    assert (
        inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.value
    ) == float(15000)
    assert (
        inst.insurance[0].benefitBalance[1].financial[0].type.coding[0].code
        == "benefit"
    )
    assert inst.insurance[0].benefitBalance[1].network.coding[0].code == "in"
    assert (
        inst.insurance[0].benefitBalance[1].network.coding[0].system
        == "http://hl7.org/fhir/benefit-network"
    )
    assert inst.insurance[0].benefitBalance[1].subCategory.coding[0].code == "69"
    assert (
        inst.insurance[0].benefitBalance[1].subCategory.coding[0].display == "Maternity"
    )
    assert (
        inst.insurance[0].benefitBalance[1].subCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.insurance[0].benefitBalance[1].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].benefitBalance[1].term.coding[0].system
        == "http://hl7.org/fhir/benefit-term"
    )
    assert inst.insurance[0].benefitBalance[1].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].benefitBalance[1].unit.coding[0].system
        == "http://hl7.org/fhir/benefit-unit"
    )
    assert inst.insurance[0].benefitBalance[2].category.coding[0].code == "oral"
    assert (
        inst.insurance[0].benefitBalance[2].category.coding[0].system
        == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.code == "SAR"
    assert (
        inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.value
    ) == float(2000)
    assert (
        inst.insurance[0].benefitBalance[2].financial[0].type.coding[0].code
        == "benefit"
    )
    assert inst.insurance[0].benefitBalance[2].network.coding[0].code == "in"
    assert (
        inst.insurance[0].benefitBalance[2].network.coding[0].system
        == "http://hl7.org/fhir/benefit-network"
    )
    assert inst.insurance[0].benefitBalance[2].subCategory.coding[0].code == "F3"
    assert (
        inst.insurance[0].benefitBalance[2].subCategory.coding[0].display
        == "Dental Coverage"
    )
    assert (
        inst.insurance[0].benefitBalance[2].subCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.insurance[0].benefitBalance[2].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].benefitBalance[2].term.coding[0].system
        == "http://hl7.org/fhir/benefit-term"
    )
    assert inst.insurance[0].benefitBalance[2].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].benefitBalance[2].unit.coding[0].system
        == "http://hl7.org/fhir/benefit-unit"
    )
    assert inst.insurance[0].benefitBalance[3].category.coding[0].code == "vision"
    assert (
        inst.insurance[0].benefitBalance[3].category.coding[0].system
        == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.insurance[0].benefitBalance[3].financial[0].allowedMoney.code == "SAR"
    assert (
        inst.insurance[0].benefitBalance[3].financial[0].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[3].financial[0].allowedMoney.value
    ) == float(400)
    assert (
        inst.insurance[0].benefitBalance[3].financial[0].type.coding[0].code
        == "benefit"
    )
    assert inst.insurance[0].benefitBalance[3].network.coding[0].code == "in"
    assert (
        inst.insurance[0].benefitBalance[3].network.coding[0].system
        == "http://hl7.org/fhir/benefit-network"
    )
    assert inst.insurance[0].benefitBalance[3].subCategory.coding[0].code == "F6"
    assert (
        inst.insurance[0].benefitBalance[3].subCategory.coding[0].display
        == "Vision Coverage"
    )
    assert (
        inst.insurance[0].benefitBalance[3].subCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.insurance[0].benefitBalance[3].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].benefitBalance[3].term.coding[0].system
        == "http://hl7.org/fhir/benefit-term"
    )
    assert inst.insurance[0].benefitBalance[3].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].benefitBalance[3].unit.coding[0].system
        == "http://hl7.org/fhir/benefit-unit"
    )
    assert inst.insurance[0].benefitBalance[4].category.coding[0].code == "vision"
    assert (
        inst.insurance[0].benefitBalance[4].category.coding[0].system
        == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.insurance[0].benefitBalance[4].financial[0].allowedString == "shared"
    assert (
        inst.insurance[0].benefitBalance[4].financial[0].type.coding[0].code == "room"
    )
    assert inst.insurance[0].benefitBalance[4].financial[1].allowedMoney.code == "SAR"
    assert (
        inst.insurance[0].benefitBalance[4].financial[1].allowedMoney.system
        == "urn:iso:std:iso:4217"
    )
    assert float(
        inst.insurance[0].benefitBalance[4].financial[1].allowedMoney.value
    ) == float(600)
    assert (
        inst.insurance[0].benefitBalance[4].financial[1].type.coding[0].code
        == "benefit"
    )
    assert inst.insurance[0].benefitBalance[4].network.coding[0].code == "in"
    assert (
        inst.insurance[0].benefitBalance[4].network.coding[0].system
        == "http://hl7.org/fhir/benefit-network"
    )
    assert inst.insurance[0].benefitBalance[4].subCategory.coding[0].code == "49"
    assert (
        inst.insurance[0].benefitBalance[4].subCategory.coding[0].display
        == "Hospital Room and Board"
    )
    assert (
        inst.insurance[0].benefitBalance[4].subCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.insurance[0].benefitBalance[4].term.coding[0].code == "day"
    assert (
        inst.insurance[0].benefitBalance[4].term.coding[0].system
        == "http://hl7.org/fhir/benefit-term"
    )
    assert inst.insurance[0].benefitBalance[4].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].benefitBalance[4].unit.coding[0].system
        == "http://hl7.org/fhir/benefit-unit"
    )
    assert inst.insurer.reference == "Organization/2"
    assert inst.outcome.coding[0].code == "complete"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/remittance-outcome"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332402"
    )
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the EligibilityResponse.</div>"
    )
    assert inst.text.status == "generated"


def test_eligibilityresponse_4(base_settings):
    """No. 4 tests collection for EligibilityResponse.
    Test File: eligibilityresponse-example-benefits.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "eligibilityresponse-example-benefits.json"
    )
    inst = eligibilityresponse.EligibilityResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EligibilityResponse" == inst.resource_type

    impl_eligibilityresponse_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EligibilityResponse" == data["resourceType"]

    inst2 = eligibilityresponse.EligibilityResponse(**data)
    impl_eligibilityresponse_4(inst2)
