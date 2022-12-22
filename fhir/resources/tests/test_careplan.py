# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CarePlan
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import careplan


def impl_careplan_1(inst):
    assert inst.activity[0].detail.code.coding[0].code == "359615001"
    assert inst.activity[0].detail.code.coding[0].display == "Partial lobectomy of lung"
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.doNotPerform is True
    assert inst.activity[0].detail.kind == "ServiceRequest"
    assert inst.activity[0].detail.performer[0].display == "M.I.M. Versteegh"
    assert inst.activity[0].detail.performer[0].reference == "Practitioner/f003"
    assert inst.activity[0].detail.scheduledString == "2011-07-07T09:30:10+01:00"
    assert inst.activity[0].detail.status == "completed"
    assert inst.addresses[0].display == "?????"
    assert inst.addresses[0].reference == "Condition/f201"
    assert inst.careTeam[0].reference == "#careteam"
    assert inst.contained[0].id == "careteam"
    assert inst.contained[1].id == "goal"
    assert inst.goal[0].reference == "#goal"
    assert inst.id == "f002"
    assert (
        inst.identifier[0].system
        == "http://www.bmc.nl/zorgportal/identifiers/careplans"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "CP2934"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2013-07-07")
    assert inst.period.start == fhirtypes.DateTime.validate("2011-07-06")
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_careplan_1(base_settings):
    """No. 1 tests collection for CarePlan.
    Test File: careplan-example-f002-lung.json
    """
    filename = base_settings["unittest_data_dir"] / "careplan-example-f002-lung.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_1(inst2)


def impl_careplan_2(inst):
    assert inst.activity[0].detail.code.coding[0].code == "367336001"
    assert inst.activity[0].detail.code.coding[0].display == "Chemotherapy"
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.doNotPerform is False
    assert inst.activity[0].detail.kind == "ServiceRequest"
    assert inst.activity[0].detail.productReference.reference == "#tpf"
    assert inst.activity[0].detail.status == "in-progress"
    assert inst.activity[0].outcomeReference[0].display == "Roel's Chemotherapy"
    assert inst.activity[0].outcomeReference[0].reference == "Procedure/f201"
    assert inst.addresses[0].display == "Roel's head-neck tumor"
    assert inst.addresses[0].reference == "Condition/f202"
    assert inst.careTeam[0].reference == "#careteam"
    assert inst.contained[0].id == "doce"
    assert inst.contained[1].id == "cisp"
    assert inst.contained[2].id == "fluo"
    assert inst.contained[3].id == "tpf"
    assert inst.contained[4].id == "careteam"
    assert inst.contained[5].id == "goal"
    assert inst.goal[0].reference == "#goal"
    assert inst.id == "f202"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_careplan_2(base_settings):
    """No. 2 tests collection for CarePlan.
    Test File: careplan-example-f202-malignancy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "careplan-example-f202-malignancy.json"
    )
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_2(inst2)


def impl_careplan_3(inst):
    assert inst.id == "obesity-narrative"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "additional"


def test_careplan_3(base_settings):
    """No. 3 tests collection for CarePlan.
    Test File: careplan-example-obesity-narrative.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "careplan-example-obesity-narrative.json"
    )
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_3(inst2)


