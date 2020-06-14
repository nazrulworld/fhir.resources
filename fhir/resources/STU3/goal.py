# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Goal
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Goal(domainresource.DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.
    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    resource_type = Field("Goal", const=True)

    addresses: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="addresses",
        title="List of `Reference` items referencing `Condition, Observation, MedicationStatement, NutritionOrder, ProcedureRequest, RiskAssessment` (represented as `dict` in JSON)",
        description="Issues addressed by this goal",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="E.g. Treatment, dietary, behavioral, etc.",
    )

    description: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="description",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Code or text describing goal",
    )

    expressedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="expressedBy",
        title="Type `Reference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON)",
        description="Who\u0027s responsible for creating Goal?",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Ids for this goal",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments about the goal",
    )

    outcomeCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="outcomeCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="What result was achieved regarding the goal?",
    )

    outcomeReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="outcomeReference",
        title="List of `Reference` items referencing `Observation` (represented as `dict` in JSON)",
        description="Observation that resulted from goal",
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="high-priority | medium-priority | low-priority",
    )

    startCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="startCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="When goal pursuit begins",
        one_of_many="start",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    startDate: fhirtypes.Date = Field(
        None,
        alias="startDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When goal pursuit begins",
        one_of_many="start",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="proposed | accepted | planned | in-progress | on-target | ahead-of-target | behind-target | sustaining | achieved | on-hold | cancelled | entered-in-error | rejected",
    )

    statusDate: fhirtypes.Date = Field(
        None,
        alias="statusDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When goal status took effect",
    )

    statusReason: fhirtypes.String = Field(
        None,
        alias="statusReason",
        title="Type `String` (represented as `dict` in JSON)",
        description="Reason for current status",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group, Organization` (represented as `dict` in JSON)",
        description="Who this goal is intended for",
    )

    target: fhirtypes.GoalTargetType = Field(
        None,
        alias="target",
        title="Type `GoalTarget` (represented as `dict` in JSON)",
        description="Target outcome for the goal",
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
            "start": ["startCodeableConcept", "startDate",],
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


class GoalTarget(backboneelement.BackboneElement):
    """ Target outcome for the goal.
    Indicates what should be done by when.
    """

    resource_type = Field("GoalTarget", const=True)

    detailCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="detailCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The target value to be achieved",
        one_of_many="detail",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    detailQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="detailQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The target value to be achieved",
        one_of_many="detail",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    detailRange: fhirtypes.RangeType = Field(
        None,
        alias="detailRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="The target value to be achieved",
        one_of_many="detail",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    dueDate: fhirtypes.Date = Field(
        None,
        alias="dueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Reach goal on or before",
        one_of_many="due",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    dueDuration: fhirtypes.DurationType = Field(
        None,
        alias="dueDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Reach goal on or before",
        one_of_many="due",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    measure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="measure",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The parameter whose value is being tracked",
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
            "detail": ["detailCodeableConcept", "detailQuantity", "detailRange",],
            "due": ["dueDate", "dueDuration",],
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
