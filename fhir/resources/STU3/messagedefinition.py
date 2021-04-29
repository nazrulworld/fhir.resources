# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition
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


class MessageDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A resource that defines a type of message that can be exchanged between
    systems.
    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """

    resource_type = Field("MessageDefinition", const=True)

    allowedResponse: typing.List[
        fhirtypes.MessageDefinitionAllowedResponseType
    ] = Field(
        None,
        alias="allowedResponse",
        title="Responses to this message",
        description=(
            "Indicates what types of messages may be sent as an application-level "
            "response to this message."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    base: fhirtypes.ReferenceType = Field(
        None,
        alias="base",
        title="Definition this one is based on",
        description=(
            "The MessageDefinition that is the basis for the contents of this "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MessageDefinition"],
    )

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Consequence | Currency | Notification",
        description="The impact of the content of the message.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["Consequence", "Currency", "Notification"],
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_category", title="Extension field for ``category``."
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the message definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the message definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the message definition was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the message definition "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the message definition",
        description=(
            "A free text natural language description of the message definition "
            "from a consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    event: fhirtypes.CodingType = Field(
        ...,
        alias="event",
        title="Event type",
        description="A coded identifier of a supported messaging event.",
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this message definition is authored "
            "for testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    focus: typing.List[fhirtypes.MessageDefinitionFocusType] = Field(
        None,
        alias="focus",
        title="Resource(s) that are the subject of the event",
        description=(
            "Identifies the resource (or resources) that are being addressed by the"
            " event.  For example, the Encounter for an admit message or two "
            "Account records for a merge."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Additional identifier for the message definition",
        description=(
            "A formal identifier that is used to identify this message definition "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for message definition (if applicable)",
        description=(
            "A legal or geographic region in which the message definition is "
            "intended to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this message definition (computer friendly)",
        description=(
            "A natural language name identifying the message definition. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    parent: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="parent",
        title="Protocol/workflow this is part of",
        description=(
            "Identifies a protocol or workflow that this MessageDefinition "
            "represents a step in."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ActivityDefinition", "PlanDefinition"],
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the message "
            "definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this message definition is defined",
        description=(
            "Explaination of why this message definition is needed and why it has "
            "been designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    replaces: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title="Takes the place of",
        description="A MessageDefinition that is superseded by this definition.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MessageDefinition"],
    )

    responseRequired: bool = Field(
        None,
        alias="responseRequired",
        title="Is a response required?",
        description="Indicates whether a response is required for this message.",
        # if property is element of this resource.
        element_property=True,
    )
    responseRequired__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_responseRequired",
        title="Extension field for ``responseRequired``.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this message definition. Enables tracking the life-cycle"
            " of the content."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this message definition (human friendly)",
        description="A short, descriptive, user-friendly title for the message definition.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this message definition (globally unique)",
        description=(
            "An absolute URI that is used to identify this message definition when "
            "it is referenced in a specification, model, design or an instance. "
            "This SHALL be a URL, SHOULD be globally unique, and SHOULD be an "
            "address at which this message definition is (or will be) published. "
            "The URL SHOULD include the major version of the message definition. "
            "For more information see [Technical and Business "
            "Versions](resource.html#versions)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate message definition instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the message definition",
        description=(
            "The identifier that is used to identify this version of the message "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the message definition"
            " author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
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
        ``MessageDefinition`` according specification,
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
            "url",
            "identifier",
            "version",
            "name",
            "title",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "base",
            "parent",
            "replaces",
            "event",
            "category",
            "focus",
            "responseRequired",
            "allowedResponse",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1929(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("date", "date__ext"), ("status", "status__ext")]
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


class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Responses to this message.
    Indicates what types of messages may be sent as an application-level
    response to this message.
    """

    resource_type = Field("MessageDefinitionAllowedResponse", const=True)

    message: fhirtypes.ReferenceType = Field(
        ...,
        alias="message",
        title="Reference to allowed message definition response",
        description=(
            "A reference to the message definition that must be adhered to by this "
            "supported response."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MessageDefinition"],
    )

    situation: fhirtypes.Markdown = Field(
        None,
        alias="situation",
        title="When should this response be used",
        description=(
            "Provides a description of the circumstances in which this response "
            "should be used (as opposed to one of the alternative responses)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    situation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_situation", title="Extension field for ``situation``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MessageDefinitionAllowedResponse`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "message", "situation"]


class MessageDefinitionFocus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource(s) that are the subject of the event.
    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """

    resource_type = Field("MessageDefinitionFocus", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type of resource",
        description="The kind of resource that must be the focus for this message.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Maximum number of focuses of this type",
        description=(
            "Identifies the maximum number of resources of this type that must be "
            "pointed to by a message in order for it to be valid against this "
            "MessageDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.UnsignedInt = Field(
        None,
        alias="min",
        title="Minimum number of focuses of this type",
        description=(
            "Identifies the minimum number of resources of this type that must be "
            "pointed to by a message in order for it to be valid against this "
            "MessageDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title="Profile that must be adhered to by focus",
        description=(
            "A profile that reflects constraints for the focal resource (and "
            "potentially for related resources)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MessageDefinitionFocus`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "profile", "min", "max"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2446(
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
