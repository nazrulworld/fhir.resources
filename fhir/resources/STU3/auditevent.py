from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class AuditEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event record kept for security purposes.
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __resource_type__ = "AuditEvent"

    action: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="action",
        title="Type of action performed during the event",
        description=(
            "Indicator for type of action performed during the event that generated"
            " the audit."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    action__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_action", title="Extension field for ``action``."
    )

    agent: typing.List[fhirtypes.AuditEventAgentType] = Field(  # type: ignore
        ...,
        alias="agent",
        title="Actor involved in the event",
        description=(
            "An actor taking an active role in the event or activity that is " "logged."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    entity: typing.List[fhirtypes.AuditEventEntityType] | None = Field(  # type: ignore
        None,
        alias="entity",
        title="Data or objects used",
        description="Specific instances of data or objects that have been accessed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    outcome: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="Whether the event succeeded or failed",
        description="Indicates whether the event succeeded or failed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    outcomeDesc: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="outcomeDesc",
        title="Description of the event outcome",
        description="A free text description of the outcome of the event.",
        json_schema_extra={
            "element_property": True,
        },
    )
    outcomeDesc__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_outcomeDesc", title="Extension field for ``outcomeDesc``."
    )

    purposeOfEvent: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="purposeOfEvent",
        title="The purposeOfUse of the event",
        description=(
            "The purposeOfUse (reason) that was used during the event being "
            "recorded."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    recorded: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="recorded",
        title="Time when the event occurred on source",
        description="The time when the event occurred on the source.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    source: fhirtypes.AuditEventSourceType = Field(  # type: ignore
        ...,
        alias="source",
        title="Audit Event Reporter",
        description="The system that is reporting the event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subtype: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="subtype",
        title="More specific type/id for the event",
        description="Identifier for the category of event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type/identifier of event",
        description=(
            "Identifier for a family of the event.  For example, a menu item, "
            "program, rule, policy, function code, application name or URL. It "
            "identifies the performed function."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEvent`` according specification,
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
            "type",
            "subtype",
            "action",
            "recorded",
            "outcome",
            "outcomeDesc",
            "purposeOfEvent",
            "agent",
            "source",
            "entity",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("recorded", "recorded__ext")]
        return required_fields


class AuditEventAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor involved in the event.
    An actor taking an active role in the event or activity that is logged.
    """

    __resource_type__ = "AuditEventAgent"

    altId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="altId",
        title="Alternative User id e.g. authentication",
        description=(
            "Alternative agent Identifier. For a human, this should be a user "
            "identifier text string from authentication system. This identifier "
            "would be one known to a common authentication system (e.g. single "
            "sign-on), if available."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    altId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_altId", title="Extension field for ``altId``."
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where",
        description="Where the event occurred.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    media: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="media",
        title="Type of media",
        description=(
            "Type of media involved. Used when the event is about "
            "exporting/importing onto media."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Human-meaningful name for the agent",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.AuditEventAgentNetworkType | None = Field(  # type: ignore
        None,
        alias="network",
        title="Logical network location for application activity",
        description=(
            "Logical network location for application activity, if the activity has"
            " a network location."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    policy: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="policy",
        title="Policy that authorized event",
        description=(
            "The policy or plan that authorized the activity being recorded. "
            "Typically, a single activity may have multiple applicable policies, "
            "such as patient consent, guarantor funding, etc. The policy would also"
            " indicate the security token used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    policy__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_policy", title="Extension field for ``policy``."
    )

    purposeOfUse: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="purposeOfUse",
        title="Reason given for this user",
        description=(
            "The reason (purpose of use), specific to this agent, that was used "
            "during the event being recorded."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Direct reference to resource",
        description="Direct reference to a resource that identifies the agent.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Device",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    requestor: bool | None = Field(  # type: ignore
        None,
        alias="requestor",
        title="Whether user is initiator",
        description=(
            "Indicator that the user is or is not the requestor, or initiator, for "
            "the event being audited."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    requestor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_requestor", title="Extension field for ``requestor``."
    )

    role: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="role",
        title="Agent role in the event",
        description=(
            "The security role that the user was acting under, that come from local"
            " codes defined by the access control security system (e.g. RBAC, ABAC)"
            " used in the local context."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    userId: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="userId",
        title="Unique identifier for the user",
        description="Unique identifier for the user actively participating in the event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventAgent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "role",
            "reference",
            "userId",
            "altId",
            "name",
            "requestor",
            "location",
            "policy",
            "media",
            "network",
            "purposeOfUse",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("requestor", "requestor__ext")]
        return required_fields


class AuditEventAgentNetwork(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Logical network location for application activity.
    Logical network location for application activity, if the activity has a
    network location.
    """

    __resource_type__ = "AuditEventAgentNetwork"

    address: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="address",
        title="Identifier for the network access point of the user device",
        description=(
            "An identifier for the network access point of the user device for the "
            "audit event."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_address", title="Extension field for ``address``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The type of network access point",
        description=(
            "An identifier for the type of network access point that originated the"
            " audit event."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventAgentNetwork`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "address", "type"]


class AuditEventEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data or objects used.
    Specific instances of data or objects that have been accessed.
    """

    __resource_type__ = "AuditEventEntity"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Descriptive text",
        description="Text that describes the entity in more detail.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    detail: typing.List[fhirtypes.AuditEventEntityDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Additional Information about the entity",
        description=(
            "Tagged value pairs for conveying additional information about the "
            "entity."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Specific instance of object",
        description=(
            "Identifies a specific instance of the entity. The reference should "
            "always be version specific."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lifecycle: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="lifecycle",
        title="Life-cycle stage for the entity",
        description="Identifier for the data life-cycle stage for the entity.",
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Descriptor for entity",
        description="A name of the entity in the audit event.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    query: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="query",
        title="Query parameters",
        description="The query parameters for a query-type entities.",
        json_schema_extra={
            "element_property": True,
        },
    )
    query__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_query", title="Extension field for ``query``."
    )

    reference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Specific instance of resource",
        description=(
            "Identifies a specific instance of the entity. The reference should be "
            "version specific."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    role: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="role",
        title="What role the entity played",
        description=(
            "Code representing the role the entity played in the event being "
            "audited."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    securityLabel: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="securityLabel",
        title="Security labels on the entity",
        description="Security labels for the identified entity.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type of entity involved",
        description="The type of the object that was involved in this audit event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventEntity`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "reference",
            "type",
            "role",
            "lifecycle",
            "securityLabel",
            "name",
            "description",
            "query",
            "detail",
        ]


class AuditEventEntityDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional Information about the entity.
    Tagged value pairs for conveying additional information about the entity.
    """

    __resource_type__ = "AuditEventEntityDetail"

    type: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Name of the property",
        description="The type of extra detail provided in the value.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    value: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Property value",
        description="The details, base64 encoded. Used to carry bulk information.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventEntityDetail`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "value"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext"), ("value", "value__ext")]
        return required_fields


class AuditEventSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Audit Event Reporter.
    The system that is reporting the event.
    """

    __resource_type__ = "AuditEventSource"

    identifier: fhirtypes.IdentifierType = Field(  # type: ignore
        ...,
        alias="identifier",
        title="The identity of source detecting the event",
        description="Identifier of the source where the event was detected.",
        json_schema_extra={
            "element_property": True,
        },
    )

    site: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="site",
        title="Logical source location within the enterprise",
        description=(
            "Logical source location within the healthcare enterprise network.  For"
            " example, a hospital or other provider location within a multi-entity "
            "provider group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    site__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_site", title="Extension field for ``site``."
    )

    type: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="The type of source where event originated",
        description="Code specifying the type of source where event originated.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventSource`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "site", "identifier", "type"]
