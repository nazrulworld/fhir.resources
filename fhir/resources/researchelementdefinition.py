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
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ResearchElementDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A population, intervention, or exposure definition.
    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """

    resource_type = Field("ResearchElementDefinition", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date`",
        description="When the research element definition was approved by publisher",
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
        title="List of `String` items",
        description="Used for footnotes or explanatory notes",
    )
    comment__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_comment", title="Extension field for ``comment``."
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
        description="Natural language description of the research element definition",
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
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
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
        title="Type `Date`",
        description="When the research element definition was last reviewed",
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="library",
        title="List of `Canonical` items referencing `Library`",
        description="Logic used by the ResearchElementDefinition",
    )
    library__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_library", title="Extension field for ``library``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this research element definition (computer friendly)",
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
        description="Why this research element definition is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
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
        title="Type `String`",
        description="Title for use in informal contexts",
    )
    shortTitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_shortTitle", title="Extension field for ``shortTitle``."
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
        description="Subordinate title of the ResearchElementDefinition",
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this research element definition (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
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
        title="Type `Code`",
        description="population | exposure | outcome",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description=(
            "Canonical identifier for this research element definition, represented"
            " as a URI (globally unique)"
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Type `String`",
        description="Describes the clinical usage of the ResearchElementDefinition",
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

    variableType: fhirtypes.Code = Field(
        None,
        alias="variableType",
        title="Type `Code`",
        description="dichotomous | continuous | descriptive",
    )
    variableType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_variableType", title="Extension field for ``variableType``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Business version of the research element definition",
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


class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What defines the members of the research element.
    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """

    resource_type = Field("ResearchElementDefinitionCharacteristic", const=True)

    definitionCanonical: fhirtypes.Canonical = Field(
        None,
        alias="definitionCanonical",
        title="Type `Canonical` referencing `ValueSet`",
        description="What code or expression defines members?",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
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
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    participantEffectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="participantEffectiveDateTime",
        title="Type `DateTime`",
        description="What time period do participants cover",
        one_of_many="participantEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    participantEffectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_participantEffectiveDateTime",
        title="Extension field for ``participantEffectiveDateTime``.",
    )

    participantEffectiveDescription: fhirtypes.String = Field(
        None,
        alias="participantEffectiveDescription",
        title="Type `String`",
        description="What time period do participants cover",
    )
    participantEffectiveDescription__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_participantEffectiveDescription",
        title="Extension field for ``participantEffectiveDescription``.",
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
        title="Type `Code`",
        description=(
            "mean | median | mean-of-mean | mean-of-median | median-of-mean | "
            "median-of-median"
        ),
    )
    participantEffectiveGroupMeasure__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_participantEffectiveGroupMeasure",
        title="Extension field for ``participantEffectiveGroupMeasure``.",
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
        title="Type `DateTime`",
        description="What time period does the study cover",
        one_of_many="studyEffective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    studyEffectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_studyEffectiveDateTime",
        title="Extension field for ``studyEffectiveDateTime``.",
    )

    studyEffectiveDescription: fhirtypes.String = Field(
        None,
        alias="studyEffectiveDescription",
        title="Type `String`",
        description="What time period does the study cover",
    )
    studyEffectiveDescription__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_studyEffectiveDescription",
        title="Extension field for ``studyEffectiveDescription``.",
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
        title="Type `Code`",
        description=(
            "mean | median | mean-of-mean | mean-of-median | median-of-mean | "
            "median-of-median"
        ),
    )
    studyEffectiveGroupMeasure__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_studyEffectiveGroupMeasure",
        title="Extension field for ``studyEffectiveGroupMeasure``.",
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
