# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Period
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from pydantic import Field

from . import fhirtypes
from .element import Element


class Period(Element):
    """Time range defined by start and end date/time.

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
