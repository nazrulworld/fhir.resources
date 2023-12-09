# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import devicemetric


def impl_devicemetric_1(inst):
    assert inst.calibration[0].state == "calibrated"
    assert inst.calibration[0].time == fhirtypes.Instant.validate(
        "2016-12-28T09:03:04-05:00"
    )
    assert inst.calibration[0].type == "two-point"
    assert inst.category == "measurement"
    assert inst.color == "blue"
    assert inst.id == "example"
    assert inst.identifier.system == "http://goodcare.org/devicemetric/id"
    assert inst.identifier.value == "345675"
    assert inst.measurementPeriod.repeat.frequency == 1
    assert float(inst.measurementPeriod.repeat.period) == float(1)
    assert inst.measurementPeriod.repeat.periodUnit == "s"
    assert inst.operationalStatus == "on"
    assert inst.parent.reference == "DeviceComponent/dc102"
    assert inst.source.reference == "Device/dev1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "150456"
    assert inst.type.coding[0].display == "MDC_PULS_OXIM_SAT_O2"
    assert inst.type.coding[0].system == "https://rtmms.nist.gov"
    assert inst.unit.coding[0].code == "262688"
    assert inst.unit.coding[0].display == "MDC_DIM_PERCENT"
    assert inst.unit.coding[0].system == "https://rtmms.nist.gov"


def test_devicemetric_1(base_settings):
    """No. 1 tests collection for DeviceMetric.
    Test File: devicemetric-example.json
    """
    filename = base_settings["unittest_data_dir"] / "devicemetric-example.json"
    inst = devicemetric.DeviceMetric.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceMetric" == inst.resource_type

    impl_devicemetric_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceMetric" == data["resourceType"]

    inst2 = devicemetric.DeviceMetric(**data)
    impl_devicemetric_1(inst2)
