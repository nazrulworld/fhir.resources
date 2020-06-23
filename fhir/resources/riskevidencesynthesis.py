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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A quantified estimate of risk based on a body of evidence.
    The RiskEvidenceSynthesis resource describes the likelihood of an outcome
    in a population plus exposure state where the risk estimate is derived from
    a combination of research studies.
    """

    resource_type = Field("RiskEvidenceSynthesis", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date`",
        description="When the risk evidence synthesis was approved by publisher",
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
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
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None, alias="date", title="Type `DateTime`", description="Date last changed"
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the risk evidence synthesis",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
        title="Type `Date`",
        description="When the risk evidence synthesis was last reviewed",
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this risk evidence synthesis (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
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
        title="Type `String`",
        description="Name of the publisher (organization or individual)",
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
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
        title="Type `Code`",
        description="draft | active | retired | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
        title="Type `String`",
        description="Name for this risk evidence synthesis (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
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
        title="Type `Uri`",
        description=(
            "Canonical identifier for this risk evidence synthesis, represented as "
            "a URI (globally unique)"
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
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
        title="Type `String`",
        description="Business version of the risk evidence synthesis",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class RiskEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How certain is the risk.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A component that contributes to the overall certainty.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What was the estimated risk.
    The estimated risk of the outcome.
    """

    resource_type = Field("RiskEvidenceSynthesisRiskEstimate", const=True)

    denominatorCount: fhirtypes.Integer = Field(
        None,
        alias="denominatorCount",
        title="Type `Integer`",
        description="Sample size for group measured",
    )
    denominatorCount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_denominatorCount",
        title="Extension field for ``denominatorCount``.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Description of risk estimate",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    numeratorCount: fhirtypes.Integer = Field(
        None,
        alias="numeratorCount",
        title="Type `Integer`",
        description="Number with the outcome",
    )
    numeratorCount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numeratorCount", title="Extension field for ``numeratorCount``."
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
        None, alias="value", title="Type `Decimal`", description="Point estimate"
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How precise the estimate is.
    A description of the precision of the estimate for the effect.
    """

    resource_type = Field(
        "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate", const=True
    )

    from_fhir: fhirtypes.Decimal = Field(
        None, alias="from", title="Type `Decimal`", description="Lower bound"
    )
    from__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_from", title="Extension field for ``from_fhir``."
    )

    level: fhirtypes.Decimal = Field(
        None,
        alias="level",
        title="Type `Decimal`",
        description="Level of confidence interval",
    )
    level__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_level", title="Extension field for ``level``."
    )

    to: fhirtypes.Decimal = Field(
        None, alias="to", title="Type `Decimal`", description="Upper bound"
    )
    to__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_to", title="Extension field for ``to``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of precision estimate",
    )


class RiskEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What sample size was involved?.
    A description of the size of the sample involved in the synthesis.
    """

    resource_type = Field("RiskEvidenceSynthesisSampleSize", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Description of sample size",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    numberOfParticipants: fhirtypes.Integer = Field(
        None,
        alias="numberOfParticipants",
        title="Type `Integer`",
        description="How many participants?",
    )
    numberOfParticipants__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfParticipants",
        title="Extension field for ``numberOfParticipants``.",
    )

    numberOfStudies: fhirtypes.Integer = Field(
        None,
        alias="numberOfStudies",
        title="Type `Integer`",
        description="How many studies?",
    )
    numberOfStudies__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfStudies", title="Extension field for ``numberOfStudies``."
    )
