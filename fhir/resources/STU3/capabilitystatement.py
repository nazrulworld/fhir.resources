# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CapabilityStatement(domainresource.DomainResource):
    """ A statement of system capabilities.
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server functionality
    or a statement of required or desired server implementation.
    """

    resource_type = Field("CapabilityStatement", const=True)

    acceptUnknown: fhirtypes.Code = Field(
        ...,
        alias="acceptUnknown",
        title="Type `Code` (represented as `dict` in JSON)",
        description="no | extensions | elements | both",
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
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date this was last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the capability statement",
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

    fhirVersion: fhirtypes.Id = Field(
        ...,
        alias="fhirVersion",
        title="Type `Id` (represented as `dict` in JSON)",
        description="FHIR Version the system uses",
    )

    format: ListType[fhirtypes.Code] = Field(
        ...,
        alias="format",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="formats supported (xml | json | ttl | mime type)",
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
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Implementation guides supported",
    )

    instantiates: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiates",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Canonical URL of another capability statement this implements",
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="instance | capability | requirements",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this capability statement (computer friendly)",
    )

    patchFormat: ListType[fhirtypes.Code] = Field(
        None,
        alias="patchFormat",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Patch formats supported",
    )

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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Why this capability statement is defined",
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this capability statement (human friendly)",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this capability statement (globally unique)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the capability statement",
    )


class CapabilityStatementDocument(backboneelement.BackboneElement):
    """ Document definition.
    A document definition.
    """

    resource_type = Field("CapabilityStatementDocument", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of document support",
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="producer | consumer",
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
    """ If this describes a specific instance.
    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """

    resource_type = Field("CapabilityStatementImplementation", const=True)

    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Describes this specific instance",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Base URL for the installation",
    )


class CapabilityStatementMessaging(backboneelement.BackboneElement):
    """ If messaging is supported.
    A description of the messaging capabilities of the solution.
    """

    resource_type = Field("CapabilityStatementMessaging", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Messaging interface behavior details",
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
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Reliable Message Cache Length (min)",
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
    """ Where messages should be sent.
    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """

    resource_type = Field("CapabilityStatementMessagingEndpoint", const=True)

    address: fhirtypes.Uri = Field(
        ...,
        alias="address",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Network address or identifier of the end-point",
    )

    protocol: fhirtypes.CodingType = Field(
        ...,
        alias="protocol",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="http | ftp | mllp +",
    )


class CapabilityStatementMessagingEvent(backboneelement.BackboneElement):
    """ Declare support for this event.
    A description of the solution's support for an event at this end-point.
    """

    resource_type = Field("CapabilityStatementMessagingEvent", const=True)

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Consequence | Currency | Notification",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Endpoint-specific event documentation",
    )

    focus: fhirtypes.Code = Field(
        ...,
        alias="focus",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Resource that\u0027s focus of message",
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="sender | receiver",
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
    """ Messages supported by this system.
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
        ...,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="sender | receiver",
    )


class CapabilityStatementRest(backboneelement.BackboneElement):
    """ If the endpoint is a RESTful one.
    A definition of the restful capabilities of the solution, if any.
    """

    resource_type = Field("CapabilityStatementRest", const=True)

    compartment: ListType[fhirtypes.Uri] = Field(
        None,
        alias="compartment",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Compartments served/used by system",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="General description of implementation",
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
        ...,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="client | server",
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
    """ What operations are supported?.
    A specification of restful operations supported by the system.
    """

    resource_type = Field("CapabilityStatementRestInteraction", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="transaction | batch | search-system | history-system",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Anything special about operation behavior",
    )


class CapabilityStatementRestOperation(backboneelement.BackboneElement):
    """ Definition of an operation or a custom query.
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name by which the operation/query is invoked",
    )


class CapabilityStatementRestResource(backboneelement.BackboneElement):
    """ Resource served on the REST interface.
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

    conditionalDelete: fhirtypes.Code = Field(
        None,
        alias="conditionalDelete",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "not-supported | single | multiple - how conditional delete is " "supported"
        ),
    )

    conditionalRead: fhirtypes.Code = Field(
        None,
        alias="conditionalRead",
        title="Type `Code` (represented as `dict` in JSON)",
        description="not-supported | modified-since | not-match | full-support",
    )

    conditionalUpdate: bool = Field(
        None,
        alias="conditionalUpdate",
        title="Type `bool`",
        description="If allows/uses conditional update",
    )

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Additional information about the use of the resource type",
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

    referencePolicy: ListType[fhirtypes.Code] = Field(
        None,
        alias="referencePolicy",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="literal | logical | resolves | enforced | local",
    )

    searchInclude: ListType[fhirtypes.String] = Field(
        None,
        alias="searchInclude",
        title="List of `String` items (represented as `dict` in JSON)",
        description="_include values supported by the server",
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
        title="List of `String` items (represented as `dict` in JSON)",
        description="_revinclude values supported by the server",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="A resource type that is supported",
    )

    updateCreate: bool = Field(
        None,
        alias="updateCreate",
        title="Type `bool`",
        description="If update can commit to a new identity",
    )

    versioning: fhirtypes.Code = Field(
        None,
        alias="versioning",
        title="Type `Code` (represented as `dict` in JSON)",
        description="no-version | versioned | versioned-update",
    )


class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    Identifies a restful operation supported by the solution.
    """

    resource_type = Field("CapabilityStatementRestResourceInteraction", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "read | vread | update | patch | delete | history-instance | history-"
            "type | create | search-type"
        ),
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Anything special about operation behavior",
    )


class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    """ Search parameters supported by implementation.
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """

    resource_type = Field("CapabilityStatementRestResourceSearchParam", const=True)

    definition: fhirtypes.Uri = Field(
        None,
        alias="definition",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Source of definition for parameter",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Server-specific usage",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of search parameter",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "number | date | string | token | reference | composite | quantity | " "uri"
        ),
    )


class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
    """ Information about security of implementation.
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

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="General description of how security works",
    )

    service: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="service",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates",
    )


class CapabilityStatementRestSecurityCertificate(backboneelement.BackboneElement):
    """ Certificates associated with security profiles.
    """

    resource_type = Field("CapabilityStatementRestSecurityCertificate", const=True)

    blob: fhirtypes.Base64Binary = Field(
        None,
        alias="blob",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="Actual certificate",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Mime type for certificates",
    )


class CapabilityStatementSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this capability statement.
    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    resource_type = Field("CapabilityStatementSoftware", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="A name the software is known by",
    )

    releaseDate: fhirtypes.DateTime = Field(
        None,
        alias="releaseDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date this version released",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Version covered by this statement",
    )
