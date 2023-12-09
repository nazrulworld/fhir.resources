# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import claim


def impl_claim_1(inst):
    assert inst.accident.date == fhirtypes.Date.validate("2014-07-09")
    assert inst.accident.locationAddress.text == "Grouse Mountain Ski Hill"
    assert inst.accident.type.coding[0].code == "SPT"
    assert inst.accident.type.coding[0].display == "Sporting Accident"
    assert (
        inst.accident.type.coding[0].system == "http://hl7.org/fhir/v3/ActIncidentCode"
    )
    assert inst.billablePeriod.end == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.billablePeriod.start == fhirtypes.DateTime.validate("2014-08-15")
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].qualification.coding[0].code == "physician"
    assert (
        inst.careTeam[0].qualification.coding[0].system
        == "http://hl7.org/fhir/provider-qualification"
    )
    assert inst.careTeam[0].responsible is True
    assert inst.careTeam[0].role.coding[0].code == "primary"
    assert (
        inst.careTeam[0].role.coding[0].system
        == "http://hl7.org/fhir/claim-careteamrole"
    )
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654456"
    assert inst.diagnosis[0].packageCode.coding[0].code == "400"
    assert inst.diagnosis[0].packageCode.coding[0].display == "Head trauma - concussion"
    assert (
        inst.diagnosis[0].packageCode.coding[0].system
        == "http://hl7.org/fhir/ex-diagnosisrelatedgroup"
    )
    assert inst.diagnosis[0].sequence == 1
    assert inst.diagnosis[0].type[0].coding[0].code == "admitting"
    assert (
        inst.diagnosis[0].type[0].coding[0].system
        == "http://hl7.org/fhir/ex-diagnosistype"
    )
    assert inst.employmentImpacted.end == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.employmentImpacted.start == fhirtypes.DateTime.validate("2014-08-16")
    assert (
        inst.enterer.identifier.system
        == "http://jurisdiction.org/facilities/HOSP1234/users"
    )
    assert inst.enterer.identifier.value == "UC1234"
    assert inst.facility.identifier.system == "http://jurisdiction.org/facilities"
    assert inst.facility.identifier.value == "HOSP1234"
    assert inst.hospitalization.end == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.hospitalization.start == fhirtypes.DateTime.validate("2014-08-15")
    assert inst.id == "960151"
    assert inst.identifier[0].system == "http://happyhospital.com/claim"
    assert inst.identifier[0].value == "96123451"
    assert inst.insurance[0].businessArrangement == "BA987123"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].preAuthRef[0] == "PA2014G56473"
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(125.0)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "exam"
    assert (
        inst.item[0].service.coding[0].system == "http://hl7.org/fhir/ex-serviceproduct"
    )
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(125.0)
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.identifier.system == "http://npid.org/providerid"
    assert inst.provider.identifier.value == "NJ12345"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total.code == "USD"
    assert inst.total.system == "urn:iso:std:iso:4217"
    assert float(inst.total.value) == float(125.0)
    assert inst.type.coding[0].code == "institutional"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "complete"


def test_claim_1(base_settings):
    """No. 1 tests collection for Claim.
    Test File: claim-example-institutional-rich.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "claim-example-institutional-rich.json"
    )
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_1(inst2)


def impl_claim_2(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "860150"
    assert inst.identifier[0].system == "http://happypdocs.com/claim"
    assert inst.identifier[0].value == "8612345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(75.0)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "exam"
    assert (
        inst.item[0].service.coding[0].system == "http://hl7.org/fhir/ex-serviceproduct"
    )
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(75.0)
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "professional"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "complete"


def test_claim_2(base_settings):
    """No. 2 tests collection for Claim.
    Test File: claim-example-professional.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-professional.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_2(inst2)


def impl_claim_3(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "123456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "100150"
    assert inst.identifier[0].system == "http://happyvalley.com/claim"
    assert inst.identifier[0].value == "12345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(135.57)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "1200"
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(135.57)
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Oral Health Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "oral"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "complete"


def test_claim_3(base_settings):
    """No. 3 tests collection for Claim.
    Test File: claim-example.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_3(inst2)


def impl_claim_4(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654321"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "660150"
    assert inst.identifier[0].system == "http://happysight.com/claim"
    assert inst.identifier[0].value == "6612345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(80.0)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "exam"
    assert (
        inst.item[0].service.coding[0].system == "http://hl7.org/fhir/ex-visionservice"
    )
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(80.0)
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Vision Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "vision"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "complete"


def test_claim_4(base_settings):
    """No. 4 tests collection for Claim.
    Test File: claim-example-vision.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-vision.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_4(inst2)


def impl_claim_5(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.contained[0].id == "claimresponse-1"
    assert inst.contained[1].id == "device-frame"
    assert inst.contained[2].id == "device-lens"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654321"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "660152"
    assert inst.identifier[0].system == "http://happysight.com/claim"
    assert inst.identifier[0].value == "6612347"
    assert inst.insurance[0].claimResponse.reference == "#claimresponse-1"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is False
    assert inst.insurance[0].preAuthRef[0] == "PR7652387237"
    assert inst.insurance[0].sequence == 1
    assert inst.insurance[1].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[1].focal is True
    assert inst.insurance[1].preAuthRef[0] == "AB543GTD7567"
    assert inst.insurance[1].sequence == 2
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].category.coding[0].code == "F6"
    assert inst.item[0].category.coding[0].display == "Vision Coverage"
    assert (
        inst.item[0].category.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.item[0].detail[0].category.coding[0].code == "F6"
    assert inst.item[0].detail[0].category.coding[0].display == "Vision Coverage"
    assert (
        inst.item[0].detail[0].category.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert float(inst.item[0].detail[0].factor) == float(1.1)
    assert inst.item[0].detail[0].modifier[0].coding[0].code == "rooh"
    assert (
        inst.item[0].detail[0].modifier[0].coding[0].system
        == "http://hl7.org/fhir/modifiers"
    )
    assert inst.item[0].detail[0].net.code == "USD"
    assert inst.item[0].detail[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[0].net.value) == float(110.0)
    assert inst.item[0].detail[0].revenue.coding[0].code == "0010"
    assert inst.item[0].detail[0].revenue.coding[0].display == "Vision Clinic"
    assert (
        inst.item[0].detail[0].revenue.coding[0].system
        == "http://hl7.org/fhir/ex-revenue-center"
    )
    assert inst.item[0].detail[0].sequence == 1
    assert inst.item[0].detail[0].service.coding[0].code == "frame"
    assert (
        inst.item[0].detail[0].service.coding[0].system
        == "http://hl7.org/fhir/ex-visionservice"
    )
    assert inst.item[0].detail[0].udi[0].reference == "#device-frame"
    assert inst.item[0].detail[0].unitPrice.code == "USD"
    assert inst.item[0].detail[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[0].unitPrice.value) == float(100.0)
    assert inst.item[0].detail[1].category.coding[0].code == "F6"
    assert inst.item[0].detail[1].category.coding[0].display == "Vision Coverage"
    assert (
        inst.item[0].detail[1].category.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.item[0].detail[1].net.code == "USD"
    assert inst.item[0].detail[1].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[1].net.value) == float(110.0)
    assert inst.item[0].detail[1].programCode[0].coding[0].code == "none"
    assert (
        inst.item[0].detail[1].programCode[0].coding[0].system
        == "http://hl7.org/fhir/ex-programcode"
    )
    assert float(inst.item[0].detail[1].quantity.value) == float(2)
    assert inst.item[0].detail[1].revenue.coding[0].code == "0010"
    assert inst.item[0].detail[1].revenue.coding[0].display == "Vision Clinic"
    assert (
        inst.item[0].detail[1].revenue.coding[0].system
        == "http://hl7.org/fhir/ex-revenue-center"
    )
    assert inst.item[0].detail[1].sequence == 2
    assert inst.item[0].detail[1].service.coding[0].code == "lens"
    assert (
        inst.item[0].detail[1].service.coding[0].system
        == "http://hl7.org/fhir/ex-visionservice"
    )
    assert inst.item[0].detail[1].subDetail[0].category.coding[0].code == "F6"
    assert (
        inst.item[0].detail[1].subDetail[0].category.coding[0].display
        == "Vision Coverage"
    )
    assert (
        inst.item[0].detail[1].subDetail[0].category.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert float(inst.item[0].detail[1].subDetail[0].factor) == float(1.1)
    assert inst.item[0].detail[1].subDetail[0].modifier[0].coding[0].code == "rooh"
    assert (
        inst.item[0].detail[1].subDetail[0].modifier[0].coding[0].system
        == "http://hl7.org/fhir/modifiers"
    )
    assert inst.item[0].detail[1].subDetail[0].net.code == "USD"
    assert inst.item[0].detail[1].subDetail[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[1].subDetail[0].net.value) == float(66.0)
    assert inst.item[0].detail[1].subDetail[0].programCode[0].coding[0].code == "none"
    assert (
        inst.item[0].detail[1].subDetail[0].programCode[0].coding[0].system
        == "http://hl7.org/fhir/ex-programcode"
    )
    assert float(inst.item[0].detail[1].subDetail[0].quantity.value) == float(2)
    assert inst.item[0].detail[1].subDetail[0].revenue.coding[0].code == "0010"
    assert (
        inst.item[0].detail[1].subDetail[0].revenue.coding[0].display == "Vision Clinic"
    )
    assert (
        inst.item[0].detail[1].subDetail[0].revenue.coding[0].system
        == "http://hl7.org/fhir/ex-revenue-center"
    )
    assert inst.item[0].detail[1].subDetail[0].sequence == 1
    assert inst.item[0].detail[1].subDetail[0].service.coding[0].code == "lens"
    assert (
        inst.item[0].detail[1].subDetail[0].service.coding[0].system
        == "http://hl7.org/fhir/ex-visionservice"
    )
    assert inst.item[0].detail[1].subDetail[0].udi[0].reference == "#device-lens"
    assert inst.item[0].detail[1].subDetail[0].unitPrice.code == "USD"
    assert (
        inst.item[0].detail[1].subDetail[0].unitPrice.system == "urn:iso:std:iso:4217"
    )
    assert float(inst.item[0].detail[1].subDetail[0].unitPrice.value) == float(30.0)
    assert inst.item[0].detail[1].subDetail[1].category.coding[0].code == "F6"
    assert (
        inst.item[0].detail[1].subDetail[1].category.coding[0].display
        == "Vision Coverage"
    )
    assert (
        inst.item[0].detail[1].subDetail[1].category.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert float(inst.item[0].detail[1].subDetail[1].factor) == float(1.1)
    assert inst.item[0].detail[1].subDetail[1].modifier[0].coding[0].code == "rooh"
    assert (
        inst.item[0].detail[1].subDetail[1].modifier[0].coding[0].system
        == "http://hl7.org/fhir/modifiers"
    )
    assert inst.item[0].detail[1].subDetail[1].net.code == "USD"
    assert inst.item[0].detail[1].subDetail[1].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[1].subDetail[1].net.value) == float(33.0)
    assert float(inst.item[0].detail[1].subDetail[1].quantity.value) == float(2)
    assert inst.item[0].detail[1].subDetail[1].revenue.coding[0].code == "0010"
    assert (
        inst.item[0].detail[1].subDetail[1].revenue.coding[0].display == "Vision Clinic"
    )
    assert (
        inst.item[0].detail[1].subDetail[1].revenue.coding[0].system
        == "http://hl7.org/fhir/ex-revenue-center"
    )
    assert inst.item[0].detail[1].subDetail[1].sequence == 2
    assert inst.item[0].detail[1].subDetail[1].service.coding[0].code == "hardening"
    assert (
        inst.item[0].detail[1].subDetail[1].service.coding[0].system
        == "http://hl7.org/fhir/ex-visionservice"
    )
    assert inst.item[0].detail[1].subDetail[1].unitPrice.code == "USD"
    assert (
        inst.item[0].detail[1].subDetail[1].unitPrice.system == "urn:iso:std:iso:4217"
    )
    assert float(inst.item[0].detail[1].subDetail[1].unitPrice.value) == float(15.0)
    assert inst.item[0].detail[1].subDetail[2].category.coding[0].code == "F6"
    assert (
        inst.item[0].detail[1].subDetail[2].category.coding[0].display
        == "Vision Coverage"
    )
    assert (
        inst.item[0].detail[1].subDetail[2].category.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert float(inst.item[0].detail[1].subDetail[2].factor) == float(1.1)
    assert inst.item[0].detail[1].subDetail[2].modifier[0].coding[0].code == "rooh"
    assert (
        inst.item[0].detail[1].subDetail[2].modifier[0].coding[0].system
        == "http://hl7.org/fhir/modifiers"
    )
    assert inst.item[0].detail[1].subDetail[2].net.code == "USD"
    assert inst.item[0].detail[1].subDetail[2].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[1].subDetail[2].net.value) == float(11.0)
    assert float(inst.item[0].detail[1].subDetail[2].quantity.value) == float(2)
    assert inst.item[0].detail[1].subDetail[2].revenue.coding[0].code == "0010"
    assert (
        inst.item[0].detail[1].subDetail[2].revenue.coding[0].display == "Vision Clinic"
    )
    assert (
        inst.item[0].detail[1].subDetail[2].revenue.coding[0].system
        == "http://hl7.org/fhir/ex-revenue-center"
    )
    assert inst.item[0].detail[1].subDetail[2].sequence == 3
    assert inst.item[0].detail[1].subDetail[2].service.coding[0].code == "UV coating"
    assert (
        inst.item[0].detail[1].subDetail[2].service.coding[0].system
        == "http://hl7.org/fhir/ex-visionservice"
    )
    assert inst.item[0].detail[1].subDetail[2].unitPrice.code == "USD"
    assert (
        inst.item[0].detail[1].subDetail[2].unitPrice.system == "urn:iso:std:iso:4217"
    )
    assert float(inst.item[0].detail[1].subDetail[2].unitPrice.value) == float(5.0)
    assert inst.item[0].detail[1].unitPrice.code == "USD"
    assert inst.item[0].detail[1].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[1].unitPrice.value) == float(55.0)
    assert inst.item[0].detail[2].category.coding[0].code == "F6"
    assert inst.item[0].detail[2].category.coding[0].display == "Vision Coverage"
    assert (
        inst.item[0].detail[2].category.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert float(inst.item[0].detail[2].factor) == float(0.07)
    assert inst.item[0].detail[2].net.code == "USD"
    assert inst.item[0].detail[2].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[2].net.value) == float(15.4)
    assert inst.item[0].detail[2].revenue.coding[0].code == "0010"
    assert inst.item[0].detail[2].revenue.coding[0].display == "Vision Clinic"
    assert (
        inst.item[0].detail[2].revenue.coding[0].system
        == "http://hl7.org/fhir/ex-revenue-center"
    )
    assert inst.item[0].detail[2].sequence == 3
    assert inst.item[0].detail[2].service.coding[0].code == "fst"
    assert (
        inst.item[0].detail[2].service.coding[0].system
        == "http://hl7.org/fhir/ex-visionservice"
    )
    assert inst.item[0].detail[2].unitPrice.code == "USD"
    assert inst.item[0].detail[2].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[2].unitPrice.value) == float(220.0)
    assert inst.item[0].modifier[0].coding[0].code == "rooh"
    assert inst.item[0].modifier[0].coding[0].system == "http://hl7.org/fhir/modifiers"
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(235.4)
    assert inst.item[0].programCode[0].coding[0].code == "none"
    assert (
        inst.item[0].programCode[0].coding[0].system
        == "http://hl7.org/fhir/ex-programcode"
    )
    assert inst.item[0].revenue.coding[0].code == "0010"
    assert inst.item[0].revenue.coding[0].display == "Vision Clinic"
    assert (
        inst.item[0].revenue.coding[0].system == "http://hl7.org/fhir/ex-revenue-center"
    )
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "glasses"
    assert (
        inst.item[0].service.coding[0].system == "http://hl7.org/fhir/ex-visionservice"
    )
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(235.4)
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.prescription.reference == "http://www.optdocs.com/prescription/12345"
    assert inst.priority.coding[0].code == "normal"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Vision Claim for Glasses</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "vision"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "complete"


def test_claim_5(base_settings):
    """No. 5 tests collection for Claim.
    Test File: claim-example-vision-glasses-3tier.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "claim-example-vision-glasses-3tier.json"
    )
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_5(inst2)


def impl_claim_6(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654456"
    assert inst.diagnosis[0].sequence == 1
    assert (
        inst.enterer.identifier.system
        == "http://jurisdiction.org/facilities/HOSP1234/users"
    )
    assert inst.enterer.identifier.value == "UC1234"
    assert inst.facility.identifier.system == "http://jurisdiction.org/facilities"
    assert inst.facility.identifier.value == "HOSP1234"
    assert inst.id == "960150"
    assert inst.identifier[0].system == "http://happyhospital.com/claim"
    assert inst.identifier[0].value == "9612345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].encounter[0].reference == "Encounter/example"
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(125.0)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "exam"
    assert (
        inst.item[0].service.coding[0].system == "http://hl7.org/fhir/ex-serviceproduct"
    )
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(125.0)
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.status == "active"
    assert inst.subType[0].coding[0].code == "emergency"
    assert inst.subType[0].coding[0].system == "http://hl7.org/fhir/ex-claimsubtype"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total.code == "USD"
    assert inst.total.system == "urn:iso:std:iso:4217"
    assert float(inst.total.value) == float(125.0)
    assert inst.type.coding[0].code == "institutional"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "complete"


def test_claim_6(base_settings):
    """No. 6 tests collection for Claim.
    Test File: claim-example-institutional.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-institutional.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_6(inst2)


def impl_claim_7(inst):
    assert inst.careTeam[0].provider.reference == "#provider-1"
    assert inst.careTeam[0].sequence == 1
    assert inst.contained[0].id == "org-insurer"
    assert inst.contained[1].id == "org-org"
    assert inst.contained[2].id == "provider-1"
    assert inst.contained[3].id == "patient-1"
    assert inst.contained[4].id == "coverage-1"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "123456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "100152"
    assert inst.identifier[0].system == "http://happyvalley.com/claim"
    assert inst.identifier[0].value == "12347"
    assert inst.insurance[0].coverage.reference == "#coverage-1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "#org-insurer"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(135.57)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "1200"
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(135.57)
    assert inst.organization.reference == "#org-org"
    assert inst.patient.reference == "#patient-1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Oral Health Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "oral"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "complete"


def test_claim_7(base_settings):
    """No. 7 tests collection for Claim.
    Test File: claim-example-oral-contained.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-oral-contained.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_7(inst2)


def impl_claim_8(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "654456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "760151"
    assert inst.identifier[0].system == "http://happypharma.com/claim"
    assert inst.identifier[0].value == "7612345"
    assert inst.information[0].category.coding[0].code == "pharmacyrefill"
    assert inst.information[0].code.coding[0].code == "new"
    assert (
        inst.information[0].code.coding[0].system
        == "http://hl7.org/fhir/pharmacy-refill"
    )
    assert inst.information[0].sequence == 1
    assert inst.information[1].category.coding[0].code == "pharmacyinformation"
    assert inst.information[1].code.coding[0].code == "refillsremaining"
    assert (
        inst.information[1].code.coding[0].system
        == "http://hl7.org/fhir/pharmacy-information"
    )
    assert inst.information[1].sequence == 2
    assert float(inst.information[1].valueQuantity.value) == float(2)
    assert inst.information[2].category.coding[0].code == "pharmacyinformation"
    assert inst.information[2].code.coding[0].code == "dayssupply"
    assert (
        inst.information[2].code.coding[0].system
        == "http://hl7.org/fhir/pharmacy-information"
    )
    assert inst.information[2].sequence == 3
    assert float(inst.information[2].valueQuantity.value) == float(90)
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].detail[0].net.code == "USD"
    assert inst.item[0].detail[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[0].net.value) == float(45.0)
    assert inst.item[0].detail[0].sequence == 1
    assert inst.item[0].detail[0].service.coding[0].code == "drugcost"
    assert (
        inst.item[0].detail[0].service.coding[0].system
        == "http://hl7.org/fhir/ex-pharmaservice"
    )
    assert inst.item[0].detail[1].net.code == "USD"
    assert inst.item[0].detail[1].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[1].net.value) == float(9.0)
    assert inst.item[0].detail[1].sequence == 2
    assert inst.item[0].detail[1].service.coding[0].code == "markup"
    assert (
        inst.item[0].detail[1].service.coding[0].system
        == "http://hl7.org/fhir/ex-pharmaservice"
    )
    assert inst.item[0].detail[2].net.code == "USD"
    assert inst.item[0].detail[2].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[2].net.value) == float(36.0)
    assert inst.item[0].detail[2].sequence == 3
    assert inst.item[0].detail[2].service.coding[0].code == "dispensefee"
    assert (
        inst.item[0].detail[2].service.coding[0].system
        == "http://hl7.org/fhir/ex-pharmaservice"
    )
    assert inst.item[0].informationLinkId[0] == 1
    assert inst.item[0].informationLinkId[1] == 2
    assert inst.item[0].informationLinkId[2] == 3
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(90.0)
    assert inst.item[0].quantity.code == "TAB"
    assert inst.item[0].quantity.system == "http://unitsofmeasure.org"
    assert inst.item[0].quantity.unit == "TAB"
    assert float(inst.item[0].quantity.value) == float(90)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "562721"
    assert inst.item[0].service.coding[0].display == "Alprazolam 0.25mg (Xanax)"
    assert inst.item[0].service.coding[0].system == "http://hl7.org/fhir/RxNorm"
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.organization.reference == "Organization/1"
    assert (
        inst.originalPrescription.reference
        == "http://pharmacy.org/MedicationRequest/AB1202B"
    )
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert (
        inst.prescription.reference == "http://pharmacy.org/MedicationRequest/AB1234G"
    )
    assert inst.priority.coding[0].code == "stat"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Pharmacy Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total.code == "USD"
    assert inst.total.system == "urn:iso:std:iso:4217"
    assert float(inst.total.value) == float(90.0)
    assert inst.type.coding[0].code == "pharmacy"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "complete"


def test_claim_8(base_settings):
    """No. 8 tests collection for Claim.
    Test File: claim-example-pharmacy-medication.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "claim-example-pharmacy-medication.json"
    )
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_8(inst2)


def impl_claim_9(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2015-03-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "123457"
    assert (
        inst.diagnosis[0].diagnosisCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/sid/icd-10"
    )
    assert inst.diagnosis[0].sequence == 1
    assert inst.fundsReserve.coding[0].code == "provider"
    assert inst.id == "100153"
    assert inst.identifier[0].system == "http://happyvalley.com/claim"
    assert inst.identifier[0].value == "12355"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].detail[0].net.code == "USD"
    assert inst.item[0].detail[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[0].net.value) == float(1000.0)
    assert inst.item[0].detail[0].sequence == 1
    assert inst.item[0].detail[0].service.coding[0].code == "ORTHOEXAM"
    assert (
        inst.item[0].detail[0].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[0].detail[0].unitPrice.code == "USD"
    assert inst.item[0].detail[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[0].unitPrice.value) == float(1000.0)
    assert inst.item[0].detail[1].net.code == "USD"
    assert inst.item[0].detail[1].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[1].net.value) == float(1500.0)
    assert inst.item[0].detail[1].sequence == 2
    assert inst.item[0].detail[1].service.coding[0].code == "ORTHODIAG"
    assert (
        inst.item[0].detail[1].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[0].detail[1].unitPrice.code == "USD"
    assert inst.item[0].detail[1].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[1].unitPrice.value) == float(1500.0)
    assert inst.item[0].detail[2].net.code == "USD"
    assert inst.item[0].detail[2].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[2].net.value) == float(500.0)
    assert inst.item[0].detail[2].sequence == 3
    assert inst.item[0].detail[2].service.coding[0].code == "ORTHOINITIAL"
    assert (
        inst.item[0].detail[2].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[0].detail[2].unitPrice.code == "USD"
    assert inst.item[0].detail[2].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[2].unitPrice.value) == float(500.0)
    assert float(inst.item[0].detail[3].quantity.value) == float(24)
    assert inst.item[0].detail[3].sequence == 4
    assert inst.item[0].detail[3].service.coding[0].code == "ORTHOMONTHS"
    assert (
        inst.item[0].detail[3].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[0].detail[4].net.code == "USD"
    assert inst.item[0].detail[4].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[4].net.value) == float(250.0)
    assert float(inst.item[0].detail[4].quantity.value) == float(24)
    assert inst.item[0].detail[4].sequence == 5
    assert inst.item[0].detail[4].service.coding[0].code == "ORTHOPERIODIC"
    assert (
        inst.item[0].detail[4].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[0].detail[4].unitPrice.code == "USD"
    assert inst.item[0].detail[4].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].detail[4].unitPrice.value) == float(250.0)
    assert inst.item[0].diagnosisLinkId[0] == 1
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(9000.0)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "ORTHPLAN"
    assert (
        inst.item[0].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2015-05-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(9000.0)
    assert inst.item[1].bodySite.coding[0].code == "21"
    assert (
        inst.item[1].bodySite.coding[0].system == "http://fdi.org/fhir/oraltoothcodes"
    )
    assert inst.item[1].careTeamLinkId[0] == 1
    assert inst.item[1].net.code == "USD"
    assert inst.item[1].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[1].net.value) == float(105.0)
    assert inst.item[1].sequence == 2
    assert inst.item[1].service.coding[0].code == "21211"
    assert (
        inst.item[1].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[1].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[1].subSite[0].coding[0].code == "L"
    assert (
        inst.item[1].subSite[0].coding[0].system
        == "http://fdi.org/fhir/oralsurfacecodes"
    )
    assert inst.item[1].unitPrice.code == "USD"
    assert inst.item[1].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[1].unitPrice.value) == float(105.0)
    assert inst.item[2].bodySite.coding[0].code == "36"
    assert (
        inst.item[2].bodySite.coding[0].system == "http://fdi.org/fhir/oraltoothcodes"
    )
    assert inst.item[2].careTeamLinkId[0] == 1
    assert inst.item[2].detail[0].net.code == "USD"
    assert inst.item[2].detail[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].detail[0].net.value) == float(750.0)
    assert inst.item[2].detail[0].sequence == 1
    assert inst.item[2].detail[0].service.coding[0].code == "27211"
    assert (
        inst.item[2].detail[0].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[2].detail[0].unitPrice.code == "USD"
    assert inst.item[2].detail[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].detail[0].unitPrice.value) == float(750.0)
    assert inst.item[2].detail[1].net.code == "USD"
    assert inst.item[2].detail[1].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].detail[1].net.value) == float(350.0)
    assert inst.item[2].detail[1].sequence == 2
    assert inst.item[2].detail[1].service.coding[0].code == "lab"
    assert (
        inst.item[2].detail[1].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[2].detail[1].unitPrice.code == "USD"
    assert inst.item[2].detail[1].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].detail[1].unitPrice.value) == float(350.0)
    assert inst.item[2].net.code == "USD"
    assert inst.item[2].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].net.value) == float(1100.0)
    assert inst.item[2].sequence == 3
    assert inst.item[2].service.coding[0].code == "27211"
    assert (
        inst.item[2].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[2].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[2].unitPrice.code == "USD"
    assert inst.item[2].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].unitPrice.value) == float(1100.0)
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Oral Health Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "oral"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "proposed"


