# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceComponent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import devicecomponent


def impl_devicecomponent_1(inst):
    assert inst.id == "example"
    assert inst.identifier.value == "0"
    assert inst.languageCode.coding[0].code == "en-US"
    assert inst.languageCode.coding[0].system == "http://tools.ietf.org/html/bcp47"
    assert inst.lastSystemChange == fhirtypes.Instant.validate("2014-10-07T14:45:00Z")
    assert inst.measurementPrinciple == "optical"
    assert inst.operationalStatus[0].coding[0].code == "off"
    assert inst.operationalStatus[0].coding[0].display == "Off"
    assert inst.operationalStatus[0].coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.parameterGroup.coding[0].code == "miscellaneous"
    assert inst.parameterGroup.coding[0].display == "Miscellaneous Parameter Group"
    assert inst.parameterGroup.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.parent.reference == "DeviceComponent/dc1"
    assert inst.source.reference == "Device/d1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "2000"
    assert inst.type.coding[0].display == "MDC_DEV_ANALY_SAT_O2_MDS"
    assert inst.type.coding[0].system == "urn:iso:std:iso:11073:10101"


def test_devicecomponent_1(base_settings):
    """No. 1 tests collection for DeviceComponent.
    Test File: devicecomponent-example.json
    """
    filename = base_settings["unittest_data_dir"] / "devicecomponent-example.json"
    inst = devicecomponent.DeviceComponent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceComponent" == inst.resource_type

    impl_devicecomponent_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceComponent" == data["resourceType"]

    inst2 = devicecomponent.DeviceComponent(**data)
    impl_devicecomponent_1(inst2)


def impl_devicecomponent_2(inst):
    assert inst.id == "example-prodspec"
    assert inst.identifier.value == "789123"
    assert inst.languageCode.coding[0].code == "en-US"
    assert inst.languageCode.coding[0].system == "http://tools.ietf.org/html/bcp47"
    assert inst.lastSystemChange == fhirtypes.Instant.validate("2014-10-07T14:45:00Z")
    assert inst.operationalStatus[0].coding[0].code == "off"
    assert inst.operationalStatus[0].coding[0].display == "Off"
    assert inst.productionSpecification[0].productionSpec == "xa-12324-b"
    assert inst.productionSpecification[0].specType.coding[0].code == "serial-number"
    assert inst.productionSpecification[0].specType.coding[0].display == "Serial number"
    assert inst.productionSpecification[1].productionSpec == "1.1"
    assert (
        inst.productionSpecification[1].specType.coding[0].code == "hardware-revision"
    )
    assert (
        inst.productionSpecification[1].specType.coding[0].display
        == "Hardware Revision"
    )
    assert inst.productionSpecification[2].productionSpec == "1.12"
    assert (
        inst.productionSpecification[2].specType.coding[0].code == "software-revision"
    )
    assert (
        inst.productionSpecification[2].specType.coding[0].display
        == "Software Revision"
    )
    assert inst.productionSpecification[3].productionSpec == "1.0.23"
    assert (
        inst.productionSpecification[3].specType.coding[0].code == "firmware-revision"
    )
    assert (
        inst.productionSpecification[3].specType.coding[0].display
        == "Firmware Revision"
    )
    assert inst.source.reference == "Device/d1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "2000"
    assert inst.type.coding[0].display == "MDC_DEV_ANALY_SAT_O2_MDS"
    assert inst.type.coding[0].system == "urn:iso:std:iso:11073:10101"


def test_devicecomponent_2(base_settings):
    """No. 2 tests collection for DeviceComponent.
    Test File: devicecomponent-example-prodspec.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "devicecomponent-example-prodspec.json"
    )
    inst = devicecomponent.DeviceComponent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceComponent" == inst.resource_type

    impl_devicecomponent_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceComponent" == data["resourceType"]

    inst2 = devicecomponent.DeviceComponent(**data)
    impl_devicecomponent_2(inst2)
