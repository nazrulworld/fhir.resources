from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

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

    __resource_type__ = "MessageDefinition"

    allowedResponse: typing.List[fhirtypes.MessageDefinitionAllowedResponseType] | None = Field(  # type: ignore
        None,
        alias="allowedResponse",
        title="Responses to this message",
        description=(
            "Indicates what types of messages may be sent as an application-level "
            "response to this message."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    base: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="base",
        title="Definition this one is based on",
        description=(
            "The MessageDefinition that is the basis for the contents of this "
            "resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MessageDefinition"],
        },
    )
    base__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_base", title="Extension field for ``base``."
    )

    category: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="category",
        title="consequence | currency | notification",
        description="The impact of the content of the message.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["consequence", "currency", "notification"],
        },
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_category", title="Extension field for ``category``."
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the message definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the message definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the message definition was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the message definition changes."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the message definition",
        description=(
            "A free text natural language description of the message definition "
            "from a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    eventCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="eventCoding",
        title="Event code  or link to the EventDefinition",
        description="Event code or link to the EventDefinition.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e event[x]
            "one_of_many": "event",
            "one_of_many_required": True,
        },
    )

    eventUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="eventUri",
        title="Event code  or link to the EventDefinition",
        description="Event code or link to the EventDefinition.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e event[x]
            "one_of_many": "event",
            "one_of_many_required": True,
        },
    )
    eventUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_eventUri", title="Extension field for ``eventUri``."
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this message definition is authored "
            "for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    focus: typing.List[fhirtypes.MessageDefinitionFocusType] | None = Field(  # type: ignore
        None,
        alias="focus",
        title="Resource(s) that are the subject of the event",
        description=(
            "Identifies the resource (or resources) that are being addressed by the"
            " event.  For example, the Encounter for an admit message or two "
            "Account records for a merge."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    graph: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="graph",
        title="Canonical reference to a GraphDefinition",
        description=(
            "Canonical reference to a GraphDefinition. If a URL is provided, it is "
            "the canonical reference to a [GraphDefinition](graphdefinition.html) "
            "that it controls what resources are to be added to the bundle when "
            "building the document. The GraphDefinition can also specify profiles "
            "that apply to the various resources."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["GraphDefinition"],
        },
    )
    graph__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_graph", title="Extension field for ``graph``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Primary key for the message definition on a given server",
        description=(
            "A formal identifier that is used to identify this message definition "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for message definition (if applicable)",
        description=(
            "A legal or geographic region in which the message definition is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this message definition (computer friendly)",
        description=(
            "A natural language name identifying the message definition. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    parent: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="parent",
        title="Protocol/workflow this is part of",
        description=(
            "Identifies a protocol or workflow that this MessageDefinition "
            "represents a step in."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ActivityDefinition", "PlanDefinition"],
        },
    )
    parent__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_parent", title="Extension field for ``parent``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the message "
            "definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="Why this message definition is defined",
        description=(
            "Explanation of why this message definition is needed and why it has "
            "been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    replaces: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="replaces",
        title="Takes the place of",
        description="A MessageDefinition that is superseded by this definition.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MessageDefinition"],
        },
    )
    replaces__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_replaces", title="Extension field for ``replaces``."
    )

    responseRequired: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="responseRequired",
        title="always | on-error | never | on-success",
        description=(
            "Declare at a message definition level whether a response is required "
            "or only upon error or success, or never."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["always", "on-error", "never", "on-success"],
        },
    )
    responseRequired__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_responseRequired",
        title="Extension field for ``responseRequired``.",
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this message definition. Enables tracking the life-cycle"
            " of the content."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this message definition (human friendly)",
        description="A short, descriptive, user-friendly title for the message definition.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Business Identifier for a given MessageDefinition",
        description=(
            "The business identifier that is used to reference the "
            "MessageDefinition and *is* expected to be consistent from server to "
            "server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate message definition instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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
            "replaces",
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
            "eventCoding",
            "eventUri",
            "category",
            "focus",
            "responseRequired",
            "allowedResponse",
            "graph",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("date", "date__ext"), ("status", "status__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        one_of_many_fields = {"event": ["eventCoding", "eventUri"]}
        return one_of_many_fields


class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Responses to this message.
    Indicates what types of messages may be sent as an application-level
    response to this message.
    """

    __resource_type__ = "MessageDefinitionAllowedResponse"

    message: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="message",
        title="Reference to allowed message definition response",
        description=(
            "A reference to the message definition that must be adhered to by this "
            "supported response."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MessageDefinition"],
        },
    )
    message__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_message", title="Extension field for ``message``."
    )

    situation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="situation",
        title="When should this response be used",
        description=(
            "Provides a description of the circumstances in which this response "
            "should be used (as opposed to one of the alternative responses)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    situation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_situation", title="Extension field for ``situation``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MessageDefinitionAllowedResponse`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "message", "situation"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("message", "message__ext")]
        return required_fields


class MessageDefinitionFocus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource(s) that are the subject of the event.
    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """

    __resource_type__ = "MessageDefinitionFocus"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Type of resource",
        description="The kind of resource that must be the focus for this message.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    max: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="max",
        title="Maximum number of focuses of this type",
        description=(
            "Identifies the maximum number of resources of this type that must be "
            "pointed to by a message in order for it to be valid against this "
            "MessageDefinition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="min",
        title="Minimum number of focuses of this type",
        description=(
            "Identifies the minimum number of resources of this type that must be "
            "pointed to by a message in order for it to be valid against this "
            "MessageDefinition."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_min", title="Extension field for ``min``."
    )

    profile: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="profile",
        title="Profile that must be adhered to by focus",
        description=(
            "A profile that reflects constraints for the focal resource (and "
            "potentially for related resources)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_profile", title="Extension field for ``profile``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MessageDefinitionFocus`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "profile", "min", "max"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("min", "min__ext")]
        return required_fields
