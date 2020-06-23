# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Subscription
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Subscription(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Server push subscription criteria.
    The subscription resource is used to define a push-based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system can take an appropriate action.
    """

    resource_type = Field("Subscription", const=True)

    channel: fhirtypes.SubscriptionChannelType = Field(
        ...,
        alias="channel",
        title="Type `SubscriptionChannel` (represented as `dict` in JSON)",
        description="The channel on which to report matches to the criteria",
    )

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Contact details for source (e.g. troubleshooting)",
    )

    criteria: fhirtypes.String = Field(
        ..., alias="criteria", title="Type `String`", description="Rule for server push"
    )
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criteria", title="Extension field for ``criteria``."
    )

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="Type `Instant`",
        description="When to automatically delete the subscription",
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    error: fhirtypes.String = Field(
        None, alias="error", title="Type `String`", description="Latest error note"
    )
    error__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_error", title="Extension field for ``error``."
    )

    reason: fhirtypes.String = Field(
        ...,
        alias="reason",
        title="Type `String`",
        description="Description of why this subscription was created",
    )
    reason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reason", title="Extension field for ``reason``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="requested | active | error | off",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )


class SubscriptionChannel(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The channel on which to report matches to the criteria.
    Details where to send notifications when resources are received that meet
    the criteria.
    """

    resource_type = Field("SubscriptionChannel", const=True)

    endpoint: fhirtypes.Url = Field(
        None,
        alias="endpoint",
        title="Type `Url`",
        description="Where the channel points to",
    )
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endpoint", title="Extension field for ``endpoint``."
    )

    header: ListType[fhirtypes.String] = Field(
        None,
        alias="header",
        title="List of `String` items",
        description="Usage depends on the channel type",
    )
    header__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_header", title="Extension field for ``header``."
    )

    payload: fhirtypes.Code = Field(
        None,
        alias="payload",
        title="Type `Code`",
        description="MIME type to send, or omit for no payload",
    )
    payload__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_payload", title="Extension field for ``payload``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="rest-hook | websocket | email | sms | message",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
