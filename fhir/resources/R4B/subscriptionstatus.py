from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionStatus
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubscriptionStatus(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Status information about a Subscription provided during event notification.
    The SubscriptionStatus resource describes the state of a Subscription
    during notifications.
    """

    __resource_type__ = "SubscriptionStatus"

    error: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="error",
        title="List of errors on the subscription",
        description=(
            "A record of errors that occurred when the server processed a "
            "notification."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    eventsSinceSubscriptionStart: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="eventsSinceSubscriptionStart",
        title="Events since the Subscription was created",
        description=(
            "The total number of actual events which have been generated since the "
            "Subscription was created (inclusive of this notification) - regardless"
            " of how many have been successfully communicated.  This number is NOT "
            "incremented for handshake and heartbeat notifications."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    eventsSinceSubscriptionStart__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_eventsSinceSubscriptionStart",
        title="Extension field for ``eventsSinceSubscriptionStart``.",
    )

    notificationEvent: typing.List[fhirtypes.SubscriptionStatusNotificationEventType] | None = Field(  # type: ignore
        None,
        alias="notificationEvent",
        title="Detailed information about any events relevant to this notification",
        description=(
            "Detailed information about events relevant to this subscription "
            "notification."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="requested | active | error | off | entered-in-error",
        description=(
            "The status of the subscription, which marks the server state for "
            "managing the subscription."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["requested", "active", "error", "off", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subscription: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subscription",
        title="Reference to the Subscription responsible for this notification",
        description="The reference to the Subscription which generated this notification.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Subscription"],
        },
    )

    topic: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="topic",
        title="Reference to the SubscriptionTopic this notification relates to",
        description=(
            "The reference to the SubscriptionTopic for the Subscription which "
            "generated this notification."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SubscriptionTopic"],
        },
    )
    topic__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_topic", title="Extension field for ``topic``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "handshake | heartbeat | event-notification | query-status | query-" "event"
        ),
        description="The type of event being conveyed with this notificaiton.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "handshake",
                "heartbeat",
                "event-notification",
                "query-status",
                "query-event",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionStatus`` according specification,
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
            "type",
            "eventsSinceSubscriptionStart",
            "notificationEvent",
            "subscription",
            "topic",
            "error",
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


class SubscriptionStatusNotificationEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Detailed information about any events relevant to this notification.
    Detailed information about events relevant to this subscription
    notification.
    """

    __resource_type__ = "SubscriptionStatusNotificationEvent"

    additionalContext: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="additionalContext",
        title="Additional context for this event",
        description=(
            "Additional context information for this event. Generally, this will "
            "contain references to additional resources included with the event "
            "(e.g., the Patient relevant to an Encounter), however it MAY refer to "
            "non-FHIR objects."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    eventNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="eventNumber",
        title="Event number",
        description=(
            "The sequential number of this event in this subscription context. Note"
            " that this value is a 64-bit integer value, encoded as a string."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    eventNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_eventNumber", title="Extension field for ``eventNumber``."
    )

    focus: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="focus",
        title="The focus of this event",
        description=(
            "The focus of this event. While this will usually be a reference to the"
            " focus resource of the event, it MAY contain a reference to a non-FHIR"
            " object."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    timestamp: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="timestamp",
        title="The instant this event occurred",
        description="The actual time this event occured on the server.",
        json_schema_extra={
            "element_property": True,
        },
    )
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timestamp", title="Extension field for ``timestamp``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionStatusNotificationEvent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "eventNumber",
            "timestamp",
            "focus",
            "additionalContext",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("eventNumber", "eventNumber__ext")]
        return required_fields
