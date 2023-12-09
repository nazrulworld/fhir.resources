# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Conformance
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Conformance(DomainResource):
    """A conformance statement.

    A conformance statement is a set of capabilities of a FHIR Server that may
    be used as a statement of actual server functionality or a statement of
    required or desired server implementation.
    """

    resource_type = Field("Conformance", const=True)

    acceptUnknown: fhirtypes.Code = Field(
        ...,
        alias="acceptUnknown",
        title="Type `Code`.",
        description="no | extensions | elements | both.",
    )

    contact: ListType[fhirtypes.ConformanceContactType] = Field(
        None,
        alias="contact",
        title="List of `ConformanceContact` items (represented as `dict` in JSON).",
        description="Contact details of the publisher.",
    )
    copyright: fhirtypes.String = Field(
        None,
        alias="copyright",
        title="Type `String`.",
        description="Use and/or publishing restrictions.",
    )
    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`.",
        description="Publication Date(/time).",
    )
    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`.",
        description="Human description of the conformance statement.",
    )

    document: ListType[fhirtypes.ConformanceDocumentType] = Field(
        None,
        alias="document",
        title="List of `ConformanceDocument` items (represented as `dict` in JSON).",
        description="Document definition.",
    )

    experimental: fhirtypes.Boolean = Field(
        None,
        alias="experimental",
        title="Type `Boolean`.",
        description="If for testing purposes, not real usage.",
    )
    fhirVersion: fhirtypes.Code = Field(
        ...,
        alias="fhirVersion",
        title="Type `Code`.",
        description="FHIR Version the system uses.",
    )

    format: ListType[fhirtypes.Code] = Field(
        None,
        alias="format",
        title="List of `Code` item.",
        description="formats supported (xml | json | mime type).",
    )

    implementation: fhirtypes.ConformanceImplementationType = Field(
        None,
        alias="implementation",
        title="Type `ConformanceImplementation` (represented as `dict` in JSON).",
        description="If this describes a specific instance.",
    )

    kind: fhirtypes.Code = Field(
        None,
        alias="kind",
        title="Type `Code`.",
        description="instance | capability | requirements.",
    )

    messaging: ListType[fhirtypes.ConformanceMessagingType] = Field(
        None,
        alias="messaging",
        title="List of `ConformanceMessaging` items (represented as `dict` in JSON).",
        description="If messaging is supported.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`.",
        description="informal name for this conformance statement.",
    )
    profile: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="profile",
        title=(
            "List of `Reference` items referencing "
            "`StructureDefinition` (represented as `dict` in JSON)."
        ),
        description="Profiles for use cases supported.",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String`.",
        description="Name of the publisher (Organization or individual).",
    )
    requirements: fhirtypes.String = Field(
        None,
        alias="requirements",
        title="Type `String`.",
        description="Why is this needed?.",
    )

    rest: ListType[fhirtypes.ConformanceRestType] = Field(
        None,
        alias="rest",
        title="List of `ConformanceRest` (represented as `dict` in JSON).",
        description="If the endpoint is a RESTful one.",
    )
    software: fhirtypes.ConformanceSoftwareType = Field(
        None,
        alias="software",
        title="List of `ConformanceSoftware` (represented as `dict` in JSON).",
        description="Software that is covered by this conformance statement.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`.",
        description="draft | active | retired.",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`.",
        description="Logical uri to reference this statement.",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`.",
        description="Logical id for this version of the statement.",
    )


class ConformanceContact(BackboneElement):
    """Contact details of the publisher.

    Contacts to assist a user in finding and communicating with the publisher.
    """

    resource_type = Field("ConformanceContact", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`.",
        description="Name of a individual to contact.",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Contact details for individual or publisher.",
    )


class ConformanceDocument(BackboneElement):
    """Document definition.

    A document definition.
    """

    resource_type = Field("ConformanceDocument", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`.",
        description="Description of document support.",
    )

    mode: fhirtypes.Code = Field(
        None, alias="mode", title="Type `Code`.", description="producer | consumer."
    )
    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title=(
            "Type `Reference` referencing `StructureDefinition`"
            " (represented as `dict` in JSON)."
        ),
        description="Constraint on a resource used in the document.",
    )


class ConformanceImplementation(BackboneElement):
    """If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    conformance statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """

    resource_type = Field("ConformanceImplementation", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`.",
        description="Describes this specific instance.",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`.",
        description="Base URL for the installation.",
    )


