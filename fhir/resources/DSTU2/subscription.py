# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/subscription.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class Subscription(domainresource.DomainResource):
    """A server push subscription criteria
    The subscription resource is used to define a push
    based subscription from a server to another system.
    Once a subscription is registered with the server,
    the server checks every resource that is created or updated,
    and if the resource matches the given criteria,
    it sends a message on the defined "channel" so that
    another system is able to take an appropriate action.
    """

    resource_type = Field("Subscription", const=True)

    criteria: fhirtypes.String = Field(
        None,
        alias="criteria",
        title="Type `String` (represented as `dict` in JSON)",
        description="Rule for server push criteria",
        element_property=True,
    )

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="Human contact for problems",
        description=(
            "Contact details for source (e.g. troubleshooting)"
            "Contact details for a human to contact about the subscription."
            "The primary use of this for system administrator troubleshooting."
        ),
        element_property=True,
    )

    reason: fhirtypes.String = Field(
        None,
        alias="reason",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of why this subscription was created",
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="requested | active | error | off",
        description=(
            "The status of the subscription, which marks the server"
            " state for managing the subscription."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["requested", "active", "error", "off"],
        element_property=True,
    )

    error: fhirtypes.String = Field(
        None,
        alias="error",
        title="Type `String` (represented as `dict` in JSON)",
        description="Latest error note",
        element_property=True,
    )

    channel: fhirtypes.SubscriptionChannelType = Field(
        None,
        alias="channel",
        title="Type `SubscriptionChannel` (represented as `dict` in JSON).",
        description="The channel on which to report matches to the criteria",
        element_property=True,
    )

    end: fhirtypes.Instant = Field(
        ...,
        alias="end",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When to automatically delete the subscription",
        element_property=True,
    )

    tag: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="tag",
        title="List of Type `Coding` (represented as `dict` in JSON).",
        description="A tag to add to matching resources",
        element_property=True,
    )


class SubscriptionChannel(BackboneElement):
    """The channel on which to report matches to the criteria


    Details where to send notifications when resources are received that meet the criteria.
    """

    resource_type = Field("SubscriptionChannel", const=True)

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="rest-hook | websocket | email | sms | message",
        description="The type of channel to send notifications on.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["rest-hook", "websocket", "email", "sms", "message"],
        element_property=True,
    )

    endpoint: fhirtypes.Uri = Field(
        None,
        alias="endpoint",
        title="Type `Uri` items (represented as `dict` in JSON)",
        description="Where the channel points to",
        element_property=True,
    )

    payload: fhirtypes.String = Field(
        None,
        alias="payload",
        title="Type `String` (represented as `dict` in JSON)",
        description="Mimetype to send, or blank for no payload",
        element_property=True,
    )

    header: fhirtypes.String = Field(
        None,
        alias="header",
        title="Type `String` (represented as `dict` in JSON)",
        description="Usage depends on the channel type",
        element_property=True,
    )
