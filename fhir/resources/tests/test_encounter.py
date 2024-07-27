# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Encounter
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import encounter
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_encounter_1(inst):
    assert (
        inst.actualPeriod.end
        == ExternalValidatorModel(
            valueDateTime="2015-01-17T16:30:00+10:00"
        ).valueDateTime
    )
    assert (
        inst.actualPeriod.start
        == ExternalValidatorModel(
            valueDateTime="2015-01-17T16:00:00+10:00"
        ).valueDateTime
    )
    assert inst.class_fhir[0].coding[0].code == "HH"
    assert inst.class_fhir[0].coding[0].display == "home health"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.contained[0].id == "home"
    assert inst.id == "home"
    assert inst.location[0].location.display == "Client's home"
    assert inst.location[0].location.reference == "#home"
    assert (
        inst.location[0].period.end
        == ExternalValidatorModel(
            valueDateTime="2015-01-17T16:30:00+10:00"
        ).valueDateTime
    )
    assert (
        inst.location[0].period.start
        == ExternalValidatorModel(
            valueDateTime="2015-01-17T16:00:00+10:00"
        ).valueDateTime
    )
    assert inst.location[0].status == "completed"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.participant[0].actor.display == "Dr Adam Careful"
    assert inst.participant[0].actor.reference == "Practitioner/example"
    assert (
        inst.participant[0].period.end
        == ExternalValidatorModel(
            valueDateTime="2015-01-17T16:30:00+10:00"
        ).valueDateTime
    )
    assert (
        inst.participant[0].period.start
        == ExternalValidatorModel(
            valueDateTime="2015-01-17T16:00:00+10:00"
        ).valueDateTime
    )
    assert inst.participant[0].type[0].coding[0].code == "PPRF"
    assert (
        inst.participant[0].type[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
        ).valueUri
    )
    assert inst.participant[1].actor.reference == "Patient/example"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Encounter with '
        "patient @example who is at home</div>"
    )
    assert inst.text.status == "generated"


def test_encounter_1(base_settings):
    """No. 1 tests collection for Encounter.
    Test File: encounter-example-home.json
    """
    filename = base_settings["unittest_data_dir"] / "encounter-example-home.json"
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_1(inst2)


def impl_encounter_2(inst):
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.id == "f201"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130404"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.participant[0].actor.reference == "Practitioner/f201"
    assert inst.priority.coding[0].code == "17621005"
    assert inst.priority.coding[0].display == "Normal"
    assert (
        inst.priority.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.reason[0].value[0].concept.text == (
        "The patient had fever peaks over the last couple of days. He"
        " is worried about these peaks."
    )
    assert inst.serviceProvider.reference == "Organization/f201"
    assert inst.status == "completed"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "11429006"
    assert inst.type[0].coding[0].display == "Consultation"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_encounter_2(base_settings):
    """No. 2 tests collection for Encounter.
    Test File: encounter-example-f201-20130404.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f201-20130404.json"
    )
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_2(inst2)


def impl_encounter_3(inst):
    assert inst.admission.admitSource.coding[0].code == "305956004"
    assert inst.admission.admitSource.coding[0].display == "Referral by physician"
    assert (
        inst.admission.admitSource.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.admission.dischargeDisposition.coding[0].code == "306689006"
    assert inst.admission.dischargeDisposition.coding[0].display == "Discharge to home"
    assert (
        inst.admission.dischargeDisposition.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.admission.preAdmissionIdentifier.system
        == ExternalValidatorModel(
            valueUri="http://www.bmc.nl/zorgportal/identifiers/pre-admissions"
        ).valueUri
    )
    assert inst.admission.preAdmissionIdentifier.use == "official"
    assert inst.admission.preAdmissionIdentifier.value == "93042"
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.id == "f003"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.bmc.nl/zorgportal/identifiers/encounters"
        ).valueUri
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v6751"
    assert inst.length.code == "min"
    assert (
        inst.length.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.length.unit == "min"
    assert float(inst.length.value) == float(90)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.participant[0].actor.display == "E.M. van den Broek"
    assert inst.participant[0].actor.reference == "Practitioner/f001"
    assert inst.priority.coding[0].code == "103391001"
    assert (
        inst.priority.coding[0].display == "Non-urgent ear, nose and throat admission"
    )
    assert (
        inst.priority.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.reason[0].value[0].concept.coding[0].code == "18099001"
    assert (
        inst.reason[0].value[0].concept.coding[0].display == "Retropharyngeal abscess"
    )
    assert (
        inst.reason[0].value[0].concept.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_encounter_3(base_settings):
    """No. 3 tests collection for Encounter.
    Test File: encounter-example-f003-abscess.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f003-abscess.json"
    )
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_3(inst2)


def impl_encounter_4(inst):
    assert inst.careTeam[0].reference == "Encounter/example"
    assert inst.class_fhir[0].coding[0].code == "IMP"
    assert inst.class_fhir[0].coding[0].display == "inpatient encounter"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "in-progress"
    assert inst.subject.reference == "Patient/example"
    assert inst.subjectStatus.coding[0].code == "receiving-care"
    assert (
        inst.subjectStatus.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/encounter-subject-status"
        ).valueUri
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Encounter with '
        "patient @example</div>"
    )
    assert inst.text.status == "generated"


def test_encounter_4(base_settings):
    """No. 4 tests collection for Encounter.
    Test File: encounter-example.json
    """
    filename = base_settings["unittest_data_dir"] / "encounter-example.json"
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_4(inst2)


def impl_encounter_5(inst):
    assert inst.class_fhir[0].coding[0].code == "IMP"
    assert inst.class_fhir[0].coding[0].display == "inpatient encounter"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.id == "genomicEncounter"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "in-progress"
    assert inst.subject.reference == "Patient/genomicPatient"
    assert inst.text.status == "generated"


def test_encounter_5(base_settings):
    """No. 5 tests collection for Encounter.
    Test File: Encounter-genomicEncounter.json
    """
    filename = base_settings["unittest_data_dir"] / "Encounter-genomicEncounter.json"
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_5(inst2)


def impl_encounter_6(inst):
    assert (
        inst.actualPeriod.end
        == ExternalValidatorModel(valueDateTime="2013-03-20").valueDateTime
    )
    assert (
        inst.actualPeriod.start
        == ExternalValidatorModel(valueDateTime="2013-03-11").valueDateTime
    )
    assert inst.class_fhir[0].coding[0].code == "IMP"
    assert inst.class_fhir[0].coding[0].display == "inpatient encounter"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.id == "colonoscopy"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.participant[0].actor.display == "Dr Adam Careful"
    assert inst.participant[0].actor.reference == "Practitioner/example"
    assert inst.participant[0].type[0].coding[0].code == "PART"
    assert (
        inst.participant[0].type[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
        ).valueUri
    )
    assert inst.reason[0].value[0].concept.text == "Routine investigation"
    assert inst.serviceProvider.display == "Gastroenterology @ Acme Hospital"
    assert inst.serviceProvider.reference == "Organization/1"
    assert inst.status == "completed"
    assert inst.subject.display == "Henry Levin the 7th"
    assert inst.subject.reference == "Patient/glossy"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "73761001"
    assert inst.type[0].coding[0].display == "Colonoscopy (procedure)"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.type[0].text == "Colonoscopy"


def test_encounter_6(base_settings):
    """No. 6 tests collection for Encounter.
    Test File: encounter-example-colonoscopy.json
    """
    filename = base_settings["unittest_data_dir"] / "encounter-example-colonoscopy.json"
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_6(inst2)


