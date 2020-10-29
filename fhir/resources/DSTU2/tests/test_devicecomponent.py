# -*- coding: utf-8 -*-
from datetime import datetime, timezone

from .. import fhirtypes  # noqa: F401
from .. import devicecomponent


def test_DeviceComponent_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "devicecomponent-example-prodspec.canonical.json"
    )
    inst = devicecomponent.DeviceComponent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceComponent" == inst.resource_type
    impl_DeviceComponent_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceComponent" == data["resourceType"]

    inst2 = devicecomponent.DeviceComponent(**data)
    impl_DeviceComponent_1(inst2)


def impl_DeviceComponent_1(inst):
    assert inst.contained[0].id == "d1"
    assert inst.contained[0].identifier[0].type.coding[0].code == "SNO"
    assert (
        inst.contained[0].identifier[0].type.coding[0].system
        == "http://hl7.org/fhir/identifier-type"
    )
    assert inst.contained[0].identifier[0].type.text == "Serial Number"
    assert inst.contained[0].identifier[0].value == "ID 13.1"
    assert inst.contained[0].identifier[1].system == "urn:iso:std:iso:11073:10101"
    assert (
        inst.contained[0].identifier[1].type.text
        == "Global Medical Device Nomenclature"
    )
    assert inst.contained[0].identifier[1].value == "2000"
    assert inst.contained[0].manufacturer == "Center4MI"
    assert inst.contained[0].model == "2-0-14"
    assert inst.contained[0].type.coding[0].code == "2000"
    assert inst.contained[0].type.coding[0].display == "MDC_DEV_ANALY_SAT_O2_MDS"
    assert inst.contained[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.id == "example-prodspec"
    assert inst.identifier.type.text == "Handle ID"
    assert inst.identifier.value == "0"
    assert inst.languageCode.coding[0].code == "en-US"
    assert inst.languageCode.coding[0].system == "http://tools.ietf.org/html/bcp47"
    assert inst.lastSystemChange == datetime(
        2014, 10, 7, 14, 45, 0, tzinfo=timezone.utc
    )
    assert inst.operationalStatus[0].coding[0].code == "0"
    assert inst.operationalStatus[0].coding[0].display == "disconnected"
    assert inst.operationalStatus[0].coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.productionSpecification[0].productionSpec == "xa-12324-b"
    assert inst.productionSpecification[0].specType.coding[0].code == "1"
    assert inst.productionSpecification[0].specType.coding[0].display == "Serial number"
    assert inst.productionSpecification[1].productionSpec == "1.1"
    assert inst.productionSpecification[1].specType.coding[0].code == "3"
    assert (
        inst.productionSpecification[1].specType.coding[0].display == "Hardware version"
    )
    assert inst.productionSpecification[2].productionSpec == "1.12"
    assert inst.productionSpecification[2].specType.coding[0].code == "4"
    assert (
        inst.productionSpecification[2].specType.coding[0].display == "Software version"
    )
    assert inst.productionSpecification[3].productionSpec == "1.0.23"
    assert inst.productionSpecification[3].specType.coding[0].code == "5"
    assert (
        inst.productionSpecification[3].specType.coding[0].display == "Firmware version"
    )
    assert inst.source.reference == "#d1"
    assert (
        inst.text.div
        == """<div>
			<p>Example of a simple MDS from a pulse oximeter containment tree</p>
		</div>"""
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "2000"
    assert inst.type.coding[0].display == "MDC_DEV_ANALY_SAT_O2_MDS"
    assert inst.type.coding[0].system == "urn:iso:std:iso:11073:10101"


def test_DeviceComponent_2(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "devicecomponent-example.canonical.json"
    )
    inst = devicecomponent.DeviceComponent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceComponent" == inst.resource_type
    impl_DeviceComponent_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceComponent" == data["resourceType"]

    inst2 = devicecomponent.DeviceComponent(**data)
    impl_DeviceComponent_2(inst2)


def impl_DeviceComponent_2(inst):
    assert inst.contained[0].id == "d1"
    assert inst.contained[0].identifier[0].type.coding[0].code == "SNO"
    assert (
        inst.contained[0].identifier[0].type.coding[0].system
        == "http://hl7.org/fhir/identifier-type"
    )
    assert inst.contained[0].identifier[0].value == "ID 13.1"
    assert inst.contained[0].identifier[1].system == "urn:iso:std:iso:11073:10101"
    assert (
        inst.contained[0].identifier[1].type.text
        == "Global Medical Device Nomenclature"
    )
    assert inst.contained[0].identifier[1].value == "2000"
    assert inst.contained[0].manufacturer == "Center4MI"
    assert inst.contained[0].model == "2-0-14"
    assert inst.contained[0].type.coding[0].code == "2000"
    assert inst.contained[0].type.coding[0].display == "MDC_DEV_ANALY_SAT_O2_MDS"
    assert inst.contained[0].type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.id == "example"
    assert inst.identifier.type.text == "Handle ID"
    assert inst.identifier.value == "0"
    assert inst.languageCode.coding[0].code == "en-US"
    assert inst.languageCode.coding[0].system == "http://tools.ietf.org/html/bcp47"
    assert inst.lastSystemChange == datetime(
        2014, 10, 7, 14, 45, 0, tzinfo=timezone.utc
    )
    assert inst.operationalStatus[0].coding[0].code == "0"
    assert inst.operationalStatus[0].coding[0].display == "disconnected"
    assert inst.operationalStatus[0].coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.source.reference == "#d1"
    assert (
        inst.text.div
        == """<div>
			<p>Example of a simple MDS from a pulse oximeter containment tree</p>
		</div>"""
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "2000"
    assert inst.type.coding[0].display == "MDC_DEV_ANALY_SAT_O2_MDS"
    assert inst.type.coding[0].system == "urn:iso:std:iso:11073:10101"
