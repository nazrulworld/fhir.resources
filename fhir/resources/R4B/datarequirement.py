from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DataRequirement
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class DataRequirement(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes a required data item.
    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """

    __resource_type__ = "DataRequirement"

    codeFilter: typing.List[fhirtypes.DataRequirementCodeFilterType] | None = Field(  # type: ignore
        None,
        alias="codeFilter",
        title="What codes are expected",
        description=(
            "Code filters specify additional constraints on the data, specifying "
            "the value set of interest for a particular element of the data. Each "
            "code filter defines an additional constraint on the data, i.e. code "
            "filters are AND'ed, not OR'ed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dateFilter: typing.List[fhirtypes.DataRequirementDateFilterType] | None = Field(  # type: ignore
        None,
        alias="dateFilter",
        title="What dates/date ranges are expected",
        description=(
            "Date filters specify additional constraints on the data in terms of "
            "the applicable date range for specific elements. Each date filter "
            "specifies an additional constraint on the data, i.e. date filters are "
            "AND'ed, not OR'ed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    limit: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="limit",
        title="Number of results",
        description=(
            "Specifies a maximum number of results that are required (uses the "
            "_count search parameter)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    limit__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_limit", title="Extension field for ``limit``."
    )

    mustSupport: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    mustSupport__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_mustSupport", title="Extension field for ``mustSupport``."
    )

    profile: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="profile",
        title="The profile of the required data",
        description=(
            "The profile of the required data, specified as the uri of the profile "
            "definition."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_profile", title="Extension field for ``profile``."
    )

    sort: typing.List[fhirtypes.DataRequirementSortType] | None = Field(  # type: ignore
        None,
        alias="sort",
        title="Order of the results",
        description="Specifies the order of the results to be returned.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
        },
    )

    subjectReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The type of the required data",
        description=(
            "The type of the required data, specified as the type name of a "
            "resource. For profiles, this value is set to the type of the base "
            "resource of the profile."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DataRequirement`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "type",
            "profile",
            "subjectCodeableConcept",
            "subjectReference",
            "mustSupport",
            "codeFilter",
            "dateFilter",
            "limit",
            "sort",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields

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
        one_of_many_fields = {"subject": ["subjectCodeableConcept", "subjectReference"]}
        return one_of_many_fields


class DataRequirementCodeFilter(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What codes are expected.
    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data. Each code
    filter defines an additional constraint on the data, i.e. code filters are
    AND'ed, not OR'ed.
    """

    __resource_type__ = "DataRequirementCodeFilter"

    code: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    path: fhirtypes.StringType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_path", title="Extension field for ``path``."
    )

    searchParam: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="searchParam",
        title="A coded (token) parameter to search on",
        description=(
            "A token parameter that refers to a search parameter defined on the "
            "specified type of the DataRequirement, and which searches on elements "
            "of type code, Coding, or CodeableConcept."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    searchParam__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_searchParam", title="Extension field for ``searchParam``."
    )

    valueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="valueSet",
        title="Valueset for the filter",
        description=(
            "The valueset for the code filter. The valueSet and code elements are "
            "additive. If valueSet is specified, the filter will return only those "
            "data items for which the value of the code-valued element specified in"
            " the path is a member of the specified valueset."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DataRequirementCodeFilter`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "path", "searchParam", "valueSet", "code"]


class DataRequirementDateFilter(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What dates/date ranges are expected.
    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements. Each date filter specifies an
    additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
    """

    __resource_type__ = "DataRequirementDateFilter"

    path: fhirtypes.StringType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_path", title="Extension field for ``path``."
    )

    searchParam: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="searchParam",
        title="A date valued parameter to search on",
        description=(
            "A date parameter that refers to a search parameter defined on the "
            "specified type of the DataRequirement, and which searches on elements "
            "of type date, dateTime, Period, Schedule, or Timing."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    searchParam__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_searchParam", title="Extension field for ``searchParam``."
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
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

    valueDuration: fhirtypes.DurationType | None = Field(  # type: ignore
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
        ``DataRequirementDateFilter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "path",
            "searchParam",
            "valueDateTime",
            "valuePeriod",
            "valueDuration",
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
            "value": ["valueDateTime", "valueDuration", "valuePeriod"]
        }
        return one_of_many_fields


class DataRequirementSort(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Order of the results.
    Specifies the order of the results to be returned.
    """

    __resource_type__ = "DataRequirementSort"

    direction: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="direction",
        title="ascending | descending",
        description="The direction of the sort, ascending or descending.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["ascending", "descending"],
        },
    )
    direction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_direction", title="Extension field for ``direction``."
    )

    path: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="path",
        title="The name of the attribute to perform the sort",
        description=(
            "The attribute of the sort. The specified path must be resolvable from "
            "the type of the required data. The path is allowed to contain "
            "qualifiers (.) to traverse sub-elements, as well as indexers ([x]) to "
            "traverse multiple-cardinality sub-elements. Note that the index must "
            "be an integer constant."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_path", title="Extension field for ``path``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DataRequirementSort`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "path", "direction"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("direction", "direction__ext"), ("path", "path__ext")]
        return required_fields
