# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class QuestionnaireResponse(domainresource.DomainResource):
    """ A structured set of questions and their answers.
    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the questionnaire being responded to.
    """

    resource_type = Field("QuestionnaireResponse", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Type `Reference` referencing `Device, Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON)",
        description="Person who received and recorded the answers",
    )

    authored: fhirtypes.DateTime = Field(
        None,
        alias="authored",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date the answers were gathered",
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="List of `Reference` items referencing `ReferralRequest, CarePlan, ProcedureRequest` (represented as `dict` in JSON)",
        description="Request fulfilled by this QuestionnaireResponse",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Encounter or Episode during which questionnaire was completed",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique id for this set of answers",
    )

    item: ListType[fhirtypes.QuestionnaireResponseItemType] = Field(
        None,
        alias="item",
        title="List of `QuestionnaireResponseItem` items (represented as `dict` in JSON)",
        description="Groups and questions",
    )

    parent: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="parent",
        title="List of `Reference` items referencing `Observation, Procedure` (represented as `dict` in JSON)",
        description="Part of this action",
    )

    questionnaire: fhirtypes.ReferenceType = Field(
        None,
        alias="questionnaire",
        title="Type `Reference` referencing `Questionnaire` (represented as `dict` in JSON)",
        description="Form being answered",
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Type `Reference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON)",
        description="The person who answered the questions",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="in-progress | completed | amended | entered-in-error | stopped",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="The subject of the questions",
    )


class QuestionnaireResponseItem(backboneelement.BackboneElement):
    """ Groups and questions.
    A group or question item from the original questionnaire for which answers
    are provided.
    """

    resource_type = Field("QuestionnaireResponseItem", const=True)

    answer: ListType[fhirtypes.QuestionnaireResponseItemAnswerType] = Field(
        None,
        alias="answer",
        title="List of `QuestionnaireResponseItemAnswer` items (represented as `dict` in JSON)",
        description="The response(s) to the question",
    )

    definition: fhirtypes.Uri = Field(
        None,
        alias="definition",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="ElementDefinition - details for the item",
    )

    item: ListType[fhirtypes.QuestionnaireResponseItemType] = Field(
        None,
        alias="item",
        title="List of `QuestionnaireResponseItem` items (represented as `dict` in JSON)",
        description="Nested questionnaire response items",
    )

    linkId: fhirtypes.String = Field(
        ...,
        alias="linkId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Pointer to specific item from Questionnaire",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="The subject this group\u0027s answers are about",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for group or question text",
    )


class QuestionnaireResponseItemAnswer(backboneelement.BackboneElement):
    """ The response(s) to the question.
    The respondent's answer(s) to the question.
    """

    resource_type = Field("QuestionnaireResponseItemAnswer", const=True)

    item: ListType[fhirtypes.QuestionnaireResponseItemType] = Field(
        None,
        alias="item",
        title="List of `QuestionnaireResponseItem` items (represented as `dict` in JSON)",
        description="Nested groups and questions",
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
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
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCoding",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueInteger",
                "valueQuantity",
                "valueReference",
                "valueString",
                "valueTime",
                "valueUri",
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
