# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

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
        title=(
            "List of `MessageDefinitionAllowedResponse` items (represented as "
            "`dict` in JSON)"
        ),
        description="Responses to this message",
    )

    base: fhirtypes.ReferenceType = Field(
        None,
        alias="base",
        title=(
            "Type `Reference` referencing `MessageDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Definition this one is based on",
    )

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Consequence | Currency | Notification",
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
        description="Date this was last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the message definition",
    )

    event: fhirtypes.CodingType = Field(
        ...,
        alias="event",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Event type",
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

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Additional identifier for the message definition",
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

    parent: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="parent",
        title=(
            "List of `Reference` items referencing `ActivityDefinition, "
            "PlanDefinition` (represented as `dict` in JSON)"
        ),
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

    replaces: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title=(
            "List of `Reference` items referencing `MessageDefinition` (represented"
            " as `dict` in JSON)"
        ),
        description="Takes the place of",
    )

    responseRequired: bool = Field(
        None,
        alias="responseRequired",
        title="Type `bool`",
        description="Is a response required?",
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
        description="Logical URI to reference this message definition (globally unique)",
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
        description="Business version of the message definition",
    )


class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """ Responses to this message.
    Indicates what types of messages may be sent as an application-level
    response to this message.
    """

    resource_type = Field("MessageDefinitionAllowedResponse", const=True)

    message: fhirtypes.ReferenceType = Field(
        ...,
        alias="message",
        title=(
            "Type `Reference` referencing `MessageDefinition` (represented as "
            "`dict` in JSON)"
        ),
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
        None,
        alias="min",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Minimum number of focuses of this type",
    )

    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title=(
            "Type `Reference` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Profile that must be adhered to by focus",
    )
