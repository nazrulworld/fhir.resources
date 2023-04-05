# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Slot
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import domainresource, fhirtypes


class Slot(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A slot of time on a schedule that may be available for booking appointments.
    """

    resource_type = Field("Slot", const=True)

    appointmentType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="appointmentType",
        title=(
            "The style of appointment or patient that may be booked in the slot "
            "(not service type)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title=(
            "Comments on the slot to describe any extended information. Such as "
            "custom constraints on the slot"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="Date/Time that the slot is to conclude",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Ids for this item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    overbooked: bool = Field(
        None,
        alias="overbooked",
        title=(
            "This slot has already been overbooked, appointments are unlikely to be"
            " accepted for this time"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    overbooked__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_overbooked", title="Extension field for ``overbooked``."
    )

    schedule: fhirtypes.ReferenceType = Field(
        ...,
        alias="schedule",
        title=(
            "The schedule resource that this slot defines an interval of status "
            "information"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Schedule"],
    )

    serviceCategory: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceCategory",
        title=(
            "A broad categorization of the service that is to be performed during "
            "this appointment"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    serviceType: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="serviceType",
        title=(
            "The type of appointments that can be booked into this slot (ideally "
            "this would be an identifiable service - which is at a location, rather"
            " than the location itself). If provided then this overrides the value "
            "provided on the Schedule resource"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["HealthcareService"],
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title=(
            "The specialty of a practitioner that would be required to perform the "
            "service requested in this appointment"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    start: fhirtypes.Instant = Field(
        None,
        alias="start",
        title="Date/Time that the slot is to begin",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="busy | free | busy-unavailable | busy-tentative | entered-in-error",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "busy",
            "free",
            "busy-unavailable",
            "busy-tentative",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Slot`` according specification,
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
            "serviceCategory",
            "serviceType",
            "specialty",
            "appointmentType",
            "schedule",
            "status",
            "start",
            "end",
            "overbooked",
            "comment",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_617(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("end", "end__ext"),
            ("start", "start__ext"),
            ("status", "status__ext"),
        ]
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
