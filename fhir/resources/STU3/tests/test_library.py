# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Library
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import library


def impl_library_1(inst):
    assert inst.content[0].contentType == "application/xml"
    assert inst.content[0].url == "http://cqlrepository.org/quick-modelinfo.xml"
    assert inst.date == fhirtypes.DateTime.validate("2016-07-08")
    assert inst.description == "Model definition for the QUICK Logical Model"
    assert inst.id == "library-quick-model-definition"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "QUICK"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "QUICK Model Definition"
    assert inst.topic[0].text == "QUICK"
    assert inst.type.coding[0].code == "model-definition"
    assert inst.version == "1.0.0"


def test_library_1(base_settings):
    """No. 1 tests collection for Library.
    Test File: library-quick-model-definition.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-quick-model-definition.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_1(inst2)


def impl_library_2(inst):
    assert inst.content[0].contentType == "application/xml"
    assert inst.content[0].url == "http://cqlrepository.org/fhirmodel-modelinfo.xml"
    assert inst.date == fhirtypes.DateTime.validate("2016-07-08")
    assert inst.description == "Model definition for the FHIR Model"
    assert inst.id == "library-fhir-model-definition"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "FHIR"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Model Definition"
    assert inst.topic[0].text == "FHIR"
    assert inst.type.coding[0].code == "model-definition"
    assert inst.version == "3.0.1"


def test_library_2(base_settings):
    """No. 2 tests collection for Library.
    Test File: library-fhir-model-definition.json
    """
    filename = base_settings["unittest_data_dir"] / "library-fhir-model-definition.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_2(inst2)


def impl_library_3(inst):
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].title == "FHIR Helpers"
    assert inst.content[0].url == "library-fhir-helpers-content.cql"
    assert inst.date == fhirtypes.DateTime.validate("2016-11-14")
    assert inst.description == "FHIR Helpers"
    assert inst.experimental is True
    assert inst.id == "library-fhir-helpers-predecessor"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "FHIRHelpers"
    assert inst.relatedArtifact[0].resource.reference == "Library/fhir-model-definition"
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.relatedArtifact[1].resource.reference == "Library/library-fhir-helpers"
    assert inst.relatedArtifact[1].type == "successor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Helpers"
    assert inst.topic[0].text == "FHIR Helpers"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "1.6"


def test_library_3(base_settings):
    """No. 3 tests collection for Library.
    Test File: library-predecessor-example.json
    """
    filename = base_settings["unittest_data_dir"] / "library-predecessor-example.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_3(inst2)


def impl_library_4(inst):
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].url == "library-cms146-example-content.cql"
    assert inst.dataRequirement[0].type == "Patient"
    assert inst.dataRequirement[1].codeFilter[0].path == "category"
    assert inst.dataRequirement[1].codeFilter[0].valueCode[0] == "diagnosis"
    assert inst.dataRequirement[1].codeFilter[1].path == "clinicalStatus"
    assert inst.dataRequirement[1].codeFilter[1].valueCode[0] == "confirmed"
    assert inst.dataRequirement[1].codeFilter[2].path == "code"
    assert (
        inst.dataRequirement[1].codeFilter[2].valueSetString
        == "2.16.840.1.113883.3.464.1003.102.12.1011"
    )
    assert inst.dataRequirement[1].type == "Condition"
    assert inst.dataRequirement[2].codeFilter[0].path == "category"
    assert inst.dataRequirement[2].codeFilter[0].valueCode[0] == "diagnosis"
    assert inst.dataRequirement[2].codeFilter[1].path == "clinicalStatus"
    assert inst.dataRequirement[2].codeFilter[1].valueCode[0] == "confirmed"
    assert inst.dataRequirement[2].codeFilter[2].path == "code"
    assert (
        inst.dataRequirement[2].codeFilter[2].valueSetString
        == "2.16.840.1.113883.3.464.1003.102.12.1012"
    )
    assert inst.dataRequirement[2].type == "Condition"
    assert inst.dataRequirement[3].codeFilter[0].path == "status"
    assert inst.dataRequirement[3].codeFilter[0].valueCode[0] == "finished"
    assert inst.dataRequirement[3].codeFilter[1].path == "class"
    assert inst.dataRequirement[3].codeFilter[1].valueCode[0] == "ambulatory"
    assert inst.dataRequirement[3].codeFilter[2].path == "type"
    assert (
        inst.dataRequirement[3].codeFilter[2].valueSetString
        == "2.16.840.1.113883.3.464.1003.101.12.1061"
    )
    assert inst.dataRequirement[3].type == "Encounter"
    assert inst.dataRequirement[4].codeFilter[0].path == "diagnosis"
    assert (
        inst.dataRequirement[4].codeFilter[0].valueSetString
        == "2.16.840.1.113883.3.464.1003.198.12.1012"
    )
    assert inst.dataRequirement[4].type == "DiagnosticReport"
    assert inst.dataRequirement[5].codeFilter[0].path == "code"
    assert (
        inst.dataRequirement[5].codeFilter[0].valueSetString
        == "2.16.840.1.113883.3.464.1003.196.12.1001"
    )
    assert inst.dataRequirement[5].type == "Medication"
    assert inst.dataRequirement[6].codeFilter[0].path == "status"
    assert inst.dataRequirement[6].codeFilter[0].valueCode[0] == "active"
    assert inst.dataRequirement[6].codeFilter[1].path == "medication.code"
    assert (
        inst.dataRequirement[6].codeFilter[1].valueSetString
        == "2.16.840.1.113883.3.464.1003.196.12.1001"
    )
    assert inst.dataRequirement[6].type == "MedicationRequest"
    assert inst.dataRequirement[7].codeFilter[0].path == "status"
    assert inst.dataRequirement[7].codeFilter[0].valueCode[0] == "completed"
    assert inst.dataRequirement[7].codeFilter[1].path == "medication.code"
    assert (
        inst.dataRequirement[7].codeFilter[1].valueSetString
        == "2.16.840.1.113883.3.464.1003.196.12.1001"
    )
    assert inst.dataRequirement[7].type == "MedicationStatement"
    assert inst.date == fhirtypes.DateTime.validate("2015-07-22")
    assert inst.description == (
        "Logic for CMS 146: Appropriate Testing for Children with " "Pharyngitis"
    )
    assert inst.id == "library-cms146-example"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "CMS146"
    assert (
        inst.relatedArtifact[0].resource.reference
        == "Library/library-quick-model-definition"
    )
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Appropriate Testing for Children with Pharyngitis"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "2.0.0"


def test_library_4(base_settings):
    """No. 4 tests collection for Library.
    Test File: library-cms146-example.json
    """
    filename = base_settings["unittest_data_dir"] / "library-cms146-example.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_4(inst2)


def impl_library_5(inst):
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].url == "http://cqlrepository.org/CMS9v4_CQM.cql"
    assert inst.dataRequirement[0].codeFilter[0].path == "code"
    assert inst.dataRequirement[0].codeFilter[0].valueSetString == "Single Live Birth"
    assert inst.dataRequirement[0].type == "Condition"
    assert inst.date == fhirtypes.DateTime.validate("2016-03-08")
    assert inst.description == (
        "Quality measure logic for measuring outcomes for exclusive "
        "breastmilk feeding of newborns"
    )
    assert inst.experimental is True
    assert inst.id == "library-exclusive-breastfeeding-cqm-logic"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "Exclusive_Breastfeeding_CQM_Logic"
    assert (
        inst.relatedArtifact[0].resource.reference
        == "Library/library-quick-model-definition"
    )
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding CQM Logic"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "1.0.0"


def test_library_5(base_settings):
    """No. 5 tests collection for Library.
    Test File: library-exclusive-breastfeeding-cqm-logic.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "library-exclusive-breastfeeding-cqm-logic.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_5(inst2)