def test_claim_9(base_settings):
    """No. 9 tests collection for Claim.
    Test File: claim-example-oral-orthoplan.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-oral-orthoplan.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_9(inst2)


def impl_claim_10(inst):
    assert inst.careTeam[0].provider.reference == "Practitioner/example"
    assert inst.careTeam[0].sequence == 1
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code == "123456"
    assert inst.diagnosis[0].sequence == 1
    assert inst.id == "100151"
    assert inst.identifier[0].system == "http://happyvalley.com/claim"
    assert inst.identifier[0].value == "12346"
    assert inst.information[0].category.coding[0].code == "missingtooth"
    assert (
        inst.information[0].category.coding[0].system
        == "http://hl7.org/fhir/claiminformationcategory"
    )
    assert inst.information[0].code.coding[0].code == "15"
    assert inst.information[0].code.coding[0].system == "http://hl7.org/fhir/ex-tooth"
    assert inst.information[0].reason.coding[0].code == "e"
    assert (
        inst.information[0].reason.coding[0].system
        == "http://hl7.org/fhir/missingtoothreason"
    )
    assert inst.information[0].sequence == 1
    assert inst.information[0].timingDate == fhirtypes.Date.validate("2012-04-07")
    assert inst.information[1].category.coding[0].code == "exception"
    assert (
        inst.information[1].category.coding[0].system
        == "http://hl7.org/fhir/claiminformationcategory"
    )
    assert inst.information[1].code.coding[0].code == "student"
    assert (
        inst.information[1].code.coding[0].system
        == "http://hl7.org/fhir/claim-exception"
    )
    assert inst.information[1].sequence == 2
    assert inst.information[1].valueString == "Happy Valley Community College"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurance[0].sequence == 1
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].careTeamLinkId[0] == 1
    assert inst.item[0].net.code == "USD"
    assert inst.item[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].net.value) == float(135.57)
    assert inst.item[0].sequence == 1
    assert inst.item[0].service.coding[0].code == "1200"
    assert (
        inst.item[0].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[0].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[0].unitPrice.code == "USD"
    assert inst.item[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].unitPrice.value) == float(135.57)
    assert inst.item[1].bodySite.coding[0].code == "21"
    assert (
        inst.item[1].bodySite.coding[0].system == "http://fdi.org/fhir/oraltoothcodes"
    )
    assert inst.item[1].careTeamLinkId[0] == 1
    assert inst.item[1].net.code == "USD"
    assert inst.item[1].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[1].net.value) == float(105.0)
    assert inst.item[1].sequence == 2
    assert inst.item[1].service.coding[0].code == "21211"
    assert (
        inst.item[1].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[1].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[1].subSite[0].coding[0].code == "L"
    assert (
        inst.item[1].subSite[0].coding[0].system
        == "http://fdi.org/fhir/oralsurfacecodes"
    )
    assert inst.item[1].unitPrice.code == "USD"
    assert inst.item[1].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[1].unitPrice.value) == float(105.0)
    assert inst.item[2].bodySite.coding[0].code == "36"
    assert (
        inst.item[2].bodySite.coding[0].system == "http://fdi.org/fhir/oraltoothcodes"
    )
    assert inst.item[2].careTeamLinkId[0] == 1
    assert float(inst.item[2].detail[0].factor) == float(0.75)
    assert inst.item[2].detail[0].net.code == "USD"
    assert inst.item[2].detail[0].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].detail[0].net.value) == float(750.0)
    assert inst.item[2].detail[0].sequence == 1
    assert inst.item[2].detail[0].service.coding[0].code == "27211"
    assert (
        inst.item[2].detail[0].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[2].detail[0].unitPrice.code == "USD"
    assert inst.item[2].detail[0].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].detail[0].unitPrice.value) == float(1000.0)
    assert inst.item[2].detail[1].net.code == "USD"
    assert inst.item[2].detail[1].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].detail[1].net.value) == float(350.0)
    assert inst.item[2].detail[1].sequence == 2
    assert inst.item[2].detail[1].service.coding[0].code == "lab"
    assert (
        inst.item[2].detail[1].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[2].detail[1].unitPrice.code == "USD"
    assert inst.item[2].detail[1].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].detail[1].unitPrice.value) == float(350.0)
    assert inst.item[2].net.code == "USD"
    assert inst.item[2].net.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].net.value) == float(1100.0)
    assert inst.item[2].sequence == 3
    assert inst.item[2].service.coding[0].code == "27211"
    assert (
        inst.item[2].service.coding[0].system
        == "http://example.org/fhir/oralservicecodes"
    )
    assert inst.item[2].servicedDate == fhirtypes.Date.validate("2014-08-16")
    assert inst.item[2].unitPrice.code == "USD"
    assert inst.item[2].unitPrice.system == "urn:iso:std:iso:4217"
    assert float(inst.item[2].unitPrice.value) == float(1100.0)
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/1"
    assert inst.payee.type.coding[0].code == "provider"
    assert inst.priority.coding[0].code == "normal"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the Oral Health Claim</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "oral"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/ex-claimtype"
    assert inst.use == "complete"


def test_claim_10(base_settings):
    """No. 10 tests collection for Claim.
    Test File: claim-example-oral-average.json
    """
    filename = base_settings["unittest_data_dir"] / "claim-example-oral-average.json"
    inst = claim.Claim.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Claim" == inst.resource_type

    impl_claim_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Claim" == data["resourceType"]

    inst2 = claim.Claim(**data)
    impl_claim_10(inst2)
