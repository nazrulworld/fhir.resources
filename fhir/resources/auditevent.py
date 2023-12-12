# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class AuditEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Record of an event.
    A record of an event relevant for purposes such as operations, privacy,
    security, maintenance, and performance analysis.
    """

    resource_type = Field("AuditEvent", const=True)

    action: fhirtypes.Code = Field(
        None,
        alias="action",
        title="Type of action performed during the event",
        description=(
            "Indicator for type of action performed during the event that generated"
            " the audit."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    action__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_action", title="Extension field for ``action``."
    )

    agent: typing.List[fhirtypes.AuditEventAgentType] = Field(
        ...,
        alias="agent",
        title="Actor involved in the event",
        description=(
            "An actor taking an active role in the event or activity that is " "logged."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    authorization: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="authorization",
        title="Authorization related to the event",
        description=(
            "The authorization (e.g., PurposeOfUse) that was used during the event "
            "being recorded."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Workflow authorization within which this event occurred",
        description=(
            "Allows tracing of authorizatino for the events and tracking whether "
            "proposals/recommendations were acted upon."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "CarePlan",
            "DeviceRequest",
            "ImmunizationRecommendation",
            "MedicationRequest",
            "NutritionOrder",
            "ServiceRequest",
            "Task",
        ],
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Type/identifier of event",
        description="Classification of the type of event.",
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Specific type of event",
        description="Describes what happened. The most specific code for the event.",
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    entity: typing.List[fhirtypes.AuditEventEntityType] = Field(
        None,
        alias="entity",
        title="Data or objects used",
        description="Specific instances of data or objects that have been accessed.",
        # if property is element of this resource.
        element_property=True,
    )

    occurredDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurredDateTime",
        title="When the activity occurred",
        description="The time or period during which the activity occurred.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurred[x]
        one_of_many="occurred",
        one_of_many_required=False,
    )
    occurredDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurredDateTime",
        title="Extension field for ``occurredDateTime``.",
    )

    occurredPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurredPeriod",
        title="When the activity occurred",
        description="The time or period during which the activity occurred.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurred[x]
        one_of_many="occurred",
        one_of_many_required=False,
    )

    outcome: fhirtypes.AuditEventOutcomeType = Field(
        None,
        alias="outcome",
        title="Whether the event succeeded or failed",
        description=(
            "Indicates whether the event succeeded or failed. A free text "
            "descripiton can be given in outcome.text."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    recorded: fhirtypes.Instant = Field(
        None,
        alias="recorded",
        title="Time when the event was recorded",
        description="The time when the event was recorded.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recorded", title="Extension field for ``recorded``."
    )

    severity: fhirtypes.Code = Field(
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
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "emergency",
            "alert",
            "critical",
            "error",
            "warning",
            "notice",
            "informational",
            "debug",
        ],
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )

    source: fhirtypes.AuditEventSourceType = Field(
        ...,
        alias="source",
        title="Audit Event Reporter",
        description="The actor that is reporting the event.",
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1198(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("recorded", "recorded__ext")]
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1198(
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
        one_of_many_fields = {"occurred": ["occurredDateTime", "occurredPeriod"]}
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


class AuditEventAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor involved in the event.
    An actor taking an active role in the event or activity that is logged.
    """

    resource_type = Field("AuditEventAgent", const=True)

    authorization: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="authorization",
        title="Allowable authorization for this agent",
        description=(
            "The authorization (e.g., PurposeOfUse) that was used during the event "
            "being recorded."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="The agent location when the event occurred",
        description=(
            "Where the agent location is known, the agent location when the event "
            "occurred."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    networkReference: fhirtypes.ReferenceType = Field(
        None,
        alias="networkReference",
        title="This agent network location for the activity",
        description=(
            "When the event utilizes a network there should be an agent describing "
            "the local system, and an agent describing remote system, with the "
            "network interface details."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e network[x]
        one_of_many="network",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    networkString: fhirtypes.String = Field(
        None,
        alias="networkString",
        title="This agent network location for the activity",
        description=(
            "When the event utilizes a network there should be an agent describing "
            "the local system, and an agent describing remote system, with the "
            "network interface details."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e network[x]
        one_of_many="network",
        one_of_many_required=False,
    )
    networkString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_networkString", title="Extension field for ``networkString``."
    )

    networkUri: fhirtypes.Uri = Field(
        None,
        alias="networkUri",
        title="This agent network location for the activity",
        description=(
            "When the event utilizes a network there should be an agent describing "
            "the local system, and an agent describing remote system, with the "
            "network interface details."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e network[x]
        one_of_many="network",
        one_of_many_required=False,
    )
    networkUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_networkUri", title="Extension field for ``networkUri``."
    )

    policy: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="policy",
        title="Policy that authorized the agent participation in the event",
        description=(
            "Where the policy(ies) are known that authorized the agent "
            "participation in the event. Typically, a single activity may have "
            "multiple applicable policies, such as patient consent, guarantor "
            "funding, etc. The policy would also indicate the security token used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    policy__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_policy", title="Extension field for ``policy``.")

    requestor: bool = Field(
        None,
        alias="requestor",
        title="Whether user is initiator",
        description=(
            "Indicator that the user is or is not the requestor, or initiator, for "
            "the event being audited."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    requestor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requestor", title="Extension field for ``requestor``."
    )

    role: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="Agent role in the event",
        description=(
            "The structural roles of the agent indicating the agent's competency. "
            "The security role enabling the agent with respect to the activity."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="How agent participated",
        description="The Functional Role of the user when performing the event.",
        # if property is element of this resource.
        element_property=True,
    )

    who: fhirtypes.ReferenceType = Field(
        ...,
        alias="who",
        title="Identifier of who",
        description="Reference to who this agent is that was involved in the event.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1693(
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
        one_of_many_fields = {
            "network": ["networkReference", "networkString", "networkUri"]
        }
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


class AuditEventEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data or objects used.
    Specific instances of data or objects that have been accessed.
    """

    resource_type = Field("AuditEventEntity", const=True)

    agent: typing.List[fhirtypes.AuditEventAgentType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    detail: typing.List[fhirtypes.AuditEventEntityDetailType] = Field(
        None,
        alias="detail",
        title="Additional Information about the entity",
        description=(
            "Tagged value pairs for conveying additional information about the "
            "entity."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    query: fhirtypes.Base64Binary = Field(
        None,
        alias="query",
        title="Query parameters",
        description="The query parameters for a query-type entities.",
        # if property is element of this resource.
        element_property=True,
    )
    query__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_query", title="Extension field for ``query``."
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="What role the entity played",
        description=(
            "Code representing the role the entity played in the event being "
            "audited."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    securityLabel: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="securityLabel",
        title="Security labels on the entity",
        description="Security labels for the identified entity.",
        # if property is element of this resource.
        element_property=True,
    )

    what: fhirtypes.ReferenceType = Field(
        None,
        alias="what",
        title="Specific instance of resource",
        description=(
            "Identifies a specific instance of the entity. The reference should be "
            "version specific. This is allowed to be a Parameters resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
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

    resource_type = Field("AuditEventEntityDetail", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Name of the property",
        description="The type of extra detail provided in the value.",
        # if property is element of this resource.
        element_property=True,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Property value",
        description="The  value of the extra detail.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2422(
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


class AuditEventOutcome(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether the event succeeded or failed.
    Indicates whether the event succeeded or failed. A free text descripiton
    can be given in outcome.text.
    """

    resource_type = Field("AuditEventOutcome", const=True)

    code: fhirtypes.CodingType = Field(
        ...,
        alias="code",
        title="Whether the event succeeded or failed",
        description="Indicates whether the event succeeded or failed.",
        # if property is element of this resource.
        element_property=True,
    )

    detail: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="detail",
        title="Additional outcome detail",
        description=(
            "Additional details about the error. This may be a text description of "
            "the error or a system code that identifies the error."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("AuditEventSource", const=True)

    observer: fhirtypes.ReferenceType = Field(
        ...,
        alias="observer",
        title="The identity of source detecting the event",
        description="Identifier of the source where the event was detected.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
    )

    site: fhirtypes.ReferenceType = Field(
        None,
        alias="site",
        title="Logical source location within the enterprise",
        description=(
            "Logical source location within the healthcare enterprise network.  For"
            " example, a hospital or other provider location within a multi-entity "
            "provider group."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="The type of source where event originated",
        description="Code specifying the type of source where event originated.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AuditEventSource`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "site", "observer", "type"]
