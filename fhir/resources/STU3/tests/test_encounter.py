# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Encounter
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import encounter


def impl_encounter_1(inst):
    assert inst.class_fhir.code == "HH"
    assert inst.class_fhir.display == "home health"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.contained[0].id == "home"
    assert inst.id == "home"
    assert inst.location[0].location.display == "Client's home"
    assert inst.location[0].location.reference == "#home"
    assert inst.location[0].period.end == fhirtypes.DateTime.validate(
        "2015-01-17T16:30:00+10:00"
    )
    assert inst.location[0].period.start == fhirtypes.DateTime.validate(
        "2015-01-17T16:00:00+10:00"
    )
    assert inst.location[0].status == "completed"
    assert inst.participant[0].individual.display == "Dr Adam Careful"
    assert inst.participant[0].individual.reference == "Practitioner/example"
    assert inst.participant[0].period.end == fhirtypes.DateTime.validate(
        "2015-01-17T16:30:00+10:00"
    )
    assert inst.participant[0].period.start == fhirtypes.DateTime.validate(
        "2015-01-17T16:00:00+10:00"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2015-01-17T16:30:00+10:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2015-01-17T16:00:00+10:00")
    assert inst.status == "finished"
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
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_1(inst2)


def impl_encounter_2(inst):
    assert inst.class_fhir.code == "AMB"
    assert inst.class_fhir.display == "ambulatory"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.id == "f201"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130404"
    assert inst.participant[0].individual.reference == "Practitioner/f201"
    assert inst.priority.coding[0].code == "17621005"
    assert inst.priority.coding[0].display == "Normal"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].text == (
        "The patient had fever peaks over the last couple of days. He"
        " is worried about these peaks."
    )
    assert inst.serviceProvider.reference == "Organization/f201"
    assert inst.status == "finished"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "11429006"
    assert inst.type[0].coding[0].display == "Consultation"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_2(base_settings):
    """No. 2 tests collection for Encounter.
    Test File: encounter-example-f201-20130404.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f201-20130404.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_2(inst2)


def impl_encounter_3(inst):
    assert inst.class_fhir.code == "AMB"
    assert inst.class_fhir.display == "ambulatory"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.hospitalization.admitSource.coding[0].code == "305956004"
    assert inst.hospitalization.admitSource.coding[0].display == "Referral by physician"
    assert inst.hospitalization.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.hospitalization.dischargeDisposition.coding[0].code == "306689006"
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].display
        == "Discharge to home"
    )
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.hospitalization.preAdmissionIdentifier.system
        == "http://www.bmc.nl/zorgportal/identifiers/pre-admissions"
    )
    assert inst.hospitalization.preAdmissionIdentifier.use == "official"
    assert inst.hospitalization.preAdmissionIdentifier.value == "93042"
    assert inst.id == "f003"
    assert (
        inst.identifier[0].system
        == "http://www.bmc.nl/zorgportal/identifiers/encounters"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v6751"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "min"
    assert float(inst.length.value) == float(90)
    assert inst.participant[0].individual.display == "E.M. van den Broek"
    assert inst.participant[0].individual.reference == "Practitioner/f001"
    assert inst.priority.coding[0].code == "103391001"
    assert (
        inst.priority.coding[0].display == "Non-urgent ear, nose and throat admission"
    )
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].coding[0].code == "18099001"
    assert inst.reason[0].coding[0].display == "Retropharyngeal abscess"
    assert inst.reason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/encounter-" "primaryDiagnosis"
    )
    assert inst.reason[0].extension[0].valuePositiveInt == 1
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "finished"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_3(base_settings):
    """No. 3 tests collection for Encounter.
    Test File: encounter-example-f003-abscess.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f003-abscess.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_3(inst2)


def impl_encounter_4(inst):
    assert inst.class_fhir.code == "IMP"
    assert inst.class_fhir.display == "inpatient encounter"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.id == "example"
    assert inst.status == "in-progress"
    assert inst.subject.reference == "Patient/example"
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
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_4(inst2)


