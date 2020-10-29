# -*- coding: utf-8 -*-
from pydantic.datetime_parse import parse_date, parse_datetime

from .. import fhirtypes  # noqa: F401
from .. import device


def test_Device_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "device-example-f001-feedingtube.canonical.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type
    impl_Device_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_Device_1(inst2)


def impl_Device_1(inst):
    assert inst.expiry == parse_date("2020-08-08")
    assert inst.id == "f001"
    assert inst.identifier[0].system == "http:/goodhealthhospital/identifier/devices"
    assert inst.identifier[0].value == "12345"
    assert inst.location.display == "Central Supply"
    assert inst.manufactureDate == parse_date("2015-08-08")
    assert inst.owner.reference == "Organization/2.16.840.1.113883.19.5"
    assert inst.status == "available"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f001</p><p><b>identifier</b>: 12345</p><p><b>type</b>: Feeding tube, device <span>(Details : {SNOMED CT code '25062003' = '25062003', given as 'Feeding tube, device'})</span></p><p><b>status</b>: available</p><p><b>manufactureDate</b>: 08/08/2015</p><p><b>expiry</b>: 08/08/2020</p><p><b>udi</b>: (01)00000123000017(10)ABC123(17)120415</p><p><b>owner</b>: <a>Organization/2.16.840.1.113883.19.5</a></p><p><b>location</b>: Central Supply</p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "25062003"
    assert inst.type.coding[0].display == "Feeding tube, device"
    assert inst.type.coding[0].system == "http://snomed.info/sct"
    assert inst.udi == "(01)00000123000017(10)ABC123(17)120415"


def test_Device_2(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "device-example-ihe-pcd.canonical.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type
    impl_Device_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_Device_2(inst2)


def impl_Device_2(inst):
    assert inst.id == "ihe-pcd"
    assert inst.identifier[0].type.coding[0].code == "SNO"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://hl7.org/fhir/identifier-type"
    )
    assert inst.identifier[0].type.text == "Serial Number"
    assert inst.identifier[0].value == "AMID-123-456"
    assert inst.lotNumber == "12345"
    assert inst.manufacturer == "Acme Devices, Inc"
    assert inst.model == "A.1.1"
    assert (
        inst.text.div
        == """<div>
      <p>Acme Patient Monitor</p>
    </div>"""
    )
    assert inst.text.status == "generated"
    assert inst.type.text == "Vital Signs Monitor"


def test_Device_3(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "device-example-pacemaker.canonical.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type
    impl_Device_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_Device_3(inst2)


def impl_Device_3(inst):
    assert inst.contact[0].system == "phone"
    assert inst.contact[0].value == "ext 4352"
    assert inst.id == "example-pacemaker"
    assert (
        inst.identifier[0].system == "http://acme.com/devices/pacemakers/octane/serial"
    )
    assert inst.identifier[0].value == "1234-5678-90AB-CDEF"
    assert inst.lotNumber == "1234-5678"
    assert inst.manufacturer == "Acme Devices, Inc"
    assert inst.model == "PM/Octane 2014"
    assert inst.patient.reference == "Patient/example"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example-pacemaker</p><p><b>identifier</b>: 1234-5678-90AB-CDEF</p><p><b>type</b>: Performance pace maker for high octane patients <span>(Details : {http://acme.com/devices code 'octane2014' = '??', given as 'Performance pace maker for high octane patients'})</span></p><p><b>manufacturer</b>: Acme Devices, Inc</p><p><b>model</b>: PM/Octane 2014</p><p><b>lotNumber</b>: 1234-5678</p><p><b>patient</b>: <a>Patient/example</a></p><p><b>contact</b>: ph: ext 4352</p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "octane2014"
    assert (
        inst.type.coding[0].display == "Performance pace maker for high octane patients"
    )
    assert inst.type.coding[0].system == "http://acme.com/devices"


def test_Device_4(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "device-example-software.canonical.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type
    impl_Device_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_Device_4(inst2)


def impl_Device_4(inst):
    assert inst.contact[0].system == "other"
    assert inst.contact[0].value == "http://acme.com"
    assert inst.id == "software"
    assert inst.identifier[0].system == "http://acme.com/ehr/client-ids"
    assert inst.identifier[0].value == "goodhealth"
    assert inst.manufacturer == "Acme Devices, Inc"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: software</p><p><b>identifier</b>: goodhealth</p><p><b>type</b>: EHR <span>(Details )</span></p><p><b>manufacturer</b>: Acme Devices, Inc</p><p><b>version</b>: 10.23-23423</p><p><b>contact</b>: http://acme.com</p><p><b>url</b>: <a>http://acme.com/goodhealth/ehr/</a></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.text == "EHR"
    assert inst.url == "http://acme.com/goodhealth/ehr/"
    assert inst.version == "10.23-23423"


def test_Device_5(base_settings):
    filename = base_settings["unittest_data_dir"] / "device-example.canonical.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type
    impl_Device_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_Device_5(inst2)


def impl_Device_5(inst):
    assert inst.contact[0].system == "phone"
    assert inst.contact[0].value == "ext 4352"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://goodcare.org/devices/id"
    assert inst.identifier[0].value == "345675"
    assert inst.identifier[1].type.coding[0].code == "SNO"
    assert (
        inst.identifier[1].type.coding[0].system
        == "http://hl7.org/fhir/identifier-type"
    )
    assert inst.identifier[1].type.text == "Serial Number"
    assert inst.identifier[1].value == "AMID-342135-8464"
    assert inst.lotNumber == "43453424"
    assert inst.manufacturer == "Acme Devices, Inc"
    assert inst.model == "AB 45-J"
    assert inst.note[0].authorReference.reference == "Practitioner/xcda-author"
    assert inst.note[0].text == "QA Checked"
    assert inst.note[0].time == parse_datetime("2015-06-28T14:03:32+10:00")
    assert inst.status == "available"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p><p><b>identifier</b>: 345675, Serial Number = AMID-342135-8464</p><p><b>type</b>: ECG <span>(Details : {SNOMED CT code '86184003' = '86184003', given as 'Electrocardiographic monitor and recorder'})</span></p><p><b>note</b>: QA Checked</p><p><b>status</b>: available</p><p><b>manufacturer</b>: Acme Devices, Inc</p><p><b>model</b>: AB 45-J</p><p><b>lotNumber</b>: 43453424</p><p><b>contact</b>: ph: ext 4352</p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "86184003"
    assert inst.type.coding[0].display == "Electrocardiographic monitor and recorder"
    assert inst.type.coding[0].system == "http://snomed.info/sct"
    assert inst.type.text == "ECG"
