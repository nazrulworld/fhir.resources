# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Measure
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Measure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A quality measure definition.
    The Measure resource provides the definition of a quality measure.
    """

    resource_type = Field("Measure", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date`",
        description="When the measure was approved by publisher",
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    clinicalRecommendationStatement: fhirtypes.Markdown = Field(
        None,
        alias="clinicalRecommendationStatement",
        title="Type `Markdown`",
        description="Summary of clinical guidelines",
    )
    clinicalRecommendationStatement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_clinicalRecommendationStatement",
        title="Extension field for ``clinicalRecommendationStatement``.",
    )

    compositeScoring: fhirtypes.CodeableConceptType = Field(
        None,
        alias="compositeScoring",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="opportunity | all-or-nothing | linear | weighted",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    contributor: ListType[fhirtypes.ContributorType] = Field(
        None,
        alias="contributor",
        title="List of `Contributor` items (represented as `dict` in JSON)",
        description="A content contributor",
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
        None,
        alias="date",
        title="Type `DateTime`",
        description="Date this was last changed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    definition: ListType[fhirtypes.Markdown] = Field(
        None,
        alias="definition",
        title="List of `Markdown` items",
        description="Defined terms used in the measure documentation",
    )
    definition__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_definition", title="Extension field for ``definition``.")

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the measure",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    disclaimer: fhirtypes.Markdown = Field(
        None,
        alias="disclaimer",
        title="Type `Markdown`",
        description="Disclaimer for use of the measure or its referenced content",
    )
    disclaimer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disclaimer", title="Extension field for ``disclaimer``."
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the measure is expected to be used",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    group: ListType[fhirtypes.MeasureGroupType] = Field(
        None,
        alias="group",
        title="List of `MeasureGroup` items (represented as `dict` in JSON)",
        description="Population criteria group",
    )

    guidance: fhirtypes.Markdown = Field(
        None,
        alias="guidance",
        title="Type `Markdown`",
        description="Additional guidance for implementers",
    )
    guidance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_guidance", title="Extension field for ``guidance``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the measure",
    )

    improvementNotation: fhirtypes.String = Field(
        None,
        alias="improvementNotation",
        title="Type `String`",
        description=(
            "Improvement notation for the measure, e.g. higher score indicates "
            "better quality"
        ),
    )
    improvementNotation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_improvementNotation",
        title="Extension field for ``improvementNotation``.",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for measure (if applicable)",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date`",
        description="When the measure was last reviewed",
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="library",
        title=(
            "List of `Reference` items referencing `Library` (represented as `dict`"
            " in JSON)"
        ),
        description="Logic used by the measure",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this measure (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
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

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown`",
        description="Why this measure is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    rateAggregation: fhirtypes.String = Field(
        None,
        alias="rateAggregation",
        title="Type `String`",
        description="How is rate aggregation performed for this measure",
    )
    rateAggregation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rateAggregation", title="Extension field for ``rateAggregation``."
    )

    rationale: fhirtypes.Markdown = Field(
        None,
        alias="rationale",
        title="Type `Markdown`",
        description="Why does this measure exist",
    )
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rationale", title="Extension field for ``rationale``."
    )

    relatedArtifact: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="Additional documentation, citations, etc",
    )

    riskAdjustment: fhirtypes.String = Field(
        None,
        alias="riskAdjustment",
        title="Type `String`",
        description="How is risk adjustment applied for this measure",
    )
    riskAdjustment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_riskAdjustment", title="Extension field for ``riskAdjustment``."
    )

    scoring: fhirtypes.CodeableConceptType = Field(
        None,
        alias="scoring",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="proportion | ratio | continuous-variable | cohort",
    )

    set: fhirtypes.String = Field(
        None,
        alias="set",
        title="Type `String`",
        description="The measure set, e.g. Preventive Care and Screening",
    )
    set__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_set", title="Extension field for ``set``."
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

    supplementalData: ListType[fhirtypes.MeasureSupplementalDataType] = Field(
        None,
        alias="supplementalData",
        title=(
            "List of `MeasureSupplementalData` items (represented as `dict` in " "JSON)"
        ),
        description="What other data should be reported with the measure",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this measure (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="E.g. Education, Treatment, Assessment, etc",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="process | outcome | structure | patient-reported-outcome | composite",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this measure (globally unique)",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Type `String`",
        description="Describes the clinical usage of the measure",
    )
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_usage", title="Extension field for ``usage``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="Context the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Business version of the measure",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class MeasureGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population criteria group.
    A group of population criteria for the measure.
    """

    resource_type = Field("MeasureGroup", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Summary description",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique identifier",
    )

    name: fhirtypes.String = Field(
        None, alias="name", title="Type `String`", description="Short name"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    population: ListType[fhirtypes.MeasureGroupPopulationType] = Field(
        None,
        alias="population",
        title="List of `MeasureGroupPopulation` items (represented as `dict` in JSON)",
        description="Population criteria",
    )

    stratifier: ListType[fhirtypes.MeasureGroupStratifierType] = Field(
        None,
        alias="stratifier",
        title="List of `MeasureGroupStratifier` items (represented as `dict` in JSON)",
        description="Stratifier criteria for the measure",
    )


class MeasureGroupPopulation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population criteria.
    A population criteria for the measure.
    """

    resource_type = Field("MeasureGroupPopulation", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-observation"
        ),
    )

    criteria: fhirtypes.String = Field(
        ...,
        alias="criteria",
        title="Type `String`",
        description=(
            "The name of a valid referenced CQL expression (may be namespaced) that"
            " defines this population criteria"
        ),
    )
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criteria", title="Extension field for ``criteria``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="The human readable description of this population criteria",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique identifier",
    )

    name: fhirtypes.String = Field(
        None, alias="name", title="Type `String`", description="Short name"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratifier criteria for the measure.
    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library, or a
    valid FHIR Resource Path.
    """

    resource_type = Field("MeasureGroupStratifier", const=True)

    criteria: fhirtypes.String = Field(
        None,
        alias="criteria",
        title="Type `String`",
        description="How the measure should be stratified",
    )
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criteria", title="Extension field for ``criteria``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description=(
            "The identifier for the stratifier used to coordinate the reported data"
            " back to this stratifier"
        ),
    )

    path: fhirtypes.String = Field(
        None, alias="path", title="Type `String`", description="Path to the stratifier"
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )


class MeasureSupplementalData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What other data should be reported with the measure.
    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """

    resource_type = Field("MeasureSupplementalData", const=True)

    criteria: fhirtypes.String = Field(
        None,
        alias="criteria",
        title="Type `String`",
        description="Expression describing additional data to be reported",
    )
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criteria", title="Extension field for ``criteria``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier, unique within the measure",
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String`",
        description="Path to the supplemental data element",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    usage: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="usage",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="supplemental-data | risk-adjustment-factor",
    )
