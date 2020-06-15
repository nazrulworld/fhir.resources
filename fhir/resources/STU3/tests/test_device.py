# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import device


def impl_device_1(inst):
    assert inst.contact[0].system == "url"
    assert inst.contact[0].value == "http://acme.com"
    assert inst.id == "software"
    assert inst.identifier[0].system == "http://acme.com/ehr/client-ids"
    assert inst.identifier[0].value == "goodhealth"
    assert inst.manufacturer == "Acme Devices, Inc"
    assert inst.text.status == "generated"
    assert inst.type.text == "EHR"
    assert inst.url == "http://acme.com/goodhealth/ehr/"
    assert inst.version == "10.23-23423"


def test_device_1(base_settings):
    """No. 1 tests collection for Device.
    Test File: device-example-software.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-software.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_1(inst2)


def impl_device_2(inst):
    assert inst.expirationDate == fhirtypes.DateTime.validate("2020-02-02")
    assert inst.id == "example-udi3"
    assert inst.identifier[0].type.coding[0].code == "SNO"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://hl7.org/fhir/identifier-type"
    )
    assert inst.identifier[0].value == "XYZ456789012345678"
    assert inst.lotNumber == "LOT123456789012345"
    assert inst.manufactureDate == fhirtypes.DateTime.validate("2013-02-02")
    assert inst.manufacturer == "GlobalMed, Inc"
    assert inst.model == "Ultra Implantable"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "inactive"
    assert inst.text.status == "generated"
    assert inst.udi.carrierHRF == (
        "+H123PARTNO1234567890120/$$420020216LOT123456789012345/SXYZ4"
        "56789012345678/16D20130202C"
    )
    assert inst.udi.entryType == "manual"
    assert inst.udi.issuer == "http://hl7.org/fhir/NamingSystem/hibcc"
    assert inst.udi.jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"
    assert inst.udi.name == "FHIR® Ulltra Implantable"


def test_device_2(base_settings):
    """No. 2 tests collection for Device.
    Test File: device-example-udi3.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-udi3.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_2(inst2)


def impl_device_3(inst):
    assert inst.expirationDate == fhirtypes.DateTime.validate("2014-02-01")
    assert inst.extension[0].url == "http://hl7.org/fhir/StructureDefinition/device-din"
    assert (
        inst.extension[0].valueIdentifier.system
        == "http://hl7.org/fhir/NamingSystem/iccbba-din"
    )
    assert inst.extension[0].valueIdentifier.value == "A99971312345600"
    assert inst.id == "example-udi2"
    assert inst.manufactureDate == fhirtypes.DateTime.validate("2013-02-01")
    assert inst.manufacturer == "Acme Devices, Inc"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "inactive"
    assert inst.text.status == "generated"
    assert inst.udi.deviceIdentifier == "A9999XYZ100T0474"
    assert inst.udi.issuer == "http://hl7.org/fhir/NamingSystem/iccbba-other"
    assert inst.udi.jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"
    assert inst.udi.name == "Bone,Putty Demineralized"


def test_device_3(base_settings):
    """No. 3 tests collection for Device.
    Test File: device-example-udi2.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-udi2.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_3(inst2)


def impl_device_4(inst):
    assert inst.expirationDate == fhirtypes.DateTime.validate("2020-08-08")
    assert inst.id == "f001"
    assert inst.identifier[0].system == "http:/goodhealthhospital/identifier/devices"
    assert inst.identifier[0].value == "12345"
    assert inst.location.display == "Central Supply"
    assert inst.manufactureDate == fhirtypes.DateTime.validate("2015-08-08")
    assert inst.owner.reference == "Organization/2.16.840.1.113883.19.5"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "25062003"
    assert inst.type.coding[0].display == "Feeding tube, device"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_device_4(base_settings):
    """No. 4 tests collection for Device.
    Test File: device-example-f001-feedingtube.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-f001-feedingtube.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_4(inst2)


