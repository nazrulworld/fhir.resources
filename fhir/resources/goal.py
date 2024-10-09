from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Goal
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Goal(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the intended objective(s) for a patient, group or organization.
    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    __resource_type__ = "Goal"

    achievementStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="achievementStatus",
        title=(
            "in-progress | improving | worsening | no-change | achieved | "
            "sustaining | not-achieved | no-progress | not-attainable"
        ),
        description=(
            "Describes the progression, or lack thereof, towards the goal against "
            "the target."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    addresses: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="addresses",
        title="Issues addressed by this goal",
        description=(
            "The identified conditions and other health record elements that are "
            "intended to be addressed by the goal."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Condition",
                "Observation",
                "MedicationStatement",
                "MedicationRequest",
                "NutritionOrder",
                "ServiceRequest",
                "RiskAssessment",
                "Procedure",
            ],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="E.g. Treatment, dietary, behavioral, etc",
        description="Indicates a category the goal falls within.",
        json_schema_extra={
            "element_property": True,
        },
    )

    continuous: bool | None = Field(  # type: ignore
        None,
        alias="continuous",
        title=(
            "After meeting the goal, ongoing activity is needed to sustain the goal"
            " objective"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    continuous__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_continuous", title="Extension field for ``continuous``."
    )

    description: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="description",
        title="Code or text describing goal",
        description=(
            "Human-readable and/or coded description of a specific desired "
            'objective of care, such as "control blood pressure" or "negotiate an '
            'obstacle course" or "dance with child at wedding".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Ids for this goal",
        description=(
            "Business identifiers assigned to this goal by the performer or other "
            "systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lifecycleStatus: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="lifecycleStatus",
        title=(
            "proposed | planned | accepted | active | on-hold | completed | "
            "cancelled | entered-in-error | rejected"
        ),
        description="The state of the goal throughout its lifecycle.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "proposed",
                "planned",
                "accepted",
                "active",
                "on-hold",
                "completed",
                "cancelled",
                "entered-in-error",
                "rejected",
            ],
        },
    )
    lifecycleStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lifecycleStatus", title="Extension field for ``lifecycleStatus``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments about the goal",
        description="Any comments related to the goal.",
        json_schema_extra={
            "element_property": True,
        },
    )

    outcome: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="What result was achieved regarding the goal?",
        description=(
            "Identifies the change (or lack of change) at the point when the status"
            " of the goal is assessed."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Observation"],
        },
    )

    priority: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="high-priority | medium-priority | low-priority",
        description=(
            "Identifies the mutually agreed level of importance associated with "
            "reaching/sustaining the goal."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    source: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Who's responsible for creating Goal?",
        description="Indicates whose goal this is - patient goal, practitioner goal, etc.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
                "CareTeam",
            ],
        },
    )

    startCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="startCodeableConcept",
        title="When goal pursuit begins",
        description="The date or event after which the goal should begin being pursued.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e start[x]
            "one_of_many": "start",
            "one_of_many_required": False,
        },
    )

    startDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="startDate",
        title="When goal pursuit begins",
        description="The date or event after which the goal should begin being pursued.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e start[x]
            "one_of_many": "start",
            "one_of_many_required": False,
        },
    )
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_startDate", title="Extension field for ``startDate``."
    )

    statusDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="statusDate",
        title="When goal status took effect",
        description=(
            "Identifies when the current status.  I.e. When initially created, when"
            " achieved, when cancelled, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    statusReason: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current status.",
        json_schema_extra={
            "element_property": True,
        },
    )
    statusReason__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_statusReason", title="Extension field for ``statusReason``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who this goal is intended for",
        description=(
            "Identifies the patient, group or organization for whom the goal is "
            "being established."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group", "Organization"],
        },
    )

    target: typing.List[fhirtypes.GoalTargetType] | None = Field(  # type: ignore
        None,
        alias="target",
        title="Target outcome for the goal",
        description="Indicates what should be done by when.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Goal`` according specification,
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
            "lifecycleStatus",
            "achievementStatus",
            "category",
            "continuous",
            "priority",
            "description",
            "subject",
            "startDate",
            "startCodeableConcept",
            "target",
            "statusDate",
            "statusReason",
            "source",
            "addresses",
            "note",
            "outcome",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("lifecycleStatus", "lifecycleStatus__ext")]
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
        one_of_many_fields = {"start": ["startCodeableConcept", "startDate"]}
        return one_of_many_fields


class GoalTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Target outcome for the goal.
    Indicates what should be done by when.
    """

    __resource_type__ = "GoalTarget"

    detailBoolean: bool | None = Field(  # type: ignore
        None,
        alias="detailBoolean",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e detail[x]
            "one_of_many": "detail",
            "one_of_many_required": False,
        },
    )
    detailBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_detailBoolean", title="Extension field for ``detailBoolean``."
    )

    detailCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="detailCodeableConcept",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e detail[x]
            "one_of_many": "detail",
            "one_of_many_required": False,
        },
    )

    detailInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="detailInteger",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e detail[x]
            "one_of_many": "detail",
            "one_of_many_required": False,
        },
    )
    detailInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_detailInteger", title="Extension field for ``detailInteger``."
    )

    detailQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="detailQuantity",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e detail[x]
            "one_of_many": "detail",
            "one_of_many_required": False,
        },
    )

    detailRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="detailRange",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e detail[x]
            "one_of_many": "detail",
            "one_of_many_required": False,
        },
    )

    detailRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="detailRatio",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e detail[x]
            "one_of_many": "detail",
            "one_of_many_required": False,
        },
    )

    detailString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="detailString",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e detail[x]
            "one_of_many": "detail",
            "one_of_many_required": False,
        },
    )
    detailString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_detailString", title="Extension field for ``detailString``."
    )

    dueDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="dueDate",
        title="Reach goal on or before",
        description=(
            "Indicates either the date or the duration after start by which the "
            "goal should be met."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e due[x]
            "one_of_many": "due",
            "one_of_many_required": False,
        },
    )
    dueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_dueDate", title="Extension field for ``dueDate``."
    )

    dueDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="dueDuration",
        title="Reach goal on or before",
        description=(
            "Indicates either the date or the duration after start by which the "
            "goal should be met."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e due[x]
            "one_of_many": "due",
            "one_of_many_required": False,
        },
    )

    measure: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="measure",
        title="The parameter whose value is being tracked",
        description=(
            "The parameter whose value is being tracked, e.g. body weight, blood "
            "pressure, or hemoglobin A1c level."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``GoalTarget`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "measure",
            "detailQuantity",
            "detailRange",
            "detailCodeableConcept",
            "detailString",
            "detailBoolean",
            "detailInteger",
            "detailRatio",
            "dueDate",
            "dueDuration",
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
            "detail": [
                "detailBoolean",
                "detailCodeableConcept",
                "detailInteger",
                "detailQuantity",
                "detailRange",
                "detailRatio",
                "detailString",
            ],
            "due": ["dueDate", "dueDuration"],
        }
        return one_of_many_fields
