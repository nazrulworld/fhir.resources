# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ArtifactAssessment
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import artifactassessment
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_artifactassessment_1(inst):
    assert inst.artifactCanonical == "http://fevir.net/resources/Evidence/7637"
    assert inst.content[0].author.display == (
        "COVID-19 Knowledge Accelerator Evidence 7637 Authors (Brian "
        "S. Alper, Harold Lehmann, Ahmad Sofi-Mahmudi, Joanne "
        "Dehnbostel, Ilkka Kunnamo)"
    )
    assert inst.content[0].classifier[0].coding[0].code == "extremely-serious-concern"
    assert (
        inst.content[0].classifier[0].coding[0].display == "extremely serious concern"
    )
    assert (
        inst.content[0].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].classifier[0].coding[0].userSelected is True
    assert inst.content[0].classifier[0].coding[0].version == "5.0.0"
    assert (
        inst.content[0].component[0].author.display
        == "Brian S. Alper, Joanne Dehnbostel, Muhammad Afzal"
    )
    assert inst.content[0].component[0].classifier[0].coding[0].code == "no-concern"
    assert (
        inst.content[0].component[0].classifier[0].coding[0].display
        == "no serious concern"
    )
    assert (
        inst.content[0].component[0].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[0].classifier[0].coding[0].userSelected is True
    assert inst.content[0].component[0].classifier[0].coding[0].version == "5.0.0"
    assert inst.content[0].component[0].summary == (
        "Inclusion of suspected COVID-19 in 1 of 3 trials may "
        "introduce selection bias, but the impact appears limited."
    )
    assert inst.content[0].component[0].type.text == "Selection Bias"
    assert inst.content[0].component[1].author.display == (
        "Brian S. Alper, Ilkka Kunnamo, Alfonso Iorio, Joanne "
        "Dehnbostel, Harold Lehmann, Kenneth Wilkins; clarifying "
        "explanation reviewed by Janice Tufte"
    )
    assert (
        inst.content[0].component[1].classifier[0].coding[0].code == "serious-concern"
    )
    assert (
        inst.content[0].component[1].classifier[0].coding[0].display
        == "serious concern"
    )
    assert (
        inst.content[0].component[1].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[1].classifier[0].coding[0].userSelected is True
    assert inst.content[0].component[1].classifier[0].coding[0].version == "5.0.0"
    assert inst.content[0].component[1].component[3].author.display == (
        "Brian S. Alper, Joanne Dehnbostel, Harold Lehmann, Kenneth " "Wilkins"
    )
    assert inst.content[0].component[1].component[3].classifier[0].text == (
        "Adaptive randomization is not a concern by itself, only if "
        "it results in a confounding difference."
    )
    assert inst.content[0].component[1].component[3].component[0].summary == (
        "Definition of Allocation Bias = A confounding covariate bias"
        " resulting from methods for assignment of the independent "
        "variable by the investigator to evaluate a response or "
        "outcome."
    )
    assert inst.content[0].component[1].component[3].component[1].summary == (
        "ATTACC implemented response-adaptive randomization on "
        "December 15, 2020, which led to imbalanced randomization."
    )
    assert inst.content[0].component[1].component[3].summary == (
        "Response-adaptive randomization led to imbalanced " "randomization."
    )
    assert inst.content[0].component[1].component[3].type.text == "Allocation Bias"
    assert inst.content[0].component[1].component[4].author.display == (
        "Brian S. Alper, Joanne Dehnbostel, Harold Lehmann, Kenneth " "Wilkins"
    )
    assert (
        inst.content[0].component[1].component[4].classifier[0].coding[0].code
        == "serious-concern"
    )
    assert (
        inst.content[0].component[1].component[4].classifier[0].coding[0].display
        == "serious concern"
    )
    assert (
        inst.content[0].component[1].component[4].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert (
        inst.content[0].component[1].component[4].classifier[0].coding[0].userSelected
        is True
    )
    assert (
        inst.content[0].component[1].component[4].classifier[0].coding[0].version
        == "5.0.0"
    )
    assert inst.content[0].component[1].component[4].component[0].summary == (
        "Definition of Confounding difference = A confounding "
        "covariate bias in which the unequal distribution of a "
        "potentially distorting variable is recognized."
    )
    assert inst.content[0].component[1].component[4].component[1].summary == (
        "Incomplete reporting limits the determination of the "
        "potential degree of influence of calendar time."
    )
    assert inst.content[0].component[1].component[4].summary == (
        "There is an unequal distribution of calendar time between "
        "the groups being compared."
    )
    assert (
        inst.content[0].component[1].component[4].type.text == "Confounding difference"
    )
    assert inst.content[0].component[1].type.text == "Confounding Covariate Bias"
    assert inst.content[0].component[2].author.display == (
        "Brian S. Alper, Joanne Dehnbostel, Harold Lehmann, Muhammad " "Afzal"
    )
    assert (
        inst.content[0].component[2].classifier[0].coding[0].code
        == "very-serious-concern"
    )
    assert (
        inst.content[0].component[2].classifier[0].coding[0].display
        == "very serious concern"
    )
    assert (
        inst.content[0].component[2].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[2].classifier[0].coding[0].userSelected is True
    assert inst.content[0].component[2].classifier[0].coding[0].version == "5.0.0"
    assert inst.content[0].component[2].component[0].summary == (
        "Definition of Performance Bias = A bias resulting from "
        "differences between the received exposure and the intended "
        "exposure."
    )
    assert inst.content[0].component[2].component[1].author.display == (
        "Brian S. Alper; clarifying explanation reviewed by Janice " "Tufte"
    )
    assert (
        inst.content[0].component[2].component[1].classifier[0].coding[0].code
        == "very-serious-concern"
    )
    assert (
        inst.content[0].component[2].component[1].classifier[0].coding[0].display
        == "very serious concern"
    )
    assert (
        inst.content[0].component[2].component[1].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert (
        inst.content[0].component[2].component[1].classifier[0].coding[0].userSelected
        is True
    )
    assert (
        inst.content[0].component[2].component[1].classifier[0].coding[0].version
        == "5.0.0"
    )
    assert inst.content[0].component[2].component[1].component[0].summary == (
        "The absolute difference in survival without intubation was "
        "1%, so 3% of the 4% absolute difference in the primary "
        'outcome can be considered "organ support without '
        'intubation".'
    )
    assert inst.content[0].component[2].component[1].component[2].summary == (
        "Awareness of treatment assignment may reduce clinical "
        'decision to initiate "organ support without intubation" in'
        " patients with higher risk of major bleeding."
    )
    assert inst.content[0].component[2].component[1].component[3].summary == (
        "Definition of Inadequate blinding of intervention deliverers"
        " = A performance bias due to awareness of the allocated "
        "intervention by individuals providing or delivering the "
        "intervention."
    )
    assert inst.content[0].component[2].component[1].summary == (
        "Lack of blinding may explain reported differences in the " "primary outcome."
    )
    assert (
        inst.content[0].component[2].component[1].type.text
        == "Inadequate blinding of intervention deliverers"
    )
    assert (
        inst.content[0].component[2].component[2].author.display
        == "Surbhi Shah, Brian S. Alper"
    )
    assert (
        inst.content[0].component[2].component[2].classifier[0].text
        == "degree of concern unclear"
    )
    assert inst.content[0].component[2].component[2].component[0].summary == (
        "Therapeutic dose anticoagulation (in the first 24-48 hours "
        "following randomization) was reported in 79.6% of the "
        "therapeutic arm and 0.9% of the usual care arm. (Table S3)"
    )
    assert inst.content[0].component[2].component[2].component[1].summary == (
        "Definition of Deviation from study intervention protocol = A"
        " performance bias in which the intervention received differs"
        " from the intervention specified in the study protocol."
    )
    assert (
        inst.content[0].component[2].component[2].summary
        == "Crossover to other intervention in 20%"
    )
    assert (
        inst.content[0].component[2].component[2].type.text
        == "Deviation from study intervention protocol"
    )
    assert inst.content[0].component[2].component[3].author.display == (
        "COVID-19 Knowledge Accelerator Working Group discussion with"
        " Brian S. Alper, Ilkka Kunnamo, Joanne Dehnbostel; "
        "Performance Bias concern initially suggested by Harold "
        "Lehmann"
    )
    assert (
        inst.content[0].component[2].component[3].classifier[0].text
        == "limited concern"
    )
    assert inst.content[0].component[2].component[3].component[0].summary == (
        "Initial adherence to the protocol-assigned anticoagulation "
        "dose after randomization was 88.3% in the therapeutic-dose "
        "anticoagulation group and 98.3% in the thromboprophylaxis "
        "group (Table S3)."
    )
    assert inst.content[0].component[2].component[3].component[1].summary == (
        "Definition of Nonadherence of implementation = A performance"
        " bias in which the intervention deliverers do not completely"
        " adhere to the expected intervention."
    )
    assert (
        inst.content[0].component[2].component[3].type.text
        == "Nonadherence of implementation"
    )
    assert inst.content[0].component[2].summary == (
        "Awareness of treatment assignment may reduce clinical "
        'decision to initiate some types of "organ support" in '
        "patients with higher risk of major bleeding."
    )
    assert inst.content[0].component[2].type.text == "Performance Bias"
    assert (
        inst.content[0].component[3].author.display
        == "Brian S. Alper, Joanne Dehnbostel, Muhammad Afzal"
    )
    assert inst.content[0].component[3].classifier[0].coding[0].code == "no-concern"
    assert (
        inst.content[0].component[3].classifier[0].coding[0].display
        == "no serious concern"
    )
    assert (
        inst.content[0].component[3].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[3].classifier[0].coding[0].userSelected is True
    assert inst.content[0].component[3].classifier[0].coding[0].version == "5.0.0"
    assert inst.content[0].component[3].component[0].summary == (
        "Definition of Detection Bias = A bias due to distortions in "
        "how variable values (data) are determined."
    )
    assert inst.content[0].component[3].type.text == "Detection Bias"
    assert (
        inst.content[0].component[4].author.display
        == "Brian S. Alper, Joanne Dehnbostel, Muhammad Afzal"
    )
    assert inst.content[0].component[4].classifier[0].coding[0].code == "no-concern"
    assert (
        inst.content[0].component[4].classifier[0].coding[0].display
        == "no serious concern"
    )
    assert (
        inst.content[0].component[4].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[4].classifier[0].coding[0].userSelected is True
    assert inst.content[0].component[4].classifier[0].coding[0].version == "5.0.0"
    assert inst.content[0].component[4].component[0].summary == (
        "Definition of Attrition Bias = A bias due to absence of "
        "expected participation or data collection after selection "
        "for study inclusion."
    )
    assert inst.content[0].component[4].summary == (
        "Only 19 of 1190 (1.6%) therapeutic group and 6 of 1054 (0.6)"
        " prophylactic group were excluded after randomization."
    )
    assert inst.content[0].component[4].type.text == "Attrition Bias"
    assert inst.content[0].component[5].author.display == (
        "Brian S. Alper, Joanne Dehnbostel, Muhammad Afzal, Janice " "Tufte"
    )
    assert (
        inst.content[0].component[5].classifier[0].coding[0].code
        == "very-serious-concern"
    )
    assert (
        inst.content[0].component[5].classifier[0].coding[0].display
        == "very serious concern"
    )
    assert (
        inst.content[0].component[5].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[5].classifier[0].coding[0].userSelected is True
    assert inst.content[0].component[5].classifier[0].coding[0].version == "5.0.0"
    assert inst.content[0].component[5].component[0].summary == (
        "Definition of Analysis Bias = A bias related to the analytic"
        " process applied to the data."
    )
    assert inst.content[0].component[5].component[1].author.display == (
        "Brian S. Alper, Joanne Dehnbostel, Muhammad Afzal, Janice " "Tufte"
    )
    assert (
        inst.content[0].component[5].component[1].classifier[0].coding[0].code
        == "very-serious-concern"
    )
    assert (
        inst.content[0].component[5].component[1].classifier[0].coding[0].display
        == "very serious concern"
    )
    assert (
        inst.content[0].component[5].component[1].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert (
        inst.content[0].component[5].component[1].classifier[0].coding[0].userSelected
        is True
    )
    assert (
        inst.content[0].component[5].component[1].classifier[0].coding[0].version
        == "5.0.0"
    )
    assert inst.content[0].component[5].component[1].component[0].summary == (
        "Definition of Bias related to selection of the analysis = An"
        " analysis bias due to inappropriate choice of analysis "
        "methods before the analysis is applied."
    )
    assert inst.content[0].component[5].component[1].component[1].summary == (
        "There was no pre-specified frequentist analysis. There was "
        "no posthoc frequentist analysis reported."
    )
    assert inst.content[0].component[5].component[1].component[2].summary == (
        "It is uncertain what a frequentist analysis would show and "
        "uncertain whether the choice of Bayesian analysis or "
        "frequentist analysis has a substantial influence on the "
        "results."
    )
    assert inst.content[0].component[5].component[1].summary == (
        "A frequentist analysis is not reported so we cannot "
        "determine if the results are sensitive to the analytic "
        "method"
    )
    assert (
        inst.content[0].component[5].component[1].type.text
        == "Bias related to selection of the analysis"
    )
    assert inst.content[0].component[5].component[2].author.display == (
        "Brian S. Alper, Joanne Dehnbostel, Muhammad Afzal, Janice " "Tufte"
    )
    assert (
        inst.content[0].component[5].component[2].classifier[0].coding[0].code
        == "very-serious-concern"
    )
    assert (
        inst.content[0].component[5].component[2].classifier[0].coding[0].display
        == "very serious concern"
    )
    assert (
        inst.content[0].component[5].component[2].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert (
        inst.content[0].component[5].component[2].classifier[0].coding[0].userSelected
        is True
    )
    assert (
        inst.content[0].component[5].component[2].classifier[0].coding[0].version
        == "5.0.0"
    )
    assert inst.content[0].component[5].component[2].component[0].summary == (
        "There was no “minimally important difference”. So a 99% "
        "probability of having an odds ratio > 1 (even if the "
        "magnitude of effect is infinitesimal) was used to decide it "
        "was time to stop the trial."
    )
    assert inst.content[0].component[5].component[2].summary == (
        "The stopping criteria were based on statistical significance"
        " and not magnitude of effect."
    )
    assert (
        inst.content[0].component[5].component[2].type.text == "Early trial termination"
    )
    assert inst.content[0].component[5].summary == (
        "It is unknown if the results are sensitive to the analytic "
        "method, and the stopping criteria were based on statistical "
        "significance and not magnitude of effect."
    )
    assert inst.content[0].component[5].type.text == "Analysis Bias"
    assert inst.content[0].freeToShare is True
    assert inst.content[0].informationType == "rating"
    assert inst.content[0].type.coding[0].code == "RiskOfBias"
    assert inst.content[0].type.coding[0].display == "Risk of bias"
    assert (
        inst.content[0].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-type"
        ).valueUri
    )
    assert inst.content[0].type.coding[0].userSelected is True
    assert inst.content[0].type.coding[0].version == "5.0.0"
    assert inst.content[1].author.display == "Ilkka Kunnamo"
    assert inst.content[1].informationType == "comment"
    assert (
        inst.content[1].summary == "Results not consistent with critically ill cohort."
    )
    assert inst.content[1].type.coding[0].code == "Inconsistency"
    assert inst.content[1].type.coding[0].display == "Inconsistency"
    assert (
        inst.content[1].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-type"
        ).valueUri
    )
    assert inst.content[1].type.coding[0].userSelected is True
    assert inst.content[1].type.coding[0].version == "5.0.0"
    assert inst.copyright == "https://creativecommons.org/licenses/by-nc-sa/4.0/"
    assert (
        inst.date
        == ExternalValidatorModel(
            valueDateTime="2021-11-02T14:31:30.239Z"
        ).valueDateTime
    )
    assert inst.id == "risk-of-bias-example"
    assert inst.identifier[0].assigner.display == "Computable Publishing LLC"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="https://fevir.net").valueUri
    )
    assert inst.identifier[0].type.text == "FEvIR Object Identifier"
    assert inst.identifier[0].value == "27751"
    assert (
        inst.lastReviewDate == ExternalValidatorModel(valueDate="2021-08-11").valueDate
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_artifactassessment_1(base_settings):
    """No. 1 tests collection for ArtifactAssessment.
    Test File: artifactassessment-risk-of-bias-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "artifactassessment-risk-of-bias-example.json"
    )
    inst = artifactassessment.ArtifactAssessment.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "ArtifactAssessment" == inst.get_resource_type()

    impl_artifactassessment_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ArtifactAssessment" == data["resourceType"]

    inst2 = artifactassessment.ArtifactAssessment(**data)
    impl_artifactassessment_1(inst2)


def impl_artifactassessment_2(inst):
    assert inst.artifactReference.display == (
        "Critically appraised summary of all-cause mortality in meta-"
        "analysis of RCTs of heparin for moderately ill patients with"
        " COVID-19"
    )
    assert inst.artifactReference.reference == "Evidence/18812"
    assert (
        inst.artifactReference.type
        == ExternalValidatorModel(valueUri="Evidence").valueUri
    )
    assert inst.content[0].author.display == "Brian S. Alper"
    assert inst.content[0].classifier[0].coding[0].code == "very-low"
    assert inst.content[0].classifier[0].coding[0].display == "Very low quality"
    assert (
        inst.content[0].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[0].author.display == "Brian S. Alper"
    assert (
        inst.content[0].component[0].classifier[0].coding[0].code == "serious-concern"
    )
    assert (
        inst.content[0].component[0].classifier[0].coding[0].display
        == "serious concern"
    )
    assert (
        inst.content[0].component[0].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[0].informationType == "rating"
    assert (
        inst.content[0].component[0].summary == "risk of bias in both included trials"
    )
    assert inst.content[0].component[0].type.coding[0].code == "RiskOfBias"
    assert inst.content[0].component[0].type.coding[0].display == "Risk of bias"
    assert (
        inst.content[0].component[0].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-type"
        ).valueUri
    )
    assert inst.content[0].component[1].author.display == "Brian S. Alper"
    assert (
        inst.content[0].component[1].classifier[0].coding[0].code == "serious-concern"
    )
    assert (
        inst.content[0].component[1].classifier[0].coding[0].display
        == "serious concern"
    )
    assert (
        inst.content[0].component[1].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[1].informationType == "rating"
    assert inst.content[0].component[1].summary == (
        "high degree of heterogeneity (I-squared 80.7%) with "
        "confidence intervals of 2 trial effect estimates barely "
        "overlapping"
    )
    assert inst.content[0].component[1].type.coding[0].code == "Inconsistency"
    assert inst.content[0].component[1].type.coding[0].display == "Inconsistency"
    assert (
        inst.content[0].component[1].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-type"
        ).valueUri
    )
    assert inst.content[0].component[2].author.display == "Brian S. Alper"
    assert inst.content[0].component[2].classifier[0].coding[0].code == "no-concern"
    assert (
        inst.content[0].component[2].classifier[0].coding[0].display
        == "no serious concern"
    )
    assert (
        inst.content[0].component[2].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[2].informationType == "rating"
    assert inst.content[0].component[2].type.coding[0].code == "Indirectness"
    assert inst.content[0].component[2].type.coding[0].display == "Indirectness"
    assert (
        inst.content[0].component[2].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-type"
        ).valueUri
    )
    assert inst.content[0].component[3].author.display == "Brian S. Alper"
    assert (
        inst.content[0].component[3].classifier[0].coding[0].code == "serious-concern"
    )
    assert (
        inst.content[0].component[3].classifier[0].coding[0].display
        == "serious concern"
    )
    assert (
        inst.content[0].component[3].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[3].informationType == "rating"
    assert inst.content[0].component[3].summary == (
        "95% confidence interval includes both large effects and no " "effects"
    )
    assert inst.content[0].component[3].type.coding[0].code == "Imprecision"
    assert inst.content[0].component[3].type.coding[0].display == "Imprecision"
    assert (
        inst.content[0].component[3].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-type"
        ).valueUri
    )
    assert inst.content[0].component[4].author.display == "Brian S. Alper"
    assert inst.content[0].component[4].classifier[0].coding[0].code == "no-concern"
    assert (
        inst.content[0].component[4].classifier[0].coding[0].display
        == "no serious concern"
    )
    assert (
        inst.content[0].component[4].classifier[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-rating"
        ).valueUri
    )
    assert inst.content[0].component[4].informationType == "rating"
    assert inst.content[0].component[4].type.coding[0].code == "PublicationBias"
    assert inst.content[0].component[4].type.coding[0].display == "Publication bias"
    assert (
        inst.content[0].component[4].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-type"
        ).valueUri
    )
    assert inst.content[0].freeToShare is True
    assert inst.content[0].informationType == "rating"
    assert inst.content[0].summary == (
        "serious concerns with risk of bias, inconsistency, and " "imprecision"
    )
    assert inst.content[0].type.coding[0].code == "Overall"
    assert inst.content[0].type.coding[0].display == "Overall certainty"
    assert (
        inst.content[0].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/certainty-type"
        ).valueUri
    )
    assert inst.copyright == "https://creativecommons.org/licenses/by-nc-sa/4.0/"
    assert (
        inst.date
        == ExternalValidatorModel(
            valueDateTime="2021-11-02T14:48:59.890Z"
        ).valueDateTime
    )
    assert inst.id == "example-certainty-rating"
    assert inst.identifier[0].assigner.display == "Computable Publishing LLC"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="https://fevir.net").valueUri
    )
    assert inst.identifier[0].type.text == "FEvIR Object Identifier"
    assert inst.identifier[0].value == "27756"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_artifactassessment_2(base_settings):
    """No. 2 tests collection for ArtifactAssessment.
    Test File: artifactassessment-example-certainty-rating.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "artifactassessment-example-certainty-rating.json"
    )
    inst = artifactassessment.ArtifactAssessment.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "ArtifactAssessment" == inst.get_resource_type()

    impl_artifactassessment_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ArtifactAssessment" == data["resourceType"]

    inst2 = artifactassessment.ArtifactAssessment(**data)
    impl_artifactassessment_2(inst2)
