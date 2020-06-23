# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DataRequirement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import element, fhirtypes


class DataRequirement(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes a required data item.
    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """

    resource_type = Field("DataRequirement", const=True)

    codeFilter: ListType[fhirtypes.DataRequirementCodeFilterType] = Field(
        None,
        alias="codeFilter",
        title=(
            "List of `DataRequirementCodeFilter` items (represented as `dict` in "
            "JSON)"
        ),
        description="What codes are expected",
    )

    dateFilter: ListType[fhirtypes.DataRequirementDateFilterType] = Field(
        None,
        alias="dateFilter",
        title=(
            "List of `DataRequirementDateFilter` items (represented as `dict` in "
            "JSON)"
        ),
        description="What dates/date ranges are expected",
    )

    mustSupport: ListType[fhirtypes.String] = Field(
        None,
        alias="mustSupport",
        title="List of `String` items",
        description=(
            "Indicates that specific structure elements are referenced by the "
            "knowledge module"
        ),
    )
    mustSupport__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_mustSupport", title="Extension field for ``mustSupport``.")

    profile: ListType[fhirtypes.Uri] = Field(
        None,
        alias="profile",
        title="List of `Uri` items",
        description="The profile of the required data",
    )
    profile__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="The type of the required data",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class DataRequirementCodeFilter(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What codes are expected.
    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data.
    """

    resource_type = Field("DataRequirementCodeFilter", const=True)

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Type `String`",
        description="The code-valued attribute of the filter",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    valueCode: ListType[fhirtypes.Code] = Field(
        None,
        alias="valueCode",
        title="List of `Code` items",
        description="What code is expected",
    )
    valueCode__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCodeableConcept: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="valueCodeableConcept",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="What CodeableConcept is expected",
    )

    valueCoding: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="valueCoding",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="What Coding is expected",
    )

    valueSetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueSetReference",
        title=(
            "Type `Reference` referencing `ValueSet` (represented as `dict` in " "JSON)"
        ),
        description="Valueset for the filter",
        one_of_many="valueSet",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueSetString: fhirtypes.String = Field(
        None,
        alias="valueSetString",
        title="Type `String`",
        description="Valueset for the filter",
        one_of_many="valueSet",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueSetString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSetString", title="Extension field for ``valueSetString``."
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
        one_of_many_fields = {"valueSet": ["valueSetReference", "valueSetString"]}
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


class DataRequirementDateFilter(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What dates/date ranges are expected.
    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements.
    """

    resource_type = Field("DataRequirementDateFilter", const=True)

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Type `String`",
        description="The date-valued attribute of the filter",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Type `DateTime`",
        description="The value of the filter, as a Period, DateTime, or Duration value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="The value of the filter, as a Period, DateTime, or Duration value",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The value of the filter, as a Period, DateTime, or Duration value",
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
            "value": ["valueDateTime", "valueDuration", "valuePeriod"]
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
