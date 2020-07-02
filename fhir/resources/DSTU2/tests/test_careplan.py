# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CarePlan
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from .. import fhirtypes  # noqa: F401
from .. import careplan


def test_CarePlan_1(base_settings):
    """"""
    filename = base_settings["unittest_data_dir"] / "careplan-example-f203-sepsis.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_1(inst2)


def impl_CarePlan_1(inst):
    assert inst.activity[0].detail.category.coding[0].code == "observation"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )

    assert inst.activity[0].detail.code.coding[0].code == "241541005"
    assert inst.activity[0].detail.code.coding[0].display == (
        "High resolution computed tomography of lungs"
    )

    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"

    assert inst.activity[0].detail.prohibited is False
    assert inst.activity[0].detail.status == "not-started"
    assert inst.contained[0].id == "goal"
    assert inst.id == "f203"
    assert inst.modified == fhirtypes.Date.validate("2013-03-11")
    assert inst.participant[0].role.coding[0].code == "425268008"
    assert inst.participant[0].role.coding[0].display == "Review of care plan"

    assert inst.participant[0].role.coding[0].system == "http://snomed.info/sct"
    assert inst.participant[1].role.coding[0].code == "278110001"
    assert inst.participant[1].role.coding[0].display == "Radiographic imaging"
    assert inst.participant[1].role.coding[0].system == "http://snomed.info/sct"

    assert inst.period.end == fhirtypes.Date.validate("2013-04-21")
    assert inst.period.start == fhirtypes.Date.validate("2013-04-14")
    assert inst.status == "completed"
    assert inst.text.status == "generated"


def test_CarePlan_2(base_settings):
    filename = base_settings["unittest_data_dir"] / "careplan-example-pregnancy.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_2(inst2)


def impl_CarePlan_2(inst):
    assert inst.activity[0].detail.category.coding[0].code == "encounter"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[0].detail.code.coding[0].code == "1an"
    assert inst.activity[0].detail.code.coding[0].system == (
        "http://example.org/mySystem"
    )
    assert inst.activity[0].detail.code.text == "First Antenatal encounter"
    assert inst.activity[0].detail.description == (
        "The first antenatal encounter. "
        "This is where a detailed physical examination "
        "is performed.             and the pregnanacy "
        "discussed with the mother-to-be."
    )
    assert inst.activity[0].detail.prohibited is False
    assert inst.activity[
        0
    ].detail.scheduledTiming.repeat.boundsPeriod.end == fhirtypes.Date.validate(
        "2013-02-28"
    )

    assert inst.activity[
        0
    ].detail.scheduledTiming.repeat.boundsPeriod.start == fhirtypes.Date.validate(
        "2013-02-14"
    )

    assert inst.activity[0].detail.status == "scheduled"
    assert inst.activity[0].extension[0].url == (
        "http://example.org/DoNotUse/careplan#andetails"
    )
    assert inst.activity[0].extension[0].valueUri == (
        "http://orionhealth.com/fhir/careplan/1andetails"
    )
    assert inst.activity[1].detail.category.coding[0].code == "encounter"
    assert inst.activity[1].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[1].detail.code.coding[0].code == "an"
    assert inst.activity[1].detail.code.coding[0].system == (
        "http://example.org/mySystem"
    )
    assert inst.activity[1].detail.code.text == "Follow-up Antenatal encounter"
    assert inst.activity[1].detail.description == (
        "The second antenatal encounter. "
        "Discuss any issues that arose from the first antenatal encounter"
    )
    assert inst.activity[1].detail.prohibited is False
    assert inst.activity[
        1
    ].detail.scheduledTiming.repeat.boundsPeriod.end == fhirtypes.Date.validate(
        "2013-03-14"
    )

    assert inst.activity[
        1
    ].detail.scheduledTiming.repeat.boundsPeriod.start == fhirtypes.Date.validate(
        "2013-03-01"
    )

    assert inst.activity[1].detail.status == "not-started"
    assert inst.activity[2].detail.category.coding[0].code == "encounter"
    assert inst.activity[2].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[2].detail.code.coding[0].code == "del"
    assert inst.activity[2].detail.code.coding[0].system == (
        "http://example.org/mySystem"
    )
    assert inst.activity[2].detail.code.text == "Delivery"
    assert inst.activity[2].detail.description == "The delivery."
    assert inst.activity[2].detail.prohibited is False
    assert inst.activity[
        2
    ].detail.scheduledTiming.repeat.boundsPeriod.end == fhirtypes.Date.validate(
        "2013-09-14"
    )
    assert inst.activity[
        2
    ].detail.scheduledTiming.repeat.boundsPeriod.start == fhirtypes.Date.validate(
        "2013-09-01"
    )
    assert inst.activity[2].detail.status == "not-started"
    assert inst.contained[0].id == "p1"
    assert inst.contained[1].id == "pr1"
    assert inst.contained[2].id == "pr2"
    assert inst.contained[3].id == "goal"
    assert inst.extension[0].url == "http://example.org/DoNotUse/careplan#lmp"
    assert inst.extension[0].valueDateTime == fhirtypes.Date.validate("2013-01-01")

    assert inst.id == "preg"
    assert inst.participant[0].role.coding[0].code == "lmc"
    assert inst.participant[0].role.coding[0].system == "http://example.org/mysys"
    assert inst.participant[0].role.text == "Midwife"
    assert inst.participant[1].role.coding[0].code == "obs"
    assert inst.participant[1].role.coding[0].system == "http://example.org/mysys"
    assert inst.participant[1].role.text == "Obstretitian"
    assert inst.period.end == fhirtypes.Date.validate("2013-10-01")

    assert inst.period.start == fhirtypes.Date.validate("2013-01-01")
    assert inst.status == "active"
    assert inst.text.status == "additional"


