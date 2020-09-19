# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Goal
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Goal(DomainResource):
    """Describes the intended objective(s) for a patient, group or organization.

    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    resource_type = Field("Goal", const=True)

    addresses: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="addresses",
        title=(
            "List of `Reference` items referencing `Condition, "
            "Observation, MedicationStatement, "
            "NutritionOrder, ProcedureRequest, "
            "RiskAssessment` (represented as `dict` in JSON)."
        ),
        description="Issues addressed by this goal.",
    )
    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, RelatedPerson`"
            "(represented as `dict` in JSON)."
        ),
        description="Who's responsible for creating Goal?.",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="E.g. Treatment, dietary, behavioral, etc..",
    )
    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Type `String`",
        description="What's the desired outcome?.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="External Ids for this goal.",
    )
    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON).",
        description="Comments about the goal.",
    )

    outcome: ListType[fhirtypes.GoalOutcomeType] = Field(
        None,
        alias="outcome",
        title="List of `GoalOutcome` items (represented as `dict` in JSON).",
        description="What was end result of goal?.",
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="high | medium |low.",
    )
    startCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="startCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="When goal pursuit begins.",
        one_of_many="start",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )
    startDate: fhirtypes.Date = Field(
        None,
        alias="startDate",
        title="Type `Date`.",
        description="When goal pursuit begins.",
        one_of_many="start",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description=(
            "proposed | planned | accepted | rejected | in-progress | achieved |"
            "sustaining | on-hold | cancelled."
        ),
    )

    statusDate: fhirtypes.Date = Field(
        None,
        alias="statusDate",
        title="Type `Date`",
        description="When goal status took effect.",
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Reason for current status.",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group,"
            " Organization` (represented as `dict` in JSON)."
        ),
        description="Who this goal is intended for.",
    )

    targetDate: fhirtypes.Date = Field(
        None,
        alias="targetDate",
        title="Type `Date`",
        description="Reach goal on or before.",
        one_of_many="target",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
    )
    targetQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="targetQuantity",
        title="Type `Quantity` referencing `Duration` (represented as `dict` in JSON).",
        description="Reach goal on or before.",
        one_of_many="target",  # Choice of Data Types. i.e reason[x]
        one_of_many_required=False,
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
            "start": ["startCodeableConcept", "startDate"],
            "target": ["targetQuantity", "targetDate"],
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


class GoalOutcome(BackboneElement):
    """What was end result of goal?.

    Identifies the change (or lack of change) at the point where the goal was
    deepmed to be cancelled or achieved.
    """

    resource_type = Field("GoalOutcome", const=True)

    resultCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="resultCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Code or observation that resulted from goal.",
        one_of_many="result",  # Choice of Data Types. i.e result[x]
        one_of_many_required=False,
    )

    resultReference: fhirtypes.ReferenceType = Field(
        None,
        alias="resultReference",
        title="Type `Reference` referencing `Observation` (represented as `dict` in JSON).",
        description="Code or observation that resulted from goal.",
        one_of_many="result",  # Choice of Data Types. i.e result[x]
        one_of_many_required=False,
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
        one_of_many_fields = {"result": ["resultReference", "resultCodeableConcept"]}
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
