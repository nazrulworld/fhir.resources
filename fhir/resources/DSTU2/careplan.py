# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CarePlan
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class CarePlan(DomainResource):
    """Healthcare plan for patient or group.

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

    author: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title=(
            "List of `Reference` items referencing `Patient, Practitioner, "
            "RelatedPerson, Organization, CareTeam` (represented as `dict` in JSON)"
        ),
        description="Who is responsible for contents of the plan",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of plan",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title=(
            "Type `Reference` referencing `Encounter, EpisodeOfCare` (represented "
            "as `dict` in JSON)"
        ),
        description="Created in context of",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Summary of nature of plan",
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

    note: fhirtypes.AnnotationType = Field(
        None,
        alias="note",
        title="Type `Annotation` items (represented as `dict` in JSON)",
        description="Comments about the plan",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period plan covers",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "draft | active | suspended | completed | entered-in-error | cancelled "
            "| unknown"
        ),
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Who care plan is for",
    )

    support: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="support",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Information considered as part of plan",
    )

    modified: fhirtypes.DateTime = Field(
        None,
        alias="title",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When last updated",
    )
    participant: ListType[fhirtypes.CarePlanParticipantType] = Field(
        None,
        alias="participant",
        title="List of `CarePlanParticipant` items (represented as `dict` in JSON).",
        description="Who's involved in plan?.",
    )

    relatedPlan: ListType[fhirtypes.CarePlanRelatedPlanType] = Field(
        None,
        alias="relatedPlan",
        title="Plans related to this one.",
        description="List of `CarePlanRelatedPlan` items (represented as `dict` in JSON).",
    )


class CarePlanActivity(BackboneElement):
    """Action to occur as part of plan.

    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """

    resource_type = Field("CarePlanActivity", const=True)

    actionResulting: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="actionResulting",
        title=(
            "List of `Reference` items referencing `Resource` "
            "(represented as `dict` in JSON)."
        ),
        description="Appointments, orders, etc..",
    )

    detail: fhirtypes.CarePlanActivityDetailType = Field(
        None,
        alias="detail",
        title="Type `CarePlanActivityDetail` (represented as `dict` in JSON).",
        description="In-line definition of activity.",
    )

    progress: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="progress",
        title="List of `Annotation` items (represented as `dict` in JSON).",
        description="Comments about the activity status/progress.",
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title=(
            "Type `Reference` referencing `Appointment, CommunicationRequest, "
            "DeviceUseRequest, DiagnosticOrder, MedicationOrder, "
            "NutritionOrder, Order, ProcedureRequest, ProcessRequest, "
            "ReferralRequest, SupplyRequest, VisionPrescription` "
            "(represented as `dict` in JSON)."
        ),
        description="Activity details defined in specific resource.",
    )


class CarePlanActivityDetail(BackboneElement):
    """In-line definition of activity.

    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """

    resource_type = Field("CarePlanActivityDetail", const=True)
    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="diet | drug | encounter | observation | procedure | supply | other.",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Detail type of activity.",
    )

    dailyAmount: fhirtypes.QuantityType = Field(
        None,
        alias="dailyAmount",
        title="Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON).",
        description="How to consume/day?.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `str`.",
        description="Extra info describing activity to perform.",
    )

    goal: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="goal",
        title="List of `Reference` items referencing `Goal` (represented as `dict` in JSON).",
        description="Goals this activity relates to.",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON).",
        description="Where it should happen.",
    )

    performer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title=(
            "List of `Reference` items referencing `Practitioner,"
            " Organization, RelatedPerson, Patient` "
            "(represented as `dict` in JSON)."
        ),
        description="Who will be responsible?.",
    )

    productCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="What is to be administered/supplied.",
        one_of_many="product",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    productReference: fhirtypes.ReferenceType = Field(
        None,
        alias="productReference",
        title=(
            "Type `Reference` referencing `Medication, Substance`"
            " (represented as `dict` in JSON)."
        ),
        description="What is to be administered/supplied.",
        one_of_many="product",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    prohibited: fhirtypes.Boolean = Field(
        None, alias="prohibited", title="Type `bool`.", description="Do NOT do."
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` "
            "(represented as `dict` in JSON)."
        ),
        description="How much to administer/supply/consume.",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Why activity should be done.",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition` "
            "(represented as `dict` in JSON)."
        ),
        description="Condition triggering need for activity.",
    )

    scheduledPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="scheduledPeriod",
        title="Type `Period` (represented as `dict` in JSON).",
        description="When activity is to occur.",
        one_of_many="scheduled",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    scheduledString: fhirtypes.String = Field(
        None,
        alias="scheduledString",
        title="Type `str`.",
        description="When activity is to occur.",
        one_of_many="scheduled",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    scheduledTiming: fhirtypes.TimingType = Field(
        None,
        alias="scheduledTiming",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="When activity is to occur.",
        one_of_many="scheduled",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `str`.",
        description="not-started | scheduled | in-progress | on-hold | completed | cancelled.",
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Reason for current status.",
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
            "scheduled": ["scheduledPeriod", "scheduledString", "scheduledTiming"],
            "product": ["productCodeableConcept", "productReference"],
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


class CarePlanParticipant(BackboneElement):
    """Who's involved in plan?.

    Identifies all people and organizations who are expected to be involved in
    the care envisioned by this plan.
    """

    resource_type = Field("CarePlanParticipant", const=True)
    member: fhirtypes.ReferenceType = Field(
        None,
        alias="member",
        title=(
            "Type `Reference` referencing `Practitioner, RelatedPerson,"
            " Patient, Organization` (represented as `dict` in JSON)."
        ),
        description="Who is involved.",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Type of involvement.",
    )


class CarePlanRelatedPlan(BackboneElement):
    """Plans related to this one.

    Identifies CarePlans with some sort of formal relationship to the current
    plan.
    """

    resource_type = Field("CarePlanRelatedPlan", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `str`.",
        description="includes | replaces | fulfills.",
    )

    plan: fhirtypes.ReferenceType = Field(
        ...,
        alias="plan",
        title="Plan relationship exists with.",
        description="Type `Reference` referencing `CarePlan` (represented as `dict` in JSON).",
    )
