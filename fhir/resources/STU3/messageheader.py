# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageHeader
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.
    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """

    resource_type = Field("MessageHeader", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="The source of the decision",
    )

    destination: ListType[fhirtypes.MessageHeaderDestinationType] = Field(
        None,
        alias="destination",
        title=(
            "List of `MessageHeaderDestination` items (represented as `dict` in "
            "JSON)"
        ),
        description="Message destination application(s)",
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="The source of the data entry",
    )

    event: fhirtypes.CodingType = Field(
        ...,
        alias="event",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Code for the event this message represents",
    )

    focus: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="focus",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="The actual content of the message",
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Cause of event",
    )

    receiver: fhirtypes.ReferenceType = Field(
        None,
        alias="receiver",
        title=(
            "Type `Reference` referencing `Practitioner, Organization` (represented"
            " as `dict` in JSON)"
        ),
        description='Intended "real-world" recipient for the data',
    )

    response: fhirtypes.MessageHeaderResponseType = Field(
        None,
        alias="response",
        title="Type `MessageHeaderResponse` (represented as `dict` in JSON)",
        description="If this is a reply to prior message",
    )

    responsible: fhirtypes.ReferenceType = Field(
        None,
        alias="responsible",
        title=(
            "Type `Reference` referencing `Practitioner, Organization` (represented"
            " as `dict` in JSON)"
        ),
        description="Final responsibility for event",
    )

    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title=(
            "Type `Reference` referencing `Practitioner, Organization` (represented"
            " as `dict` in JSON)"
        ),
        description="Real world sender of the message",
    )

    source: fhirtypes.MessageHeaderSourceType = Field(
        ...,
        alias="source",
        title="Type `MessageHeaderSource` (represented as `dict` in JSON)",
        description="Message source application",
    )

    timestamp: fhirtypes.Instant = Field(
        ...,
        alias="timestamp",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Time that the message was sent",
    )


class MessageHeaderDestination(backboneelement.BackboneElement):
    """ Message destination application(s).
    The destination application which the message is intended for.
    """

    resource_type = Field("MessageHeaderDestination", const=True)

    endpoint: fhirtypes.Uri = Field(
        ...,
        alias="endpoint",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Actual destination address or id",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of system",
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="Particular delivery destination within the destination",
    )


class MessageHeaderResponse(backboneelement.BackboneElement):
    """ If this is a reply to prior message.
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """

    resource_type = Field("MessageHeaderResponse", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="ok | transient-error | fatal-error",
    )

    details: fhirtypes.ReferenceType = Field(
        None,
        alias="details",
        title=(
            "Type `Reference` referencing `OperationOutcome` (represented as `dict`"
            " in JSON)"
        ),
        description="Specific list of hints/warnings/errors",
    )

    identifier: fhirtypes.Id = Field(
        ...,
        alias="identifier",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Id of original message",
    )


class MessageHeaderSource(backboneelement.BackboneElement):
    """ Message source application.
    The source application from which this message originated.
    """

    resource_type = Field("MessageHeaderSource", const=True)

    contact: fhirtypes.ContactPointType = Field(
        None,
        alias="contact",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="Human contact for problems",
    )

    endpoint: fhirtypes.Uri = Field(
        ...,
        alias="endpoint",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Actual message source address or id",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of system",
    )

    software: fhirtypes.String = Field(
        None,
        alias="software",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of software running the system",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Version of software running",
    )
