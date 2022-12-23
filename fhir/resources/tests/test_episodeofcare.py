# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EpisodeOfCare
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import episodeofcare


def impl_episodeofcare_1(inst):
    assert inst.account[0].display == "example account"
    assert inst.account[0].reference == "Account/example"
    assert inst.careManager.display == "Amanda Assigned"
    assert inst.careManager.reference == "Practitioner/14"
    assert inst.diagnosis[0].condition.reference == "Condition/stroke"
    assert inst.diagnosis[0].rank == 1
    assert inst.diagnosis[0].role.coding[0].code == "CC"
    assert inst.diagnosis[0].role.coding[0].display == "Chief complaint"
    assert (
        inst.diagnosis[0].role.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/diagnosis-role"
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system == "http://example.org/sampleepisodeofcare-identifier"
    )
    assert inst.identifier[0].value == "123"
    assert inst.managingOrganization.reference == "Organization/hl7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.period.start == fhirtypes.DateTime.validate("2014-09-01")
    assert inst.referralRequest[0].display == "Referral from Example Aged Care Services"
    assert inst.status == "active"
    assert inst.statusHistory[0].period.end == fhirtypes.DateTime.validate("2014-09-14")
    assert inst.statusHistory[0].period.start == fhirtypes.DateTime.validate(
        "2014-09-01"
    )
    assert inst.statusHistory[0].status == "planned"
    assert inst.statusHistory[1].period.end == fhirtypes.DateTime.validate("2014-09-21")
    assert inst.statusHistory[1].period.start == fhirtypes.DateTime.validate(
        "2014-09-15"
    )
    assert inst.statusHistory[1].status == "active"
    assert inst.statusHistory[2].period.end == fhirtypes.DateTime.validate("2014-09-24")
    assert inst.statusHistory[2].period.start == fhirtypes.DateTime.validate(
        "2014-09-22"
    )
    assert inst.statusHistory[2].status == "onhold"
    assert inst.statusHistory[3].period.start == fhirtypes.DateTime.validate(
        "2014-09-25"
    )
    assert inst.statusHistory[3].status == "active"
    assert inst.team[0].display == "example care team"
    assert inst.team[0].reference == "CareTeam/example"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "hacc"
    assert inst.type[0].coding[0].display == "Home and Community Care"
    assert (
        inst.type[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/episodeofcare-type"
    )


def test_episodeofcare_1(base_settings):
    """No. 1 tests collection for EpisodeOfCare.
    Test File: episodeofcare-example.json
    """
    filename = base_settings["unittest_data_dir"] / "episodeofcare-example.json"
    inst = episodeofcare.EpisodeOfCare.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EpisodeOfCare" == inst.resource_type

    impl_episodeofcare_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EpisodeOfCare" == data["resourceType"]

    inst2 = episodeofcare.EpisodeOfCare(**data)
    impl_episodeofcare_1(inst2)