def impl_device_5(inst):
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
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "octane2014"
    assert (
        inst.type.coding[0].display == "Performance pace maker for high octane patients"
    )
    assert inst.type.coding[0].system == "http://acme.com/devices"


def test_device_5(base_settings):
    """No. 5 tests collection for Device.
    Test File: device-example-pacemaker.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-pacemaker.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_5(inst2)


def impl_device_6(inst):
    assert inst.id == "example-udi4"
    assert inst.lotNumber == "RZ12345678"
    assert inst.manufacturer == "GlobalMed, Inc"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "inactive"
    assert inst.text.status == "generated"
    assert inst.udi.carrierHRF == "=)1TE123456A&)RZ12345678"
    assert inst.udi.issuer == "http://hl7.org/fhir/NamingSystem/iccbba-blood"
    assert inst.udi.jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"


def test_device_6(base_settings):
    """No. 6 tests collection for Device.
    Test File: device-example-udi4.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-udi4.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_6(inst2)


def impl_device_7(inst):
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
    assert inst.text.status == "generated"
    assert inst.type.text == "Vital Signs Monitor"


def test_device_7(base_settings):
    """No. 7 tests collection for Device.
    Test File: device-example-ihe-pcd.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-ihe-pcd.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_7(inst2)


def impl_device_8(inst):
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
    assert inst.note[0].time == fhirtypes.DateTime.validate("2015-06-28T14:03:32+10:00")
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "86184003"
    assert inst.type.coding[0].display == "Electrocardiographic monitor and recorder"
    assert inst.type.coding[0].system == "http://snomed.info/sct"
    assert inst.type.text == "ECG"


def test_device_8(base_settings):
    """No. 8 tests collection for Device.
    Test File: device-example.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_8(inst2)


def impl_device_9(inst):
    assert inst.expirationDate == fhirtypes.DateTime.validate("2014-11-20")
    assert inst.id == "example-udi1"
    assert (
        inst.identifier[0].system == "http://acme.com/devices/pacemakers/octane/serial"
    )
    assert inst.identifier[0].value == "1234-5678-90AB-CDEF"
    assert inst.identifier[1].type.coding[0].code == "SNO"
    assert (
        inst.identifier[1].type.coding[0].system
        == "http://hl7.org/fhir/identifier-type"
    )
    assert inst.identifier[1].value == "10987654d321"
    assert inst.lotNumber == "7654321D"
    assert inst.manufacturer == "Acme Devices, Inc"
    assert inst.model == "PM/Octane 2014"
    assert inst.patient.reference == "Patient/example"
    assert inst.safety[0].coding[0].code == "mr-unsafe"
    assert inst.safety[0].coding[0].display == "MR Unsafe"
    assert inst.safety[0].coding[0].system == "urn:oid:2.16.840.1.113883.3.26.1.1"
    assert inst.safety[0].text == "MR Unsafe"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "468063009"
    assert inst.type.coding[0].display == "Coated femoral stem prosthesis, modular"
    assert inst.type.coding[0].system == "http://snomed.info/sct"
    assert inst.type.text == "Coated femoral stem prosthesis, modular"
    assert inst.udi.carrierAIDC == bytes_validator(
        (
            "XWQyMDExMDg1NzY3NDAwMjAxNzE3MTQxMTIwMTBOWUZVTDAx4oaUMjExOTI4"
            "MzfihpQ3MTNBMUIyQzNENEU1RjZH"
        )
    )
    assert (
        inst.udi.carrierHRF
        == "{01}00844588003288{17}141120{10}7654321D{21}10987654d321"
    )
    assert inst.udi.deviceIdentifier == "00844588003288"
    assert inst.udi.entryType == "barcode"
    assert inst.udi.issuer == "http://hl7.org/fhir/NamingSystem/gs1"
    assert inst.udi.jurisdiction == "http://hl7.org/fhir/NamingSystem/fda-udi"
    assert inst.udi.name == "FHIR® Hip System"


def test_device_9(base_settings):
    """No. 9 tests collection for Device.
    Test File: device-example-udi1.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-udi1.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_9(inst2)
