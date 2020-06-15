# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CarePlan
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient or group.
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """

    resource_type = Field("CarePlan", const=True)

    activity: ListType[fhirtypes.CarePlanActivityType] = Field(
        None,
        alias="activity",
        title="List of `CarePlanActivity` items (represented as `dict` in JSON)",
        description="Action to occur as part of plan",
    )

    addresses: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="addresses",
        title=(
            "List of `Reference` items referencing `Condition` (represented as "
            "`dict` in JSON)"
        ),
        description="Health issues this plan addresses",
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, PractitionerRole,"
            " Device, RelatedPerson, Organization, CareTeam` (represented as `dict`"
            " in JSON)"
        ),
        description="Who is the designated responsible party",
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `CarePlan` (represented as "
            "`dict` in JSON)"
        ),
        description="Fulfills CarePlan",
    )

    careTeam: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="careTeam",
        title=(
            "List of `Reference` items referencing `CareTeam` (represented as "
            "`dict` in JSON)"
        ),
        description="Who\u0027s involved in plan?",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of plan",
    )

    contributor: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="contributor",
        title=(
            "List of `Reference` items referencing `Patient, Practitioner, "
            "PractitionerRole, Device, RelatedPerson, Organization, CareTeam` "
            "(represented as `dict` in JSON)"
        ),
        description="Who provided the content of the care plan",
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date record was first recorded",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Summary of nature of plan",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Encounter created as part of",
    )

    goal: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="goal",
        title=(
            "List of `Reference` items referencing `Goal` (represented as `dict` in"
            " JSON)"
        ),
        description="Desired outcome of plan",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Ids for this plan",
    )

    instantiatesCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="instantiatesCanonical",
        title=(
            "List of `Canonical` items referencing `PlanDefinition, Questionnaire, "
            "Measure, ActivityDefinition, OperationDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Instantiates FHIR protocol or definition",
    )

    instantiatesUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiatesUri",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Instantiates external protocol or definition",
    )

    intent: fhirtypes.Code = Field(
        ...,
        alias="intent",
        title="Type `Code` (represented as `dict` in JSON)",
        description="proposal | plan | order | option",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments about the plan",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title=(
            "List of `Reference` items referencing `CarePlan` (represented as "
            "`dict` in JSON)"
        ),
        description="Part of referenced CarePlan",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period plan covers",
    )

    replaces: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title=(
            "List of `Reference` items referencing `CarePlan` (represented as "
            "`dict` in JSON)"
        ),
        description="CarePlan replaced by this CarePlan",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "draft | active | on-hold | revoked | completed | entered-in-error | "
            "unknown"
        ),
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Who the care plan is for",
    )

    supportingInfo: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Information considered as part of plan",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human-friendly name for the care plan",
    )


class CarePlanActivity(backboneelement.BackboneElement):
    """ Action to occur as part of plan.
    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """

    resource_type = Field("CarePlanActivity", const=True)

    detail: fhirtypes.CarePlanActivityDetailType = Field(
        None,
        alias="detail",
        title="Type `CarePlanActivityDetail` (represented as `dict` in JSON)",
        description="In-line definition of activity",
    )

    outcomeCodeableConcept: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="outcomeCodeableConcept",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Results of the activity",
    )

    outcomeReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="outcomeReference",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Appointment, Encounter, Procedure, etc.",
    )

    progress: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="progress",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments about the activity status/progress",
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title=(
            "Type `Reference` referencing `Appointment, CommunicationRequest, "
            "DeviceRequest, MedicationRequest, NutritionOrder, Task, "
            "ServiceRequest, VisionPrescription, RequestGroup` (represented as "
            "`dict` in JSON)"
        ),
        description="Activity details defined in specific resource",
    )


class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ In-line definition of activity.
    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """

    resource_type = Field("CarePlanActivityDetail", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Detail type of activity",
    )

    dailyAmount: fhirtypes.QuantityType = Field(
        None,
        alias="dailyAmount",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="How to consume/day?",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Extra info describing activity to perform",
    )

    doNotPerform: bool = Field(
        None,
        alias="doNotPerform",
        title="Type `bool`",
        description="If true, activity is prohibiting action",
    )

    goal: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="goal",
        title=(
            "List of `Reference` items referencing `Goal` (represented as `dict` in"
            " JSON)"
        ),
        description="Goals this activity relates to",
    )

    instantiatesCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="instantiatesCanonical",
        title=(
            "List of `Canonical` items referencing `PlanDefinition, "
            "ActivityDefinition, Questionnaire, Measure, OperationDefinition` "
            "(represented as `dict` in JSON)"
        ),
        description="Instantiates FHIR protocol or definition",
    )

    instantiatesUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiatesUri",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Instantiates external protocol or definition",
    )

    kind: fhirtypes.Code = Field(
        None,
        alias="kind",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "Appointment | CommunicationRequest | DeviceRequest | MedicationRequest"
            " | NutritionOrder | Task | ServiceRequest | VisionPrescription"
        ),
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Where it should happen",
    )

    performer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title=(
            "List of `Reference` items referencing `Practitioner, PractitionerRole,"
            " Organization, RelatedPerson, Patient, CareTeam, HealthcareService, "
            "Device` (represented as `dict` in JSON)"
        ),
        description="Who will be responsible?",
    )

    productCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What is to be administered/supplied",
        one_of_many="product",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    productReference: fhirtypes.ReferenceType = Field(
        None,
        alias="productReference",
        title=(
            "Type `Reference` referencing `Medication, Substance` (represented as "
            "`dict` in JSON)"
        ),
        description="What is to be administered/supplied",
        one_of_many="product",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="How much to administer/supply/consume",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why activity should be done or why activity was prohibited",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "DiagnosticReport, DocumentReference` (represented as `dict` in JSON)"
        ),
        description="Why activity is needed",
    )

    scheduledPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="scheduledPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When activity is to occur",
        one_of_many="scheduled",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    scheduledString: fhirtypes.String = Field(
        None,
        alias="scheduledString",
        title="Type `String` (represented as `dict` in JSON)",
        description="When activity is to occur",
        one_of_many="scheduled",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    scheduledTiming: fhirtypes.TimingType = Field(
        None,
        alias="scheduledTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="When activity is to occur",
        one_of_many="scheduled",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "not-started | scheduled | in-progress | on-hold | completed | "
            "cancelled | stopped | unknown | entered-in-error"
        ),
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reason for current status",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
