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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A series of measurements taken by a device.
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    resource_type = Field("SampledData", const=True)

    data: fhirtypes.String = Field(
        ...,
        alias="data",
        title="Type `String`",
        description='Decimal values with spaces, or "E" | "U" | "L"',
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_data", title="Extension field for ``data``."
    )

    dimensions: fhirtypes.PositiveInt = Field(
        ...,
        alias="dimensions",
        title="Type `PositiveInt`",
        description="Number of sample points at each time point",
    )
    dimensions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dimensions", title="Extension field for ``dimensions``."
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal`",
        description="Multiply data by this before adding to origin",
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    lowerLimit: fhirtypes.Decimal = Field(
        None,
        alias="lowerLimit",
        title="Type `Decimal`",
        description="Lower limit of detection",
    )
    lowerLimit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lowerLimit", title="Extension field for ``lowerLimit``."
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
        title="Type `Decimal`",
        description="Number of milliseconds between samples",
    )
    period__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_period", title="Extension field for ``period``."
    )

    upperLimit: fhirtypes.Decimal = Field(
        None,
        alias="upperLimit",
        title="Type `Decimal`",
        description="Upper limit of detection",
    )
    upperLimit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_upperLimit", title="Extension field for ``upperLimit``."
    )
