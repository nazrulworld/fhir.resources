# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class AuditEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event record kept for security purposes.
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    resource_type = Field("AuditEvent", const=True)

    action: fhirtypes.Code = Field(
        None,
        alias="action",
        title="Type `Code`",
        description="Type of action performed during the event",
    )
    action__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_action", title="Extension field for ``action``."
    )

    agent: ListType[fhirtypes.AuditEventAgentType] = Field(
        ...,
        alias="agent",
        title="List of `AuditEventAgent` items (represented as `dict` in JSON)",
        description="Actor involved in the event",
    )

    entity: ListType[fhirtypes.AuditEventEntityType] = Field(
        None,
        alias="entity",
        title="List of `AuditEventEntity` items (represented as `dict` in JSON)",
        description="Data or objects used",
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="Type `Code`",
        description="Whether the event succeeded or failed",
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    outcomeDesc: fhirtypes.String = Field(
        None,
        alias="outcomeDesc",
        title="Type `String`",
        description="Description of the event outcome",
    )
    outcomeDesc__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_outcomeDesc", title="Extension field for ``outcomeDesc``."
    )

    purposeOfEvent: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="purposeOfEvent",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The purposeOfUse of the event",
    )

    recorded: fhirtypes.Instant = Field(
        ...,
        alias="recorded",
        title="Type `Instant`",
        description="Time when the event occurred on source",
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    source: fhirtypes.AuditEventSourceType = Field(
        ...,
        alias="source",
        title="Type `AuditEventSource` (represented as `dict` in JSON)",
        description="Audit Event Reporter",
    )

    subtype: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="subtype",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="More specific type/id for the event",
    )

    type: fhirtypes.CodingType = Field(
        ...,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Type/identifier of event",
    )


class AuditEventAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor involved in the event.
    An actor taking an active role in the event or activity that is logged.
    """

    resource_type = Field("AuditEventAgent", const=True)

    altId: fhirtypes.String = Field(
        None,
        alias="altId",
        title="Type `String`",
        description="Alternative User id e.g. authentication",
    )
    altId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_altId", title="Extension field for ``altId``."
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Where",
    )

    media: fhirtypes.CodingType = Field(
        None,
        alias="media",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Type of media",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Human-meaningful name for the agent",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.AuditEventAgentNetworkType = Field(
        None,
        alias="network",
        title="Type `AuditEventAgentNetwork` (represented as `dict` in JSON)",
        description="Logical network location for application activity",
    )

    policy: ListType[fhirtypes.Uri] = Field(
        None,
        alias="policy",
        title="List of `Uri` items",
        description="Policy that authorized event",
    )
    policy__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_policy", title="Extension field for ``policy``."
    )

    purposeOfUse: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="purposeOfUse",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason given for this user",
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title=(
            "Type `Reference` referencing `Practitioner, Organization, Device, "
            "Patient, RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Direct reference to resource",
    )

    requestor: bool = Field(
        ...,
        alias="requestor",
        title="Type `bool`",
        description="Whether user is initiator",
    )
    requestor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requestor", title="Extension field for ``requestor``."
    )

    role: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Agent role in the event",
    )

    userId: fhirtypes.IdentifierType = Field(
        None,
        alias="userId",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique identifier for the user",
    )


class AuditEventAgentNetwork(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Logical network location for application activity.
    Logical network location for application activity, if the activity has a
    network location.
    """

    resource_type = Field("AuditEventAgentNetwork", const=True)

    address: fhirtypes.String = Field(
        None,
        alias="address",
        title="Type `String`",
        description="Identifier for the network access point of the user device",
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_address", title="Extension field for ``address``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`",
        description="The type of network access point",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class AuditEventEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data or objects used.
    Specific instances of data or objects that have been accessed.
    """

    resource_type = Field("AuditEventEntity", const=True)

    description: fhirtypes.String = Field(
        None, alias="description", title="Type `String`", description="Descriptive text"
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    detail: ListType[fhirtypes.AuditEventEntityDetailType] = Field(
        None,
        alias="detail",
        title="List of `AuditEventEntityDetail` items (represented as `dict` in JSON)",
        description="Additional Information about the entity",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Specific instance of object",
    )

    lifecycle: fhirtypes.CodingType = Field(
        None,
        alias="lifecycle",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Life-cycle stage for the entity",
    )

    name: fhirtypes.String = Field(
        None, alias="name", title="Type `String`", description="Descriptor for entity"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    query: fhirtypes.Base64Binary = Field(
        None, alias="query", title="Type `Base64Binary`", description="Query parameters"
    )
    query__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_query", title="Extension field for ``query``."
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Specific instance of resource",
    )

    role: fhirtypes.CodingType = Field(
        None,
        alias="role",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="What role the entity played",
    )

    securityLabel: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Security labels on the entity",
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Type of entity involved",
    )


class AuditEventEntityDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional Information about the entity.
    Tagged value pairs for conveying additional information about the entity.
    """

    resource_type = Field("AuditEventEntityDetail", const=True)

    type: fhirtypes.String = Field(
        ..., alias="type", title="Type `String`", description="Name of the property"
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    value: fhirtypes.Base64Binary = Field(
        ..., alias="value", title="Type `Base64Binary`", description="Property value"
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class AuditEventSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Audit Event Reporter.
    The system that is reporting the event.
    """

    resource_type = Field("AuditEventSource", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="The identity of source detecting the event",
    )

    site: fhirtypes.String = Field(
        None,
        alias="site",
        title="Type `String`",
        description="Logical source location within the enterprise",
    )
    site__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_site", title="Extension field for ``site``."
    )

    type: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="type",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="The type of source where event originated",
    )
