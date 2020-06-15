# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ResearchElementDefinition(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.
    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """

    resource_type = Field("ResearchElementDefinition", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the research element definition was approved by publisher",
    )

    author: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who authored the content",
    )

    characteristic: ListType[
        fhirtypes.ResearchElementDefinitionCharacteristicType
    ] = Field(
        ...,
        alias="characteristic",
        title=(
            "List of `ResearchElementDefinitionCharacteristic` items (represented "
            "as `dict` in JSON)"
        ),
        description="What defines the members of the research element",
    )

    comment: ListType[fhirtypes.String] = Field(
        None,
        alias="comment",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Used for footnotes or explanatory notes",
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
        description="Natural language description of the research element definition",
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
        description="When the research element definition is expected to be used",
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

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the research element definition",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for research element definition (if applicable)",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the research element definition was last reviewed",
    )

    library: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="library",
        title=(
            "List of `Canonical` items referencing `Library` (represented as `dict`"
            " in JSON)"
        ),
        description="Logic used by the ResearchElementDefinition",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this research element definition (computer friendly)",
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
        description="Why this research element definition is defined",
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

    shortTitle: fhirtypes.String = Field(
        None,
        alias="shortTitle",
        title="Type `String` (represented as `dict` in JSON)",
        description="Title for use in informal contexts",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Subordinate title of the ResearchElementDefinition",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this research element definition (human friendly)",
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "The category of the ResearchElementDefinition, such as Education, "
            "Treatment, Assessment, etc."
        ),
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="population | exposure | outcome",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this research element definition, represented"
            " as a URI (globally unique)"
        ),
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Type `String` (represented as `dict` in JSON)",
        description="Describes the clinical usage of the ResearchElementDefinition",
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    variableType: fhirtypes.Code = Field(
        None,
        alias="variableType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="dichotomous | continuous | descriptive",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the research element definition",
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


class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the research element.
    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """

    resource_type = Field("ResearchElementDefinitionCharacteristic", const=True)

    definitionCanonical: fhirtypes.Canonical = Field(
        None,
        alias="definitionCanonical",
        title=(
            "Type `Canonical` referencing `ValueSet` (represented as `dict` in " "JSON)"
        ),
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    definitionCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="definitionCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    definitionDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="definitionDataRequirement",
        title="Type `DataRequirement` (represented as `dict` in JSON)",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    definitionExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="definitionExpression",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    exclude: bool = Field(
        None,
        alias="exclude",
        title="Type `bool`",
        description="Whether the characteristic includes or excludes members",
    )

    participantEffectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="participantEffectiveDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="What time period do participants cover",
        one_of_many="participantEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    participantEffectiveDescription: fhirtypes.String = Field(
        None,
        alias="participantEffectiveDescription",
        title="Type `String` (represented as `dict` in JSON)",
        description="What time period do participants cover",
    )

    participantEffectiveDuration: fhirtypes.DurationType = Field(
        None,
        alias="participantEffectiveDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="What time period do participants cover",
        one_of_many="participantEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    participantEffectiveGroupMeasure: fhirtypes.Code = Field(
        None,
        alias="participantEffectiveGroupMeasure",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "mean | median | mean-of-mean | mean-of-median | median-of-mean | "
            "median-of-median"
        ),
    )

    participantEffectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="participantEffectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="What time period do participants cover",
        one_of_many="participantEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    participantEffectiveTimeFromStart: fhirtypes.DurationType = Field(
        None,
        alias="participantEffectiveTimeFromStart",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Observation time from study start",
    )

    participantEffectiveTiming: fhirtypes.TimingType = Field(
        None,
        alias="participantEffectiveTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="What time period do participants cover",
        one_of_many="participantEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    studyEffectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="studyEffectiveDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="What time period does the study cover",
        one_of_many="studyEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    studyEffectiveDescription: fhirtypes.String = Field(
        None,
        alias="studyEffectiveDescription",
        title="Type `String` (represented as `dict` in JSON)",
        description="What time period does the study cover",
    )

    studyEffectiveDuration: fhirtypes.DurationType = Field(
        None,
        alias="studyEffectiveDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="What time period does the study cover",
        one_of_many="studyEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    studyEffectiveGroupMeasure: fhirtypes.Code = Field(
        None,
        alias="studyEffectiveGroupMeasure",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "mean | median | mean-of-mean | mean-of-median | median-of-mean | "
            "median-of-median"
        ),
    )

    studyEffectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="studyEffectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="What time period does the study cover",
        one_of_many="studyEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    studyEffectiveTimeFromStart: fhirtypes.DurationType = Field(
        None,
        alias="studyEffectiveTimeFromStart",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Observation time from study start",
    )

    studyEffectiveTiming: fhirtypes.TimingType = Field(
        None,
        alias="studyEffectiveTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="What time period does the study cover",
        one_of_many="studyEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    unitOfMeasure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unitOfMeasure",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What unit is the outcome described in?",
    )

    usageContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="usageContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="What code/value pairs define members?",
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
            "definition": [
                "definitionCanonical",
                "definitionCodeableConcept",
                "definitionDataRequirement",
                "definitionExpression",
            ],
            "participantEffective": [
                "participantEffectiveDateTime",
                "participantEffectiveDuration",
                "participantEffectivePeriod",
                "participantEffectiveTiming",
            ],
            "studyEffective": [
                "studyEffectiveDateTime",
                "studyEffectiveDuration",
                "studyEffectivePeriod",
                "studyEffectiveTiming",
            ],
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
