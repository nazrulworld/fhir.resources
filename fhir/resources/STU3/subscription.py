# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Subscription
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

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

    resource_type = Field("Subscription", const=True)

    channel: fhirtypes.SubscriptionChannelType = Field(
        ...,
        alias="channel",
        title="The channel on which to report matches to the criteria",
        description=(
            "Details where to send notifications when resources are received that "
            "meet the criteria."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="Contact details for source (e.g. troubleshooting)",
        description=(
            "Contact details for a human to contact about the subscription. The "
            "primary use of this for system administrator troubleshooting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    criteria: fhirtypes.String = Field(
        None,
        alias="criteria",
        title="Rule for server push criteria",
        description=(
            "The rules that the server should use to determine when to generate "
            "notifications for this subscription."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_criteria", title="Extension field for ``criteria``."
    )

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="When to automatically delete the subscription",
        description="The time for the server to turn the subscription off.",
        # if property is element of this resource.
        element_property=True,
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    error: fhirtypes.String = Field(
        None,
        alias="error",
        title="Latest error note",
        description=(
            "A record of the last error that occurred when the server processed a "
            "notification."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    error__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_error", title="Extension field for ``error``."
    )

    reason: fhirtypes.String = Field(
        None,
        alias="reason",
        title="Description of why this subscription was created",
        description="A description of why this subscription is defined.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    reason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reason", title="Extension field for ``reason``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="requested | active | error | off",
        description=(
            "The status of the subscription, which marks the server state for "
            "managing the subscription."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["requested", "active", "error", "off"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    tag: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="tag",
        title="A tag to add to matching resources",
        description=(
            "A tag to add to any resource that matches the criteria, after the "
            "subscription is processed."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1478(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class SubscriptionChannel(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The channel on which to report matches to the criteria.
    Details where to send notifications when resources are received that meet
    the criteria.
    """

    resource_type = Field("SubscriptionChannel", const=True)

    endpoint: fhirtypes.Uri = Field(
        None,
        alias="endpoint",
        title="Where the channel points to",
        description="The uri that describes the actual end-point to send messages to.",
        # if property is element of this resource.
        element_property=True,
    )
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endpoint", title="Extension field for ``endpoint``."
    )

    header: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="header",
        title="Usage depends on the channel type",
        description="Additional headers / information to send as part of the notification.",
        # if property is element of this resource.
        element_property=True,
    )
    header__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_header", title="Extension field for ``header``.")

    payload: fhirtypes.String = Field(
        None,
        alias="payload",
        title="Mimetype to send, or omit for no payload",
        description=(
            "The mime type to send the payload in - either application/fhir+xml, or"
            " application/fhir+json. If the payload is not present, then there is "
            "no payload in the notification, just a notification."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    payload__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_payload", title="Extension field for ``payload``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="rest-hook | websocket | email | sms | message",
        description="The type of channel to send notifications on.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["rest-hook", "websocket", "email", "sms", "message"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2173(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
