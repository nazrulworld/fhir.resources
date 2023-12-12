# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/messageheader.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class MessageHeader(domainresource.DomainResource):
    """A resource that describes a message that is exchanged between systems.

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
        title="The source of the decision",
        description=(
            "The logical author of the message - the person or device that decided "
            "the described event should happen. When there is more than one "
            "candidate, pick the most proximal to the MessageHeader. Can provide "
            "other authors in extensions."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    data: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="data",
        title=(
            "List of `Reference` items referencing `Resource` (represented as `dict` "
            "in JSON)."
        ),
        description="The actual content of the message.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    destination: ListType[fhirtypes.MessageHeaderDestinationType] = Field(
        None,
        alias="destination",
        title="Message destination application(s)",
        description="The destination application which the message is intended for.",
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title="The source of the data entry",
        description=(
            "The person or device that performed the data entry leading to this "
            "message. When there is more than one candidate, pick the most proximal"
            " to the message. Can provide other enterers in extensions."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    event: fhirtypes.CodingType = Field(
        ...,
        alias="event",
        title="Code for the event this message represents or link to event definition",
        description=(
            "Code that identifies the event this message represents and connects it"
            " with its definition. Events defined as part of the FHIR specification"
            ' have the system value "http://terminology.hl7.org/CodeSystem/message-'
            'events".  Alternatively uri to the EventDefinition.'
        ),
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Cause of event",
        description=(
            "Coded indication of the cause for the event - indicates  a reason for "
            "the occurrence of the event that is a focus of this message."
        ),
    )

    receiver: fhirtypes.ReferenceType = Field(
        None,
        alias="receiver",
        title=(
            "Type `Reference` referencing `Practitioner, Organization` (represented as "
            "`dict` in JSON)."
        ),
        description='Intended "real-world" recipient for the data.',
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    response: fhirtypes.MessageHeaderResponseType = Field(
        None,
        alias="response",
        title="If this is a reply to prior message",
        description=(
            "Information about the message that this message is a response to.  "
            "Only present if this message is a response."
        ),
    )

    responsible: fhirtypes.ReferenceType = Field(
        None,
        alias="responsible",
        title="Final responsibility for event",
        description=(
            "The person or organization that accepts overall responsibility for the"
            " contents of the message. The implication is that the message event "
            "happened under the policies of the responsible party."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    source: fhirtypes.MessageHeaderSourceType = Field(
        ...,
        alias="source",
        title="Message source application",
        description="The source application from which this message originated.",
    )

    timestamp: fhirtypes.Instant = Field(
        ...,
        alias="timestamp",
        title="Type `Instant` (represented as `str` in JSON).",
        description="Time that the message was sent.",
    )


class MessageHeaderDestination(backboneelement.BackboneElement):
    """Message destination application(s).

    The destination application which the message is intended for.
    """

    resource_type = Field("MessageHeaderDestination", const=True)

    endpoint: fhirtypes.Uri = Field(
        ...,
        alias="endpoint",
        title="Actual destination address or id",
        description="Indicates where the message should be routed to.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of system",
        description="Human-readable name for the target system.",
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title="Particular delivery destination within the destination",
        description=(
            "Identifies the target end system in situations where the initial "
            "message transmission is to an intermediary system."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )


class MessageHeaderResponse(backboneelement.BackboneElement):
    """If this is a reply to prior message.

    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """

    resource_type = Field("MessageHeaderResponse", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="ok | transient-error | fatal-error",
        description=(
            "Code that identifies the type of response to the message - whether it "
            "was successful or not, and whether it should be resent or not."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["ok", "transient-error", "fatal-error"],
    )

    details: fhirtypes.ReferenceType = Field(
        None,
        alias="details",
        title="Specific list of hints/warnings/errors",
        description="Full details of any issues found in the message.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["OperationOutcome"],
    )

    identifier: fhirtypes.Id = Field(
        ...,
        alias="identifier",
        title="Id of original message",
        description=(
            "The MessageHeader.id of the message to which this message is a "
            "response."
        ),
    )


class MessageHeaderSource(backboneelement.BackboneElement):
    """Message source application.

    The source application from which this message originated.
    """

    resource_type = Field("MessageHeaderSource", const=True)

    contact: fhirtypes.ContactPointType = Field(
        None,
        alias="contact",
        title="Human contact for problems",
        description=(
            "An e-mail, phone, website or other contact point to use to resolve "
            "issues with message communications."
        ),
    )

    endpoint: fhirtypes.Uri = Field(
        ...,
        alias="endpoint",
        title="Actual message source address or id",
        description="Identifies the routing target to send acknowledgements to.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of system",
        description="Human-readable name for the source system.",
    )

    software: fhirtypes.String = Field(
        None,
        alias="software",
        title="Name of software running the system",
        description="May include configuration or other information useful in debugging.",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Version of software running",
        description=(
            "Can convey versions of multiple systems in situations where a message "
            "passes through multiple hands."
        ),
    )
