from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class AuditEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Record of an event.
    A record of an event relevant for purposes such as operations, privacy,
    security, maintenance, and performance analysis.
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

    authorization: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="authorization",
        title="Authorization related to the event",
        description=(
            "The authorization (e.g., PurposeOfUse) that was used during the event "
            "being recorded."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Workflow authorization within which this event occurred",
        description=(
            "Allows tracing of authorizatino for the events and tracking whether "
            "proposals/recommendations were acted upon."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "DeviceRequest",
                "ImmunizationRecommendation",
                "MedicationRequest",
                "NutritionOrder",
                "ServiceRequest",
                "Task",
            ],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Type/identifier of event",
        description="Classification of the type of event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Specific type of event",
        description="Describes what happened. The most specific code for the event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title=(
            "Encounter within which this event occurred or which the event is "
            "tightly associated"
        ),
        description=(
            "This will typically be the encounter the event occurred, but some "
            "events may be initiated prior to or after the official completion of "
            "an encounter but still be tied to the context of the encounter (e.g. "
            "pre-admission lab tests)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
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

    occurredDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="occurredDateTime",
        title="When the activity occurred",
        description="The time or period during which the activity occurred.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurred[x]
            "one_of_many": "occurred",
            "one_of_many_required": False,
        },
    )
    occurredDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_occurredDateTime",
        title="Extension field for ``occurredDateTime``.",
    )

    occurredPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="occurredPeriod",
        title="When the activity occurred",
        description="The time or period during which the activity occurred.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurred[x]
            "one_of_many": "occurred",
            "one_of_many_required": False,
        },
    )

    outcome: fhirtypes.AuditEventOutcomeType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="Whether the event succeeded or failed",
        description=(
            "Indicates whether the event succeeded or failed. A free text "
            "descripiton can be given in outcome.text."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="patient",
        title=(
            "The patient is the subject of the data used/created/updated/deleted "
            "during the activity"
        ),
        description=(
            "The patient element is available to enable deterministic tracking of "
            "activities that involve the patient as the subject of the data used in"
            " an activity."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    recorded: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="recorded",
        title="Time when the event was recorded",
        description="The time when the event was recorded.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    severity: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="severity",
        title=(
            "emergency | alert | critical | error | warning | notice | "
            "informational | debug"
        ),
        description=(
            "Indicates and enables segmentation of various severity including "
            "debugging from critical."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "emergency",
                "alert",
                "critical",
                "error",
                "warning",
                "notice",
                "informational",
                "debug",
            ],
        },
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_severity", title="Extension field for ``severity``."
    )

    source: fhirtypes.AuditEventSourceType = Field(  # type: ignore
        ...,
        alias="source",
        title="Audit Event Reporter",
        description="The actor that is reporting the event.",
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
            "category",
            "code",
            "action",
            "severity",
            "occurredPeriod",
            "occurredDateTime",
            "recorded",
            "outcome",
            "authorization",
            "basedOn",
            "patient",
            "encounter",
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
        one_of_many_fields = {"occurred": ["occurredDateTime", "occurredPeriod"]}
        return one_of_many_fields


class AuditEventAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor involved in the event.
    An actor taking an active role in the event or activity that is logged.
    """

    __resource_type__ = "AuditEventAgent"

    authorization: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="authorization",
        title="Allowable authorization for this agent",
        description=(
            "The authorization (e.g., PurposeOfUse) that was used during the event "
            "being recorded."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="The agent location when the event occurred",
        description=(
            "Where the agent location is known, the agent location when the event "
            "occurred."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    networkReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="networkReference",
        title="This agent network location for the activity",
        description=(
            "When the event utilizes a network there should be an agent describing "
            "the local system, and an agent describing remote system, with the "
            "network interface details."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e network[x]
            "one_of_many": "network",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Endpoint"],
        },
    )

    networkString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="networkString",
        title="This agent network location for the activity",
        description=(
            "When the event utilizes a network there should be an agent describing "
            "the local system, and an agent describing remote system, with the "
            "network interface details."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e network[x]
            "one_of_many": "network",
            "one_of_many_required": False,
        },
    )
    networkString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_networkString", title="Extension field for ``networkString``."
    )

    networkUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="networkUri",
        title="This agent network location for the activity",
        description=(
            "When the event utilizes a network there should be an agent describing "
            "the local system, and an agent describing remote system, with the "
            "network interface details."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e network[x]
            "one_of_many": "network",
            "one_of_many_required": False,
        },
    )
    networkUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_networkUri", title="Extension field for ``networkUri``."
    )

    policy: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="policy",
        title="Policy that authorized the agent participation in the event",
        description=(
            "Where the policy(ies) are known that authorized the agent "
            "participation in the event. Typically, a single activity may have "
            "multiple applicable policies, such as patient consent, guarantor "
            "funding, etc. The policy would also indicate the security token used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    policy__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_policy", title="Extension field for ``policy``."
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
            "The structural roles of the agent indicating the agent's competency. "
            "The security role enabling the agent with respect to the activity."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="How agent participated",
        description="The Functional Role of the user when performing the event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    who: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="who",
        title="Identifier of who",
        description="Reference to who this agent is that was involved in the event.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "CareTeam",
                "Patient",
                "Device",
                "RelatedPerson",
            ],
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
            "type",
            "role",
            "who",
            "requestor",
            "location",
            "policy",
            "networkReference",
            "networkUri",
            "networkString",
            "authorization",
        ]

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
        one_of_many_fields = {
            "network": ["networkReference", "networkString", "networkUri"]
        }
        return one_of_many_fields


class AuditEventEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data or objects used.
    Specific instances of data or objects that have been accessed.
    """

    __resource_type__ = "AuditEventEntity"

    agent: typing.List[fhirtypes.AuditEventAgentType] | None = Field(  # type: ignore
        None,
        alias="agent",
        title="Entity is attributed to this agent",
        description=(
            "The entity is attributed to an agent to express the agent's "
            "responsibility for that entity in the activity. This is most used to "
            "indicate when persistence media (the entity) are used by an agent. For"
            " example when importing data from a device, the device would be "
            "described in an entity, and the user importing data from that media "
            "would be indicated as the entity.agent."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
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

    securityLabel: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="securityLabel",
        title="Security labels on the entity",
        description="Security labels for the identified entity.",
        json_schema_extra={
            "element_property": True,
        },
    )

    what: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="what",
        title="Specific instance of resource",
        description=(
            "Identifies a specific instance of the entity. The reference should be "
            "version specific. This is allowed to be a Parameters resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
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
            "what",
            "role",
            "securityLabel",
            "query",
            "detail",
            "agent",
        ]


class AuditEventEntityDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional Information about the entity.
    Tagged value pairs for conveying additional information about the entity.
    """

    __resource_type__ = "AuditEventEntityDetail"

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Name of the property",
        description="The type of extra detail provided in the value.",
        json_schema_extra={
            "element_property": True,
        },
    )

    valueBase64Binary: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="valueBase64Binary",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="valueDateTime",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="valueInteger",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valuePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="valuePeriod",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="valueRatio",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="valueTime",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventEntityDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueQuantity",
            "valueCodeableConcept",
            "valueString",
            "valueBoolean",
            "valueInteger",
            "valueRange",
            "valueRatio",
            "valueTime",
            "valueDateTime",
            "valuePeriod",
            "valueBase64Binary",
        ]

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
        one_of_many_fields = {
            "value": [
                "valueBase64Binary",
                "valueBoolean",
                "valueCodeableConcept",
                "valueDateTime",
                "valueInteger",
                "valuePeriod",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueString",
                "valueTime",
            ]
        }
        return one_of_many_fields


class AuditEventOutcome(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether the event succeeded or failed.
    Indicates whether the event succeeded or failed. A free text descripiton
    can be given in outcome.text.
    """

    __resource_type__ = "AuditEventOutcome"

    code: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="code",
        title="Whether the event succeeded or failed",
        description="Indicates whether the event succeeded or failed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Additional outcome detail",
        description=(
            "Additional details about the error. This may be a text description of "
            "the error or a system code that identifies the error."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventOutcome`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "detail"]


class AuditEventSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Audit Event Reporter.
    The actor that is reporting the event.
    """

    __resource_type__ = "AuditEventSource"

    observer: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="observer",
        title="The identity of source detecting the event",
        description="Identifier of the source where the event was detected.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "CareTeam",
                "Patient",
                "Device",
                "RelatedPerson",
            ],
        },
    )

    site: fhirtypes.ReferenceType | None = Field(  # type: ignore
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
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
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
        return ["id", "extension", "modifierExtension", "site", "observer", "type"]