def impl_encounter_7(inst):
    assert inst.admission.admitSource.coding[0].code == "305997006"
    assert inst.admission.admitSource.coding[0].display == "Referral by radiologist"
    assert (
        inst.admission.admitSource.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.admission.dischargeDisposition.coding[0].code == "306689006"
    assert inst.admission.dischargeDisposition.coding[0].display == "Discharge to home"
    assert (
        inst.admission.dischargeDisposition.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.admission.preAdmissionIdentifier.system
        == ExternalValidatorModel(
            valueUri="http://www.bmc.nl/zorgportal/identifiers/pre-admissions"
        ).valueUri
    )
    assert inst.admission.preAdmissionIdentifier.use == "official"
    assert inst.admission.preAdmissionIdentifier.value == "98682"
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.id == "f002"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.bmc.nl/zorgportal/identifiers/encounters"
        ).valueUri
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v3251"
    assert inst.length.code == "min"
    assert (
        inst.length.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.length.unit == "min"
    assert float(inst.length.value) == float(140)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.participant[0].actor.display == "M.I.M Versteegh"
    assert inst.participant[0].actor.reference == "Practitioner/f003"
    assert inst.priority.coding[0].code == "103391001"
    assert inst.priority.coding[0].display == "Urgent"
    assert (
        inst.priority.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.reason[0].value[0].concept.coding[0].code == "34068001"
    assert (
        inst.reason[0].value[0].concept.coding[0].display == "Partial lobectomy of lung"
    )
    assert (
        inst.reason[0].value[0].concept.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.serviceProvider.display == "BMC"
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_encounter_7(base_settings):
    """No. 7 tests collection for Encounter.
    Test File: encounter-example-f002-lung.json
    """
    filename = base_settings["unittest_data_dir"] / "encounter-example-f002-lung.json"
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_7(inst2)


def impl_encounter_8(inst):
    assert inst.account[0].reference == "Account/example"
    assert (
        inst.actualPeriod.end
        == ExternalValidatorModel(valueDateTime="2013-03-20").valueDateTime
    )
    assert (
        inst.actualPeriod.start
        == ExternalValidatorModel(valueDateTime="2013-03-11").valueDateTime
    )
    assert inst.admission.admitSource.coding[0].code == "309902002"
    assert (
        inst.admission.admitSource.coding[0].display == "Clinical Oncology Department"
    )
    assert (
        inst.admission.admitSource.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.admission.destination.reference == "Location/2"
    assert inst.admission.origin.reference == "Location/2"
    assert inst.admission.reAdmission.coding[0].display == "readmitted"
    assert inst.appointment[0].reference == "Appointment/example"
    assert inst.basedOn[0].reference == "ServiceRequest/myringotomy"
    assert inst.class_fhir[0].coding[0].code == "IMP"
    assert inst.class_fhir[0].coding[0].display == "inpatient encounter"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.diagnosis[0].condition[0].reference.reference == "Condition/stroke"
    assert inst.diagnosis[0].use[0].coding[0].code == "AD"
    assert inst.diagnosis[0].use[0].coding[0].display == "Admission diagnosis"
    assert (
        inst.diagnosis[0].use[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/diagnosis-role"
        ).valueUri
    )
    assert inst.diagnosis[1].condition[0].reference.reference == "Condition/f201"
    assert inst.diagnosis[1].use[0].coding[0].code == "DD"
    assert inst.diagnosis[1].use[0].coding[0].display == "Discharge diagnosis"
    assert (
        inst.diagnosis[1].use[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/diagnosis-role"
        ).valueUri
    )
    assert inst.dietPreference[0].coding[0].code == "276026009"
    assert inst.dietPreference[0].coding[0].display == "Fluid balance regulation"
    assert (
        inst.dietPreference[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.episodeOfCare[0].reference == "EpisodeOfCare/example"
    assert inst.id == "f203"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130311"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.partOf.reference == "Encounter/f203"
    assert inst.participant[0].actor.reference == "Practitioner/f201"
    assert inst.participant[0].type[0].coding[0].code == "PART"
    assert (
        inst.participant[0].type[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
        ).valueUri
    )
    assert inst.priority.coding[0].code == "394849002"
    assert inst.priority.coding[0].display == "High priority"
    assert (
        inst.priority.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.reason[0].value[0].concept.text == (
        "The patient seems to suffer from bilateral pneumonia and "
        "renal insufficiency, most likely due to chemotherapy."
    )
    assert inst.serviceProvider.reference == "Organization/2"
    assert inst.specialArrangement[0].coding[0].code == "wheel"
    assert inst.specialArrangement[0].coding[0].display == "Wheelchair"
    assert (
        inst.specialArrangement[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/encounter-special-arrangements"
        ).valueUri
    )
    assert inst.specialCourtesy[0].coding[0].code == "NRM"
    assert inst.specialCourtesy[0].coding[0].display == "normal courtesy"
    assert (
        inst.specialCourtesy[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-EncounterSpecialCourtesy"
        ).valueUri
    )
    assert inst.status == "completed"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "183807002"
    assert inst.type[0].coding[0].display == "Inpatient stay for nine days"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_encounter_8(base_settings):
    """No. 8 tests collection for Encounter.
    Test File: encounter-example-f203-20130311.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f203-20130311.json"
    )
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_8(inst2)


def impl_encounter_9(inst):
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.id == "xcda"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://healthcare.example.org/identifiers/enocunter"
        ).valueUri
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "1234213.52345873"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.participant[0].actor.reference == "Practitioner/xcda1"
    assert inst.reason[0].value[0].concept.coding[0].code == "T-D8200"
    assert inst.reason[0].value[0].concept.coding[0].display == "Arm"
    assert (
        inst.reason[0].value[0].concept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://ihe.net/xds/connectathon/eventCodes"
        ).valueUri
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.status == "generated"


def test_encounter_9(base_settings):
    """No. 9 tests collection for Encounter.
    Test File: encounter-example-xcda.json
    """
    filename = base_settings["unittest_data_dir"] / "encounter-example-xcda.json"
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_9(inst2)


def impl_encounter_10(inst):
    assert inst.class_fhir[0].coding[0].code == "AMB"
    assert inst.class_fhir[0].coding[0].display == "ambulatory"
    assert (
        inst.class_fhir[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.diagnosis[0].condition[0].concept.text == (
        "Complications from Roel's TPF chemotherapy on January 28th, " "2013"
    )
    assert inst.diagnosis[0].use[0].coding[0].code == "AD"
    assert inst.diagnosis[0].use[0].coding[0].display == "Admission diagnosis"
    assert (
        inst.diagnosis[0].use[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/diagnosis-role"
        ).valueUri
    )
    assert (
        inst.diagnosis[1].condition[0].concept.text
        == "The patient is treated for a tumor"
    )
    assert inst.diagnosis[1].use[0].coding[0].code == "CC"
    assert inst.diagnosis[1].use[0].coding[0].display == "Chief complaint"
    assert (
        inst.diagnosis[1].use[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/diagnosis-role"
        ).valueUri
    )
    assert inst.id == "f202"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130128"
    assert inst.length.code == "min"
    assert (
        inst.length.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.length.unit == "minutes"
    assert float(inst.length.value) == float(56)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.participant[0].actor.reference == "Practitioner/f201"
    assert inst.priority.coding[0].code == "103391001"
    assert inst.priority.coding[0].display == "Urgent"
    assert (
        inst.priority.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.reason[0].value[0].concept.text == "The patient is treated for a tumor."
    assert inst.serviceProvider.reference == "Organization/f201"
    assert inst.status == "completed"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "367336001"
    assert inst.type[0].coding[0].display == "Chemotherapy"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_encounter_10(base_settings):
    """No. 10 tests collection for Encounter.
    Test File: encounter-example-f202-20130128.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f202-20130128.json"
    )
    inst = encounter.Encounter.model_validate_json(Path(filename).read_bytes())
    assert "Encounter" == inst.get_resource_type()

    impl_encounter_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_10(inst2)
