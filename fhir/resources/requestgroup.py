# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RequestGroup
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class RequestGroup(domainresource.DomainResource):
    """ A group of related requests.
    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """

    resource_type = Field("RequestGroup", const=True)

    action: ListType[fhirtypes.RequestGroupActionType] = Field(
        None,
        alias="action",
        title="List of `RequestGroupAction` items (represented as `dict` in JSON)",
        description="Proposed actions, if any",
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Device, Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="Device or practitioner that authored the request group",
    )

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the request group was authored",
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Fulfills plan, proposal, or order",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What\u0027s being requested/ordered",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Created as part of",
    )

    groupIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="groupIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Composite request this is part of",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier",
    )

    instantiatesCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="instantiatesCanonical",
        title="List of `Canonical` items (represented as `dict` in JSON)",
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
        description=(
            "proposal | plan | directive | order | original-order | reflex-order | "
            "filler-order | instance-order | option"
        ),
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Additional notes about the response",
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Code` (represented as `dict` in JSON)",
        description="routine | urgent | asap | stat",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why the request group is needed",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "DiagnosticReport, DocumentReference` (represented as `dict` in JSON)"
        ),
        description="Why the request group is needed",
    )

    replaces: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Request(s) replaced by this request",
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
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Who the request group is about",
    )


class RequestGroupAction(backboneelement.BackboneElement):
    """ Proposed actions, if any.
    The actions, if any, produced by the evaluation of the artifact.
    """

    resource_type = Field("RequestGroupAction", const=True)

    action: ListType[fhirtypes.RequestGroupActionType] = Field(
        None,
        alias="action",
        title="List of `RequestGroupAction` items (represented as `dict` in JSON)",
        description="Sub action",
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

    condition: ListType[fhirtypes.RequestGroupActionConditionType] = Field(
        None,
        alias="condition",
        title=(
            "List of `RequestGroupActionCondition` items (represented as `dict` in "
            "JSON)"
        ),
        description="Whether or not the action is applicable",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short description of the action",
    )

    documentation: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="documentation",
        title="List of `RelatedArtifact` items (represented as `dict` in JSON)",
        description="Supporting documentation for the intended performer of the action",
    )

    groupingBehavior: fhirtypes.Code = Field(
        None,
        alias="groupingBehavior",
        title="Type `Code` (represented as `dict` in JSON)",
        description="visual-group | logical-group | sentence-group",
    )

    participant: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="participant",
        title=(
            "List of `Reference` items referencing `Patient, Practitioner, "
            "PractitionerRole, RelatedPerson, Device` (represented as `dict` in "
            "JSON)"
        ),
        description="Who should perform the action",
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

    relatedAction: ListType[fhirtypes.RequestGroupActionRelatedActionType] = Field(
        None,
        alias="relatedAction",
        title=(
            "List of `RequestGroupActionRelatedAction` items (represented as `dict`"
            " in JSON)"
        ),
        description="Relationship to another action",
    )

    requiredBehavior: fhirtypes.Code = Field(
        None,
        alias="requiredBehavior",
        title="Type `Code` (represented as `dict` in JSON)",
        description="must | could | must-unless-documented",
    )

    resource: fhirtypes.ReferenceType = Field(
        None,
        alias="resource",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="The target of the action",
    )

    selectionBehavior: fhirtypes.Code = Field(
        None,
        alias="selectionBehavior",
        title="Type `Code` (represented as `dict` in JSON)",
        description="any | all | all-or-none | exactly-one | at-most-one | one-or-more",
    )

    textEquivalent: fhirtypes.String = Field(
        None,
        alias="textEquivalent",
        title="Type `String` (represented as `dict` in JSON)",
        description=(
            "Static text equivalent of the action, used if the dynamic aspects "
            "cannot be interpreted by the receiving system"
        ),
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
            "timing": [
                "timingAge",
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


class RequestGroupActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.
    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """

    resource_type = Field("RequestGroupActionCondition", const=True)

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


class RequestGroupActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """

    resource_type = Field("RequestGroupActionRelatedAction", const=True)

    actionId: fhirtypes.Id = Field(
        ...,
        alias="actionId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="What action this is related to",
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
        description=(
            "before-start | before | before-end | concurrent-with-start | "
            "concurrent | concurrent-with-end | after-start | after | after-end"
        ),
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
