# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SampledData
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class SampledData(element.Element):
    """ A series of measurements taken by a device.
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    resource_type = Field("SampledData", const=True)

    data: fhirtypes.String = Field(
        ...,
        alias="data",
        title="Type `String` (represented as `dict` in JSON)",
        description='Decimal values with spaces, or "E" | "U" | "L"',
    )

    dimensions: fhirtypes.PositiveInt = Field(
        ...,
        alias="dimensions",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Number of sample points at each time point",
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Multiply data by this before adding to origin",
    )

    lowerLimit: fhirtypes.Decimal = Field(
        None,
        alias="lowerLimit",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Lower limit of detection",
    )

    origin: fhirtypes.QuantityType = Field(
        ...,
        alias="origin",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Zero value and units",
    )

    period: fhirtypes.Decimal = Field(
        ...,
        alias="period",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Number of milliseconds between samples",
    )

    upperLimit: fhirtypes.Decimal = Field(
        None,
        alias="upperLimit",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Upper limit of detection",
    )