def test_CarePlan_3(base_settings):
    filename = base_settings["unittest_data_dir"] / "careplan-example-integrated.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_3(inst2)


def impl_CarePlan_3(inst):
    assert inst.activity[0].detail.category.coding[0].code == "other"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[0].detail.description == (
        "Eve will review photos of high and low density foods and share with her parents"
    )
    assert inst.activity[0].detail.extension[0].url == (
        "http://example.org/DoNotUse/StructureDefinition/RevisionDate"
    )
    assert inst.activity[0].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )

    assert inst.activity[0].detail.prohibited is False
    assert inst.activity[0].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-09-10"
    )

    assert inst.activity[0].detail.status == "not-started"
    assert inst.activity[0].progress[0].text == (
        "Eve eats one meal a day with her parents"
    )

    assert inst.activity[0].progress[0].time == fhirtypes.Date.validate("2012-09-10")

    assert inst.activity[1].detail.category.coding[0].code == "other"
    assert inst.activity[1].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[1].detail.description == (
        "Eve will ask her dad to asist her to " "put the head of her bed on blocks"
    )
    assert inst.activity[1].detail.extension[0].url == (
        "http://example.org/DoNotUse/General/RevisionDate"
    )
    assert inst.activity[1].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )
    assert inst.activity[1].detail.prohibited is False
    assert inst.activity[1].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-09-10"
    )

    assert inst.activity[1].detail.status == "not-started"
    assert inst.activity[1].progress[0].text == (
        "Eve will sleep in her bed more often than the couch"
    )
    assert inst.activity[1].progress[0].time == fhirtypes.Date.validate("2012-09-10")

    assert inst.activity[2].detail.category.coding[0].code == "other"
    assert inst.activity[2].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[2].detail.description == (
        "Eve will reduce her intake of coffee and chocolate"
    )
    assert inst.activity[2].detail.extension[0].url == (
        "http://example.org/DoNotUse/General/RevisionDate"
    )
    assert inst.activity[2].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )

    assert inst.activity[2].detail.prohibited is False
    assert inst.activity[2].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-09-10"
    )

    assert inst.activity[2].detail.status == "in-progress"
    assert inst.activity[3].detail.category.coding[0].code == "other"
    assert inst.activity[3].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[3].detail.description == (
        "Eve will walk her friend's dog up and down a big hill 15-30 minutes 3 days a week"
    )
    assert inst.activity[3].detail.extension[0].url == (
        "http://example.org/DoNotUse/General/RevisionDate"
    )
    assert inst.activity[3].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )

    assert inst.activity[3].detail.prohibited is False
    assert inst.activity[3].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-08-27"
    )

    assert inst.activity[3].detail.status == "in-progress"
    assert inst.activity[3].progress[0].text == (
        "Eve would like to try for 5 days a week."
    )
    assert inst.activity[3].progress[0].time == fhirtypes.Date.validate("2012-08-27")

    assert inst.activity[3].progress[1].text == "Eve is still walking the dogs."
    assert inst.activity[3].progress[1].time == fhirtypes.Date.validate("2012-09-10")

    assert inst.activity[4].detail.category.coding[0].code == "other"
    assert inst.activity[4].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[4].detail.description == (
        "Eve will walk 3 blocks to her parents house twice a week"
    )
    assert inst.activity[4].detail.extension[0].url == (
        "http://example.org/DoNotUse/General/RevisionDate"
    )
    assert inst.activity[4].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )
    assert inst.activity[4].detail.prohibited is False
    assert inst.activity[4].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-07-23"
    )

    assert inst.activity[4].detail.status == "in-progress"
    assert inst.activity[4].progress[0].text == "Eve walked 4 times the last week."
    assert inst.activity[4].progress[0].time == fhirtypes.Date.validate("2012-08-13")

    assert inst.activity[4].progress[1].text == (
        "Eve did not walk to her parents the last week, but has plans to start again"
    )
    assert inst.activity[4].progress[1].time == fhirtypes.Date.validate("2012-09-10")

    assert inst.activity[5].detail.category.coding[0].code == "other"
    assert inst.activity[5].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[5].detail.description == (
        "Eve will us a calendar to check off after medications are taken"
    )
    assert inst.activity[5].detail.extension[0].url == (
        "http://example.org/DoNotUse/General/RevisionDate"
    )
    assert inst.activity[5].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-08-13"
    )
    assert inst.activity[5].detail.prohibited is False
    assert inst.activity[5].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-07-23"
    )
    assert inst.activity[5].detail.status == "in-progress"
    assert inst.activity[6].detail.category.coding[0].code == "other"
    assert inst.activity[6].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[6].detail.description == (
        "Eve will use her lights MWF after her shower for 3 minutes"
    )
    assert inst.activity[6].detail.extension[0].url == (
        "http://example.org/DoNotUse/General/RevisionDate"
    )
    assert inst.activity[6].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-08-27"
    )
    assert inst.activity[6].detail.prohibited is False
    assert inst.activity[6].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-07-23"
    )

    assert inst.activity[6].detail.status == "in-progress"
    assert inst.activity[6].progress[0].text == (
        "After restarting the vinegar soaks the psoriasis is "
        "improved and Eve plans to treat the remainder "
        "with light treatments.  She plans to start this week."
    )
    assert inst.activity[6].progress[0].time == fhirtypes.Date.validate("2012-08-13")
    assert inst.activity[6].progress[1].text == (
        "Since her skin is improved Eve has not "
        "been using the light treatment as often, maybe "
        "once a week.  She would like to increase to "
        "3 times a week again"
    )
    assert inst.activity[6].progress[1].time == fhirtypes.Date.validate("2012-08-27")

    assert inst.activity[7].detail.category.coding[0].code == "other"
    assert inst.activity[7].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[7].detail.description == (
        "Eve will use a calendar of a chart to help "
        "her remember when to take her medications"
    )
    assert inst.activity[7].detail.extension[0].url == (
        "http://example.org/DoNotUse/General/RevisionDate"
    )
    assert inst.activity[7].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-09-10"
    )

    assert inst.activity[7].detail.prohibited is False
    assert inst.activity[7].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-07-10"
    )
    assert inst.activity[7].detail.status == "in-progress"
    assert inst.activity[7].progress[0].text == (
        "Eve created a chart as a reminer to take "
        "the medications that do not fit in her pill box"
    )
    assert inst.activity[7].progress[0].time == fhirtypes.Date.validate("2012-07-23")
    assert inst.activity[8].detail.category.coding[0].code == "other"
    assert inst.activity[8].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[8].detail.description == (
        "Eve will start using stretch bands and one step "
        "2 days a week Mon/Wed 6-7am and maybe Friday afternoon"
    )
    assert inst.activity[8].detail.extension[0].url == (
        "http://example.org/DoNotUse/General/RevisionDate"
    )
    assert inst.activity[8].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-08-23"
    )
    assert inst.activity[8].detail.prohibited is False
    assert inst.activity[8].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-07-23"
    )

    assert inst.activity[8].detail.status == "on-hold"
    assert inst.activity[8].progress[0].text == "Will be able to esume exercise."
    assert inst.activity[8].progress[0].time == fhirtypes.Date.validate("2012-07-30")

    assert inst.activity[8].progress[1].text == (
        "Eve prefers to focus on walking at this time"
    )
    assert inst.activity[8].progress[1].time == fhirtypes.Date.validate("2012-08-13")

    assert inst.activity[9].detail.category.coding[0].code == "other"
    assert inst.activity[9].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[9].detail.description == (
        "Eve will match a printed medication worksheet with the medication bottles at home"
    )
    assert inst.activity[9].detail.extension[0].url == (
        "http://example.org/DoNotUse/General/RevisionDate"
    )
    assert inst.activity[9].detail.extension[0].valueDate == fhirtypes.Date.validate(
        "2012-07-23"
    )
    assert inst.activity[9].detail.prohibited is False
    assert inst.activity[9].detail.scheduledPeriod.start == fhirtypes.Date.validate(
        "2012-07-10"
    )
    assert inst.activity[9].detail.status == "completed"
    assert inst.contained[0].id == "p1"
    assert inst.contained[1].id == "p2"
    assert inst.contained[2].id == "p3"
    assert inst.contained[3].id == "g1"
    assert inst.contained[4].id == "g2"
    assert inst.contained[5].id == "g3"
    assert inst.contained[6].id == "g4"
    assert inst.contained[7].id == "g5"
    assert inst.id == "integrate"
    assert inst.modified == fhirtypes.Date.validate("2012-09-10")

    assert inst.note.text == (
        "Patient family is not ready to commit to goal "
        "setting at this time.  Goal setting will "
        "be addressed in the future"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_CarePlan_4(base_settings):
    filename = base_settings["unittest_data_dir"] / "careplan-example-f001-heart.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_4(inst2)


def impl_CarePlan_4(inst):
    assert inst.activity[0].detail.category.coding[0].code == "procedure"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[0].detail.code.coding[0].code == "64915003"
    assert inst.activity[0].detail.code.coding[0].display == "Operation on heart"
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.prohibited is True
    assert inst.activity[0].detail.scheduledString == "2011-06-27T09:30:10+01:00"
    assert inst.activity[0].detail.status == "completed"
    assert inst.contained[0].id == "goal"
    assert inst.id == "f001"
    assert inst.identifier[0].system == (
        "http://www.bmc.nl/zorgportal/identifiers/careplans"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "CP2903"
    assert inst.modified == fhirtypes.DateTime.validate("2011-06-27T09:30:10+01:00")
    assert inst.period.end == fhirtypes.Date.validate("2011-06-27")

    assert inst.period.start == fhirtypes.Date.validate("2011-06-26")
    assert inst.status == "completed"
    assert inst.text.status == "generated"


def test_CarePlan_5(base_settings):
    filename = base_settings["unittest_data_dir"] / "careplan-example-f201-renal.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_5(inst2)


def impl_CarePlan_5(inst):
    assert inst.activity[0].detail.category.coding[0].code == "diet"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[0].detail.code.coding[0].code == "284093001"
    assert inst.activity[0].detail.code.coding[0].display == "Potassium supplementation"
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.dailyAmount.code == "258718000"
    assert inst.activity[0].detail.dailyAmount.system == "http://snomed.info/sct"
    assert inst.activity[0].detail.dailyAmount.unit == "mmol"
    assert inst.activity[0].detail.dailyAmount.value == 80
    assert inst.activity[0].detail.prohibited is False
    assert inst.activity[0].detail.scheduledString == "daily"
    assert inst.activity[0].detail.status == "completed"
    assert inst.activity[1].detail.category.coding[0].code == "observation"
    assert inst.activity[1].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[1].detail.code.coding[0].code == "306005"
    assert inst.activity[1].detail.code.coding[0].display == "Echography of kidney"
    assert inst.activity[1].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[1].detail.prohibited is False
    assert inst.activity[1].detail.status == "completed"
    assert inst.contained[0].id == "goal"
    assert inst.id == "f201"
    assert inst.modified == fhirtypes.Date.validate("2013-03-11")

    assert inst.participant[0].role.coding[0].code == "425268008"
    assert inst.participant[0].role.coding[0].display == "Review of care plan"
    assert inst.participant[0].role.coding[0].system == "http://snomed.info/sct"
    assert inst.participant[1].role.coding[0].code == "229774002"
    assert inst.participant[1].role.coding[0].display == "Carer"
    assert inst.participant[1].role.coding[0].system == "http://snomed.info/sct"
    assert inst.period.end == fhirtypes.Date.validate("2013-03-13")

    assert inst.period.start == fhirtypes.Date.validate("2013-03-11")

    assert inst.status == "draft"
    assert inst.text.status == "generated"


def test_CarePlan_6(base_settings):
    filename = base_settings["unittest_data_dir"] / "careplan-example-GPVisit.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_6(inst2)


def impl_CarePlan_6(inst):
    assert inst.activity[0].detail.category.coding[0].code == "encounter"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )

    assert inst.activity[0].detail.code.coding[0].code == "nursecon"
    assert inst.activity[0].detail.code.coding[0].system == "http://example.org/local"
    assert inst.activity[0].detail.code.text == "Nurse Consultation"
    assert inst.activity[0].detail.prohibited is False
    assert inst.activity[0].detail.scheduledPeriod.end == fhirtypes.DateTime.validate(
        "2013-01-01T10:50:00+00:00"
    )
    assert inst.activity[0].detail.scheduledPeriod.start == fhirtypes.DateTime.validate(
        "2013-01-01T10:38:00+00:00"
    )

    assert inst.activity[0].detail.status == "completed"
    assert inst.activity[1].detail.category.coding[0].code == "encounter"
    assert inst.activity[1].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )

    assert inst.activity[1].detail.code.coding[0].code == "doccon"
    assert inst.activity[1].detail.code.coding[0].system == "http://example.org/local"
    assert inst.activity[1].detail.code.text == "Doctor Consultation"
    assert inst.activity[1].detail.prohibited is False
    assert inst.activity[1].detail.status == "scheduled"
    assert inst.contained[0].id == "p1"
    assert inst.contained[1].id == "goal"
    assert inst.id == "gpvisit"
    assert inst.participant[0].id == "part1"
    assert inst.participant[0].role.coding[0].code == "nur"
    assert inst.participant[0].role.coding[0].system == "http://example.org/local"
    assert inst.participant[0].role.text == "nurse"
    assert inst.participant[1].id == "part2"
    assert inst.participant[1].role.coding[0].code == "doc"
    assert inst.participant[1].role.coding[0].system == "http://example.org/local"
    assert inst.participant[1].role.text == "doctor"
    assert inst.period.start == fhirtypes.DateTime.validate("2013-01-01T10:30:00+00:00")

    assert inst.status == "active"
    assert inst.text.status == "additional"


