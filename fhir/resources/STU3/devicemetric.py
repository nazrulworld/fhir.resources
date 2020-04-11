# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.

    Describes a measurement, calculation or setting capability of a medical
    device.
    """

    resource_type = "DeviceMetric"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.calibration = None
        """ Describes the calibrations that have been performed or that are
        required to be performed.
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """

        self.category = None
        """ measurement | setting | calculation | unspecified.
        Type `str`. """

        self.color = None
        """ black | red | green | yellow | blue | magenta | cyan | white.
        Type `str`. """

        self.identifier = None
        """ Unique identifier of this DeviceMetric.
        Type `Identifier` (represented as `dict` in JSON). """

        self.measurementPeriod = None
        """ Describes the measurement repetition time.
        Type `Timing` (represented as `dict` in JSON). """

        self.operationalStatus = None
        """ on | off | standby | entered-in-error.
        Type `str`. """

        self.parent = None
        """ Describes the link to the parent DeviceComponent.
        Type `FHIRReference` referencing `['DeviceComponent']` (represented as `dict` in JSON). """

        self.source = None
        """ Describes the link to the source Device.
        Type `FHIRReference` referencing `['Device']` (represented as `dict` in JSON). """

        self.type = None
        """ Identity of metric, for example Heart Rate or PEEP Setting.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.unit = None
        """ Unit of Measure for the Metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(DeviceMetric, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend(
            [
                (
                    "calibration",
                    "calibration",
                    DeviceMetricCalibration,
                    "DeviceMetricCalibration",
                    True,
                    None,
                    False,
                ),
                ("category", "category", str, "code", False, None, True),
                ("color", "color", str, "code", False, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    True,
                ),
                (
                    "measurementPeriod",
                    "measurementPeriod",
                    timing.Timing,
                    "Timing",
                    False,
                    None,
                    False,
                ),
                (
                    "operationalStatus",
                    "operationalStatus",
                    str,
                    "code",
                    False,
                    None,
                    False,
                ),
                (
                    "parent",
                    "parent",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "source",
                    "source",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "unit",
                    "unit",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class DeviceMetricCalibration(backboneelement.BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """

    resource_type = "DeviceMetricCalibration"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.state = None
        """ not-calibrated | calibration-required | calibrated | unspecified.
        Type `str`. """

        self.time = None
        """ Describes the time last calibration has been performed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.type = None
        """ unspecified | offset | gain | two-point.
        Type `str`. """

        super(DeviceMetricCalibration, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend(
            [
                ("state", "state", str, "code", False, None, False),
                ("time", "time", fhirdate.FHIRDate, "instant", False, None, False),
                ("type", "type", str, "code", False, None, False),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
