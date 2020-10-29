# -*- coding: utf-8 -*-
from datetime import date

from pydantic.datetime_parse import parse_date

from .. import fhirtypes  # noqa: F401
from .. import episodeofcare


def test_EpisodeOfCare_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "episodeofcare-example.canonical.json"
    )
    inst = episodeofcare.EpisodeOfCare.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EpisodeOfCare" == inst.resource_type
    impl_EpisodeOfCare_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EpisodeOfCare" == data["resourceType"]

    inst2 = episodeofcare.EpisodeOfCare(**data)
    impl_EpisodeOfCare_1(inst2)


def impl_EpisodeOfCare_1(inst):
    assert inst.careManager.display == "Amanda Assigned"
    assert inst.careManager.reference == "Practitioner/14"
    assert inst.careTeam[0].member.display == "Henry Seven"
    assert inst.careTeam[0].member.reference == "Practitioner/13"
    assert inst.careTeam[0].period.end == parse_date("2014-09-16")
    assert inst.careTeam[0].period.start == parse_date("2014-09-01")
    assert inst.careTeam[0].role[0].coding[0].code == "AO"
    assert inst.careTeam[0].role[0].coding[0].display == "Assessment Worker"
    assert (
        inst.careTeam[0].role[0].coding[0].system
        == "http://example.org/EpisodeOfCare/Role"
    )
    assert inst.condition[0].display == "Severe burn of left ear"
    assert inst.condition[0].reference == "Condition/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system == "http://example.org/sampleepisodeofcare-identifier"
    )
    assert inst.identifier[0].value == "123"
    assert inst.managingOrganization.reference == "Organization/hl7"
    assert inst.patient.reference == "Patient/example"
    assert inst.period.start == parse_date("2014-09-01")
    assert inst.referralRequest[0].display == "Referral from Example Aged Care Services"
    assert inst.status == "active"
    assert inst.statusHistory[0].period.end == parse_date("2014-09-14")
    assert inst.statusHistory[0].period.start == parse_date("2014-09-01")
    assert inst.statusHistory[0].status == "planned"
    assert inst.statusHistory[1].period.end == parse_date("2014-09-21")
    assert inst.statusHistory[1].period.start == parse_date("2014-09-15")
    assert inst.statusHistory[1].status == "active"
    assert inst.statusHistory[2].period.end == parse_date("2014-09-24")
    assert inst.statusHistory[2].period.start == parse_date("2014-09-22")
    assert inst.statusHistory[2].status == "onhold"
    assert inst.statusHistory[3].period.start == parse_date("2014-09-25")
    assert inst.statusHistory[3].status == "active"
    assert (
        inst.text.div
        == """<div>
      HACC Program for Peter James Chalmers at HL7 Healthcare 15 Sept 2014 - current<br/>
			was on leave from 22 Sept - 24 Sept while in respite care
    </div>"""
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "HACC"
    assert inst.type[0].coding[0].display == "Home and Community Care Package"
    assert inst.type[0].coding[0].system == "http://example.org/EpisodeOfCare/Type"
