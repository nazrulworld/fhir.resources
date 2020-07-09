# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class QuestionnaireResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A structured set of questions and their answers.
    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the questionnaire being responded to.
    """

    resource_type = Field("QuestionnaireResponse", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Person who received and recorded the answers",
        description=(
            "Person who received the answers to the questions in the "
            "QuestionnaireResponse and recorded them in the system."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Practitioner",
            "PractitionerRole",
            "Patient",
            "RelatedPerson",
            "Organization",
        ],
    )

    authored: fhirtypes.DateTime = Field(
        None,
        alias="authored",
        title="Date the answers were gathered",
        description="The date and/or time that this set of answers were last changed.",
        # if property is element of this resource.
        element_property=True,
    )
    authored__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authored", title="Extension field for ``authored``."
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Request fulfilled by this QuestionnaireResponse",
        description=(
            "The order, proposal or plan that is fulfilled in whole or in part by "
            "this QuestionnaireResponse.  For example, a ServiceRequest seeking an "
            "intake assessment or a decision support recommendation to assess for "
            "post-partum depression."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan", "ServiceRequest"],
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter created as part of",
        description=(
            "The Encounter during which this questionnaire response was created or "
            "to which the creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique id for this set of answers",
        description=(
            "A business identifier assigned to a particular completed (or partially"
            " completed) questionnaire."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    item: ListType[fhirtypes.QuestionnaireResponseItemType] = Field(
        None,
        alias="item",
        title="Groups and questions",
        description=(
            "A group or question item from the original questionnaire for which "
            "answers are provided."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of this action",
        description=(
            "A procedure or observation that this questionnaire was performed as "
            "part of the execution of.  For example, the surgery a checklist was "
            "executed as part of."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation", "Procedure"],
    )

    questionnaire: fhirtypes.Canonical = Field(
        None,
        alias="questionnaire",
        title="Form being answered",
        description=(
            "The Questionnaire that defines and organizes the questions for which "
            "answers are being provided."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Questionnaire"],
    )
    questionnaire__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_questionnaire", title="Extension field for ``questionnaire``."
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="The person who answered the questions",
        description="The person who answered the questions about the subject.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
        ],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="in-progress | completed | amended | entered-in-error | stopped",
        description=(
            "The position of the questionnaire response within its overall "
            "lifecycle."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "in-progress",
            "completed",
            "amended",
            "entered-in-error",
            "stopped",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="The subject of the questions",
        description=(
            "The subject of the questionnaire response.  This could be a patient, "
            "organization, practitioner, device, etc.  This is who/what the answers"
            " apply to, but is not necessarily the source of information."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )


class QuestionnaireResponseItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Groups and questions.
    A group or question item from the original questionnaire for which answers
    are provided.
    """

    resource_type = Field("QuestionnaireResponseItem", const=True)

    answer: ListType[fhirtypes.QuestionnaireResponseItemAnswerType] = Field(
        None,
        alias="answer",
        title="The response(s) to the question",
        description="The respondent's answer(s) to the question.",
        # if property is element of this resource.
        element_property=True,
    )

    definition: fhirtypes.Uri = Field(
        None,
        alias="definition",
        title="ElementDefinition - details for the item",
        description=(
            "A reference to an [ElementDefinition](elementdefinition.html) that "
            "provides the details for the item."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    item: ListType[fhirtypes.QuestionnaireResponseItemType] = Field(
        None,
        alias="item",
        title="Nested questionnaire response items",
        description="Questions or sub-groups nested beneath a question or group.",
        # if property is element of this resource.
        element_property=True,
    )

    linkId: fhirtypes.String = Field(
        ...,
        alias="linkId",
        title="Pointer to specific item from Questionnaire",
        description=(
            "The item from the Questionnaire that corresponds to this item in the "
            "QuestionnaireResponse resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Name for group or question text",
        description=(
            "Text that is displayed above the contents of the group or as the text "
            "of the question being answered."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )


class QuestionnaireResponseItemAnswer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The response(s) to the question.
    The respondent's answer(s) to the question.
    """

    resource_type = Field("QuestionnaireResponseItemAnswer", const=True)

    item: ListType[fhirtypes.QuestionnaireResponseItemType] = Field(
        None,
        alias="item",
        title="Nested groups and questions",
        description="Nested groups and/or questions found within this particular answer.",
        # if property is element of this resource.
        element_property=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Single-valued answer to the question",
        description=(
            "The answer (or one of the answers) provided by the respondent to the "
            "question."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
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
