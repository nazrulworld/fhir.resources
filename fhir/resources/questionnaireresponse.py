from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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
        title="The individual or device that received and recorded the answers",
        description=(
            "The individual or device that received the answers to the questions in"
            " the QuestionnaireResponse and recorded them in the system."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Device",
                "Practitioner",
                "PractitionerRole",
                "Patient",
                "RelatedPerson",
                "Organization",
            ],
        },
    )

    authored: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="authored",
        title="Date the answers were gathered",
        description=(
            "The date and/or time that this questionnaire response was last "
            "modified by the user - e.g. changing answers or revising status."
        ),
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
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this questionnaire response.  For example, a ServiceRequest seeking an"
            " intake assessment or a decision support recommendation to assess for "
            "post-partum depression."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CarePlan", "ServiceRequest"],
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter the questionnaire response is part of",
        description=(
            "The Encounter during which this questionnaire response was created or "
            "to which the creation of this record is tightly associated."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier for this set of answers",
        description=(
            "Business identifiers assigned to this questionnaire response by the "
            "performer and/or other systems.  These identifiers remain constant as "
            "the resource is updated and propagates from server to server."
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

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Part of referenced event",
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

    questionnaire: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="questionnaire",
        title="Canonical URL of Questionnaire being answered",
        description=(
            "The Questionnaire that defines and organizes the questions for which "
            "answers are being provided."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Questionnaire"],
        },
    )
    questionnaire__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_questionnaire", title="Extension field for ``questionnaire``."
    )

    source: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="source",
        title="The individual or device that answered the questions",
        description=(
            "The individual or device that answered the questions about the " "subject."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Device",
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="in-progress | completed | amended | entered-in-error | stopped",
        description="The current state of the questionnaire response.",
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
            "partOf",
            "questionnaire",
            "status",
            "subject",
            "encounter",
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
        required_fields = [
            ("questionnaire", "questionnaire__ext"),
            ("status", "status__ext"),
        ]
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
        title="Child items of group item",
        description="Sub-questions, sub-groups or display items nested beneath a group.",
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
        title="Child items of question",
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
            "one_of_many_required": True,
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
