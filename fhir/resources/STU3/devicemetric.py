# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceMetric(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Measurement, calculation or setting capability of a medical device.
    Describes a measurement, calculation or setting capability of a medical
    device.
    """

    resource_type = Field("DeviceMetric", const=True)

    calibration: ListType[fhirtypes.DeviceMetricCalibrationType] = Field(
        None,
        alias="calibration",
        title=(
            "List of `DeviceMetricCalibration` items (represented as `dict` in " "JSON)"
        ),
        description=(
            "Describes the calibrations that have been performed or that are "
            "required to be performed"
        ),
    )

    category: fhirtypes.Code = Field(
        ...,
        alias="category",
        title="Type `Code`",
        description="measurement | setting | calculation | unspecified",
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_category", title="Extension field for ``category``."
    )

    color: fhirtypes.Code = Field(
        None,
        alias="color",
        title="Type `Code`",
        description="black | red | green | yellow | blue | magenta | cyan | white",
    )
    color__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_color", title="Extension field for ``color``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique identifier of this DeviceMetric",
    )

    measurementPeriod: fhirtypes.TimingType = Field(
        None,
        alias="measurementPeriod",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Describes the measurement repetition time",
    )

    operationalStatus: fhirtypes.Code = Field(
        None,
        alias="operationalStatus",
        title="Type `Code`",
        description="on | off | standby | entered-in-error",
    )
    operationalStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_operationalStatus",
        title="Extension field for ``operationalStatus``.",
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title=(
            "Type `Reference` referencing `DeviceComponent` (represented as `dict` "
            "in JSON)"
        ),
        description="Describes the link to the parent DeviceComponent",
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="Describes the link to the source Device",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Identity of metric, for example Heart Rate or PEEP Setting",
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Unit of Measure for the Metric",
    )


class DeviceMetricCalibration(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the calibrations that have been performed or that are required to
    be performed.
    """

    resource_type = Field("DeviceMetricCalibration", const=True)

    state: fhirtypes.Code = Field(
        None,
        alias="state",
        title="Type `Code`",
        description="not-calibrated | calibration-required | calibrated | unspecified",
    )
    state__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_state", title="Extension field for ``state``."
    )

    time: fhirtypes.Instant = Field(
        None,
        alias="time",
        title="Type `Instant`",
        description="Describes the time last calibration has been performed",
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_time", title="Extension field for ``time``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`",
        description="unspecified | offset | gain | two-point",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
