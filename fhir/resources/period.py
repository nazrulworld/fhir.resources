# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Period
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import element, fhirtypes


class Period(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Time range defined by start and end date/time.
    A time period defined by a start and end date and optionally time.
    """

    resource_type = Field("Period", const=True)

    end: fhirtypes.DateTime = Field(
        None,
        alias="end",
        title="End time with inclusive boundary, if not ongoing",
        description=(
            "The end of the period. If the end of the period is missing, it means "
            "no end was known or planned at the time the instance was created. The "
            "start may be in the past, and the end date in the future, which means "
            "that period is expected/planned to end at that time."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    start: fhirtypes.DateTime = Field(
        None,
        alias="start",
        title="Starting time with inclusive boundary",
        description="The start of the period. The boundary is inclusive.",
        # if property is element of this resource.
        element_property=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Period`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "start", "end"]
