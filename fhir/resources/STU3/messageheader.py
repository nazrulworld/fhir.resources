# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageHeader
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class MessageHeader(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A resource that describes a message that is exchanged between systems.
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    destination: typing.List[fhirtypes.MessageHeaderDestinationType] = Field(
        None,
        alias="destination",
        title="Message destination application(s)",
        description="The destination application which the message is intended for.",
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    event: fhirtypes.CodingType = Field(
        ...,
        alias="event",
        title="Code for the event this message represents",
        description=(
            "Code that identifies the event this message represents and connects it"
            " with its definition. Events defined as part of the FHIR specification"
            ' have the system value "http://hl7.org/fhir/message-events".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    focus: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="focus",
        title="The actual content of the message",
        description=(
            "The actual data of the message - a reference to the root/focus class "
            "of the event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Cause of event",
        description=(
            "Coded indication of the cause for the event - indicates  a reason for "
            "the occurrence of the event that is a focus of this message."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    receiver: fhirtypes.ReferenceType = Field(
        None,
        alias="receiver",
        title='Intended "real-world" recipient for the data',
        description=(
            "Allows data conveyed by a message to be addressed to a particular "
            "person or department when routing to a specific application isn't "
            "sufficient."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title="Real world sender of the message",
        description=(
            "Identifies the sending system to allow the use of a trust " "relationship."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    source: fhirtypes.MessageHeaderSourceType = Field(
        ...,
        alias="source",
        title="Message source application",
        description="The source application from which this message originated.",
        # if property is element of this resource.
        element_property=True,
    )

    timestamp: fhirtypes.Instant = Field(
        None,
        alias="timestamp",
        title="Time that the message was sent",
        description="The time that the message was sent.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timestamp", title="Extension field for ``timestamp``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MessageHeader`` according specification,
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
            "event",
            "destination",
            "receiver",
            "sender",
            "timestamp",
            "enterer",
            "author",
            "source",
            "responsible",
            "reason",
            "response",
            "focus",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1485(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("timestamp", "timestamp__ext")]
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


class MessageHeaderDestination(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message destination application(s).
    The destination application which the message is intended for.
    """

    resource_type = Field("MessageHeaderDestination", const=True)

    endpoint: fhirtypes.Uri = Field(
        None,
        alias="endpoint",
        title="Actual destination address or id",
        description="Indicates where the message should be routed to.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endpoint", title="Extension field for ``endpoint``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of system",
        description="Human-readable name for the target system.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title="Particular delivery destination within the destination",
        description=(
            "Identifies the target end system in situations where the initial "
            "message transmission is to an intermediary system."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MessageHeaderDestination`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "target", "endpoint"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2635(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("endpoint", "endpoint__ext")]
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


class MessageHeaderResponse(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this is a reply to prior message.
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """

    resource_type = Field("MessageHeaderResponse", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="ok | transient-error | fatal-error",
        description=(
            "Code that identifies the type of response to the message - whether it "
            "was successful or not, and whether it should be resent or not."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["ok", "transient-error", "fatal-error"],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    details: fhirtypes.ReferenceType = Field(
        None,
        alias="details",
        title="Specific list of hints/warnings/errors",
        description="Full details of any issues found in the message.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["OperationOutcome"],
    )

    identifier: fhirtypes.Id = Field(
        None,
        alias="identifier",
        title="Id of original message",
        description=(
            "The MessageHeader.id of the message to which this message is a "
            "response."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    identifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identifier", title="Extension field for ``identifier``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MessageHeaderResponse`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "identifier", "code", "details"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2319(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("identifier", "identifier__ext")]
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


class MessageHeaderSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message source application.
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
        # if property is element of this resource.
        element_property=True,
    )

    endpoint: fhirtypes.Uri = Field(
        None,
        alias="endpoint",
        title="Actual message source address or id",
        description="Identifies the routing target to send acknowledgements to.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endpoint", title="Extension field for ``endpoint``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of system",
        description="Human-readable name for the source system.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    software: fhirtypes.String = Field(
        None,
        alias="software",
        title="Name of software running the system",
        description="May include configuration or other information useful in debugging.",
        # if property is element of this resource.
        element_property=True,
    )
    software__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_software", title="Extension field for ``software``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Version of software running",
        description=(
            "Can convey versions of multiple systems in situations where a message "
            "passes through multiple hands."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MessageHeaderSource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "software",
            "version",
            "contact",
            "endpoint",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2097(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("endpoint", "endpoint__ext")]
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
