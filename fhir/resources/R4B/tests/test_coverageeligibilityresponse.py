# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import coverageeligibilityresponse
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_coverageeligibilityresponse_1(inst):
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-08-16"}
        ).valueDateTime
    )
    assert inst.disposition == "Policy is currently in-force."
    assert inst.id == "E2500"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse"}
        ).valueUri
    )
    assert inst.identifier[0].value == "881234"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].inforce is True
    assert inst.insurer.reference == "Organization/2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcome == "complete"
    assert inst.patient.reference == "Patient/pat1"
    assert inst.purpose[0] == "validation"
    assert inst.request.reference == (
        "http://www.BenefitsInc.com/fhir/coverageeligibilityrequest/2" "25476332402"
    )
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the CoverageEligibilityResponse.</div>"
    )
    assert inst.text.status == "generated"


def test_coverageeligibilityresponse_1(base_settings):
    """No. 1 tests collection for CoverageEligibilityResponse.
    Test File: coverageeligibilityresponse-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "coverageeligibilityresponse-example.json"
    )
    inst = coverageeligibilityresponse.CoverageEligibilityResponse.model_validate_json(
        filename.read_bytes()
    )
    assert "CoverageEligibilityResponse" == inst.get_resource_type()

    impl_coverageeligibilityresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CoverageEligibilityResponse" == data["resourceType"]

    inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(**data)
    impl_coverageeligibilityresponse_1(inst2)


def impl_coverageeligibilityresponse_2(inst):
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-09-16"}
        ).valueDateTime
    )
    assert inst.disposition == (
        "Eligibiliy request could not be processed, please address "
        "errors before submitting."
    )
    assert inst.error[0].code.coding[0].code == "a001"
    assert (
        inst.error[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/adjudication-error"}
        ).valueUri
    )
    assert inst.form.coding[0].code == "ELRSP/2017/01"
    assert (
        inst.form.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://national.org/form"}
        ).valueUri
    )
    assert inst.id == "E2503"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse"}
        ).valueUri
    )
    assert inst.identifier[0].value == "8812343"
    assert inst.insurer.reference == "Organization/2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcome == "error"
    assert inst.patient.reference == "Patient/f201"
    assert inst.purpose[0] == "validation"
    assert inst.request.reference == (
        "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse/" "225476332406"
    )
    assert (
        inst.requestor.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://national.org/clinic"}
        ).valueUri
    )
    assert inst.requestor.identifier.value == "OR1234"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the CoverageEligibilityResponse.</div>"
    )
    assert inst.text.status == "generated"


def test_coverageeligibilityresponse_2(base_settings):
    """No. 2 tests collection for CoverageEligibilityResponse.
    Test File: coverageeligibilityresponse-example-error.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "coverageeligibilityresponse-example-error.json"
    )
    inst = coverageeligibilityresponse.CoverageEligibilityResponse.model_validate_json(
        filename.read_bytes()
    )
    assert "CoverageEligibilityResponse" == inst.get_resource_type()

    impl_coverageeligibilityresponse_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CoverageEligibilityResponse" == data["resourceType"]

    inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(**data)
    impl_coverageeligibilityresponse_2(inst2)


