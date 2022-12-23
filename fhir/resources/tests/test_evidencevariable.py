# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import evidencevariable


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
        == "http://snomed.info/sct"
    )
    assert inst.characteristic[0].description == "placebo"
    assert inst.id == "example-placebo"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "placebo"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"


def test_evidencevariable_1(base_settings):
    """No. 1 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-placebo.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "evidencevariable-example-placebo.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
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
    assert inst.characteristic[0].timeFromStart.quantity.code == "d"
    assert (
        inst.characteristic[0].timeFromStart.quantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[0].timeFromStart.quantity.unit == "day"
    assert float(inst.characteristic[0].timeFromStart.quantity.value) == float(90)
    assert inst.handling == "dichotomous"
    assert inst.id == "example-mRS0-2-at-90days"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Modified Rankin Scale score 0-2 at 90 days after treatment"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"


def test_evidencevariable_2(base_settings):
    """No. 2 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-mRS0-2-at-90days.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-mRS0-2-at-90days.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
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
    assert inst.id == "example-alteplase-for-stroke"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Alteplase for Stroke"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"


def test_evidencevariable_3(base_settings):
    """No. 3 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-alteplase-for-stroke.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-alteplase-for-stroke.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
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
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.characteristic[0].description == "no alteplase"
    assert inst.characteristic[0].exclude is True
    assert inst.id == "example-no-alteplase"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "no alteplase"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"


def test_evidencevariable_4(base_settings):
    """No. 4 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-no-alteplase.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-no-alteplase.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_4(inst2)


