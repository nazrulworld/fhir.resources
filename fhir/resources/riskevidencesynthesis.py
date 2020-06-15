# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class RiskEvidenceSynthesis(domainresource.DomainResource):
    """ A quantified estimate of risk based on a body of evidence.
    The RiskEvidenceSynthesis resource describes the likelihood of an outcome
    in a population plus exposure state where the risk estimate is derived from
    a combination of research studies.
    """

    resource_type = Field("RiskEvidenceSynthesis", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the risk evidence synthesis was approved by publisher",
    )

    author: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who authored the content",
    )

    certainty: ListType[fhirtypes.RiskEvidenceSynthesisCertaintyType] = Field(
        None,
        alias="certainty",
        title=(
            "List of `RiskEvidenceSynthesisCertainty` items (represented as `dict` "
            "in JSON)"
        ),
        description="How certain is the risk",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the risk evidence synthesis",
    )

    editor: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="editor",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who edited the content",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the risk evidence synthesis is expected to be used",
    )

    endorser: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who endorsed the content",
    )

    exposure: fhirtypes.ReferenceType = Field(
        None,
        alias="exposure",
        title=(
            "Type `Reference` referencing `EvidenceVariable` (represented as `dict`"
            " in JSON)"
        ),
        description="What exposure?",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the risk evidence synthesis",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for risk evidence synthesis (if applicable)",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the risk evidence synthesis was last reviewed",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this risk evidence synthesis (computer friendly)",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Used for footnotes or explanatory notes",
    )

    outcome: fhirtypes.ReferenceType = Field(
        ...,
        alias="outcome",
        title=(
            "Type `Reference` referencing `EvidenceVariable` (represented as `dict`"
            " in JSON)"
        ),
        description="What outcome?",
    )

    population: fhirtypes.ReferenceType = Field(
        ...,
        alias="population",
        title=(
            "Type `Reference` referencing `EvidenceVariable` (represented as `dict`"
            " in JSON)"
        ),
        description="What population?",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    relatedArtifact: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="Additional documentation, citations, etc.",
    )

    reviewer: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who reviewed the content",
    )

    riskEstimate: fhirtypes.RiskEvidenceSynthesisRiskEstimateType = Field(
        None,
        alias="riskEstimate",
        title=(
            "Type `RiskEvidenceSynthesisRiskEstimate` (represented as `dict` in "
            "JSON)"
        ),
        description="What was the estimated risk",
    )

    sampleSize: fhirtypes.RiskEvidenceSynthesisSampleSizeType = Field(
        None,
        alias="sampleSize",
        title="Type `RiskEvidenceSynthesisSampleSize` (represented as `dict` in JSON)",
        description="What sample size was involved?",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    studyType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="studyType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of study",
    )

    synthesisType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="synthesisType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of synthesis",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this risk evidence synthesis (human friendly)",
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "The category of the EffectEvidenceSynthesis, such as Education, "
            "Treatment, Assessment, etc."
        ),
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this risk evidence synthesis, represented as "
            "a URI (globally unique)"
        ),
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the risk evidence synthesis",
    )


class RiskEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """ How certain is the risk.
    A description of the certainty of the risk estimate.
    """

    resource_type = Field("RiskEvidenceSynthesisCertainty", const=True)

    certaintySubcomponent: ListType[
        fhirtypes.RiskEvidenceSynthesisCertaintyCertaintySubcomponentType
    ] = Field(
        None,
        alias="certaintySubcomponent",
        title=(
            "List of `RiskEvidenceSynthesisCertaintyCertaintySubcomponent` items "
            "(represented as `dict` in JSON)"
        ),
        description="A component that contributes to the overall certainty",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Used for footnotes or explanatory notes",
    )

    rating: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="rating",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Certainty rating",
    )


class RiskEvidenceSynthesisCertaintyCertaintySubcomponent(
    backboneelement.BackboneElement
):
    """ A component that contributes to the overall certainty.
    A description of a component of the overall certainty.
    """

    resource_type = Field(
        "RiskEvidenceSynthesisCertaintyCertaintySubcomponent", const=True
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Used for footnotes or explanatory notes",
    )

    rating: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="rating",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Subcomponent certainty rating",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of subcomponent of certainty rating",
    )


class RiskEvidenceSynthesisRiskEstimate(backboneelement.BackboneElement):
    """ What was the estimated risk.
    The estimated risk of the outcome.
    """

    resource_type = Field("RiskEvidenceSynthesisRiskEstimate", const=True)

    denominatorCount: fhirtypes.Integer = Field(
        None,
        alias="denominatorCount",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Sample size for group measured",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of risk estimate",
    )

    numeratorCount: fhirtypes.Integer = Field(
        None,
        alias="numeratorCount",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Number with the outcome",
    )

    precisionEstimate: ListType[
        fhirtypes.RiskEvidenceSynthesisRiskEstimatePrecisionEstimateType
    ] = Field(
        None,
        alias="precisionEstimate",
        title=(
            "List of `RiskEvidenceSynthesisRiskEstimatePrecisionEstimate` items "
            "(represented as `dict` in JSON)"
        ),
        description="How precise the estimate is",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of risk estimate",
    )

    unitOfMeasure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unitOfMeasure",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What unit is the outcome described in?",
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Point estimate",
    )


class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(
    backboneelement.BackboneElement
):
    """ How precise the estimate is.
    A description of the precision of the estimate for the effect.
    """

    resource_type = Field(
        "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate", const=True
    )

    from_fhir: fhirtypes.Decimal = Field(
        None,
        alias="from",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Lower bound",
    )

    level: fhirtypes.Decimal = Field(
        None,
        alias="level",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Level of confidence interval",
    )

    to: fhirtypes.Decimal = Field(
        None,
        alias="to",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Upper bound",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of precision estimate",
    )


class RiskEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """ What sample size was involved?.
    A description of the size of the sample involved in the synthesis.
    """

    resource_type = Field("RiskEvidenceSynthesisSampleSize", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of sample size",
    )

    numberOfParticipants: fhirtypes.Integer = Field(
        None,
        alias="numberOfParticipants",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="How many participants?",
    )

    numberOfStudies: fhirtypes.Integer = Field(
        None,
        alias="numberOfStudies",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="How many studies?",
    )
