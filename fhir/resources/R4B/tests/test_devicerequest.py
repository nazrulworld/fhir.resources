# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import devicerequest
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_devicerequest_1(inst):
    assert (
        inst.authoredOn
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-05-08T09:33:27+07:00"}
        ).valueDateTime
    )
    assert inst.basedOn[0].display == "Homecare - DM follow-up"
    assert inst.codeCodeableConcept.coding[0].code == "43148-6"
    assert (
        inst.codeCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.codeCodeableConcept.text == "Insulin delivery device panel"
    assert inst.encounter.display == "Encounter 1"
    assert inst.groupIdentifier.value == "ip_request1"
    assert inst.id == "insulinpump"
    assert inst.identifier[0].value == "ip_request1.1"
    assert inst.instantiatesCanonical[0] == (
        "http://motivemi.com/artifacts/PlanDefinition/low-suicide-" "risk-order-set"
    )
    assert inst.intent == "instance-order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == "this is the right device brand and model"
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-05-08T09:33:27+07:00"}
        ).valueDateTime
    )
    assert inst.performer.display == "Nurse Rossignol"
    assert inst.performerType.coding[0].display == "Qualified nurse"
    assert inst.performerType.text == "Nurse"
    assert inst.priorRequest[0].display == "CGM ambulatory"
    assert inst.priority == "routine"
    assert inst.reasonCode[0].text == "gastroparesis"
    assert inst.reasonReference[0].display == "Gastroparesis"
    assert inst.relevantHistory[0].display == "Request for unspecified device"
    assert inst.requester.display == "Dr. Adam Careful"
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/dicom"
    assert inst.supportingInfo[0].display == "Previous results"
    assert inst.text.status == "generated"


def test_devicerequest_1(base_settings):
    """No. 1 tests collection for DeviceRequest.
    Test File: devicerequest-example-insulinpump.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "devicerequest-example-insulinpump.json"
    )
    inst = devicerequest.DeviceRequest.model_validate_json(filename.read_bytes())
    assert "DeviceRequest" == inst.get_resource_type()

    impl_devicerequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "DeviceRequest" == data["resourceType"]

    inst2 = devicerequest.DeviceRequest(**data)
    impl_devicerequest_1(inst2)


def impl_devicerequest_2(inst):
    assert inst.codeCodeableConcept.coding[0].code == "lens"
    assert (
        inst.codeCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct"
            }
        ).valueUri
    )
    assert (
        inst.groupIdentifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.org"}
        ).valueUri
    )
    assert inst.groupIdentifier.value == "15013"
    assert inst.id == "left-lens"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.happysight.com/prescription"}
        ).valueUri
    )
    assert inst.identifier[0].value == "15013L"
    assert inst.intent == "original-order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-06-15"}
        ).valueDateTime
    )
    assert inst.parameter[0].code.coding[0].code == "28842-3"
    assert (
        inst.parameter[0].code.coding[0].display
        == "Sphere distance Glasses prescription.lens - left"
    )
    assert (
        inst.parameter[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.parameter[0].code.text == "sphere, left lens"
    assert inst.parameter[0].valueQuantity.code == "[diop]"
    assert (
        inst.parameter[0].valueQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.parameter[0].valueQuantity.unit == "Diopter"
    assert float(inst.parameter[0].valueQuantity.value) == float(-1.0)
    assert inst.parameter[1].code.coding[0].code == "28843-1"
    assert (
        inst.parameter[1].code.coding[0].display
        == "Cylinder base distance Glasses prescription.lens - left"
    )
    assert (
        inst.parameter[1].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.parameter[1].code.text == "cylinder, left lens"
    assert inst.parameter[1].valueQuantity.code == "[diop]"
    assert (
        inst.parameter[1].valueQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.parameter[1].valueQuantity.unit == "Diopter"
    assert float(inst.parameter[1].valueQuantity.value) == float(-0.5)
    assert inst.parameter[2].code.coding[0].code == "28844-9"
    assert (
        inst.parameter[2].code.coding[0].display
        == " Axis distance Glasses prescription.lens - left"
    )
    assert (
        inst.parameter[2].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.parameter[2].code.text == "axis, left lens"
    assert inst.parameter[2].valueQuantity.code == "deg"
    assert (
        inst.parameter[2].valueQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.parameter[2].valueQuantity.unit == "Degrees"
    assert float(inst.parameter[2].valueQuantity.value) == float(180)
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_devicerequest_2(base_settings):
    """No. 2 tests collection for DeviceRequest.
    Test File: devicerequest-left-lens.json
    """
    filename = base_settings["unittest_data_dir"] / "devicerequest-left-lens.json"
    inst = devicerequest.DeviceRequest.model_validate_json(filename.read_bytes())
    assert "DeviceRequest" == inst.get_resource_type()

    impl_devicerequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "DeviceRequest" == data["resourceType"]

    inst2 = devicerequest.DeviceRequest(**data)
    impl_devicerequest_2(inst2)


def impl_devicerequest_3(inst):
    assert inst.codeCodeableConcept.coding[0].code == "lens"
    assert (
        inst.codeCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct"
            }
        ).valueUri
    )
    assert (
        inst.groupIdentifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://acme.org"}
        ).valueUri
    )
    assert inst.groupIdentifier.value == "15013"
    assert inst.id == "right-lens"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.happysight.com/prescription"}
        ).valueUri
    )
    assert inst.identifier[0].value == "15013R"
    assert inst.intent == "original-order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-06-15"}
        ).valueDateTime
    )
    assert inst.parameter[0].code.coding[0].code == "28826-6"
    assert (
        inst.parameter[0].code.coding[0].display
        == "Sphere distance Glasses prescription.lens - right"
    )
    assert (
        inst.parameter[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.parameter[0].code.text == "sphere, right lens"
    assert inst.parameter[0].valueQuantity.code == "[diop]"
    assert (
        inst.parameter[0].valueQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.parameter[0].valueQuantity.unit == "Diopter"
    assert float(inst.parameter[0].valueQuantity.value) == float(-2.0)
    assert inst.parameter[1].code.coding[0].code == "28829-0"
    assert (
        inst.parameter[1].code.coding[0].display
        == "Prism base distance Glasses prescription.lens - right"
    )
    assert (
        inst.parameter[1].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.parameter[1].code.text == "prisms, right lens"
    assert inst.parameter[1].valueQuantity.code == "[diop]"
    assert (
        inst.parameter[1].valueQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.parameter[1].valueQuantity.unit == "Diopter"
    assert float(inst.parameter[1].valueQuantity.value) == float(-2.0)
    assert inst.parameter[2].code.coding[0].code == "28810-0"
    assert inst.parameter[2].code.coding[0].display == "Add 1 LM glasses lens - right"
    assert (
        inst.parameter[2].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.parameter[2].code.text == "add, right lens"
    assert inst.parameter[2].valueQuantity.code == "[diop]"
    assert (
        inst.parameter[2].valueQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.parameter[2].valueQuantity.unit == "Diopter"
    assert float(inst.parameter[2].valueQuantity.value) == float(2.0)
    assert inst.requester.reference == "Practitioner/example"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_devicerequest_3(base_settings):
    """No. 3 tests collection for DeviceRequest.
    Test File: devicerequest-right-lens.json
    """
    filename = base_settings["unittest_data_dir"] / "devicerequest-right-lens.json"
    inst = devicerequest.DeviceRequest.model_validate_json(filename.read_bytes())
    assert "DeviceRequest" == inst.get_resource_type()

    impl_devicerequest_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "DeviceRequest" == data["resourceType"]

    inst2 = devicerequest.DeviceRequest(**data)
    impl_devicerequest_3(inst2)


def impl_devicerequest_4(inst):
    assert inst.codeReference.reference == "Device/example"
    assert inst.id == "example"
    assert inst.intent == "original-order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_devicerequest_4(base_settings):
    """No. 4 tests collection for DeviceRequest.
    Test File: devicerequest-example.json
    """
    filename = base_settings["unittest_data_dir"] / "devicerequest-example.json"
    inst = devicerequest.DeviceRequest.model_validate_json(filename.read_bytes())
    assert "DeviceRequest" == inst.get_resource_type()

    impl_devicerequest_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "DeviceRequest" == data["resourceType"]

    inst2 = devicerequest.DeviceRequest(**data)
    impl_devicerequest_4(inst2)