def impl_encounter_5(inst):
    assert inst.class_fhir.code == "AMB"
    assert inst.class_fhir.display == "ambulatory"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.hospitalization.admitSource.coding[0].code == "305997006"
    assert (
        inst.hospitalization.admitSource.coding[0].display == "Referral by radiologist"
    )
    assert inst.hospitalization.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.hospitalization.dischargeDisposition.coding[0].code == "306689006"
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].display
        == "Discharge to home"
    )
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.hospitalization.preAdmissionIdentifier.system
        == "http://www.bmc.nl/zorgportal/identifiers/pre-admissions"
    )
    assert inst.hospitalization.preAdmissionIdentifier.use == "official"
    assert inst.hospitalization.preAdmissionIdentifier.value == "98682"
    assert inst.id == "f002"
    assert (
        inst.identifier[0].system
        == "http://www.bmc.nl/zorgportal/identifiers/encounters"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v3251"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "min"
    assert float(inst.length.value) == float(140)
    assert inst.participant[0].individual.display == "M.I.M Versteegh"
    assert inst.participant[0].individual.reference == "Practitioner/f003"
    assert inst.priority.coding[0].code == "103391001"
    assert inst.priority.coding[0].display == "Urgent"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].coding[0].code == "34068001"
    assert inst.reason[0].coding[0].display == "Partial lobectomy of lung"
    assert inst.reason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.serviceProvider.display == "BMC"
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "finished"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_5(base_settings):
    """No. 5 tests collection for Encounter.
    Test File: encounter-example-f002-lung.json
    """
    filename = base_settings["unittest_data_dir"] / "encounter-example-f002-lung.json"
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_5(inst2)


