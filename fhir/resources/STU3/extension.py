# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Extension
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator

from . import element, fhirtypes


class Extension(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Optional Extensions Element.
    Optional Extension Element - found in all resources.
    """

    resource_type = Field("Extension", const=True)

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="identifies the meaning of the extension",
        description=(
            "Source of the definition for the extension code - a logical name or a "
            "URL."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueAge: fhirtypes.AgeType = Field(
        None,
        alias="valueAge",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="valueAnnotation",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
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
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="valueContactPoint",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueCount: fhirtypes.CountType = Field(
        None,
        alias="valueCount",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
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
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDistance: fhirtypes.DistanceType = Field(
        None,
        alias="valueDistance",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="valueHumanName",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="valueIdentifier",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueInstant: fhirtypes.Instant = Field(
        None,
        alias="valueInstant",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="valueMarkdown",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueMeta: fhirtypes.MetaType = Field(
        None,
        alias="valueMeta",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueOid: fhirtypes.Oid = Field(
        None,
        alias="valueOid",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="valuePositiveInt",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
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
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="valueSignature",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueTiming: fhirtypes.TimingType = Field(
        None,
        alias="valueTiming",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="valueUnsignedInt",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Extension`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "url",
            "valueBase64Binary",
            "valueBoolean",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInstant",
            "valueInteger",
            "valueMarkdown",
            "valueOid",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueAddress",
            "valueAge",
            "valueAnnotation",
            "valueAttachment",
            "valueCodeableConcept",
            "valueCoding",
            "valueContactPoint",
            "valueCount",
            "valueDistance",
            "valueDuration",
            "valueHumanName",
            "valueIdentifier",
            "valueMoney",
            "valuePeriod",
            "valueQuantity",
            "valueRange",
            "valueRatio",
            "valueReference",
            "valueSampledData",
            "valueSignature",
            "valueTiming",
            "valueMeta",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1136(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
                "valueAddress",
                "valueAge",
                "valueAnnotation",
                "valueAttachment",
                "valueBase64Binary",
                "valueBoolean",
                "valueCode",
                "valueCodeableConcept",
                "valueCoding",
                "valueContactPoint",
                "valueCount",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueDistance",
                "valueDuration",
                "valueHumanName",
                "valueId",
                "valueIdentifier",
                "valueInstant",
                "valueInteger",
                "valueMarkdown",
                "valueMeta",
                "valueMoney",
                "valueOid",
                "valuePeriod",
                "valuePositiveInt",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueReference",
                "valueSampledData",
                "valueSignature",
                "valueString",
                "valueTime",
                "valueTiming",
                "valueUnsignedInt",
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
