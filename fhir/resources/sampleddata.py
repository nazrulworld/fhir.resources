# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SampledData
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
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
        None,
        alias="data",
        title='Decimal values with spaces, or "E" | "U" | "L"',
        description=(
            "A series of data points which are decimal values separated by a single"
            ' space (character u20). The special values "E" (error), "L" (below '
            'detection limit) and "U" (above detection limit) can also be used in '
            "place of a decimal value."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_data", title="Extension field for ``data``."
    )

    dimensions: fhirtypes.PositiveInt = Field(
        ...,
        alias="dimensions",
        title="Number of sample points at each time point",
        description=(
            "The number of sample points at each time point. If this value is "
            "greater than one, then the dimensions will be interlaced - all the "
            "sample points for a point in time will be recorded at once."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    dimensions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dimensions", title="Extension field for ``dimensions``."
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Multiply data by this before adding to origin",
        description=(
            "A correction factor that is applied to the sampled data points before "
            "they are added to the origin."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    lowerLimit: fhirtypes.Decimal = Field(
        None,
        alias="lowerLimit",
        title="Lower limit of detection",
        description=(
            "The lower limit of detection of the measured points. This is needed if"
            ' any of the data points have the value "L" (lower than detection '
            "limit)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lowerLimit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lowerLimit", title="Extension field for ``lowerLimit``."
    )

    origin: fhirtypes.QuantityType = Field(
        ...,
        alias="origin",
        title="Zero value and units",
        description=(
            "The base quantity that a measured value of zero represents. In "
            "addition, this provides the units of the entire measurement series."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.Decimal = Field(
        ...,
        alias="period",
        title="Number of milliseconds between samples",
        description="The length of time between sampling times, measured in milliseconds.",
        # if property is element of this resource.
        element_property=True,
    )
    period__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_period", title="Extension field for ``period``."
    )

    upperLimit: fhirtypes.Decimal = Field(
        None,
        alias="upperLimit",
        title="Upper limit of detection",
        description=(
            "The upper limit of detection of the measured points. This is needed if"
            ' any of the data points have the value "U" (higher than detection '
            "limit)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    upperLimit__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_upperLimit", title="Extension field for ``upperLimit``."
    )
