# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/questionnaireresponse.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class QuestionnaireResponse(domainresource.DomainResource):
    """A structured set of questions and their answers



    A structured set of questions and their answers. The questions
    are ordered and grouped into coherent subsets, corresponding
    to the structure of the grouping of the underlying questions.
    """

    resource_type = Field("QuestionnaireResponse", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique id for this set of answers",
        description=(
            "A business identifier assigned to a particular "
            "completed (or partially completed) questionnaire."
        ),
        element_property=True,
    )

    questionnaire: fhirtypes.ReferenceType = Field(
        None,
        alias="questionnaire",
        title="Type 'Reference' referencing 'Questionnaire'  (represented as 'dict' in JSON).",
        description="Form being answered",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Questionnaire"],
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON).",
        description="in-progress | completed | amended",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["in-progress", "completed", "amended"],
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="The subject of the questions",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type 'Reference' referencing 'Device', 'Practitioner', "
            "'Patient' and 'RelatedPerson'  (represented as 'dict' in JSON)."
        ),
        description="Person who received and recorded the answers",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "Practitioner", "Patient", "RelatedPerson"],
        element_property=True,
    )

    authored: fhirtypes.DateTime = Field(
        None,
        alias="authored",
        title="Date this version was authored",
        description=(
            "The date and/or time that this version of "
            "the questionnaire response was authored."
        ),
        element_property=True,
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title=(
            "Type 'Reference' referencing 'Patient', "
            "'Practitioner' and 'RelatedPerson'  (represented as 'dict' in JSON)."
        ),
        description="Person who received and recorded the answers",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "RelatedPerson"],
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type 'Reference' referencing 'Encounter'  (represented as 'dict' in JSON).",
        description="Primary encounter during which the answers were collected",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
        element_property=True,
    )

    group: fhirtypes.QuestionnaireResponseGroupType = Field(
        None,
        alias="group",
        title="Grouped questions",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class QuestionnaireResponseGroup(BackboneElement):
    """Grouped questions

    A group of questions to a possibly similarly grouped set
    of questions in the questionnaire response.
    """

    resource_type = Field("QuestionnaireResponseGroup", const=True)

    linkId: fhirtypes.String = Field(
        None,
        alias="linkId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Corresponding group within Questionnaire",
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this group",
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional text for the group",
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="The subject this group's answers are about",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    group: ListType[fhirtypes.QuestionnaireResponseGroupType] = Field(
        None,
        alias="group",
        title="Nested questionnaire response group",
        description=(
            "A sub-group within a group. "
            "The ordering of groups within this group is relevant."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    question: ListType[fhirtypes.QuestionnaireResponseGroupQuestionType] = Field(
        None,
        alias="question",
        title="Questions in this group",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class QuestionnaireResponseGroupQuestion(BackboneElement):
    """Questions in this group

    Set of questions within this group.
    The order of questions within the group is relevant.
    """

    resource_type = Field("QuestionnaireResponseGroupQuestion", const=True)

    linkId: fhirtypes.String = Field(
        None,
        alias="linkId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Corresponding question within Questionnaire",
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Text of the question as it is shown to the user",
        element_property=True,
    )

    answer: ListType[
        fhirtypes.QuestionnaireResponseGroupQuestionAnswerType
    ] = Field(  # noqa: B950
        None,
        alias="answer",
        title="The response(s) to the question",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class QuestionnaireResponseGroupQuestionAnswer(BackboneElement):
    """The response(s) to the question


    The respondent's answer(s) to the question.
    """

    resource_type = Field("QuestionnaireResponseGroupQuestionAnswer", const=True)

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided "
            "by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided "
            "by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided "
            "by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided "
            "by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided "
            "by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueInstant: fhirtypes.Instant = Field(
        ...,
        alias="valueInstant",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided "
            "by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) "
            "provided by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided "
            "by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) "
            "provided by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided "
            "by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by "
            "the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        ...,
        alias="valueQuantity",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) "
            "provided by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) "
            "provided by the respondent to the question."
        ),
        # if property is element of this resource.
        element_property=True,
        one_of_many="value",
        one_of_many_required=False,
    )

    group: ListType[fhirtypes.QuestionnaireResponseGroupType] = Field(
        None,
        alias="group",
        title="Nested questionnaire response group",
        description=(
            "Nested group, containing nested question for this question. "
            "The order of groups within the question is relevant."
        ),
        # if property is element of this resource.
        element_property=True,
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
            "value": [
                "valueBoolean",
                "valueDecimal",
                "valueInteger",
                "valueDate",
                "valueDateTime",
                "valueInstant",
                "valueTime",
                "valueString",
                "valueUri",
                "valueAttachment",
                "valueCoding",
                "valueQuantity",
                "valueReference",
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
