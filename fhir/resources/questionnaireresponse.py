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
        title=(
            "Type `Reference` referencing `Device, Practitioner, PractitionerRole, "
            "Patient, RelatedPerson, Organization` (represented as `dict` in JSON)"
        ),
        description="Person who received and recorded the answers",
    )

    authored: fhirtypes.DateTime = Field(
        None,
        alias="authored",
        title="Type `DateTime`",
        description="Date the answers were gathered",
    )
    authored__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authored", title="Extension field for ``authored``."
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `CarePlan, ServiceRequest` "
            "(represented as `dict` in JSON)"
        ),
        description="Request fulfilled by this QuestionnaireResponse",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Encounter created as part of",
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
        title=(
            "List of `QuestionnaireResponseItem` items (represented as `dict` in "
            "JSON)"
        ),
        description="Groups and questions",
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title=(
            "List of `Reference` items referencing `Observation, Procedure` "
            "(represented as `dict` in JSON)"
        ),
        description="Part of this action",
    )

    questionnaire: fhirtypes.Canonical = Field(
        None,
        alias="questionnaire",
        title="Type `Canonical` referencing `Questionnaire`",
        description="Form being answered",
    )
    questionnaire__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_questionnaire", title="Extension field for ``questionnaire``."
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, PractitionerRole,"
            " RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="The person who answered the questions",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="in-progress | completed | amended | entered-in-error | stopped",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="The subject of the questions",
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
        title=(
            "List of `QuestionnaireResponseItemAnswer` items (represented as `dict`"
            " in JSON)"
        ),
        description="The response(s) to the question",
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

    item: ListType[fhirtypes.QuestionnaireResponseItemType] = Field(
        None,
        alias="item",
        title=(
            "List of `QuestionnaireResponseItem` items (represented as `dict` in "
            "JSON)"
        ),
        description="Nested questionnaire response items",
    )

    linkId: fhirtypes.String = Field(
        ...,
        alias="linkId",
        title="Type `String`",
        description="Pointer to specific item from Questionnaire",
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String`",
        description="Name for group or question text",
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
        title=(
            "List of `QuestionnaireResponseItem` items (represented as `dict` in "
            "JSON)"
        ),
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
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
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
        title="Type `Date`",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime`",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal`",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer`",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
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
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String`",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time`",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri`",
        description="Single-valued answer to the question",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
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