class ConformanceMessaging(BackboneElement):
    """If messaging is supported.

    A description of the messaging capabilities of the solution.
    """

    resource_type = Field("ConformanceMessaging", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`.",
        description="Messaging interface behavior details.",
    )

    endpoint: ListType[fhirtypes.ConformanceMessagingEndpointType] = Field(
        None,
        alias="endpoint",
        title="List of `ConformanceMessagingEndpoint` items (represented as `dict` in JSON).",
        description="A messaging service end-point.",
    )
    event: ListType[fhirtypes.ConformanceMessagingEventType] = Field(
        None,
        alias="event",
        title="List of `ConformanceMessagingEvent` items (represented as `dict` in JSON).",
        description="Declare support for this event.",
    )

    reliableCache: fhirtypes.UnsignedInt = Field(
        None,
        alias="reliableCache",
        title="Type `UnsignedInt`.",
        description="Reliable Message Cache Length (min).",
    )


class ConformanceMessagingEndpoint(BackboneElement):
    """A messaging service end-point.

    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """

    resource_type = Field("ConformanceMessagingEndpoint", const=True)

    address: fhirtypes.Uri = Field(
        None, alias="address", title="Type `Uri`.", description="Address of end-point."
    )

    protocol: fhirtypes.CodingType = Field(
        ..., alias="protocol", title="Type `Code`.", description="http | ftp | mllp +."
    )


class ConformanceMessagingEvent(BackboneElement):
    """Declare support for this event.

    A description of the solution's support for an event at this end-point.
    """

    resource_type = Field("ConformanceMessagingEvent", const=True)

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Type `Code`.",
        description="Consequence | Currency | Notification.",
    )

    code: fhirtypes.CodingType = Field(
        None, alias="code", title="Type `Coding`.", description="Event type."
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`.",
        description="Endpoint-specific event documentation.",
    )

    focus: fhirtypes.Code = Field(
        None,
        alias="focus",
        title="Type `Code`.",
        description="Resource that's focus of message.",
    )

    mode: fhirtypes.Code = Field(
        None, alias="mode", title="Type `Code`.", description="sender | receiver."
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title=(
            "Type `Reference` referencing `StructureDefinition`"
            " (represented as `dict` in JSON)."
        ),
        description="Profile that describes the request.",
    )
    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title=(
            "Type `Reference` referencing `StructureDefinition`"
            " (represented as `dict` in JSON)."
        ),
        description="Profile that describes the response.",
    )


class ConformanceRest(BackboneElement):
    """If the endpoint is a RESTful one.

    A definition of the restful capabilities of the solution, if any.
    """

    resource_type = Field("ConformanceRest", const=True)

    compartment: ListType[fhirtypes.Uri] = Field(
        None,
        alias="compartment",
        title="List of `Uri` item.",
        description="Compartments served/used by system.",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="`Uri` item.",
        description="General description of implementation.",
    )
    interaction: ListType[fhirtypes.ConformanceRestInteractionType] = Field(
        None,
        alias="interaction",
        title="List of `ConformanceRestInteraction` items (represented as `dict` in JSON).",
        description="What operations are supported?.",
    )

    mode: fhirtypes.Code = Field(
        ..., alias="mode", title="Type `Code`", description="client | server."
    )

    operation: ListType[fhirtypes.ConformanceRestOperationType] = Field(
        None,
        alias="operation",
        title="List of `ConformanceRestOperation` items (represented as `dict` in JSON).",
        description="Definition of an operation or a custom query.",
    )

    resource: ListType[fhirtypes.ConformanceRestResourceType] = Field(
        None,
        alias="resource",
        title="List of `ConformanceRestResource` items (represented as `dict` in JSON).",
        description="Resource served on the REST interface.",
    )
    searchParam: ListType[fhirtypes.ConformanceRestResourceSearchParamType] = Field(
        None,
        alias="searchParam",
        title=(
            "List of `ConformanceRestResourceSearchParam` "
            "items (represented as `dict` in JSON)."
        ),
        description="Search params for searching all resources.",
    )

    security: fhirtypes.ConformanceRestSecurityType = Field(
        None,
        alias="security",
        title="List of `ConformanceRestSecurity` items (represented as `dict` in JSON).",
        description="Information about security of implementation.",
    )

    transactionMode: fhirtypes.Code = Field(
        None,
        alias="transactionMode",
        title="Type `Code`",
        description="not-supported | batch | transaction | both.",
    )


class ConformanceRestInteraction(BackboneElement):
    """What operations are supported?.

    A specification of restful operations supported by the system.
    """

    resource_type = Field("ConformanceRestInteraction", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="transaction | search-system | history-system.",
    )
    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Anything special about operation behavior.",
    )


class ConformanceRestOperation(BackboneElement):
    """Definition of an operation or a custom query.

    Definition of an operation or a named query and with its parameters and
    their meaning and type.
    """

    resource_type = Field("ConformanceRestOperation", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Name by which the operation/query is invoked.",
    )
    definition: fhirtypes.ReferenceType = Field(
        ...,
        alias="definition",
        title=(
            "Type `Reference` referencing `OperationDefinition`"
            " (represented as `dict` in JSON)."
        ),
        description=None,
    )


class ConformanceRestResource(BackboneElement):
    """Resource served on the REST interface.

    A specification of the restful capabilities of the solution for a specific
    resource type.
    """

    resource_type = Field("ConformanceRestResource", const=True)

    conditionalCreate: fhirtypes.Boolean = Field(
        None,
        alias="conditionalCreate",
        title="Type `Boolean`",
        description="If allows/uses conditional create.",
    )

    conditionalDelete: fhirtypes.Code = Field(
        None,
        alias="conditionalDelete",
        title="Type `Code`",
        description="not-supported | single | multiple - how conditional delete is supported.",
    )

    conditionalUpdate: fhirtypes.Boolean = Field(
        None,
        alias="conditionalUpdate",
        title="Type `Boolean`",
        description="If allows/uses conditional update.",
    )

    interaction: ListType[fhirtypes.ConformanceRestResourceInteractionType] = Field(
        None,
        alias="interaction",
        title=(
            "List of `ConformanceRestResourceInteraction` "
            "items (represented as `dict` in JSON)."
        ),
        description="What operations are supported?.",
    )

    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title=(
            "Type `Reference` referencing `StructureDefinition`"
            " (represented as `dict` in JSON)."
        ),
        description="Base System profile for all uses of resource.",
    )

    readHistory: fhirtypes.Boolean = Field(
        None,
        alias="readHistory",
        title="Type `Boolean`",
        description="Whether vRead can return past versions.",
    )

    searchInclude: ListType[fhirtypes.String] = Field(
        None,
        alias="searchInclude",
        title="List of `str` items.",
        description="_include values supported by the server.",
    )
    searchParam: ListType[fhirtypes.ConformanceRestResourceSearchParamType] = Field(
        None,
        alias="searchParam",
        title=(
            "List of `ConformanceRestResourceSearchParam` items "
            "(represented as `dict` in JSON)."
        ),
        description="Search params supported by implementation.",
    )
    searchRevInclude: ListType[fhirtypes.String] = Field(
        None,
        alias="searchRevInclude",
        title="List of `str` items.",
        description="_revinclude values supported by the server.",
    )
    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`",
        description="A resource type that is supported.",
    )

    updateCreate: fhirtypes.Boolean = Field(
        None,
        alias="updateCreate",
        title="Type `Boolean`",
        description="If update can commit to a new identity.",
    )

    versioning: fhirtypes.Code = Field(
        None,
        alias="versioning",
        title="Type `Code`",
        description="no-version | versioned | versioned-update.",
    )


class ConformanceRestResourceInteraction(BackboneElement):
    """What operations are supported?.

    Identifies a restful operation supported by the solution.
    """

    resource_type = Field("ConformanceRestResourceInteraction", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code`",
        description=(
            "read | vread | update | delete | history-instance |"
            " validate | history-type | create | search-type."
        ),
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Anything special about operation behavior.",
    )


class ConformanceRestResourceSearchParam(BackboneElement):
    """Search params supported by implementation.

    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """

    resource_type = Field("ConformanceRestResourceSearchParam", const=True)

    chain: ListType[fhirtypes.String] = Field(
        None,
        alias="chain",
        title="List of `str` items.",
        description="Chained names supported.",
    )

    definition: fhirtypes.Uri = Field(
        None,
        alias="definition",
        title="Type Uri",
        description="Source of definition for parameter.",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type String",
        description="Server-specific usage.",
    )

    modifier: ListType[fhirtypes.Code] = Field(
        None,
        alias="modifier",
        title="List of `Code` items.",
        description=(
            "missing | exact | contains | not | text | "
            "in | not-in | below | above | type."
        ),
    )

    name: fhirtypes.String = Field(
        None, alias="name", title="Type String", description="Name of search parameter."
    )

    target: ListType[fhirtypes.Code] = Field(
        None,
        alias="target",
        title="List of `Code` items.",
        description="Types of resource (if a resource reference).",
    )
    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type Code",
        description="number | date | string | token | reference | composite | quantity | uri.",
    )


class ConformanceRestSecurity(BackboneElement):
    """Information about security of implementation.

    Information about security implementation from an interface perspective -
    what a client needs to know.
    """

    resource_type = Field("ConformanceRestSecurity", const=True)

    certificate: ListType[fhirtypes.ConformanceRestSecurityCertificateType] = Field(
        None,
        alias="certificate",
        title=(
            "List of `ConformanceRestSecurityCertificate` "
            "items (represented as `dict` in JSON)."
        ),
        description="Certificates associated with security profiles.",
    )

    cors: fhirtypes.Boolean = Field(
        None,
        alias="cors",
        title="Type `bool`.",
        description="Adds CORS Headers (http://enable-cors.org/).",
    )
    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`.",
        description="General description of how security works.",
    )

    service: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="service",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates.",
    )


class ConformanceRestSecurityCertificate(BackboneElement):
    """Certificates associated with security profiles."""

    resource_type = Field("ConformanceRestSecurityCertificate", const=True)
    blob: fhirtypes.Base64Binary = Field(
        None,
        alias="blob",
        title="Type `Base64Binary`.",
        description="Actual certificate.",
    )
    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`.",
        description="Mime type for certificate.",
    )


class ConformanceSoftware(BackboneElement):
    """Software that is covered by this conformance statement.

    Software that is covered by this conformance statement.  It is used when
    the conformance statement describes the capabilities of a particular
    software version, independent of an installation.
    """

    resource_type = Field("ConformanceSoftware", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`.",
        description="A name the software is known by.",
    )
    releaseDate: fhirtypes.DateTime = Field(
        None,
        alias="releaseDate",
        title="Type `DateTime`.",
        description="Date this version released.",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`.",
        description="Version covered by this statement.",
    )