def test_CarePlan_7(base_settings):
    filename = base_settings["unittest_data_dir"] / "careplan-example.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_7(inst2)


def impl_CarePlan_7(inst):
    assert inst.activity[0].detail.category.coding[0].code == "observation"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[0].detail.code.text == "a code for weight measurement"
    assert inst.activity[0].detail.prohibited is False
    assert inst.activity[0].detail.scheduledTiming.repeat.frequency == 1
    assert inst.activity[0].detail.scheduledTiming.repeat.period == 1
    assert inst.activity[0].detail.scheduledTiming.repeat.periodUnits == "d"
    assert inst.contained[0].id == "p1"
    assert inst.contained[1].id == "pr1"
    assert inst.contained[2].id == "goal"
    assert inst.id == "example"
    assert inst.participant[0].role.text == "responsiblePerson"
    assert inst.participant[1].role.text == "adviser"
    assert inst.period.end == fhirtypes.DateTime.validate("2013-01-01")

    assert inst.status == "active"
    assert inst.text.status == "additional"


def test_CarePlan_8(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "careplan-example-f202-malignancy.json"
    )
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_8(inst2)


def impl_CarePlan_8(inst):
    assert inst.activity[0].detail.category.coding[0].code == "procedure"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[0].detail.code.coding[0].code == "367336001"
    assert inst.activity[0].detail.code.coding[0].display == "Chemotherapy"
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.prohibited is False
    assert inst.activity[0].detail.status == "in-progress"
    assert inst.contained[0].id == "doce"
    assert inst.contained[1].id == "cisp"
    assert inst.contained[2].id == "fluo"
    assert inst.contained[3].id == "tpf"
    assert inst.contained[4].id == "goal"
    assert inst.id == "f202"
    assert inst.participant[0].role.coding[0].code == "28995006"
    assert inst.participant[0].role.coding[0].display == "Treated with"
    assert inst.participant[0].role.coding[0].system == "http://snomed.info/sct"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_CarePlan_9(base_settings):
    filename = base_settings["unittest_data_dir"] / "careplan-example-f003-pharynx.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_9(inst2)


