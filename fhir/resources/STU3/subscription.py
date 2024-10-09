from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Subscription
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Subscription(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A server push subscription criteria.
    The subscription resource is used to define a push based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system is able to take an appropriate action.
    """

    __resource_type__ = "Subscription"

    channel: fhirtypes.SubscriptionChannelType = Field(  # type: ignore
        ...,
        alias="channel",
        title="The channel on which to report matches to the criteria",
        description=(
            "Details where to send notifications when resources are received that "
            "meet the criteria."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for source (e.g. troubleshooting)",
        description=(
            "Contact details for a human to contact about the subscription. The "
            "primary use of this for system administrator troubleshooting."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    criteria: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="criteria",
        title="Rule for server push criteria",
        description=(
            "The rules that the server should use to determine when to generate "
            "notifications for this subscription."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_criteria", title="Extension field for ``criteria``."
    )

    end: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="end",
        title="When to automatically delete the subscription",
        description="The time for the server to turn the subscription off.",
        json_schema_extra={
            "element_property": True,
        },
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_end", title="Extension field for ``end``."
    )

    error: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="error",
        title="Latest error note",
        description=(
            "A record of the last error that occurred when the server processed a "
            "notification."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    error__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_error", title="Extension field for ``error``."
    )

    reason: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Description of why this subscription was created",
        description="A description of why this subscription is defined.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    reason__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_reason", title="Extension field for ``reason``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="requested | active | error | off",
        description=(
            "The status of the subscription, which marks the server state for "
            "managing the subscription."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["requested", "active", "error", "off"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    tag: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="tag",
        title="A tag to add to matching resources",
        description=(
            "A tag to add to any resource that matches the criteria, after the "
            "subscription is processed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Subscription`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "status",
            "contact",
            "end",
            "reason",
            "criteria",
            "error",
            "channel",
            "tag",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("criteria", "criteria__ext"),
            ("reason", "reason__ext"),
            ("status", "status__ext"),
        ]
        return required_fields


class SubscriptionChannel(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The channel on which to report matches to the criteria.
    Details where to send notifications when resources are received that meet
    the criteria.
    """

    __resource_type__ = "SubscriptionChannel"

    endpoint: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="endpoint",
        title="Where the channel points to",
        description="The uri that describes the actual end-point to send messages to.",
        json_schema_extra={
            "element_property": True,
        },
    )
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_endpoint", title="Extension field for ``endpoint``."
    )

    header: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="header",
        title="Usage depends on the channel type",
        description="Additional headers / information to send as part of the notification.",
        json_schema_extra={
            "element_property": True,
        },
    )
    header__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_header", title="Extension field for ``header``."
    )

    payload: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="payload",
        title="Mimetype to send, or omit for no payload",
        description=(
            "The mime type to send the payload in - either application/fhir+xml, or"
            " application/fhir+json. If the payload is not present, then there is "
            "no payload in the notification, just a notification."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    payload__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_payload", title="Extension field for ``payload``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="rest-hook | websocket | email | sms | message",
        description="The type of channel to send notifications on.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["rest-hook", "websocket", "email", "sms", "message"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionChannel`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "endpoint",
            "payload",
            "header",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields
