# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DataRequirement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import element, fhirtypes


class DataRequirement(element.Element):
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
            "the value set of interest for a particular element of the data."
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
            "the applicable date range for specific elements."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    mustSupport: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="mustSupport",
        title=(
            "Indicates that specific structure elements are referenced by the "
            "knowledge module"
        ),
        description=(
            "Indicates that specific elements of the type are referenced by the "
            "knowledge module and must be supported by the consumer in order to "
            "obtain an effective evaluation. This does not mean that a value is "
            "required for this element, only that the consuming system must "
            "understand the element and be able to provide values for it if they "
            "are available. Note that the value for this element can be a path to "
            "allow references to nested elements. In that case, all the elements "
            "along the path must be supported."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    mustSupport__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_mustSupport", title="Extension field for ``mustSupport``.")

    profile: typing.List[fhirtypes.Uri] = Field(
        None,
        alias="profile",
        title="The profile of the required data",
        description=(
            "The profile of the required data, specified as the uri of the profile "
            "definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    profile__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_profile", title="Extension field for ``profile``.")

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
            "mustSupport",
            "codeFilter",
            "dateFilter",
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


class DataRequirementCodeFilter(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What codes are expected.
    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data.
    """

    resource_type = Field("DataRequirementCodeFilter", const=True)

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="The code-valued attribute of the filter",
        description=(
            "The code-valued attribute of the filter. The specified path must be "
            "resolvable from the type of the required data. The path is allowed to "
            "contain qualifiers (.) to traverse sub-elements, as well as indexers "
            "([x]) to traverse multiple-cardinality sub-elements. Note that the "
            "index must be an integer constant. The path must resolve to an element"
            " of type code, Coding, or CodeableConcept."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    valueCode: typing.List[fhirtypes.Code] = Field(
        None,
        alias="valueCode",
        title="What code is expected",
        description=(
            "The codes for the code filter. Only one of valueSet, valueCode, "
            "valueCoding, or valueCodeableConcept may be specified. If values are "
            "given, the filter will return only those data items for which the "
            "code-valued attribute specified by the path has a value that is one of"
            " the specified codes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    valueCode__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_valueCode", title="Extension field for ``valueCode``.")

    valueCodeableConcept: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="valueCodeableConcept",
        title="What CodeableConcept is expected",
        description=(
            "The CodeableConcepts for the code filter. Only one of valueSet, "
            "valueCode, valueConding, or valueCodeableConcept may be specified. If "
            "values are given, the filter will return only those data items for "
            "which the code-valued attribute specified by the path has a value that"
            " is one of the specified CodeableConcepts."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueCoding: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="valueCoding",
        title="What Coding is expected",
        description=(
            "The Codings for the code filter. Only one of valueSet, valueCode, "
            "valueConding, or valueCodeableConcept may be specified. If values are "
            "given, the filter will return only those data items for which the "
            "code-valued attribute specified by the path has a value that is one of"
            " the specified Codings."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueSetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueSetReference",
        title="Valueset for the filter",
        description=(
            "The valueset for the code filter. The valueSet and value elements are "
            "exclusive. If valueSet is specified, the filter will return only those"
            " data items for which the value of the code-valued element specified "
            "in the path is a member of the specified valueset."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e valueSet[x]
        one_of_many="valueSet",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )

    valueSetString: fhirtypes.String = Field(
        None,
        alias="valueSetString",
        title="Valueset for the filter",
        description=(
            "The valueset for the code filter. The valueSet and value elements are "
            "exclusive. If valueSet is specified, the filter will return only those"
            " data items for which the value of the code-valued element specified "
            "in the path is a member of the specified valueset."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e valueSet[x]
        one_of_many="valueSet",
        one_of_many_required=False,
    )
    valueSetString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSetString", title="Extension field for ``valueSetString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DataRequirementCodeFilter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "path",
            "valueSetString",
            "valueSetReference",
            "valueCode",
            "valueCoding",
            "valueCodeableConcept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2722(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("path", "path__ext")]
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
    def validate_one_of_many_2722(
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What dates/date ranges are expected.
    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements.
    """

    resource_type = Field("DataRequirementDateFilter", const=True)

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="The date-valued attribute of the filter",
        description=(
            "The date-valued attribute of the filter. The specified path must be "
            "resolvable from the type of the required data. The path is allowed to "
            "contain qualifiers (.) to traverse sub-elements, as well as indexers "
            "([x]) to traverse multiple-cardinality sub-elements. Note that the "
            "index must be an integer constant. The path must resolve to an element"
            " of type dateTime, Period, Schedule, or Timing."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
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
            "will return only those data items that fall within Duration from now."
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
            "will return only those data items that fall within Duration from now."
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
            "will return only those data items that fall within Duration from now."
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
            "valueDateTime",
            "valuePeriod",
            "valueDuration",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2725(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("path", "path__ext")]
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
