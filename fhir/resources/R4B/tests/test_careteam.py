# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CareTeam
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import careteam
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_careteam_1(inst):
    assert inst.category[0].coding[0].code == "LA27976-2"
    assert inst.category[0].coding[0].display == "Encounter-focused care team"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.contained[0].id == "pr1"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example"
    assert inst.identifier[0].value == "12345"
    assert inst.managingOrganization[0].reference == "Organization/f001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Peter James Charlmers Care Plan for Inpatient Encounter"
    assert inst.participant[0].member.display == "Peter James Chalmers"
    assert inst.participant[0].member.reference == "Patient/example"
    assert inst.participant[0].role[0].text == "responsiblePerson"
    assert inst.participant[1].member.display == "Dorothy Dietition"
    assert inst.participant[1].member.reference == "#pr1"
    assert inst.participant[1].onBehalfOf.reference == "Organization/f001"
    assert (
        inst.participant[1].period.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-01-01"}
        ).valueDateTime
    )
    assert inst.participant[1].role[0].text == "adviser"
    assert (
        inst.period.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-01-01"}
        ).valueDateTime
    )
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
    inst = careteam.CareTeam.model_validate_json(filename.read_bytes())
    assert "CareTeam" == inst.get_resource_type()

    impl_careteam_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CareTeam" == data["resourceType"]

    inst2 = careteam.CareTeam(**data)
    impl_careteam_1(inst2)
