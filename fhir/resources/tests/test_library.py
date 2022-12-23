# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Library
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import library


def impl_library_1(inst):
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/xml"
    assert inst.content[0].url == "elm/OMTK-modelinfo-0.1.0.xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.date == fhirtypes.DateTime.validate("2017-05-05")
    assert inst.description == (
        "Opioid Management Terminology Knowledge Base Model "
        "Definition for use in implementing CDC Opioid Prescribing "
        "Guidelines."
    )
    assert inst.experimental is True
    assert inst.id == "omtk-modelinfo"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OMTKModelInfo"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
        "This library defines the Opioid Management Terminology " "Knowledge Base model"
    )
    assert inst.status == "active"
    assert inst.title == "OMTK Model Info"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "model-definition"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used to resolve data elements in the Opioid "
        "Management Terminology Knowledge Base model"
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Medication requested (situation)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Chronic pain (finding)"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "0.1.0"


def test_library_1(base_settings):
    """No. 1 tests collection for Library.
    Test File: library-omtk-modelinfo.json
    """
    filename = base_settings["unittest_data_dir"] / "library-omtk-modelinfo.json"
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
    assert inst.content[0].contentType == "text/cql"
    assert inst.content[0].url == "library-hiv-indicators-content.cql"
    assert inst.content[1].contentType == "application/elm+xml"
    assert inst.date == fhirtypes.DateTime.validate("2018-08-03")
    assert inst.description == "HIV Indicators Reporting Example"
    assert inst.experimental is True
    assert inst.id == "hiv-indicators"
    assert inst.identifier[0].system == "http://ohie.org/Library/"
    assert inst.identifier[0].value == "hiv-indicators"
    assert (
        inst.relatedArtifact[0].document.url
        == "http://wiki.ihe.net/index.php/Aggregate_Data_Exchange_-_HIV"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert (
        inst.relatedArtifact[0].url
        == "http://wiki.ihe.net/index.php/Aggregate_Data_Exchange_-_HIV"
    )
    assert inst.status == "draft"
    assert inst.title == "HIV Indicators"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.url == "http://ohie.org/Library/hiv-indicators"
    assert inst.version == "0.0.0"


def test_library_2(base_settings):
    """No. 2 tests collection for Library.
    Test File: library-hiv-indicators.json
    """
    filename = base_settings["unittest_data_dir"] / "library-hiv-indicators.json"
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
    assert inst.content[0].contentType == "application/xml"
    assert inst.content[0].url == "http://cqlrepository.org/quick-modelinfo.xml"
    assert inst.date == fhirtypes.DateTime.validate("2016-07-08")
    assert inst.description == "Model definition for the QUICK Logical Model"
    assert inst.experimental is True
    assert inst.id == "library-quick-model-definition"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "QUICK"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "QUICK Model Definition"
    assert inst.topic[0].text == "QUICK"
    assert inst.type.coding[0].code == "model-definition"
    assert inst.version == "1.0.0"


def test_library_3(base_settings):
    """No. 3 tests collection for Library.
    Test File: library-quick-model-definition.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-quick-model-definition.json"
    )
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
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.dataRequirement[0].codeFilter[0].path == "medicationCodeableConcept"
    assert (
        inst.dataRequirement[0].codeFilter[0].valueSet
        == "http://example.org/fhir/ValueSet/benzodiazepines"
    )
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.dataRequirement[1].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[1].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-abused-in-" "ambulatory-care"
    )
    assert inst.dataRequirement[1].type == "MedicationRequest"
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.description == (
        "Opioid decision support logic to avoid prescribing opioid "
        "pain medication and benzodiazepines concurrently whenever "
        "possible."
    )
    assert inst.experimental is False
    assert inst.id == "opioidcds-recommendation-11"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_REC_11"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
        "The purpose of this library is to determine whether opioid "
        "pain medication and benzodiazepines have been prescribed "
        "concurrently."
    )
    assert (
        inst.relatedArtifact[0].display
        == "CDC guideline for prescribing opioids for chronic pain"
    )
    assert inst.relatedArtifact[0].document.url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[0].url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Library/opioidcds-common"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.title == "Opioid CDS Logic for recommendation #11"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used to notify the prescriber/user to avoid "
        "prescribing opioid pain medication and benzodiazepines "
        "concurrently."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Medication requested (situation)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Chronic pain (finding)"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "0.1.0"


def test_library_4(base_settings):
    """No. 4 tests collection for Library.
    Test File: library-opioidcds-recommendation-11.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-11.json"
    )
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
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.dataRequirement[0].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[0].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-indicating-end-of-" "life"
    )
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.dataRequirement[1].codeFilter[0].path == "code"
    assert inst.dataRequirement[1].type == "Procedure"
    assert inst.dataRequirement[2].codeFilter[0].path == "code"
    assert inst.dataRequirement[2].type == "Procedure"
    assert inst.dataRequirement[3].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[3].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-abused-in-" "ambulatory-care"
    )
    assert inst.dataRequirement[3].type == "MedicationRequest"
    assert inst.dataRequirement[4].type == "Encounter"
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.experimental is False
    assert inst.id == "opioidcds-recommendation-07"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_REC_07"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
        "The purpose of this library is to determine whether the "
        "patient has been evaluated for benefits and harms within 1 "
        "to 4 weeks of starting opioid therapy and every 3 months or "
        "more subsequently."
    )
    assert (
        inst.relatedArtifact[0].display
        == "CDC guideline for prescribing opioids for chronic pain"
    )
    assert inst.relatedArtifact[0].document.url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[0].url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Library/opioidcds-common"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.title == "Opioid CDS Logic for recommendation #7"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used to notify the prescriber/user whether "
        "an evaluation for benefits and harms associated with opioid "
        "therapy is recommended for the patient."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Medication requested (situation)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Chronic pain (finding)"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "0.1.0"


