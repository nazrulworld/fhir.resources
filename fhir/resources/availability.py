# -*- coding: utf-8 -*-
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

    resource_type = Field("Availability", const=True)

    availableTime: typing.List[fhirtypes.AvailabilityAvailableTimeType] = Field(
        None,
        alias="availableTime",
        title="Times the {item} is available",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    notAvailableTime: typing.List[fhirtypes.AvailabilityNotAvailableTimeType] = Field(
        None,
        alias="notAvailableTime",
        title="Not available during this time due to provided reason",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("AvailabilityAvailableTime", const=True)

    allDay: bool = Field(
        None,
        alias="allDay",
        title="Always available? i.e. 24 hour service",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allDay", title="Extension field for ``allDay``."
    )

    availableEndTime: fhirtypes.Time = Field(
        None,
        alias="availableEndTime",
        title="Closing time of day (ignored if allDay = true)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    availableEndTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availableEndTime",
        title="Extension field for ``availableEndTime``.",
    )

    availableStartTime: fhirtypes.Time = Field(
        None,
        alias="availableStartTime",
        title="Opening time of day (ignored if allDay = true)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    availableStartTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availableStartTime",
        title="Extension field for ``availableStartTime``.",
    )

    daysOfWeek: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="daysOfWeek",
        title="mon | tue | wed | thu | fri | sat | sun",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
    )
    daysOfWeek__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_daysOfWeek", title="Extension field for ``daysOfWeek``.")

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

    resource_type = Field("AvailabilityNotAvailableTime", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Reason presented to the user explaining why time not available",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    during: fhirtypes.PeriodType = Field(
        None,
        alias="during",
        title="Service not available during this period",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AvailabilityNotAvailableTime`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "description", "during"]
