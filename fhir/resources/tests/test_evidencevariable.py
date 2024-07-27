# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import evidencevariable
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_evidencevariable_1(inst):
    assert inst.actual is True
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].code == "182886004"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].display
        == "Placebo given (situation)"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.characteristic[0].description == "placebo"
    assert inst.description == "placebo"
    assert inst.id == "example-placebo"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "Placebo"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "placebo"


def test_evidencevariable_1(base_settings):
    """No. 1 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-placebo.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-placebo.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_1(inst2)


def impl_evidencevariable_2(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionExpression.description == "mRS 0-2"
    assert inst.characteristic[0].definitionExpression.expression == (
        '["Observation": code in "75859-9|LOINC"] mRS where '
        "mRS.value between 0 and 2"
    )
    assert inst.characteristic[0].definitionExpression.language == "text/cql"
    assert inst.characteristic[0].description == "mRS 0-2 at 90 days"
    assert (
        inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].code
        == "study-start"
    )
    assert (
        inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].display
        == "Study Start"
    )
    assert (
        inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/evidence-variable-event"
        ).valueUri
    )
    assert inst.characteristic[0].timeFromEvent[0].quantity.code == "d"
    assert (
        inst.characteristic[0].timeFromEvent[0].quantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[0].timeFromEvent[0].quantity.unit == "day"
    assert float(inst.characteristic[0].timeFromEvent[0].quantity.value) == float(90)
    assert (
        inst.description == "Modified Rankin Scale score 0-2 at 90 days after treatment"
    )
    assert inst.handling == "dichotomous"
    assert inst.id == "example-mRS0-2-at-90days"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "ModifiedRankinScaleScore02At90DaysAfterTreatment"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Modified Rankin Scale score 0-2 at 90 days after treatment"


def test_evidencevariable_2(base_settings):
    """No. 2 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-mRS0-2-at-90days.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-mRS0-2-at-90days.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_2(inst2)


def impl_evidencevariable_3(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionCanonical == (
        "http://example.org/fhir/ActivityDefinition/example-" "alteplase-dosing"
    )
    assert inst.characteristic[0].description == (
        "IV alteplase 0.9 mg/kg (maximum 90 mg) as 10% of dose over 1"
        " minute and 90% over 1 hour"
    )
    assert inst.description == "Alteplase for Stroke"
    assert inst.id == "example-alteplase-for-stroke"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "AlteplaseForStroke"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Alteplase for Stroke"


def test_evidencevariable_3(base_settings):
    """No. 3 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-alteplase-for-stroke.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-alteplase-for-stroke.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_3(inst2)


def impl_evidencevariable_4(inst):
    assert inst.actual is False
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].code == "8410"
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].display
        == "alteplase"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://www.nlm.nih.gov/research/umls/rxnorm"
        ).valueUri
    )
    assert inst.characteristic[0].description == "no alteplase"
    assert inst.characteristic[0].exclude is True
    assert inst.description == "no alteplase"
    assert inst.id == "example-no-alteplase"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "NoAlteplase"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "no alteplase"


def test_evidencevariable_4(base_settings):
    """No. 4 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-no-alteplase.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-no-alteplase.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_4(inst2)


def impl_evidencevariable_5(inst):
    assert inst.actual is False
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .definitionCodeableConcept.coding[0]
        .code
        == "718705001"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .definitionCodeableConcept.coding[0]
        .display
        == "Functionally dependent (finding)"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .definitionCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[0].definitionByCombination.characteristic[0].description
        == "functionally dependent at 90 days"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .timeFromEvent[0]
        .eventCodeableConcept.coding[0]
        .code
        == "study-start"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .timeFromEvent[0]
        .eventCodeableConcept.coding[0]
        .display
        == "Study Start"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .timeFromEvent[0]
        .eventCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/evidence-variable-event"
        ).valueUri
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .timeFromEvent[0]
        .quantity.code
        == "d"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .timeFromEvent[0]
        .quantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .timeFromEvent[0]
        .quantity.unit
        == "day"
    )
    assert float(
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .timeFromEvent[0]
        .quantity.value
    ) == float(90)
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .definitionCodeableConcept.coding[0]
        .code
        == "419099009"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .definitionCodeableConcept.coding[0]
        .display
        == "Dead (finding)"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .definitionCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[0].definitionByCombination.characteristic[1].description
        == "dead at 90 days"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .timeFromEvent[0]
        .quantity.code
        == "d"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .timeFromEvent[0]
        .quantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .timeFromEvent[0]
        .quantity.unit
        == "day"
    )
    assert float(
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .timeFromEvent[0]
        .quantity.value
    ) == float(90)
    assert inst.characteristic[0].definitionByCombination.code == "any-of"
    assert (
        inst.characteristic[0].description
        == "Dead or functionally dependent at 90 days"
    )
    assert inst.description == "Dead or functionally dependent at 90 days"
    assert inst.handling == "dichotomous"
    assert inst.id == "example-dead-or-dependent-90day"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "DeadOrFunctionallyDependentAt90Days"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Dead or functionally dependent at 90 days"


def test_evidencevariable_5(base_settings):
    """No. 5 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-dead-or-dependent-90day.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-dead-or-dependent-90day.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_5(inst2)


def impl_evidencevariable_6(inst):
    assert inst.actual is True
    assert inst.author[0].name == "Brian S. Alper"
    assert (
        inst.characteristic[0].definitionByTypeAndValue.type.coding[0].code
        == "424144002"
    )
    assert (
        inst.characteristic[0].definitionByTypeAndValue.type.coding[0].display
        == "Current chronological age"
    )
    assert (
        inst.characteristic[0].definitionByTypeAndValue.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.characteristic[0].definitionByTypeAndValue.valueQuantity.code == "a"
    assert (
        inst.characteristic[0].definitionByTypeAndValue.valueQuantity.comparator == ">="
    )
    assert (
        inst.characteristic[0].definitionByTypeAndValue.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[0].definitionByTypeAndValue.valueQuantity.unit == "year"
    assert float(
        inst.characteristic[0].definitionByTypeAndValue.valueQuantity.value
    ) == float(18)
    assert inst.characteristic[0].description == "adult (age ≥18 years old)"
    assert inst.characteristic[0].exclude is False
    assert (
        inst.characteristic[1].definitionByTypeAndValue.type.coding[0].code == "39156-5"
    )
    assert (
        inst.characteristic[1].definitionByTypeAndValue.type.coding[0].display
        == "Body mass index (BMI) [Ratio]"
    )
    assert (
        inst.characteristic[1].definitionByTypeAndValue.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert inst.characteristic[1].definitionByTypeAndValue.valueQuantity.code == "kg/m2"
    assert (
        inst.characteristic[1].definitionByTypeAndValue.valueQuantity.comparator == ">="
    )
    assert (
        inst.characteristic[1].definitionByTypeAndValue.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[1].definitionByTypeAndValue.valueQuantity.unit == "kg/m2"
    assert float(
        inst.characteristic[1].definitionByTypeAndValue.valueQuantity.value
    ) == float(30)
    assert inst.characteristic[1].description == "obese (Body mass index >= 30 kg/m2)"
    assert inst.characteristic[1].exclude is False
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "support@computablepublishing.com"
    assert inst.copyright == "https://creativecommons.org/licenses/by-nc-sa/4.0/"
    assert (
        inst.date
        == ExternalValidatorModel(
            valueDateTime="2022-07-24T21:00:00.088Z"
        ).valueDateTime
    )
    assert inst.description == "obese, adult (age ≥18 years old) patients"
    assert inst.id == "example-eligibility-criteria-adults-with-obesity"
    assert inst.identifier[0].assigner.display == "Computable Publishing LLC"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="https://fevir.net").valueUri
    )
    assert inst.identifier[0].type.text == "FEvIR Object Identifier"
    assert inst.identifier[0].value == "49218"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "StudyEligibilityCriteriaObesePatients18YearsOld"
    assert inst.publisher == "Computable Publishing LLC"
    assert (
        inst.relatedArtifact[0].document.url
        == ExternalValidatorModel(
            valueUrl="https://academic.oup.com/eurheartj/article/43/20/1955/6542137"
        ).valueUrl
    )
    assert inst.relatedArtifact[0].label == "data source"
    assert inst.relatedArtifact[0].type == "derived-from"
    assert (
        inst.relatedArtifact[1].classifier[0].text
        == "Citation Resource for the original article"
    )
    assert inst.relatedArtifact[1].display == (
        "Citation Resource for 2022 Systematic Review of bariatric "
        "surgery mortality effect - PMID 35243488"
    )
    assert inst.relatedArtifact[1].resourceReference.display == (
        "StudyCitation: 2022 Systematic Review of bariatric surgery "
        "mortality effect 35243488"
    )
    assert inst.relatedArtifact[1].resourceReference.reference == "Citation/33400"
    assert (
        inst.relatedArtifact[1].resourceReference.type
        == ExternalValidatorModel(valueUri="Citation").valueUri
    )
    assert inst.relatedArtifact[1].type == "supported-with"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "StudyEligibilityCriteria: Obese patients ≥ 18 years old"


def test_evidencevariable_6(base_settings):
    """No. 6 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-eligibility-criteria-adults-with-obesity.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-eligibility-criteria-adults-with-obesity.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_6(inst2)


def impl_evidencevariable_7(inst):
    assert inst.actual is True
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .definitionReference.display
        == "ECASS III Trial Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .definitionReference.reference
        == "Group/ECASSIII-Trial-Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[0]
        .definitionReference.type
        == ExternalValidatorModel(valueUri="Group").valueUri
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .definitionReference.display
        == "IST3 Trial Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .definitionReference.reference
        == "Group/IST3-Trial-Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[1]
        .definitionReference.type
        == ExternalValidatorModel(valueUri="Group").valueUri
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[2]
        .definitionReference.display
        == "ECASS Trial Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[2]
        .definitionReference.reference
        == "Group/ECASS-Trial-Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[2]
        .definitionReference.type
        == ExternalValidatorModel(valueUri="Group").valueUri
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[3]
        .definitionReference.display
        == "ECASSII Trial Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[3]
        .definitionReference.reference
        == "Group/ECASSII-Trial-Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[3]
        .definitionReference.type
        == ExternalValidatorModel(valueUri="Group").valueUri
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[4]
        .definitionReference.display
        == "EPITHET Trial Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[4]
        .definitionReference.reference
        == "Group/EPITHET-Trial-Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[4]
        .definitionReference.type
        == ExternalValidatorModel(valueUri="Group").valueUri
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[5]
        .definitionReference.display
        == "ATLANTIS Trial Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[5]
        .definitionReference.reference
        == "Group/ATLANTIS-Trial-Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[5]
        .definitionReference.type
        == ExternalValidatorModel(valueUri="Group").valueUri
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[6]
        .definitionReference.display
        == "NINDS Trial Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[6]
        .definitionReference.reference
        == "Group/NINDS-Trial-Cohort"
    )
    assert (
        inst.characteristic[0]
        .definitionByCombination.characteristic[6]
        .definitionReference.type
        == ExternalValidatorModel(valueUri="Group").valueUri
    )
    assert inst.characteristic[0].definitionByCombination.code == "any-of"
    assert inst.characteristic[0].description == (
        "Stroke Thrombolysis Trialists’ Collaborators Group "
        "collection used for individual patient data meta-analysis"
    )
    assert inst.description == (
        "Stroke Thrombolysis Trialists’ Collaborators Group "
        "collection used for individual patient data meta-analysis"
    )
    assert inst.id == (
        "example-Stroke-Thrombolysis-Trialists-2014-2016-IPD-MA-" "Cohort"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "StrokeThrombolysisTrialists20142016IPDMACohort"
    assert (
        inst.relatedArtifact[0].document.url
        == ExternalValidatorModel(
            valueUrl="https://doi.org/10.1016/S0140-6736(14)60584-5"
        ).valueUrl
    )
    assert inst.relatedArtifact[0].label == "Emberson 2014"
    assert inst.relatedArtifact[0].type == "citation"
    assert inst.relatedArtifact[1].display == "Figure 2 Lees 2016"
    assert (
        inst.relatedArtifact[1].document.url
        == ExternalValidatorModel(
            valueUrl="https://doi.org/10.1161/STROKEAHA.116.013644"
        ).valueUrl
    )
    assert inst.relatedArtifact[1].label == "Lees 2016"
    assert inst.relatedArtifact[1].type == "citation"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == (
        "Stroke Thrombolysis Trialists’ Collaborators Group "
        "collection used for individual patient data meta-analysis"
    )


def test_evidencevariable_7(base_settings):
    """No. 7 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-Stroke-Thrombolysis-Trialists-2014-2016-IPD-MA-Cohort.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-Stroke-Thrombolysis-Trialists-2014-2016-IPD-MA-Cohort.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_7(inst2)


def impl_evidencevariable_8(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].code == "1386000"
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].display
        == "Intracranial hemorrhage (disorder)"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.characteristic[0].description == "intracranial hemorrhage within 7 days"
    assert inst.characteristic[0].timeFromEvent[0].description == "within 7 days"
    assert (
        inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].code
        == "study-start"
    )
    assert (
        inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].display
        == "Study Start"
    )
    assert (
        inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/evidence-variable-event"
        ).valueUri
    )
    assert inst.characteristic[0].timeFromEvent[0].range.high.code == "d"
    assert (
        inst.characteristic[0].timeFromEvent[0].range.high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[0].timeFromEvent[0].range.high.unit == "day"
    assert float(inst.characteristic[0].timeFromEvent[0].range.high.value) == float(7)
    assert inst.characteristic[0].timeFromEvent[0].range.low.code == "d"
    assert (
        inst.characteristic[0].timeFromEvent[0].range.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[0].timeFromEvent[0].range.low.unit == "day"
    assert float(inst.characteristic[0].timeFromEvent[0].range.low.value) == float(0)
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].code == "419620001"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].display
        == "Death (event)"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.characteristic[1].description == "death within 7 days"
    assert inst.characteristic[1].timeFromEvent[0].description == "within 7 days"
    assert inst.characteristic[1].timeFromEvent[0].range.high.code == "d"
    assert (
        inst.characteristic[1].timeFromEvent[0].range.high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[1].timeFromEvent[0].range.high.unit == "day"
    assert float(inst.characteristic[1].timeFromEvent[0].range.high.value) == float(7)
    assert inst.characteristic[1].timeFromEvent[0].range.low.code == "d"
    assert (
        inst.characteristic[1].timeFromEvent[0].range.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[1].timeFromEvent[0].range.low.unit == "day"
    assert float(inst.characteristic[1].timeFromEvent[0].range.low.value) == float(0)
    assert inst.description == "Fatal Intracranial Hemorrhage Within Seven Days"
    assert inst.handling == "dichotomous"
    assert inst.id == "example-fatal-ICH-in-7-days"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "FatalIntracranialHemorrhageWithinSevenDays"
    assert inst.note[0].text == "Death must be due to intracranial hemorrhage"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Fatal Intracranial Hemorrhage Within Seven Days"


def test_evidencevariable_8(base_settings):
    """No. 8 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-fatal-ICH-in-7-days.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-fatal-ICH-in-7-days.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_8(inst2)


def impl_evidencevariable_9(inst):
    assert inst.actual is False
    assert inst.author[0].name == "Brian S. Alper"
    assert (
        inst.characteristic[0].definitionByTypeAndValue.type.coding[0].code
        == "397669002"
    )
    assert (
        inst.characteristic[0].definitionByTypeAndValue.type.coding[0].display == "Age"
    )
    assert (
        inst.characteristic[0].definitionByTypeAndValue.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.characteristic[0].definitionByTypeAndValue.valueQuantity.code == "a"
    assert (
        inst.characteristic[0].definitionByTypeAndValue.valueQuantity.comparator == ">="
    )
    assert (
        inst.characteristic[0].definitionByTypeAndValue.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[0].definitionByTypeAndValue.valueQuantity.unit == "years"
    assert float(
        inst.characteristic[0].definitionByTypeAndValue.valueQuantity.value
    ) == float(18)
    assert inst.characteristic[0].description == "Adult."
    assert inst.characteristic[0].exclude is False
    assert (
        inst.characteristic[1].definitionByTypeAndValue.type.coding[0].code
        == "64572001"
    )
    assert (
        inst.characteristic[1].definitionByTypeAndValue.type.coding[0].display
        == "Disease (disorder)"
    )
    assert (
        inst.characteristic[1].definitionByTypeAndValue.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[1].definitionByTypeAndValue.type.coding[1].code
        == "Condition"
    )
    assert (
        inst.characteristic[1].definitionByTypeAndValue.type.coding[1].display
        == "Condition"
    )
    assert (
        inst.characteristic[1].definitionByTypeAndValue.type.coding[1].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/resource-types"
        ).valueUri
    )
    assert (
        inst.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .code
        == "44054006"
    )
    assert (
        inst.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .display
        == "Diabetes mellitus type 2 (disorder)"
    )
    assert (
        inst.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.characteristic[1].description == "Diagnosed with type 2 diabetes."
    assert inst.characteristic[1].exclude is False
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "39156-5"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Body mass index (BMI) [Ratio]"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.code
        == "kg/m2"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.comparator
        == ">="
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.unit
        == "kg/m2"
    )
    assert float(
        inst.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.value
    ) == float(40)
    assert (
        inst.characteristic[2].definitionByCombination.characteristic[0].description
        == "Body Mass Index (BMI) ≥ 40.0 kg/m2"
    )
    assert (
        inst.characteristic[2].definitionByCombination.characteristic[0].exclude
        is False
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "39156-5"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Body mass index (BMI) [Ratio]"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.code
        == "kg/m2"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.comparator
        == ">="
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.unit
        == "kg/m2"
    )
    assert float(
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueQuantity.value
    ) == float(37.5)
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .description
        == "BMI ≥ 37.5 kg/m2"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[0]
        .exclude
        is False
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "103579009"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Race (observable entity)"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .code
        == "2028-9"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .display
        == "Asian"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="urn:oid:2.16.840.1.113883.6.238").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.text
        == "Asian American"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[1]
        .description
        == "Asian American"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.characteristic[1]
        .linkId
        == "AsianAmerican"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[1]
        .definitionByCombination.code
        == "all-of"
    )
    assert (
        inst.characteristic[2].definitionByCombination.characteristic[1].description
        == "BMI ≥ 37.5 kg/m2 in Asian Americans"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "39156-5"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Body mass index (BMI) [Ratio]"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.high.code
        == "kg/m2"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.high.unit
        == "kg/m2"
    )
    assert float(
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.high.value
    ) == float(39.9)
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.low.code
        == "kg/m2"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.low.unit
        == "kg/m2"
    )
    assert float(
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.low.value
    ) == float(35)
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[0]
        .description
        == "BMI ≥ 35.0 kg/m2 and ≤ 39.9 kg/m2"
    )
    assert inst.characteristic[2].definitionByCombination.characteristic[
        2
    ].definitionByCombination.characteristic[1].definitionCodeableConcept.text == (
        "achieving durable weight loss and improvement in "
        "comorbidities (including hyperglycemia) with nonsurgical "
        "methods"
    )
    assert inst.characteristic[2].definitionByCombination.characteristic[
        2
    ].definitionByCombination.characteristic[1].description == (
        "who do not achieve durable weight loss and improvement in "
        "comorbidities (including hyperglycemia) with nonsurgical "
        "methods."
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.characteristic[1]
        .exclude
        is True
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[2]
        .definitionByCombination.code
        == "all-of"
    )
    assert inst.characteristic[2].definitionByCombination.characteristic[
        2
    ].description == (
        "BMI ≥ 35.0 kg/m2 and ≤ 39.9 kg/m2 who do not achieve durable"
        " weight loss and improvement in comorbidities (including "
        "hyperglycemia) with nonsurgical methods."
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "39156-5"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Body mass index (BMI) [Ratio]"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.high.code
        == "kg/m2"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.high.unit
        == "kg/m2"
    )
    assert float(
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.high.value
    ) == float(37.4)
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.low.code
        == "kg/m2"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.low.unit
        == "kg/m2"
    )
    assert float(
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueRange.low.value
    ) == float(32.5)
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[0]
        .description
        == "BMI ≥ 32.5 kg/m2 and ≤ 37.4 kg/m2"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionId
        == "AsianAmerican"
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[1]
        .description
        == "Asian American"
    )
    assert inst.characteristic[2].definitionByCombination.characteristic[
        3
    ].definitionByCombination.characteristic[2].definitionCodeableConcept.text == (
        "achieving durable weight loss and improvement in "
        "comorbidities (including hyperglycemia) with nonsurgical "
        "methods"
    )
    assert inst.characteristic[2].definitionByCombination.characteristic[
        3
    ].definitionByCombination.characteristic[2].description == (
        "who do not achieve durable weight loss and improvement in "
        "comorbidities (including hyperglycemia) with nonsurgical "
        "methods."
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.characteristic[2]
        .exclude
        is True
    )
    assert (
        inst.characteristic[2]
        .definitionByCombination.characteristic[3]
        .definitionByCombination.code
        == "all-of"
    )
    assert inst.characteristic[2].definitionByCombination.characteristic[
        3
    ].description == (
        "BMI ≥ 32.5 kg/m2 and ≤ 37.4 kg/m2 in Asian Americans who do "
        "not achieve durable weight loss and improvement in "
        "comorbidities (including hyperglycemia) with nonsurgical "
        "methods."
    )
    assert inst.characteristic[2].definitionByCombination.code == "any-of"
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "64572001"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Disease (disorder)"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[1]
        .code
        == "Condition"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[1]
        .display
        == "Condition"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[1]
        .system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/resource-types"
        ).valueUri
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueReference.display
        == "Acute Coronary Heart Disease Value Set"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueReference.reference
        == "ValueSet/32152"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueReference.type
        == ExternalValidatorModel(valueUri="ValueSet").valueUri
    )
    assert inst.characteristic[3].definitionByCombination.characteristic[
        0
    ].description == (
        "acute coronary heart disease (a value set covering many " "forms)"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "71388002"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Procedure (procedure)"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[1]
        .code
        == "Procedure"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[1]
        .display
        == "Procedure"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[1]
        .system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/resource-types"
        ).valueUri
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .code
        == "81266008"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .display
        == "Heart revascularization (procedure)"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[3].definitionByCombination.characteristic[1].description
        == "coronary artery angioplasty or bypass"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "64572001"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Disease (disorder)"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[1]
        .code
        == "Condition"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[1]
        .display
        == "Condition"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[1]
        .system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/resource-types"
        ).valueUri
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .code
        == "230690007"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .display
        == "Cerebrovascular accident (disorder)"
    )
    assert (
        inst.characteristic[3]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[3].definitionByCombination.characteristic[2].description
        == "stroke"
    )
    assert inst.characteristic[3].definitionByCombination.code == "any-of"
    assert inst.characteristic[3].description == (
        "Cardiovascular event (myocardial infarction, acute coronary "
        "syndrome, coronary artery angioplasty or bypass, stroke) in "
        "the past six months."
    )
    assert inst.characteristic[3].exclude is True
    assert inst.characteristic[3].note[0].text == (
        "placeholder for now to represent 'screened surgical " "candidate'"
    )
    assert (
        inst.characteristic[3].timeFromEvent[0].description == "in the past six months"
    )
    assert inst.characteristic[3].timeFromEvent[0].note[0].text == (
        "occurrence within the range is equivalent to 'in the past " "six months'"
    )
    assert inst.characteristic[3].timeFromEvent[0].range.high.code == "mo"
    assert (
        inst.characteristic[3].timeFromEvent[0].range.high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[3].timeFromEvent[0].range.high.unit == "months"
    assert float(inst.characteristic[3].timeFromEvent[0].range.high.value) == float(0)
    assert inst.characteristic[3].timeFromEvent[0].range.low.code == "mo"
    assert (
        inst.characteristic[3].timeFromEvent[0].range.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[3].timeFromEvent[0].range.low.unit == "months"
    assert float(inst.characteristic[3].timeFromEvent[0].range.low.value) == float(-6)
    assert inst.characteristic[4].definitionCodeableConcept.text == (
        "Current evidence of congestive heart failure, angina "
        "pectoris, or symptomatic peripheral vascular disease."
    )
    assert inst.characteristic[4].description == (
        "Current evidence of congestive heart failure, angina "
        "pectoris, or symptomatic peripheral vascular disease."
    )
    assert inst.characteristic[4].exclude is True
    assert inst.characteristic[4].note[0].text == (
        "This may be possible to encode as presence of "
        "Disease(disorder) without 'in remission'"
    )
    assert inst.characteristic[4].note[1].text == (
        "placeholder for now to represent 'screened surgical " "candidate'"
    )
    assert inst.characteristic[5].definitionCodeableConcept.text == (
        "Cardiac stress test indicating that surgery or IMM would not" " be safe."
    )
    assert inst.characteristic[5].description == (
        "Cardiac stress test indicating that surgery or IMM would not" " be safe."
    )
    assert inst.characteristic[5].exclude is True
    assert inst.characteristic[5].note[0].text == (
        "placeholder for now to represent 'screened surgical " "candidate'"
    )
    assert (
        inst.characteristic[6].definitionByTypeAndValue.type.coding[0].code
        == "64572001"
    )
    assert (
        inst.characteristic[6].definitionByTypeAndValue.type.coding[0].display
        == "Disease (disorder)"
    )
    assert (
        inst.characteristic[6].definitionByTypeAndValue.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[6].definitionByTypeAndValue.type.coding[1].code
        == "Condition"
    )
    assert (
        inst.characteristic[6].definitionByTypeAndValue.type.coding[1].display
        == "Condition"
    )
    assert (
        inst.characteristic[6].definitionByTypeAndValue.type.coding[1].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/resource-types"
        ).valueUri
    )
    assert (
        inst.characteristic[6]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .code
        == "59282003"
    )
    assert (
        inst.characteristic[6]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .display
        == "Pulmonary embolism (disorder)"
    )
    assert (
        inst.characteristic[6]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[6].description
        == "Pulmonary embolus in the past six months."
    )
    assert inst.characteristic[6].exclude is True
    assert inst.characteristic[6].note[0].text == (
        "placeholder for now to represent 'screened surgical " "candidate'"
    )
    assert (
        inst.characteristic[6].timeFromEvent[0].description == "in the past six months"
    )
    assert inst.characteristic[6].timeFromEvent[0].note[0].text == (
        "occurrence within the range is equivalent to 'in the past " "six months'"
    )
    assert inst.characteristic[6].timeFromEvent[0].range.high.code == "mo"
    assert (
        inst.characteristic[6].timeFromEvent[0].range.high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[6].timeFromEvent[0].range.high.unit == "months"
    assert float(inst.characteristic[6].timeFromEvent[0].range.high.value) == float(0)
    assert inst.characteristic[6].timeFromEvent[0].range.low.code == "mo"
    assert (
        inst.characteristic[6].timeFromEvent[0].range.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[6].timeFromEvent[0].range.low.unit == "months"
    assert float(inst.characteristic[6].timeFromEvent[0].range.low.value) == float(-6)
    assert (
        inst.characteristic[7].definitionByTypeAndValue.type.coding[0].code
        == "64572001"
    )
    assert (
        inst.characteristic[7].definitionByTypeAndValue.type.coding[0].display
        == "Disease (disorder)"
    )
    assert (
        inst.characteristic[7].definitionByTypeAndValue.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[7].definitionByTypeAndValue.type.coding[1].code
        == "Condition"
    )
    assert (
        inst.characteristic[7].definitionByTypeAndValue.type.coding[1].display
        == "Condition"
    )
    assert (
        inst.characteristic[7].definitionByTypeAndValue.type.coding[1].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/resource-types"
        ).valueUri
    )
    assert (
        inst.characteristic[7]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .code
        == "64156001"
    )
    assert (
        inst.characteristic[7]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .display
        == "Thrombophlebitis (disorder)"
    )
    assert (
        inst.characteristic[7]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[7].description == "Thrombophlebitis in the past six months."
    )
    assert inst.characteristic[7].exclude is True
    assert inst.characteristic[7].note[0].text == (
        "placeholder for now to represent 'screened surgical " "candidate'"
    )
    assert (
        inst.characteristic[7].timeFromEvent[0].description == "in the past six months"
    )
    assert inst.characteristic[7].timeFromEvent[0].note[0].text == (
        "occurrence within the range is equivalent to 'in the past " "six months'"
    )
    assert inst.characteristic[7].timeFromEvent[0].range.high.code == "mo"
    assert (
        inst.characteristic[7].timeFromEvent[0].range.high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[7].timeFromEvent[0].range.high.unit == "months"
    assert float(inst.characteristic[7].timeFromEvent[0].range.high.value) == float(0)
    assert inst.characteristic[7].timeFromEvent[0].range.low.code == "mo"
    assert (
        inst.characteristic[7].timeFromEvent[0].range.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[7].timeFromEvent[0].range.low.unit == "months"
    assert float(inst.characteristic[7].timeFromEvent[0].range.low.value) == float(-6)
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "64572001"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Disease (disorder)"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[1]
        .code
        == "Condition"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[1]
        .display
        == "Condition"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.type.coding[1]
        .system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/resource-types"
        ).valueUri
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .code
        == "363346000"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .display
        == "Malignant neoplastic disease (disorder)"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[0]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[8].definitionByCombination.characteristic[0].description
        == "Cancer of any kind"
    )
    assert (
        inst.characteristic[8].definitionByCombination.characteristic[0].exclude
        is False
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "64572001"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Disease (disorder)"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[1]
        .code
        == "Condition"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[1]
        .display
        == "Condition"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.type.coding[1]
        .system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/resource-types"
        ).valueUri
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .code
        == "254701007"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .display
        == "Basal cell carcinoma of skin (disorder)"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[1]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[8].definitionByCombination.characteristic[1].description
        == "(except basal cell skin cancer)"
    )
    assert (
        inst.characteristic[8].definitionByCombination.characteristic[1].exclude is True
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[0]
        .code
        == "64572001"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[0]
        .display
        == "Disease (disorder)"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[1]
        .code
        == "Condition"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[1]
        .display
        == "Condition"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.type.coding[1]
        .system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/resource-types"
        ).valueUri
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .code
        == "109355002"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .display
        == "Carcinoma in situ (disorder)"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[2]
        .definitionByTypeAndValue.valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[8].definitionByCombination.characteristic[2].description
        == "(except cancer in situ)"
    )
    assert (
        inst.characteristic[8].definitionByCombination.characteristic[2].exclude is True
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .definitionCodeableConcept.coding[0]
        .code
        == "395100000"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .definitionCodeableConcept.coding[0]
        .display
        == "No evidence of cancer found (situation)"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .definitionCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.characteristic[8].definitionByCombination.characteristic[3].description
        == "unless documented to be disease-free for five years"
    )
    assert (
        inst.characteristic[8].definitionByCombination.characteristic[3].exclude is True
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .timeFromEvent[0]
        .description
        == "for five years"
    )
    assert inst.characteristic[8].definitionByCombination.characteristic[
        3
    ].timeFromEvent[0].note[0].text == (
        "presence throughout the range is equivalent to 'for five " "years'"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .timeFromEvent[0]
        .range.high.code
        == "a"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .timeFromEvent[0]
        .range.high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .timeFromEvent[0]
        .range.high.unit
        == "years"
    )
    assert float(
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .timeFromEvent[0]
        .range.high.value
    ) == float(0)
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .timeFromEvent[0]
        .range.low.code
        == "a"
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .timeFromEvent[0]
        .range.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert (
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .timeFromEvent[0]
        .range.low.unit
        == "years"
    )
    assert float(
        inst.characteristic[8]
        .definitionByCombination.characteristic[3]
        .timeFromEvent[0]
        .range.low.value
    ) == float(-5)
    assert inst.characteristic[8].definitionByCombination.code == "all-of"
    assert inst.characteristic[8].description == (
        "Cancer of any kind (except basal cell skin cancer or cancer "
        "in situ) unless documented to be disease-free for five "
        "years."
    )
    assert inst.characteristic[8].exclude is True
    assert inst.characteristic[8].note[0].text == (
        "This combination logic fails if the patient has both a basal"
        " cell skin cancer or cancer in situ and a cancer of another "
        "kind."
    )
    assert inst.characteristic[8].note[1].text == (
        "placeholder for now to represent 'screened surgical " "candidate'"
    )
    assert (
        inst.characteristic[9].definitionCodeableConcept.text
        == "history of coagulopathy"
    )
    assert inst.characteristic[9].description == "History of coagulopathy"
    assert inst.characteristic[9].exclude is True
    assert inst.characteristic[9].note[0].text == (
        "placeholder for now to represent 'screened surgical " "candidate'"
    )
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "support@computablepublishing.com"
    assert inst.copyright == "https://creativecommons.org/licenses/by-nc-sa/4.0/"
    assert (
        inst.effectivePeriod.start
        == ExternalValidatorModel(valueDateTime="2021-01").valueDateTime
    )
    assert inst.id == "example-eligibility-criteria-ada-rec-bariatric"
    assert inst.identifier[0].assigner.display == "Computable Publishing LLC"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="https://fevir.net").valueUri
    )
    assert inst.identifier[0].type.text == "FEvIR Object Identifier"
    assert inst.identifier[0].value == "32140"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == (
        "RecommendationEligibilityCriteriaEligibilityCriteriaForBaria"
        "tricSurgeryADARecommendation816"
    )
    assert inst.publisher == "Computable Publishing LLC"
    assert inst.shortTitle == "Recommend bariatric surgery if BMI 35 or higher"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == (
        "RecommendationEligibilityCriteria: Eligibility Criteria for "
        "Bariatric Surgery (ADA Recommendation 8.16)"
    )


def test_evidencevariable_9(base_settings):
    """No. 9 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-eligibility-criteria-ada-rec-bariatric.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-eligibility-criteria-ada-rec-bariatric.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_9(inst2)


def impl_evidencevariable_10(inst):
    assert inst.actual is False
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].code == "718705001"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].display
        == "Functionally dependent (finding)"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.characteristic[0].description == "not functionally dependent at 90 days"
    assert inst.characteristic[0].exclude is True
    assert (
        inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].code
        == "study-start"
    )
    assert (
        inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].display
        == "Study Start"
    )
    assert (
        inst.characteristic[0].timeFromEvent[0].eventCodeableConcept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/evidence-variable-event"
        ).valueUri
    )
    assert inst.characteristic[0].timeFromEvent[0].quantity.code == "d"
    assert (
        inst.characteristic[0].timeFromEvent[0].quantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[0].timeFromEvent[0].quantity.unit == "day"
    assert float(inst.characteristic[0].timeFromEvent[0].quantity.value) == float(90)
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].code == "419099009"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].display
        == "Dead (finding)"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.characteristic[1].description == "alive at 90 days"
    assert inst.characteristic[1].exclude is True
    assert (
        inst.characteristic[1].timeFromEvent[0].eventCodeableConcept.coding[0].code
        == "study-start"
    )
    assert (
        inst.characteristic[1].timeFromEvent[0].eventCodeableConcept.coding[0].display
        == "Study Start"
    )
    assert (
        inst.characteristic[1].timeFromEvent[0].eventCodeableConcept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/evidence-variable-event"
        ).valueUri
    )
    assert inst.characteristic[1].timeFromEvent[0].quantity.code == "d"
    assert (
        inst.characteristic[1].timeFromEvent[0].quantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.characteristic[1].timeFromEvent[0].quantity.unit == "day"
    assert float(inst.characteristic[1].timeFromEvent[0].quantity.value) == float(90)
    assert inst.description == "Alive and not functionally dependent at 90 days"
    assert inst.handling == "dichotomous"
    assert inst.id == "example-alive-independent-90day"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "AliveAndNotFunctionallyDependentAt90Days"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Alive and not functionally dependent at 90 days"


def test_evidencevariable_10(base_settings):
    """No. 10 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-alive-independent-90day.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-alive-independent-90day.json"
    )
    inst = evidencevariable.EvidenceVariable.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EvidenceVariable" == inst.get_resource_type()

    impl_evidencevariable_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_10(inst2)
