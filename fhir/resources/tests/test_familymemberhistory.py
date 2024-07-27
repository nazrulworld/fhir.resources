# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import familymemberhistory
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_familymemberhistory_1(inst):
    assert inst.condition[0].code.coding[0].code == "315619001"
    assert inst.condition[0].code.coding[0].display == "Myocardial Infarction"
    assert (
        inst.condition[0].code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.condition[0].code.text == "Heart Attack"
    assert inst.condition[0].contributedToDeath is True
    assert inst.condition[0].note[0].text == (
        "Was fishing at the time. At least he went doing someting he " "loved."
    )
    assert inst.condition[0].onsetAge.code == "a"
    assert (
        inst.condition[0].onsetAge.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.condition[0].onsetAge.unit == "yr"
    assert float(inst.condition[0].onsetAge.value) == float(74)
    assert inst.date == ExternalValidatorModel(valueDateTime="2011-03-18").valueDateTime
    assert inst.id == "father"
    assert inst.identifier[0].value == "12345"
    assert (
        inst.instantiatesUri[0]
        == ExternalValidatorModel(
            valueUri="http://example.org/family-member-history-questionnaire"
        ).valueUri
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.participant[0].actor.reference == "Practitioner/f201"
    assert inst.participant[0].function.coding[0].code == "verifier"
    assert inst.participant[0].function.coding[0].display == "Verifier"
    assert (
        inst.participant[0].function.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/provenance-participant-type"
        ).valueUri
    )
    assert inst.patient.display == "Peter Patient"
    assert inst.patient.reference == "Patient/example"
    assert inst.relationship.coding[0].code == "FTH"
    assert inst.relationship.coding[0].display == "father"
    assert (
        inst.relationship.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-RoleCode"
        ).valueUri
    )
    assert inst.sex.coding[0].code == "male"
    assert inst.sex.coding[0].display == "Male"
    assert (
        inst.sex.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/administrative-gender"
        ).valueUri
    )
    assert inst.status == "completed"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Father died of a'
        " heart attack aged 74</div>"
    )
    assert inst.text.status == "generated"


def test_familymemberhistory_1(base_settings):
    """No. 1 tests collection for FamilyMemberHistory.
    Test File: familymemberhistory-example.json
    """
    filename = base_settings["unittest_data_dir"] / "familymemberhistory-example.json"
    inst = familymemberhistory.FamilyMemberHistory.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "FamilyMemberHistory" == inst.get_resource_type()

    impl_familymemberhistory_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "FamilyMemberHistory" == data["resourceType"]

    inst2 = familymemberhistory.FamilyMemberHistory(**data)
    impl_familymemberhistory_1(inst2)


def impl_familymemberhistory_2(inst):
    assert inst.condition[0].code.coding[0].code == "700146008"
    assert (
        inst.condition[0].code.coding[0].display
        == "No history of malignant neoplasm of breast"
    )
    assert (
        inst.condition[0].code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.condition[0].code.text == "No history of malignant tumor of breast"
    assert inst.id == "negation"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.patient.display == "Peter Patient"
    assert inst.patient.reference == "Patient/100"
    assert inst.relationship.coding[0].code == "MTH"
    assert inst.relationship.coding[0].display == "mother"
    assert (
        inst.relationship.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-RoleCode"
        ).valueUri
    )
    assert inst.status == "completed"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Mother has no '
        "history of malignant tumor of breast</div>"
    )
    assert inst.text.status == "generated"


def test_familymemberhistory_2(base_settings):
    """No. 2 tests collection for FamilyMemberHistory.
    Test File: familymemberhistory-example-negation.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "familymemberhistory-example-negation.json"
    )
    inst = familymemberhistory.FamilyMemberHistory.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "FamilyMemberHistory" == inst.get_resource_type()

    impl_familymemberhistory_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "FamilyMemberHistory" == data["resourceType"]

    inst2 = familymemberhistory.FamilyMemberHistory(**data)
    impl_familymemberhistory_2(inst2)


def impl_familymemberhistory_3(inst):
    assert inst.condition[0].code.coding[0].code == "371041009"
    assert inst.condition[0].code.coding[0].display == "Embolic Stroke"
    assert (
        inst.condition[0].code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.condition[0].code.text == "Stroke"
    assert inst.condition[0].onsetAge.code == "a"
    assert (
        inst.condition[0].onsetAge.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.condition[0].onsetAge.unit == "yr"
    assert float(inst.condition[0].onsetAge.value) == float(56)
    assert inst.id == "mother"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.patient.display == "Peter Patient"
    assert inst.patient.reference == "Patient/100"
    assert inst.relationship.coding[0].code == "MTH"
    assert inst.relationship.coding[0].display == "mother"
    assert (
        inst.relationship.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-RoleCode"
        ).valueUri
    )
    assert inst.status == "completed"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Mother died of a'
        " stroke aged 56</div>"
    )
    assert inst.text.status == "generated"


def test_familymemberhistory_3(base_settings):
    """No. 3 tests collection for FamilyMemberHistory.
    Test File: familymemberhistory-example-mother.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "familymemberhistory-example-mother.json"
    )
    inst = familymemberhistory.FamilyMemberHistory.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "FamilyMemberHistory" == inst.get_resource_type()

    impl_familymemberhistory_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "FamilyMemberHistory" == data["resourceType"]

    inst2 = familymemberhistory.FamilyMemberHistory(**data)
    impl_familymemberhistory_3(inst2)
