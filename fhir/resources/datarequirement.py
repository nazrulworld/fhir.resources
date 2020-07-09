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
        title="What codes are expected",
        description=(
            "Code filters specify additional constraints on the data, specifying "
            "the value set of interest for a particular element of the data. Each "
            "code filter defines an additional constraint on the data, i.e. code "
            "filters are AND'ed, not OR'ed."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    dateFilter: ListType[fhirtypes.DataRequirementDateFilterType] = Field(
        None,
        alias="dateFilter",
        title="What dates/date ranges are expected",
        description=(
            "Date filters specify additional constraints on the data in terms of "
            "the applicable date range for specific elements. Each date filter "
            "specifies an additional constraint on the data, i.e. date filters are "
            "AND'ed, not OR'ed."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    limit: fhirtypes.PositiveInt = Field(
        None,
        alias="limit",
        title="Number of results",
        description=(
            "Specifies a maximum number of results that are required (uses the "
            "_count search parameter)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    limit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_limit", title="Extension field for ``limit``."
    )

    mustSupport: ListType[fhirtypes.String] = Field(
        None,
        alias="mustSupport",
        title=(
            "Indicates specific structure elements that are referenced by the "
            "knowledge module"
        ),
        description=(
            "Indicates that specific elements of the type are referenced by the "
            "knowledge module and must be supported by the consumer in order to "
            "obtain an effective evaluation. This does not mean that a value is "
            "required for this element, only that the consuming system must "
            "understand the element and be able to provide values for it if they "
            "are available.   The value of mustSupport SHALL be a FHIRPath "
            "resolveable on the type of the DataRequirement. The path SHALL consist"
            " only of identifiers, constant indexers, and .resolve() (see the "
            "[Simple FHIRPath Profile](fhirpath.html#simple) for full details)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    mustSupport__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_mustSupport", title="Extension field for ``mustSupport``.")

    profile: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="profile",
        title="The profile of the required data",
        description=(
            "The profile of the required data, specified as the uri of the profile "
            "definition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    profile__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    sort: ListType[fhirtypes.DataRequirementSortType] = Field(
        None,
        alias="sort",
        title="Order of the results",
        description="Specifies the order of the results to be returned.",
        # if property is element of this resource.
        element_property=True,
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        description=(
            "The intended subjects of the data requirement. If this element is not "
            "provided, a Patient subject is assumed."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        description=(
            "The intended subjects of the data requirement. If this element is not "
            "provided, a Patient subject is assumed."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="The type of the required data",
        description=(
            "The type of the required data, specified as the type name of a "
            "resource. For profiles, this value is set to the type of the base "
            "resource of the profile."
        ),
        # if property is element of this resource.
        element_property=True,
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
        title="What code is expected",
        description=(
            "The codes for the code filter. If values are given, the filter will "
            "return only those data items for which the code-valued attribute "
            "specified by the path has a value that is one of the specified codes. "
            "If codes are specified in addition to a value set, the filter returns "
            "items matching a code in the value set or one of the specified codes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="A code-valued attribute to filter on",
        description=(
            "The code-valued attribute of the filter. The specified path SHALL be a"
            " FHIRPath resolveable on the specified type of the DataRequirement, "
            "and SHALL consist only of identifiers, constant indexers, and "
            ".resolve(). The path is allowed to contain qualifiers (.) to traverse "
            "sub-elements, as well as indexers ([x]) to traverse multiple-"
            "cardinality sub-elements (see the [Simple FHIRPath "
            "Profile](fhirpath.html#simple) for full details). Note that the index "
            "must be an integer constant. The path must resolve to an element of "
            "type code, Coding, or CodeableConcept."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    searchParam: fhirtypes.String = Field(
        None,
        alias="searchParam",
        title="A coded (token) parameter to search on",
        description=(
            "A token parameter that refers to a search parameter defined on the "
            "specified type of the DataRequirement, and which searches on elements "
            "of type code, Coding, or CodeableConcept."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    searchParam__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_searchParam", title="Extension field for ``searchParam``."
    )

    valueSet: fhirtypes.Canonical = Field(
        None,
        alias="valueSet",
        title="Valueset for the filter",
        description=(
            "The valueset for the code filter. The valueSet and code elements are "
            "additive. If valueSet is specified, the filter will return only those "
            "data items for which the value of the code-valued element specified in"
            " the path is a member of the specified valueset."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
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
        title="A date-valued attribute to filter on",
        description=(
            "The date-valued attribute of the filter. The specified path SHALL be a"
            " FHIRPath resolveable on the specified type of the DataRequirement, "
            "and SHALL consist only of identifiers, constant indexers, and "
            ".resolve(). The path is allowed to contain qualifiers (.) to traverse "
            "sub-elements, as well as indexers ([x]) to traverse multiple-"
            "cardinality sub-elements (see the [Simple FHIRPath "
            "Profile](fhirpath.html#simple) for full details). Note that the index "
            "must be an integer constant. The path must resolve to an element of "
            "type date, dateTime, Period, Schedule, or Timing."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    searchParam: fhirtypes.String = Field(
        None,
        alias="searchParam",
        title="A date valued parameter to search on",
        description=(
            "A date parameter that refers to a search parameter defined on the "
            "specified type of the DataRequirement, and which searches on elements "
            "of type date, dateTime, Period, Schedule, or Timing."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    searchParam__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_searchParam", title="Extension field for ``searchParam``."
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="The value of the filter, as a Period, DateTime, or Duration value",
        description=(
            "The value of the filter. If period is specified, the filter will "
            "return only those data items that fall within the bounds determined by"
            " the Period, inclusive of the period boundaries. If dateTime is "
            "specified, the filter will return only those data items that are equal"
            " to the specified dateTime. If a Duration is specified, the filter "
            "will return only those data items that fall within Duration before "
            "now."
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

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="The value of the filter, as a Period, DateTime, or Duration value",
        description=(
            "The value of the filter. If period is specified, the filter will "
            "return only those data items that fall within the bounds determined by"
            " the Period, inclusive of the period boundaries. If dateTime is "
            "specified, the filter will return only those data items that are equal"
            " to the specified dateTime. If a Duration is specified, the filter "
            "will return only those data items that fall within Duration before "
            "now."
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
        title="The value of the filter, as a Period, DateTime, or Duration value",
        description=(
            "The value of the filter. If period is specified, the filter will "
            "return only those data items that fall within the bounds determined by"
            " the Period, inclusive of the period boundaries. If dateTime is "
            "specified, the filter will return only those data items that are equal"
            " to the specified dateTime. If a Duration is specified, the filter "
            "will return only those data items that fall within Duration before "
            "now."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
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
        title="ascending | descending",
        description="The direction of the sort, ascending or descending.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["ascending", "descending"],
    )
    direction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_direction", title="Extension field for ``direction``."
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="The name of the attribute to perform the sort",
        description=(
            "The attribute of the sort. The specified path must be resolvable from "
            "the type of the required data. The path is allowed to contain "
            "qualifiers (.) to traverse sub-elements, as well as indexers ([x]) to "
            "traverse multiple-cardinality sub-elements. Note that the index must "
            "be an integer constant."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )
