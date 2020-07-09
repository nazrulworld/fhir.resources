# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Slot
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class Slot(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A slot of time on a schedule that may be available for booking appointments.
    """

    resource_type = Field("Slot", const=True)

    appointmentType: fhirtypes.CodeableConceptType = Field(
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
        ...,
        alias="end",
        title="Date/Time that the slot is to conclude",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
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

    serviceCategory: ListType[fhirtypes.CodeableConceptType] = Field(
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

    serviceType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceType",
        title=(
            "The type of appointments that can be booked into this slot (ideally "
            "this would be an identifiable service - which is at a location, rather"
            " than the location itself). If provided then this overrides the value "
            "provided on the availability resource"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
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
        ...,
        alias="start",
        title="Date/Time that the slot is to begin",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="busy | free | busy-unavailable | busy-tentative | entered-in-error",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