def impl_careplan_4(inst):
    assert inst.activity[0].detail.code.coding[0].code == "3141-9"
    assert inst.activity[0].detail.code.coding[0].display == "Weight Measured"
    assert inst.activity[0].detail.code.coding[0].system == "http://loinc.org"
    assert inst.activity[0].detail.code.coding[1].code == "27113001"
    assert inst.activity[0].detail.code.coding[1].display == "Body weight"
    assert inst.activity[0].detail.code.coding[1].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.doNotPerform is False
    assert inst.activity[0].detail.location.display == "Patient's home"
    assert inst.activity[0].detail.performer[0].display == "Peter James Chalmers"
    assert inst.activity[0].detail.performer[0].reference == "Patient/example"
    assert inst.activity[0].detail.scheduledTiming.repeat.frequency == 1
    assert float(inst.activity[0].detail.scheduledTiming.repeat.period) == float(1)
    assert inst.activity[0].detail.scheduledTiming.repeat.periodUnit == "d"
    assert inst.activity[0].detail.status == "completed"
    assert (
        inst.activity[0].detail.statusReason.text
        == "Achieved weight loss to mitigate diabetes risk."
    )
    assert inst.activity[0].outcomeCodeableConcept[0].coding[0].code == "161832001"
    assert (
        inst.activity[0].outcomeCodeableConcept[0].coding[0].display
        == "Progressive weight loss"
    )
    assert (
        inst.activity[0].outcomeCodeableConcept[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.activity[0].outcomeReference[0].display == "Weight Measured"
    assert inst.activity[0].outcomeReference[0].reference == "Observation/example"
    assert inst.addresses[0].display == "obesity"
    assert inst.addresses[0].reference == "#p1"
    assert inst.author.display == "Dr Adam Careful"
    assert inst.author.reference == "Practitioner/example"
    assert inst.basedOn[0].display == "Management of Type 2 Diabetes"
    assert inst.careTeam[0].reference == "CareTeam/example"
    assert inst.category[0].text == "Weight management plan"
    assert inst.contained[0].id == "p1"
    assert inst.created == fhirtypes.DateTime.validate("2016-01-01")
    assert inst.description == "Manage obesity and weight loss"
    assert inst.encounter.reference == "Encounter/home"
    assert inst.goal[0].reference == "Goal/example"
    assert inst.id == "example"
    assert inst.identifier[0].value == "12345"
    assert inst.instantiatesUri[0] == "http://example.org/protocol-for-obesity"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.partOf[0].display == "Overall wellness plan"
    assert inst.period.end == fhirtypes.DateTime.validate("2017-06-01")
    assert inst.replaces[0].display == "Plan from urgent care clinic"
    assert inst.status == "active"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "additional"


def test_careplan_4(base_settings):
    """No. 4 tests collection for CarePlan.
    Test File: careplan-example.json
    """
    filename = base_settings["unittest_data_dir"] / "careplan-example.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_4(inst2)


def impl_careplan_5(inst):
    assert inst.activity[0].detail.code.coding[0].code == "284093001"
    assert inst.activity[0].detail.code.coding[0].display == "Potassium supplementation"
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.dailyAmount.code == "258718000"
    assert inst.activity[0].detail.dailyAmount.system == "http://snomed.info/sct"
    assert inst.activity[0].detail.dailyAmount.unit == "mmol"
    assert float(inst.activity[0].detail.dailyAmount.value) == float(80)
    assert inst.activity[0].detail.doNotPerform is False
    assert inst.activity[0].detail.kind == "NutritionOrder"
    assert inst.activity[0].detail.productReference.display == "Potassium"
    assert inst.activity[0].detail.productReference.reference == "Substance/f203"
    assert inst.activity[0].detail.scheduledString == "daily"
    assert inst.activity[0].detail.status == "completed"
    assert inst.activity[1].detail.code.coding[0].code == "306005"
    assert inst.activity[1].detail.code.coding[0].display == "Echography of kidney"
    assert inst.activity[1].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[1].detail.doNotPerform is False
    assert inst.activity[1].detail.kind == "ServiceRequest"
    assert inst.activity[1].detail.status == "completed"
    assert inst.addresses[0].display == "Roel's renal insufficiency"
    assert inst.addresses[0].reference == "Condition/f204"
    assert inst.careTeam[0].reference == "#careteam"
    assert inst.contained[0].id == "careteam"
    assert inst.contained[1].id == "goal"
    assert inst.goal[0].reference == "#goal"
    assert inst.id == "f201"
    assert inst.intent == "proposal"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2013-03-13")
    assert inst.period.start == fhirtypes.DateTime.validate("2013-03-11")
    assert inst.status == "draft"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_careplan_5(base_settings):
    """No. 5 tests collection for CarePlan.
    Test File: careplan-example-f201-renal.json
    """
    filename = base_settings["unittest_data_dir"] / "careplan-example-f201-renal.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_5(inst2)


def impl_careplan_6(inst):
    assert inst.activity[0].detail.code.coding[0].code == "nursecon"
    assert inst.activity[0].detail.code.coding[0].system == "http://example.org/local"
    assert inst.activity[0].detail.code.text == "Nurse Consultation"
    assert inst.activity[0].detail.doNotPerform is False
    assert inst.activity[0].detail.kind == "Appointment"
    assert inst.activity[0].detail.performer[0].display == "Nurse Nancy"
    assert inst.activity[0].detail.performer[0].reference == "Practitioner/13"
    assert inst.activity[0].detail.scheduledPeriod.end == fhirtypes.DateTime.validate(
        "2013-01-01T10:50:00+00:00"
    )
    assert inst.activity[0].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2013-01-01T10:38:00+00:00"
    )
    assert inst.activity[0].detail.status == "completed"
    assert inst.activity[0].outcomeReference[0].reference == "Encounter/example"
    assert inst.activity[1].detail.code.coding[0].code == "doccon"
    assert inst.activity[1].detail.code.coding[0].system == "http://example.org/local"
    assert inst.activity[1].detail.code.text == "Doctor Consultation"
    assert inst.activity[1].detail.doNotPerform is False
    assert inst.activity[1].detail.kind == "Appointment"
    assert inst.activity[1].detail.performer[0].display == "Doctor Dave"
    assert inst.activity[1].detail.performer[0].reference == "Practitioner/14"
    assert inst.activity[1].detail.status == "scheduled"
    assert inst.addresses[0].display == "obesity"
    assert inst.addresses[0].reference == "#p1"
    assert inst.careTeam[0].reference == "#careteam"
    assert inst.contained[0].id == "p1"
    assert inst.contained[1].id == "careteam"
    assert inst.contained[2].id == "goal"
    assert inst.goal[0].reference == "#goal"
    assert inst.id == "gpvisit"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.start == fhirtypes.DateTime.validate("2013-01-01T10:30:00+00:00")
    assert inst.status == "active"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/100"
    assert inst.text.status == "additional"


def test_careplan_6(base_settings):
    """No. 6 tests collection for CarePlan.
    Test File: careplan-example-GPVisit.json
    """
    filename = base_settings["unittest_data_dir"] / "careplan-example-GPVisit.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_6(inst2)


def impl_careplan_7(inst):
    assert inst.activity[0].detail.description == (
        "Eve will review photos of high and low density foods and "
        "share with her parents"
    )
    assert inst.activity[0].detail.doNotPerform is False
    assert (
        inst.activity[0].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[0].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )
    assert inst.activity[0].detail.goal[0].reference == "#g1"
    assert inst.activity[0].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-09-10"
    )
    assert inst.activity[0].detail.status == "not-started"
    assert (
        inst.activity[0].progress[0].text == "Eve eats one meal a day with her parents"
    )
    assert inst.activity[0].progress[0].time == fhirtypes.DateTime.validate(
        "2012-09-10"
    )
    assert inst.activity[1].detail.description == (
        "Eve will ask her dad to asist her to put the head of her bed" " on blocks"
    )
    assert inst.activity[1].detail.doNotPerform is False
    assert (
        inst.activity[1].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[1].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )
    assert inst.activity[1].detail.goal[0].reference == "#g1"
    assert inst.activity[1].detail.kind == "CommunicationRequest"
    assert inst.activity[1].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-09-10"
    )
    assert inst.activity[1].detail.status == "not-started"
    assert (
        inst.activity[1].progress[0].text
        == "Eve will sleep in her bed more often than the couch"
    )
    assert inst.activity[1].progress[0].time == fhirtypes.DateTime.validate(
        "2012-09-10"
    )
    assert (
        inst.activity[2].detail.description
        == "Eve will reduce her intake of coffee and chocolate"
    )
    assert inst.activity[2].detail.doNotPerform is False
    assert (
        inst.activity[2].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[2].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )
    assert inst.activity[2].detail.goal[0].reference == "#g2"
    assert inst.activity[2].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-09-10"
    )
    assert inst.activity[2].detail.status == "in-progress"
    assert inst.activity[3].detail.description == (
        "Eve will walk her friend's dog up and down a big hill 15-30 "
        "minutes 3 days a week"
    )
    assert inst.activity[3].detail.doNotPerform is False
    assert (
        inst.activity[3].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[3].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )
    assert inst.activity[3].detail.goal[0].reference == "#g3"
    assert inst.activity[3].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-08-27"
    )
    assert inst.activity[3].detail.status == "in-progress"
    assert (
        inst.activity[3].progress[0].text == "Eve would like to try for 5 days a week."
    )
    assert inst.activity[3].progress[0].time == fhirtypes.DateTime.validate(
        "2012-08-27"
    )
    assert inst.activity[3].progress[1].text == "Eve is still walking the dogs."
    assert inst.activity[3].progress[1].time == fhirtypes.DateTime.validate(
        "2012-09-10"
    )
    assert (
        inst.activity[4].detail.description
        == "Eve will walk 3 blocks to her parents house twice a week"
    )
    assert inst.activity[4].detail.doNotPerform is False
    assert (
        inst.activity[4].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[4].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )
    assert inst.activity[4].detail.goal[0].reference == "#g3"
    assert inst.activity[4].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-07-23"
    )
    assert inst.activity[4].detail.status == "in-progress"
    assert inst.activity[4].progress[0].text == "Eve walked 4 times the last week."
    assert inst.activity[4].progress[0].time == fhirtypes.DateTime.validate(
        "2012-08-13"
    )
    assert inst.activity[4].progress[1].text == (
        "Eve did not walk to her parents the last week, but has plans" " to start again"
    )
    assert inst.activity[4].progress[1].time == fhirtypes.DateTime.validate(
        "2012-09-10"
    )
    assert inst.activity[5].detail.description == (
        "Eve will use a calendar to check off after medications are " "taken"
    )
    assert inst.activity[5].detail.doNotPerform is False
    assert (
        inst.activity[5].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[5].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-08-13"
    )
    assert inst.activity[5].detail.goal[0].reference == "#g4"
    assert inst.activity[5].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-07-23"
    )
    assert inst.activity[5].detail.status == "in-progress"
    assert (
        inst.activity[6].detail.description
        == "Eve will use her lights MWF after her shower for 3 minutes"
    )
    assert inst.activity[6].detail.doNotPerform is False
    assert (
        inst.activity[6].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[6].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-08-27"
    )
    assert inst.activity[6].detail.goal[0].reference == "#g5"
    assert inst.activity[6].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-07-23"
    )
    assert inst.activity[6].detail.status == "in-progress"
    assert inst.activity[6].progress[0].text == (
        "After restarting the vinegar soaks the psoriasis is improved"
        " and Eve plans to treat the remainder with light treatments."
        "  She plans to start this week."
    )
    assert inst.activity[6].progress[0].time == fhirtypes.DateTime.validate(
        "2012-08-13"
    )
    assert inst.activity[6].progress[1].text == (
        "Since her skin is improved Eve has not been using the light "
        "treatment as often, maybe once a week.  She would like to "
        "increase to 3 times a week again"
    )
    assert inst.activity[6].progress[1].time == fhirtypes.DateTime.validate(
        "2012-08-27"
    )
    assert inst.activity[7].detail.description == (
        "Eve will use a calendar of a chart to help her remember when"
        " to take her medications"
    )
    assert inst.activity[7].detail.doNotPerform is False
    assert (
        inst.activity[7].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[7].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )
    assert inst.activity[7].detail.goal[0].reference == "#g4"
    assert inst.activity[7].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-07-10"
    )
    assert inst.activity[7].detail.status == "in-progress"
    assert inst.activity[7].progress[0].text == (
        "Eve created a chart as a reminer to take the medications "
        "that do not fit in her pill box"
    )
    assert inst.activity[7].progress[0].time == fhirtypes.DateTime.validate(
        "2012-07-23"
    )
    assert inst.activity[8].detail.description == (
        "Eve will start using stretch bands and one step 2 days a "
        "week Mon/Wed 6-7am and maybe Friday afternoon"
    )
    assert inst.activity[8].detail.doNotPerform is False
    assert (
        inst.activity[8].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[8].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-08-23"
    )
    assert inst.activity[8].detail.goal[0].reference == "#g3"
    assert inst.activity[8].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-07-23"
    )
    assert inst.activity[8].detail.status == "on-hold"
    assert inst.activity[8].progress[0].text == "Will be able to esume exercise."
    assert inst.activity[8].progress[0].time == fhirtypes.DateTime.validate(
        "2012-07-30"
    )
    assert (
        inst.activity[8].progress[1].text
        == "Eve prefers to focus on walking at this time"
    )
    assert inst.activity[8].progress[1].time == fhirtypes.DateTime.validate(
        "2012-08-13"
    )
    assert inst.activity[9].detail.description == (
        "Eve will match a printed medication worksheet with the "
        "medication bottles at home"
    )
    assert inst.activity[9].detail.doNotPerform is False
    assert (
        inst.activity[9].detail.extension[0].url
        == "http://example.org/fhir/StructureDefinition/RevisionDate"
    )
    assert inst.activity[9].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-07-23"
    )
    assert inst.activity[9].detail.goal[0].reference == "#g4"
    assert inst.activity[9].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2012-07-10"
    )
    assert inst.activity[9].detail.status == "completed"
    assert inst.addresses[0].display == "GERDS"
    assert inst.addresses[0].reference == "#p1"
    assert inst.addresses[1].display == "Obesity"
    assert inst.addresses[1].reference == "#p2"
    assert inst.addresses[2].display == "Psoriasis"
    assert inst.addresses[2].reference == "#p3"
    assert inst.contained[0].id == "p1"
    assert inst.contained[1].id == "p2"
    assert inst.contained[2].id == "p3"
    assert inst.contained[3].id == "g1"
    assert inst.contained[4].id == "g2"
    assert inst.contained[5].id == "g3"
    assert inst.contained[6].id == "g4"
    assert inst.contained[7].id == "g5"
    assert inst.goal[0].reference == "#g1"
    assert inst.goal[1].reference == "#g2"
    assert inst.goal[2].reference == "#g3"
    assert inst.goal[3].reference == "#g4"
    assert inst.goal[4].reference == "#g5"
    assert inst.id == "integrate"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == (
        "Patient family is not ready to commit to goal setting at "
        "this time.  Goal setting will be addressed in the future"
    )
    assert inst.status == "active"
    assert inst.subject.display == "Eve Everywoman"
    assert inst.subject.reference == "Patient/1"
    assert inst.text.status == "generated"