def impl_CarePlan_9(inst):
    assert inst.activity[0].detail.category.coding[0].code == "procedure"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[0].detail.code.coding[0].code == "172960003"
    assert inst.activity[0].detail.code.coding[0].display == (
        "Incision of retropharyngeal abscess"
    )
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.prohibited is True
    assert inst.activity[0].detail.scheduledString == "2011-06-27T09:30:10+01:00"
    assert inst.activity[0].detail.status == "completed"
    assert inst.contained[0].id == "goal"
    assert inst.id == "f003"
    assert inst.identifier[0].system == (
        "http://www.bmc.nl/zorgportal/identifiers/careplans"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "CP3953"
    assert inst.modified, fhirtypes.DateTime.validate("2013-06-27T09:30:10+01:00")

    assert inst.period.end == fhirtypes.DateTime.validate("2013-03-08T09:30:10+01:00")

    assert inst.period.start == fhirtypes.DateTime.validate("2013-03-08T09:00:10+01:00")

    assert inst.status == "completed"
    assert inst.text.status == "generated"


def test_CarePlan_10(base_settings):
    filename = base_settings["unittest_data_dir"] / "careplan-example-f002-lung.json"
    inst = careplan.CarePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CarePlan" == inst.resource_type
    impl_CarePlan_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CarePlan" == data["resourceType"]

    inst2 = careplan.CarePlan(**data)
    impl_CarePlan_10(inst2)


def impl_CarePlan_10(inst):
    assert inst.activity[0].detail.category.coding[0].code == "procedure"
    assert inst.activity[0].detail.category.coding[0].system == (
        "http://hl7.org/fhir/care-plan-activity-category"
    )
    assert inst.activity[0].detail.code.coding[0].code == "359615001"
    assert inst.activity[0].detail.code.coding[0].display == "Partial lobectomy of lung"
    assert inst.activity[0].detail.code.coding[0].system == "http://snomed.info/sct"
    assert inst.activity[0].detail.prohibited is True
    assert inst.activity[0].detail.scheduledString == "2011-07-07T09:30:10+01:00"
    assert inst.activity[0].detail.status == "completed"
    assert inst.contained[0].id == "goal"
    assert inst.id == "f002"
    assert inst.identifier[0].system == (
        "http://www.bmc.nl/zorgportal/identifiers/careplans"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "CP2934"
    assert inst.modified == fhirtypes.DateTime.validate("2011-07-07T09:30:10+01:00")

    assert inst.period.end == fhirtypes.DateTime.validate("2013-07-07")

    assert inst.period.start == fhirtypes.DateTime.validate("2011-07-06")

    assert inst.status == "completed"
    assert inst.text.status == "generated"
