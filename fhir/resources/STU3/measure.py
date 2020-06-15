# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Measure
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Measure(domainresource.DomainResource):
    """ A quality measure definition.
    The Measure resource provides the definition of a quality measure.
    """

    resource_type = Field("Measure", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the measure was approved by publisher",
    )

    clinicalRecommendationStatement: fhirtypes.Markdown = Field(
        None,
        alias="clinicalRecommendationStatement",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Summary of clinical guidelines",
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
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date this was last changed",
    )

    definition: ListType[fhirtypes.Markdown] = Field(
        None,
        alias="definition",
        title="List of `Markdown` items (represented as `dict` in JSON)",
        description="Defined terms used in the measure documentation",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the measure",
    )

    disclaimer: fhirtypes.Markdown = Field(
        None,
        alias="disclaimer",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Disclaimer for use of the measure or its referenced content",
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

    group: ListType[fhirtypes.MeasureGroupType] = Field(
        None,
        alias="group",
        title="List of `MeasureGroup` items (represented as `dict` in JSON)",
        description="Population criteria group",
    )

    guidance: fhirtypes.Markdown = Field(
        None,
        alias="guidance",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Additional guidance for implementers",
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
        title="Type `String` (represented as `dict` in JSON)",
        description=(
            "Improvement notation for the measure, e.g. higher score indicates "
            "better quality"
        ),
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
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the measure was last reviewed",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this measure (computer friendly)",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Why this measure is defined",
    )

    rateAggregation: fhirtypes.String = Field(
        None,
        alias="rateAggregation",
        title="Type `String` (represented as `dict` in JSON)",
        description="How is rate aggregation performed for this measure",
    )

    rationale: fhirtypes.Markdown = Field(
        None,
        alias="rationale",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Why does this measure exist",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="How is risk adjustment applied for this measure",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="The measure set, e.g. Preventive Care and Screening",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this measure (human friendly)",
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
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this measure (globally unique)",
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Type `String` (represented as `dict` in JSON)",
        description="Describes the clinical usage of the measure",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the measure",
    )


class MeasureGroup(backboneelement.BackboneElement):
    """ Population criteria group.
    A group of population criteria for the measure.
    """

    resource_type = Field("MeasureGroup", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Summary description",
    )

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique identifier",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short name",
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
    """ Population criteria.
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
        title="Type `String` (represented as `dict` in JSON)",
        description=(
            "The name of a valid referenced CQL expression (may be namespaced) that"
            " defines this population criteria"
        ),
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="The human readable description of this population criteria",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique identifier",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short name",
    )


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """ Stratifier criteria for the measure.
    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library, or a
    valid FHIR Resource Path.
    """

    resource_type = Field("MeasureGroupStratifier", const=True)

    criteria: fhirtypes.String = Field(
        None,
        alias="criteria",
        title="Type `String` (represented as `dict` in JSON)",
        description="How the measure should be stratified",
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
        None,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="Path to the stratifier",
    )


class MeasureSupplementalData(backboneelement.BackboneElement):
    """ What other data should be reported with the measure.
    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """

    resource_type = Field("MeasureSupplementalData", const=True)

    criteria: fhirtypes.String = Field(
        None,
        alias="criteria",
        title="Type `String` (represented as `dict` in JSON)",
        description="Expression describing additional data to be reported",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Path to the supplemental data element",
    )

    usage: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="usage",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="supplemental-data | risk-adjustment-factor",
    )
