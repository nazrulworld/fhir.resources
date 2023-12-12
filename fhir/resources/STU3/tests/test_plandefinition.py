# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import plandefinition


def impl_plandefinition_1(inst):
    assert (
        inst.action[0].action[0].action[0].action[0].action[0].definition.reference
        == "#1111"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[0]
        .extension[0]
        .extension[0]
        .url
        == "day"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[0]
        .extension[0]
        .extension[0]
        .valueInteger
        == 1
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[0]
        .extension[0]
        .extension[1]
        .url
        == "day"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[0]
        .extension[0]
        .extension[1]
        .valueInteger
        == 8
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"
    )
    assert inst.action[0].action[0].action[0].action[0].action[0].id == "action-1"
    assert (
        inst.action[0].action[0].action[0].action[0].action[0].textEquivalent
        == "Gemcitabine 1250 mg/m² IV over 30 minutes on days 1 and 8"
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[1].definition.reference
        == "#2222"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[1]
        .extension[0]
        .extension[0]
        .url
        == "day"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[1]
        .extension[0]
        .extension[0]
        .valueInteger
        == 1
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[1].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"
    )
    assert inst.action[0].action[0].action[0].action[0].action[1].id == "action-2"
    assert (
        inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].actionId
        == "action-1"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[1]
        .relatedAction[0]
        .relationship
        == "concurrent-with-start"
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[1].textEquivalent
        == "CARBOplatin AUC 5 IV over 30 minutes on Day 1"
    )
    assert inst.action[0].action[0].action[0].action[0].id == "cycle-definition-1"
    assert (
        inst.action[0].action[0].action[0].action[0].textEquivalent
        == "21-day cycle for 6 cycles"
    )
    assert inst.action[0].action[0].action[0].action[0].timingTiming.repeat.count == 6
    assert float(
        inst.action[0].action[0].action[0].action[0].timingTiming.repeat.duration
    ) == float(21)
    assert (
        inst.action[0].action[0].action[0].action[0].timingTiming.repeat.durationUnit
        == "d"
    )
    assert inst.action[0].action[0].action[0].groupingBehavior == "sentence-group"
    assert inst.action[0].action[0].action[0].selectionBehavior == "exactly-one"
    assert inst.action[0].action[0].selectionBehavior == "all"
    assert inst.action[0].selectionBehavior == "exactly-one"
    assert inst.approvalDate == fhirtypes.Date.validate("2016-07-27")
    assert inst.contained[0].id == "1111"
    assert inst.contained[1].id == "2222"
    assert inst.contributor[0].name == "Lee Surprenant"
    assert inst.contributor[0].type == "author"
    assert inst.copyright == "All rights reserved."
    assert inst.experimental is True
    assert inst.id == "KDN5"
    assert inst.identifier[0].system == "http://example.org/ordertemplates"
    assert inst.identifier[0].value == "KDN5"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2016-07-27")
    assert inst.publisher == "National Comprehensive Cancer Network, Inc."
    assert (
        inst.relatedArtifact[0].display == "NCCN Guidelines for Kidney Cancer. V.2.2016"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.relatedArtifact[0].url == (
        "http://www.example.org/professionals/physician_gls/PDF/kidne" "y.pdf"
    )
    assert (
        inst.relatedArtifact[1].citation
        == "Oudard S, et al. J Urol. 2007;177(5):1698-702"
    )
    assert inst.relatedArtifact[1].type == "citation"
    assert inst.relatedArtifact[1].url == "http://www.ncbi.nlm.nih.gov/pubmed/17437788"
    assert inst.status == "draft"
    assert inst.text.status == "additional"
    assert inst.title == "Gemcitabine/CARBOplatin"
    assert inst.type.text == "Chemotherapy Order Template"
    assert inst.useContext[0].code.code == "treamentSetting-or-diseaseStatus"
    assert (
        inst.useContext[0].code.system
        == "http://example.org/fhir/CodeSystem/indications"
    )
    assert (
        inst.useContext[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    )
    assert inst.useContext[0].extension[0].valueString == "A"
    assert inst.useContext[0].valueCodeableConcept.text == "Metastatic"
    assert inst.useContext[1].code.code == "disease-or-histology"
    assert (
        inst.useContext[1].code.system
        == "http://example.org/fhir/CodeSystem/indications"
    )
    assert (
        inst.useContext[1].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    )
    assert inst.useContext[1].extension[0].valueString == "A"
    assert (
        inst.useContext[1].valueCodeableConcept.text
        == "Collecting Duct/Medullary Subtypes"
    )
    assert inst.useContext[2].code.code == "focus"
    assert inst.useContext[2].code.system == "http://hl7.org/fhir/usage-context-type"
    assert (
        inst.useContext[2].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    )
    assert inst.useContext[2].extension[0].valueString == "A"
    assert inst.useContext[2].valueCodeableConcept.text == "Kidney Cancer"
    assert inst.useContext[3].code.code == "treatmentSetting-or-diseaseStatus"
    assert (
        inst.useContext[3].code.system
        == "http://example.org/fhir/CodeSystem/indications"
    )
    assert (
        inst.useContext[3].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    )
    assert inst.useContext[3].extension[0].valueString == "B"
    assert inst.useContext[3].valueCodeableConcept.text == "Relapsed"
    assert inst.useContext[4].code.code == "disease-or-histology"
    assert (
        inst.useContext[4].code.system
        == "http://example.org/fhir/CodeSystem/indications"
    )
    assert (
        inst.useContext[4].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    )
    assert inst.useContext[4].extension[0].valueString == "B"
    assert (
        inst.useContext[4].valueCodeableConcept.text
        == "Collecting Duct/Medullary Subtypes"
    )
    assert inst.useContext[5].code.code == "focus"
    assert inst.useContext[5].code.system == "http://hl7.org/fhir/usage-context-type"
    assert (
        inst.useContext[5].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/usagecontext-group"
    )
    assert inst.useContext[5].extension[0].valueString == "B"
    assert inst.useContext[5].valueCodeableConcept.text == (
        "Kidney Cancer – Collecting Duct/Medullary Subtypes - " "Metastatic"
    )
    assert inst.version == "1"


def test_plandefinition_1(base_settings):
    """No. 1 tests collection for PlanDefinition.
    Test File: plandefinition-example-kdn5-simplified.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-example-kdn5-simplified.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_1(inst2)


def impl_plandefinition_2(inst):
    assert (
        inst.action[0].action[0].definition.reference
        == "#activitydefinition-medicationrequest-1"
    )
    assert inst.action[0].action[0].id == "medication-action-1"
    assert inst.action[0].action[0].title == "Administer Medication 1"
    assert (
        inst.action[0].action[1].definition.reference
        == "#activitydefinition-medicationrequest-2"
    )
    assert inst.action[0].action[1].id == "medication-action-2"
    assert inst.action[0].action[1].relatedAction[0].actionId == "medication-action-1"
    assert inst.action[0].action[1].relatedAction[0].offsetDuration.unit == "h"
    assert float(
        inst.action[0].action[1].relatedAction[0].offsetDuration.value
    ) == float(1)
    assert inst.action[0].action[1].relatedAction[0].relationship == "after-end"
    assert inst.action[0].action[1].title == "Administer Medication 2"
    assert inst.action[0].groupingBehavior == "logical-group"
    assert inst.action[0].selectionBehavior == "all"
    assert inst.contained[0].id == "activitydefinition-medicationrequest-1"
    assert inst.contained[1].id == "activitydefinition-medicationrequest-2"
    assert inst.id == "options-example"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "This example illustrates relationships between actions."


def test_plandefinition_2(base_settings):
    """No. 2 tests collection for PlanDefinition.
    Test File: plandefinition-options-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-options-example.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_2(inst2)


def impl_plandefinition_3(inst):
    assert (
        inst.action[0].action[0].dynamicValue[0].expression
        == "Communication Request to Provider"
    )
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert inst.action[0].action[0].textEquivalent == (
        "A Breastfeeding Readiness Assessment is recommended, please "
        "authorize or reject the order."
    )
    assert inst.action[0].action[0].title == "Notify the provider to sign the order."
    assert inst.action[0].action[0].type.code == "create"
    assert (
        inst.action[0].condition[0].expression
        == "Should Notify Provider to Sign Assessment Order"
    )
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
        "Mother should be administered a breastfeeding readiness " "assessment."
    )
    assert inst.action[0].triggerDefinition[0].eventName == "Admission"
    assert inst.action[0].triggerDefinition[0].type == "named-event"
    assert inst.action[0].triggerDefinition[1].eventName == "Birth"
    assert inst.action[0].triggerDefinition[1].type == "named-event"
    assert (
        inst.action[0].triggerDefinition[2].eventName == "Infant Transfer to Recovery"
    )
    assert inst.action[0].triggerDefinition[2].type == "named-event"
    assert inst.action[0].triggerDefinition[3].eventName == "Transfer to Post-Partum"
    assert inst.action[0].triggerDefinition[3].type == "named-event"
    assert inst.date == fhirtypes.DateTime.validate("2015-03-08")
    assert inst.id == "exclusive-breastfeeding-intervention-02"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-intervention-02"
    assert (
        inst.library[0].reference == "Library/library-exclusive-breastfeeding-cds-logic"
    )
    assert (
        inst.relatedArtifact[0].resource.reference
        == "Measure/measure-exclusive-breastfeeding"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Intervention-02"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.version == "1.0.0"


def test_plandefinition_3(base_settings):
    """No. 3 tests collection for PlanDefinition.
    Test File: plandefinition-exclusive-breastfeeding-intervention-02.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-exclusive-breastfeeding-intervention-02.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_3(inst2)


def impl_plandefinition_4(inst):
    assert (
        inst.action[0].action[0].dynamicValue[0].expression
        == "Communication Request to Charge Nurse"
    )
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert inst.action[0].action[0].textEquivalent == (
        "A Breastfeeding Readiness Assessment is recommended, please "
        "administer the assessment."
    )
    assert (
        inst.action[0].action[0].title
        == "Notify the charge nurse to perform the assessment."
    )
    assert inst.action[0].action[0].type.code == "create"
    assert (
        inst.action[0].action[1].dynamicValue[0].expression
        == "Communication Request to Bedside Nurse"
    )
    assert inst.action[0].action[1].dynamicValue[0].path == "/"
    assert inst.action[0].action[1].textEquivalent == (
        "A Breastfeeding Readiness Assessment is recommended, please "
        "administer the assessment."
    )
    assert (
        inst.action[0].action[1].title
        == "Notify the bedside nurse to perform the assessment."
    )
    assert inst.action[0].action[1].type.code == "create"
    assert (
        inst.action[0].condition[0].expression
        == "Should Notify Nurse to Perform Assessment"
    )
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
        "Mother should be administered a breastfeeding readiness " "assessment."
    )
    assert inst.action[0].triggerDefinition[0].eventName == "Admission"
    assert inst.action[0].triggerDefinition[0].type == "named-event"
    assert inst.action[0].triggerDefinition[1].eventName == "Birth"
    assert inst.action[0].triggerDefinition[1].type == "named-event"
    assert (
        inst.action[0].triggerDefinition[2].eventName == "Infant Transfer to Recovery"
    )
    assert inst.action[0].triggerDefinition[2].type == "named-event"
    assert inst.action[0].triggerDefinition[3].eventName == "Transfer to Post-Partum"
    assert inst.action[0].triggerDefinition[3].type == "named-event"
    assert inst.date == fhirtypes.DateTime.validate("2015-03-08")
    assert inst.id == "exclusive-breastfeeding-intervention-03"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-intervention-03"
    assert (
        inst.library[0].reference == "Library/library-exclusive-breastfeeding-cds-logic"
    )
    assert (
        inst.relatedArtifact[0].resource.reference
        == "Measure/measure-exclusive-breastfeeding"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Intervention-03"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.version == "1.0.0"


def test_plandefinition_4(base_settings):
    """No. 4 tests collection for PlanDefinition.
    Test File: plandefinition-exclusive-breastfeeding-intervention-03.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-exclusive-breastfeeding-intervention-03.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_4(inst2)


def impl_plandefinition_5(inst):
    assert inst.action[0].cardinalityBehavior == "single"
    assert inst.action[0].condition[0].expression == (
        "exists ([Condition: Obesity]) or not exists ([Observation: "
        "BMI] O where O.effectiveDateTime 2 years or less before "
        "Today())"
    )
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].condition[0].language == "text/cql"
    assert inst.action[0].definition.reference == "#procedure"
    assert inst.action[0].goalId[0] == "reduce-bmi-ratio"
    assert inst.action[0].label == "Measure BMI"
    assert inst.action[0].requiredBehavior == "must-unless-documented"
    assert (
        inst.action[0].title
        == "Measure, Weight, Height, Waist, Circumference; Calculate BMI"
    )
    assert inst.contained[0].id == "procedure"
    assert inst.contributor[0].contact[0].telecom[0].system == "url"
    assert (
        inst.contributor[0].contact[0].telecom[0].value
        == "https://www.nhlbi.nih.gov/health-pro/guidelines"
    )
    assert inst.contributor[0].name == "National Heart, Lung, and Blood Institute"
    assert inst.contributor[0].type == "author"
    assert inst.goal[0].addresses[0].coding[0].code == "414916001"
    assert inst.goal[0].addresses[0].coding[0].display == "Obesity (disorder)"
    assert inst.goal[0].addresses[0].coding[0].system == "http://snomed.info/sct"
    assert inst.goal[0].category.text == "Treatment"
    assert inst.goal[0].description.text == "Reduce BMI to below 25"
    assert inst.goal[0].documentation[0].display == "Evaluation and Treatment Strategy"
    assert inst.goal[0].documentation[0].type == "justification"
    assert inst.goal[0].documentation[0].url == (
        "https://www.nhlbi.nih.gov/health-"
        "pro/guidelines/current/obesity-"
        "guidelines/e_textbook/txgd/42.htm"
    )
    assert inst.goal[0].id == "reduce-bmi-ratio"
    assert inst.goal[0].priority.text == "medium-priority"
    assert inst.goal[0].start.text == "When the patient's BMI Ratio is at or above 25"
    assert inst.goal[0].target[0].detailRange.high.unit == "kg/m2"
    assert float(inst.goal[0].target[0].detailRange.high.value) == float(24.9)
    assert inst.goal[0].target[0].due.unit == "a"
    assert float(inst.goal[0].target[0].due.value) == float(1)
    assert inst.goal[0].target[0].measure.coding[0].code == "39156-5"
    assert (
        inst.goal[0].target[0].measure.coding[0].display
        == "Body mass index (BMI) [Ratio]"
    )
    assert inst.goal[0].target[0].measure.coding[0].system == "http://loinc.org"
    assert inst.id == "protocol-example"
    assert inst.identifier[0].system == "http://acme.org"
    assert inst.identifier[0].value == "example-1"
    assert inst.purpose == (
        "Example of A medical algorithm for assessment and treatment "
        "of overweight and obesity"
    )
    assert (
        inst.relatedArtifact[0].display == "Overweight and Obesity Treatment Guidelines"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.relatedArtifact[0].url == (
        "http://www.nhlbi.nih.gov/health-"
        "pro/guidelines/current/obesity-"
        "guidelines/e_textbook/txgd/algorthm/algorthm.htm"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Obesity Assessment Protocol"
    assert inst.type.coding[0].code == "protocol"
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "414916001"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Obesity (disorder)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )


def test_plandefinition_5(base_settings):
    """No. 5 tests collection for PlanDefinition.
    Test File: plandefinition-protocol-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-protocol-example.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_5(inst2)


def impl_plandefinition_6(inst):
    assert (
        inst.action[0].action[0].action[0].definition.reference
        == "#referralToMentalHealthCare"
    )
    assert inst.action[0].action[0].action[0].dynamicValue[0].expression == "Now()"
    assert inst.action[0].action[0].action[0].dynamicValue[0].path == "timing.event"
    assert inst.action[0].action[0].action[0].dynamicValue[1].expression == (
        "Code '261QM0850X' from SuicideRiskLogic.\"NUCC Provider "
        "Taxonomy\" display 'Adult Mental Health'"
    )
    assert inst.action[0].action[0].action[0].dynamicValue[1].path == "specialty"
    assert (
        inst.action[0].action[0].action[0].dynamicValue[2].expression
        == "SuicideRiskLogic.ReferralRequestFulfillmentTime"
    )
    assert (
        inst.action[0].action[0].action[0].dynamicValue[2].path == "occurrenceDateTime"
    )
    assert (
        inst.action[0].action[0].action[0].dynamicValue[3].expression
        == "SuicideRiskLogic.Patient"
    )
    assert inst.action[0].action[0].action[0].dynamicValue[3].path == "subject"
    assert (
        inst.action[0].action[0].action[0].dynamicValue[4].expression
        == "SuicideRiskLogic.Practitioner"
    )
    assert inst.action[0].action[0].action[0].dynamicValue[4].path == "requester.agent"
    assert (
        inst.action[0].action[0].action[0].dynamicValue[5].expression
        == "SuicideRiskLogic.RiskAssessmentScore"
    )
    assert inst.action[0].action[0].action[0].dynamicValue[5].path == "reasonCode"
    assert (
        inst.action[0].action[0].action[0].dynamicValue[6].expression
        == "SuicideRiskLogic.RiskAssessment"
    )
    assert inst.action[0].action[0].action[0].dynamicValue[6].path == "reasonReference"
    assert inst.action[0].action[0].action[0].textEquivalent == (
        "Refer to outpatient mental health program for evaluation and"
        " treatment of mental health conditions now"
    )
    assert inst.action[0].action[0].groupingBehavior == "logical-group"
    assert inst.action[0].action[0].selectionBehavior == "any"
    assert inst.action[0].action[0].title == "Consults and Referrals"
    assert (
        inst.action[0].action[1].action[0].action[0].action[0].definition.reference
        == "#citalopramPrescription"
    )
    assert (
        inst.action[0]
        .action[1]
        .action[0]
        .action[0]
        .action[0]
        .dynamicValue[0]
        .expression
        == "'draft'"
    )
    assert (
        inst.action[0].action[1].action[0].action[0].action[0].dynamicValue[0].path
        == "status"
    )
    assert (
        inst.action[0]
        .action[1]
        .action[0]
        .action[0]
        .action[0]
        .dynamicValue[1]
        .expression
        == "SuicideRiskLogic.Patient"
    )
    assert (
        inst.action[0].action[1].action[0].action[0].action[0].dynamicValue[1].path
        == "patient"
    )
    assert (
        inst.action[0]
        .action[1]
        .action[0]
        .action[0]
        .action[0]
        .dynamicValue[2]
        .expression
        == "SuicideRiskLogic.Practitioner"
    )
    assert (
        inst.action[0].action[1].action[0].action[0].action[0].dynamicValue[2].path
        == "prescriber"
    )
    assert (
        inst.action[0]
        .action[1]
        .action[0]
        .action[0]
        .action[0]
        .dynamicValue[3]
        .expression
        == "SuicideRiskLogic.RiskAssessmentScore"
    )
    assert (
        inst.action[0].action[1].action[0].action[0].action[0].dynamicValue[3].path
        == "reasonCode"
    )
    assert (
        inst.action[0]
        .action[1]
        .action[0]
        .action[0]
        .action[0]
        .dynamicValue[4]
        .expression
        == "SuicideRiskLogic.RiskAssessment"
    )
    assert (
        inst.action[0].action[1].action[0].action[0].action[0].dynamicValue[4].path
        == "reasonReference"
    )
    assert inst.action[0].action[1].action[0].action[0].action[0].textEquivalent == (
        "citalopram 20 mg tablet 1 tablet oral 1 time daily now (30 "
        "table; 3 refills)"
    )
    assert inst.action[0].action[1].action[0].action[0].action[1].textEquivalent == (
        "escitalopram 10 mg tablet 1 tablet oral 1 time daily now (30"
        " tablet; 3 refills)"
    )
    assert inst.action[0].action[1].action[0].action[0].action[2].textEquivalent == (
        "fluoxetine 20 mg capsule 1 capsule oral 1 time daily now (30"
        " tablet; 3 refills)"
    )
    assert inst.action[0].action[1].action[0].action[0].action[3].textEquivalent == (
        "paroxetine 20 mg tablet 1 tablet oral 1 time daily now (30 "
        "tablet; 3 refills)"
    )
    assert inst.action[0].action[1].action[0].action[0].action[4].textEquivalent == (
        "sertraline 50 mg tablet 1 tablet oral 1 time daily now (30 "
        "tablet; 3 refills)"
    )
    assert (
        inst.action[0]
        .action[1]
        .action[0]
        .action[0]
        .documentation[0]
        .document.contentType
        == "text/html"
    )
    assert inst.action[0].action[1].action[0].action[0].documentation[
        0
    ].document.title == (
        "National Library of Medicine. DailyMed website. CITALOPRAM- "
        "citalopram hydrobromide tablet, film coated."
    )
    assert inst.action[0].action[1].action[0].action[0].documentation[
        0
    ].document.url == (
        "http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6dae"
        "b45c-451d-b135-bf8f-2d6dff4b6b01"
    )
    assert (
        inst.action[0].action[1].action[0].action[0].documentation[0].type == "citation"
    )
    assert (
        inst.action[0].action[1].action[0].action[0].groupingBehavior == "logical-group"
    )
    assert (
        inst.action[0].action[1].action[0].action[0].selectionBehavior == "at-most-one"
    )
    assert inst.action[0].action[1].action[0].action[0].title == (
        "Selective Serotonin Reuptake Inhibitors (Choose a mazimum of"
        " one or document reasons for exception)"
    )
    assert inst.action[0].action[1].action[0].action[1].textEquivalent == (
        "Dopamine Norepinephrine Reuptake Inhibitors (Choose a "
        "maximum of one or document reasons for exception)"
    )
    assert inst.action[0].action[1].action[0].action[2].textEquivalent == (
        "Serotonin Norepinephrine Reuptake Inhibitors (Choose a "
        "maximum of one or doument reasons for exception)"
    )
    assert inst.action[0].action[1].action[0].action[3].textEquivalent == (
        "Norepinephrine-Serotonin Modulators (Choose a maximum of one"
        " or document reasons for exception)"
    )
    assert (
        inst.action[0].action[1].action[0].documentation[0].document.contentType
        == "text/html"
    )
    assert inst.action[0].action[1].action[0].documentation[0].document.extension[
        0
    ].url == ("http://hl7.org/fhir/StructureDefinition/cqif-" "qualityOfEvidence")
    assert (
        inst.action[0]
        .action[1]
        .action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "high"
    )
    assert (
        inst.action[0]
        .action[1]
        .action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/evidence-quality"
    )
    assert (
        inst.action[0]
        .action[1]
        .action[0]
        .documentation[0]
        .document.extension[0]
        .valueCodeableConcept.text
        == "High Quality"
    )
    assert inst.action[0].action[1].action[0].documentation[0].document.title == (
        "Practice Guideline for the Treatment of Patients with Major "
        "Depressive Disorder"
    )
    assert inst.action[0].action[1].action[0].documentation[0].document.url == (
        "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_"
        "guidelines/guidelines/mdd.pdf"
    )
    assert inst.action[0].action[1].action[0].documentation[0].type == "citation"
    assert inst.action[0].action[1].action[0].groupingBehavior == "logical-group"
    assert inst.action[0].action[1].action[0].selectionBehavior == "at-most-one"
    assert inst.action[0].action[1].action[0].title == "First-Line Antidepressants"
    assert inst.action[0].action[1].groupingBehavior == "logical-group"
    assert inst.action[0].action[1].selectionBehavior == "at-most-one"
    assert inst.action[0].action[1].title == "Medications"
    assert inst.action[0].title == "Suicide Risk Assessment and Outpatient Management"
    assert inst.approvalDate == fhirtypes.Date.validate("2016-03-12")
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "415-362-4007"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "info@motivemi.com"
    assert inst.contained[0].id == "referralToMentalHealthCare"
    assert inst.contained[1].id == "citalopramPrescription"
    assert inst.contained[2].id == "citalopramMedication"
    assert inst.contained[3].id == "citalopramSubstance"
    assert inst.contributor[0].contact[0].telecom[0].system == "phone"
    assert inst.contributor[0].contact[0].telecom[0].use == "work"
    assert inst.contributor[0].contact[0].telecom[0].value == "415-362-4007"
    assert inst.contributor[0].contact[0].telecom[1].system == "email"
    assert inst.contributor[0].contact[0].telecom[1].use == "work"
    assert inst.contributor[0].contact[0].telecom[1].value == "info@motivemi.com"
    assert inst.contributor[0].name == "Motive Medical Intelligence"
    assert inst.contributor[0].type == "author"
    assert inst.copyright == (
        "© Copyright 2016 Motive Medical Intelligence. All rights " "reserved."
    )
    assert inst.date == fhirtypes.DateTime.validate("2015-08-15")
    assert inst.description == (
        "Orders to be applied to a patient characterized as low " "suicide risk."
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate("2017-12-31")
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2016-01-01")
    assert inst.experimental is True
    assert inst.id == "low-suicide-risk-order-set"
    assert inst.identifier[0].system == "http://motivemi.com/artifacts"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "mmi:low-suicide-risk-order-set"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2016-08-15")
    assert inst.library[0].display == "SuicideRiskLogic"
    assert inst.library[0].reference == "Library/suiciderisk-orderset-logic"
    assert inst.name == "LowSuicideRiskOrderSet"
    assert inst.publisher == "Motive Medical Intelligence"
    assert inst.purpose == (
        "This order set helps ensure consistent application of "
        "appropriate orders for the care of low suicide risk "
        "patients."
    )
    assert inst.relatedArtifact[0].display == (
        "Practice Guideline for the Treatment of Patients with Major "
        "Depressive Disorder"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.relatedArtifact[0].url == (
        "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_"
        "guidelines/guidelines/mdd.pdf"
    )
    assert (
        inst.relatedArtifact[1].resource.reference
        == "ActivityDefinition/referralPrimaryCareMentalHealth"
    )
    assert inst.relatedArtifact[1].type == "composed-of"
    assert (
        inst.relatedArtifact[2].resource.reference
        == "ActivityDefinition/citalopramPrescription"
    )
    assert inst.relatedArtifact[2].type == "composed-of"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Low Suicide Risk Order Set"
    assert inst.topic[0].text == "Suicide risk assessment"
    assert inst.url == (
        "http://motivemi.com/artifacts/PlanDefinition/low-suicide-" "risk-order-set"
    )
    assert inst.usage == (
        "This order set should be applied after assessing a patient "
        "for suicide risk, when the findings of that assessment "
        "indicate the patient has low suicide risk."
    )
    assert inst.useContext[0].code.code == "age"
    assert inst.useContext[0].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "D000328"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "Adult"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "https://meshb.nlm.nih.gov"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "87512008"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Mild major depression"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[2].code.code == "focus"
    assert inst.useContext[2].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[2].valueCodeableConcept.coding[0].code == "40379007"
    assert (
        inst.useContext[2].valueCodeableConcept.coding[0].display
        == "Major depression, recurrent, mild"
    )
    assert (
        inst.useContext[2].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[3].code.code == "focus"
    assert inst.useContext[3].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[3].valueCodeableConcept.coding[0].code == "394687007"
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].display == "Low suicide risk"
    )
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[4].code.code == "focus"
    assert inst.useContext[4].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[4].valueCodeableConcept.coding[0].code == "225337009"
    assert (
        inst.useContext[4].valueCodeableConcept.coding[0].display
        == "Suicide risk assessment"
    )
    assert (
        inst.useContext[4].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[5].code.code == "user"
    assert inst.useContext[5].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[5].valueCodeableConcept.coding[0].code == "309343006"
    assert inst.useContext[5].valueCodeableConcept.coding[0].display == "Physician"
    assert (
        inst.useContext[5].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[6].code.code == "venue"
    assert inst.useContext[6].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[6].valueCodeableConcept.coding[0].code == "440655000"
    assert (
        inst.useContext[6].valueCodeableConcept.coding[0].display
        == "Outpatient environment"
    )
    assert (
        inst.useContext[6].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "1.0.0"


def test_plandefinition_6(base_settings):
    """No. 6 tests collection for PlanDefinition.
    Test File: plandefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "plandefinition-example.json"
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_6(inst2)


def impl_plandefinition_7(inst):
    assert (
        inst.action[0].action[0].dynamicValue[0].expression
        == "Create Lactation Consult Request"
    )
    assert inst.action[0].action[0].dynamicValue[0].path == "/"
    assert (
        inst.action[0].action[0].textEquivalent == "Create a lactation consult request"
    )
    assert inst.action[0].action[0].title == "Create a lactation consult request."
    assert inst.action[0].action[0].type.code == "create"
    assert inst.action[0].condition[0].expression == "Should Create Lactation Consult"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == (
        "Mother should be referred to a lactation specialist for " "consultation."
    )
    assert inst.action[0].triggerDefinition[0].eventName == "Admission"
    assert inst.action[0].triggerDefinition[0].type == "named-event"
    assert inst.action[0].triggerDefinition[1].eventName == "Birth"
    assert inst.action[0].triggerDefinition[1].type == "named-event"
    assert (
        inst.action[0].triggerDefinition[2].eventName == "Infant Transfer to Recovery"
    )
    assert inst.action[0].triggerDefinition[2].type == "named-event"
    assert inst.action[0].triggerDefinition[3].eventName == "Transfer to Post-Partum"
    assert inst.action[0].triggerDefinition[3].type == "named-event"
    assert inst.date == fhirtypes.DateTime.validate("2015-03-08")
    assert inst.description == (
        "Exclusive breastfeeding intervention intended to improve "
        "outcomes for exclusive breastmilk feeding of newborns by "
        "creating a lactation consult for the mother if appropriate."
    )
    assert inst.id == "exclusive-breastfeeding-intervention-04"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "exclusive-breastfeeding-intervention-04"
    assert (
        inst.library[0].reference == "Library/library-exclusive-breastfeeding-cds-logic"
    )
    assert (
        inst.relatedArtifact[0].resource.reference
        == "Measure/measure-exclusive-breastfeeding"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding Intervention-04"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.version == "1.0.0"


def test_plandefinition_7(base_settings):
    """No. 7 tests collection for PlanDefinition.
    Test File: plandefinition-exclusive-breastfeeding-intervention-04.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-exclusive-breastfeeding-intervention-04.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_7(inst2)


def impl_plandefinition_8(inst):
    assert (
        inst.action[0].action[0].condition[0].expression
        == "Should Administer Zika Virus Exposure Assessment"
    )
    assert inst.action[0].action[0].condition[0].kind == "applicability"
    assert (
        inst.action[0].action[0].definition.reference
        == "ActivityDefinition/administer-zika-virus-exposure-assessment"
    )
    assert (
        inst.action[0].action[1].condition[0].expression
        == "Should Order Serum + Urine rRT-PCR Test"
    )
    assert inst.action[0].action[1].condition[0].kind == "applicability"
    assert (
        inst.action[0].action[1].definition.reference
        == "ActivityDefinition/order-serum-urine-rrt-pcr-test"
    )
    assert (
        inst.action[0].action[2].condition[0].expression
        == "Should Order Serum Zika Virus IgM + Dengue Virus IgM"
    )
    assert inst.action[0].action[2].condition[0].kind == "applicability"
    assert (
        inst.action[0].action[2].definition.reference
        == "ActivityDefinition/order-serum-zika-dengue-virus-igm"
    )
    assert (
        inst.action[0].action[3].condition[0].expression
        == "Should Consider IgM Antibody Testing"
    )
    assert inst.action[0].action[3].condition[0].kind == "applicability"
    assert (
        inst.action[0].action[3].definition.reference
        == "ActivityDefinition/consider-igm-antibody-testing"
    )
    assert (
        inst.action[0].action[4].action[0].definition.reference
        == "ActivityDefinition/provide-mosquito-prevention-advice"
    )
    assert (
        inst.action[0].action[4].action[1].definition.reference
        == "ActivityDefinition/provide-contraception-advice"
    )
    assert (
        inst.action[0].action[4].condition[0].expression
        == "Should Provide Mosquito Prevention and Contraception Advice"
    )
    assert inst.action[0].action[4].condition[0].kind == "applicability"
    assert inst.action[0].condition[0].expression == "Is Patient Pregnant"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == "Zika Virus Assessment"
    assert inst.action[0].triggerDefinition[0].eventName == "patient-view"
    assert inst.action[0].triggerDefinition[0].type == "named-event"
    assert inst.date == fhirtypes.DateTime.validate("2016-11-14")
    assert inst.description == (
        "Zika Virus Management intervention describing the CDC "
        "Guidelines for Zika Virus Reporting and Management."
    )
    assert inst.id == "zika-virus-intervention-initial"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "zika-virus-intervention"
    assert inst.library[0].reference == "Library/zika-virus-intervention-logic"
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.relatedArtifact[0].url == (
        "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm" "6539e1_w"
    )
    assert (
        inst.relatedArtifact[1].resource.reference
        == "PlanDefinition/zika-virus-intervention"
    )
    assert inst.relatedArtifact[1].type == "successor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Example Zika Virus Intervention"
    assert inst.topic[0].text == "Zika Virus Management"
    assert inst.url == "http://example.org/PlanDefinition/zika-virus-intervention"
    assert inst.version == "1.0.0"


def test_plandefinition_8(base_settings):
    """No. 8 tests collection for PlanDefinition.
    Test File: plandefinition-predecessor-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "plandefinition-predecessor-example.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_8(inst2)


def impl_plandefinition_9(inst):
    assert (
        inst.action[0].action[0].condition[0].expression
        == "Should Administer Zika Virus Exposure Assessment"
    )
    assert inst.action[0].action[0].condition[0].kind == "applicability"
    assert (
        inst.action[0].action[0].definition.reference
        == "ActivityDefinition/administer-zika-virus-exposure-assessment"
    )
    assert (
        inst.action[0].action[1].condition[0].expression
        == "Should Order Serum + Urine rRT-PCR Test"
    )
    assert inst.action[0].action[1].condition[0].kind == "applicability"
    assert (
        inst.action[0].action[1].definition.reference
        == "ActivityDefinition/order-serum-urine-rrt-pcr-test"
    )
    assert (
        inst.action[0].action[2].condition[0].expression
        == "Should Order Serum Zika Virus IgM + Dengue Virus IgM"
    )
    assert inst.action[0].action[2].condition[0].kind == "applicability"
    assert (
        inst.action[0].action[2].definition.reference
        == "ActivityDefinition/order-serum-zika-dengue-virus-igm"
    )
    assert (
        inst.action[0].action[3].condition[0].expression
        == "Should Consider IgM Antibody Testing"
    )
    assert inst.action[0].action[3].condition[0].kind == "applicability"
    assert (
        inst.action[0].action[3].definition.reference
        == "ActivityDefinition/consider-igm-antibody-testing"
    )
    assert (
        inst.action[0].action[4].action[0].definition.reference
        == "ActivityDefinition/provide-mosquito-prevention-advice"
    )
    assert (
        inst.action[0].action[4].action[1].definition.reference
        == "ActivityDefinition/provide-contraception-advice"
    )
    assert (
        inst.action[0].action[4].condition[0].expression
        == "Should Provide Mosquito Prevention and Contraception Advice"
    )
    assert inst.action[0].action[4].condition[0].kind == "applicability"
    assert inst.action[0].condition[0].expression == "Is Patient Pregnant"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].title == "Zika Virus Assessment"
    assert inst.action[0].triggerDefinition[0].eventName == "patient-view"
    assert inst.action[0].triggerDefinition[0].type == "named-event"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-12")
    assert inst.description == (
        "Zika Virus Management intervention describing the CDC "
        "Guidelines for Zika Virus Reporting and Management."
    )
    assert inst.id == "zika-virus-intervention"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "zika-virus-intervention"
    assert inst.library[0].reference == "Library/zika-virus-intervention-logic"
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.relatedArtifact[0].url == (
        "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm" "6539e1_w"
    )
    assert (
        inst.relatedArtifact[1].resource.reference
        == "PlanDefinition/zika-virus-intervention-initial"
    )
    assert inst.relatedArtifact[1].type == "predecessor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Example Zika Virus Intervention"
    assert inst.topic[0].text == "Zika Virus Management"
    assert inst.url == "http://example.org/PlanDefinition/zika-virus-intervention"
    assert inst.version == "2.0.0"


def test_plandefinition_9(base_settings):
    """No. 9 tests collection for PlanDefinition.
    Test File: plandefinition-zika-virus-intervention.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-zika-virus-intervention.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_9(inst2)


def impl_plandefinition_10(inst):
    assert inst.action[0].condition[0].expression == "NoScreening"
    assert inst.action[0].condition[0].kind == "applicability"
    assert inst.action[0].dynamicValue[0].expression == "ChlamydiaScreeningRequest"
    assert inst.action[0].dynamicValue[0].path == "~"
    assert inst.action[0].title == (
        "Patient has not had chlamydia screening within the " "recommended timeframe..."
    )
    assert inst.date == fhirtypes.DateTime.validate("2015-07-22")
    assert inst.description == "Chlamydia Screening CDS Example Using Common"
    assert inst.id == "chlamydia-screening-intervention"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "ChlamydiaScreening_CDS_UsingCommon"
    assert inst.library[0].reference == "Library/example"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Chalmydia Screening CDS Example Using Common"
    assert inst.topic[0].text == "Chlamydia Screeening"
    assert inst.version == "2.0.0"


def test_plandefinition_10(base_settings):
    """No. 10 tests collection for PlanDefinition.
    Test File: plandefinition-chlamydia-screening-intervention.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "plandefinition-chlamydia-screening-intervention.json"
    )
    inst = plandefinition.PlanDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PlanDefinition" == inst.resource_type

    impl_plandefinition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PlanDefinition" == data["resourceType"]

    inst2 = plandefinition.PlanDefinition(**data)
    impl_plandefinition_10(inst2)
