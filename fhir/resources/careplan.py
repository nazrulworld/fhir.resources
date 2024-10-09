from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/CarePlan
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CarePlan(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Healthcare plan for patient or group.
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """

    __resource_type__ = "CarePlan"

    activity: typing.List[fhirtypes.CarePlanActivityType] | None = Field(  # type: ignore
        None,
        alias="activity",
        title="Action to occur or has occurred as part of plan",
        description=(
            "Identifies an action that has occurred or is a planned action to occur"
            " as part of the plan. For example, a medication to be used, lab tests "
            "to perform, self-monitoring that has occurred, education etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    addresses: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="addresses",
        title="Health issues this plan addresses",
        description=(
            "Identifies the conditions/problems/concerns/diagnoses/etc. whose "
            "management and/or mitigation are handled by this plan."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition"],
        },
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Fulfills plan, proposal or order",
        description=(
            "A higher-level request resource (i.e. a plan, proposal or order) that "
            "is fulfilled in whole or in part by this care plan."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "ServiceRequest",
                "RequestOrchestration",
                "NutritionOrder",
            ],
        },
    )

    careTeam: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="careTeam",
        title="Who's involved in plan?",
        description=(
            "Identifies all people and organizations who are expected to be "
            "involved in the care envisioned by this plan."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CareTeam"],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Type of plan",
        description=(
            'Identifies what "kind" of plan this is to support differentiation '
            'between multiple co-existing plans; e.g. "Home health", "psychiatric",'
            ' "asthma", "disease management", "wellness plan", etc.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contributor: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="contributor",
        title="Who provided the content of the care plan",
        description=(
            "Identifies the individual(s), organization or device who provided the "
            "contents of the care plan."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "Device",
                "RelatedPerson",
                "Organization",
                "CareTeam",
            ],
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Date record was first recorded",
        description=(
            "Represents when this particular CarePlan record was created in the "
            "system, which is often a system-generated date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    custodian: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="custodian",
        title="Who is the designated responsible party",
        description=(
            "When populated, the custodian is responsible for the care plan. The "
            "care plan is attributed to the custodian."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "Device",
                "RelatedPerson",
                "Organization",
                "CareTeam",
            ],
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Summary of nature of plan",
        description="A description of the scope and nature of the plan.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="The Encounter during which this CarePlan was created",
        description=(
            "The Encounter during which this CarePlan was created or to which the "
            "creation of this record is tightly associated."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    goal: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="goal",
        title="Desired outcome of plan",
        description="Describes the intended objective(s) of carrying out the care plan.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Goal"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Ids for this plan",
        description=(
            "Business identifiers assigned to this care plan by the performer or "
            "other systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    instantiatesCanonical: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a FHIR-defined protocol, guideline, questionnaire "
            "or other definition that is adhered to in whole or in part by this "
            "CarePlan."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "PlanDefinition",
                "Questionnaire",
                "Measure",
                "ActivityDefinition",
                "OperationDefinition",
            ],
        },
    )
    instantiatesCanonical__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "questionnaire or other definition that is adhered to in whole or in "
            "part by this CarePlan."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesUri__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    intent: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="intent",
        title="proposal | plan | order | option | directive",
        description=(
            "Indicates the level of authority/intentionality associated with the "
            "care plan and where the care plan fits into the workflow chain."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["proposal", "plan", "order", "option", "directive"],
        },
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_intent", title="Extension field for ``intent``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments about the plan",
        description="General notes about the care plan not covered elsewhere.",
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Part of referenced CarePlan",
        description=(
            "A larger care plan of which this particular care plan is a component "
            "or step."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CarePlan"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Time period plan covers",
        description=(
            "Indicates when the plan did (or is intended to) come into effect and "
            "end."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    replaces: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="replaces",
        title="CarePlan replaced by this CarePlan",
        description=(
            "Completed or terminated care plan whose function is taken by this new "
            "care plan."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CarePlan"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "draft | active | on-hold | revoked | completed | entered-in-error | "
            "unknown"
        ),
        description=(
            "Indicates whether the plan is currently being acted upon, represents "
            "future intentions or is now a historical record."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "draft",
                "active",
                "on-hold",
                "revoked",
                "completed",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who the care plan is for",
        description=(
            "Identifies the patient or group whose intended care is described by "
            "the plan."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingInfo",
        title="Information considered as part of plan",
        description=(
            "Identifies portions of the patient's record that specifically "
            "influenced the formation of the plan.  These might include "
            "comorbidities, recent procedures, limitations, recent assessments, "
            "etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Human-friendly name for the care plan",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CarePlan`` according specification,
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
            "identifier",
            "instantiatesCanonical",
            "instantiatesUri",
            "basedOn",
            "replaces",
            "partOf",
            "status",
            "intent",
            "category",
            "title",
            "description",
            "subject",
            "encounter",
            "period",
            "created",
            "custodian",
            "contributor",
            "careTeam",
            "addresses",
            "supportingInfo",
            "goal",
            "activity",
            "note",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("intent", "intent__ext"), ("status", "status__ext")]
        return required_fields


class CarePlanActivity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Action to occur or has occurred as part of plan.
    Identifies an action that has occurred or is a planned action to occur as
    part of the plan. For example, a medication to be used, lab tests to
    perform, self-monitoring that has occurred, education etc.
    """

    __resource_type__ = "CarePlanActivity"

    performedActivity: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="performedActivity",
        title=(
            "Results of the activity (concept, or Appointment, Encounter, "
            "Procedure, etc.)"
        ),
        description=(
            "Identifies the activity that was performed. For example, an activity "
            "could be patient education, exercise, or a medication administration. "
            'The reference to an "event" resource, such as Procedure or Encounter '
            "or Observation, represents the activity that was performed. The "
            "requested activity can be conveyed using the "
            "CarePlan.activity.plannedActivityReference (a reference to a \u201crequest\u201d"
            " resource)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    plannedActivityReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="plannedActivityReference",
        title="Activity that is intended to be part of the care plan",
        description=(
            "The details of the proposed activity represented in a specific "
            "resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Appointment",
                "CommunicationRequest",
                "DeviceRequest",
                "MedicationRequest",
                "NutritionOrder",
                "Task",
                "ServiceRequest",
                "VisionPrescription",
                "RequestOrchestration",
                "ImmunizationRecommendation",
                "SupplyRequest",
            ],
        },
    )

    progress: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="progress",
        title="Comments about the activity status/progress",
        description="Notes about the adherence/status/progress of the activity.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CarePlanActivity`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "performedActivity",
            "progress",
            "plannedActivityReference",
        ]
