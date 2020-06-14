# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Period
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Period(element.Element):
    """ Time range defined by start and end date/time.
    A time period defined by a start and end date and optionally time.
    """

    resource_type = Field("Period", const=True)

    end: fhirtypes.DateTime = Field(
        None,
        alias="end",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="End time with inclusive boundary, if not ongoing",
    )

    start: fhirtypes.DateTime = Field(
        None,
        alias="start",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Starting time with inclusive boundary",
    )
