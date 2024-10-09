from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceMetric(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Measurement, calculation or setting capability of a medical device.
    Describes a measurement, calculation or setting capability of a medical
    device.
    """

    __resource_type__ = "DeviceMetric"

    calibration: typing.List[fhirtypes.DeviceMetricCalibrationType] | None = Field(  # type: ignore
        None,
        alias="calibration",
        title=(
            "Describes the calibrations that have been performed or that are "
            "required to be performed"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="category",
        title="measurement | setting | calculation | unspecified",
        description=(
            "Indicates the category of the observation generation process. A "
            "DeviceMetric can be for example a setting, measurement, or "
            "calculation."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["measurement", "setting", "calculation", "unspecified"],
        },
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_category", title="Extension field for ``category``."
    )

    color: fhirtypes.CodeType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "black",
                "red",
                "green",
                "yellow",
                "blue",
                "magenta",
                "cyan",
                "white",
            ],
        },
    )
    color__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_color", title="Extension field for ``color``."
    )

    identifier: fhirtypes.IdentifierType = Field(  # type: ignore
        ...,
        alias="identifier",
        title="Unique identifier of this DeviceMetric",
        description=(
            "Describes the unique identification of this metric that has been "
            "assigned by the device or gateway software. For example: handle ID.  "
            "It should be noted that in order to make the identifier unique, the "
            "system element of the identifier should be set to the unique "
            "identifier of the device."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    measurementPeriod: fhirtypes.TimingType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    operationalStatus: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="operationalStatus",
        title="on | off | standby | entered-in-error",
        description=(
            "Indicates current operational state of the device. For example: On, "
            "Off, Standby, etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["on", "off", "standby", "entered-in-error"],
        },
    )
    operationalStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_operationalStatus",
        title="Extension field for ``operationalStatus``.",
    )

    parent: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="parent",
        title="Describes the link to the parent DeviceComponent",
        description=(
            "Describes the link to the  DeviceComponent that this DeviceMetric "
            "belongs to and that provide information about the location of this "
            "DeviceMetric in the containment structure of the parent Device. An "
            "example would be a DeviceComponent that represents a Channel. This "
            "reference can be used by a client application to distinguish "
            "DeviceMetrics that have the same type, but should be interpreted based"
            " on their containment location."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DeviceComponent"],
        },
    )

    source: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Describes the link to the source Device",
        description=(
            "Describes the link to the  Device that this DeviceMetric belongs to "
            "and that contains administrative device information such as "
            "manufacturer, serial number, etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Identity of metric, for example Heart Rate or PEEP Setting",
        description=(
            "Describes the type of the metric. For example: Heart Rate, PEEP "
            "Setting, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unit: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="unit",
        title="Unit of Measure for the Metric",
        description=(
            "Describes the unit that an observed value determined for this metric "
            "will have. For example: Percent, Seconds, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceMetric`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "type",
            "unit",
            "source",
            "parent",
            "operationalStatus",
            "color",
            "category",
            "measurementPeriod",
            "calibration",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("category", "category__ext")]
        return required_fields


class DeviceMetricCalibration(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the calibrations that have been performed or that are required to
    be performed.
    """

    __resource_type__ = "DeviceMetricCalibration"

    state: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="state",
        title="not-calibrated | calibration-required | calibrated | unspecified",
        description="Describes the state of the calibration.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "not-calibrated",
                "calibration-required",
                "calibrated",
                "unspecified",
            ],
        },
    )
    state__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_state", title="Extension field for ``state``."
    )

    time: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="time",
        title="Describes the time last calibration has been performed",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_time", title="Extension field for ``time``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="unspecified | offset | gain | two-point",
        description="Describes the type of the calibration method.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["unspecified", "offset", "gain", "two-point"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceMetricCalibration`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "state", "time"]