def impl_evidencevariable_5(inst):
    assert inst.actual is False
    assert inst.characteristicCombination == "union"
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].code == "718705001"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].display
        == "Functionally dependent (finding)"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.characteristic[0].description == "functionally dependent at 90 days"
    assert inst.characteristic[0].timeFromStart.quantity.code == "d"
    assert (
        inst.characteristic[0].timeFromStart.quantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[0].timeFromStart.quantity.unit == "day"
    assert float(inst.characteristic[0].timeFromStart.quantity.value) == float(90)
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].code == "419099009"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].display
        == "Dead (finding)"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.characteristic[1].description == "dead at 90 days"
    assert inst.characteristic[1].timeFromStart.quantity.code == "d"
    assert (
        inst.characteristic[1].timeFromStart.quantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[1].timeFromStart.quantity.unit == "day"
    assert float(inst.characteristic[1].timeFromStart.quantity.value) == float(90)
    assert inst.handling == "dichotomous"
    assert inst.id == "example-dead-or-dependent-90day"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Dead or functionally dependent at 90 days"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"


def test_evidencevariable_5(base_settings):
    """No. 5 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-dead-or-dependent-90day.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-dead-or-dependent-90day.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_5(inst2)


def impl_evidencevariable_6(inst):
    assert inst.actual is True
    assert inst.characteristicCombination == "union"
    assert (
        inst.characteristic[0].definitionReference.display == "ECASS III Trial Cohort"
    )
    assert (
        inst.characteristic[0].definitionReference.reference
        == "Group/ECASSIII-Trial-Cohort"
    )
    assert inst.characteristic[0].definitionReference.type == "Group"
    assert inst.characteristic[1].definitionReference.display == "IST3 Trial Cohort"
    assert (
        inst.characteristic[1].definitionReference.reference
        == "Group/IST3-Trial-Cohort"
    )
    assert inst.characteristic[1].definitionReference.type == "Group"
    assert inst.characteristic[2].definitionReference.display == "ECASS Trial Cohort"
    assert (
        inst.characteristic[2].definitionReference.reference
        == "Group/ECASS-Trial-Cohort"
    )
    assert inst.characteristic[2].definitionReference.type == "Group"
    assert inst.characteristic[3].definitionReference.display == "ECASSII Trial Cohort"
    assert (
        inst.characteristic[3].definitionReference.reference
        == "Group/ECASSII-Trial-Cohort"
    )
    assert inst.characteristic[3].definitionReference.type == "Group"
    assert inst.characteristic[4].definitionReference.display == "EPITHET Trial Cohort"
    assert (
        inst.characteristic[4].definitionReference.reference
        == "Group/EPITHET-Trial-Cohort"
    )
    assert inst.characteristic[4].definitionReference.type == "Group"
    assert inst.characteristic[5].definitionReference.display == "ATLANTIS Trial Cohort"
    assert (
        inst.characteristic[5].definitionReference.reference
        == "Group/ATLANTIS-Trial-Cohort"
    )
    assert inst.characteristic[5].definitionReference.type == "Group"
    assert inst.characteristic[6].definitionReference.display == "NINDS Trial Cohort"
    assert (
        inst.characteristic[6].definitionReference.reference
        == "Group/NINDS-Trial-Cohort"
    )
    assert inst.characteristic[6].definitionReference.type == "Group"
    assert inst.id == (
        "example-Stroke-Thrombolysis-Trialists-2014-2016-IPD-MA-" "Cohort"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "Stroke Thrombolysis Trialists’ 2014-2016 IPD-MA Cohort"
    assert inst.relatedArtifact[0].label == "Emberson 2014"
    assert inst.relatedArtifact[0].type == "citation"
    assert (
        inst.relatedArtifact[0].url == "https://doi.org/10.1016/S0140-6736(14)60584-5"
    )
    assert inst.relatedArtifact[1].display == "Figure 2 Lees 2016"
    assert inst.relatedArtifact[1].label == "Lees 2016"
    assert inst.relatedArtifact[1].type == "citation"
    assert inst.relatedArtifact[1].url == "https://doi.org/10.1161/STROKEAHA.116.013644"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == (
        "Stroke Thrombolysis Trialists’ Collaborators Group "
        "collection used for individual patient data meta-analysis"
    )
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"


def test_evidencevariable_6(base_settings):
    """No. 6 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-Stroke-Thrombolysis-
    Trialists-2014-2016-IPD-MA-Cohort.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-Stroke-Thrombolysis-Trialists-2014-2016-IPD-MA-Cohort.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_6(inst2)


def impl_evidencevariable_7(inst):
    assert inst.actual is True
    assert inst.characteristicCombination == "intersection"
    assert inst.characteristic[0].definitionCodeableConcept.coding[0].code == "1386000"
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].display
        == "Intracranial hemorrhage (disorder)"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.characteristic[0].description == "intracranial hemorrhage within 7 days"
    assert inst.characteristic[0].timeFromStart.description == "within 7 days"
    assert inst.characteristic[0].timeFromStart.range.high.code == "d"
    assert (
        inst.characteristic[0].timeFromStart.range.high.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[0].timeFromStart.range.high.unit == "day"
    assert float(inst.characteristic[0].timeFromStart.range.high.value) == float(7)
    assert inst.characteristic[0].timeFromStart.range.low.code == "d"
    assert (
        inst.characteristic[0].timeFromStart.range.low.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[0].timeFromStart.range.low.unit == "day"
    assert float(inst.characteristic[0].timeFromStart.range.low.value) == float(0)
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].code == "419620001"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].display
        == "Death (event)"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.characteristic[1].description == "death within 7 days"
    assert inst.characteristic[1].timeFromStart.description == "within 7 days"
    assert inst.characteristic[1].timeFromStart.range.high.code == "d"
    assert (
        inst.characteristic[1].timeFromStart.range.high.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[1].timeFromStart.range.high.unit == "day"
    assert float(inst.characteristic[1].timeFromStart.range.high.value) == float(7)
    assert inst.characteristic[1].timeFromStart.range.low.code == "d"
    assert (
        inst.characteristic[1].timeFromStart.range.low.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[1].timeFromStart.range.low.unit == "day"
    assert float(inst.characteristic[1].timeFromStart.range.low.value) == float(0)
    assert inst.handling == "dichotomous"
    assert inst.id == "example-fatal-ICH-in-7-days"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Death must be due to intracranial hemorrhage"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Fatal Intracranial Hemorrhage Within Seven Days"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"
    assert inst.useContext[1].code.code == "1386000"
    assert inst.useContext[1].code.display == "Intracranial hemorrhage"
    assert inst.useContext[1].code.system == "http://snomed.info/sct"
    assert inst.useContext[1].valueRange.high.unit == "d"
    assert float(inst.useContext[1].valueRange.high.value) == float(7)
    assert inst.useContext[1].valueRange.low.unit == "d"
    assert float(inst.useContext[1].valueRange.low.value) == float(0)


def test_evidencevariable_7(base_settings):
    """No. 7 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-fatal-ICH-in-7-days.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-fatal-ICH-in-7-days.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_7(inst2)


def impl_evidencevariable_8(inst):
    assert inst.actual is False
    assert inst.characteristicCombination == "intersection"
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].code == "718705001"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].display
        == "Functionally dependent (finding)"
    )
    assert (
        inst.characteristic[0].definitionCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.characteristic[0].description == "not functionally dependent at 90 days"
    assert inst.characteristic[0].exclude is True
    assert inst.characteristic[0].timeFromStart.quantity.code == "d"
    assert (
        inst.characteristic[0].timeFromStart.quantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[0].timeFromStart.quantity.unit == "day"
    assert float(inst.characteristic[0].timeFromStart.quantity.value) == float(90)
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].code == "419099009"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].display
        == "Dead (finding)"
    )
    assert (
        inst.characteristic[1].definitionCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.characteristic[1].description == "alive at 90 days"
    assert inst.characteristic[1].exclude is True
    assert inst.characteristic[1].timeFromStart.quantity.code == "d"
    assert (
        inst.characteristic[1].timeFromStart.quantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[1].timeFromStart.quantity.unit == "day"
    assert float(inst.characteristic[1].timeFromStart.quantity.value) == float(90)
    assert inst.handling == "dichotomous"
    assert inst.id == "example-alive-independent-90day"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Alive and not functionally dependent at 90 days"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"


def test_evidencevariable_8(base_settings):
    """No. 8 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-alive-independent-90day.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-alive-independent-90day.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_8(inst2)


def impl_evidencevariable_9(inst):
    assert inst.actual is True
    assert inst.characteristic[0].definitionExpression.description == "mRS 3-6"
    assert inst.characteristic[0].definitionExpression.expression == (
        '["Observation": code in "75859-9|LOINC"] mRS where '
        "mRS.value between 3 and 6"
    )
    assert inst.characteristic[0].definitionExpression.language == "text/cql"
    assert inst.characteristic[0].description == "mRS 3-6 at 90 days"
    assert inst.characteristic[0].timeFromStart.quantity.code == "d"
    assert (
        inst.characteristic[0].timeFromStart.quantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.characteristic[0].timeFromStart.quantity.unit == "day"
    assert float(inst.characteristic[0].timeFromStart.quantity.value) == float(90)
    assert inst.handling == "dichotomous"
    assert inst.id == "example-mRS3-6-at-90days"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Modified Rankin Scale score 3-6 at 90 days after treatment"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"


def test_evidencevariable_9(base_settings):
    """No. 9 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-mRS3-6-at-90days.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-mRS3-6-at-90days.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_9(inst2)


def impl_evidencevariable_10(inst):
    assert inst.actual is True
    assert inst.characteristicCombination == "union"
    assert inst.characteristic[0].definitionReference.display == "NINDS 1995"
    assert inst.characteristic[0].definitionReference.type == "Evidence"
    assert inst.characteristic[1].definitionReference.display == "ECASS 1995"
    assert inst.characteristic[1].definitionReference.type == "Evidence"
    assert inst.characteristic[2].definitionReference.display == "ECASS II 1998"
    assert inst.characteristic[2].definitionReference.type == "Evidence"
    assert inst.characteristic[3].definitionReference.display == "ATLANTIS B 1999"
    assert inst.characteristic[3].definitionReference.type == "Evidence"
    assert inst.characteristic[4].definitionReference.display == "ATLANTIS A 2000"
    assert inst.characteristic[4].definitionReference.type == "Evidence"
    assert inst.characteristic[5].definitionReference.display == "IST3 2012"
    assert inst.characteristic[5].definitionReference.type == "Evidence"
    assert inst.handling == "dichotomous"
    assert inst.id == "example-Wardlaw2014Analysis1.16.3EvidenceSet"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "Wardlaw 2014 Analysis 1.16.3 Evidence set"
    assert inst.note[0].text == (
        "Short names for Evidence sources are detailed in "
        '"References to studies included in this review"'
    )
    assert inst.relatedArtifact[0].citation == (
        "Wardlaw JM, Murray V, Berge E, del Zoppo GJ. Thrombolysis "
        "for acute ischaemic stroke. Cochrane Database Syst Rev. 2014"
        " Jul 29(7):CD000213. PMID 25072528"
    )
    assert inst.relatedArtifact[0].display == "Analysis 1.16.3 from Wardlaw 2014"
    assert inst.relatedArtifact[0].label == "Wardlaw 2014"
    assert inst.relatedArtifact[0].type == "citation"
    assert (
        inst.relatedArtifact[0].url == "https://doi.org/10.1002/14651858.CD000213.pub3"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Wardlaw 2014 Analysis 1.16.3 Evidence set"
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"


def test_evidencevariable_10(base_settings):
    """No. 10 tests collection for EvidenceVariable.
    Test File: evidencevariable-example-Wardlaw2014Analysis1.16.3EvidenceSet.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidencevariable-example-Wardlaw2014Analysis1.16.3EvidenceSet.json"
    )
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_10(inst2)
