from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Slot
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class Slot(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A slot of time on a schedule that may be available for booking appointments.
    """

    __resource_type__ = "Slot"

    appointmentType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="appointmentType",
        title=(
            "The style of appointment or patient that may be booked in the slot "
            "(not service type)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title=(
            "Comments on the slot to describe any extended information. Such as "
            "custom constraints on the slot"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    end: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="end",
        title="Date/Time that the slot is to conclude",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_end", title="Extension field for ``end``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Ids for this item",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    overbooked: bool | None = Field(  # type: ignore
        None,
        alias="overbooked",
        title=(
            "This slot has already been overbooked, appointments are unlikely to be"
            " accepted for this time"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    overbooked__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_overbooked", title="Extension field for ``overbooked``."
    )

    schedule: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="schedule",
        title=(
            "The schedule resource that this slot defines an interval of status "
            "information"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Schedule"],
        },
    )

    serviceCategory: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="serviceCategory",
        title=(
            "A broad categorization of the service that is to be performed during "
            "this appointment"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    serviceType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="serviceType",
        title=(
            "The type of appointments that can be booked into this slot (ideally "
            "this would be an identifiable service - which is at a location, rather"
            " than the location itself). If provided then this overrides the value "
            "provided on the availability resource"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="specialty",
        title=(
            "The specialty of a practitioner that would be required to perform the "
            "service requested in this appointment"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    start: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="start",
        title="Date/Time that the slot is to begin",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_start", title="Extension field for ``start``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="busy | free | busy-unavailable | busy-tentative | entered-in-error",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "busy",
                "free",
                "busy-unavailable",
                "busy-tentative",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
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
        return required_fields
