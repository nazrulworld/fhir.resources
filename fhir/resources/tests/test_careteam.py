# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CareTeam
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import careteam


def impl_careteam_1(inst):
    assert inst.category[0].coding[0].code == "LA27976-2"
    assert inst.category[0].coding[0].display == "Encounter-focused care team"
    assert inst.category[0].coding[0].system == "http://loinc.org"
    assert inst.contained[0].id == "pr1"
    assert inst.id == "example"
    assert inst.identifier[0].value == "12345"
    assert inst.managingOrganization[0].reference == "Organization/f001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "Peter James Charlmers Care Team for Inpatient Encounter"
    assert inst.participant[0].member.display == "Peter James Chalmers"
    assert inst.participant[0].member.reference == "Patient/example"
    assert inst.participant[0].role.text == "responsiblePerson"
    assert inst.participant[
        1
    ].coverageTiming.repeat.boundsPeriod.end == fhirtypes.DateTime.validate(
        "2013-01-01"
    )
    assert inst.participant[
        1
    ].coverageTiming.repeat.boundsPeriod.start == fhirtypes.DateTime.validate(
        "2010-12-23"
    )
    assert inst.participant[1].coverageTiming.repeat.dayOfWeek[0] == "mon"
    assert inst.participant[1].coverageTiming.repeat.frequency == 1
    assert float(inst.participant[1].coverageTiming.repeat.period) == float(1)
    assert inst.participant[1].coverageTiming.repeat.periodUnit == "d"
    assert inst.participant[1].coverageTiming.repeat.when[0] == "MORN"
    assert inst.participant[1].member.display == "Dorothy Dietition"
    assert inst.participant[1].member.reference == "#pr1"
    assert inst.participant[1].onBehalfOf.reference == "Organization/f001"
    assert inst.participant[1].role.text == "adviser"
    assert inst.period.end == fhirtypes.DateTime.validate("2013-01-01")
    assert inst.status == "active"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == '<div xmlns="http://www.w3.org/1999/xhtml">Care Team</div>'
    assert inst.text.status == "generated"


def test_careteam_1(base_settings):
    """No. 1 tests collection for CareTeam.
    Test File: careteam-example.json
    """
    filename = base_settings["unittest_data_dir"] / "careteam-example.json"
    inst = careteam.CareTeam.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CareTeam" == inst.resource_type

    impl_careteam_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CareTeam" == data["resourceType"]

    inst2 = careteam.CareTeam(**data)
    impl_careteam_1(inst2)
