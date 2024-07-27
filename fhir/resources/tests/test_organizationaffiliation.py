# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import organizationaffiliation
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_organizationaffiliation_1(inst):
    assert inst.active is True
    assert inst.code[0].coding[0].code == "provider"
    assert (
        inst.code[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/organization-role"
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "general.practice@example.org"
    assert inst.endpoint[0].reference == "Endpoint/example"
    assert inst.healthcareService[0].reference == "HealthcareService/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="http://www.acme.org/practitioners").valueUri
    )
    assert inst.identifier[0].value == "23"
    assert inst.location[0].display == "South Wing, second floor"
    assert inst.location[0].reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.network[0].display == "HL7 Payer Network"
    assert inst.network[0].reference == "Organization/hl7pay"
    assert inst.organization.reference == "Organization/hl7pay"
    assert inst.participatingOrganization.reference == "Organization/f001"
    assert (
        inst.period.end
        == ExternalValidatorModel(valueDateTime="2012-03-31").valueDateTime
    )
    assert (
        inst.period.start
        == ExternalValidatorModel(valueDateTime="2012-01-01").valueDateTime
    )
    assert inst.specialty[0].coding[0].code == "408443003"
    assert inst.specialty[0].coding[0].display == "General medical practice"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.text.status == "generated"


def test_organizationaffiliation_1(base_settings):
    """No. 1 tests collection for OrganizationAffiliation.
    Test File: organizationaffiliation-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "organizationaffiliation-example.json"
    )
    inst = organizationaffiliation.OrganizationAffiliation.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "OrganizationAffiliation" == inst.get_resource_type()

    impl_organizationaffiliation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OrganizationAffiliation" == data["resourceType"]

    inst2 = organizationaffiliation.OrganizationAffiliation(**data)
    impl_organizationaffiliation_1(inst2)


def impl_organizationaffiliation_2(inst):
    assert inst.active is True
    assert inst.code[0].coding[0].code == "member"
    assert inst.code[0].coding[0].display == "Member"
    assert (
        inst.code[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/organization-role"
        ).valueUri
    )
    assert inst.code[0].text == "Hospital member"
    assert inst.endpoint[0].display == "Founding Fathers Memorial Hospital HIE endpoint"
    assert inst.id == "orgrole2"
    assert inst.identifier[0].assigner.display == "Monument Health Information Exchange"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://example.org/www.monumentHIE.com"
        ).valueUri
    )
    assert inst.identifier[0].type.text == "member hospital"
    assert inst.identifier[0].use == "secondary"
    assert inst.identifier[0].value == "hosp32"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.organization.display == "Monument Health Information Exchange"
    assert (
        inst.participatingOrganization.display == "Founding Fathers Memorial Hospital"
    )
    assert inst.text.status == "generated"


def test_organizationaffiliation_2(base_settings):
    """No. 2 tests collection for OrganizationAffiliation.
    Test File: orgrole-example-hie.json
    """
    filename = base_settings["unittest_data_dir"] / "orgrole-example-hie.json"
    inst = organizationaffiliation.OrganizationAffiliation.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "OrganizationAffiliation" == inst.get_resource_type()

    impl_organizationaffiliation_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OrganizationAffiliation" == data["resourceType"]

    inst2 = organizationaffiliation.OrganizationAffiliation(**data)
    impl_organizationaffiliation_2(inst2)


def impl_organizationaffiliation_3(inst):
    assert inst.active is True
    assert inst.code[0].coding[0].code == "provider"
    assert inst.code[0].coding[0].display == "Provider"
    assert (
        inst.code[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/organization-role"
        ).valueUri
    )
    assert inst.code[0].coding[0].userSelected is True
    assert inst.code[0].text == "Provider of rehabilitation services"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "202-109-8765"
    assert inst.healthcareService[0].display == "Inpatient rehabilitation services"
    assert inst.healthcareService[1].display == "Outpatient rehabilitation services"
    assert inst.id == "orgrole1"
    assert inst.identifier[0].assigner.display == "Founding Fathers Memorial Hospital"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://example.org/www.foundingfathersmemorial.com"
        ).valueUri
    )
    assert inst.identifier[0].use == "secondary"
    assert inst.identifier[0].value == "service002"
    assert inst.location[0].display == "Founding Fathers Memorial Hospital"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.network[0].display == "Patriot Preferred Provider Network"
    assert inst.organization.display == "Founding Fathers Memorial Hospital"
    assert (
        inst.participatingOrganization.display
        == "Independence Rehabilitation Services, Inc."
    )
    assert (
        inst.period.end
        == ExternalValidatorModel(valueDateTime="2022-02-01").valueDateTime
    )
    assert (
        inst.period.start
        == ExternalValidatorModel(valueDateTime="2018-02-09").valueDateTime
    )
    assert inst.specialty[0].coding[0].code == "394602003"
    assert inst.specialty[0].coding[0].display == "Rehabilitation - specialty"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.specialty[0].text == "Rehabilitation"
    assert inst.text.status == "generated"


def test_organizationaffiliation_3(base_settings):
    """No. 3 tests collection for OrganizationAffiliation.
    Test File: orgrole-example-services.json
    """
    filename = base_settings["unittest_data_dir"] / "orgrole-example-services.json"
    inst = organizationaffiliation.OrganizationAffiliation.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "OrganizationAffiliation" == inst.get_resource_type()

    impl_organizationaffiliation_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OrganizationAffiliation" == data["resourceType"]

    inst2 = organizationaffiliation.OrganizationAffiliation(**data)
    impl_organizationaffiliation_3(inst2)
