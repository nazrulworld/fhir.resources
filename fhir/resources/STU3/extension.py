from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Extension
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class Extension(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Optional Extensions Element.
    Optional Extension Element - found in all resources.
    """

    __resource_type__ = "Extension"

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="identifies the meaning of the extension",
        description=(
            "Source of the definition for the extension code - a logical name or a "
            "URL."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )

    valueAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="valueAddress",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueAge: fhirtypes.AgeType | None = Field(  # type: ignore
        None,
        alias="valueAge",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueAnnotation: fhirtypes.AnnotationType | None = Field(  # type: ignore
        None,
        alias="valueAnnotation",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueBase64Binary: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="valueBase64Binary",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
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
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="valueCode",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="valueCoding",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueContactPoint: fhirtypes.ContactPointType | None = Field(  # type: ignore
        None,
        alias="valueContactPoint",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCount: fhirtypes.CountType | None = Field(  # type: ignore
        None,
        alias="valueCount",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
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
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="valueDateTime",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="valueDecimal",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDistance: fhirtypes.DistanceType | None = Field(  # type: ignore
        None,
        alias="valueDistance",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="valueDuration",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueHumanName: fhirtypes.HumanNameType | None = Field(  # type: ignore
        None,
        alias="valueHumanName",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="valueId",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="valueIdentifier",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueInstant: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="valueInstant",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="valueInteger",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueMarkdown: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="valueMarkdown",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueMeta: fhirtypes.MetaType | None = Field(  # type: ignore
        None,
        alias="valueMeta",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueMoney: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="valueMoney",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueOid: fhirtypes.OidType | None = Field(  # type: ignore
        None,
        alias="valueOid",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valuePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="valuePeriod",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valuePositiveInt: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="valuePositiveInt",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        None,
        alias="valueRatio",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
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
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueSampledData: fhirtypes.SampledDataType | None = Field(  # type: ignore
        None,
        alias="valueSampledData",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueSignature: fhirtypes.SignatureType | None = Field(  # type: ignore
        None,
        alias="valueSignature",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="valueTime",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="valueTiming",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueUnsignedInt: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="valueUnsignedInt",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="valueUri",
        title="Value of extension",
        description=(
            "Value of extension - may be a resource or one of a constrained set of "
            "the data types (see Extensibility in the spec for list)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
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
        return one_of_many_fields
