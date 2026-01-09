# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import researchstudy
from .conftest import ExternalValidatorModel


def impl_researchstudy_1(inst):
    assert inst.associatedParty[0].classifier[0].text == "INDUSTRY"
    assert inst.associatedParty[0].name == "Alebund Pharmaceuticals"
    assert inst.associatedParty[0].role.coding[0].code == "sponsor"
    assert inst.associatedParty[0].role.coding[0].display == "Sponsor"
    assert (
        inst.associatedParty[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/research-study-party-role"}
        ).valueUri
    )
    assert inst.associatedParty[1].classifier[0].text == "INDUSTRY"
    assert inst.associatedParty[1].name == "Alebund Pty Ltd"
    assert inst.associatedParty[1].role.coding[0].code == "lead-sponsor"
    assert inst.associatedParty[1].role.coding[0].display == "Lead Sponsor"
    assert (
        inst.associatedParty[1].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/research-study-party-role"}
        ).valueUri
    )
    assert inst.associatedParty[2].classifier[0].text == "Contact"
    assert inst.associatedParty[2].name == "Zhen LIU"
    assert inst.associatedParty[2].party.reference == "#NCT05503693-CentralContact-0"
    assert (
        inst.associatedParty[2].party.type
        == ExternalValidatorModel.model_validate({"valueUri": "Practitioner"}).valueUri
    )
    assert inst.associatedParty[2].role.coding[0].code == "recruitment-contact"
    assert inst.associatedParty[2].role.coding[0].display == "Recruitment Contact"
    assert (
        inst.associatedParty[2].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/research-study-party-role"}
        ).valueUri
    )
    assert inst.associatedParty[3].name == "Sam Francis, Doctor"
    assert inst.associatedParty[3].party.display == "Nucleus Network"
    assert inst.associatedParty[3].role.text == "Principal Investigator"
    assert inst.classifier[0].text == "Has Results: False"
    assert inst.classifier[1].text == "Oversight Classifier: oversightHasDmc Yes"
    assert inst.classifier[2].text == "Oversight Classifier: isFdaRegulatedDrug No"
    assert inst.classifier[3].text == "Oversight Classifier: isFdaRegulatedDevice No"
    assert inst.comparisonGroup[0].description == "AP303"
    assert inst.comparisonGroup[0].intendedExposure[0].display == "Drug: AP303 50 μg"
    assert (
        inst.comparisonGroup[0].intendedExposure[0].reference
        == "#NCT05503693-drug------ap303-50-g"
    )
    assert (
        inst.comparisonGroup[0].intendedExposure[0].type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.comparisonGroup[0].intendedExposure[1].display == "Drug: AP303 150 μg"
    assert (
        inst.comparisonGroup[0].intendedExposure[1].reference
        == "#NCT05503693-drug------ap303-150-g"
    )
    assert (
        inst.comparisonGroup[0].intendedExposure[1].type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.comparisonGroup[0].intendedExposure[2].display == "Drug: AP303 300 μg"
    assert (
        inst.comparisonGroup[0].intendedExposure[2].reference
        == "#NCT05503693-drug------ap303-300-g"
    )
    assert (
        inst.comparisonGroup[0].intendedExposure[2].type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.comparisonGroup[0].intendedExposure[3].display == "Drug: AP303 600 μg"
    assert (
        inst.comparisonGroup[0].intendedExposure[3].reference
        == "#NCT05503693-drug------ap303-600-g"
    )
    assert (
        inst.comparisonGroup[0].intendedExposure[3].type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.comparisonGroup[0].linkId == "ap303"
    assert inst.comparisonGroup[0].name == "AP303"
    assert inst.comparisonGroup[0].type.text == "Experimental"
    assert inst.comparisonGroup[1].description == "Placebo"
    assert inst.comparisonGroup[1].intendedExposure[0].display == "Drug: Placebo 50 μg"
    assert (
        inst.comparisonGroup[1].intendedExposure[0].reference
        == "#NCT05503693-drug------placebo-50-g"
    )
    assert (
        inst.comparisonGroup[1].intendedExposure[0].type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.comparisonGroup[1].intendedExposure[1].display == "Drug: Placebo 150 μg"
    assert (
        inst.comparisonGroup[1].intendedExposure[1].reference
        == "#NCT05503693-drug------placebo-150-g"
    )
    assert (
        inst.comparisonGroup[1].intendedExposure[1].type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.comparisonGroup[1].intendedExposure[2].display == "Drug: Placebo 300 μg"
    assert (
        inst.comparisonGroup[1].intendedExposure[2].reference
        == "#NCT05503693-drug------placebo-300-g"
    )
    assert (
        inst.comparisonGroup[1].intendedExposure[2].type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.comparisonGroup[1].intendedExposure[3].display == "Drug: Placebo 600 μg"
    assert (
        inst.comparisonGroup[1].intendedExposure[3].reference
        == "#NCT05503693-drug------placebo-600-g"
    )
    assert (
        inst.comparisonGroup[1].intendedExposure[3].type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.comparisonGroup[1].linkId == "placebo"
    assert inst.comparisonGroup[1].name == "Placebo"
    assert inst.comparisonGroup[1].type.text == "Placebo Comparator"
    assert inst.condition[0].text == "Healthy Subjects"
    assert inst.contained[0].id == "NCT05503693-drug------ap303-50-g"
    assert inst.contained[1].id == "NCT05503693-drug------ap303-150-g"
    assert inst.contained[2].id == "NCT05503693-drug------ap303-300-g"
    assert inst.contained[3].id == "NCT05503693-drug------ap303-600-g"
    assert inst.contained[4].id == "NCT05503693-drug------placebo-50-g"
    assert inst.contained[5].id == "NCT05503693-drug------placebo-150-g"
    assert inst.contained[6].id == "NCT05503693-drug------placebo-300-g"
    assert inst.contained[7].id == "NCT05503693-drug------placebo-600-g"
    assert inst.contained[8].id == "NCT05503693-CentralContact-0"
    assert inst.contained[9].id == "NCT05503693-Location-0-ResearchStudy"
    assert inst.id == "example-ctgov-study-record"
    assert inst.identifier[0].assigner.display == "Computable Publishing LLC"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net"}
        ).valueUri
    )
    assert inst.identifier[0].type.text == "FEvIR Object Identifier"
    assert inst.identifier[0].value == "112103"
    assert (
        inst.identifier[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://clinicaltrials.gov"}
        ).valueUri
    )
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "NCT05503693"
    assert inst.identifier[2].assigner.display == "Alebund Pharmaceuticals"
    assert inst.identifier[2].value == "AP303-PK-01"
    assert inst.keyword[0].text == (
        "Safety, Tolerability, Pharmacokinetics, AP303, Healthy " "Subjects"
    )
    assert inst.label[0].type.text == "Official Title"
    assert inst.name == "NCT05503693_FHIR_Transform"
    assert inst.outcomeMeasure[0].description == (
        "Incidence and severity of adverse events (AEs), laboratory, "
        "ECG, and vital sign changes"
    )
    assert (
        inst.outcomeMeasure[0].name
        == "Single Dose and Food Effect Safety Outcome Measures"
    )
    assert (
        inst.outcomeMeasure[0].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[0].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[0].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[0].reference.identifier.value
        == "NCT05503693-primaryOutcome-0"
    )
    assert (
        inst.outcomeMeasure[0].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[0].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[0].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[0].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.outcomeMeasure[1].description == (
        "Incidence and severity of AEs, laboratory, ECG, and vital " "sign changes."
    )
    assert inst.outcomeMeasure[1].name == "Multiple Dose Safety Outcome Measures"
    assert (
        inst.outcomeMeasure[1].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[1].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[1].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[1].reference.identifier.value
        == "NCT05503693-primaryOutcome-1"
    )
    assert (
        inst.outcomeMeasure[1].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[1].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[1].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[1].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.outcomeMeasure[2].description == "PK characteristics after single dose"
    assert inst.outcomeMeasure[2].name == "Cmax after single dose"
    assert (
        inst.outcomeMeasure[2].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[2].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[2].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[2].reference.identifier.value
        == "NCT05503693-primaryOutcome-2"
    )
    assert (
        inst.outcomeMeasure[2].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[2].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[2].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[2].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.outcomeMeasure[3].description == "PK characteristics after single dose"
    assert inst.outcomeMeasure[3].name == "Tmax after single dose"
    assert (
        inst.outcomeMeasure[3].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[3].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[3].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[3].reference.identifier.value
        == "NCT05503693-primaryOutcome-3"
    )
    assert (
        inst.outcomeMeasure[3].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[3].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[3].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[3].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.outcomeMeasure[4].description == "PK characteristics after single dose"
    assert inst.outcomeMeasure[4].name == "AUC0-last after single dose"
    assert (
        inst.outcomeMeasure[4].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[4].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[4].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[4].reference.identifier.value
        == "NCT05503693-primaryOutcome-4"
    )
    assert (
        inst.outcomeMeasure[4].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[4].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[4].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[4].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.outcomeMeasure[5].description == "PK characteristics after single dose"
    assert inst.outcomeMeasure[5].name == "AUC0-inf after single dose"
    assert (
        inst.outcomeMeasure[5].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[5].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[5].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[5].reference.identifier.value
        == "NCT05503693-primaryOutcome-5"
    )
    assert (
        inst.outcomeMeasure[5].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[5].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[5].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[5].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.outcomeMeasure[6].description == "PK characteristics after single dose"
    assert inst.outcomeMeasure[6].name == "t1/2 after single dose"
    assert (
        inst.outcomeMeasure[6].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[6].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[6].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[6].reference.identifier.value
        == "NCT05503693-primaryOutcome-6"
    )
    assert (
        inst.outcomeMeasure[6].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[6].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[6].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[6].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.outcomeMeasure[7].description == "PK characteristics after single dose"
    assert inst.outcomeMeasure[7].name == "CL/F after single dose"
    assert (
        inst.outcomeMeasure[7].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[7].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[7].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[7].reference.identifier.value
        == "NCT05503693-primaryOutcome-7"
    )
    assert (
        inst.outcomeMeasure[7].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[7].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[7].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[7].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.outcomeMeasure[8].description == "PK characteristics after single dose"
    assert inst.outcomeMeasure[8].name == "Ae and CLR (if warranted) after single dose"
    assert (
        inst.outcomeMeasure[8].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[8].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[8].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[8].reference.identifier.value
        == "NCT05503693-primaryOutcome-8"
    )
    assert (
        inst.outcomeMeasure[8].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[8].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[8].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[8].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.outcomeMeasure[9].description == "PK characteristics after single dose"
    assert inst.outcomeMeasure[9].name == "V/F after single dose"
    assert (
        inst.outcomeMeasure[9].reference.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.outcomeMeasure[9].reference.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.outcomeMeasure[9].reference.identifier.type.text
        == "FEvIR Linking Identifier"
    )
    assert (
        inst.outcomeMeasure[9].reference.identifier.value
        == "NCT05503693-primaryOutcome-9"
    )
    assert (
        inst.outcomeMeasure[9].reference.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.outcomeMeasure[9].type[0].coding[0].code == "primary"
    assert inst.outcomeMeasure[9].type[0].coding[0].display == "Primary"
    assert (
        inst.outcomeMeasure[9].type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-objective-type"
            }
        ).valueUri
    )
    assert inst.phase.coding[0].code == "phase-1"
    assert inst.phase.coding[0].display == "Phase 1"
    assert (
        inst.phase.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/research-study-phase"}
        ).valueUri
    )
    assert inst.primaryPurposeType.coding[0].code == "treatment"
    assert inst.primaryPurposeType.coding[0].display == "Treatment"
    assert (
        inst.primaryPurposeType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type"
            }
        ).valueUri
    )
    assert inst.progressStatus[0].state.coding[0].code == "recruiting"
    assert inst.progressStatus[0].state.coding[0].display == "Recruiting"
    assert (
        inst.progressStatus[0].state.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/research-study-status"}
        ).valueUri
    )
    assert inst.progressStatus[1].actual is False
    assert (
        inst.progressStatus[1].period.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-06"}
        ).valueDateTime
    )
    assert (
        inst.progressStatus[1].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-12-06"}
        ).valueDateTime
    )
    assert inst.progressStatus[1].state.coding[0].code == "overall-study"
    assert inst.progressStatus[1].state.coding[0].display == "Overall Study"
    assert (
        inst.progressStatus[1].state.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/research-study-status"}
        ).valueUri
    )
    assert (
        inst.recruitment.eligibility.identifier.assigner.display
        == "Computable Publishing LLC"
    )
    assert (
        inst.recruitment.eligibility.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/FLI"}
        ).valueUri
    )
    assert (
        inst.recruitment.eligibility.identifier.type.text == "FEvIR Linking Identifier"
    )
    assert (
        inst.recruitment.eligibility.identifier.value
        == "NCT05503693 Eligibility Criteria"
    )
    assert (
        inst.recruitment.eligibility.reference
        == "https://fevir.net/resources/EvidenceVariable/112075"
    )
    assert (
        inst.recruitment.eligibility.type
        == ExternalValidatorModel.model_validate(
            {"valueUri": "EvidenceVariable"}
        ).valueUri
    )
    assert inst.recruitment.targetNumber == 62
    assert (
        inst.relatedArtifact[0].document.url
        == ExternalValidatorModel.model_validate(
            {"valueUrl": "https://beta.clinicaltrials.gov/api/v2/studies/NCT05503693"}
        ).valueUrl
    )
    assert inst.relatedArtifact[0].type == "transforms"
    assert inst.relatedArtifact[1].display == (
        "Computable Publishing®: ClinicalTrials.gov-to-FEvIR " "Converter"
    )
    assert (
        inst.relatedArtifact[1].document.url
        == ExternalValidatorModel.model_validate(
            {"valueUrl": "https://fevir.net/resources/Project/29885"}
        ).valueUrl
    )
    assert inst.relatedArtifact[1].type == "transformed-with"
    assert inst.site[0].reference == "#NCT05503693-Location-0-ResearchStudy"
    assert (
        inst.site[0].type
        == ExternalValidatorModel.model_validate({"valueUri": "ResearchStudy"}).valueUri
    )
    assert inst.status == "active"
    assert inst.studyDesign[0].text == "Design Masking: Quadruple"
    assert inst.studyDesign[1].text == "Design Who Masked: Participant"
    assert inst.studyDesign[2].text == "Design Who Masked: Care Provider"
    assert inst.studyDesign[3].text == "Design Who Masked: Investigator"
    assert inst.studyDesign[4].text == "Design Who Masked: Outcomes Assessor"
    assert inst.studyDesign[5].text == "Design Allocation: Randomized"
    assert (
        inst.studyDesign[6].text == "Design Intervention Model: Sequential Assignment"
    )
    assert inst.studyDesign[7].text == "CT.gov StudyType: INTERVENTIONAL"
    assert inst.text.status == "generated"
    assert inst.title == (
        "A Safety, Tolerability, and Pharmacokinetics Study of AP303 "
        "in Healthy Subjects"
    )
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://fevir.net/resources/ResearchStudy/112103"}
        ).valueUri
    )


def test_researchstudy_1(base_settings):
    """No. 1 tests collection for ResearchStudy.
    Test File: researchstudy-example-ctgov-study-record.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "researchstudy-example-ctgov-study-record.json"
    )
    inst = researchstudy.ResearchStudy.model_validate_json(filename.read_bytes())
    assert "ResearchStudy" == inst.get_resource_type()

    impl_researchstudy_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ResearchStudy" == data["resourceType"]

    inst2 = researchstudy.ResearchStudy(**data)
    impl_researchstudy_1(inst2)
