# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class EffectEvidenceSynthesis(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A quantified estimate of effect based on a body of evidence.
    The EffectEvidenceSynthesis resource describes the difference in an outcome
    between exposures states in a population where the effect estimate is
    derived from a combination of research studies.
    """

    resource_type = Field("EffectEvidenceSynthesis", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date`",
        description="When the effect evidence synthesis was approved by publisher",
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

    certainty: ListType[fhirtypes.EffectEvidenceSynthesisCertaintyType] = Field(
        None,
        alias="certainty",
        title=(
            "List of `EffectEvidenceSynthesisCertainty` items (represented as "
            "`dict` in JSON)"
        ),
        description="How certain is the effect",
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
        description="Natural language description of the effect evidence synthesis",
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

    effectEstimate: ListType[
        fhirtypes.EffectEvidenceSynthesisEffectEstimateType
    ] = Field(
        None,
        alias="effectEstimate",
        title=(
            "List of `EffectEvidenceSynthesisEffectEstimate` items (represented as "
            "`dict` in JSON)"
        ),
        description="What was the estimated effect",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the effect evidence synthesis is expected to be used",
    )

    endorser: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who endorsed the content",
    )

    exposure: fhirtypes.ReferenceType = Field(
        ...,
        alias="exposure",
        title=(
            "Type `Reference` referencing `EvidenceVariable` (represented as `dict`"
            " in JSON)"
        ),
        description="What exposure?",
    )

    exposureAlternative: fhirtypes.ReferenceType = Field(
        ...,
        alias="exposureAlternative",
        title=(
            "Type `Reference` referencing `EvidenceVariable` (represented as `dict`"
            " in JSON)"
        ),
        description="What comparison exposure?",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the effect evidence synthesis",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for effect evidence synthesis (if applicable)",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date`",
        description="When the effect evidence synthesis was last reviewed",
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this effect evidence synthesis (computer friendly)",
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

    resultsByExposure: ListType[
        fhirtypes.EffectEvidenceSynthesisResultsByExposureType
    ] = Field(
        None,
        alias="resultsByExposure",
        title=(
            "List of `EffectEvidenceSynthesisResultsByExposure` items (represented "
            "as `dict` in JSON)"
        ),
        description="What was the result per exposure?",
    )

    reviewer: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who reviewed the content",
    )

    sampleSize: fhirtypes.EffectEvidenceSynthesisSampleSizeType = Field(
        None,
        alias="sampleSize",
        title=(
            "Type `EffectEvidenceSynthesisSampleSize` (represented as `dict` in "
            "JSON)"
        ),
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
        description="Name for this effect evidence synthesis (human friendly)",
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
            "Canonical identifier for this effect evidence synthesis, represented "
            "as a URI (globally unique)"
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
        description="Business version of the effect evidence synthesis",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class EffectEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How certain is the effect.
    A description of the certainty of the effect estimate.
    """

    resource_type = Field("EffectEvidenceSynthesisCertainty", const=True)

    certaintySubcomponent: ListType[
        fhirtypes.EffectEvidenceSynthesisCertaintyCertaintySubcomponentType
    ] = Field(
        None,
        alias="certaintySubcomponent",
        title=(
            "List of `EffectEvidenceSynthesisCertaintyCertaintySubcomponent` items "
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


class EffectEvidenceSynthesisCertaintyCertaintySubcomponent(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A component that contributes to the overall certainty.
    A description of a component of the overall certainty.
    """

    resource_type = Field(
        "EffectEvidenceSynthesisCertaintyCertaintySubcomponent", const=True
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


class EffectEvidenceSynthesisEffectEstimate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What was the estimated effect.
    The estimated effect of the exposure variant.
    """

    resource_type = Field("EffectEvidenceSynthesisEffectEstimate", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Description of effect estimate",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    precisionEstimate: ListType[
        fhirtypes.EffectEvidenceSynthesisEffectEstimatePrecisionEstimateType
    ] = Field(
        None,
        alias="precisionEstimate",
        title=(
            "List of `EffectEvidenceSynthesisEffectEstimatePrecisionEstimate` items"
            " (represented as `dict` in JSON)"
        ),
        description="How precise the estimate is",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of efffect estimate",
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

    variantState: fhirtypes.CodeableConceptType = Field(
        None,
        alias="variantState",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Variant exposure states",
    )


class EffectEvidenceSynthesisEffectEstimatePrecisionEstimate(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How precise the estimate is.
    A description of the precision of the estimate for the effect.
    """

    resource_type = Field(
        "EffectEvidenceSynthesisEffectEstimatePrecisionEstimate", const=True
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


class EffectEvidenceSynthesisResultsByExposure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What was the result per exposure?.
    A description of the results for each exposure considered in the effect
    estimate.
    """

    resource_type = Field("EffectEvidenceSynthesisResultsByExposure", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Description of results by exposure",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    exposureState: fhirtypes.Code = Field(
        None,
        alias="exposureState",
        title="Type `Code`",
        description="exposure | exposure-alternative",
    )
    exposureState__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exposureState", title="Extension field for ``exposureState``."
    )

    riskEvidenceSynthesis: fhirtypes.ReferenceType = Field(
        ...,
        alias="riskEvidenceSynthesis",
        title=(
            "Type `Reference` referencing `RiskEvidenceSynthesis` (represented as "
            "`dict` in JSON)"
        ),
        description="Risk evidence synthesis",
    )

    variantState: fhirtypes.CodeableConceptType = Field(
        None,
        alias="variantState",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Variant exposure states",
    )


class EffectEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What sample size was involved?.
    A description of the size of the sample involved in the synthesis.
    """

    resource_type = Field("EffectEvidenceSynthesisSampleSize", const=True)

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
