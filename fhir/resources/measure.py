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
from typing import Union

from pydantic import Field, root_validator

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

    author: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who authored the content",
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
        title="Type `Date`",
        description="When the measure was last reviewed",
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="library",
        title="List of `Canonical` items referencing `Library`",
        description="Logic used by the measure",
    )
    library__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_library", title="Extension field for ``library``."
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
        description="Detailed description of why the measure exists",
    )
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rationale", title="Extension field for ``rationale``."
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
        title="Type `String`",
        description="How risk adjustment is applied for this measure",
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

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="draft | active | retired | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type `Reference` referencing `Group` (represented as `dict` in JSON)",
        description=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Type `String`",
        description="Subordinate title of the measure",
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subtitle", title="Extension field for ``subtitle``."
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
        description=(
            "The category of the measure, such as Education, Treatment, Assessment,"
            " etc."
        ),
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
        description=(
            "Canonical identifier for this measure, represented as a URI (globally "
            "unique)"
        ),
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
        description="The context that the content is intended to support",
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
        one_of_many_fields = {"subject": ["subjectCodeableConcept", "subjectReference"]}
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population criteria group.
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
        title="Type `String`",
        description="Summary description",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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

    criteria: fhirtypes.ExpressionType = Field(
        ...,
        alias="criteria",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="The criteria that defines this population",
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


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratifier criteria for the measure.
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
        title=(
            "List of `MeasureGroupStratifierComponent` items (represented as `dict`"
            " in JSON)"
        ),
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
        title="Type `String`",
        description="The human readable description of this stratifier",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )


class MeasureGroupStratifierComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratifier criteria component for the measure.
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
        title="Type `String`",
        description="The human readable description of this stratifier component",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
        title="Type `String`",
        description="The human readable description of this supplemental data",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    usage: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="usage",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="supplemental-data | risk-adjustment-factor",
    )
