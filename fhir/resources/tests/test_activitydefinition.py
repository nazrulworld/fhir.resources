# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ActivityDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import activitydefinition


def impl_activitydefinition_1(inst):
    assert inst.code.coding[0].code == "zika-virus-exposure-assessment"
    assert inst.code.coding[0].system == "http://example.org/questionnaires"
    assert inst.description == "Administer Zika Virus Exposure Assessment"
    assert inst.experimental is True
    assert inst.id == "administer-zika-virus-exposure-assessment"
    assert inst.kind == "ServiceRequest"
    assert inst.library[0] == (
        "http://example.org/fhir/Library/zika-virus-intervention-" "logic"
    )
    assert inst.participant[0].type == "practitioner"
    assert (
        inst.relatedArtifact[0].document.url
        == "https://www.cdc.gov/zika/hc-providers/pregnant-woman.html"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert (
        inst.relatedArtifact[0].url
        == "https://www.cdc.gov/zika/hc-providers/pregnant-woman.html"
    )
    assert inst.relatedArtifact[1].resource == (
        "http://hl7.org/fhir/Questionnaire/zika-virus-exposure-" "assessment"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == (
        "http://example.org/ActivityDefinition/administer-zika-virus-"
        "exposure-assessment"
    )
    assert inst.useContext[0].code.code == "age"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueRange.low.unit == "a"
    assert float(inst.useContext[0].valueRange.low.value) == float(12)


def test_activitydefinition_1(base_settings):
    """No. 1 tests collection for ActivityDefinition.
    Test File: activitydefinition-administer-zika-virus-exposure-assessment.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "activitydefinition-administer-zika-virus-exposure-assessment.json"
    )
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_1(inst2)


def impl_activitydefinition_2(inst):
    assert inst.code.text == "Provide Mosquito Prevention Advice"
    assert inst.description == "Provide mosquito prevention advice"
    assert inst.experimental is True
    assert inst.id == "provide-mosquito-prevention-advice"
    assert inst.kind == "CommunicationRequest"
    assert inst.library[0] == (
        "http://example.org/fhir/Library/zika-virus-intervention-" "logic"
    )
    assert inst.participant[0].type == "practitioner"
    assert (
        inst.relatedArtifact[0].display
        == "Advice for patients about how to avoid Mosquito bites."
    )
    assert (
        inst.relatedArtifact[0].document.url
        == "http://www.cdc.gov/zika/prevention/index.html"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert (
        inst.relatedArtifact[0].url == "http://www.cdc.gov/zika/prevention/index.html"
    )
    assert inst.relatedArtifact[1].display == (
        "Advice for patients about which mosquito repellents are "
        "effective and safe to use in pregnancy. [DEET, IF3535 and "
        "Picardin are safe during]"
    )
    assert inst.relatedArtifact[1].document.url == (
        "https://www.epa.gov/insect-repellents/find-insect-repellent-" "right-you"
    )
    assert inst.relatedArtifact[1].type == "documentation"
    assert inst.relatedArtifact[1].url == (
        "https://www.epa.gov/insect-repellents/find-insect-repellent-" "right-you"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == (
        "http://example.org/ActivityDefinition/provide-mosquito-" "prevention-advice"
    )


def test_activitydefinition_2(base_settings):
    """No. 2 tests collection for ActivityDefinition.
    Test File: activitydefinition-provide-mosquito-prevention-advice.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "activitydefinition-provide-mosquito-prevention-advice.json"
    )
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_2(inst2)


def impl_activitydefinition_3(inst):
    assert inst.approvalDate == fhirtypes.Date.validate("2016-03-12")
    assert inst.author[0].name == "Motive Medical Intelligence"
    assert inst.author[0].telecom[0].system == "phone"
    assert inst.author[0].telecom[0].use == "work"
    assert inst.author[0].telecom[0].value == "415-362-4007"
    assert inst.author[0].telecom[1].system == "email"
    assert inst.author[0].telecom[1].use == "work"
    assert inst.author[0].telecom[1].value == "info@motivemi.com"
    assert inst.code.coding[0].code == "306206005"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Referral to service (procedure)"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "415-362-4007"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "info@motivemi.com"
    assert inst.copyright == (
        "© Copyright 2016 Motive Medical Intelligence. All rights " "reserved."
    )
    assert inst.date == fhirtypes.DateTime.validate("2017-03-03T14:06:00Z")
    assert inst.description == (
        "refer to primary care mental-health integrated care program "
        "for evaluation and treatment of mental health conditions now"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate("2017-12-31")
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2016-01-01")
    assert inst.experimental is True
    assert inst.id == "referralPrimaryCareMentalHealth-initial"
    assert inst.identifier[0].system == "http://motivemi.com/artifacts"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "referralPrimaryCareMentalHealth"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.kind == "ServiceRequest"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2016-08-15")
    assert inst.name == "ReferralPrimaryCareMentalHealth"
    assert inst.participant[0].type == "practitioner"
    assert inst.publisher == "Motive Medical Intelligence"
    assert inst.relatedArtifact[0].display == (
        "Practice Guideline for the Treatment of Patients with Major "
        "Depressive Disorder"
    )
    assert inst.relatedArtifact[0].document.url == (
        "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_"
        "guidelines/guidelines/mdd.pdf"
    )
    assert inst.relatedArtifact[0].type == "citation"
    assert inst.relatedArtifact[0].url == (
        "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_"
        "guidelines/guidelines/mdd.pdf"
    )
    assert inst.relatedArtifact[1].resource == (
        "http://example.org/fhir/ActivityDefinition/referralPrimaryCa" "reMentalHealth"
    )
    assert inst.relatedArtifact[1].type == "successor"
    assert inst.status == "retired"
    assert inst.text.status == "generated"
    assert inst.title == "Referral to Primary Care Mental Health"
    assert inst.topic[0].text == "Mental Health Referral"
    assert inst.url == (
        "http://motivemi.com/artifacts/ActivityDefinition/referralPri"
        "maryCareMentalHealth"
    )
    assert inst.useContext[0].code.code == "age"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "D000328"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "Adult"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "https://meshb.nlm.nih.gov"
    )
    assert inst.useContext[1].code.code == "focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
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
    assert (
        inst.useContext[2].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
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
    assert (
        inst.useContext[3].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[3].valueCodeableConcept.coding[0].code == "225444004"
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].display
        == "At risk for suicide (finding)"
    )
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[4].code.code == "focus"
    assert (
        inst.useContext[4].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[4].valueCodeableConcept.coding[0].code == "306206005"
    assert (
        inst.useContext[4].valueCodeableConcept.coding[0].display
        == "Referral to service (procedure)"
    )
    assert (
        inst.useContext[4].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[5].code.code == "user"
    assert (
        inst.useContext[5].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[5].valueCodeableConcept.coding[0].code == "309343006"
    assert inst.useContext[5].valueCodeableConcept.coding[0].display == "Physician"
    assert (
        inst.useContext[5].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[6].code.code == "venue"
    assert (
        inst.useContext[6].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
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


def test_activitydefinition_3(base_settings):
    """No. 3 tests collection for ActivityDefinition.
    Test File: activitydefinition-predecessor-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "activitydefinition-predecessor-example.json"
    )
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_3(inst2)


def impl_activitydefinition_4(inst):
    assert inst.code.text == "Serum Zika and Dengue Virus IgM"
    assert inst.description == "Order Serum Zika and Dengue Virus IgM"
    assert inst.experimental is True
    assert inst.id == "serum-zika-dengue-virus-igm"
    assert inst.kind == "ServiceRequest"
    assert inst.library[0] == (
        "http://example.org/fhir/Library/zika-virus-intervention-" "logic"
    )
    assert inst.participant[0].type == "practitioner"
    assert inst.relatedArtifact[0].display == (
        "Explanation of diagnostic tests for Zika virus and which to "
        "use based on the patient’s clinical and exposure history."
    )
    assert (
        inst.relatedArtifact[0].document.url
        == "http://www.cdc.gov/zika/hc-providers/diagnostic.html"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert (
        inst.relatedArtifact[0].url
        == "http://www.cdc.gov/zika/hc-providers/diagnostic.html"
    )
    assert inst.relatedArtifact[1].resource == (
        "http://example.org/fhir/ActivityDefinition/serum-dengue-" "virus-igm"
    )
    assert inst.relatedArtifact[1].type == "derived-from"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == (
        "http://example.org/ActivityDefinition/serum-zika-dengue-" "virus-igm"
    )


def test_activitydefinition_4(base_settings):
    """No. 4 tests collection for ActivityDefinition.
    Test File: activitydefinition-order-serum-zika-dengue-virus-igm.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "activitydefinition-order-serum-zika-dengue-virus-igm.json"
    )
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_4(inst2)


def impl_activitydefinition_5(inst):
    assert inst.approvalDate == fhirtypes.Date.validate("2016-03-12")
    assert inst.author[0].name == "Motive Medical Intelligence"
    assert inst.author[0].telecom[0].system == "phone"
    assert inst.author[0].telecom[0].use == "work"
    assert inst.author[0].telecom[0].value == "415-362-4007"
    assert inst.author[0].telecom[1].system == "email"
    assert inst.author[0].telecom[1].use == "work"
    assert inst.author[0].telecom[1].value == "info@motivemi.com"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "415-362-4007"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "info@motivemi.com"
    assert inst.contained[0].id == "citalopramMedication"
    assert inst.contained[1].id == "citalopramSubstance"
    assert inst.copyright == (
        "© Copyright 2016 Motive Medical Intelligence. All rights " "reserved."
    )
    assert inst.date == fhirtypes.DateTime.validate("2015-08-15")
    assert inst.description == (
        "Citalopram 20 mg tablet 1 tablet oral 1 time daily now (30 " "table; 3 refills"
    )
    assert inst.dosage[0].doseAndRate[0].doseQuantity.unit == "{tbl}"
    assert float(inst.dosage[0].doseAndRate[0].doseQuantity.value) == float(1)
    assert inst.dosage[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosage[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosage[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosage[0].route.coding[0].code == "26643006"
    assert inst.dosage[0].route.coding[0].display == "Oral route (qualifier value)"
    assert inst.dosage[0].route.text == "Oral route (qualifier value)"
    assert inst.dosage[0].text == "1 tablet oral 1 time daily"
    assert inst.dosage[0].timing.repeat.frequency == 1
    assert float(inst.dosage[0].timing.repeat.period) == float(1)
    assert inst.dosage[0].timing.repeat.periodUnit == "d"
    assert (
        inst.dynamicValue[0].expression.description
        == "dispenseRequest.numberOfRepeatsAllowed is three (3)"
    )
    assert inst.dynamicValue[0].expression.expression == "3"
    assert inst.dynamicValue[0].expression.language == "text/cql"
    assert inst.dynamicValue[0].path == "dispenseRequest.numberOfRepeatsAllowed"
    assert (
        inst.dynamicValue[1].expression.description
        == "dispenseRequest.quantity is thirty (30) tablets"
    )
    assert inst.dynamicValue[1].expression.expression == "30 '{tbl}'"
    assert inst.dynamicValue[1].expression.language == "text/cql"
    assert inst.dynamicValue[1].path == "dispenseRequest.quantity"
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate("2017-12-31")
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2016-01-01")
    assert inst.experimental is True
    assert inst.id == "citalopramPrescription"
    assert inst.identifier[0].system == "http://motivemi.com"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "citalopramPrescription"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.kind == "MedicationRequest"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2016-08-15")
    assert inst.name == "CitalopramPrescription"
    assert inst.productReference.reference == "#citalopramMedication"
    assert inst.publisher == "Motive Medical Intelligence"
    assert inst.purpose == (
        "Defines a guideline supported prescription for the treatment"
        " of depressive disorders"
    )
    assert inst.relatedArtifact[0].display == (
        "Practice Guideline for the Treatment of Patients with Major "
        "Depressive Disorder"
    )
    assert inst.relatedArtifact[0].document.url == (
        "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_"
        "guidelines/guidelines/mdd.pdf"
    )
    assert inst.relatedArtifact[0].type == "citation"
    assert inst.relatedArtifact[0].url == (
        "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_"
        "guidelines/guidelines/mdd.pdf"
    )
    assert inst.relatedArtifact[1].resource == "#citalopramMedication"
    assert inst.relatedArtifact[1].type == "composed-of"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Citalopram Prescription"
    assert inst.topic[0].text == "Mental Health Treatment"
    assert inst.url == (
        "http://motivemi.com/artifacts/ActivityDefinition/citalopramP" "rescription"
    )
    assert inst.usage == (
        "This activity definition is used as part of various suicide " "risk order sets"
    )
    assert inst.useContext[0].code.code == "age"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "D000328"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "Adult"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "https://meshb.nlm.nih.gov"
    )
    assert inst.useContext[1].code.code == "focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
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
    assert (
        inst.useContext[2].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
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
    assert (
        inst.useContext[3].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[3].valueCodeableConcept.coding[0].code == "225444004"
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].display
        == "At risk for suicide (finding)"
    )
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[4].code.code == "focus"
    assert (
        inst.useContext[4].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[4].valueCodeableConcept.coding[0].code == "306206005"
    assert (
        inst.useContext[4].valueCodeableConcept.coding[0].display
        == "Referral to service (procedure)"
    )
    assert (
        inst.useContext[4].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[5].code.code == "user"
    assert (
        inst.useContext[5].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[5].valueCodeableConcept.coding[0].code == "309343006"
    assert inst.useContext[5].valueCodeableConcept.coding[0].display == "Physician"
    assert (
        inst.useContext[5].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[6].code.code == "venue"
    assert (
        inst.useContext[6].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
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


def test_activitydefinition_5(base_settings):
    """No. 5 tests collection for ActivityDefinition.
    Test File: activitydefinition-medicationorder-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "activitydefinition-medicationorder-example.json"
    )
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_5(inst2)


def impl_activitydefinition_6(inst):
    assert inst.code.coding[0].code == "1155608"
    assert inst.code.coding[0].display == "alteplase injectable product"
    assert inst.code.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.dosage[0].doseAndRate[0].doseQuantity.code == "mg/kg"
    assert (
        inst.dosage[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    )
    assert float(inst.dosage[0].doseAndRate[0].doseQuantity.value) == float(0.9)
    assert inst.dosage[0].doseAndRate[0].type.coding[0].code == "calculated"
    assert inst.dosage[0].doseAndRate[0].type.coding[0].display == "Calculated"
    assert (
        inst.dosage[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosage[0].maxDosePerAdministration.code == "mg"
    assert inst.dosage[0].maxDosePerAdministration.system == "http://unitsofmeasure.org"
    assert float(inst.dosage[0].maxDosePerAdministration.value) == float(90)
    assert inst.dosage[0].route.coding[0].code == "47625008"
    assert inst.dosage[0].route.coding[0].display == "Intravenous use"
    assert inst.dosage[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage[0].sequence == 1
    assert inst.dosage[0].text == "give 10% of dose over 1 minute"
    assert inst.dosage[1].doseAndRate[0].doseQuantity.code == "mg/kg"
    assert (
        inst.dosage[1].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    )
    assert float(inst.dosage[1].doseAndRate[0].doseQuantity.value) == float(0.9)
    assert inst.dosage[1].doseAndRate[0].type.coding[0].code == "calculated"
    assert inst.dosage[1].doseAndRate[0].type.coding[0].display == "Calculated"
    assert (
        inst.dosage[1].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosage[1].maxDosePerAdministration.code == "mg"
    assert inst.dosage[1].maxDosePerAdministration.system == "http://unitsofmeasure.org"
    assert float(inst.dosage[1].maxDosePerAdministration.value) == float(90)
    assert inst.dosage[1].route.coding[0].code == "47625008"
    assert inst.dosage[1].route.coding[0].display == "Intravenous use"
    assert inst.dosage[1].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage[1].sequence == 2
    assert inst.dosage[1].text == "give remaining 90% of dose over 1 hour"
    assert inst.experimental is True
    assert inst.id == "example-alteplase-dosing"
    assert inst.intent == "order"
    assert inst.kind == "MedicationRequest"
    assert inst.name == "Alteplase Dosing for Stroke"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == (
        "http://example.org/fhir/ActivityDefinition/example-" "alteplase-dosing"
    )


def test_activitydefinition_6(base_settings):
    """No. 6 tests collection for ActivityDefinition.
    Test File: activitydefinition-example-alteplase-dosing.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "activitydefinition-example-alteplase-dosing.json"
    )
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_6(inst2)


def impl_activitydefinition_7(inst):
    assert inst.approvalDate == fhirtypes.Date.validate("2017-03-01")
    assert inst.author[0].name == "Motive Medical Intelligence"
    assert inst.author[0].telecom[0].system == "phone"
    assert inst.author[0].telecom[0].use == "work"
    assert inst.author[0].telecom[0].value == "415-362-4007"
    assert inst.author[0].telecom[1].system == "email"
    assert inst.author[0].telecom[1].use == "work"
    assert inst.author[0].telecom[1].value == "info@motivemi.com"
    assert inst.code.coding[0].code == "306206005"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Referral to service (procedure)"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "415-362-4007"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "info@motivemi.com"
    assert inst.copyright == (
        "© Copyright 2016 Motive Medical Intelligence. All rights " "reserved."
    )
    assert inst.date == fhirtypes.DateTime.validate("2017-03-03T14:06:00Z")
    assert inst.description == (
        "refer to primary care mental-health integrated care program "
        "for evaluation and treatment of mental health conditions now"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate("2017-12-31")
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2017-03-01")
    assert inst.experimental is True
    assert inst.id == "referralPrimaryCareMentalHealth"
    assert inst.identifier[0].system == "http://motivemi.com/artifacts"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "referralPrimaryCareMentalHealth"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.kind == "ServiceRequest"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2017-03-01")
    assert inst.name == "ReferralPrimaryCareMentalHealth"
    assert inst.participant[0].type == "practitioner"
    assert inst.publisher == "Motive Medical Intelligence"
    assert inst.relatedArtifact[0].display == (
        "Practice Guideline for the Treatment of Patients with Major "
        "Depressive Disorder"
    )
    assert inst.relatedArtifact[0].document.url == (
        "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_"
        "guidelines/guidelines/mdd.pdf"
    )
    assert inst.relatedArtifact[0].type == "citation"
    assert inst.relatedArtifact[0].url == (
        "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_"
        "guidelines/guidelines/mdd.pdf"
    )
    assert inst.relatedArtifact[1].resource == (
        "http://example.org/fhir/ActivityDefinition/referralPrimaryCa"
        "reMentalHealth-initial"
    )
    assert inst.relatedArtifact[1].type == "predecessor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Referral to Primary Care Mental Health"
    assert inst.topic[0].text == "Mental Health Referral"
    assert inst.url == (
        "http://motivemi.com/artifacts/ActivityDefinition/referralPri"
        "maryCareMentalHealth"
    )
    assert inst.useContext[0].code.code == "age"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "D000328"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "Adult"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "https://meshb.nlm.nih.gov"
    )
    assert inst.useContext[1].code.code == "focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
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
    assert (
        inst.useContext[2].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
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
    assert (
        inst.useContext[3].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[3].valueCodeableConcept.coding[0].code == "225444004"
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].display
        == "At risk for suicide (finding)"
    )
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[4].code.code == "focus"
    assert (
        inst.useContext[4].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[4].valueCodeableConcept.coding[0].code == "306206005"
    assert (
        inst.useContext[4].valueCodeableConcept.coding[0].display
        == "Referral to service (procedure)"
    )
    assert (
        inst.useContext[4].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[5].code.code == "user"
    assert (
        inst.useContext[5].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[5].valueCodeableConcept.coding[0].code == "309343006"
    assert inst.useContext[5].valueCodeableConcept.coding[0].display == "Physician"
    assert (
        inst.useContext[5].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[6].code.code == "venue"
    assert (
        inst.useContext[6].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[6].valueCodeableConcept.coding[0].code == "440655000"
    assert (
        inst.useContext[6].valueCodeableConcept.coding[0].display
        == "Outpatient environment"
    )
    assert (
        inst.useContext[6].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "1.1.0"


def test_activitydefinition_7(base_settings):
    """No. 7 tests collection for ActivityDefinition.
    Test File: activitydefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "activitydefinition-example.json"
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_7(inst2)


def impl_activitydefinition_8(inst):
    assert inst.code.text == "Serum Dengue Virus IgM"
    assert inst.description == "Order Serum Dengue Virus IgM"
    assert inst.experimental is True
    assert inst.id == "serum-dengue-virus-igm"
    assert inst.kind == "ServiceRequest"
    assert inst.participant[0].type == "practitioner"
    assert inst.relatedArtifact[0].display == (
        "Explanation of diagnostic tests for Dengue virus and which "
        "to use based on the patient’s clinical and exposure history."
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://example.org/ActivityDefinition/serum-dengue-virus-igm"


def test_activitydefinition_8(base_settings):
    """No. 8 tests collection for ActivityDefinition.
    Test File: activitydefinition-order-serum-dengue-virus-igm.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "activitydefinition-order-serum-dengue-virus-igm.json"
    )
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_8(inst2)


def impl_activitydefinition_9(inst):
    assert inst.bodySite[0].coding[0].code == "17401000"
    assert inst.bodySite[0].coding[0].display == "Heart valve structure"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[0].code == "34068001"
    assert inst.code.coding[0].display == "Heart valve replacement"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.description == "Heart valve replacement"
    assert inst.experimental is True
    assert inst.id == "heart-valve-replacement"
    assert inst.kind == "ServiceRequest"
    assert inst.location.reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.participant[0].role.coding[0].code == "207RI0011X"
    assert inst.participant[0].role.coding[0].display == "Interventional Cardiology"
    assert (
        inst.participant[0].role.coding[0].system == "http://nucc.org/provider-taxonomy"
    )
    assert inst.participant[0].role.text == "Interventional Cardiology"
    assert inst.participant[0].type == "practitioner"
    assert (
        inst.purpose == "Describes the proposal to perform a Heart Valve replacement."
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.topic[0].coding[0].code == "34068001"
    assert inst.topic[0].coding[0].display == "Heart valve replacement"
    assert inst.topic[0].coding[0].system == "http://snomed.info/sct"
    assert inst.useContext[0].code.code == "age"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "D000328"
    assert inst.useContext[0].valueCodeableConcept.coding[0].display == "Adult"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "https://meshb.nlm.nih.gov"
    )
    assert inst.useContext[1].code.code == "user"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "309343006"
    assert inst.useContext[1].valueCodeableConcept.coding[0].display == "Physician"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )


def test_activitydefinition_9(base_settings):
    """No. 9 tests collection for ActivityDefinition.
    Test File: activitydefinition-servicerequest-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "activitydefinition-servicerequest-example.json"
    )
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_9(inst2)


def impl_activitydefinition_10(inst):
    assert inst.code.coding[0].code == "BlueTubes"
    assert inst.code.coding[0].display == "Blood collect tubes blue cap"
    assert inst.description == "10 Blood collect tubes blue cap"
    assert inst.experimental is True
    assert inst.id == "blood-tubes-supply"
    assert inst.kind == "SupplyRequest"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.purpose == (
        "Describes a request for 10 Blood collection tubes with blue " "caps."
    )
    assert float(inst.quantity.value) == float(10)
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.transform == "http://example.org/fhir/StructureMap/supplyrequest-transform"
    )


def test_activitydefinition_10(base_settings):
    """No. 10 tests collection for ActivityDefinition.
    Test File: activitydefinition-supplyrequest-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "activitydefinition-supplyrequest-example.json"
    )
    inst = activitydefinition.ActivityDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActivityDefinition" == inst.resource_type

    impl_activitydefinition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActivityDefinition" == data["resourceType"]

    inst2 = activitydefinition.ActivityDefinition(**data)
    impl_activitydefinition_10(inst2)