def impl_coverageeligibilityresponse_3(inst):
    assert inst.contained[0].id == "coverage-1"
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-09-16"}
        ).valueDateTime
    )
    assert inst.disposition == "Policy is currently in-force."
    assert inst.form.coding[0].code == "ELRSP/2017/01"
    assert (
        inst.form.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://national.org/form"}
        ).valueUri
    )
    assert inst.id == "E2502"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse"}
        ).valueUri
    )
    assert inst.identifier[0].value == "8812342"
    assert inst.insurance[0].coverage.reference == "#coverage-1"
    assert inst.insurance[0].inforce is True
    assert inst.insurance[0].item[0].benefit[0].allowedMoney.currency == "USD"
    assert float(inst.insurance[0].item[0].benefit[0].allowedMoney.value) == float(
        500000
    )
    assert inst.insurance[0].item[0].benefit[0].type.coding[0].code == "benefit"
    assert inst.insurance[0].item[0].benefit[0].usedMoney.currency == "USD"
    assert float(inst.insurance[0].item[0].benefit[0].usedMoney.value) == float(3748.0)
    assert inst.insurance[0].item[0].benefit[1].allowedMoney.currency == "USD"
    assert float(inst.insurance[0].item[0].benefit[1].allowedMoney.value) == float(100)
    assert inst.insurance[0].item[0].benefit[1].type.coding[0].code == "copay-maximum"
    assert inst.insurance[0].item[0].benefit[2].allowedUnsignedInt == 20
    assert inst.insurance[0].item[0].benefit[2].type.coding[0].code == "copay-percent"
    assert inst.insurance[0].item[0].category.coding[0].code == "30"
    assert (
        inst.insurance[0].item[0].category.coding[0].display
        == "Health Benefit Plan Coverage"
    )
    assert (
        inst.insurance[0].item[0].category.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"}
        ).valueUri
    )
    assert inst.insurance[0].item[0].network.coding[0].code == "in"
    assert (
        inst.insurance[0].item[0].network.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-network"}
        ).valueUri
    )
    assert inst.insurance[0].item[0].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].item[0].term.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-term"}
        ).valueUri
    )
    assert inst.insurance[0].item[0].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].item[0].unit.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-unit"}
        ).valueUri
    )
    assert inst.insurance[0].item[1].benefit[0].allowedMoney.currency == "USD"
    assert float(inst.insurance[0].item[1].benefit[0].allowedMoney.value) == float(
        15000
    )
    assert inst.insurance[0].item[1].benefit[0].type.coding[0].code == "benefit"
    assert inst.insurance[0].item[1].category.coding[0].code == "69"
    assert inst.insurance[0].item[1].category.coding[0].display == "Maternity"
    assert (
        inst.insurance[0].item[1].category.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"}
        ).valueUri
    )
    assert inst.insurance[0].item[1].network.coding[0].code == "in"
    assert (
        inst.insurance[0].item[1].network.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-network"}
        ).valueUri
    )
    assert inst.insurance[0].item[1].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].item[1].term.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-term"}
        ).valueUri
    )
    assert inst.insurance[0].item[1].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].item[1].unit.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-unit"}
        ).valueUri
    )
    assert inst.insurance[0].item[2].benefit[0].allowedMoney.currency == "USD"
    assert float(inst.insurance[0].item[2].benefit[0].allowedMoney.value) == float(2000)
    assert inst.insurance[0].item[2].benefit[0].type.coding[0].code == "benefit"
    assert inst.insurance[0].item[2].category.coding[0].code == "F3"
    assert inst.insurance[0].item[2].category.coding[0].display == "Dental Coverage"
    assert (
        inst.insurance[0].item[2].category.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"}
        ).valueUri
    )
    assert inst.insurance[0].item[2].network.coding[0].code == "in"
    assert (
        inst.insurance[0].item[2].network.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-network"}
        ).valueUri
    )
    assert inst.insurance[0].item[2].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].item[2].term.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-term"}
        ).valueUri
    )
    assert inst.insurance[0].item[2].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].item[2].unit.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-unit"}
        ).valueUri
    )
    assert inst.insurance[0].item[3].category.coding[0].code == "F6"
    assert inst.insurance[0].item[3].category.coding[0].display == "Vision Coverage"
    assert (
        inst.insurance[0].item[3].category.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"}
        ).valueUri
    )
    assert inst.insurance[0].item[3].description == (
        "Vision products and services such as exams, glasses and " "contact lenses."
    )
    assert inst.insurance[0].item[3].excluded is True
    assert inst.insurance[0].item[3].name == "Vision"
    assert inst.insurer.reference == "Organization/2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcome == "complete"
    assert inst.patient.reference == "Patient/f201"
    assert inst.purpose[0] == "validation"
    assert inst.purpose[1] == "benefits"
    assert inst.request.reference == (
        "http://www.BenefitsInc.com/fhir/coverageeligibilityrequest/2" "25476332405"
    )
    assert (
        inst.requestor.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://national.org/clinic"}
        ).valueUri
    )
    assert inst.requestor.identifier.value == "OR1234"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the CoverageEligibilityResponse.</div>"
    )
    assert inst.text.status == "generated"


