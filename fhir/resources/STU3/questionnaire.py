# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.
    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """

    resource_type = Field("Questionnaire", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the questionnaire was approved by publisher",
    )

    code: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Concept that represents the overall questionnaire",
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
        description="Date this was last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the questionnaire",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the questionnaire is expected to be used",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the questionnaire",
    )

    item: ListType[fhirtypes.QuestionnaireItemType] = Field(
        None,
        alias="item",
        title="List of `QuestionnaireItem` items (represented as `dict` in JSON)",
        description="Questions and sections within the Questionnaire",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for questionnaire (if applicable)",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the questionnaire was last reviewed",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this questionnaire (computer friendly)",
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
        description="Why this questionnaire is defined",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    subjectType: ListType[fhirtypes.Code] = Field(
        None,
        alias="subjectType",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Resource that can be subject of QuestionnaireResponse",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this questionnaire (human friendly)",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this questionnaire (globally unique)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the questionnaire",
    )


class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.
    A particular question, question grouping or display text that is part of
    the questionnaire.
    """

    resource_type = Field("QuestionnaireItem", const=True)

    code: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Corresponding concept for this item in a terminology",
    )

    definition: fhirtypes.Uri = Field(
        None,
        alias="definition",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="ElementDefinition - details for the item",
    )

    enableWhen: ListType[fhirtypes.QuestionnaireItemEnableWhenType] = Field(
        None,
        alias="enableWhen",
        title="List of `QuestionnaireItemEnableWhen` items (represented as `dict` in JSON)",
        description="Only allow data when",
    )

    initialAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="initialAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialBoolean: bool = Field(
        None,
        alias="initialBoolean",
        title="Type `bool`",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialCoding: fhirtypes.CodingType = Field(
        None,
        alias="initialCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialDate: fhirtypes.Date = Field(
        None,
        alias="initialDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialDateTime: fhirtypes.DateTime = Field(
        None,
        alias="initialDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialDecimal: fhirtypes.Decimal = Field(
        None,
        alias="initialDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialInteger: fhirtypes.Integer = Field(
        None,
        alias="initialInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="initialQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialReference: fhirtypes.ReferenceType = Field(
        None,
        alias="initialReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialString: fhirtypes.String = Field(
        None,
        alias="initialString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialTime: fhirtypes.Time = Field(
        None,
        alias="initialTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialUri: fhirtypes.Uri = Field(
        None,
        alias="initialUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    item: ListType[fhirtypes.QuestionnaireItemType] = Field(
        None,
        alias="item",
        title="List of `QuestionnaireItem` items (represented as `dict` in JSON)",
        description="Nested questionnaire items",
    )

    linkId: fhirtypes.String = Field(
        ...,
        alias="linkId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Unique id for item in questionnaire",
    )

    maxLength: fhirtypes.Integer = Field(
        None,
        alias="maxLength",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="No more than this many characters",
    )

    option: ListType[fhirtypes.QuestionnaireItemOptionType] = Field(
        None,
        alias="option",
        title="List of `QuestionnaireItemOption` items (represented as `dict` in JSON)",
        description="Permitted answer",
    )

    options: fhirtypes.ReferenceType = Field(
        None,
        alias="options",
        title="Type `Reference` referencing `ValueSet` (represented as `dict` in JSON)",
        description="Valueset containing permitted answers",
    )

    prefix: fhirtypes.String = Field(
        None,
        alias="prefix",
        title="Type `String` (represented as `dict` in JSON)",
        description='E.g. "1(a)", "2.5.3"',
    )

    readOnly: bool = Field(
        None,
        alias="readOnly",
        title="Type `bool`",
        description="Don\u0027t allow human editing",
    )

    repeats: bool = Field(
        None,
        alias="repeats",
        title="Type `bool`",
        description="Whether the item may repeat",
    )

    required: bool = Field(
        None,
        alias="required",
        title="Type `bool`",
        description="Whether the item must be included in data results",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Primary text for the item",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="group | display | boolean | decimal | integer | date | dateTime +",
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
            "initial": [
                "initialAttachment",
                "initialBoolean",
                "initialCoding",
                "initialDate",
                "initialDateTime",
                "initialDecimal",
                "initialInteger",
                "initialQuantity",
                "initialReference",
                "initialString",
                "initialTime",
                "initialUri",
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


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ Only allow data when.
    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """

    resource_type = Field("QuestionnaireItemEnableWhen", const=True)

    answerAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="answerAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerBoolean: bool = Field(
        None,
        alias="answerBoolean",
        title="Type `bool`",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerCoding: fhirtypes.CodingType = Field(
        None,
        alias="answerCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerDate: fhirtypes.Date = Field(
        None,
        alias="answerDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerDateTime: fhirtypes.DateTime = Field(
        None,
        alias="answerDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerDecimal: fhirtypes.Decimal = Field(
        None,
        alias="answerDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerInteger: fhirtypes.Integer = Field(
        None,
        alias="answerInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="answerQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerReference: fhirtypes.ReferenceType = Field(
        None,
        alias="answerReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerString: fhirtypes.String = Field(
        None,
        alias="answerString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerTime: fhirtypes.Time = Field(
        None,
        alias="answerTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerUri: fhirtypes.Uri = Field(
        None,
        alias="answerUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    hasAnswer: bool = Field(
        None,
        alias="hasAnswer",
        title="Type `bool`",
        description="Enable when answered or not",
    )

    question: fhirtypes.String = Field(
        ...,
        alias="question",
        title="Type `String` (represented as `dict` in JSON)",
        description="Question that determines whether item is enabled",
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
            "answer": [
                "answerAttachment",
                "answerBoolean",
                "answerCoding",
                "answerDate",
                "answerDateTime",
                "answerDecimal",
                "answerInteger",
                "answerQuantity",
                "answerReference",
                "answerString",
                "answerTime",
                "answerUri",
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


class QuestionnaireItemOption(backboneelement.BackboneElement):
    """ Permitted answer.
    One of the permitted answers for a "choice" or "open-choice" question.
    """

    resource_type = Field("QuestionnaireItemOption", const=True)

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Answer value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Answer value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Answer value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Answer value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Answer value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
                "valueCoding",
                "valueDate",
                "valueInteger",
                "valueString",
                "valueTime",
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