def impl_library_6(inst):
    assert inst.approvalDate == fhirtypes.Date.validate("2016-03-12")
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "415-362-4007"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "info@motivemi.com"
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].url == "library-mmi-suiciderisk-orderset-logic-content.cql"
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
    assert inst.dataRequirement[0].codeFilter[0].path == "code"
    assert (
        inst.dataRequirement[0].codeFilter[0].valueSetString
        == "Suicide Risk Assessment"
    )
    assert inst.dataRequirement[0].type == "RiskAssessment"
    assert inst.date == fhirtypes.DateTime.validate("2015-07-22")
    assert inst.description == "Logic for Suicide Risk Order Sets"
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate("2017-12-31")
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2016-01-01")
    assert inst.experimental is True
    assert inst.id == "suiciderisk-orderset-logic"
    assert inst.identifier[0].system == "http://motivemi.com/artifacts"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "mmi:suiciderisk-orderset-logic"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2016-08-15")
    assert inst.name == "SuicideRiskOrderSetLogic"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "Patient"
    assert inst.parameter[0].type == "Patient"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "Encounter"
    assert inst.parameter[1].type == "Encounter"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "Practitioner"
    assert inst.parameter[2].type == "Practitioner"
    assert inst.parameter[2].use == "in"
    assert inst.publisher == "Motive Medical Intelligence"
    assert inst.relatedArtifact[0].display == (
        "Practice Guideline for the Treatment of Patients with Major "
        "Depressive Disorder"
    )
    assert inst.relatedArtifact[0].type == "citation"
    assert inst.relatedArtifact[0].url == (
        "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_"
        "guidelines/guidelines/mdd.pdf"
    )
    assert (
        inst.relatedArtifact[1].resource.reference
        == "Library/library-fhir-model-definition"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.relatedArtifact[2].resource.display == "FHIRHelpers"
    assert inst.relatedArtifact[2].resource.reference == "Library/library-fhir-helpers"
    assert inst.relatedArtifact[2].type == "depends-on"
    assert (
        inst.relatedArtifact[3].resource.reference
        == "http://nucc.org/provider-taxonomy"
    )
    assert inst.relatedArtifact[3].type == "depends-on"
    assert inst.relatedArtifact[4].resource.display == "Suicide Risk Assessment"
    assert inst.relatedArtifact[4].resource.reference == "ValueSet/1.2.3.4.5"
    assert inst.relatedArtifact[4].type == "depends-on"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Suicide Risk Order Set Logic"
    assert inst.topic[0].text == "Suicide Risk Order Set Logic"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.url == (
        "http://motivemi.com/artifacts/Library/suiciderisk-orderset-" "logic"
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
    assert inst.useContext[3].valueCodeableConcept.coding[0].code == "225444004"
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].display
        == "At risk for suicide (finding)"
    )
    assert (
        inst.useContext[3].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[4].code.code == "user"
    assert inst.useContext[4].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[4].valueCodeableConcept.coding[0].code == "309343006"
    assert inst.useContext[4].valueCodeableConcept.coding[0].display == "Physician"
    assert (
        inst.useContext[4].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[5].code.code == "venue"
    assert inst.useContext[5].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[5].valueCodeableConcept.coding[0].code == "440655000"
    assert (
        inst.useContext[5].valueCodeableConcept.coding[0].display
        == "Outpatient environment"
    )
    assert (
        inst.useContext[5].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "1.0.0"


def test_library_6(base_settings):
    """No. 6 tests collection for Library.
    Test File: library-mmi-suiciderisk-orderset-logic.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "library-mmi-suiciderisk-orderset-logic.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_6(inst2)


def impl_library_7(inst):
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].url == "library-example-content.cql"
    assert inst.dataRequirement[0].codeFilter[0].path == "code"
    assert (
        inst.dataRequirement[0].codeFilter[0].valueSetString
        == "Other Female Reproductive Conditions"
    )
    assert inst.dataRequirement[0].type == "Condition"
    assert inst.date == fhirtypes.DateTime.validate("2015-07-22")
    assert (
        inst.description
        == "Common Logic for adherence to Chlamydia Screening guidelines"
    )
    assert inst.id == "example"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "ChalmydiaScreening_Common"
    assert (
        inst.relatedArtifact[0].resource.reference
        == "Library/library-quick-model-definition"
    )
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Chlamydia Screening Common Library"
    assert inst.topic[0].text == "Chlamydia Screening"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "2.0.0"


def test_library_7(base_settings):
    """No. 7 tests collection for Library.
    Test File: library-example.json
    """
    filename = base_settings["unittest_data_dir"] / "library-example.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_7(inst2)


def impl_library_8(inst):
    assert inst.date == fhirtypes.DateTime.validate("2017-03-10")
    assert inst.description == (
        "Artifacts required for implementation of Zika Virus " "Management"
    )
    assert inst.id == "composition-example"
    assert inst.identifier[0].system == "http://example.org"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "Zika Artifacts"
    assert (
        inst.relatedArtifact[0].resource.reference
        == "ActivityDefinition/administer-zika-virus-exposure-assessment"
    )
    assert inst.relatedArtifact[0].type == "composed-of"
    assert (
        inst.relatedArtifact[1].resource.reference
        == "ActivityDefinition/order-serum-zika-dengue-virus-igm"
    )
    assert inst.relatedArtifact[1].type == "composed-of"
    assert (
        inst.relatedArtifact[2].resource.reference
        == "ActivityDefinition/provide-mosquito-prevention-advice"
    )
    assert inst.relatedArtifact[2].type == "composed-of"
    assert (
        inst.relatedArtifact[3].resource.reference
        == "Library/zika-virus-intervention-logic"
    )
    assert inst.relatedArtifact[3].type == "composed-of"
    assert (
        inst.relatedArtifact[4].resource.reference
        == "PlanDefinition/zika-virus-intervention"
    )
    assert inst.relatedArtifact[4].type == "composed-of"
    assert (
        inst.relatedArtifact[5].resource.reference
        == "Questionnaire/zika-virus-exposure-assessment"
    )
    assert inst.relatedArtifact[5].type == "composed-of"
    assert inst.relatedArtifact[6].type == "derived-from"
    assert inst.relatedArtifact[6].url == (
        "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm" "6539e1_w"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Zika Artifacts"
    assert inst.topic[0].text == "Zika Virus Management"
    assert inst.type.coding[0].code == "asset-collection"
    assert inst.version == "1.0.0"


def test_library_8(base_settings):
    """No. 8 tests collection for Library.
    Test File: library-composition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "library-composition-example.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_8(inst2)


def impl_library_9(inst):
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].url == "http://cqlrepository.org/CMS9v4_CDS.cql"
    assert inst.dataRequirement[0].codeFilter[0].path == "code"
    assert inst.dataRequirement[0].codeFilter[0].valueSetString == "Single Live Birth"
    assert inst.dataRequirement[0].type == "Condition"
    assert inst.date == fhirtypes.DateTime.validate("2016-03-08")
    assert inst.description == (
        "Decision support logic for improving outcomes for exclusive "
        "breastmilk feeding of newborns"
    )
    assert inst.experimental is True
    assert inst.id == "library-exclusive-breastfeeding-cds-logic"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "Exclusive_Breastfeeding_CDS_Logic"
    assert (
        inst.relatedArtifact[0].resource.reference
        == "Library/library-quick-model-definition"
    )
    assert inst.relatedArtifact[0].type == "depends-on"
    assert (
        inst.relatedArtifact[1].resource.reference
        == "Measure/measure-exclusive-breastfeeding"
    )
    assert inst.relatedArtifact[1].type == "derived-from"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Exclusive Breastfeeding CDS Logic"
    assert inst.topic[0].text == "Exclusive Breastfeeding"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "1.0.0"


def test_library_9(base_settings):
    """No. 9 tests collection for Library.
    Test File: library-exclusive-breastfeeding-cds-logic.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "library-exclusive-breastfeeding-cds-logic.json"
    )
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_9(inst2)


def impl_library_10(inst):
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].title == "FHIR Helpers"
    assert inst.content[0].url == "library-fhir-helpers-content.cql"
    assert inst.date == fhirtypes.DateTime.validate("2016-11-14")
    assert inst.description == "FHIR Helpers"
    assert inst.experimental is True
    assert inst.id == "library-fhir-helpers"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "FHIRHelpers"
    assert inst.relatedArtifact[0].resource.reference == "Library/fhir-model-definition"
    assert inst.relatedArtifact[0].type == "depends-on"
    assert (
        inst.relatedArtifact[1].resource.reference == "library-fhir-helpers-predecessor"
    )
    assert inst.relatedArtifact[1].type == "predecessor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Helpers"
    assert inst.topic[0].text == "FHIR Helpers"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "1.8"


def test_library_10(base_settings):
    """No. 10 tests collection for Library.
    Test File: library-fhir-helpers.json
    """
    filename = base_settings["unittest_data_dir"] / "library-fhir-helpers.json"
    inst = library.Library.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Library" == inst.resource_type

    impl_library_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Library" == data["resourceType"]

    inst2 = library.Library(**data)
    impl_library_10(inst2)
