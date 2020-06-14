# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Subscription
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Subscription(domainresource.DomainResource):
    """ A server push subscription criteria.
    The subscription resource is used to define a push based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system is able to take an appropriate action.
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
        ...,
        alias="criteria",
        title="Type `String` (represented as `dict` in JSON)",
        description="Rule for server push criteria",
    )

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When to automatically delete the subscription",
    )

    error: fhirtypes.String = Field(
        None,
        alias="error",
        title="Type `String` (represented as `dict` in JSON)",
        description="Latest error note",
    )

    reason: fhirtypes.String = Field(
        ...,
        alias="reason",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of why this subscription was created",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="requested | active | error | off",
    )

    tag: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="tag",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="A tag to add to matching resources",
    )


class SubscriptionChannel(backboneelement.BackboneElement):
    """ The channel on which to report matches to the criteria.
    Details where to send notifications when resources are received that meet
    the criteria.
    """

    resource_type = Field("SubscriptionChannel", const=True)

    endpoint: fhirtypes.Uri = Field(
        None,
        alias="endpoint",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Where the channel points to",
    )

    header: ListType[fhirtypes.String] = Field(
        None,
        alias="header",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Usage depends on the channel type",
    )

    payload: fhirtypes.String = Field(
        None,
        alias="payload",
        title="Type `String` (represented as `dict` in JSON)",
        description="Mimetype to send, or omit for no payload",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="rest-hook | websocket | email | sms | message",
    )
