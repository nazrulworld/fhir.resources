# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Library
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class Library(domainresource.DomainResource):
    """ Represents a library of quality improvement components.
    The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge
    assets such as logic libraries and information model descriptions, as well
    as to describe a collection of knowledge assets.
    """

    resource_type = Field("Library", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the library was approved by publisher",
    )

    author: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who authored the content",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    content: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="content",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Contents of the library, either embedded or referenced",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    dataRequirement: ListType[fhirtypes.DataRequirementType] = Field(
        None,
        alias="dataRequirement",
        title="List of `DataRequirement` items (represented as `dict` in JSON)",
        description="What data is referenced by this library",
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
        description="Natural language description of the library",
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
        description="When the library is expected to be used",
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
        description="Additional identifier for the library",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for library (if applicable)",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the library was last reviewed",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this library (computer friendly)",
    )

    parameter: ListType[fhirtypes.ParameterDefinitionType] = Field(
        None,
        alias="parameter",
        title="List of `ParameterDefinition` items (represented as `dict` in JSON)",
        description="Parameters defined by the library",
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
        description="Why this library is defined",
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
        description="Type of individual the library content is focused on",
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type `Reference` referencing `Group` (represented as `dict` in JSON)",
        description="Type of individual the library content is focused on",
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Type `String` (represented as `dict` in JSON)",
        description="Subordinate title of the library",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this library (human friendly)",
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="E.g. Education, Treatment, Assessment, etc.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "logic-library | model-definition | asset-collection | module-" "definition"
        ),
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this library, represented as a URI (globally "
            "unique)"
        ),
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Type `String` (represented as `dict` in JSON)",
        description="Describes the clinical usage of the library",
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
        description="Business version of the library",
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
