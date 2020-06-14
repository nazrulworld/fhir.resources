# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MessageDefinition(domainresource.DomainResource):
    """ A resource that defines a type of message that can be exchanged between
    systems.
    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """

    resource_type = Field("MessageDefinition", const=True)

    allowedResponse: ListType[fhirtypes.MessageDefinitionAllowedResponseType] = Field(
        None,
        alias="allowedResponse",
        title="List of `MessageDefinitionAllowedResponse` items (represented as `dict` in JSON)",
        description="Responses to this message",
    )

    base: fhirtypes.Canonical = Field(
        None,
        alias="base",
        title="Type `Canonical` referencing `MessageDefinition` (represented as `dict` in JSON)",
        description="Definition this one is based on",
    )

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Type `Code` (represented as `dict` in JSON)",
        description="consequence | currency | notification",
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
        ...,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the message definition",
    )

    eventCoding: fhirtypes.CodingType = Field(
        None,
        alias="eventCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Event code  or link to the EventDefinition",
        one_of_many="event",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    eventUri: fhirtypes.Uri = Field(
        None,
        alias="eventUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Event code  or link to the EventDefinition",
        one_of_many="event",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    focus: ListType[fhirtypes.MessageDefinitionFocusType] = Field(
        None,
        alias="focus",
        title="List of `MessageDefinitionFocus` items (represented as `dict` in JSON)",
        description="Resource(s) that are the subject of the event",
    )

    graph: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="graph",
        title="List of `Canonical` items referencing `GraphDefinition` (represented as `dict` in JSON)",
        description="Canonical reference to a GraphDefinition",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Primary key for the message definition on a given server",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for message definition (if applicable)",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this message definition (computer friendly)",
    )

    parent: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="parent",
        title="List of `Canonical` items referencing `ActivityDefinition, PlanDefinition` (represented as `dict` in JSON)",
        description="Protocol/workflow this is part of",
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
        description="Why this message definition is defined",
    )

    replaces: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="replaces",
        title="List of `Canonical` items referencing `MessageDefinition` (represented as `dict` in JSON)",
        description="Takes the place of",
    )

    responseRequired: fhirtypes.Code = Field(
        None,
        alias="responseRequired",
        title="Type `Code` (represented as `dict` in JSON)",
        description="always | on-error | never | on-success",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this message definition (human friendly)",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Business Identifier for a given MessageDefinition",
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
        description="Business version of the message definition",
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
            "event": ["eventCoding", "eventUri",],
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


class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """ Responses to this message.
    Indicates what types of messages may be sent as an application-level
    response to this message.
    """

    resource_type = Field("MessageDefinitionAllowedResponse", const=True)

    message: fhirtypes.Canonical = Field(
        ...,
        alias="message",
        title="Type `Canonical` referencing `MessageDefinition` (represented as `dict` in JSON)",
        description="Reference to allowed message definition response",
    )

    situation: fhirtypes.Markdown = Field(
        None,
        alias="situation",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="When should this response be used",
    )


class MessageDefinitionFocus(backboneelement.BackboneElement):
    """ Resource(s) that are the subject of the event.
    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """

    resource_type = Field("MessageDefinitionFocus", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Type of resource",
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String` (represented as `dict` in JSON)",
        description="Maximum number of focuses of this type",
    )

    min: fhirtypes.UnsignedInt = Field(
        ...,
        alias="min",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Minimum number of focuses of this type",
    )

    profile: fhirtypes.Canonical = Field(
        None,
        alias="profile",
        title="Type `Canonical` referencing `StructureDefinition` (represented as `dict` in JSON)",
        description="Profile that must be adhered to by focus",
    )
