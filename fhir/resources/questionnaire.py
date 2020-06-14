# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
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
        description="Date last changed",
    )

    derivedFrom: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="derivedFrom",
        title="List of `Canonical` items referencing `Questionnaire` (represented as `dict` in JSON)",
        description="Instantiates protocol or definition",
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
        description="Canonical identifier for this questionnaire, represented as a URI (globally unique)",
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
        description="Business version of the questionnaire",
    )


class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.
    A particular question, question grouping or display text that is part of
    the questionnaire.
    """

    resource_type = Field("QuestionnaireItem", const=True)

    answerOption: ListType[fhirtypes.QuestionnaireItemAnswerOptionType] = Field(
        None,
        alias="answerOption",
        title="List of `QuestionnaireItemAnswerOption` items (represented as `dict` in JSON)",
        description="Permitted answer",
    )

    answerValueSet: fhirtypes.Canonical = Field(
        None,
        alias="answerValueSet",
        title="Type `Canonical` referencing `ValueSet` (represented as `dict` in JSON)",
        description="Valueset containing permitted answers",
    )

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

    enableBehavior: fhirtypes.Code = Field(
        None,
        alias="enableBehavior",
        title="Type `Code` (represented as `dict` in JSON)",
        description="all | any",
    )

    enableWhen: ListType[fhirtypes.QuestionnaireItemEnableWhenType] = Field(
        None,
        alias="enableWhen",
        title="List of `QuestionnaireItemEnableWhen` items (represented as `dict` in JSON)",
        description="Only allow data when",
    )

    initial: ListType[fhirtypes.QuestionnaireItemInitialType] = Field(
        None,
        alias="initial",
        title="List of `QuestionnaireItemInitial` items (represented as `dict` in JSON)",
        description="Initial value(s) when item is first rendered",
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


class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """ Permitted answer.
    One of the permitted answers for a "choice" or "open-choice" question.
    """

    resource_type = Field("QuestionnaireItemAnswerOption", const=True)

    initialSelected: bool = Field(
        None,
        alias="initialSelected",
        title="Type `bool`",
        description="Whether option is selected by default",
    )

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

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
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
                "valueReference",
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


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ Only allow data when.
    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """

    resource_type = Field("QuestionnaireItemEnableWhen", const=True)

    answerBoolean: bool = Field(
        None,
        alias="answerBoolean",
        title="Type `bool`",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    answerCoding: fhirtypes.CodingType = Field(
        None,
        alias="answerCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    answerDate: fhirtypes.Date = Field(
        None,
        alias="answerDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    answerDateTime: fhirtypes.DateTime = Field(
        None,
        alias="answerDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    answerDecimal: fhirtypes.Decimal = Field(
        None,
        alias="answerDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    answerInteger: fhirtypes.Integer = Field(
        None,
        alias="answerInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    answerQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="answerQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    answerReference: fhirtypes.ReferenceType = Field(
        None,
        alias="answerReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    answerString: fhirtypes.String = Field(
        None,
        alias="answerString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    answerTime: fhirtypes.Time = Field(
        None,
        alias="answerTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Value for question comparison based on operator",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    operator: fhirtypes.Code = Field(
        ...,
        alias="operator",
        title="Type `Code` (represented as `dict` in JSON)",
        description="exists | = | != | \u003e | \u003c | \u003e= | \u003c=",
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


class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """ Initial value(s) when item is first rendered.
    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """

    resource_type = Field("QuestionnaireItemInitial", const=True)

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Actual value for initializing the question",
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
