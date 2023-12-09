# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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

    description: fhirtypes.Markdown = Field(
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

    doseNumber: fhirtypes.String = Field(
        None,
        alias="doseNumber",
        title="Dose number within series",
        description=(
            "Nominal position in a series as determined by the outcome of the "
            "evaluation process."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    doseNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_doseNumber", title="Extension field for ``doseNumber``."
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
        title="Reason why the doese is considered valid, invalid or some other status",
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

    seriesDoses: fhirtypes.String = Field(
        None,
        alias="seriesDoses",
        title="Recommended number of doses for immunity",
        description=(
            "The recommended number of doses to achieve immunity as determined by "
            "the outcome of the evaluation process."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    seriesDoses__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_seriesDoses", title="Extension field for ``seriesDoses``."
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
        title="The vaccine preventable disease schedule being evaluated",
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
            "doseNumber",
            "seriesDoses",
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
