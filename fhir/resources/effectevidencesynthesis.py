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
        title="When the effect evidence synthesis was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    author: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual or organization primarily involved in the creation and "
            "maintenance of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    certainty: ListType[fhirtypes.EffectEvidenceSynthesisCertaintyType] = Field(
        None,
        alias="certainty",
        title="How certain is the effect",
        description="A description of the certainty of the effect estimate.",
        # if property is element of this resource.
        element_property=True,
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the effect evidence synthesis and/or"
            " its contents. Copyright statements are generally legal restrictions "
            "on the use and publishing of the effect evidence synthesis."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the effect evidence synthesis was"
            " published. The date must change when the business version changes and"
            " it must change if the status code changes. In addition, it should "
            "change when the substantive content of the effect evidence synthesis "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the effect evidence synthesis",
        description=(
            "A free text natural language description of the effect evidence "
            "synthesis from a consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    editor: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="editor",
        title="Who edited the content",
        description=(
            "An individual or organization primarily responsible for internal "
            "coherence of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    effectEstimate: ListType[
        fhirtypes.EffectEvidenceSynthesisEffectEstimateType
    ] = Field(
        None,
        alias="effectEstimate",
        title="What was the estimated effect",
        description="The estimated effect of the exposure variant.",
        # if property is element of this resource.
        element_property=True,
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the effect evidence synthesis is expected to be used",
        description=(
            "The period during which the effect evidence synthesis content was or "
            "is planned to be in active use."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    endorser: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individual or organization responsible for officially endorsing the"
            " content for use in some setting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    exposure: fhirtypes.ReferenceType = Field(
        ...,
        alias="exposure",
        title="What exposure?",
        description=(
            "A reference to a EvidenceVariable resource that defines the exposure "
            "for the research."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    exposureAlternative: fhirtypes.ReferenceType = Field(
        ...,
        alias="exposureAlternative",
        title="What comparison exposure?",
        description=(
            "A reference to a EvidenceVariable resource that defines the comparison"
            " exposure for the research."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the effect evidence synthesis",
        description=(
            "A formal identifier that is used to identify this effect evidence "
            "synthesis when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for effect evidence synthesis (if applicable)",
        description=(
            "A legal or geographic region in which the effect evidence synthesis is"
            " intended to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the effect evidence synthesis was last reviewed",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this effect evidence synthesis (computer friendly)",
        description=(
            "A natural language name identifying the effect evidence synthesis. "
            "This name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Used for footnotes or explanatory notes",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    outcome: fhirtypes.ReferenceType = Field(
        ...,
        alias="outcome",
        title="What outcome?",
        description=(
            "A reference to a EvidenceVariable resomece that defines the outcome "
            "for the research."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    population: fhirtypes.ReferenceType = Field(
        ...,
        alias="population",
        title="What population?",
        description=(
            "A reference to a EvidenceVariable resource that defines the population"
            " for the research."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EvidenceVariable"],
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the effect "
            "evidence synthesis."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    relatedArtifact: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc.",
        description=(
            "Related artifacts such as additional documentation, justification, or "
            "bibliographic references."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    resultsByExposure: ListType[
        fhirtypes.EffectEvidenceSynthesisResultsByExposureType
    ] = Field(
        None,
        alias="resultsByExposure",
        title="What was the result per exposure?",
        description=(
            "A description of the results for each exposure considered in the "
            "effect estimate."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reviewer: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individual or organization primarily responsible for review of some"
            " aspect of the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sampleSize: fhirtypes.EffectEvidenceSynthesisSampleSizeType = Field(
        None,
        alias="sampleSize",
        title="What sample size was involved?",
        description="A description of the size of the sample involved in the synthesis.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this effect evidence synthesis. Enables tracking the "
            "life-cycle of the content."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    studyType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="studyType",
        title="Type of study",
        description="Type of study eg randomized trial.",
        # if property is element of this resource.
        element_property=True,
    )

    synthesisType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="synthesisType",
        title="Type of synthesis",
        description="Type of synthesis eg meta-analysis.",
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this effect evidence synthesis (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the effect evidence "
            "synthesis."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title=(
            "The category of the EffectEvidenceSynthesis, such as Education, "
            "Treatment, Assessment, etc."
        ),
        description=(
            "Descriptive topics related to the content of the "
            "EffectEvidenceSynthesis. Topics provide a high-level categorization "
            "grouping types of EffectEvidenceSynthesiss that can be useful for "
            "filtering and searching."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this effect evidence synthesis, represented "
            "as a URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this effect evidence "
            "synthesis when it is referenced in a specification, model, design or "
            "an instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this effect evidence synthesis is (or will "
            "be) published. This URL can be the target of a canonical reference. It"
            " SHALL remain the same when the effect evidence synthesis is stored on"
            " different servers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate effect evidence synthesis "
            "instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the effect evidence synthesis",
        description=(
            "The identifier that is used to identify this version of the effect "
            "evidence synthesis when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the effect "
            "evidence synthesis author and is not expected to be globally unique. "
            "For example, it might be a timestamp (e.g. yyyymmdd) if a managed "
            "version is not available. There is also no expectation that versions "
            "can be placed in a lexicographical sequence."
        ),
        # if property is element of this resource.
        element_property=True,
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
        title="A component that contributes to the overall certainty",
        description="A description of a component of the overall certainty.",
        # if property is element of this resource.
        element_property=True,
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Used for footnotes or explanatory notes",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    rating: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="rating",
        title="Certainty rating",
        description="A rating of the certainty of the effect estimate.",
        # if property is element of this resource.
        element_property=True,
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
        title="Used for footnotes or explanatory notes",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    rating: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="rating",
        title="Subcomponent certainty rating",
        description="A rating of a subcomponent of rating certainty.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of subcomponent of certainty rating",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Description of effect estimate",
        description="Human-readable summary of effect estimate.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    precisionEstimate: ListType[
        fhirtypes.EffectEvidenceSynthesisEffectEstimatePrecisionEstimateType
    ] = Field(
        None,
        alias="precisionEstimate",
        title="How precise the estimate is",
        description="A description of the precision of the estimate for the effect.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of efffect estimate",
        description="Examples include relative risk and mean difference.",
        # if property is element of this resource.
        element_property=True,
    )

    unitOfMeasure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unitOfMeasure",
        title="What unit is the outcome described in?",
        description="Specifies the UCUM unit for the outcome.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Point estimate",
        description="The point estimate of the effect estimate.",
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    variantState: fhirtypes.CodeableConceptType = Field(
        None,
        alias="variantState",
        title="Variant exposure states",
        description="Used to define variant exposure states such as low-risk state.",
        # if property is element of this resource.
        element_property=True,
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
        None,
        alias="from",
        title="Lower bound",
        description="Lower bound of confidence interval.",
        # if property is element of this resource.
        element_property=True,
    )
    from__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_from", title="Extension field for ``from_fhir``."
    )

    level: fhirtypes.Decimal = Field(
        None,
        alias="level",
        title="Level of confidence interval",
        description="Use 95 for a 95% confidence interval.",
        # if property is element of this resource.
        element_property=True,
    )
    level__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_level", title="Extension field for ``level``."
    )

    to: fhirtypes.Decimal = Field(
        None,
        alias="to",
        title="Upper bound",
        description="Upper bound of confidence interval.",
        # if property is element of this resource.
        element_property=True,
    )
    to__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_to", title="Extension field for ``to``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of precision estimate",
        description="Examples include confidence interval and interquartile range.",
        # if property is element of this resource.
        element_property=True,
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
        title="Description of results by exposure",
        description="Human-readable summary of results by exposure state.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    exposureState: fhirtypes.Code = Field(
        None,
        alias="exposureState",
        title="exposure | exposure-alternative",
        description=(
            "Whether these results are for the exposure state or alternative "
            "exposure state."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["exposure", "exposure-alternative"],
    )
    exposureState__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exposureState", title="Extension field for ``exposureState``."
    )

    riskEvidenceSynthesis: fhirtypes.ReferenceType = Field(
        ...,
        alias="riskEvidenceSynthesis",
        title="Risk evidence synthesis",
        description="Reference to a RiskEvidenceSynthesis resource.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["RiskEvidenceSynthesis"],
    )

    variantState: fhirtypes.CodeableConceptType = Field(
        None,
        alias="variantState",
        title="Variant exposure states",
        description="Used to define variant exposure states such as low-risk state.",
        # if property is element of this resource.
        element_property=True,
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
        title="Description of sample size",
        description="Human-readable summary of sample size.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    numberOfParticipants: fhirtypes.Integer = Field(
        None,
        alias="numberOfParticipants",
        title="How many participants?",
        description="Number of participants included in this evidence synthesis.",
        # if property is element of this resource.
        element_property=True,
    )
    numberOfParticipants__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfParticipants",
        title="Extension field for ``numberOfParticipants``.",
    )

    numberOfStudies: fhirtypes.Integer = Field(
        None,
        alias="numberOfStudies",
        title="How many studies?",
        description="Number of studies included in this evidence synthesis.",
        # if property is element of this resource.
        element_property=True,
    )
    numberOfStudies__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfStudies", title="Extension field for ``numberOfStudies``."
    )
