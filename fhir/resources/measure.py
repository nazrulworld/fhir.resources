# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Measure
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

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

    author: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who authored the content",
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
        description="When the measure is expected to be used",
    )

    endorser: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who endorsed the content",
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

    improvementNotation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="improvementNotation",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="increase | decrease",
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

    library: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="library",
        title="List of `Canonical` items referencing `Library` (represented as `dict` in JSON)",
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
        description="Detailed description of why the measure exists",
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

    riskAdjustment: fhirtypes.String = Field(
        None,
        alias="riskAdjustment",
        title="Type `String` (represented as `dict` in JSON)",
        description="How risk adjustment is applied for this measure",
    )

    scoring: fhirtypes.CodeableConceptType = Field(
        None,
        alias="scoring",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="proportion | ratio | continuous-variable | cohort",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device",
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type `Reference` referencing `Group` (represented as `dict` in JSON)",
        description="E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device",
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Type `String` (represented as `dict` in JSON)",
        description="Subordinate title of the measure",
    )

    supplementalData: ListType[fhirtypes.MeasureSupplementalDataType] = Field(
        None,
        alias="supplementalData",
        title="List of `MeasureSupplementalData` items (represented as `dict` in JSON)",
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
        description="The category of the measure, such as Education, Treatment, Assessment, etc.",
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
        description="Canonical identifier for this measure, represented as a URI (globally unique)",
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
        description="The context that the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the measure",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "subject": ["subjectCodeableConcept", "subjectReference",],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class MeasureGroup(backboneelement.BackboneElement):
    """ Population criteria group.
    A group of population criteria for the measure.
    """

    resource_type = Field("MeasureGroup", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Meaning of the group",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Summary description",
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
        description="initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation",
    )

    criteria: fhirtypes.ExpressionType = Field(
        ...,
        alias="criteria",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="The criteria that defines this population",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="The human readable description of this population criteria",
    )


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """ Stratifier criteria for the measure.
    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library or a
    valid FHIR Resource Path.
    """

    resource_type = Field("MeasureGroupStratifier", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Meaning of the stratifier",
    )

    component: ListType[fhirtypes.MeasureGroupStratifierComponentType] = Field(
        None,
        alias="component",
        title="List of `MeasureGroupStratifierComponent` items (represented as `dict` in JSON)",
        description="Stratifier criteria component for the measure",
    )

    criteria: fhirtypes.ExpressionType = Field(
        None,
        alias="criteria",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="How the measure should be stratified",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="The human readable description of this stratifier",
    )


class MeasureGroupStratifierComponent(backboneelement.BackboneElement):
    """ Stratifier criteria component for the measure.
    A component of the stratifier criteria for the measure report, specified as
    either the name of a valid CQL expression defined within a referenced
    library or a valid FHIR Resource Path.
    """

    resource_type = Field("MeasureGroupStratifierComponent", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Meaning of the stratifier component",
    )

    criteria: fhirtypes.ExpressionType = Field(
        ...,
        alias="criteria",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="Component of how the measure should be stratified",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="The human readable description of this stratifier component",
    )


class MeasureSupplementalData(backboneelement.BackboneElement):
    """ What other data should be reported with the measure.
    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """

    resource_type = Field("MeasureSupplementalData", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Meaning of the supplemental data",
    )

    criteria: fhirtypes.ExpressionType = Field(
        ...,
        alias="criteria",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="Expression describing additional data to be reported",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="The human readable description of this supplemental data",
    )

    usage: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="usage",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="supplemental-data | risk-adjustment-factor",
    )
