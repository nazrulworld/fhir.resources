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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A resource that defines a type of message that can be exchanged between
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
        title="Type `Code`",
        description="Consequence | Currency | Notification",
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_category", title="Extension field for ``category``."
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
        ...,
        alias="date",
        title="Type `DateTime`",
        description="Date this was last changed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the message definition",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
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
        title="Type `String`",
        description="Name for this message definition (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
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
        description="Why this message definition is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
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
    responseRequired__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_responseRequired",
        title="Extension field for ``responseRequired``.",
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

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this message definition (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this message definition (globally unique)",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
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
        description="Business version of the message definition",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Responses to this message.
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
        title="Type `Markdown`",
        description="When should this response be used",
    )
    situation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_situation", title="Extension field for ``situation``."
    )


class MessageDefinitionFocus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource(s) that are the subject of the event.
    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """

    resource_type = Field("MessageDefinitionFocus", const=True)

    code: fhirtypes.Code = Field(
        ..., alias="code", title="Type `Code`", description="Type of resource"
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String`",
        description="Maximum number of focuses of this type",
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.UnsignedInt = Field(
        None,
        alias="min",
        title="Type `UnsignedInt`",
        description="Minimum number of focuses of this type",
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
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