def impl_encounter_6(inst):
    assert inst.account[0].reference == "Account/example"
    assert inst.appointment.reference == "Appointment/example"
    assert inst.class_fhir.code == "IMP"
    assert inst.class_fhir.display == "inpatient encounter"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.diagnosis[0].condition.reference == "Condition/stroke"
    assert inst.diagnosis[0].rank == 1
    assert inst.diagnosis[0].role.coding[0].code == "AD"
    assert inst.diagnosis[0].role.coding[0].display == "Admission diagnosis"
    assert (
        inst.diagnosis[0].role.coding[0].system == "http://hl7.org/fhir/diagnosis-role"
    )
    assert inst.diagnosis[1].condition.reference == "Condition/f201"
    assert inst.diagnosis[1].role.coding[0].code == "DD"
    assert inst.diagnosis[1].role.coding[0].display == "Discharge diagnosis"
    assert (
        inst.diagnosis[1].role.coding[0].system == "http://hl7.org/fhir/diagnosis-role"
    )
    assert inst.episodeOfCare[0].reference == "EpisodeOfCare/example"
    assert inst.hospitalization.admitSource.coding[0].code == "309902002"
    assert (
        inst.hospitalization.admitSource.coding[0].display
        == "Clinical Oncology Department"
    )
    assert inst.hospitalization.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.hospitalization.destination.reference == "Location/2"
    assert inst.hospitalization.dietPreference[0].coding[0].code == "276026009"
    assert (
        inst.hospitalization.dietPreference[0].coding[0].display
        == "Fluid balance regulation"
    )
    assert (
        inst.hospitalization.dietPreference[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.hospitalization.origin.reference == "Location/2"
    assert inst.hospitalization.reAdmission.coding[0].display == "readmitted"
    assert inst.hospitalization.specialArrangement[0].coding[0].code == "wheel"
    assert inst.hospitalization.specialArrangement[0].coding[0].display == "Wheelchair"
    assert (
        inst.hospitalization.specialArrangement[0].coding[0].system
        == "http://hl7.org/fhir/encounter-special-arrangements"
    )
    assert inst.hospitalization.specialCourtesy[0].coding[0].code == "NRM"
    assert (
        inst.hospitalization.specialCourtesy[0].coding[0].display == "normal courtesy"
    )
    assert (
        inst.hospitalization.specialCourtesy[0].coding[0].system
        == "http://hl7.org/fhir/v3/EncounterSpecialCourtesy"
    )
    assert inst.id == "f203"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130311"
    assert inst.incomingReferral[0].reference == "ReferralRequest/example"
    assert inst.partOf.reference == "Encounter/f203"
    assert inst.participant[0].individual.reference == "Practitioner/f201"
    assert inst.participant[0].type[0].coding[0].code == "PART"
    assert (
        inst.participant[0].type[0].coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2013-03-20")
    assert inst.period.start == fhirtypes.DateTime.validate("2013-03-11")
    assert inst.priority.coding[0].code == "394849002"
    assert inst.priority.coding[0].display == "High priority"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].text == (
        "The patient seems to suffer from bilateral pneumonia and "
        "renal insufficiency, most likely due to chemotherapy."
    )
    assert inst.serviceProvider.reference == "Organization/2"
    assert inst.status == "finished"
    assert inst.statusHistory[0].period.start == fhirtypes.DateTime.validate(
        "2013-03-08"
    )
    assert inst.statusHistory[0].status == "arrived"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "183807002"
    assert inst.type[0].coding[0].display == "Inpatient stay for nine days"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_6(base_settings):
    """No. 6 tests collection for Encounter.
    Test File: encounter-example-f203-20130311.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f203-20130311.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_6(inst2)


def impl_encounter_7(inst):
    assert inst.class_fhir.code == "AMB"
    assert inst.class_fhir.display == "ambulatory"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.id == "xcda"
    assert (
        inst.identifier[0].system
        == "http://healthcare.example.org/identifiers/enocunter"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "1234213.52345873"
    assert inst.participant[0].individual.reference == "Practitioner/xcda1"
    assert inst.reason[0].coding[0].code == "T-D8200"
    assert inst.reason[0].coding[0].display == "Arm"
    assert (
        inst.reason[0].coding[0].system == "http://ihe.net/xds/connectathon/eventCodes"
    )
    assert inst.status == "finished"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.status == "generated"


def test_encounter_7(base_settings):
    """No. 7 tests collection for Encounter.
    Test File: encounter-example-xcda.json
    """
    filename = base_settings["unittest_data_dir"] / "encounter-example-xcda.json"
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_7(inst2)


def impl_encounter_8(inst):
    assert inst.class_fhir.code == "AMB"
    assert inst.class_fhir.display == "ambulatory"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.diagnosis[0].condition.display == (
        "Complications from Roel's TPF chemotherapy on January 28th, " "2013"
    )
    assert inst.diagnosis[0].rank == 1
    assert inst.diagnosis[0].role.coding[0].code == "AD"
    assert inst.diagnosis[0].role.coding[0].display == "Admission diagnosis"
    assert (
        inst.diagnosis[0].role.coding[0].system == "http://hl7.org/fhir/diagnosis-role"
    )
    assert inst.id == "f202"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130128"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "minutes"
    assert float(inst.length.value) == float(56)
    assert inst.participant[0].individual.reference == "Practitioner/f201"
    assert inst.priority.coding[0].code == "103391001"
    assert inst.priority.coding[0].display == "Urgent"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/encounter-" "primaryDiagnosis"
    )
    assert inst.reason[0].extension[0].valuePositiveInt == 2
    assert inst.reason[0].text == "The patient is treated for a tumor."
    assert inst.serviceProvider.reference == "Organization/f201"
    assert inst.status == "finished"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "367336001"
    assert inst.type[0].coding[0].display == "Chemotherapy"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_8(base_settings):
    """No. 8 tests collection for Encounter.
    Test File: encounter-example-f202-20130128.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-f202-20130128.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_8(inst2)


def impl_encounter_9(inst):
    assert inst.classHistory[0].class_fhir.code == "EMER"
    assert inst.classHistory[0].class_fhir.display == "emergency"
    assert inst.classHistory[0].class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.classHistory[0].period.end == fhirtypes.DateTime.validate(
        "2017-02-01T09:27:00+10:00"
    )
    assert inst.classHistory[0].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T07:15:00+10:00"
    )
    assert inst.classHistory[1].class_fhir.code == "IMP"
    assert inst.classHistory[1].class_fhir.display == "inpatient encounter"
    assert inst.classHistory[1].class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.classHistory[1].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T09:27:00+10:00"
    )
    assert inst.class_fhir.code == "IMP"
    assert inst.class_fhir.display == "inpatient encounter"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.hospitalization.admitSource.coding[0].code == "emd"
    assert (
        inst.hospitalization.admitSource.coding[0].display
        == "From accident/emergency department"
    )
    assert (
        inst.hospitalization.admitSource.coding[0].system
        == "http://hl7.org/fhir/admit-source"
    )
    assert inst.id == "emerg"
    assert inst.location[0].location.display == "Emergency Waiting Room"
    assert inst.location[0].period.end == fhirtypes.DateTime.validate(
        "2017-02-01T08:45:00+10:00"
    )
    assert inst.location[0].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T07:15:00+10:00"
    )
    assert inst.location[0].status == "active"
    assert inst.location[1].location.display == "Emergency"
    assert inst.location[1].period.end == fhirtypes.DateTime.validate(
        "2017-02-01T09:27:00+10:00"
    )
    assert inst.location[1].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T08:45:00+10:00"
    )
    assert inst.location[1].status == "active"
    assert inst.location[2].location.display == "Ward 1, Room 42, Bed 1"
    assert inst.location[2].period.end == fhirtypes.DateTime.validate(
        "2017-02-01T12:15:00+10:00"
    )
    assert inst.location[2].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T09:27:00+10:00"
    )
    assert inst.location[2].status == "active"
    assert inst.location[3].location.display == "Ward 1, Room 42, Bed 1"
    assert inst.location[3].period.end == fhirtypes.DateTime.validate(
        "2017-02-01T12:45:00+10:00"
    )
    assert inst.location[3].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T12:15:00+10:00"
    )
    assert inst.location[3].status == "reserved"
    assert inst.location[4].location.display == "Ward 1, Room 42, Bed 1"
    assert inst.location[4].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T12:45:00+10:00"
    )
    assert inst.location[4].status == "active"
    assert inst.period.start == fhirtypes.DateTime.validate("2017-02-01T07:15:00+10:00")
    assert inst.status == "in-progress"
    assert inst.statusHistory[0].period.end == fhirtypes.DateTime.validate(
        "2017-02-01T07:35:00+10:00"
    )
    assert inst.statusHistory[0].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T07:15:00+10:00"
    )
    assert inst.statusHistory[0].status == "arrived"
    assert inst.statusHistory[1].period.end == fhirtypes.DateTime.validate(
        "2017-02-01T08:45:00+10:00"
    )
    assert inst.statusHistory[1].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T07:35:00+10:00"
    )
    assert inst.statusHistory[1].status == "triaged"
    assert inst.statusHistory[2].period.end == fhirtypes.DateTime.validate(
        "2017-02-01T12:15:00+10:00"
    )
    assert inst.statusHistory[2].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T08:45:00+10:00"
    )
    assert inst.statusHistory[2].status == "in-progress"
    assert inst.statusHistory[3].period.end == fhirtypes.DateTime.validate(
        "2017-02-01T12:45:00+10:00"
    )
    assert inst.statusHistory[3].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T12:15:00+10:00"
    )
    assert inst.statusHistory[3].status == "onleave"
    assert inst.statusHistory[4].period.start == fhirtypes.DateTime.validate(
        "2017-02-01T12:45:00+10:00"
    )
    assert inst.statusHistory[4].status == "in-progress"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Emergency visit '
        "that escalated into inpatient patient @example</div>"
    )
    assert inst.text.status == "generated"


