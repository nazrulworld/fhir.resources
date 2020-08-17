# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/devicemetric.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceMetric(domainresource.DomainResource):
    """Measurement, calculation or setting capability of a medical device.

    Describes a measurement, calculation or setting capability of a medical
    device.
    """

    resource_type = Field("DeviceMetric", const=True)

    calibration: ListType[fhirtypes.DeviceMetricCalibrationType] = Field(
        None,
        alias="calibration",
        title=(
            "Describes the calibrations that have been performed or that are "
            "required to be performed"
        ),
        description=None,
    )

    category: fhirtypes.Code = Field(
        ...,
        alias="category",
        title="measurement | setting | calculation | unspecified",
        description=(
            "Indicates the category of the observation generation process. A "
            "DeviceMetric can be for example a setting, measurement, or "
            "calculation."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["measurement", "setting", "calculation", "unspecified"],
    )

    color: fhirtypes.Code = Field(
        None,
        alias="color",
        title="black | red | green | yellow | blue | magenta | cyan | white",
        description=(
            "Describes the color representation for the metric. This is often used "
            "to aid clinicians to track and identify parameter types by color. In "
            "practice, consider a Patient Monitor that has ECG/HR and Pleth for "
            "example; the parameters are displayed in different characteristic "
            "colors, such as HR-blue, BP-green, and PR and SpO2- magenta."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "black",
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "white",
        ],
    )

    identifier: fhirtypes.IdentifierType = Field(
        ...,
        alias="identifier",
        title="Instance identifier",
        description=(
            "Unique instance identifiers assigned to a device by the device or "
            "gateway software, manufacturers, other organizations or owners. For "
            "example: handle ID."
        ),
    )

    measurementPeriod: fhirtypes.TimingType = Field(
        None,
        alias="measurementPeriod",
        title="Describes the measurement repetition time",
        description=(
            "Describes the measurement repetition time. This is not necessarily the"
            " same as the update period. The measurement repetition time can range "
            "from milliseconds up to hours. An example for a measurement repetition"
            " time in the range of milliseconds is the sampling rate of an ECG. An "
            "example for a measurement repetition time in the range of hours is a "
            "NIBP that is triggered automatically every hour. The update period may"
            " be different than the measurement repetition time, if the device does"
            " not update the published observed value with the same frequency as it"
            " was measured."
        ),
    )

    operationalStatus: fhirtypes.Code = Field(
        None,
        alias="operationalStatus",
        title="on | off | standby",
        description=(
            "Indicates current operational state of the device. For example: On, "
            "Off, Standby, etc."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["on", "off", "standby"],
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title="Describes the link to the parent Device",
        description=(
            "Describes the link to the  Device that this DeviceMetric belongs to "
            "and that provide information about the location of this DeviceMetric "
            "in the containment structure of the parent Device. An example would be"
            " a Device that represents a Channel. This reference can be used by a "
            "client application to distinguish DeviceMetrics that have the same "
            "type, but should be interpreted based on their containment location."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceComponent"],
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Describes the link to the source Device",
        description=(
            "Describes the link to the  Device that this DeviceMetric belongs to "
            "and that contains administrative device information such as "
            "manufacturer, serial number, etc."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Identity of metric, for example Heart Rate or PEEP Setting",
        description=(
            "Describes the type of the metric. For example: Heart Rate, PEEP "
            "Setting, etc."
        ),
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Unit of Measure for the Metric",
        description=(
            "Describes the unit that an observed value determined for this metric "
            "will have. For example: Percent, Seconds, etc."
        ),
    )


class DeviceMetricCalibration(backboneelement.BackboneElement):
    """Describes the calibrations that have been performed or that are required to
    be performed.
    """

    resource_type = Field("DeviceMetricCalibration", const=True)

    state: fhirtypes.Code = Field(
        None,
        alias="state",
        title="not-calibrated | calibration-required | calibrated | unspecified",
        description="Describes the state of the calibration.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "not-calibrated",
            "calibration-required",
            "calibrated",
            "unspecified",
        ],
    )

    time: fhirtypes.Instant = Field(
        None,
        alias="time",
        title="Describes the time last calibration has been performed",
        description=None,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="unspecified | offset | gain | two-point",
        description="Describes the type of the calibration method.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["unspecified", "offset", "gain", "two-point"],
    )
