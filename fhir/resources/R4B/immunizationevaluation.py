# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import domainresource, fhirtypes


class ImmunizationEvaluation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Immunization evaluation information.
    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """

    resource_type = Field("ImmunizationEvaluation", const=True)

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title="Who is responsible for publishing the recommendations",
        description="Indicates the authority who published the protocol (e.g. ACIP).",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date evaluation was performed",
        description=(
            "The date the evaluation of the vaccine administration event was "
            "performed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Evaluation notes",
        description="Additional information about the evaluation.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    doseNumberPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="doseNumberPositiveInt",
        title="Dose number within series",
        description="Nominal position in a series.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e doseNumber[x]
        one_of_many="doseNumber",
        one_of_many_required=False,
    )
    doseNumberPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_doseNumberPositiveInt",
        title="Extension field for ``doseNumberPositiveInt``.",
    )

    doseNumberString: fhirtypes.String = Field(
        None,
        alias="doseNumberString",
        title="Dose number within series",
        description="Nominal position in a series.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e doseNumber[x]
        one_of_many="doseNumber",
        one_of_many_required=False,
    )
    doseNumberString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_doseNumberString",
        title="Extension field for ``doseNumberString``.",
    )

    doseStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="doseStatus",
        title="Status of the dose relative to published recommendations",
        description=(
            "Indicates if the dose is valid or not valid with respect to the "
            "published recommendations."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    doseStatusReason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="doseStatusReason",
        title="Reason for the dose status",
        description=(
            "Provides an explanation as to why the vaccine administration event is "
            "valid or not relative to the published recommendations."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="A unique identifier assigned to this immunization evaluation record.",
        # if property is element of this resource.
        element_property=True,
    )

    immunizationEvent: fhirtypes.ReferenceType = Field(
        ...,
        alias="immunizationEvent",
        title="Immunization being evaluated",
        description="The vaccine administration event being evaluated.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Immunization"],
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who this evaluation is for",
        description="The individual for whom the evaluation is being done.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Name of vaccine series",
        description=(
            "One possible path to achieve presumed immunity against a disease - "
            "within the context of an authority."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    series__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_series", title="Extension field for ``series``."
    )

    seriesDosesPositiveInt: fhirtypes.PositiveInt = Field(
        None,
        alias="seriesDosesPositiveInt",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e seriesDoses[x]
        one_of_many="seriesDoses",
        one_of_many_required=False,
    )
    seriesDosesPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_seriesDosesPositiveInt",
        title="Extension field for ``seriesDosesPositiveInt``.",
    )

    seriesDosesString: fhirtypes.String = Field(
        None,
        alias="seriesDosesString",
        title="Recommended number of doses for immunity",
        description="The recommended number of doses to achieve immunity.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e seriesDoses[x]
        one_of_many="seriesDoses",
        one_of_many_required=False,
    )
    seriesDosesString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_seriesDosesString",
        title="Extension field for ``seriesDosesString``.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="completed | entered-in-error",
        description=(
            "Indicates the current status of the evaluation of the vaccination "
            "administration event."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["completed", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    targetDisease: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="targetDisease",
        title="Evaluation target disease",
        description="The vaccine preventable disease the dose is being evaluated against.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImmunizationEvaluation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "status",
            "patient",
            "date",
            "authority",
            "targetDisease",
            "immunizationEvent",
            "doseStatus",
            "doseStatusReason",
            "description",
            "series",
            "doseNumberPositiveInt",
            "doseNumberString",
            "seriesDosesPositiveInt",
            "seriesDosesString",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2515(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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
    def validate_one_of_many_2515(
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
            "doseNumber": ["doseNumberPositiveInt", "doseNumberString"],
            "seriesDoses": ["seriesDosesPositiveInt", "seriesDosesString"],
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
