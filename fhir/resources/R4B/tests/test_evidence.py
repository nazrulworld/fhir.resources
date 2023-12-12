# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Evidence
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import evidence


def impl_evidence_1(inst):
    assert inst.description == (
        "0.4% incidence of fatal intracranial hemorrhage within 7 "
        "days without alteplase in patients with acute ischemic "
        "stroke"
    )
    assert inst.id == "example-stroke-no-alteplase-fatalICH"
    assert inst.relatedArtifact[0].label == "Emberson 2014"
    assert inst.relatedArtifact[0].type == "citation"
    assert (
        inst.relatedArtifact[0].url == "https://doi.org/10.1016/S0140-6736(14)60584-5"
    )
    assert inst.statistic[0].numberOfEvents == 13
    assert float(inst.statistic[0].quantity.value) == float(0.00386298627)
    assert inst.statistic[0].sampleSize.numberOfParticipants == 3365
    assert inst.statistic[0].sampleSize.numberOfStudies == 9
    assert inst.statistic[0].statisticType.coding[0].code == "C44256"
    assert inst.statistic[0].statisticType.coding[0].display == "Proportion"
    assert (
        inst.statistic[0].statisticType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/statistic-type"
    )
    assert inst.status == "draft"
    assert inst.studyType.coding[0].code == "RCT"
    assert inst.studyType.coding[0].display == "randomized trial"
    assert (
        inst.studyType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/study-type"
    )
    assert inst.synthesisType.coding[0].code == "IPD-MA"
    assert (
        inst.synthesisType.coding[0].display == "individual patient data meta-analysis"
    )
    assert (
        inst.synthesisType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/synthesis-type"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Risk of fatal ICH without alteplase for stroke"
    assert inst.url == (
        "http://hl7.org/fhir/Evidence/example-stroke-no-alteplase-" "fatalICH"
    )
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
    assert (
        inst.variableDefinition[0].intended.display
        == "adults with acute ischemic stroke"
    )
    assert inst.variableDefinition[0].intended.reference == "Group/AcuteIschemicStroke"
    assert inst.variableDefinition[0].intended.type == "Group"
    assert (
        inst.variableDefinition[0].observed.display
        == "adults with acute ischemic stroke"
    )
    assert inst.variableDefinition[0].observed.reference == "Group/AcuteIschemicStroke"
    assert inst.variableDefinition[0].observed.type == "Group"
    assert inst.variableDefinition[0].variableRole.coding[0].code == "population"
    assert inst.variableDefinition[0].variableRole.coding[0].display == "population"
    assert (
        inst.variableDefinition[0].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert (
        inst.variableDefinition[1].intended.display
        == "adults with acute ischemic stroke treated without alteplase"
    )
    assert (
        inst.variableDefinition[1].intended.reference
        == "Group/AcuteIschemicStrokeTreatedWithoutAlteplase"
    )
    assert inst.variableDefinition[1].intended.type == "Group"
    assert (
        inst.variableDefinition[1].observed.display
        == "Emberson 2014 IPD-MA No Alteplase Cohort"
    )
    assert (
        inst.variableDefinition[1].observed.reference
        == "Group/Emberson-2014-IPD-MA-No-Alteplase-Cohort"
    )
    assert inst.variableDefinition[1].observed.type == "Group"
    assert inst.variableDefinition[1].variableRole.coding[0].code == "population"
    assert inst.variableDefinition[1].variableRole.coding[0].display == "population"
    assert (
        inst.variableDefinition[1].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert inst.variableDefinition[2].intended.display == "fatal ICH"
    assert (
        inst.variableDefinition[2].intended.reference
        == "EvidenceVariable/example-fatal-ICH-in-7-days"
    )
    assert inst.variableDefinition[2].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[2].observed.display == "fatal ICH"
    assert (
        inst.variableDefinition[2].observed.reference
        == "EvidenceVariable/example-fatal-ICH-in-7-days"
    )
    assert inst.variableDefinition[2].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[2].variableRole.coding[0].code == "measuredVariable"
    assert (
        inst.variableDefinition[2].variableRole.coding[0].display == "measured variable"
    )
    assert (
        inst.variableDefinition[2].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )


def test_evidence_1(base_settings):
    """No. 1 tests collection for Evidence.
    Test File: evidence-example-stroke-no-alteplase-fatalICH.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidence-example-stroke-no-alteplase-fatalICH.json"
    )
    inst = evidence.Evidence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Evidence" == inst.resource_type

    impl_evidence_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Evidence" == data["resourceType"]

    inst2 = evidence.Evidence(**data)
    impl_evidence_1(inst2)


def impl_evidence_2(inst):
    assert inst.certainty[0].description == (
        "Very low certainty due to risk of bias, inconsistency, "
        "imprecision, and indirectness"
    )
    assert inst.certainty[0].rating.coding[0].code == "very-low"
    assert inst.certainty[0].rating.coding[0].display == "Very low quality"
    assert (
        inst.certainty[0].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[0].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[0].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[0].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[0].type.coding[0].code == "PublicationBias"
    assert (
        inst.certainty[0].subcomponent[0].type.coding[0].display == "Publication bias"
    )
    assert (
        inst.certainty[0].subcomponent[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[1].note[0].text == (
        "IST-3 had inconsistent results and contributed large " "proportion of data"
    )
    assert inst.certainty[0].subcomponent[1].rating.coding[0].code == "serious-concern"
    assert (
        inst.certainty[0].subcomponent[1].rating.coding[0].display == "serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[1].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[1].type.coding[0].code == "Inconsistency"
    assert inst.certainty[0].subcomponent[1].type.coding[0].display == "Inconsistency"
    assert (
        inst.certainty[0].subcomponent[1].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[2].rating.coding[0].code == "serious-concern"
    assert (
        inst.certainty[0].subcomponent[2].rating.coding[0].display == "serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[2].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[2].type.coding[0].code == "Imprecision"
    assert inst.certainty[0].subcomponent[2].type.coding[0].display == "Imprecision"
    assert (
        inst.certainty[0].subcomponent[2].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[3].note[0].text == (
        "resuts derived for 3 - 4.5 hours assume data from 0 - 6 "
        "hours is informative"
    )
    assert inst.certainty[0].subcomponent[3].rating.coding[0].code == "serious-concern"
    assert (
        inst.certainty[0].subcomponent[3].rating.coding[0].display == "serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[3].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[3].type.coding[0].code == "Indirectness"
    assert inst.certainty[0].subcomponent[3].type.coding[0].display == "Indirectness"
    assert (
        inst.certainty[0].subcomponent[3].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[4].note[0].text == (
        "results largely influenced by IST-3 trial which was "
        "unblinded and ECASS III which had baseline imbalances"
    )
    assert inst.certainty[0].subcomponent[4].rating.coding[0].code == "serious-concern"
    assert (
        inst.certainty[0].subcomponent[4].rating.coding[0].display == "serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[4].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[4].type.coding[0].code == "RiskOfBias"
    assert inst.certainty[0].subcomponent[4].type.coding[0].display == "Risk of bias"
    assert (
        inst.certainty[0].subcomponent[4].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].type.coding[0].code == "Overall"
    assert inst.certainty[0].type.coding[0].display == "Overall quality"
    assert (
        inst.certainty[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.description == (
        "mRS 0-2 at 90 days Odds Ratio 1.2 for Alteplase vs. No "
        "Alteplase in patients with acute ischemic stroke 3-4.5 hours"
        " prior"
    )
    assert inst.id == "example-stroke-3-4half-alteplase-vs-no-alteplase-mRS0-2"
    assert inst.relatedArtifact[0].display == "Figure 2 Lees 2016"
    assert inst.relatedArtifact[0].label == "Lees 2016"
    assert inst.relatedArtifact[0].type == "citation"
    assert inst.relatedArtifact[0].url == "https://doi.org/10.1161/STROKEAHA.116.013644"
    assert inst.statistic[0].attributeEstimate[0].description == "95% CI 1.06 to 1.3"
    assert float(inst.statistic[0].attributeEstimate[0].level) == float(0.95)
    assert float(inst.statistic[0].attributeEstimate[0].range.high.value) == float(1.3)
    assert float(inst.statistic[0].attributeEstimate[0].range.low.value) == float(1.06)
    assert inst.statistic[0].attributeEstimate[0].type.coding[0].code == "C53324"
    assert (
        inst.statistic[0].attributeEstimate[0].type.coding[0].display
        == "Confidence interval"
    )
    assert inst.statistic[0].attributeEstimate[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/attribute-estimate-" "type"
    )
    assert float(inst.statistic[0].quantity.value) == float(1.2)
    assert inst.statistic[0].sampleSize.numberOfStudies == 9
    assert inst.statistic[0].statisticType.coding[0].code == "C16932"
    assert inst.statistic[0].statisticType.coding[0].display == "Odds Ratio"
    assert (
        inst.statistic[0].statisticType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/statistic-type"
    )
    assert inst.status == "draft"
    assert inst.studyType.coding[0].code == "RCT"
    assert inst.studyType.coding[0].display == "randomized trial"
    assert (
        inst.studyType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/study-type"
    )
    assert inst.synthesisType.coding[0].code == "IPD-MA"
    assert (
        inst.synthesisType.coding[0].display == "individual patient data meta-analysis"
    )
    assert (
        inst.synthesisType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/synthesis-type"
    )
    assert inst.text.status == "generated"
    assert inst.title == (
        "Effect of Alteplase vs No alteplase on mRS 0-2 at 90 days in"
        " Stroke 3-4.5 hours prior"
    )
    assert inst.url == (
        "http://hl7.org/fhir/Evidence/example-stroke-3-4half-"
        "alteplase-vs-no-alteplase-mRS0-2"
    )
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"
    assert inst.variableDefinition[0].directnessMatch.coding[0].code == "moderate"
    assert (
        inst.variableDefinition[0].directnessMatch.coding[0].display
        == "Moderate quality match"
    )
    assert (
        inst.variableDefinition[0].directnessMatch.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/directness"
    )
    assert inst.variableDefinition[0].intended.display == "stroke at 3-4.5 hours"
    assert (
        inst.variableDefinition[0].intended.reference
        == "Group/AcuteIschemicStroke3-4halfHours"
    )
    assert inst.variableDefinition[0].intended.type == "Group"
    assert (
        inst.variableDefinition[0].observed.display
        == "Stroke Thrombolysis Trialists’ 2014-2016 IPD-MA Cohort"
    )
    assert inst.variableDefinition[0].observed.reference == (
        "EvidenceVariable/Stroke-Thrombolysis-" "Trialists-2014-2016-IPD-MA-Cohort"
    )
    assert inst.variableDefinition[0].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[0].variableRole.coding[0].code == "population"
    assert inst.variableDefinition[0].variableRole.coding[0].display == "population"
    assert (
        inst.variableDefinition[0].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert (
        inst.variableDefinition[1].intended.display
        == "Alive and not functionally dependent at 90 days"
    )
    assert (
        inst.variableDefinition[1].intended.reference
        == "EvidenceVariable/example-alive-independent-90day"
    )
    assert inst.variableDefinition[1].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[1].observed.display == "mRS 0-2 at 90 days"
    assert (
        inst.variableDefinition[1].observed.reference
        == "EvidenceVariable/example-mRS0-2-at-90days"
    )
    assert inst.variableDefinition[1].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[1].variableRole.coding[0].code == "measuredVariable"
    assert (
        inst.variableDefinition[1].variableRole.coding[0].display == "measured variable"
    )
    assert (
        inst.variableDefinition[1].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert inst.variableDefinition[2].intended.display == "Alteplase for Stroke"
    assert (
        inst.variableDefinition[2].intended.reference
        == "EvidenceVariable/example-alteplase-for-stroke"
    )
    assert inst.variableDefinition[2].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[2].observed.display == "Alteplase for Stroke"
    assert (
        inst.variableDefinition[2].observed.reference
        == "EvidenceVariable/example-alteplase-for-stroke"
    )
    assert inst.variableDefinition[2].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[2].variableRole.coding[0].code == "exposure"
    assert inst.variableDefinition[2].variableRole.coding[0].display == "exposure"
    assert (
        inst.variableDefinition[2].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert inst.variableDefinition[3].intended.display == "no alteplase"
    assert (
        inst.variableDefinition[3].intended.reference
        == "EvidenceVariable/example-no-alteplase"
    )
    assert inst.variableDefinition[3].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[3].observed.display == "no alteplase"
    assert (
        inst.variableDefinition[3].observed.reference
        == "EvidenceVariable/example-no-alteplase"
    )
    assert inst.variableDefinition[3].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[3].variableRole.coding[0].code == "referenceExposure"
    assert (
        inst.variableDefinition[3].variableRole.coding[0].display
        == "reference exposure"
    )
    assert (
        inst.variableDefinition[3].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )


def test_evidence_2(base_settings):
    """No. 2 tests collection for Evidence.
    Test File: evidence-example-stroke-3-4half-alteplase-vs-no-alteplase-mRS0-2.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidence-example-stroke-3-4half-alteplase-vs-no-alteplase-mRS0-2.json"
    )
    inst = evidence.Evidence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Evidence" == inst.resource_type

    impl_evidence_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Evidence" == data["resourceType"]

    inst2 = evidence.Evidence(**data)
    impl_evidence_2(inst2)


def impl_evidence_3(inst):
    assert inst.certainty[0].description == "Moderate certainty due to risk of bias"
    assert inst.certainty[0].rating.coding[0].code == "moderate"
    assert inst.certainty[0].rating.coding[0].display == "Moderate"
    assert (
        inst.certainty[0].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[0].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[0].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[0].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[0].type.coding[0].code == "PublicationBias"
    assert (
        inst.certainty[0].subcomponent[0].type.coding[0].display == "Publication bias"
    )
    assert (
        inst.certainty[0].subcomponent[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[1].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[1].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[1].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[1].type.coding[0].code == "Inconsistency"
    assert inst.certainty[0].subcomponent[1].type.coding[0].display == "Inconsistency"
    assert (
        inst.certainty[0].subcomponent[1].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[2].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[2].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[2].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[2].type.coding[0].code == "Imprecision"
    assert inst.certainty[0].subcomponent[2].type.coding[0].display == "Imprecision"
    assert (
        inst.certainty[0].subcomponent[2].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[3].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[3].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[3].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[3].type.coding[0].code == "Indirectness"
    assert inst.certainty[0].subcomponent[3].type.coding[0].display == "Indirectness"
    assert (
        inst.certainty[0].subcomponent[3].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[4].note[0].text == (
        "results largely influenced by IST-3 trial which was "
        "unblinded and NINDS trial which had allocation concealment "
        "not stated and baseline imbalances"
    )
    assert inst.certainty[0].subcomponent[4].rating.coding[0].code == "serious-concern"
    assert (
        inst.certainty[0].subcomponent[4].rating.coding[0].display == "serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[4].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[4].type.coding[0].code == "RiskOfBias"
    assert inst.certainty[0].subcomponent[4].type.coding[0].display == "Risk of bias"
    assert (
        inst.certainty[0].subcomponent[4].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].type.coding[0].code == "Overall"
    assert inst.certainty[0].type.coding[0].display == "Overall quality"
    assert (
        inst.certainty[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.description == (
        "mRS 3-6 at 90 days Odds Ratio 0.65 for Alteplase vs. No "
        "Alteplase in patients with acute ischemic stroke 0-3 hours "
        "prior"
    )
    assert inst.id == "example-stroke-0-3-alteplase-vs-no-alteplase-mRS3-6"
    assert inst.relatedArtifact[0].citation == (
        "Wardlaw JM, Murray V, Berge E, del Zoppo GJ. Thrombolysis "
        "for acute ischaemic stroke. Cochrane Database Syst Rev. 2014"
        " Jul 29(7):CD000213. PMID 25072528"
    )
    assert inst.relatedArtifact[0].display == "Analysis 1.16 from Wardlaw 2014"
    assert inst.relatedArtifact[0].label == "Wardlaw 2014"
    assert inst.relatedArtifact[0].type == "citation"
    assert (
        inst.relatedArtifact[0].url == "https://doi.org/10.1002/14651858.CD000213.pub3"
    )
    assert inst.statistic[0].attributeEstimate[0].description == "95% CI 0.54 to 0.80"
    assert float(inst.statistic[0].attributeEstimate[0].level) == float(0.95)
    assert float(inst.statistic[0].attributeEstimate[0].range.high.value) == float(0.8)
    assert float(inst.statistic[0].attributeEstimate[0].range.low.value) == float(0.54)
    assert inst.statistic[0].attributeEstimate[0].type.coding[0].code == "C53324"
    assert (
        inst.statistic[0].attributeEstimate[0].type.coding[0].display
        == "Confidence interval"
    )
    assert inst.statistic[0].attributeEstimate[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/attribute-estimate-" "type"
    )
    assert inst.statistic[0].attributeEstimate[1].description == "P-value = 0.000023"
    assert float(inst.statistic[0].attributeEstimate[1].quantity.value) == float(
        2.3e-05
    )
    assert inst.statistic[0].attributeEstimate[1].type.coding[0].code == "C44185"
    assert inst.statistic[0].attributeEstimate[1].type.coding[0].display == "P-value"
    assert inst.statistic[0].attributeEstimate[1].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/attribute-estimate-" "type"
    )
    assert (
        inst.statistic[0].attributeEstimate[2].description
        == "Heterogeneity I-sq = 0.0%"
    )
    assert inst.statistic[0].attributeEstimate[2].quantity.code == "%"
    assert (
        inst.statistic[0].attributeEstimate[2].quantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.statistic[0].attributeEstimate[2].quantity.unit == "%"
    assert float(inst.statistic[0].attributeEstimate[2].quantity.value) == float(0)
    assert inst.statistic[0].attributeEstimate[2].type.coding[0].code == "0000420"
    assert inst.statistic[0].attributeEstimate[2].type.coding[0].display == "I-squared"
    assert inst.statistic[0].attributeEstimate[2].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/attribute-estimate-" "type"
    )
    assert inst.statistic[0].numberOfEvents == 1137
    assert float(inst.statistic[0].quantity.value) == float(0.65)
    assert inst.statistic[0].sampleSize.numberOfParticipants == 1779
    assert inst.statistic[0].sampleSize.numberOfStudies == 6
    assert inst.statistic[0].statisticType.coding[0].code == "C16932"
    assert inst.statistic[0].statisticType.coding[0].display == "Odds Ratio"
    assert (
        inst.statistic[0].statisticType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/statistic-type"
    )
    assert inst.status == "draft"
    assert inst.studyType.coding[0].code == "RCT"
    assert inst.studyType.coding[0].display == "randomized trial"
    assert (
        inst.studyType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/study-type"
    )
    assert inst.synthesisType.coding[0].code == "std-MA"
    assert inst.synthesisType.coding[0].display == "summary data meta-analysis"
    assert (
        inst.synthesisType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/synthesis-type"
    )
    assert inst.text.status == "generated"
    assert inst.title == (
        "Effect of Alteplase vs No alteplase on mRS 3-6 at 90 days in"
        " Stroke 0-3 hours prior"
    )
    assert inst.url == (
        "http://hl7.org/fhir/Evidence/example-stroke-0-3-alteplase-"
        "vs-no-alteplase-mRS3-6"
    )
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"
    assert inst.variableDefinition[0].intended.display == "stroke at 0-3 hours"
    assert (
        inst.variableDefinition[0].intended.reference
        == "Group/AcuteIschemicStroke0-3Hours"
    )
    assert inst.variableDefinition[0].intended.type == "Group"
    assert (
        inst.variableDefinition[0].observed.display
        == "Wardlaw 2014 Analysis 1.16.3 Evidence set"
    )
    assert (
        inst.variableDefinition[0].observed.reference
        == "EvidenceVariable/Wardlaw2014Analysis1.16.3EvidenceSet"
    )
    assert inst.variableDefinition[0].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[0].variableRole.coding[0].code == "population"
    assert inst.variableDefinition[0].variableRole.coding[0].display == "population"
    assert (
        inst.variableDefinition[0].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert (
        inst.variableDefinition[1].intended.display
        == "Dead or functionally dependent at 90 days"
    )
    assert (
        inst.variableDefinition[1].intended.reference
        == "EvidenceVariable/example-dead-or-dependent-90day"
    )
    assert inst.variableDefinition[1].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[1].observed.display == "mRS 3-6 at 90 days"
    assert (
        inst.variableDefinition[1].observed.reference
        == "EvidenceVariable/example-mRS3-6-at-90days"
    )
    assert inst.variableDefinition[1].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[1].variableRole.coding[0].code == "measuredVariable"
    assert (
        inst.variableDefinition[1].variableRole.coding[0].display == "measured variable"
    )
    assert (
        inst.variableDefinition[1].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert inst.variableDefinition[2].intended.display == "Alteplase for Stroke"
    assert (
        inst.variableDefinition[2].intended.reference
        == "EvidenceVariable/example-alteplase-for-stroke"
    )
    assert inst.variableDefinition[2].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[2].observed.display == "Alteplase for Stroke"
    assert (
        inst.variableDefinition[2].observed.reference
        == "EvidenceVariable/example-alteplase-for-stroke"
    )
    assert inst.variableDefinition[2].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[2].variableRole.coding[0].code == "exposure"
    assert inst.variableDefinition[2].variableRole.coding[0].display == "exposure"
    assert (
        inst.variableDefinition[2].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert inst.variableDefinition[3].intended.display == "no alteplase"
    assert (
        inst.variableDefinition[3].intended.reference
        == "EvidenceVariable/example-no-alteplase"
    )
    assert inst.variableDefinition[3].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[3].observed.display == "no alteplase"
    assert (
        inst.variableDefinition[3].observed.reference
        == "EvidenceVariable/example-no-alteplase"
    )
    assert inst.variableDefinition[3].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[3].variableRole.coding[0].code == "referenceExposure"
    assert (
        inst.variableDefinition[3].variableRole.coding[0].display
        == "reference exposure"
    )
    assert (
        inst.variableDefinition[3].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )


def test_evidence_3(base_settings):
    """No. 3 tests collection for Evidence.
    Test File: evidence-example-stroke-0-3-alteplase-vs-no-alteplase-mRS3-6.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidence-example-stroke-0-3-alteplase-vs-no-alteplase-mRS3-6.json"
    )
    inst = evidence.Evidence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Evidence" == inst.resource_type

    impl_evidence_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Evidence" == data["resourceType"]

    inst2 = evidence.Evidence(**data)
    impl_evidence_3(inst2)


def impl_evidence_4(inst):
    assert inst.description == (
        "2.7% incidence of fatal intracranial hemorrhage within 7 "
        "days with alteplase in patients with acute ischemic stroke"
    )
    assert inst.id == "example-stroke-alteplase-fatalICH"
    assert inst.relatedArtifact[0].label == "Emberson 2014"
    assert inst.relatedArtifact[0].type == "citation"
    assert (
        inst.relatedArtifact[0].url == "https://doi.org/10.1016/S0140-6736(14)60584-5"
    )
    assert inst.statistic[0].numberOfEvents == 91
    assert float(inst.statistic[0].quantity.value) == float(0.026835741669)
    assert inst.statistic[0].sampleSize.numberOfParticipants == 3391
    assert inst.statistic[0].sampleSize.numberOfStudies == 9
    assert inst.statistic[0].statisticType.coding[0].code == "C44256"
    assert inst.statistic[0].statisticType.coding[0].display == "Proportion"
    assert (
        inst.statistic[0].statisticType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/statistic-type"
    )
    assert inst.status == "draft"
    assert inst.studyType.coding[0].code == "RCT"
    assert inst.studyType.coding[0].display == "randomized trial"
    assert (
        inst.studyType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/study-type"
    )
    assert inst.synthesisType.coding[0].code == "IPD-MA"
    assert (
        inst.synthesisType.coding[0].display == "individual patient data meta-analysis"
    )
    assert (
        inst.synthesisType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/synthesis-type"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Risk of fatal ICH with alteplase for stroke"
    assert inst.url == (
        "http://hl7.org/fhir/Evidence/example-stroke-alteplase-" "fatalICH"
    )
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
    assert (
        inst.variableDefinition[0].intended.display
        == "adults with acute ischemic stroke"
    )
    assert inst.variableDefinition[0].intended.reference == "Group/AcuteIschemicStroke"
    assert inst.variableDefinition[0].intended.type == "Group"
    assert (
        inst.variableDefinition[0].observed.display
        == "adults with acute ischemic stroke"
    )
    assert inst.variableDefinition[0].observed.reference == "Group/AcuteIschemicStroke"
    assert inst.variableDefinition[0].observed.type == "Group"
    assert inst.variableDefinition[0].variableRole.coding[0].code == "population"
    assert inst.variableDefinition[0].variableRole.coding[0].display == "population"
    assert (
        inst.variableDefinition[0].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert (
        inst.variableDefinition[1].intended.display
        == "adults with acute ischemic stroke treated with alteplase"
    )
    assert (
        inst.variableDefinition[1].intended.reference
        == "Group/AcuteIschemicStrokeTreatedWithAlteplase"
    )
    assert inst.variableDefinition[1].intended.type == "Group"
    assert (
        inst.variableDefinition[1].observed.display
        == "Emberson 2014 IPD-MA Alteplase Cohort"
    )
    assert (
        inst.variableDefinition[1].observed.reference
        == "Group/Emberson-2014-IPD-MA-Alteplase-Cohort"
    )
    assert inst.variableDefinition[1].observed.type == "Group"
    assert inst.variableDefinition[1].variableRole.coding[0].code == "population"
    assert inst.variableDefinition[1].variableRole.coding[0].display == "population"
    assert (
        inst.variableDefinition[1].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert inst.variableDefinition[2].intended.display == "fatal ICH"
    assert (
        inst.variableDefinition[2].intended.reference
        == "EvidenceVariable/example-fatal-ICH-in-7-days"
    )
    assert inst.variableDefinition[2].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[2].observed.display == "fatal ICH"
    assert (
        inst.variableDefinition[2].observed.reference
        == "EvidenceVariable/example-fatal-ICH-in-7-days"
    )
    assert inst.variableDefinition[2].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[2].variableRole.coding[0].code == "measuredVariable"
    assert (
        inst.variableDefinition[2].variableRole.coding[0].display == "measured variable"
    )
    assert (
        inst.variableDefinition[2].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )


def test_evidence_4(base_settings):
    """No. 4 tests collection for Evidence.
    Test File: evidence-example-stroke-alteplase-fatalICH.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidence-example-stroke-alteplase-fatalICH.json"
    )
    inst = evidence.Evidence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Evidence" == inst.resource_type

    impl_evidence_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Evidence" == data["resourceType"]

    inst2 = evidence.Evidence(**data)
    impl_evidence_4(inst2)


def impl_evidence_5(inst):
    assert inst.certainty[0].rating.coding[0].code == "high"
    assert inst.certainty[0].rating.coding[0].display == "High quality"
    assert (
        inst.certainty[0].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[0].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[0].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[0].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[0].type.coding[0].code == "RiskOfBias"
    assert inst.certainty[0].subcomponent[0].type.coding[0].display == "Risk of bias"
    assert (
        inst.certainty[0].subcomponent[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[1].description == (
        "Estimated risk from validation calibration plot consistent "
        "with predicted risk; observed risk in subgroup with ASTRAL "
        "score = 12 consistent with validation calibration plot"
    )
    assert inst.certainty[0].subcomponent[1].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[1].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[1].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[1].type.coding[0].code == "Inconsistency"
    assert inst.certainty[0].subcomponent[1].type.coding[0].display == "Inconsistency"
    assert (
        inst.certainty[0].subcomponent[1].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[2].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[2].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[2].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[2].type.coding[0].code == "Indirectness"
    assert inst.certainty[0].subcomponent[2].type.coding[0].display == "Indirectness"
    assert (
        inst.certainty[0].subcomponent[2].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[3].description == "Narrow confidence interval"
    assert inst.certainty[0].subcomponent[3].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[3].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[3].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[3].type.coding[0].code == "Imprecision"
    assert inst.certainty[0].subcomponent[3].type.coding[0].display == "Imprecision"
    assert (
        inst.certainty[0].subcomponent[3].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].subcomponent[4].rating.coding[0].code == "no-concern"
    assert (
        inst.certainty[0].subcomponent[4].rating.coding[0].display
        == "no serious concern"
    )
    assert (
        inst.certainty[0].subcomponent[4].rating.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-rating"
    )
    assert inst.certainty[0].subcomponent[4].type.coding[0].code == "PublicationBias"
    assert (
        inst.certainty[0].subcomponent[4].type.coding[0].display == "Publication bias"
    )
    assert (
        inst.certainty[0].subcomponent[4].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.certainty[0].type.coding[0].code == "Overall"
    assert inst.certainty[0].type.coding[0].display == "Overall quality"
    assert (
        inst.certainty[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/certainty-type"
    )
    assert inst.description == "5.3% risk of mRS 3-6 at 90 days"
    assert inst.id == "example-ASTRAL-12-alteplase-mRS3-6"
    assert inst.relatedArtifact[0].display == (
        "External Validation of the ASTRAL and DRAGON Scores for "
        "Prediction of Functional Outcome in Stroke."
    )
    assert inst.relatedArtifact[0].label == "Cooray 2016 Validation Study"
    assert inst.relatedArtifact[0].type == "citation"
    assert inst.relatedArtifact[0].url == "https://doi.org/10.1161/STROKEAHA.116.012802"
    assert inst.statistic[0].description == "5.3% risk"
    assert float(inst.statistic[0].quantity.value) == float(0.0525)
    assert inst.statistic[0].sampleSize.numberOfParticipants == 36131
    assert inst.statistic[0].statisticType.coding[0].code == "C44256"
    assert inst.statistic[0].statisticType.coding[0].display == "Proportion"
    assert (
        inst.statistic[0].statisticType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/statistic-type"
    )
    assert inst.statistic[0].statisticType.text == "derived proportion"
    assert inst.status == "draft"
    assert inst.studyType.coding[0].code == "series"
    assert inst.studyType.coding[0].display == "uncontrolled cohort or case series"
    assert (
        inst.studyType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/study-type"
    )
    assert inst.text.status == "generated"
    assert inst.title == (
        "Risk of mRS3-6 at 90 days after Alteplase for Stroke if " "ASTRAL score 12"
    )
    assert inst.url == (
        "http://hl7.org/fhir/Evidence/example-ASTRAL-12-alteplase-" "mRS3-6"
    )
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == "http://terminology.hl7.org/CodeSystem/usage-context-type"
    )
    assert inst.useContext[0].valueCodeableConcept.text == "Stroke"
    assert inst.variableDefinition[0].intended.display == (
        "patients 0-4.5 hours after acute ischemic stroke onset with "
        "ASTRAL score = 12"
    )
    assert inst.variableDefinition[0].intended.reference == "Group/ASTRAL-12"
    assert inst.variableDefinition[0].intended.type == "Group"
    assert inst.variableDefinition[0].observed.display == "ASTRAL validation cohort"
    assert (
        inst.variableDefinition[0].observed.reference
        == "Group/ASTRAL-Cooray-validation-cohort"
    )
    assert inst.variableDefinition[0].observed.type == "Group"
    assert inst.variableDefinition[0].variableRole.coding[0].code == "population"
    assert inst.variableDefinition[0].variableRole.coding[0].display == "population"
    assert (
        inst.variableDefinition[0].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert (
        inst.variableDefinition[1].description
        == "functionally dependent or dead at 3 months"
    )
    assert inst.variableDefinition[1].directnessMatch.coding[0].code == "high"
    assert (
        inst.variableDefinition[1].directnessMatch.coding[0].display
        == "High quality match"
    )
    assert (
        inst.variableDefinition[1].directnessMatch.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/directness"
    )
    assert (
        inst.variableDefinition[1].intended.display
        == "Dead or functionally dependent at 90 days"
    )
    assert (
        inst.variableDefinition[1].intended.reference
        == "EvidenceVariable/example-dead-or-dependent-90day"
    )
    assert inst.variableDefinition[1].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[1].observed.display == "mRS 3-6 at 90 days"
    assert (
        inst.variableDefinition[1].observed.reference
        == "EvidenceVariable/example-mRS3-6-at-90days"
    )
    assert inst.variableDefinition[1].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[1].variableRole.coding[0].code == "measuredVariable"
    assert (
        inst.variableDefinition[1].variableRole.coding[0].display == "measured variable"
    )
    assert (
        inst.variableDefinition[1].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )
    assert inst.variableDefinition[2].directnessMatch.coding[0].code == "exact"
    assert inst.variableDefinition[2].directnessMatch.coding[0].display == "Exact match"
    assert (
        inst.variableDefinition[2].directnessMatch.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/directness"
    )
    assert inst.variableDefinition[2].intended.display == "Alteplase for Stroke"
    assert (
        inst.variableDefinition[2].intended.reference
        == "EvidenceVariable/example-alteplase-for-stroke"
    )
    assert inst.variableDefinition[2].intended.type == "EvidenceVariable"
    assert inst.variableDefinition[2].observed.display == "Alteplase for Stroke"
    assert (
        inst.variableDefinition[2].observed.reference
        == "EvidenceVariable/example-alteplase-for-stroke"
    )
    assert inst.variableDefinition[2].observed.type == "EvidenceVariable"
    assert inst.variableDefinition[2].variableRole.coding[0].code == "exposure"
    assert inst.variableDefinition[2].variableRole.coding[0].display == "exposure"
    assert (
        inst.variableDefinition[2].variableRole.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/variable-role"
    )


def test_evidence_5(base_settings):
    """No. 5 tests collection for Evidence.
    Test File: evidence-example-ASTRAL-12-alteplase-mRS3-6.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "evidence-example-ASTRAL-12-alteplase-mRS3-6.json"
    )
    inst = evidence.Evidence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Evidence" == inst.resource_type

    impl_evidence_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Evidence" == data["resourceType"]

    inst2 = evidence.Evidence(**data)
    impl_evidence_5(inst2)