def test_careplan_7(base_settings):
    """No. 7 tests collection for CarePlan.
    Test File: careplan-example-integrated.json
    """
    filename = base_settings["unittest_data_dir"] / "careplan-example-integrated.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_7(inst2)


def impl_careplan_8(inst):
    assert inst.activity[0].detail.code.coding[0].code == "172960003"
    assert (
        inst.activity[0].detail.code.coding[0].display
        == "Incision of retropharyngeal abscess"
    )
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.doNotPerform is True
    assert inst.activity[0].detail.kind == "ServiceRequest"
    assert inst.activity[0].detail.performer[0].display == "E.M. van den broek"
    assert inst.activity[0].detail.performer[0].reference == "Practitioner/f001"
    assert inst.activity[0].detail.scheduledString == "2011-06-27T09:30:10+01:00"
    assert inst.activity[0].detail.status == "completed"
    assert inst.addresses[0].display == "?????"
    assert inst.addresses[0].reference == "Condition/f201"
    assert inst.careTeam[0].reference == "#careteam"
    assert inst.contained[0].id == "careteam"
    assert inst.contained[1].id == "goal"
    assert inst.goal[0].reference == "#goal"
    assert inst.id == "f003"
    assert (
        inst.identifier[0].system
        == "http://www.bmc.nl/zorgportal/identifiers/careplans"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "CP3953"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2013-03-08T09:30:10+01:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2013-03-08T09:00:10+01:00")
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_careplan_8(base_settings):
    """No. 8 tests collection for CarePlan.
    Test File: careplan-example-f003-pharynx.json
    """
    filename = base_settings["unittest_data_dir"] / "careplan-example-f003-pharynx.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_8(inst2)


def impl_careplan_9(inst):
    assert inst.activity[0].detail.code.coding[0].code == "64915003"
    assert inst.activity[0].detail.code.coding[0].display == "Operation on heart"
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.doNotPerform is True
    assert inst.activity[0].detail.kind == "ServiceRequest"
    assert inst.activity[0].detail.performer[0].display == "P. Voigt"
    assert inst.activity[0].detail.performer[0].reference == "Practitioner/f002"
    assert inst.activity[0].detail.scheduledString == "2011-06-27T09:30:10+01:00"
    assert inst.activity[0].detail.status == "completed"
    assert inst.addresses[0].display == "?????"
    assert inst.addresses[0].reference == "Condition/f201"
    assert inst.careTeam[0].reference == "#careteam"
    assert inst.contained[0].id == "careteam"
    assert inst.contained[1].id == "goal"
    assert inst.goal[0].reference == "#goal"
    assert inst.id == "f001"
    assert (
        inst.identifier[0].system
        == "http://www.bmc.nl/zorgportal/identifiers/careplans"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "CP2903"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2011-06-27")
    assert inst.period.start == fhirtypes.DateTime.validate("2011-06-26")
    assert inst.status == "completed"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_careplan_9(base_settings):
    """No. 9 tests collection for CarePlan.
    Test File: careplan-example-f001-heart.json
    """
    filename = base_settings["unittest_data_dir"] / "careplan-example-f001-heart.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_9(inst2)


def impl_careplan_10(inst):
    assert inst.activity[0].reference.display == "Prenatal vitamin MedicationRequest"
    assert inst.activity[1].detail.code.coding[0].code == "1an"
    assert (
        inst.activity[1].detail.code.coding[0].system == "http://example.org/mySystem"
    )
    assert inst.activity[1].detail.code.text == "First Antenatal encounter"
    assert inst.activity[1].detail.description == (
        "The first antenatal encounter. This is where a detailed "
        "physical examination is performed.             and the "
        "pregnanacy discussed with the mother-to-be."
    )
    assert inst.activity[1].detail.doNotPerform is False
    assert inst.activity[1].detail.kind == "Appointment"
    assert inst.activity[1].detail.performer[0].display == "Mavis Midwife"
    assert inst.activity[1].detail.performer[0].reference == "#pr1"
    assert inst.activity[
        1
    ].detail.scheduledTiming.repeat.boundsPeriod.end == fhirtypes.DateTime.validate(
        "2013-02-28"
    )
    assert inst.activity[
        1
    ].detail.scheduledTiming.repeat.boundsPeriod.start == fhirtypes.DateTime.validate(
        "2013-02-14"
    )
    assert inst.activity[1].detail.status == "scheduled"
    assert inst.activity[1].extension[0].url == (
        "http://example.org/fhir/StructureDefinition/careplan#andetai" "ls"
    )
    assert (
        inst.activity[1].extension[0].valueUri
        == "http://orionhealth.com/fhir/careplan/1andetails"
    )
    assert inst.activity[2].detail.code.coding[0].code == "an"
    assert (
        inst.activity[2].detail.code.coding[0].system == "http://example.org/mySystem"
    )
    assert inst.activity[2].detail.code.text == "Follow-up Antenatal encounter"
    assert inst.activity[2].detail.description == (
        "The second antenatal encounter. Discuss any issues that "
        "arose from the first antenatal encounter"
    )
    assert inst.activity[2].detail.doNotPerform is False
    assert inst.activity[2].detail.kind == "Appointment"
    assert inst.activity[2].detail.performer[0].display == "Mavis Midwife"
    assert inst.activity[2].detail.performer[0].reference == "#pr1"
    assert inst.activity[
        2
    ].detail.scheduledTiming.repeat.boundsPeriod.end == fhirtypes.DateTime.validate(
        "2013-03-14"
    )
    assert inst.activity[
        2
    ].detail.scheduledTiming.repeat.boundsPeriod.start == fhirtypes.DateTime.validate(
        "2013-03-01"
    )
    assert inst.activity[2].detail.status == "not-started"
    assert inst.activity[3].detail.code.coding[0].code == "del"
    assert (
        inst.activity[3].detail.code.coding[0].system == "http://example.org/mySystem"
    )
    assert inst.activity[3].detail.code.text == "Delivery"
    assert inst.activity[3].detail.description == "The delivery."
    assert inst.activity[3].detail.doNotPerform is False
    assert inst.activity[3].detail.kind == "Appointment"
    assert inst.activity[3].detail.performer[0].display == "Mavis Midwife"
    assert inst.activity[3].detail.performer[0].reference == "#pr1"
    assert inst.activity[
        3
    ].detail.scheduledTiming.repeat.boundsPeriod.end == fhirtypes.DateTime.validate(
        "2013-09-14"
    )
    assert inst.activity[
        3
    ].detail.scheduledTiming.repeat.boundsPeriod.start == fhirtypes.DateTime.validate(
        "2013-09-01"
    )
    assert inst.activity[3].detail.status == "not-started"
    assert inst.addresses[0].display == "pregnancy"
    assert inst.addresses[0].reference == "#p1"
    assert inst.careTeam[0].reference == "#careteam"
    assert inst.contained[0].id == "p1"
    assert inst.contained[1].id == "pr1"
    assert inst.contained[2].id == "pr2"
    assert inst.contained[3].id == "careteam"
    assert inst.contained[4].id == "goal"
    assert (
        inst.extension[0].url
        == "http://example.org/fhir/StructureDefinition/careplan#lmp"
    )
    assert inst.extension[0].valueDateTime == fhirtypes.DateTime.validate("2013-01-01")
    assert inst.goal[0].reference == "#goal"
    assert inst.id == "preg"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2013-10-01")
    assert inst.period.start == fhirtypes.DateTime.validate("2013-01-01")
    assert inst.status == "active"
    assert inst.subject.display == "Eve Everywoman"
    assert inst.subject.reference == "Patient/1"
    assert inst.text.status == "additional"


def test_careplan_10(base_settings):
    """No. 10 tests collection for CarePlan.
    Test File: careplan-example-pregnancy.json
    """
    filename = base_settings["unittest_data_dir"] / "careplan-example-pregnancy.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type

    impl_careplan_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_careplan_10(inst2)
