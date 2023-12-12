# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class DeviceMetric(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Measurement, calculation or setting capability of a medical device.
    Describes a measurement, calculation or setting capability of a device.
    """

    resource_type = Field("DeviceMetric", const=True)

    calibration: typing.List[fhirtypes.DeviceMetricCalibrationType] = Field(
        None,
        alias="calibration",
        title=(
            "Describes the calibrations that have been performed or that are "
            "required to be performed"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="measurement | setting | calculation | unspecified",
        description=(
            "Indicates the category of the observation generation process. A "
            "DeviceMetric can be for example a setting, measurement, or "
            "calculation."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["measurement", "setting", "calculation", "unspecified"],
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_category", title="Extension field for ``category``."
    )

    color: fhirtypes.Code = Field(
        None,
        alias="color",
        title="Color name (from CSS4) or #RRGGBB code",
        description=(
            "The preferred color associated with the metric (e.g., display color). "
            "This is often used to aid clinicians to track and identify parameter "
            "types by color. In practice, consider a Patient Monitor that has "
            "ECG/HR and Pleth; the metrics are displayed in different "
            "characteristic colors, such as HR in blue, BP in green, and PR and "
            "SpO2 in magenta."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    color__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_color", title="Extension field for ``color``."
    )

    device: fhirtypes.ReferenceType = Field(
        ...,
        alias="device",
        title="Describes the link to the Device",
        description=(
            "Describes the link to the Device.  This is also known as a channel "
            "device."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Instance identifier",
        description=(
            "Instance identifiers assigned to a device, by the device or gateway "
            "software, manufacturers, other organizations or owners. For example, "
            "handle ID."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    measurementFrequency: fhirtypes.QuantityType = Field(
        None,
        alias="measurementFrequency",
        title="Indicates how often the metric is taken or recorded",
        description=(
            "The frequency at which the metric is taken or recorded. Devices "
            "measure metrics at a wide range of frequencies; for example, an ECG "
            "might sample measurements in the millisecond range, while an NIBP "
            "might trigger only once an hour. Less often, the measurementFrequency "
            "may be based on a unit other than time, such as distance (e.g. for a "
            "measuring wheel). The update period may be different than the "
            "measurement frequency, if the device does not update the published "
            "observed value with the same frequency as it was measured."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    operationalStatus: fhirtypes.Code = Field(
        None,
        alias="operationalStatus",
        title="on | off | standby | entered-in-error",
        description=(
            "Indicates current operational state of the device. For example: On, "
            "Off, Standby, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["on", "off", "standby", "entered-in-error"],
    )
    operationalStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_operationalStatus",
        title="Extension field for ``operationalStatus``.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Identity of metric, for example Heart Rate or PEEP Setting",
        description=(
            "Describes the type of the metric. For example: Heart Rate, PEEP "
            "Setting, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Unit of Measure for the Metric",
        description=(
            "Describes the unit that an observed value determined for this metric "
            "will have. For example: Percent, Seconds, etc."
        ),
        # if property is element of this resource.
        element_property=True,
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
            "device",
            "operationalStatus",
            "color",
            "category",
            "measurementFrequency",
            "calibration",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1371(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("category", "category__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class DeviceMetricCalibration(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the calibrations that have been performed or that are required to
    be performed.
    """

    resource_type = Field("DeviceMetricCalibration", const=True)

    state: fhirtypes.Code = Field(
        None,
        alias="state",
        title="not-calibrated | calibration-required | calibrated | unspecified",
        description="Describes the state of the calibration.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "not-calibrated",
            "calibration-required",
            "calibrated",
            "unspecified",
        ],
    )
    state__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_state", title="Extension field for ``state``."
    )

    time: fhirtypes.Instant = Field(
        None,
        alias="time",
        title="Describes the time last calibration has been performed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    time__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_time", title="Extension field for ``time``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="unspecified | offset | gain | two-point",
        description="Describes the type of the calibration method.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["unspecified", "offset", "gain", "two-point"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DeviceMetricCalibration`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "state", "time"]
