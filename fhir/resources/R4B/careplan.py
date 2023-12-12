# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CarePlan
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

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

    resource_type = Field("CarePlan", const=True)

    activity: typing.List[fhirtypes.CarePlanActivityType] = Field(
        None,
        alias="activity",
        title="Action to occur as part of plan",
        description=(
            "Identifies a planned action to occur as part of the plan.  For "
            "example, a medication to be used, lab tests to perform, self-"
            "monitoring, education, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    addresses: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="addresses",
        title="Health issues this plan addresses",
        description=(
            "Identifies the conditions/problems/concerns/diagnoses/etc. whose "
            "management and/or mitigation are handled by this plan."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Who is the designated responsible party",
        description=(
            "When populated, the author is responsible for the care plan.  The care"
            " plan is attributed to the author."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "Device",
            "RelatedPerson",
            "Organization",
            "CareTeam",
        ],
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Fulfills CarePlan",
        description="A care plan that is fulfilled in whole or in part by this care plan.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan"],
    )

    careTeam: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="careTeam",
        title="Who's involved in plan?",
        description=(
            "Identifies all people and organizations who are expected to be "
            "involved in the care envisioned by this plan."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CareTeam"],
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Type of plan",
        description=(
            'Identifies what "kind" of plan this is to support differentiation '
            'between multiple co-existing plans; e.g. "Home health", "psychiatric",'
            ' "asthma", "disease management", "wellness plan", etc.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contributor: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="contributor",
        title="Who provided the content of the care plan",
        description=(
            "Identifies the individual(s) or organization who provided the contents"
            " of the care plan."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "Device",
            "RelatedPerson",
            "Organization",
            "CareTeam",
        ],
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Date record was first recorded",
        description=(
            "Represents when this particular CarePlan record was created in the "
            "system, which is often a system-generated date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Summary of nature of plan",
        description="A description of the scope and nature of the plan.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter created as part of",
        description=(
            "The Encounter during which this CarePlan was created or to which the "
            "creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    goal: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="goal",
        title="Desired outcome of plan",
        description="Describes the intended objective(s) of carrying out the care plan.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Goal"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Ids for this plan",
        description=(
            "Business identifiers assigned to this care plan by the performer or "
            "other systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    instantiatesCanonical: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a FHIR-defined protocol, guideline, questionnaire "
            "or other definition that is adhered to in whole or in part by this "
            "CarePlan."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "PlanDefinition",
            "Questionnaire",
            "Measure",
            "ActivityDefinition",
            "OperationDefinition",
        ],
    )
    instantiatesCanonical__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "questionnaire or other definition that is adhered to in whole or in "
            "part by this CarePlan."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    instantiatesUri__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    intent: fhirtypes.Code = Field(
        None,
        alias="intent",
        title="proposal | plan | order | option",
        description=(
            "Indicates the level of authority/intentionality associated with the "
            "care plan and where the care plan fits into the workflow chain."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["proposal", "plan", "order", "option"],
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_intent", title="Extension field for ``intent``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments about the plan",
        description="General notes about the care plan not covered elsewhere.",
        # if property is element of this resource.
        element_property=True,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced CarePlan",
        description=(
            "A larger care plan of which this particular care plan is a component "
            "or step."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period plan covers",
        description=(
            "Indicates when the plan did (or is intended to) come into effect and "
            "end."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    replaces: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title="CarePlan replaced by this CarePlan",
        description=(
            "Completed or terminated care plan whose function is taken by this new "
            "care plan."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan"],
    )

    status: fhirtypes.Code = Field(
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
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "draft",
            "active",
            "on-hold",
            "revoked",
            "completed",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who the care plan is for",
        description=(
            "Identifies the patient or group whose intended care is described by "
            "the plan."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title="Information considered as part of plan",
        description=(
            "Identifies portions of the patient's record that specifically "
            "influenced the formation of the plan.  These might include "
            "comorbidities, recent procedures, limitations, recent assessments, "
            "etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Human-friendly name for the care plan",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
            "author",
            "contributor",
            "careTeam",
            "addresses",
            "supportingInfo",
            "goal",
            "activity",
            "note",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_951(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("intent", "intent__ext"), ("status", "status__ext")]
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


class CarePlanActivity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Action to occur as part of plan.
    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """

    resource_type = Field("CarePlanActivity", const=True)

    detail: fhirtypes.CarePlanActivityDetailType = Field(
        None,
        alias="detail",
        title="In-line definition of activity",
        description=(
            "A simple summary of a planned activity suitable for a general care "
            "plan system (e.g. form driven) that doesn't know about specific "
            "resources such as procedure etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    outcomeCodeableConcept: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="outcomeCodeableConcept",
        title="Results of the activity",
        description=(
            "Identifies the outcome at the point when the status of the activity is"
            " assessed.  For example, the outcome of an education activity could be"
            " patient understands (or not)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    outcomeReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="outcomeReference",
        title="Appointment, Encounter, Procedure, etc.",
        description=(
            "Details of the outcome or action resulting from the activity.  The "
            'reference to an "event" resource, such as Procedure or Encounter or '
            "Observation, is the result/outcome of the activity itself.  The "
            "activity can be conveyed using CarePlan.activity.detail OR using the "
            "CarePlan.activity.reference (a reference to a \u201crequest\u201d resource)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    progress: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="progress",
        title="Comments about the activity status/progress",
        description="Notes about the adherence/status/progress of the activity.",
        # if property is element of this resource.
        element_property=True,
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title="Activity details defined in specific resource",
        description=(
            "The details of the proposed activity represented in a specific "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Appointment",
            "CommunicationRequest",
            "DeviceRequest",
            "MedicationRequest",
            "NutritionOrder",
            "Task",
            "ServiceRequest",
            "VisionPrescription",
            "RequestGroup",
        ],
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
            "outcomeCodeableConcept",
            "outcomeReference",
            "progress",
            "reference",
            "detail",
        ]


class CarePlanActivityDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    In-line definition of activity.
    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """

    resource_type = Field("CarePlanActivityDetail", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Detail type of activity",
        description=(
            "Detailed description of the type of planned activity; e.g. what lab "
            "test, what procedure, what kind of encounter."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dailyAmount: fhirtypes.QuantityType = Field(
        None,
        alias="dailyAmount",
        title="How to consume/day?",
        description="Identifies the quantity expected to be consumed in a given day.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Extra info describing activity to perform",
        description=(
            "This provides a textual description of constraints on the intended "
            "activity occurrence, including relation to other activities.  It may "
            "also include objectives, pre-conditions and end-conditions.  Finally, "
            "it may convey specifics about the activity such as body site, method, "
            "route, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    doNotPerform: bool = Field(
        None,
        alias="doNotPerform",
        title="If true, activity is prohibiting action",
        description=(
            "If true, indicates that the described activity is one that must NOT be"
            " engaged in when following the plan.  If false, or missing, indicates "
            "that the described activity is one that should be engaged in when "
            "following the plan."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doNotPerform", title="Extension field for ``doNotPerform``."
    )

    goal: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="goal",
        title="Goals this activity relates to",
        description=(
            "Internal reference that identifies the goals that this activity is "
            "intended to contribute towards meeting."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Goal"],
    )

    instantiatesCanonical: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a FHIR-defined protocol, guideline, questionnaire "
            "or other definition that is adhered to in whole or in part by this "
            "CarePlan activity."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "PlanDefinition",
            "ActivityDefinition",
            "Questionnaire",
            "Measure",
            "OperationDefinition",
        ],
    )
    instantiatesCanonical__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "questionnaire or other definition that is adhered to in whole or in "
            "part by this CarePlan activity."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    instantiatesUri__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    kind: fhirtypes.Code = Field(
        None,
        alias="kind",
        title=(
            "Appointment | CommunicationRequest | DeviceRequest | MedicationRequest"
            " | NutritionOrder | Task | ServiceRequest | VisionPrescription"
        ),
        description=(
            "A description of the kind of resource the in-line definition of a care"
            " plan activity is representing.  The CarePlan.activity.detail is an "
            "in-line definition when a resource is not referenced using "
            "CarePlan.activity.reference.  For example, a MedicationRequest, a "
            "ServiceRequest, or a CommunicationRequest."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "Appointment",
            "CommunicationRequest",
            "DeviceRequest",
            "MedicationRequest",
            "NutritionOrder",
            "Task",
            "ServiceRequest",
            "VisionPrescription",
        ],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where it should happen",
        description=(
            "Identifies the facility where the activity will occur; e.g. home, "
            "hospital, specific clinic, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    performer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title="Who will be responsible?",
        description="Identifies who's expected to be involved in the activity.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "RelatedPerson",
            "Patient",
            "CareTeam",
            "HealthcareService",
            "Device",
        ],
    )

    productCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productCodeableConcept",
        title="What is to be administered/supplied",
        description=(
            "Identifies the food, drug or other product to be consumed or supplied "
            "in the activity."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e product[x]
        one_of_many="product",
        one_of_many_required=False,
    )

    productReference: fhirtypes.ReferenceType = Field(
        None,
        alias="productReference",
        title="What is to be administered/supplied",
        description=(
            "Identifies the food, drug or other product to be consumed or supplied "
            "in the activity."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e product[x]
        one_of_many="product",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication", "Substance"],
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="How much to administer/supply/consume",
        description=(
            "Identifies the quantity expected to be supplied, administered or "
            "consumed by the subject."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why activity should be done or why activity was prohibited",
        description=(
            "Provides the rationale that drove the inclusion of this particular "
            "activity as part of the plan or the reason why the activity was "
            "prohibited."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why activity is needed",
        description=(
            "Indicates another resource, such as the health condition(s), whose "
            "existence justifies this request and drove the inclusion of this "
            "particular activity as part of the plan."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "DiagnosticReport",
            "DocumentReference",
        ],
    )

    scheduledPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="scheduledPeriod",
        title="When activity is to occur",
        description=(
            "The period, timing or frequency upon which the described activity is "
            "to occur."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e scheduled[x]
        one_of_many="scheduled",
        one_of_many_required=False,
    )

    scheduledString: fhirtypes.String = Field(
        None,
        alias="scheduledString",
        title="When activity is to occur",
        description=(
            "The period, timing or frequency upon which the described activity is "
            "to occur."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e scheduled[x]
        one_of_many="scheduled",
        one_of_many_required=False,
    )
    scheduledString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_scheduledString", title="Extension field for ``scheduledString``."
    )

    scheduledTiming: fhirtypes.TimingType = Field(
        None,
        alias="scheduledTiming",
        title="When activity is to occur",
        description=(
            "The period, timing or frequency upon which the described activity is "
            "to occur."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e scheduled[x]
        one_of_many="scheduled",
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "not-started | scheduled | in-progress | on-hold | completed | "
            "cancelled | stopped | unknown | entered-in-error"
        ),
        description="Identifies what progress is being made for the specific activity.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "not-started",
            "scheduled",
            "in-progress",
            "on-hold",
            "completed",
            "cancelled",
            "stopped",
            "unknown",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Reason for current status",
        description=(
            "Provides reason why the activity isn't yet started, is on hold, was "
            "cancelled, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CarePlanActivityDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "kind",
            "instantiatesCanonical",
            "instantiatesUri",
            "code",
            "reasonCode",
            "reasonReference",
            "goal",
            "status",
            "statusReason",
            "doNotPerform",
            "scheduledTiming",
            "scheduledPeriod",
            "scheduledString",
            "location",
            "performer",
            "productCodeableConcept",
            "productReference",
            "dailyAmount",
            "quantity",
            "description",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2389(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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
    def validate_one_of_many_2389(
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
            "product": ["productCodeableConcept", "productReference"],
            "scheduled": ["scheduledPeriod", "scheduledString", "scheduledTiming"],
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