def test_encounter_9(base_settings):
    """No. 9 tests collection for Encounter.
    Test File: encounter-example-emerg.json
    """
    filename = base_settings["unittest_data_dir"] / "encounter-example-emerg.json"
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_9(inst2)


def impl_encounter_10(inst):
    assert inst.class_fhir.code == "AMB"
    assert inst.class_fhir.display == "ambulatory"
    assert inst.class_fhir.system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.hospitalization.admitSource.coding[0].code == "305956004"
    assert inst.hospitalization.admitSource.coding[0].display == "Referral by physician"
    assert inst.hospitalization.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.hospitalization.dischargeDisposition.coding[0].code == "306689006"
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].display
        == "Discharge to home"
    )
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.hospitalization.preAdmissionIdentifier.system
        == "http://www.amc.nl/zorgportal/identifiers/pre-admissions"
    )
    assert inst.hospitalization.preAdmissionIdentifier.use == "official"
    assert inst.hospitalization.preAdmissionIdentifier.value == "93042"
    assert inst.id == "f001"
    assert (
        inst.identifier[0].system == "http://www.amc.nl/zorgportal/identifiers/visits"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v1451"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "min"
    assert float(inst.length.value) == float(140)
    assert inst.participant[0].individual.display == "P. Voigt"
    assert inst.participant[0].individual.reference == "Practitioner/f002"
    assert inst.priority.coding[0].code == "310361003"
    assert inst.priority.coding[0].display == "Non-urgent cardiological admission"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].coding[0].code == "34068001"
    assert inst.reason[0].coding[0].display == "Heart valve replacement"
    assert inst.reason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.serviceProvider.display == "Burgers University Medical Center"
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "finished"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_encounter_10(base_settings):
    """No. 10 tests collection for Encounter.
    Test File: encounter-example-f001-heart.json
    """
    filename = base_settings["unittest_data_dir"] / "encounter-example-f001-heart.json"
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type

    impl_encounter_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_encounter_10(inst2)
