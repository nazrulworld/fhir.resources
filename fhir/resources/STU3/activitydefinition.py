# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ActivityDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ActivityDefinition(domainresource.DomainResource):
    """ The definition of a specific activity to be taken, independent of any
    particular patient or context.
    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """

    resource_type = Field("ActivityDefinition", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the activity definition was approved by publisher",
    )

    bodySite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="What part of body to perform on",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Detail type of activity",
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

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the activity definition",
    )

    dosage: ListType[fhirtypes.DosageType] = Field(
        None,
        alias="dosage",
        title="List of `Dosage` items (represented as `dict` in JSON)",
        description="Detailed dosage instructions",
    )

    dynamicValue: ListType[fhirtypes.ActivityDefinitionDynamicValueType] = Field(
        None,
        alias="dynamicValue",
        title=(
            "List of `ActivityDefinitionDynamicValue` items (represented as `dict` "
            "in JSON)"
        ),
        description="Dynamic aspects of the definition",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the activity definition is expected to be used",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the activity definition",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for activity definition (if applicable)",
    )

    kind: fhirtypes.Code = Field(
        None,
        alias="kind",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Kind of resource",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the activity definition was last reviewed",
    )

    library: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="library",
        title=(
            "List of `Reference` items referencing `Library` (represented as `dict`"
            " in JSON)"
        ),
        description="Logic used by the asset",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Where it should happen",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this activity definition (computer friendly)",
    )

    participant: ListType[fhirtypes.ActivityDefinitionParticipantType] = Field(
        None,
        alias="participant",
        title=(
            "List of `ActivityDefinitionParticipant` items (represented as `dict` "
            "in JSON)"
        ),
        description="Who should participate in the action",
    )

    productCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What\u0027s administered/supplied",
        one_of_many="product",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    productReference: fhirtypes.ReferenceType = Field(
        None,
        alias="productReference",
        title=(
            "Type `Reference` referencing `Medication, Substance` (represented as "
            "`dict` in JSON)"
        ),
        description="What\u0027s administered/supplied",
        one_of_many="product",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        description="Why this activity definition is defined",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="How much is administered/consumed/supplied",
    )

    relatedArtifact: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="Additional documentation, citations, etc",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When activity is to occur",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When activity is to occur",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingRange: fhirtypes.RangeType = Field(
        None,
        alias="timingRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="When activity is to occur",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingTiming: fhirtypes.TimingType = Field(
        None,
        alias="timingTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="When activity is to occur",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this activity definition (human friendly)",
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="E.g. Education, Treatment, Assessment, etc",
    )

    transform: fhirtypes.ReferenceType = Field(
        None,
        alias="transform",
        title=(
            "Type `Reference` referencing `StructureMap` (represented as `dict` in "
            "JSON)"
        ),
        description="Transform to apply the template",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this activity definition (globally unique)",
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Type `String` (represented as `dict` in JSON)",
        description="Describes the clinical usage of the asset",
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
        description="Business version of the activity definition",
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
            "product": ["productCodeableConcept", "productReference"],
            "timing": ["timingDateTime", "timingPeriod", "timingRange", "timingTiming"],
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


class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.
    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    intent resource that would contain the result.
    """

    resource_type = Field("ActivityDefinitionDynamicValue", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Natural language description of the dynamic value",
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String` (represented as `dict` in JSON)",
        description="An expression that provides the dynamic value for the customization",
    )

    language: fhirtypes.String = Field(
        None,
        alias="language",
        title="Type `String` (represented as `dict` in JSON)",
        description="Language of the expression",
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="The path to the element to be set dynamically",
    )


class ActivityDefinitionParticipant(backboneelement.BackboneElement):
    """ Who should participate in the action.
    Indicates who should participate in performing the action described.
    """

    resource_type = Field("ActivityDefinitionParticipant", const=True)

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="E.g. Nurse, Surgeon, Parent, etc",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="patient | practitioner | related-person",
    )
