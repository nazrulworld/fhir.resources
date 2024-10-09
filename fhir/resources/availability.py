from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Availability
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, element, fhirtypes


class Availability(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Availability data for an {item}.
    """

    __resource_type__ = "Availability"

    availableTime: typing.List[fhirtypes.AvailabilityAvailableTimeType] | None = Field(  # type: ignore
        None,
        alias="availableTime",
        title="Times the {item} is available",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    notAvailableTime: typing.List[fhirtypes.AvailabilityNotAvailableTimeType] | None = Field(  # type: ignore
        None,
        alias="notAvailableTime",
        title="Not available during this time due to provided reason",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Availability`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "availableTime", "notAvailableTime"]


class AvailabilityAvailableTime(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Times the {item} is available.
    """

    __resource_type__ = "AvailabilityAvailableTime"

    allDay: bool | None = Field(  # type: ignore
        None,
        alias="allDay",
        title="Always available? i.e. 24 hour service",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_allDay", title="Extension field for ``allDay``."
    )

    availableEndTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="availableEndTime",
        title="Closing time of day (ignored if allDay = true)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    availableEndTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_availableEndTime",
        title="Extension field for ``availableEndTime``.",
    )

    availableStartTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="availableStartTime",
        title="Opening time of day (ignored if allDay = true)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    availableStartTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_availableStartTime",
        title="Extension field for ``availableStartTime``.",
    )

    daysOfWeek: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="daysOfWeek",
        title="mon | tue | wed | thu | fri | sat | sun",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
        },
    )
    daysOfWeek__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_daysOfWeek", title="Extension field for ``daysOfWeek``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AvailabilityAvailableTime`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "daysOfWeek",
            "allDay",
            "availableStartTime",
            "availableEndTime",
        ]


class AvailabilityNotAvailableTime(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Not available during this time due to provided reason.
    """

    __resource_type__ = "AvailabilityNotAvailableTime"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Reason presented to the user explaining why time not available",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    during: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="during",
        title="Service not available during this period",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AvailabilityNotAvailableTime`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "description", "during"]
