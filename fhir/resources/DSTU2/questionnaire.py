# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/questionnaire.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class Questionnaire(domainresource.DomainResource):
    """A structured set of questions



    A structured set of questions intended to guide
    the collection of answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the
    structure of the grouping of the underlying questions.
    """

    resource_type = Field("Questionnaire", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifiers for this questionnaire",
        description=(
            "This records identifiers associated with this "
            "question set that are defined by business processes "
            "and/or used to refer to it when a direct URL reference "
            "to the resource itself is not appropriate (e.g. in CDA "
            "documents, or in written / printed documentation)."
        ),
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Logical identifier for this version of Questionnaire",
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON).",
        description="draft | published | retired",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "published", "retired"],
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date this version was authored",
        description="The date that this questionnaire was last changed.",
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Organization/individual who designed the questionnaire",
        element_property=True,
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact information of the publisher",
        description=(
            "Contact details to assist a user in "
            "finding and communicating with the publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    subjectType: ListType[fhirtypes.Code] = Field(
        None,
        alias="subjectType",
        title="List of Type `Code` (represented as `dict` in JSON).",
        description="Resource that can be subject of QuestionnaireResponse",
        element_property=True,
    )

    group: fhirtypes.QuestionnaireGroupType = Field(
        None,
        alias="group",
        title="Grouped questions",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class QuestionnaireGroup(BackboneElement):
    """Grouped questions

    A collection of related questions (or further groupings of questions).
    """

    resource_type = Field("QuestionnaireGroup", const=True)

    linkId: fhirtypes.String = Field(
        None,
        alias="linkId",
        title="Type `String` (represented as `dict` in JSON)",
        description="To link questionnaire with questionnaire response",
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name to be displayed for group",
        element_property=True,
    )

    concept: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="concept",
        title="Concept that represents this section in a questionnaire",
        description=(
            "Identifies a how this group of questions is known "
            "in a particular terminology such as LOINC."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional text for the group",
        element_property=True,
    )

    required: bool = Field(
        None,
        alias="required",
        title="Whether the group must be included in data results",
        description=(
            "If true, indicates that the group must be present and "
            "have required questions within it answered. If false, "
            "the group may be skipped when answering the questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    repeats: bool = Field(
        None,
        alias="repeats",
        title="Whether the group may repeat",
        description=(
            "Whether the group may occur multiple times in the instance, "
            "containing multiple sets of answers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    group: ListType[fhirtypes.QuestionnaireGroupType] = Field(
        None,
        alias="group",
        title="Nested questionnaire group",
        description=(
            "A sub-group within a group. The ordering of "
            "groups within this group is relevant."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    question: ListType[fhirtypes.QuestionnaireGroupQuestionType] = Field(
        None,
        alias="question",
        title="Questions in this group",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class QuestionnaireGroupQuestion(BackboneElement):
    """Questions in this group

    Set of questions within this group. The order of questions within the group is relevant.
    """

    resource_type = Field("QuestionnaireGroupQuestion", const=True)

    linkId: fhirtypes.String = Field(
        None,
        alias="linkId",
        title="Type `String` (represented as `dict` in JSON)",
        description="To link questionnaire with questionnaire response",
        element_property=True,
    )

    concept: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="concept",
        title="Concept that represents this question in a questionnaire",
        description=(
            "Identifies a how this question is known in "
            "a particular terminology such as LOINC."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Text of the question as it is shown to the user",
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON).",
        description="boolean | decimal | integer | date | dateTime +",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["boolean", "decimal", "integer", "date", "dateTime"],
        element_property=True,
    )

    required: bool = Field(
        None,
        alias="required",
        title="Whether the question must be answered in data results",
        description=(
            "If true, indicates that the question must be "
            "answered and have required groups within it also present. "
            "If false, the question and any contained groups may be "
            "skipped when answering the questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    repeats: bool = Field(
        None,
        alias="repeats",
        title="Whether the question  can have multiple answers",
        description="If true, the question may have more than one answer.",
        # if property is element of this resource.
        element_property=True,
    )

    options: fhirtypes.ReferenceType = Field(
        None,
        alias="options",
        title="Type 'Reference' referencing 'ValueSet' (represented as 'dict' in JSON).",
        description="Valueset containing permitted answers",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
        element_property=True,
    )

    option: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="option",
        title="Permitted answer",
        description=(
            "For a 'choice' question, identifies "
            "one of the permitted answers for the question."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    group: ListType[fhirtypes.QuestionnaireGroupType] = Field(
        None,
        alias="group",
        title="Nested questionnaire group",
        description=(
            "Nested group, containing nested question for this question."
            " The order of groups within the question is relevant."
        ),
        # if property is element of this resource.
        element_property=True,
    )
