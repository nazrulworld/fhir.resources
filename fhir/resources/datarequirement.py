# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DataRequirement
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import datatype, element, fhirtypes


class DataRequirement(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes a required data item.
    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """

    resource_type = Field("DataRequirement", const=True)

    codeFilter: typing.List[fhirtypes.DataRequirementCodeFilterType] = Field(
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

    dateFilter: typing.List[fhirtypes.DataRequirementDateFilterType] = Field(
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

    mustSupport: typing.List[typing.Optional[fhirtypes.String]] = Field(
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
            "resolvable on the type of the DataRequirement. The path SHALL consist "
            "only of identifiers, constant indexers, and .resolve() (see the "
            "[Simple FHIRPath Profile](fhirpath.html#simple) for full details)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    mustSupport__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_mustSupport", title="Extension field for ``mustSupport``.")

    profile: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
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
    profile__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_profile", title="Extension field for ``profile``.")

    sort: typing.List[fhirtypes.DataRequirementSortType] = Field(
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
        None,
        alias="type",
        title="The type of the required data",
        description=(
            "The type of the required data, specified as the type name of a "
            "resource. For profiles, this value is set to the type of the base "
            "resource of the profile."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    valueFilter: typing.List[fhirtypes.DataRequirementValueFilterType] = Field(
        None,
        alias="valueFilter",
        title="What values are expected",
        description=(
            "Value filters specify additional constraints on the data for elements "
            "other than code-valued or date-valued. Each value filter specifies an "
            "additional constraint on the data (i.e. valueFilters are AND'ed, not "
            "OR'ed)."
        ),
        # if property is element of this resource.
        element_property=True,
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
            "valueFilter",
            "limit",
            "sort",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1731(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1731(
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What codes are expected.
    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data. Each code
    filter defines an additional constraint on the data, i.e. code filters are
    AND'ed, not OR'ed.
    """

    resource_type = Field("DataRequirementCodeFilter", const=True)

    code: typing.List[fhirtypes.CodingType] = Field(
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
            " FHIRPath resolvable on the specified type of the DataRequirement, and"
            " SHALL consist only of identifiers, constant indexers, and .resolve()."
            " The path is allowed to contain qualifiers (.) to traverse sub-"
            "elements, as well as indexers ([x]) to traverse multiple-cardinality "
            "sub-elements (see the [Simple FHIRPath Profile](fhirpath.html#simple) "
            "for full details). Note that the index must be an integer constant. "
            "The path must resolve to an element of type code, Coding, or "
            "CodeableConcept."
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
        title="ValueSet for the filter",
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

    resource_type = Field("DataRequirementDateFilter", const=True)

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="A date-valued attribute to filter on",
        description=(
            "The date-valued attribute of the filter. The specified path SHALL be a"
            " FHIRPath resolvable on the specified type of the DataRequirement, and"
            " SHALL consist only of identifiers, constant indexers, and .resolve()."
            " The path is allowed to contain qualifiers (.) to traverse sub-"
            "elements, as well as indexers ([x]) to traverse multiple-cardinality "
            "sub-elements (see the [Simple FHIRPath Profile](fhirpath.html#simple) "
            "for full details). Note that the index must be an integer constant. "
            "The path must resolve to an element of type date, dateTime, Period, "
            "Schedule, or Timing."
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2725(
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Order of the results.
    Specifies the order of the results to be returned.
    """

    resource_type = Field("DataRequirementSort", const=True)

    direction: fhirtypes.Code = Field(
        None,
        alias="direction",
        title="ascending | descending",
        description="The direction of the sort, ascending or descending.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["ascending", "descending"],
    )
    direction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_direction", title="Extension field for ``direction``."
    )

    path: fhirtypes.String = Field(
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
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DataRequirementSort`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "path", "direction"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2155(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("direction", "direction__ext"), ("path", "path__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class DataRequirementValueFilter(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What values are expected.
    Value filters specify additional constraints on the data for elements other
    than code-valued or date-valued. Each value filter specifies an additional
    constraint on the data (i.e. valueFilters are AND'ed, not OR'ed).
    """

    resource_type = Field("DataRequirementValueFilter", const=True)

    comparator: fhirtypes.Code = Field(
        None,
        alias="comparator",
        title="eq | gt | lt | ge | le | sa | eb",
        description="The comparator to be used to determine whether the value is matching.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["eq", "gt", "lt", "ge", "le", "sa", "eb"],
    )
    comparator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comparator", title="Extension field for ``comparator``."
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="An attribute to filter on",
        description=(
            "The attribute of the filter. The specified path SHALL be a FHIRPath "
            "resolvable on the specified type of the DataRequirement, and SHALL "
            "consist only of identifiers, constant indexers, and .resolve(). The "
            "path is allowed to contain qualifiers (.) to traverse sub-elements, as"
            " well as indexers ([x]) to traverse multiple-cardinality sub-elements "
            "(see the [Simple FHIRPath Profile](fhirpath.html#simple) for full "
            "details). Note that the index must be an integer constant. The path "
            "must resolve to an element of a type that is comparable to the "
            "valueFilter.value[x] element for the filter."
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
        title="A parameter to search on",
        description=(
            "A search parameter defined on the specified type of the "
            "DataRequirement, and which searches on elements of a type compatible "
            "with the type of the valueFilter.value[x] for the filter."
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
        description="The value of the filter.",
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
        description="The value of the filter.",
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
        description="The value of the filter.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DataRequirementValueFilter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "path",
            "searchParam",
            "comparator",
            "valueDateTime",
            "valuePeriod",
            "valueDuration",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2852(
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
