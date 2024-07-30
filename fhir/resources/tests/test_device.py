# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import device
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_device_1(inst):
    assert inst.contact[0].system == "url"
    assert inst.contact[0].value == "http://acme.com"
    assert inst.id == "example-software"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/ehr/client-ids"}
        ).valueUri
    )
    assert inst.identifier[0].value == "goodhealth"
    assert inst.manufacturer == "Acme Devices, Inc"
    assert inst.text.status == "generated"
    assert inst.type[0].text == "EHR"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/goodhealth/ehr/"}
        ).valueUri
    )
    assert inst.version[0].value == "10.23-23423"


def test_device_1(base_settings):
    """No. 1 tests collection for Device.
    Test File: device-example-software.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-software.json"
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_1(inst2)


def impl_device_2(inst):
    assert (
        inst.expirationDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2020-02-02"}
        ).valueDateTime
    )
    assert inst.id == "example-udi3"
    assert inst.identifier[0].type.coding[0].code == "SNO"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.identifier[0].value == "XYZ456789012345678"
    assert inst.lotNumber == "LOT123456789012345"
    assert (
        inst.manufactureDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-02-02"}
        ).valueDateTime
    )
    assert inst.manufacturer == "GlobalMed, Inc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "Ultra Implantable"
    assert inst.status == "inactive"
    assert inst.text.status == "generated"
    assert inst.udiCarrier[0].carrierHRF == (
        "+H123PARTNO1234567890120/$$420020216LOT123456789012345/SXYZ4"
        "56789012345678/16D20130202C"
    )
    assert inst.udiCarrier[0].deviceIdentifier == "007444534255003288"
    assert inst.udiCarrier[0].entryType == "manual"
    assert (
        inst.udiCarrier[0].issuer
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/hibcc"}
        ).valueUri
    )
    assert (
        inst.udiCarrier[0].jurisdiction
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/fda-udi"}
        ).valueUri
    )


def test_device_2(base_settings):
    """No. 2 tests collection for Device.
    Test File: device-example-udi3.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-udi3.json"
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_2(inst2)


def impl_device_3(inst):
    assert inst.conformsTo[0].specification.coding[0].code == "528388"
    assert (
        inst.conformsTo[0].specification.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.conformsTo[0].specification.text
        == "MDC_DEV_SPEC_PROFILE_PULS_OXIM: Pulse Oximeter"
    )
    assert inst.conformsTo[0].version == "1"
    assert inst.id == "NoninBlePulseOx"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:1.2.840.10004.1.1.1.0.0.1.0.0.1.2680"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "SYSID"
    assert inst.identifier[0].type.coding[0].display == "System Identifier"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifiers"
            }
        ).valueUri
    )
    assert inst.identifier[0].value == "74-E8-FF-FE-FF-05-1C-00"
    assert (
        inst.identifier[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/sid/eui-48"}
        ).valueUri
    )
    assert inst.identifier[1].type.coding[0].code == "BTMAC"
    assert inst.identifier[1].type.coding[0].display == "Bluetooth Address"
    assert (
        inst.identifier[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifiers"
            }
        ).valueUri
    )
    assert inst.identifier[1].value == "00-1C-05-FF-E8-74"
    assert inst.manufacturer == "Nonin_Medical_Inc."
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.modelNumber == "Model 3230"
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "Nonin3230_501900083"
    assert inst.property[0].type.coding[0].code == "532353"
    assert (
        inst.property[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.property[0].type.text == (
        "MDC_REG_CERT_DATA_CONTINUA_CERT_DEV_LIST: Continua certified" " device list"
    )
    assert inst.property[0].valueCodeableConcept.coding[0].code == "4"
    assert (
        inst.property[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ContinuaPAN"}
        ).valueUri
    )
    assert inst.property[1].type.coding[0].code == "532354.0"
    assert (
        inst.property[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"}
        ).valueUri
    )
    assert inst.property[1].type.text == "regulation-status"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "N"
    assert (
        inst.property[1].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0136"}
        ).valueUri
    )
    assert inst.property[1].valueCodeableConcept.text == "Device is Regulated"
    assert inst.property[2].type.coding[0].code == "68220"
    assert (
        inst.property[2].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.property[2].type.text
        == "MDC_TIME_SYNC_PROTOCOL: Time synchronization protocol"
    )
    assert inst.property[2].valueCodeableConcept.coding[0].code == "532224"
    assert (
        inst.property[2].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.property[2].valueCodeableConcept.text
        == "MDC_TIME_SYNC_NONE: No time synchronization"
    )
    assert inst.property[3].type.coding[0].code == "68219.0"
    assert (
        inst.property[3].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"}
        ).valueUri
    )
    assert inst.property[3].type.text == "mds-time-capab-real-time-clock"
    assert inst.property[3].valueCodeableConcept.coding[0].code == "Y"
    assert (
        inst.property[3].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0136"}
        ).valueUri
    )
    assert inst.property[3].valueCodeableConcept.text == "real time clock supported"
    assert inst.property[4].type.coding[0].code == "68219.1"
    assert (
        inst.property[4].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"}
        ).valueUri
    )
    assert inst.property[4].type.text == "mds-time-capab-set-clock"
    assert inst.property[4].valueCodeableConcept.coding[0].code == "Y"
    assert (
        inst.property[4].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0136"}
        ).valueUri
    )
    assert inst.property[4].valueCodeableConcept.text == "setting the time supported"
    assert inst.serialNumber == "501900083"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "65573"
    assert inst.type[0].coding[0].display == "MDC_MOC_VMS_MDS_SIMP"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.type[0].text == "MDC_MOC_VMS_MDS_SIMP: Personal Health Device"
    assert inst.udiCarrier[0].carrierHRF == "(01)120359741556(21)501900083"
    assert inst.udiCarrier[0].deviceIdentifier == "120359741556"
    assert inst.udiCarrier[0].entryType == "unknown"
    assert (
        inst.udiCarrier[0].issuer
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/gs1-di"}
        ).valueUri
    )
    assert (
        inst.udiCarrier[0].jurisdiction
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/fda-udi"}
        ).valueUri
    )
    assert inst.version[0].type.coding[0].code == "531976"
    assert (
        inst.version[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.version[0].type.text == "MDC_ID_PROD_SPEC_FW: Firmware revision"
    assert inst.version[0].value == "r2.1"
    assert inst.version[1].type.coding[0].code == "531975"
    assert (
        inst.version[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.version[1].type.text == "MDC_ID_PROD_SPEC_SW: Software revision"
    assert inst.version[1].value == "r1.5 9.7"
    assert inst.version[2].type.coding[0].code == "531974"
    assert (
        inst.version[2].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.version[2].type.text == "MDC_ID_PROD_SPEC_HW: Hardware revision"
    assert inst.version[2].value == "r1.0"
    assert inst.version[3].type.coding[0].code == "532352"
    assert (
        inst.version[3].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.version[3].type.text
        == "MDC_REG_CERT_DATA_CONTINUA_VERSION: Continua version"
    )
    assert inst.version[3].value == "6.0"


def test_device_3(base_settings):
    """No. 3 tests collection for Device.
    Test File: device-example-NoninBlePulseOx.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-NoninBlePulseOx.json"
    )
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_3(inst2)


def impl_device_4(inst):
    assert (
        inst.expirationDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-02-01"}
        ).valueDateTime
    )
    assert inst.id == "example-udi2"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/iccbba-din"}
        ).valueUri
    )
    assert inst.identifier[0].value == "A99971312345600"
    assert (
        inst.manufactureDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-02-01"}
        ).valueDateTime
    )
    assert inst.manufacturer == "Acme Devices, Inc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.status == "inactive"
    assert inst.text.status == "generated"
    assert inst.udiCarrier[0].deviceIdentifier == "A9999XYZ100T0474"
    assert (
        inst.udiCarrier[0].issuer
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/iccbba-other"}
        ).valueUri
    )
    assert (
        inst.udiCarrier[0].jurisdiction
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/fda-udi"}
        ).valueUri
    )


def test_device_4(base_settings):
    """No. 4 tests collection for Device.
    Test File: device-example-udi2.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example-udi2.json"
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_4(inst2)


def impl_device_5(inst):
    assert inst.conformsTo[0].specification.coding[0].code == "528392"
    assert (
        inst.conformsTo[0].specification.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.conformsTo[0].specification.text
        == "MDC_DEV_SPEC_PROFILE_TEMP: Thermometer"
    )
    assert inst.conformsTo[0].version == "1"
    assert inst.id == "PhilipsThermometer"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:1.2.840.10004.1.1.1.0.0.1.0.0.1.2680"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "SYSID"
    assert inst.identifier[0].type.coding[0].display == "System Identifier"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifiers"
            }
        ).valueUri
    )
    assert inst.identifier[0].value == "1C-87-74-FF-FE-00-EC-20"
    assert (
        inst.identifier[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/sid/eui-48"}
        ).valueUri
    )
    assert inst.identifier[1].type.coding[0].code == "BTMAC"
    assert inst.identifier[1].type.coding[0].display == "Bluetooth Address"
    assert (
        inst.identifier[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifiers"
            }
        ).valueUri
    )
    assert inst.identifier[1].value == "1C-87-74-00-EC-20"
    assert inst.manufacturer == "Philips"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.modelNumber == "DL8740"
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "Philips ear thermometer"
    assert inst.property[0].type.coding[0].code == "532353"
    assert (
        inst.property[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.property[0].type.text == (
        "MDC_REG_CERT_DATA_CONTINUA_CERT_DEV_LIST: Continua certified" " device list"
    )
    assert inst.property[0].valueCodeableConcept.coding[0].code == "32776"
    assert (
        inst.property[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ContinuaPAN"}
        ).valueUri
    )
    assert inst.property[1].type.coding[0].code == "532354.0"
    assert (
        inst.property[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"}
        ).valueUri
    )
    assert inst.property[1].type.text == "regulation-status"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "N"
    assert (
        inst.property[1].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0136"}
        ).valueUri
    )
    assert inst.property[1].valueCodeableConcept.text == "Device is Regulated"
    assert inst.property[2].type.coding[0].code == "68220"
    assert (
        inst.property[2].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.property[2].type.text
        == "MDC_TIME_SYNC_PROTOCOL: Time synchronization protocol"
    )
    assert inst.property[2].valueCodeableConcept.coding[0].code == "532224"
    assert (
        inst.property[2].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.property[2].valueCodeableConcept.text
        == "MDC_TIME_SYNC_NONE: No time synchronization"
    )
    assert inst.property[3].type.coding[0].code == "68219.0"
    assert (
        inst.property[3].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"}
        ).valueUri
    )
    assert inst.property[3].type.text == "mds-time-capab-real-time-clock"
    assert inst.property[3].valueCodeableConcept.coding[0].code == "Y"
    assert (
        inst.property[3].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0136"}
        ).valueUri
    )
    assert inst.property[3].valueCodeableConcept.text == "real time clock supported"
    assert inst.property[4].type.coding[0].code == "68219.1"
    assert (
        inst.property[4].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/ASN1ToHL7"}
        ).valueUri
    )
    assert inst.property[4].type.text == "mds-time-capab-set-clock"
    assert inst.property[4].valueCodeableConcept.coding[0].code == "Y"
    assert (
        inst.property[4].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0136"}
        ).valueUri
    )
    assert inst.property[4].valueCodeableConcept.text == "setting the time supported"
    assert inst.serialNumber == "162502000528"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "65573"
    assert inst.type[0].coding[0].display == "MDC_MOC_VMS_MDS_SIMP"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.type[0].text == "MDC_MOC_VMS_MDS_SIMP: Personal Health Device"
    assert inst.udiCarrier[0].carrierHRF == "(01)31368092380192(21)162502000528"
    assert inst.udiCarrier[0].deviceIdentifier == "31368092380192"
    assert inst.udiCarrier[0].entryType == "unknown"
    assert (
        inst.udiCarrier[0].issuer
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/gs1-di"}
        ).valueUri
    )
    assert (
        inst.udiCarrier[0].jurisdiction
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/fda-udi"}
        ).valueUri
    )
    assert inst.version[0].type.coding[0].code == "531976"
    assert (
        inst.version[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.version[0].type.text == "MDC_ID_PROD_SPEC_FW: Firmware revision"
    assert inst.version[0].value == "1.60"
    assert inst.version[1].type.coding[0].code == "531975"
    assert (
        inst.version[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.version[1].type.text == "MDC_ID_PROD_SPEC_SW: Software revision"
    assert inst.version[1].value == "1.50"
    assert inst.version[2].type.coding[0].code == "531974"
    assert (
        inst.version[2].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.version[2].type.text == "MDC_ID_PROD_SPEC_SW: Hardware revision"
    assert inst.version[2].value == "1.40"
    assert inst.version[3].type.coding[0].code == "532352"
    assert (
        inst.version[3].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.version[3].type.text
        == "MDC_REG_CERT_DATA_CONTINUA_VERSION: Continua version"
    )
    assert inst.version[3].value == "5.1"


def test_device_5(base_settings):
    """No. 5 tests collection for Device.
    Test File: device-example-PhilipsThermometer.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-PhilipsThermometer.json"
    )
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_5(inst2)


def impl_device_6(inst):
    assert inst.displayName == "Lavender Tube"
    assert inst.id == "device-example-specimen-container-lavender-vacutainer"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/containers/id"}
        ).valueUri
    )
    assert inst.identifier[0].value == "345675"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.property[0].type.coding[0].code == "tube-type"
    assert inst.property[0].type.coding[0].display == "Tube Type"
    assert (
        inst.property[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/containers/codes"}
        ).valueUri
    )
    assert inst.property[0].valueCodeableConcept.coding[0].code == "lavender"
    assert inst.property[0].valueCodeableConcept.coding[0].display == "lavender-tube"
    assert (
        inst.property[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/containers/types"}
        ).valueUri
    )
    assert inst.property[1].type.coding[0].code == "amount"
    assert inst.property[1].type.coding[0].display == "Amount"
    assert (
        inst.property[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/containers/codes"}
        ).valueUri
    )
    assert inst.property[1].valueCodeableConcept.coding[0].code == "4.5mL"
    assert inst.property[1].valueCodeableConcept.coding[0].display == "4.5 mL"
    assert (
        inst.property[1].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/containers/capacities"}
        ).valueUri
    )
    assert inst.property[2].type.coding[0].code == "additive"
    assert inst.property[2].type.coding[0].display == "Additive"
    assert (
        inst.property[2].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/containers/codes"}
        ).valueUri
    )
    assert inst.property[2].valueCodeableConcept.coding[0].code == "EDTA"
    assert inst.property[2].valueCodeableConcept.coding[0].display == "EDTA"
    assert (
        inst.property[2].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.com/containers/additive"}
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_device_6(base_settings):
    """No. 6 tests collection for Device.
    Test File: device-example-specimen-container-lavender-vacutainer.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "device-example-specimen-container-lavender-vacutainer.json"
    )
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_6(inst2)


def impl_device_7(inst):
    assert inst.conformsTo[0].specification.coding[0].code == "528392"
    assert (
        inst.conformsTo[0].specification.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.conformsTo[0].specification.text
        == "MDC_DEV_SPEC_PROFILE_TEMP: Thermometer"
    )
    assert inst.conformsTo[0].version == "1"
    assert inst.id == "KinsaThermometer"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:1.2.840.10004.1.1.1.0.0.1.0.0.1.2680"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "SYSID"
    assert inst.identifier[0].type.coding[0].display == "System Identifier"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifiers"
            }
        ).valueUri
    )
    assert inst.identifier[0].value == "00-00-52-49-20-45-4C-42"
    assert (
        inst.identifier[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/sid/eui-48"}
        ).valueUri
    )
    assert inst.identifier[1].type.coding[0].code == "BTMAC"
    assert inst.identifier[1].type.coding[0].display == "Bluetooth Address"
    assert (
        inst.identifier[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/ContinuaDeviceIdentifiers"
            }
        ).valueUri
    )
    assert inst.identifier[1].value == "10-CE-A9-80-14-66"
    assert inst.manufacturer == "Kinsa"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.modelNumber == "KS_1i9JfKh"
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "KS_1i9JfKh"
    assert inst.property[0].type.coding[0].code == "68220"
    assert (
        inst.property[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.property[0].type.text
        == "MDC_TIME_SYNC_PROTOCOL: Time synchronization protocol"
    )
    assert inst.property[0].valueCodeableConcept.coding[0].code == "532224"
    assert (
        inst.property[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert (
        inst.property[0].valueCodeableConcept.text
        == "MDC_TIME_SYNC_NONE: No time synchronization"
    )
    assert inst.serialNumber == "1i9JfKh"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "65573"
    assert inst.type[0].coding[0].display == "MDC_MOC_VMS_MDS_SIMP"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.type[0].text == "MDC_MOC_VMS_MDS_SIMP: Personal Health Device"
    assert inst.udiCarrier[0].carrierHRF == "(01)18479793050726(21)1i9JfKh"
    assert inst.udiCarrier[0].deviceIdentifier == "18479793050726"
    assert inst.udiCarrier[0].entryType == "unknown"
    assert (
        inst.udiCarrier[0].issuer
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/gs1-di"}
        ).valueUri
    )
    assert (
        inst.udiCarrier[0].jurisdiction
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/fda-udi"}
        ).valueUri
    )
    assert inst.version[0].type.coding[0].code == "531976"
    assert (
        inst.version[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.version[0].type.text == "MDC_ID_PROD_SPEC_FW: Firmware revision"
    assert inst.version[0].value == "1.00"
    assert inst.version[1].type.coding[0].code == "531975"
    assert (
        inst.version[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.version[1].type.text == "MDC_ID_PROD_SPEC_SW: Software revision"
    assert inst.version[1].value == "V2.19"
    assert inst.version[2].type.coding[0].code == "531974"
    assert (
        inst.version[2].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:11073:10101"}
        ).valueUri
    )
    assert inst.version[2].type.text == "MDC_ID_PROD_SPEC_SW: Hardware revision"
    assert inst.version[2].value == "1.00"


def test_device_7(base_settings):
    """No. 7 tests collection for Device.
    Test File: device-example-KinsaThermometer.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-KinsaThermometer.json"
    )
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_7(inst2)


def impl_device_8(inst):
    assert inst.id == "f001"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http:/goodhealthhospital/identifier/devices"}
        ).valueUri
    )
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_device_8(base_settings):
    """No. 8 tests collection for Device.
    Test File: device-example-f001-feedingtube.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-f001-feedingtube.json"
    )
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_8(inst2)


def impl_device_9(inst):
    assert inst.id == "NGS-device"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/devices"}
        ).valueUri
    )
    assert inst.identifier[0].value == "11111"
    assert inst.manufacturer == "Illumina"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "NextSeq 550 Instrument"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "49062001"
    assert inst.type[0].coding[0].display == "Device (physical object)"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )


def test_device_9(base_settings):
    """No. 9 tests collection for Device.
    Test File: Device-NGS-device.json
    """
    filename = base_settings["unittest_data_dir"] / "Device-NGS-device.json"
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_9(inst2)


def impl_device_10(inst):
    assert inst.id == "Triodenovo-SW"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/devices"}
        ).valueUri
    )
    assert inst.identifier[0].value == "11112"
    assert inst.manufacturer == "Vanderbilt Genetics Institute"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name[0].type == "user-friendly-name"
    assert inst.name[0].value == "Triodenovo Software"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "706687001"
    assert inst.type[0].coding[0].display == "Software (physical object)"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.version[0].value == "0.06"


def test_device_10(base_settings):
    """No. 10 tests collection for Device.
    Test File: Device-Triodenovo-SW.json
    """
    filename = base_settings["unittest_data_dir"] / "Device-Triodenovo-SW.json"
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_10(inst2)
