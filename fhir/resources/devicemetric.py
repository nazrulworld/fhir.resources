# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="measurement | setting | calculation | unspecified",
    )

    color: fhirtypes.Code = Field(
        None,
        alias="color",
        title="Type `Code` (represented as `dict` in JSON)",
        description="black | red | green | yellow | blue | magenta | cyan | white",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Instance identifier",
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="on | off | standby | entered-in-error",
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title="Type `Reference` referencing `Device` (represented as `dict` in JSON)",
        description="Describes the link to the parent Device",
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
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """

    resource_type = Field("DeviceMetricCalibration", const=True)

    state: fhirtypes.Code = Field(
        None,
        alias="state",
        title="Type `Code` (represented as `dict` in JSON)",
        description="not-calibrated | calibration-required | calibrated | unspecified",
    )

    time: fhirtypes.Instant = Field(
        None,
        alias="time",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Describes the time last calibration has been performed",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="unspecified | offset | gain | two-point",
    )
