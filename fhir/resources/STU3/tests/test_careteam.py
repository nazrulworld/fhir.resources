# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CareTeam
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import careteam


def impl_careteam_1(inst):
    assert inst.category[0].coding[0].code == "encounter"
    assert inst.category[0].coding[0].system == "http://hl7.org/fhir/care-team-category"
    assert inst.contained[0].id == "pr1"
    assert inst.context.reference == "Encounter/example"
    assert inst.id == "example"
    assert inst.identifier[0].value == "12345"
    assert inst.managingOrganization[0].reference == "Organization/f001"
    assert inst.name == "Peter James Charlmers Care Plan for Inpatient Encounter"
    assert inst.participant[0].member.display == "Peter James Chalmers"
    assert inst.participant[0].member.reference == "Patient/example"
    assert inst.participant[0].role.text == "responsiblePerson"
    assert inst.participant[1].member.display == "Dorothy Dietition"
    assert inst.participant[1].member.reference == "#pr1"
    assert inst.participant[1].onBehalfOf.reference == "Organization/f001"
    assert inst.participant[1].period.end == fhirtypes.DateTime.validate("2013-01-01")
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