def test_coverageeligibilityresponse_3(base_settings):
    """No. 3 tests collection for CoverageEligibilityResponse.
    Test File: coverageeligibilityresponse-example-benefits-2.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "coverageeligibilityresponse-example-benefits-2.json"
    )
    inst = coverageeligibilityresponse.CoverageEligibilityResponse.model_validate_json(
        filename.read_bytes()
    )
    assert "CoverageEligibilityResponse" == inst.get_resource_type()

    impl_coverageeligibilityresponse_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CoverageEligibilityResponse" == data["resourceType"]

    inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(**data)
    impl_coverageeligibilityresponse_3(inst2)


def impl_coverageeligibilityresponse_4(inst):
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-08-16"}
        ).valueDateTime
    )
    assert inst.disposition == "Policy is currently in-force."
    assert inst.id == "E2501"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse"}
        ).valueUri
    )
    assert inst.identifier[0].value == "881234"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].inforce is True
    assert inst.insurance[0].item[0].benefit[0].allowedMoney.currency == "SAR"
    assert float(inst.insurance[0].item[0].benefit[0].allowedMoney.value) == float(
        500000
    )
    assert inst.insurance[0].item[0].benefit[0].type.coding[0].code == "benefit"
    assert inst.insurance[0].item[0].benefit[1].allowedMoney.currency == "SAR"
    assert float(inst.insurance[0].item[0].benefit[1].allowedMoney.value) == float(100)
    assert inst.insurance[0].item[0].benefit[1].type.coding[0].code == "copay-maximum"
    assert inst.insurance[0].item[0].benefit[2].allowedUnsignedInt == 20
    assert inst.insurance[0].item[0].benefit[2].type.coding[0].code == "copay-percent"
    assert inst.insurance[0].item[0].category.coding[0].code == "30"
    assert (
        inst.insurance[0].item[0].category.coding[0].display
        == "Health Benefit Plan Coverage"
    )
    assert (
        inst.insurance[0].item[0].category.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"}
        ).valueUri
    )
    assert inst.insurance[0].item[0].network.coding[0].code == "in"
    assert (
        inst.insurance[0].item[0].network.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-network"}
        ).valueUri
    )
    assert inst.insurance[0].item[0].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].item[0].term.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-term"}
        ).valueUri
    )
    assert inst.insurance[0].item[0].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].item[0].unit.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-unit"}
        ).valueUri
    )
    assert inst.insurance[0].item[1].benefit[0].allowedMoney.currency == "SAR"
    assert float(inst.insurance[0].item[1].benefit[0].allowedMoney.value) == float(
        15000
    )
    assert inst.insurance[0].item[1].benefit[0].type.coding[0].code == "benefit"
    assert inst.insurance[0].item[1].category.coding[0].code == "69"
    assert inst.insurance[0].item[1].category.coding[0].display == "Maternity"
    assert (
        inst.insurance[0].item[1].category.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"}
        ).valueUri
    )
    assert inst.insurance[0].item[1].network.coding[0].code == "in"
    assert (
        inst.insurance[0].item[1].network.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-network"}
        ).valueUri
    )
    assert inst.insurance[0].item[1].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].item[1].term.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-term"}
        ).valueUri
    )
    assert inst.insurance[0].item[1].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].item[1].unit.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-unit"}
        ).valueUri
    )
    assert inst.insurance[0].item[2].benefit[0].allowedMoney.currency == "SAR"
    assert float(inst.insurance[0].item[2].benefit[0].allowedMoney.value) == float(2000)
    assert inst.insurance[0].item[2].benefit[0].type.coding[0].code == "benefit"
    assert inst.insurance[0].item[2].category.coding[0].code == "F3"
    assert inst.insurance[0].item[2].category.coding[0].display == "Dental Coverage"
    assert (
        inst.insurance[0].item[2].category.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"}
        ).valueUri
    )
    assert inst.insurance[0].item[2].network.coding[0].code == "in"
    assert (
        inst.insurance[0].item[2].network.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-network"}
        ).valueUri
    )
    assert inst.insurance[0].item[2].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].item[2].term.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-term"}
        ).valueUri
    )
    assert inst.insurance[0].item[2].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].item[2].unit.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-unit"}
        ).valueUri
    )
    assert inst.insurance[0].item[3].benefit[0].allowedMoney.currency == "SAR"
    assert float(inst.insurance[0].item[3].benefit[0].allowedMoney.value) == float(400)
    assert inst.insurance[0].item[3].benefit[0].type.coding[0].code == "benefit"
    assert inst.insurance[0].item[3].category.coding[0].code == "F6"
    assert inst.insurance[0].item[3].category.coding[0].display == "Vision Coverage"
    assert (
        inst.insurance[0].item[3].category.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"}
        ).valueUri
    )
    assert inst.insurance[0].item[3].network.coding[0].code == "in"
    assert (
        inst.insurance[0].item[3].network.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-network"}
        ).valueUri
    )
    assert inst.insurance[0].item[3].term.coding[0].code == "annual"
    assert (
        inst.insurance[0].item[3].term.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-term"}
        ).valueUri
    )
    assert inst.insurance[0].item[3].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].item[3].unit.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-unit"}
        ).valueUri
    )
    assert inst.insurance[0].item[4].benefit[0].allowedString == "shared"
    assert inst.insurance[0].item[4].benefit[0].type.coding[0].code == "room"
    assert inst.insurance[0].item[4].benefit[1].allowedMoney.currency == "SAR"
    assert float(inst.insurance[0].item[4].benefit[1].allowedMoney.value) == float(600)
    assert inst.insurance[0].item[4].benefit[1].type.coding[0].code == "benefit"
    assert inst.insurance[0].item[4].category.coding[0].code == "49"
    assert (
        inst.insurance[0].item[4].category.coding[0].display
        == "Hospital Room and Board"
    )
    assert (
        inst.insurance[0].item[4].category.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"}
        ).valueUri
    )
    assert inst.insurance[0].item[4].network.coding[0].code == "in"
    assert (
        inst.insurance[0].item[4].network.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-network"}
        ).valueUri
    )
    assert inst.insurance[0].item[4].term.coding[0].code == "day"
    assert (
        inst.insurance[0].item[4].term.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-term"}
        ).valueUri
    )
    assert inst.insurance[0].item[4].unit.coding[0].code == "individual"
    assert (
        inst.insurance[0].item[4].unit.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/benefit-unit"}
        ).valueUri
    )
    assert inst.insurer.reference == "Organization/2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcome == "complete"
    assert inst.patient.reference == "Patient/pat1"
    assert inst.purpose[0] == "validation"
    assert inst.purpose[1] == "benefits"
    assert inst.request.reference == (
        "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse/" "225476332402"
    )
    assert (
        inst.servicedDate
        == ExternalValidatorModel.model_validate({"valueDate": "2014-09-17"}).valueDate
    )
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the CoverageEligibilityResponse.</div>"
    )
    assert inst.text.status == "generated"


def test_coverageeligibilityresponse_4(base_settings):
    """No. 4 tests collection for CoverageEligibilityResponse.
    Test File: coverageeligibilityresponse-example-benefits.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "coverageeligibilityresponse-example-benefits.json"
    )
    inst = coverageeligibilityresponse.CoverageEligibilityResponse.model_validate_json(
        filename.read_bytes()
    )
    assert "CoverageEligibilityResponse" == inst.get_resource_type()

    impl_coverageeligibilityresponse_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CoverageEligibilityResponse" == data["resourceType"]

    inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(**data)
    impl_coverageeligibilityresponse_4(inst2)
