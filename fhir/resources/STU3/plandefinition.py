# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class PlanDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The definition of a plan for a series of actions, independent of any
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
        title="Type `Date`",
        description="When the plan definition was approved by publisher",
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    contributor: ListType[fhirtypes.ContributorType] = Field(
        None,
        alias="contributor",
        title="List of `Contributor` items (represented as `dict` in JSON)",
        description="A content contributor",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="Date this was last changed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the plan definition",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the plan definition is expected to be used",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
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
        title="Type `Date`",
        description="When the plan definition was last reviewed",
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="library",
        title=(
            "List of `Reference` items referencing `Library` (represented as `dict`"
            " in JSON)"
        ),
        description="Logic used by the plan definition",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this plan definition (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String`",
        description="Name of the publisher (organization or individual)",
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown`",
        description="Why this plan definition is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    relatedArtifact: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="Related artifacts for the asset",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="draft | active | retired | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this plan definition (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="E.g. Education, Treatment, Assessment, etc",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="order-set | protocol | eca-rule",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this plan definition (globally unique)",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Type `String`",
        description="Describes the clinical usage of the asset",
    )
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_usage", title="Extension field for ``usage``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="Context the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Business version of the plan definition",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class PlanDefinitionAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Action defined by the plan.
    An action to be taken as part of the plan.
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
        title="Type `Code`",
        description="single | multiple",
    )
    cardinalityBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_cardinalityBehavior",
        title="Extension field for ``cardinalityBehavior``.",
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
        title=(
            "List of `PlanDefinitionActionCondition` items (represented as `dict` "
            "in JSON)"
        ),
        description="Whether or not the action is applicable",
    )

    definition: fhirtypes.ReferenceType = Field(
        None,
        alias="definition",
        title=(
            "Type `Reference` referencing `ActivityDefinition, PlanDefinition` "
            "(represented as `dict` in JSON)"
        ),
        description="Description of the activity to be performed",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Short description of the action",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
        title=(
            "List of `PlanDefinitionActionDynamicValue` items (represented as "
            "`dict` in JSON)"
        ),
        description="Dynamic aspects of the definition",
    )

    goalId: ListType[fhirtypes.Id] = Field(
        None,
        alias="goalId",
        title="List of `Id` items",
        description="What goals this action supports",
    )
    goalId__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_goalId", title="Extension field for ``goalId``."
    )

    groupingBehavior: fhirtypes.Code = Field(
        None,
        alias="groupingBehavior",
        title="Type `Code`",
        description="visual-group | logical-group | sentence-group",
    )
    groupingBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_groupingBehavior",
        title="Extension field for ``groupingBehavior``.",
    )

    input: ListType[fhirtypes.DataRequirementType] = Field(
        None,
        alias="input",
        title="List of `DataRequirement` items (represented as `dict` in JSON)",
        description="Input data requirements",
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Type `String`",
        description="User-visible label for the action (e.g. 1. or A.)",
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
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
        title=(
            "List of `PlanDefinitionActionParticipant` items (represented as `dict`"
            " in JSON)"
        ),
        description="Who should participate in the action",
    )

    precheckBehavior: fhirtypes.Code = Field(
        None, alias="precheckBehavior", title="Type `Code`", description="yes | no"
    )
    precheckBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_precheckBehavior",
        title="Extension field for ``precheckBehavior``.",
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
        title=(
            "List of `PlanDefinitionActionRelatedAction` items (represented as "
            "`dict` in JSON)"
        ),
        description="Relationship to another action",
    )

    requiredBehavior: fhirtypes.Code = Field(
        None,
        alias="requiredBehavior",
        title="Type `Code`",
        description="must | could | must-unless-documented",
    )
    requiredBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_requiredBehavior",
        title="Extension field for ``requiredBehavior``.",
    )

    selectionBehavior: fhirtypes.Code = Field(
        None,
        alias="selectionBehavior",
        title="Type `Code`",
        description="any | all | all-or-none | exactly-one | at-most-one | one-or-more",
    )
    selectionBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_selectionBehavior",
        title="Extension field for ``selectionBehavior``.",
    )

    textEquivalent: fhirtypes.String = Field(
        None,
        alias="textEquivalent",
        title="Type `String`",
        description=(
            "Static text equivalent of the action, used if the dynamic aspects "
            "cannot be interpreted by the receiving system"
        ),
    )
    textEquivalent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_textEquivalent", title="Extension field for ``textEquivalent``."
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="Type `DateTime`",
        description="When the action should take place",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timingDateTime", title="Extension field for ``timingDateTime``."
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
        None, alias="title", title="Type `String`", description="User-visible title"
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    transform: fhirtypes.ReferenceType = Field(
        None,
        alias="transform",
        title=(
            "Type `Reference` referencing `StructureMap` (represented as `dict` in "
            "JSON)"
        ),
        description="Transform to apply the template",
    )

    triggerDefinition: ListType[fhirtypes.TriggerDefinitionType] = Field(
        None,
        alias="triggerDefinition",
        title="List of `TriggerDefinition` items (represented as `dict` in JSON)",
        description="When the action should be triggered",
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON)",
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
            "timing": [
                "timingDateTime",
                "timingDuration",
                "timingPeriod",
                "timingRange",
                "timingTiming",
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


class PlanDefinitionActionCondition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether or not the action is applicable.
    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """

    resource_type = Field("PlanDefinitionActionCondition", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Natural language description of the condition",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String`",
        description="Boolean-valued expression",
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="Type `Code`",
        description="applicability | start | stop",
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    language: fhirtypes.String = Field(
        None,
        alias="language",
        title="Type `String`",
        description="Language of the expression",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )


class PlanDefinitionActionDynamicValue(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dynamic aspects of the definition.
    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """

    resource_type = Field("PlanDefinitionActionDynamicValue", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Natural language description of the dynamic value",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String`",
        description="An expression that provides the dynamic value for the customization",
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    language: fhirtypes.String = Field(
        None,
        alias="language",
        title="Type `String`",
        description="Language of the expression",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String`",
        description="The path to the element to be set dynamically",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )


class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who should participate in the action.
    Indicates who should participate in performing the action described.
    """

    resource_type = Field("PlanDefinitionActionParticipant", const=True)

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="E.g. Nurse, Surgeon, Parent, etc",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="patient | practitioner | related-person",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationship to another action.
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """

    resource_type = Field("PlanDefinitionActionRelatedAction", const=True)

    actionId: fhirtypes.Id = Field(
        ...,
        alias="actionId",
        title="Type `Id`",
        description="What action is this related to",
    )
    actionId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actionId", title="Extension field for ``actionId``."
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
        title="Type `Code`",
        description=(
            "before-start | before | before-end | concurrent-with-start | "
            "concurrent | concurrent-with-end | after-start | after | after-end"
        ),
    )
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relationship", title="Extension field for ``relationship``."
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
        one_of_many_fields = {"offset": ["offsetDuration", "offsetRange"]}
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What the plan is trying to accomplish.
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
        description="E.g. Treatment, dietary, behavioral, etc",
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
        title=(
            "List of `PlanDefinitionGoalTarget` items (represented as `dict` in "
            "JSON)"
        ),
        description="Target outcome for the goal",
    )


class PlanDefinitionGoalTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Target outcome for the goal.
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
            "detail": ["detailCodeableConcept", "detailQuantity", "detailRange"]
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
