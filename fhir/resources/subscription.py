# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Subscription
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Subscription(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Notification about a SubscriptionTopic.
    The subscription resource describes a particular client's request to be
    notified about a SubscriptionTopic.
    """

    resource_type = Field("Subscription", const=True)

    channelType: fhirtypes.CodingType = Field(
        ...,
        alias="channelType",
        title="Channel type for notifications",
        description="The type of channel to send notifications on.",
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

    content: fhirtypes.Code = Field(
        None,
        alias="content",
        title="empty | id-only | full-resource",
        description=(
            "How much of the resource content to deliver in the notification "
            "payload. The choices are an empty payload, only the resource id, or "
            "the full resource content."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["empty", "id-only", "full-resource"],
    )
    content__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_content", title="Extension field for ``content``."
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="MIME type to send, or omit for no payload",
        description=(
            "The MIME type to send the payload in - e.g., `application/fhir+xml` or"
            " `application/fhir+json`. Note that:  * clients may request "
            "notifications in a specific FHIR version by using the [FHIR Version "
            "Parameter](http.html#version-parameter) - e.g., "
            "`application/fhir+json; fhirVersion=4.0`.  * additional MIME types can"
            " be allowed by channels - e.g., `text/plain` and `text/html` are "
            "defined by the Email channel."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
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

    endpoint: fhirtypes.Url = Field(
        None,
        alias="endpoint",
        title="Where the channel points to",
        description="The url that describes the actual end-point to send notifications to.",
        # if property is element of this resource.
        element_property=True,
    )
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endpoint", title="Extension field for ``endpoint``."
    )

    filterBy: typing.List[fhirtypes.SubscriptionFilterByType] = Field(
        None,
        alias="filterBy",
        title="Criteria for narrowing the subscription topic stream",
        description=(
            "The filter properties to be applied to narrow the subscription topic "
            "stream.  When multiple filters are applied, evaluates to true if all "
            "the conditions applicable to that resource are met; otherwise it "
            "returns false (i.e., logical AND)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    heartbeatPeriod: fhirtypes.UnsignedInt = Field(
        None,
        alias="heartbeatPeriod",
        title="Interval in seconds to send 'heartbeat' notification",
        description=(
            "If present, a 'heartbeat' notification (keep-alive) is sent via this "
            "channel with an interval period equal to this elements integer value "
            "in seconds.  If not present, a heartbeat notification is not sent."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    heartbeatPeriod__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_heartbeatPeriod", title="Extension field for ``heartbeatPeriod``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifiers (business identifier)",
        description=(
            "A formal identifier that is used to identify this code system when it "
            "is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    managingEntity: fhirtypes.ReferenceType = Field(
        None,
        alias="managingEntity",
        title="Entity responsible for Subscription changes",
        description=(
            "Entity with authorization to make subsequent revisions to the "
            "Subscription and also determines what data the subscription is "
            "authorized to disclose."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "CareTeam",
            "HealthcareService",
            "Organization",
            "RelatedPerson",
            "Patient",
            "Practitioner",
            "PractitionerRole",
        ],
    )

    maxCount: fhirtypes.PositiveInt = Field(
        None,
        alias="maxCount",
        title="Maximum number of events that can be combined in a single notification",
        description=(
            "If present, the maximum number of events that will be included in a "
            "notification bundle. Note that this is not a strict limit on the "
            "number of entries in a bundle, as dependent resources can be included."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    maxCount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxCount", title="Extension field for ``maxCount``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Human readable name for this subscription",
        description="A natural language name identifying the subscription.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    parameter: typing.List[fhirtypes.SubscriptionParameterType] = Field(
        None,
        alias="parameter",
        title="Channel type",
        description=(
            "Channel-dependent information to send as part of the notification "
            "(e.g., HTTP Headers)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reason: fhirtypes.String = Field(
        None,
        alias="reason",
        title="Description of why this subscription was created",
        description="A description of why this subscription is defined.",
        # if property is element of this resource.
        element_property=True,
    )
    reason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reason", title="Extension field for ``reason``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="requested | active | error | off | entered-in-error",
        description=(
            "The status of the subscription, which marks the server state for "
            "managing the subscription."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["requested", "active", "error", "off", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    timeout: fhirtypes.UnsignedInt = Field(
        None,
        alias="timeout",
        title="Timeout in seconds to attempt notification delivery",
        description=(
            "If present, the maximum amount of time a server will allow before "
            "failing a notification attempt."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    timeout__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timeout", title="Extension field for ``timeout``."
    )

    topic: fhirtypes.Canonical = Field(
        None,
        alias="topic",
        title="Reference to the subscription topic being subscribed to",
        description="The reference to the subscription topic to be notified about.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubscriptionTopic"],
    )
    topic__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_topic", title="Extension field for ``topic``."
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
            "identifier",
            "name",
            "status",
            "topic",
            "contact",
            "end",
            "managingEntity",
            "reason",
            "filterBy",
            "channelType",
            "endpoint",
            "parameter",
            "heartbeatPeriod",
            "timeout",
            "contentType",
            "content",
            "maxCount",
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
        required_fields = [("status", "status__ext"), ("topic", "topic__ext")]
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


class SubscriptionFilterBy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Criteria for narrowing the subscription topic stream.
    The filter properties to be applied to narrow the subscription topic
    stream.  When multiple filters are applied, evaluates to true if all the
    conditions applicable to that resource are met; otherwise it returns false
    (i.e., logical AND).
    """

    resource_type = Field("SubscriptionFilterBy", const=True)

    comparator: fhirtypes.Code = Field(
        None,
        alias="comparator",
        title="eq | ne | gt | lt | ge | le | sa | eb | ap",
        description="Comparator applied to this filter parameter.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["eq", "ne", "gt", "lt", "ge", "le", "sa", "eb", "ap"],
    )
    comparator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comparator", title="Extension field for ``comparator``."
    )

    filterParameter: fhirtypes.String = Field(
        None,
        alias="filterParameter",
        title="Filter label defined in SubscriptionTopic",
        description=(
            "The filter as defined in the "
            "`SubscriptionTopic.canFilterBy.filterParameter` element."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    filterParameter__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_filterParameter", title="Extension field for ``filterParameter``."
    )

    modifier: fhirtypes.Code = Field(
        None,
        alias="modifier",
        title=(
            "missing | exact | contains | not | text | in | not-in | below | above "
            "| type | identifier | of-type | code-text | text-advanced | iterate"
        ),
        description="Modifier applied to this filter parameter.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "missing",
            "exact",
            "contains",
            "not",
            "text",
            "in",
            "not-in",
            "below",
            "above",
            "type",
            "identifier",
            "of-type",
            "code-text",
            "text-advanced",
            "iterate",
        ],
    )
    modifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_modifier", title="Extension field for ``modifier``."
    )

    resourceType: fhirtypes.Uri = Field(
        None,
        alias="resourceType",
        title=(
            "Allowed Resource (reference to definition) for this Subscription " "filter"
        ),
        description=(
            "A resource listed in the `SubscriptionTopic` this `Subscription` "
            "references (`SubscriptionTopic.canFilterBy.resource`). This element "
            "can be used to differentiate filters for topics that include more than"
            " one resource type."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    resourceType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resourceType", title="Extension field for ``resourceType``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Literal value or resource path",
        description=(
            "The literal value or resource path as is legal in search - for "
            "example, `Patient/123` or `le1950`."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionFilterBy`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "resourceType",
            "filterParameter",
            "comparator",
            "modifier",
            "value",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2290(
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
            ("filterParameter", "filterParameter__ext"),
            ("value", "value__ext"),
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


class SubscriptionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Channel type.
    Channel-dependent information to send as part of the notification (e.g.,
    HTTP Headers).
    """

    resource_type = Field("SubscriptionParameter", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name (key) of the parameter",
        description=(
            "Parameter name for information passed to the channel for "
            "notifications, for example in the case of a REST hook wanting to pass "
            "through an authorization header, the name would be Authorization."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Value of the parameter to use or pass through",
        description=(
            "Parameter value for information passed to the channel for "
            "notifications, for example in the case of a REST hook wanting to pass "
            "through an authorization header, the value would be `Bearer 0193...`."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubscriptionParameter`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2411(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("value", "value__ext")]
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