def test_library_5(base_settings):
    """No. 5 tests collection for Library.
    Test File: library-opioidcds-recommendation-07.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-07.json"
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
    assert inst.approvalDate == fhirtypes.Date.validate("2021-03-02")
    assert inst.content[0].contentType == "application/xml"
    assert inst.content[0].url == "http://cqlrepository.org/fhirmodel-modelinfo.xml"
    assert inst.date == fhirtypes.DateTime.validate("2016-07-08")
    assert inst.description == "Model definition for the FHIR Model"
    assert inst.experimental is False
    assert inst.id == "FHIR-ModelInfo"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "FHIR"
    assert inst.lastReviewDate == fhirtypes.Date.validate("2021-03-02")
    assert inst.name == "FHIR"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Model Definition"
    assert inst.topic[0].text == "FHIR"
    assert inst.type.coding[0].code == "model-definition"
    assert inst.url == "http://hl7.org/fhir/Library/FHIR-ModelInfo"
    assert inst.version == "4.3.0"


def test_library_6(base_settings):
    """No. 6 tests collection for Library.
    Test File: library-fhir-model-definition.json
    """
    filename = base_settings["unittest_data_dir"] / "library-fhir-model-definition.json"
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
    assert inst.content[0].title == "FHIR Helpers"
    assert inst.content[0].url == "library-fhir-helpers-content.cql"
    assert inst.date == fhirtypes.DateTime.validate("2016-11-14")
    assert inst.description == "FHIR Helpers"
    assert inst.experimental is True
    assert inst.id == "library-fhir-helpers-predecessor"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "FHIRHelpers"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.relatedArtifact[0].resource
        == "http://example.org/fhir/Library/fhir-model-definition"
    )
    assert inst.relatedArtifact[0].type == "depends-on"
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Library/library-fhir-helpers"
    )
    assert inst.relatedArtifact[1].type == "successor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR Helpers"
    assert inst.topic[0].text == "FHIR Helpers"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.version == "1.6"


def test_library_7(base_settings):
    """No. 7 tests collection for Library.
    Test File: library-predecessor-example.json
    """
    filename = base_settings["unittest_data_dir"] / "library-predecessor-example.json"
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
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.dataRequirement[0].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[0].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-indicating-end-of-" "life"
    )
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.dataRequirement[1].codeFilter[0].path == "medicationCodeableConcept"
    assert inst.dataRequirement[1].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/opioids-abused-in-" "ambulatory-care"
    )
    assert inst.dataRequirement[1].type == "MedicationRequest"
    assert inst.dataRequirement[2].codeFilter[0].path == "combo-code"
    assert inst.dataRequirement[2].codeFilter[0].valueSet == (
        "http://example.org/fhir/ValueSet/illicit-drug-urine-" "screening"
    )
    assert inst.dataRequirement[2].type == "Observation"
    assert inst.dataRequirement[3].codeFilter[0].path == "combo-code"
    assert (
        inst.dataRequirement[3].codeFilter[0].valueSet
        == "http://example.org/fhir/ValueSet/opioid-urine-screening"
    )
    assert inst.dataRequirement[3].type == "Observation"
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.description == (
        "Opioid decision support logic to evaluate whether the "
        "patient has had a urine screening in the past 12 months and "
        "provide analysis."
    )
    assert inst.experimental is False
    assert inst.id == "opioidcds-recommendation-10"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_REC_10"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert (
        inst.relatedArtifact[0].display
        == "CDC guideline for prescribing opioids for chronic pain"
    )
    assert inst.relatedArtifact[0].document.url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[0].url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Library/opioidcds-common"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.status == "active"
    assert inst.title == "Opioid CDS Logic for recommendation #10"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is used to notify the prescriber/user whether "
        "the patient has had a urine screening in the past 12 months "
        "and to provide analysis if true."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Medication requested (situation)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Chronic pain (finding)"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "0.1.0"


def test_library_8(base_settings):
    """No. 8 tests collection for Library.
    Test File: library-opioidcds-recommendation-10.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-10.json"
    )
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
    assert inst.content[1].contentType == "application/elm+xml"
    assert inst.dataRequirement[0].type == "Patient"
    assert inst.dataRequirement[1].codeFilter[0].code[0].code == "diagnosis"
    assert inst.dataRequirement[1].codeFilter[0].path == "category"
    assert inst.dataRequirement[1].codeFilter[1].code[0].code == "confirmed"
    assert inst.dataRequirement[1].codeFilter[1].path == "clinicalStatus"
    assert inst.dataRequirement[1].codeFilter[2].path == "code"
    assert (
        inst.dataRequirement[1].codeFilter[2].valueSet
        == "urn:oid:2.16.840.1.113883.3.464.1003.102.12.1011"
    )
    assert inst.dataRequirement[1].type == "Condition"
    assert inst.dataRequirement[2].codeFilter[0].code[0].code == "diagnosis"
    assert inst.dataRequirement[2].codeFilter[0].path == "category"
    assert inst.dataRequirement[2].codeFilter[1].code[0].code == "confirmed"
    assert inst.dataRequirement[2].codeFilter[1].path == "clinicalStatus"
    assert inst.dataRequirement[2].codeFilter[2].path == "code"
    assert (
        inst.dataRequirement[2].codeFilter[2].valueSet
        == "urn:oid:2.16.840.1.113883.3.464.1003.102.12.1012"
    )
    assert inst.dataRequirement[2].type == "Condition"
    assert inst.dataRequirement[3].codeFilter[0].code[0].code == "finished"
    assert inst.dataRequirement[3].codeFilter[0].path == "status"
    assert inst.dataRequirement[3].codeFilter[1].code[0].code == "ambulatory"
    assert inst.dataRequirement[3].codeFilter[1].path == "class"
    assert inst.dataRequirement[3].codeFilter[2].path == "type"
    assert (
        inst.dataRequirement[3].codeFilter[2].valueSet
        == "urn:oid:2.16.840.1.113883.3.464.1003.101.12.1061"
    )
    assert inst.dataRequirement[3].type == "Encounter"
    assert inst.dataRequirement[4].codeFilter[0].path == "diagnosis"
    assert (
        inst.dataRequirement[4].codeFilter[0].valueSet
        == "urn:oid:2.16.840.1.113883.3.464.1003.198.12.1012"
    )
    assert inst.dataRequirement[4].type == "DiagnosticReport"
    assert inst.dataRequirement[5].codeFilter[0].path == "code"
    assert (
        inst.dataRequirement[5].codeFilter[0].valueSet
        == "urn:oid:2.16.840.1.113883.3.464.1003.196.12.1001"
    )
    assert inst.dataRequirement[5].type == "Medication"
    assert inst.dataRequirement[6].codeFilter[0].code[0].code == "active"
    assert inst.dataRequirement[6].codeFilter[0].path == "status"
    assert inst.dataRequirement[6].codeFilter[1].path == "medication.code"
    assert (
        inst.dataRequirement[6].codeFilter[1].valueSet
        == "urn:oid:2.16.840.1.113883.3.464.1003.196.12.1001"
    )
    assert inst.dataRequirement[6].type == "MedicationRequest"
    assert inst.dataRequirement[7].codeFilter[0].code[0].code == "completed"
    assert inst.dataRequirement[7].codeFilter[0].path == "status"
    assert inst.dataRequirement[7].codeFilter[1].path == "medication.code"
    assert (
        inst.dataRequirement[7].codeFilter[1].valueSet
        == "urn:oid:2.16.840.1.113883.3.464.1003.196.12.1001"
    )
    assert inst.dataRequirement[7].type == "MedicationStatement"
    assert inst.date == fhirtypes.DateTime.validate("2015-07-22")
    assert inst.description == (
        "Logic for CMS 146: Appropriate Testing for Children with " "Pharyngitis"
    )
    assert inst.experimental is True
    assert inst.id == "library-cms146-example"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "CMS146"
    assert inst.name == "CMS146"
    assert (
        inst.relatedArtifact[0].resource
        == "http://hl7.org/fhir/Library/library-quick-model-definition"
    )
    assert inst.relatedArtifact[0].type == "depends-on"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CMS146: Appropriate Testing for Children with Pharyngitis"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.url == "http://hl7.org/fhir/Library/library-cms146-example"
    assert inst.version == "2.0.0"


