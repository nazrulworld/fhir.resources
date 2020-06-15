# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Parameters
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, fhirtypes, resource


class Parameters(resource.Resource):
    """ Operation Request or Response.
    This special resource type is used to represent an operation request and
    response (operations.html). It has no other use, and there is no RESTful
    endpoint associated with it.
    """

    resource_type = Field("Parameters", const=True)

    parameter: ListType[fhirtypes.ParametersParameterType] = Field(
        None,
        alias="parameter",
        title="List of `ParametersParameter` items (represented as `dict` in JSON)",
        description="Operation Parameter",
    )


class ParametersParameter(backboneelement.BackboneElement):
    """ Operation Parameter.
    A parameter passed to or received from the operation.
    """

    resource_type = Field("ParametersParameter", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name from the definition",
    )

    part: ListType[fhirtypes.ParametersParameterType] = Field(
        None,
        alias="part",
        title="List of `ParametersParameter` items (represented as `dict` in JSON)",
        description="Named part of a multi-part parameter",
    )

    resource: fhirtypes.ResourceType = Field(
        None,
        alias="resource",
        title="Type `Resource` (represented as `dict` in JSON)",
        description="If parameter is a whole resource",
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueAge: fhirtypes.AgeType = Field(
        None,
        alias="valueAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="valueAnnotation",
        title="Type `Annotation` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="valueContactPoint",
        title="Type `ContactPoint` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCount: fhirtypes.CountType = Field(
        None,
        alias="valueCount",
        title="Type `Count` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDistance: fhirtypes.DistanceType = Field(
        None,
        alias="valueDistance",
        title="Type `Distance` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="valueHumanName",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueId: fhirtypes.Id = Field(
        None,
        alias="valueId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="valueIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueInstant: fhirtypes.Instant = Field(
        None,
        alias="valueInstant",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="valueMarkdown",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueMeta: fhirtypes.MetaType = Field(
        None,
        alias="valueMeta",
        title="Type `Meta` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueOid: fhirtypes.Oid = Field(
        None,
        alias="valueOid",
        title="Type `Oid` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valuePositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="valuePositiveInt",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="Type `SampledData` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="valueSignature",
        title="Type `Signature` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueTime: fhirtypes.Time = Field(
        None,
        alias="valueTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueTiming: fhirtypes.TimingType = Field(
        None,
        alias="valueTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="valueUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="If parameter is a data type",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="If parameter is a data type",
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
