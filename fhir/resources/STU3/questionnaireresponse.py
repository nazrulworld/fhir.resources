from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class QuestionnaireResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A structured set of questions and their answers.
    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the questionnaire being responded to.
    """

    __resource_type__ = "QuestionnaireResponse"

    author: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="author",
        title="Person who received and recorded the answers",
        description=(
            "Person who received the answers to the questions in the "
            "QuestionnaireResponse and recorded them in the system."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Device",
                "Practitioner",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    authored: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="authored",
        title="Date the answers were gathered",
        description="The date and/or time that this set of answers were last changed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    authored__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_authored", title="Extension field for ``authored``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Request fulfilled by this QuestionnaireResponse",
        description=(
            "The order, proposal or plan that is fulfilled in whole or in part by "
            "this QuestionnaireResponse.  For example, a ProcedureRequest seeking "
            "an intake assessment or a decision support recommendation to assess "
            "for post-partum depression."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ReferralRequest", "CarePlan", "ProcedureRequest"],
        },
    )

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Encounter or Episode during which questionnaire was completed",
        description=(
            "The encounter or episode of care with primary association to the "
            "questionnaire response."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique id for this set of answers",
        description=(
            "A business identifier assigned to a particular completed (or partially"
            " completed) questionnaire."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    item: typing.List[fhirtypes.QuestionnaireResponseItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Groups and questions",
        description=(
            "A group or question item from the original questionnaire for which "
            "answers are provided."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    parent: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="parent",
        title="Part of this action",
        description=(
            "A procedure or observation that this questionnaire was performed as "
            "part of the execution of.  For example, the surgery a checklist was "
            "executed as part of."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Observation", "Procedure"],
        },
    )

    questionnaire: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="questionnaire",
        title="Form being answered",
        description=(
            "The Questionnaire that defines and organizes the questions for which "
            "answers are being provided."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Questionnaire"],
        },
    )

    source: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="source",
        title="The person who answered the questions",
        description="The person who answered the questions about the subject.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Practitioner", "RelatedPerson"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="in-progress | completed | amended | entered-in-error | stopped",
        description=(
            "The position of the questionnaire response within its overall "
            "lifecycle."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "in-progress",
                "completed",
                "amended",
                "entered-in-error",
                "stopped",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="The subject of the questions",
        description=(
            "The subject of the questionnaire response.  This could be a patient, "
            "organization, practitioner, device, etc.  This is who/what the answers"
            " apply to, but is not necessarily the source of information."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``QuestionnaireResponse`` according specification,
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
            "basedOn",
            "parent",
            "questionnaire",
            "status",
            "subject",
            "context",
            "authored",
            "author",
            "source",
            "item",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class QuestionnaireResponseItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Groups and questions.
    A group or question item from the original questionnaire for which answers
    are provided.
    """

    __resource_type__ = "QuestionnaireResponseItem"

    answer: typing.List[fhirtypes.QuestionnaireResponseItemAnswerType] | None = Field(  # type: ignore
        None,
        alias="answer",
        title="The response(s) to the question",
        description="The respondent's answer(s) to the question.",
        json_schema_extra={
            "element_property": True,
        },
    )

    definition: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="definition",
        title="ElementDefinition - details for the item",
        description=(
            "A reference to an [ElementDefinition](elementdefinition.html) that "
            "provides the details for the item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
    )

    item: typing.List[fhirtypes.QuestionnaireResponseItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Nested questionnaire response items",
        description="Questions or sub-groups nested beneath a question or group.",
        json_schema_extra={
            "element_property": True,
        },
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Pointer to specific item from Questionnaire",
        description=(
            "The item from the Questionnaire that corresponds to this item in the "
            "QuestionnaireResponse resource."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="The subject this group's answers are about",
        description=(
            "More specific subject this section's answers are about, details the "
            "subject given in QuestionnaireResponse."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Name for group or question text",
        description=(
            "Text that is displayed above the contents of the group or as the text "
            "of the question being answered."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``QuestionnaireResponseItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "definition",
            "text",
            "subject",
            "answer",
            "item",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("linkId", "linkId__ext")]
        return required_fields


class QuestionnaireResponseItemAnswer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The response(s) to the question.
    The respondent's answer(s) to the question.
    """

    __resource_type__ = "QuestionnaireResponseItemAnswer"

    item: typing.List[fhirtypes.QuestionnaireResponseItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Nested groups and questions",
        description="Nested groups and/or questions found within this particular answer.",
        json_schema_extra={
            "element_property": True,
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="valueCoding",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="valueDate",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="valueDateTime",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="valueDecimal",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="valueInteger",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="valueReference",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="valueTime",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="valueUri",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``QuestionnaireResponseItemAnswer`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "valueBoolean",
            "valueDecimal",
            "valueInteger",
            "valueDate",
            "valueDateTime",
            "valueTime",
            "valueString",
            "valueUri",
            "valueAttachment",
            "valueCoding",
            "valueQuantity",
            "valueReference",
            "item",
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
            ]
        }
        return one_of_many_fields