def test_library_9(base_settings):
    """No. 9 tests collection for Library.
    Test File: library-cms146-example.json
    """
    filename = base_settings["unittest_data_dir"] / "library-cms146-example.json"
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
    assert inst.author[0].name == "Kensaku Kawamoto, MD, PhD, MHS"
    assert inst.author[1].name == "Bryn Rhodes"
    assert inst.author[2].name == "Floyd Eisenberg, MD, MPH"
    assert inst.author[3].name == "Robert McClure, MD, MPH"
    assert inst.content[0].contentType == "application/elm+xml"
    assert inst.copyright == "© CDC 2016+."
    assert inst.dataRequirement[0].codeFilter[0].code[0].code == "active"
    assert inst.dataRequirement[0].codeFilter[0].path == "status"
    assert inst.dataRequirement[0].codeFilter[1].code[0].code == "outpatient"
    assert inst.dataRequirement[0].codeFilter[1].code[0].system == (
        "http://terminology.hl7.org/CodeSystem/medicationrequest-" "category"
    )
    assert inst.dataRequirement[0].codeFilter[1].path == "category"
    assert inst.dataRequirement[0].id == "medications"
    assert inst.dataRequirement[0].type == "MedicationRequest"
    assert inst.date == fhirtypes.DateTime.validate("2018-03-25T13:49:09-06:00")
    assert inst.description == (
        "Opioid Decision Support Logic for use in implementing CDC "
        "Opioid Prescribing Guidelines."
    )
    assert inst.experimental is False
    assert inst.id == "opioidcds-recommendation-05"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "OpioidCDS_REC_05"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Centers for Disease Control and Prevention (CDC)"
    assert inst.purpose == (
        "This library works in concert with the OMTK logic library to"
        " provide decision support for Morphine Milligram Equivalence"
        " calculations and dynamic value resolution."
    )
    assert (
        inst.relatedArtifact[0].display
        == "CDC guideline for prescribing opioids for chronic pain"
    )
    assert inst.relatedArtifact[0].document.url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert inst.relatedArtifact[0].type == "documentation"
    assert inst.relatedArtifact[0].url == (
        "https://guidelines.gov/summaries/summary/50153/cdc-"
        "guideline-for-prescribing-opioids-for-chronic-pain---united-"
        "states-2016#420"
    )
    assert (
        inst.relatedArtifact[1].resource
        == "http://example.org/fhir/Library/opioidcds-common"
    )
    assert inst.relatedArtifact[1].type == "depends-on"
    assert inst.relatedArtifact[2].display == "MME Conversion Tables"
    assert inst.relatedArtifact[2].document.url == (
        "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily" "_dose-a.pdf"
    )
    assert inst.relatedArtifact[2].type == "documentation"
    assert inst.relatedArtifact[2].url == (
        "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily" "_dose-a.pdf"
    )
    assert inst.status == "active"
    assert inst.title == "Opioid CDS Logic for recommendation #5"
    assert inst.topic[0].text == "Opioid Prescribing"
    assert inst.type.coding[0].code == "logic-library"
    assert inst.type.coding[0].display == "Logic Library"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/library-type"
    )
    assert inst.usage == (
        "This library is to notify the prescriber/user whether the "
        "current prescription exceeds the recommended MME."
    )
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.display == "Clinical Focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "182888003"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Medication requested (situation)"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.useContext[1].code.code == "focus"
    assert inst.useContext[1].code.display == "Clinical Focus"
    assert (
        inst.useContext[1].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[1].valueCodeableConcept.coding[0].code == "82423001"
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].display
        == "Chronic pain (finding)"
    )
    assert (
        inst.useContext[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.version == "0.1.0"


def test_library_10(base_settings):
    """No. 10 tests collection for Library.
    Test File: library-opioidcds-recommendation-05.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "library-opioidcds-recommendation-05.json"
    )
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
