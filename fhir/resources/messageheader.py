# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageHeader
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
            "The logical author of the message - the personor device that decided "
            "the described event should happen. When there is more than one "
            "candidate, pick the most proximal to the MessageHeader. Can provide "
            "other authors in extensions."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Device",
            "Organization",
        ],
    )

    definition: fhirtypes.Canonical = Field(
        None,
        alias="definition",
        title="Link to the definition for this message",
        description="Permanent link to the MessageDefinition for this message.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MessageDefinition"],
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    destination: typing.List[fhirtypes.MessageHeaderDestinationType] = Field(
        None,
        alias="destination",
        title="Message destination application(s)",
        description="The destination application which the message is intended for.",
        # if property is element of this resource.
        element_property=True,
    )

    eventCanonical: fhirtypes.Canonical = Field(
        None,
        alias="eventCanonical",
        title="Event code or link to EventDefinition",
        description=(
            "Code that identifies the event this message represents and connects it"
            " with its definition. Events defined as part of the FHIR specification"
            " are defined by the implementation.  Alternatively a canonical uri to "
            "the EventDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e event[x]
        one_of_many="event",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EventDefinition"],
    )
    eventCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eventCanonical", title="Extension field for ``eventCanonical``."
    )

    eventCoding: fhirtypes.CodingType = Field(
        None,
        alias="eventCoding",
        title="Event code or link to EventDefinition",
        description=(
            "Code that identifies the event this message represents and connects it"
            " with its definition. Events defined as part of the FHIR specification"
            " are defined by the implementation.  Alternatively a canonical uri to "
            "the EventDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e event[x]
        one_of_many="event",
        one_of_many_required=True,
    )

    focus: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="focus",
        title="The actual content of the message",
        description=(
            "The actual data of the message - a reference to the root/focus class "
            "of the event. This is allowed to be a Parameters resource."
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
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
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
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Device",
            "Organization",
        ],
    )

    source: fhirtypes.MessageHeaderSourceType = Field(
        ...,
        alias="source",
        title="Message source application",
        description="The source application from which this message originated.",
        # if property is element of this resource.
        element_property=True,
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
            "eventCoding",
            "eventCanonical",
            "destination",
            "sender",
            "author",
            "source",
            "responsible",
            "reason",
            "response",
            "focus",
            "definition",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1485(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"event": ["eventCanonical", "eventCoding"]}
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class MessageHeaderDestination(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message destination application(s).
    The destination application which the message is intended for.
    """

    resource_type = Field("MessageHeaderDestination", const=True)

    endpointReference: fhirtypes.ReferenceType = Field(
        None,
        alias="endpointReference",
        title="Actual destination address or Endpoint resource",
        description="Indicates where the message should be routed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e endpoint[x]
        one_of_many="endpoint",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    endpointUrl: fhirtypes.Url = Field(
        None,
        alias="endpointUrl",
        title="Actual destination address or Endpoint resource",
        description="Indicates where the message should be routed.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e endpoint[x]
        one_of_many="endpoint",
        one_of_many_required=False,
    )
    endpointUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endpointUrl", title="Extension field for ``endpointUrl``."
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
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
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
        return [
            "id",
            "extension",
            "modifierExtension",
            "endpointUrl",
            "endpointReference",
            "name",
            "target",
            "receiver",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2635(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"endpoint": ["endpointReference", "endpointUrl"]}
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

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

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Bundle.identifier of original message",
        description=(
            "The Bundle.identifier of the message to which this message is a "
            "response."
        ),
        # if property is element of this resource.
        element_property=True,
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
        required_fields = [("code", "code__ext")]
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

    endpointReference: fhirtypes.ReferenceType = Field(
        None,
        alias="endpointReference",
        title="Actual source address or Endpoint resource",
        description="Identifies the routing target to send acknowledgements to.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e endpoint[x]
        one_of_many="endpoint",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    endpointUrl: fhirtypes.Url = Field(
        None,
        alias="endpointUrl",
        title="Actual source address or Endpoint resource",
        description="Identifies the routing target to send acknowledgements to.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e endpoint[x]
        one_of_many="endpoint",
        one_of_many_required=False,
    )
    endpointUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_endpointUrl", title="Extension field for ``endpointUrl``."
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
            "endpointUrl",
            "endpointReference",
            "name",
            "software",
            "version",
            "contact",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2097(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"endpoint": ["endpointReference", "endpointUrl"]}
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
