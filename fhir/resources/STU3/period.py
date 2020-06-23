# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Period
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Period(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Time range defined by start and end date/time.
    A time period defined by a start and end date and optionally time.
    """

    resource_type = Field("Period", const=True)

    end: fhirtypes.DateTime = Field(
        None,
        alias="end",
        title="Type `DateTime`",
        description="End time with inclusive boundary, if not ongoing",
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    start: fhirtypes.DateTime = Field(
        None,
        alias="start",
        title="Type `DateTime`",
        description="Starting time with inclusive boundary",
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )
