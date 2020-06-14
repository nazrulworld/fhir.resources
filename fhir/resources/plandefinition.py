# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class PlanDefinition(domainresource.DomainResource):
    """ The definition of a plan for a series of actions, independent of any
    specific patient or context.
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    resource_type = Field("PlanDefinition", const=True)

    action: ListType[fhirtypes.PlanDefinitionActionType] = Field(
        None,
        alias="action",
        title="List of `PlanDefinitionAction` items (represented as `dict` in JSON)",
        description="Action defined by the plan",
    )

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the plan definition was approved by publisher",
    )

    author: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who authored the content",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the plan definition",
    )

    editor: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="editor",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who edited the content",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the plan definition is expected to be used",
    )

    endorser: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who endorsed the content",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    goal: ListType[fhirtypes.PlanDefinitionGoalType] = Field(
        None,
        alias="goal",
        title="List of `PlanDefinitionGoal` items (represented as `dict` in JSON)",
        description="What the plan is trying to accomplish",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the plan definition",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for plan definition (if applicable)",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the plan definition was last reviewed",
    )

    library: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="library",
        title="List of `Canonical` items referencing `Library` (represented as `dict` in JSON)",
        description="Logic used by the plan definition",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this plan definition (computer friendly)",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Why this plan definition is defined",
    )

    relatedArtifact: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="Additional documentation, citations",
    )

    reviewer: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Who reviewed the content",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of individual the plan definition is focused on",
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type `Reference` referencing `Group` (represented as `dict` in JSON)",
        description="Type of individual the plan definition is focused on",
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Type `String` (represented as `dict` in JSON)",
        description="Subordinate title of the plan definition",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this plan definition (human friendly)",
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="E.g. Education, Treatment, Assessment",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="order-set | clinical-protocol | eca-rule | workflow-definition",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Canonical identifier for this plan definition, represented as a URI (globally unique)",
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Type `String` (represented as `dict` in JSON)",
        description="Describes the clinical usage of the plan",
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the plan definition",
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
            "subject": ["subjectCodeableConcept", "subjectReference",],
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


class PlanDefinitionAction(backboneelement.BackboneElement):
    """ Action defined by the plan.
    An action or group of actions to be taken as part of the plan.
    """

    resource_type = Field("PlanDefinitionAction", const=True)

    action: ListType[fhirtypes.PlanDefinitionActionType] = Field(
        None,
        alias="action",
        title="List of `PlanDefinitionAction` items (represented as `dict` in JSON)",
        description="A sub-action",
    )

    cardinalityBehavior: fhirtypes.Code = Field(
        None,
        alias="cardinalityBehavior",
        title="Type `Code` (represented as `dict` in JSON)",
        description="single | multiple",
    )

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Code representing the meaning of the action or sub-actions",
    )

    condition: ListType[fhirtypes.PlanDefinitionActionConditionType] = Field(
        None,
        alias="condition",
        title="List of `PlanDefinitionActionCondition` items (represented as `dict` in JSON)",
        description="Whether or not the action is applicable",
    )

    definitionCanonical: fhirtypes.Canonical = Field(
        None,
        alias="definitionCanonical",
        title="Type `Canonical` referencing `ActivityDefinition, PlanDefinition, Questionnaire` (represented as `dict` in JSON)",
        description="Description of the activity to be performed",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    definitionUri: fhirtypes.Uri = Field(
        None,
        alias="definitionUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Description of the activity to be performed",
        one_of_many="definition",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Brief description of the action",
    )

    documentation: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="documentation",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="Supporting documentation for the intended performer of the action",
    )

    dynamicValue: ListType[fhirtypes.PlanDefinitionActionDynamicValueType] = Field(
        None,
        alias="dynamicValue",
        title="List of `PlanDefinitionActionDynamicValue` items (represented as `dict` in JSON)",
        description="Dynamic aspects of the definition",
    )

    goalId: ListType[fhirtypes.Id] = Field(
        None,
        alias="goalId",
        title="List of `Id` items (represented as `dict` in JSON)",
        description="What goals this action supports",
    )

    groupingBehavior: fhirtypes.Code = Field(
        None,
        alias="groupingBehavior",
        title="Type `Code` (represented as `dict` in JSON)",
        description="visual-group | logical-group | sentence-group",
    )

    input: ListType[fhirtypes.DataRequirementType] = Field(
        None,
        alias="input",
        title="List of `DataRequirement` items (represented as `dict` in JSON)",
        description="Input data requirements",
    )

    output: ListType[fhirtypes.DataRequirementType] = Field(
        None,
        alias="output",
        title="List of `DataRequirement` items (represented as `dict` in JSON)",
        description="Output data definition",
    )

    participant: ListType[fhirtypes.PlanDefinitionActionParticipantType] = Field(
        None,
        alias="participant",
        title="List of `PlanDefinitionActionParticipant` items (represented as `dict` in JSON)",
        description="Who should participate in the action",
    )

    precheckBehavior: fhirtypes.Code = Field(
        None,
        alias="precheckBehavior",
        title="Type `Code` (represented as `dict` in JSON)",
        description="yes | no",
    )

    prefix: fhirtypes.String = Field(
        None,
        alias="prefix",
        title="Type `String` (represented as `dict` in JSON)",
        description="User-visible prefix for the action (e.g. 1. or A.)",
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Code` (represented as `dict` in JSON)",
        description="routine | urgent | asap | stat",
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why the action should be performed",
    )

    relatedAction: ListType[fhirtypes.PlanDefinitionActionRelatedActionType] = Field(
        None,
        alias="relatedAction",
        title="List of `PlanDefinitionActionRelatedAction` items (represented as `dict` in JSON)",
        description="Relationship to another action",
    )

    requiredBehavior: fhirtypes.Code = Field(
        None,
        alias="requiredBehavior",
        title="Type `Code` (represented as `dict` in JSON)",
        description="must | could | must-unless-documented",
    )

    selectionBehavior: fhirtypes.Code = Field(
        None,
        alias="selectionBehavior",
        title="Type `Code` (represented as `dict` in JSON)",
        description="any | all | all-or-none | exactly-one | at-most-one | one-or-more",
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of individual the action is focused on",
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type `Reference` referencing `Group` (represented as `dict` in JSON)",
        description="Type of individual the action is focused on",
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    textEquivalent: fhirtypes.String = Field(
        None,
        alias="textEquivalent",
        title="Type `String` (represented as `dict` in JSON)",
        description="Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system",
    )

    timingAge: fhirtypes.AgeType = Field(
        None,
        alias="timingAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="When the action should take place",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the action should take place",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingDuration: fhirtypes.DurationType = Field(
        None,
        alias="timingDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="When the action should take place",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the action should take place",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingRange: fhirtypes.RangeType = Field(
        None,
        alias="timingRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="When the action should take place",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingTiming: fhirtypes.TimingType = Field(
        None,
        alias="timingTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="When the action should take place",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="User-visible title",
    )

    transform: fhirtypes.Canonical = Field(
        None,
        alias="transform",
        title="Type `Canonical` referencing `StructureMap` (represented as `dict` in JSON)",
        description="Transform to apply the template",
    )

    trigger: ListType[fhirtypes.TriggerDefinitionType] = Field(
        None,
        alias="trigger",
        title="List of `TriggerDefinition` items (represented as `dict` in JSON)",
        description="When the action should be triggered",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="create | update | remove | fire-event",
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
            "definition": ["definitionCanonical", "definitionUri",],
            "subject": ["subjectCodeableConcept", "subjectReference",],
            "timing": [
                "timingAge",
                "timingDateTime",
                "timingDuration",
                "timingPeriod",
                "timingRange",
                "timingTiming",
            ],
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


class PlanDefinitionActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.
    An expression that describes applicability criteria or start/stop
    conditions for the action.
    """

    resource_type = Field("PlanDefinitionActionCondition", const=True)

    expression: fhirtypes.ExpressionType = Field(
        None,
        alias="expression",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="Boolean-valued expression",
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="Type `Code` (represented as `dict` in JSON)",
        description="applicability | start | stop",
    )


class PlanDefinitionActionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.
    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """

    resource_type = Field("PlanDefinitionActionDynamicValue", const=True)

    expression: fhirtypes.ExpressionType = Field(
        None,
        alias="expression",
        title="Type `Expression` (represented as `dict` in JSON)",
        description="An expression that provides the dynamic value for the customization",
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="The path to the element to be set dynamically",
    )


class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    """ Who should participate in the action.
    Indicates who should participate in performing the action described.
    """

    resource_type = Field("PlanDefinitionActionParticipant", const=True)

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="E.g. Nurse, Surgeon, Parent",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="patient | practitioner | related-person | device",
    )


class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """

    resource_type = Field("PlanDefinitionActionRelatedAction", const=True)

    actionId: fhirtypes.Id = Field(
        ...,
        alias="actionId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="What action is this related to",
    )

    offsetDuration: fhirtypes.DurationType = Field(
        None,
        alias="offsetDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Time offset for the relationship",
        one_of_many="offset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    offsetRange: fhirtypes.RangeType = Field(
        None,
        alias="offsetRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Time offset for the relationship",
        one_of_many="offset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    relationship: fhirtypes.Code = Field(
        ...,
        alias="relationship",
        title="Type `Code` (represented as `dict` in JSON)",
        description="before-start | before | before-end | concurrent-with-start | concurrent | concurrent-with-end | after-start | after | after-end",
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
            "offset": ["offsetDuration", "offsetRange",],
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


class PlanDefinitionGoal(backboneelement.BackboneElement):
    """ What the plan is trying to accomplish.
    Goals that describe what the activities within the plan are intended to
    achieve. For example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    resource_type = Field("PlanDefinitionGoal", const=True)

    addresses: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="addresses",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="What does the goal address",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="E.g. Treatment, dietary, behavioral",
    )

    description: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="description",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Code or text describing the goal",
    )

    documentation: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="documentation",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="Supporting documentation for the goal",
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="high-priority | medium-priority | low-priority",
    )

    start: fhirtypes.CodeableConceptType = Field(
        None,
        alias="start",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="When goal pursuit begins",
    )

    target: ListType[fhirtypes.PlanDefinitionGoalTargetType] = Field(
        None,
        alias="target",
        title="List of `PlanDefinitionGoalTarget` items (represented as `dict` in JSON)",
        description="Target outcome for the goal",
    )


class PlanDefinitionGoalTarget(backboneelement.BackboneElement):
    """ Target outcome for the goal.
    Indicates what should be done and within what timeframe.
    """

    resource_type = Field("PlanDefinitionGoalTarget", const=True)

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

    due: fhirtypes.DurationType = Field(
        None,
        alias="due",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Reach goal within",
    )

    measure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="measure",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The parameter whose value is to be tracked",
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
