# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DataRequirement
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
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

    limit: fhirtypes.PositiveInt = Field(
        None, alias="limit", title="Type `PositiveInt`", description="Number of results"
    )
    limit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_limit", title="Extension field for ``limit``."
    )

    mustSupport: ListType[fhirtypes.String] = Field(
        None,
        alias="mustSupport",
        title="List of `String` items",
        description=(
            "Indicates specific structure elements that are referenced by the "
            "knowledge module"
        ),
    )
    mustSupport__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_mustSupport", title="Extension field for ``mustSupport``.")

    profile: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="profile",
        title="List of `Canonical` items referencing `StructureDefinition`",
        description="The profile of the required data",
    )
    profile__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    sort: ListType[fhirtypes.DataRequirementSortType] = Field(
        None,
        alias="sort",
        title="List of `DataRequirementSort` items (represented as `dict` in JSON)",
        description="Order of the results",
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type `Reference` referencing `Group` (represented as `dict` in JSON)",
        description=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        one_of_many="subject",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        one_of_many_fields = {"subject": ["subjectCodeableConcept", "subjectReference"]}
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


class DataRequirementCodeFilter(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What codes are expected.
    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data. Each code
    filter defines an additional constraint on the data, i.e. code filters are
    AND'ed, not OR'ed.
    """

    resource_type = Field("DataRequirementCodeFilter", const=True)

    code: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="What code is expected",
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String`",
        description="A code-valued attribute to filter on",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    searchParam: fhirtypes.String = Field(
        None,
        alias="searchParam",
        title="Type `String`",
        description="A coded (token) parameter to search on",
    )
    searchParam__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_searchParam", title="Extension field for ``searchParam``."
    )

    valueSet: fhirtypes.Canonical = Field(
        None,
        alias="valueSet",
        title="Type `Canonical` referencing `ValueSet`",
        description="Valueset for the filter",
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )


class DataRequirementDateFilter(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What dates/date ranges are expected.
    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements. Each date filter specifies an
    additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
    """

    resource_type = Field("DataRequirementDateFilter", const=True)

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String`",
        description="A date-valued attribute to filter on",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    searchParam: fhirtypes.String = Field(
        None,
        alias="searchParam",
        title="Type `String`",
        description="A date valued parameter to search on",
    )
    searchParam__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_searchParam", title="Extension field for ``searchParam``."
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


class DataRequirementSort(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Order of the results.
    Specifies the order of the results to be returned.
    """

    resource_type = Field("DataRequirementSort", const=True)

    direction: fhirtypes.Code = Field(
        ...,
        alias="direction",
        title="Type `Code`",
        description="ascending | descending",
    )
    direction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_direction", title="Extension field for ``direction``."
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Type `String`",
        description="The name of the attribute to perform the sort",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )
