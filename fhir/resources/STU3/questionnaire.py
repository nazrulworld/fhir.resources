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
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Questionnaire(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A structured set of questions.
    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """

    resource_type = Field("Questionnaire", const=True)

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date`",
        description="When the questionnaire was approved by publisher",
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
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
        description="Natural language description of the questionnaire",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
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
        title="Type `Date`",
        description="When the questionnaire was last reviewed",
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this questionnaire (computer friendly)",
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
        description="Why this questionnaire is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
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

    subjectType: ListType[fhirtypes.Code] = Field(
        None,
        alias="subjectType",
        title="List of `Code` items",
        description="Resource that can be subject of QuestionnaireResponse",
    )
    subjectType__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_subjectType", title="Extension field for ``subjectType``.")

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this questionnaire (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this questionnaire (globally unique)",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
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
        description="Business version of the questionnaire",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class QuestionnaireItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Questions and sections within the Questionnaire.
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
        title="Type `Uri`",
        description="ElementDefinition - details for the item",
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    enableWhen: ListType[fhirtypes.QuestionnaireItemEnableWhenType] = Field(
        None,
        alias="enableWhen",
        title=(
            "List of `QuestionnaireItemEnableWhen` items (represented as `dict` in "
            "JSON)"
        ),
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
    initialBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initialBoolean", title="Extension field for ``initialBoolean``."
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
        title="Type `Date`",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    initialDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initialDate", title="Extension field for ``initialDate``."
    )

    initialDateTime: fhirtypes.DateTime = Field(
        None,
        alias="initialDateTime",
        title="Type `DateTime`",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    initialDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initialDateTime", title="Extension field for ``initialDateTime``."
    )

    initialDecimal: fhirtypes.Decimal = Field(
        None,
        alias="initialDecimal",
        title="Type `Decimal`",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    initialDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initialDecimal", title="Extension field for ``initialDecimal``."
    )

    initialInteger: fhirtypes.Integer = Field(
        None,
        alias="initialInteger",
        title="Type `Integer`",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    initialInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initialInteger", title="Extension field for ``initialInteger``."
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
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    initialString: fhirtypes.String = Field(
        None,
        alias="initialString",
        title="Type `String`",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    initialString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initialString", title="Extension field for ``initialString``."
    )

    initialTime: fhirtypes.Time = Field(
        None,
        alias="initialTime",
        title="Type `Time`",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    initialTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initialTime", title="Extension field for ``initialTime``."
    )

    initialUri: fhirtypes.Uri = Field(
        None,
        alias="initialUri",
        title="Type `Uri`",
        description="Default value when item is first rendered",
        one_of_many="initial",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    initialUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_initialUri", title="Extension field for ``initialUri``."
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
        title="Type `String`",
        description="Unique id for item in questionnaire",
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    maxLength: fhirtypes.Integer = Field(
        None,
        alias="maxLength",
        title="Type `Integer`",
        description="No more than this many characters",
    )
    maxLength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxLength", title="Extension field for ``maxLength``."
    )

    option: ListType[fhirtypes.QuestionnaireItemOptionType] = Field(
        None,
        alias="option",
        title=(
            "List of `QuestionnaireItemOption` items (represented as `dict` in " "JSON)"
        ),
        description="Permitted answer",
    )

    options: fhirtypes.ReferenceType = Field(
        None,
        alias="options",
        title=(
            "Type `Reference` referencing `ValueSet` (represented as `dict` in " "JSON)"
        ),
        description="Valueset containing permitted answers",
    )

    prefix: fhirtypes.String = Field(
        None, alias="prefix", title="Type `String`", description='E.g. "1(a)", "2.5.3"'
    )
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_prefix", title="Extension field for ``prefix``."
    )

    readOnly: bool = Field(
        None,
        alias="readOnly",
        title="Type `bool`",
        description="Don\u0027t allow human editing",
    )
    readOnly__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_readOnly", title="Extension field for ``readOnly``."
    )

    repeats: bool = Field(
        None,
        alias="repeats",
        title="Type `bool`",
        description="Whether the item may repeat",
    )
    repeats__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_repeats", title="Extension field for ``repeats``."
    )

    required: bool = Field(
        None,
        alias="required",
        title="Type `bool`",
        description="Whether the item must be included in data results",
    )
    required__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_required", title="Extension field for ``required``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String`",
        description="Primary text for the item",
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="group | display | boolean | decimal | integer | date | dateTime +",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
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


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Only allow data when.
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
    answerBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerBoolean", title="Extension field for ``answerBoolean``."
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
        title="Type `Date`",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    answerDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerDate", title="Extension field for ``answerDate``."
    )

    answerDateTime: fhirtypes.DateTime = Field(
        None,
        alias="answerDateTime",
        title="Type `DateTime`",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    answerDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerDateTime", title="Extension field for ``answerDateTime``."
    )

    answerDecimal: fhirtypes.Decimal = Field(
        None,
        alias="answerDecimal",
        title="Type `Decimal`",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    answerDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerDecimal", title="Extension field for ``answerDecimal``."
    )

    answerInteger: fhirtypes.Integer = Field(
        None,
        alias="answerInteger",
        title="Type `Integer`",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    answerInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerInteger", title="Extension field for ``answerInteger``."
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
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    answerString: fhirtypes.String = Field(
        None,
        alias="answerString",
        title="Type `String`",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    answerString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerString", title="Extension field for ``answerString``."
    )

    answerTime: fhirtypes.Time = Field(
        None,
        alias="answerTime",
        title="Type `Time`",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    answerTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerTime", title="Extension field for ``answerTime``."
    )

    answerUri: fhirtypes.Uri = Field(
        None,
        alias="answerUri",
        title="Type `Uri`",
        description="Value question must have",
        one_of_many="answer",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    answerUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_answerUri", title="Extension field for ``answerUri``."
    )

    hasAnswer: bool = Field(
        None,
        alias="hasAnswer",
        title="Type `bool`",
        description="Enable when answered or not",
    )
    hasAnswer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_hasAnswer", title="Extension field for ``hasAnswer``."
    )

    question: fhirtypes.String = Field(
        ...,
        alias="question",
        title="Type `String`",
        description="Question that determines whether item is enabled",
    )
    question__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_question", title="Extension field for ``question``."
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


class QuestionnaireItemOption(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Permitted answer.
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
        title="Type `Date`",
        description="Answer value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer`",
        description="Answer value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`",
        description="Answer value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time`",
        description="Answer value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
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
