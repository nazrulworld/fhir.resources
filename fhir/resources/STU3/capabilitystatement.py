# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CapabilityStatement(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A statement of system capabilities.
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server functionality
    or a statement of required or desired server implementation.
    """

    resource_type = Field("CapabilityStatement", const=True)

    acceptUnknown: fhirtypes.Code = Field(
        ...,
        alias="acceptUnknown",
        title="Type `Code`",
        description="no | extensions | elements | both",
    )
    acceptUnknown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_acceptUnknown", title="Extension field for ``acceptUnknown``."
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Type `DateTime`",
        description="Date this was last changed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the capability statement",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    document: ListType[fhirtypes.CapabilityStatementDocumentType] = Field(
        None,
        alias="document",
        title=(
            "List of `CapabilityStatementDocument` items (represented as `dict` in "
            "JSON)"
        ),
        description="Document definition",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: fhirtypes.Id = Field(
        ...,
        alias="fhirVersion",
        title="Type `Id`",
        description="FHIR Version the system uses",
    )
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    format: ListType[fhirtypes.Code] = Field(
        ...,
        alias="format",
        title="List of `Code` items",
        description="formats supported (xml | json | ttl | mime type)",
    )
    format__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_format", title="Extension field for ``format``."
    )

    implementation: fhirtypes.CapabilityStatementImplementationType = Field(
        None,
        alias="implementation",
        title=(
            "Type `CapabilityStatementImplementation` (represented as `dict` in "
            "JSON)"
        ),
        description="If this describes a specific instance",
    )

    implementationGuide: ListType[fhirtypes.Uri] = Field(
        None,
        alias="implementationGuide",
        title="List of `Uri` items",
        description="Implementation guides supported",
    )
    implementationGuide__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_implementationGuide",
        title="Extension field for ``implementationGuide``.",
    )

    instantiates: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiates",
        title="List of `Uri` items",
        description="Canonical URL of another capability statement this implements",
    )
    instantiates__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiates", title="Extension field for ``instantiates``."
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for capability statement (if applicable)",
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="Type `Code`",
        description="instance | capability | requirements",
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    messaging: ListType[fhirtypes.CapabilityStatementMessagingType] = Field(
        None,
        alias="messaging",
        title=(
            "List of `CapabilityStatementMessaging` items (represented as `dict` in"
            " JSON)"
        ),
        description="If messaging is supported",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this capability statement (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    patchFormat: ListType[fhirtypes.Code] = Field(
        None,
        alias="patchFormat",
        title="List of `Code` items",
        description="Patch formats supported",
    )
    patchFormat__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_patchFormat", title="Extension field for ``patchFormat``.")

    profile: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="profile",
        title=(
            "List of `Reference` items referencing `StructureDefinition` "
            "(represented as `dict` in JSON)"
        ),
        description="Profiles for use cases supported",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String`",
        description="Name of the publisher (organization or individual)",
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown`",
        description="Why this capability statement is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    rest: ListType[fhirtypes.CapabilityStatementRestType] = Field(
        None,
        alias="rest",
        title=(
            "List of `CapabilityStatementRest` items (represented as `dict` in " "JSON)"
        ),
        description="If the endpoint is a RESTful one",
    )

    software: fhirtypes.CapabilityStatementSoftwareType = Field(
        None,
        alias="software",
        title="Type `CapabilityStatementSoftware` (represented as `dict` in JSON)",
        description="Software that is covered by this capability statement",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="draft | active | retired | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this capability statement (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this capability statement (globally unique)",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="Context the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Business version of the capability statement",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class CapabilityStatementDocument(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Document definition.
    A document definition.
    """

    resource_type = Field("CapabilityStatementDocument", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Description of document support",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    mode: fhirtypes.Code = Field(
        ..., alias="mode", title="Type `Code`", description="producer | consumer"
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    profile: fhirtypes.ReferenceType = Field(
        ...,
        alias="profile",
        title=(
            "Type `Reference` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Constraint on a resource used in the document",
    )


class CapabilityStatementImplementation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this describes a specific instance.
    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """

    resource_type = Field("CapabilityStatementImplementation", const=True)

    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Type `String`",
        description="Describes this specific instance",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Base URL for the installation",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )


class CapabilityStatementMessaging(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If messaging is supported.
    A description of the messaging capabilities of the solution.
    """

    resource_type = Field("CapabilityStatementMessaging", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Messaging interface behavior details",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    endpoint: ListType[fhirtypes.CapabilityStatementMessagingEndpointType] = Field(
        None,
        alias="endpoint",
        title=(
            "List of `CapabilityStatementMessagingEndpoint` items (represented as "
            "`dict` in JSON)"
        ),
        description="Where messages should be sent",
    )

    event: ListType[fhirtypes.CapabilityStatementMessagingEventType] = Field(
        None,
        alias="event",
        title=(
            "List of `CapabilityStatementMessagingEvent` items (represented as "
            "`dict` in JSON)"
        ),
        description="Declare support for this event",
    )

    reliableCache: fhirtypes.UnsignedInt = Field(
        None,
        alias="reliableCache",
        title="Type `UnsignedInt`",
        description="Reliable Message Cache Length (min)",
    )
    reliableCache__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reliableCache", title="Extension field for ``reliableCache``."
    )

    supportedMessage: ListType[
        fhirtypes.CapabilityStatementMessagingSupportedMessageType
    ] = Field(
        None,
        alias="supportedMessage",
        title=(
            "List of `CapabilityStatementMessagingSupportedMessage` items "
            "(represented as `dict` in JSON)"
        ),
        description="Messages supported by this system",
    )


class CapabilityStatementMessagingEndpoint(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Where messages should be sent.
    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """

    resource_type = Field("CapabilityStatementMessagingEndpoint", const=True)

    address: fhirtypes.Uri = Field(
        ...,
        alias="address",
        title="Type `Uri`",
        description="Network address or identifier of the end-point",
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_address", title="Extension field for ``address``."
    )

    protocol: fhirtypes.CodingType = Field(
        ...,
        alias="protocol",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="http | ftp | mllp +",
    )


class CapabilityStatementMessagingEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Declare support for this event.
    A description of the solution's support for an event at this end-point.
    """

    resource_type = Field("CapabilityStatementMessagingEvent", const=True)

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Type `Code`",
        description="Consequence | Currency | Notification",
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_category", title="Extension field for ``category``."
    )

    code: fhirtypes.CodingType = Field(
        ...,
        alias="code",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Event type",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Endpoint-specific event documentation",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    focus: fhirtypes.Code = Field(
        ...,
        alias="focus",
        title="Type `Code`",
        description="Resource that\u0027s focus of message",
    )
    focus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_focus", title="Extension field for ``focus``."
    )

    mode: fhirtypes.Code = Field(
        ..., alias="mode", title="Type `Code`", description="sender | receiver"
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    request: fhirtypes.ReferenceType = Field(
        ...,
        alias="request",
        title=(
            "Type `Reference` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Profile that describes the request",
    )

    response: fhirtypes.ReferenceType = Field(
        ...,
        alias="response",
        title=(
            "Type `Reference` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Profile that describes the response",
    )


class CapabilityStatementMessagingSupportedMessage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Messages supported by this system.
    References to message definitions for messages this system can send or
    receive.
    """

    resource_type = Field("CapabilityStatementMessagingSupportedMessage", const=True)

    definition: fhirtypes.ReferenceType = Field(
        ...,
        alias="definition",
        title=(
            "Type `Reference` referencing `MessageDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Message supported by this system",
    )

    mode: fhirtypes.Code = Field(
        ..., alias="mode", title="Type `Code`", description="sender | receiver"
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )


class CapabilityStatementRest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If the endpoint is a RESTful one.
    A definition of the restful capabilities of the solution, if any.
    """

    resource_type = Field("CapabilityStatementRest", const=True)

    compartment: ListType[fhirtypes.Uri] = Field(
        None,
        alias="compartment",
        title="List of `Uri` items",
        description="Compartments served/used by system",
    )
    compartment__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_compartment", title="Extension field for ``compartment``.")

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="General description of implementation",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    interaction: ListType[fhirtypes.CapabilityStatementRestInteractionType] = Field(
        None,
        alias="interaction",
        title=(
            "List of `CapabilityStatementRestInteraction` items (represented as "
            "`dict` in JSON)"
        ),
        description="What operations are supported?",
    )

    mode: fhirtypes.Code = Field(
        ..., alias="mode", title="Type `Code`", description="client | server"
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    operation: ListType[fhirtypes.CapabilityStatementRestOperationType] = Field(
        None,
        alias="operation",
        title=(
            "List of `CapabilityStatementRestOperation` items (represented as "
            "`dict` in JSON)"
        ),
        description="Definition of an operation or a custom query",
    )

    resource: ListType[fhirtypes.CapabilityStatementRestResourceType] = Field(
        None,
        alias="resource",
        title=(
            "List of `CapabilityStatementRestResource` items (represented as `dict`"
            " in JSON)"
        ),
        description="Resource served on the REST interface",
    )

    searchParam: ListType[
        fhirtypes.CapabilityStatementRestResourceSearchParamType
    ] = Field(
        None,
        alias="searchParam",
        title=(
            "List of `CapabilityStatementRestResourceSearchParam` items "
            "(represented as `dict` in JSON)"
        ),
        description="Search parameters for searching all resources",
    )

    security: fhirtypes.CapabilityStatementRestSecurityType = Field(
        None,
        alias="security",
        title="Type `CapabilityStatementRestSecurity` (represented as `dict` in JSON)",
        description="Information about security of implementation",
    )


class CapabilityStatementRestInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What operations are supported?.
    A specification of restful operations supported by the system.
    """

    resource_type = Field("CapabilityStatementRestInteraction", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="transaction | batch | search-system | history-system",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Anything special about operation behavior",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )


class CapabilityStatementRestOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an operation or a custom query.
    Definition of an operation or a named query together with its parameters
    and their meaning and type.
    """

    resource_type = Field("CapabilityStatementRestOperation", const=True)

    definition: fhirtypes.ReferenceType = Field(
        ...,
        alias="definition",
        title=(
            "Type `Reference` referencing `OperationDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="The defined operation/query",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Name by which the operation/query is invoked",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )


class CapabilityStatementRestResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource served on the REST interface.
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """

    resource_type = Field("CapabilityStatementRestResource", const=True)

    conditionalCreate: bool = Field(
        None,
        alias="conditionalCreate",
        title="Type `bool`",
        description="If allows/uses conditional create",
    )
    conditionalCreate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_conditionalCreate",
        title="Extension field for ``conditionalCreate``.",
    )

    conditionalDelete: fhirtypes.Code = Field(
        None,
        alias="conditionalDelete",
        title="Type `Code`",
        description=(
            "not-supported | single | multiple - how conditional delete is " "supported"
        ),
    )
    conditionalDelete__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_conditionalDelete",
        title="Extension field for ``conditionalDelete``.",
    )

    conditionalRead: fhirtypes.Code = Field(
        None,
        alias="conditionalRead",
        title="Type `Code`",
        description="not-supported | modified-since | not-match | full-support",
    )
    conditionalRead__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_conditionalRead", title="Extension field for ``conditionalRead``."
    )

    conditionalUpdate: bool = Field(
        None,
        alias="conditionalUpdate",
        title="Type `bool`",
        description="If allows/uses conditional update",
    )
    conditionalUpdate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_conditionalUpdate",
        title="Extension field for ``conditionalUpdate``.",
    )

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Type `Markdown`",
        description="Additional information about the use of the resource type",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    interaction: ListType[
        fhirtypes.CapabilityStatementRestResourceInteractionType
    ] = Field(
        ...,
        alias="interaction",
        title=(
            "List of `CapabilityStatementRestResourceInteraction` items "
            "(represented as `dict` in JSON)"
        ),
        description="What operations are supported?",
    )

    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title=(
            "Type `Reference` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Base System profile for all uses of resource",
    )

    readHistory: bool = Field(
        None,
        alias="readHistory",
        title="Type `bool`",
        description="Whether vRead can return past versions",
    )
    readHistory__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_readHistory", title="Extension field for ``readHistory``."
    )

    referencePolicy: ListType[fhirtypes.Code] = Field(
        None,
        alias="referencePolicy",
        title="List of `Code` items",
        description="literal | logical | resolves | enforced | local",
    )
    referencePolicy__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_referencePolicy", title="Extension field for ``referencePolicy``."
    )

    searchInclude: ListType[fhirtypes.String] = Field(
        None,
        alias="searchInclude",
        title="List of `String` items",
        description="_include values supported by the server",
    )
    searchInclude__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_searchInclude", title="Extension field for ``searchInclude``."
    )

    searchParam: ListType[
        fhirtypes.CapabilityStatementRestResourceSearchParamType
    ] = Field(
        None,
        alias="searchParam",
        title=(
            "List of `CapabilityStatementRestResourceSearchParam` items "
            "(represented as `dict` in JSON)"
        ),
        description="Search parameters supported by implementation",
    )

    searchRevInclude: ListType[fhirtypes.String] = Field(
        None,
        alias="searchRevInclude",
        title="List of `String` items",
        description="_revinclude values supported by the server",
    )
    searchRevInclude__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_searchRevInclude",
        title="Extension field for ``searchRevInclude``.",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="A resource type that is supported",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    updateCreate: bool = Field(
        None,
        alias="updateCreate",
        title="Type `bool`",
        description="If update can commit to a new identity",
    )
    updateCreate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_updateCreate", title="Extension field for ``updateCreate``."
    )

    versioning: fhirtypes.Code = Field(
        None,
        alias="versioning",
        title="Type `Code`",
        description="no-version | versioned | versioned-update",
    )
    versioning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versioning", title="Extension field for ``versioning``."
    )


class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What operations are supported?.
    Identifies a restful operation supported by the solution.
    """

    resource_type = Field("CapabilityStatementRestResourceInteraction", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description=(
            "read | vread | update | patch | delete | history-instance | history-"
            "type | create | search-type"
        ),
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Anything special about operation behavior",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )


class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search parameters supported by implementation.
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """

    resource_type = Field("CapabilityStatementRestResourceSearchParam", const=True)

    definition: fhirtypes.Uri = Field(
        None,
        alias="definition",
        title="Type `Uri`",
        description="Source of definition for parameter",
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Server-specific usage",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.String = Field(
        ..., alias="name", title="Type `String`", description="Name of search parameter"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description=(
            "number | date | string | token | reference | composite | quantity | " "uri"
        ),
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about security of implementation.
    Information about security implementation from an interface perspective -
    what a client needs to know.
    """

    resource_type = Field("CapabilityStatementRestSecurity", const=True)

    certificate: ListType[
        fhirtypes.CapabilityStatementRestSecurityCertificateType
    ] = Field(
        None,
        alias="certificate",
        title=(
            "List of `CapabilityStatementRestSecurityCertificate` items "
            "(represented as `dict` in JSON)"
        ),
        description="Certificates associated with security profiles",
    )

    cors: bool = Field(
        None,
        alias="cors",
        title="Type `bool`",
        description="Adds CORS Headers (http://enable-cors.org/)",
    )
    cors__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_cors", title="Extension field for ``cors``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="General description of how security works",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    service: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="service",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates",
    )


class CapabilityStatementRestSecurityCertificate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Certificates associated with security profiles.
    """

    resource_type = Field("CapabilityStatementRestSecurityCertificate", const=True)

    blob: fhirtypes.Base64Binary = Field(
        None,
        alias="blob",
        title="Type `Base64Binary`",
        description="Actual certificate",
    )
    blob__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_blob", title="Extension field for ``blob``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`",
        description="Mime type for certificates",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class CapabilityStatementSoftware(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Software that is covered by this capability statement.
    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    resource_type = Field("CapabilityStatementSoftware", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="A name the software is known by",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    releaseDate: fhirtypes.DateTime = Field(
        None,
        alias="releaseDate",
        title="Type `DateTime`",
        description="Date this version released",
    )
    releaseDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_releaseDate", title="Extension field for ``releaseDate``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Version covered by this statement",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )
