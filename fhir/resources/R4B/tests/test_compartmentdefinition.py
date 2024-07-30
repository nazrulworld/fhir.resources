# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CompartmentDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import compartmentdefinition
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_compartmentdefinition_1(inst):
    assert inst.code == "Device"
    assert inst.contact[0].name == "[string]"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2017-02-24"}
        ).valueDateTime
    )
    assert inst.description == (
        "The set of resources associated with a particular Device "
        "(example with Communication and CommunicationRequest "
        "resourses only)."
    )
    assert inst.experimental is True
    assert inst.id == "example"
    assert inst.name == "EXAMPLE"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.purpose == (
        "Provides an example of a FHIR compartment definition based "
        "on the Device resource type."
    )
    assert inst.resource[0].code == "Communication"
    assert (
        inst.resource[0].documentation
        == "The device used as the message sender and recipient"
    )
    assert inst.resource[0].param[0] == "sender"
    assert inst.resource[0].param[1] == "recipient"
    assert inst.resource[1].code == "CommunicationRequest"
    assert (
        inst.resource[1].documentation
        == "The device used as the message sender and recipient"
    )
    assert inst.resource[1].param[0] == "sender"
    assert inst.resource[1].param[1] == "recipient"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/example"}
        ).valueUri
    )
    assert inst.useContext[0].code.code == "focus"
    assert (
        inst.useContext[0].code.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/usage-context-type"}
        ).valueUri
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "Device"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/resource-types"}
        ).valueUri
    )


def test_compartmentdefinition_1(base_settings):
    """No. 1 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "compartmentdefinition-example.json"
    inst = compartmentdefinition.CompartmentDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "CompartmentDefinition" == inst.get_resource_type()

    impl_compartmentdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CompartmentDefinition" == data["resourceType"]

    inst2 = compartmentdefinition.CompartmentDefinition(**data)
    impl_compartmentdefinition_1(inst2)


def impl_compartmentdefinition_2(inst):
    assert inst.code == "RelatedPerson"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-05-28T12:47:40+10:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.id == "relatedPerson"
    assert inst.name == "Base FHIR compartment definition for RelatedPerson"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdministrableProductDefinition"
    assert inst.resource[3].code == "AdverseEvent"
    assert inst.resource[3].param[0] == "recorder"
    assert inst.resource[4].code == "AllergyIntolerance"
    assert inst.resource[4].param[0] == "asserter"
    assert inst.resource[5].code == "Appointment"
    assert inst.resource[5].param[0] == "actor"
    assert inst.resource[6].code == "AppointmentResponse"
    assert inst.resource[6].param[0] == "actor"
    assert inst.resource[7].code == "AuditEvent"
    assert inst.resource[8].code == "Basic"
    assert inst.resource[8].param[0] == "author"
    assert inst.resource[9].code == "Binary"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/relatedPerson"}
        ).valueUri
    )
    assert inst.version == "4.3.0"


def test_compartmentdefinition_2(base_settings):
    """No. 2 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-relatedperson.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "compartmentdefinition-relatedperson.json"
    )
    inst = compartmentdefinition.CompartmentDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "CompartmentDefinition" == inst.get_resource_type()

    impl_compartmentdefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CompartmentDefinition" == data["resourceType"]

    inst2 = compartmentdefinition.CompartmentDefinition(**data)
    impl_compartmentdefinition_2(inst2)


def impl_compartmentdefinition_3(inst):
    assert inst.code == "Patient"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-05-28T12:47:40+10:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.id == "patient"
    assert inst.name == "Base FHIR compartment definition for Patient"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[0].param[0] == "subject"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdministrableProductDefinition"
    assert inst.resource[3].code == "AdverseEvent"
    assert inst.resource[3].param[0] == "subject"
    assert inst.resource[4].code == "AllergyIntolerance"
    assert inst.resource[4].param[0] == "patient"
    assert inst.resource[4].param[1] == "recorder"
    assert inst.resource[4].param[2] == "asserter"
    assert inst.resource[5].code == "Appointment"
    assert inst.resource[5].param[0] == "actor"
    assert inst.resource[6].code == "AppointmentResponse"
    assert inst.resource[6].param[0] == "actor"
    assert inst.resource[7].code == "AuditEvent"
    assert inst.resource[7].param[0] == "patient"
    assert inst.resource[8].code == "Basic"
    assert inst.resource[8].param[0] == "patient"
    assert inst.resource[8].param[1] == "author"
    assert inst.resource[9].code == "Binary"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/patient"}
        ).valueUri
    )
    assert inst.version == "4.3.0"


def test_compartmentdefinition_3(base_settings):
    """No. 3 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-patient.json
    """
    filename = base_settings["unittest_data_dir"] / "compartmentdefinition-patient.json"
    inst = compartmentdefinition.CompartmentDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "CompartmentDefinition" == inst.get_resource_type()

    impl_compartmentdefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CompartmentDefinition" == data["resourceType"]

    inst2 = compartmentdefinition.CompartmentDefinition(**data)
    impl_compartmentdefinition_3(inst2)


def impl_compartmentdefinition_4(inst):
    assert inst.code == "Practitioner"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-05-28T12:47:40+10:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.id == "practitioner"
    assert inst.name == "Base FHIR compartment definition for Practitioner"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[0].param[0] == "subject"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdministrableProductDefinition"
    assert inst.resource[3].code == "AdverseEvent"
    assert inst.resource[3].param[0] == "recorder"
    assert inst.resource[4].code == "AllergyIntolerance"
    assert inst.resource[4].param[0] == "recorder"
    assert inst.resource[4].param[1] == "asserter"
    assert inst.resource[5].code == "Appointment"
    assert inst.resource[5].param[0] == "actor"
    assert inst.resource[6].code == "AppointmentResponse"
    assert inst.resource[6].param[0] == "actor"
    assert inst.resource[7].code == "AuditEvent"
    assert inst.resource[7].param[0] == "agent"
    assert inst.resource[8].code == "Basic"
    assert inst.resource[8].param[0] == "author"
    assert inst.resource[9].code == "Binary"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/practitioner"}
        ).valueUri
    )
    assert inst.version == "4.3.0"


def test_compartmentdefinition_4(base_settings):
    """No. 4 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-practitioner.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "compartmentdefinition-practitioner.json"
    )
    inst = compartmentdefinition.CompartmentDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "CompartmentDefinition" == inst.get_resource_type()

    impl_compartmentdefinition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CompartmentDefinition" == data["resourceType"]

    inst2 = compartmentdefinition.CompartmentDefinition(**data)
    impl_compartmentdefinition_4(inst2)


def impl_compartmentdefinition_5(inst):
    assert inst.code == "Encounter"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-05-28T12:47:40+10:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.id == "encounter"
    assert inst.name == "Base FHIR compartment definition for Encounter"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdministrableProductDefinition"
    assert inst.resource[3].code == "AdverseEvent"
    assert inst.resource[4].code == "AllergyIntolerance"
    assert inst.resource[5].code == "Appointment"
    assert inst.resource[6].code == "AppointmentResponse"
    assert inst.resource[7].code == "AuditEvent"
    assert inst.resource[8].code == "Basic"
    assert inst.resource[9].code == "Binary"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/encounter"}
        ).valueUri
    )
    assert inst.version == "4.3.0"


def test_compartmentdefinition_5(base_settings):
    """No. 5 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-encounter.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "compartmentdefinition-encounter.json"
    )
    inst = compartmentdefinition.CompartmentDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "CompartmentDefinition" == inst.get_resource_type()

    impl_compartmentdefinition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CompartmentDefinition" == data["resourceType"]

    inst2 = compartmentdefinition.CompartmentDefinition(**data)
    impl_compartmentdefinition_5(inst2)


def impl_compartmentdefinition_6(inst):
    assert inst.code == "Device"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-05-28T12:47:40+10:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "There is an instance of the device compartment for each "
        "Device resource, and the identity of the compartment is the "
        "same as the Device. The set of resources associated with a "
        "particular device"
    )
    assert inst.experimental is True
    assert inst.id == "device"
    assert inst.name == "Base FHIR compartment definition for Device"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[0].param[0] == "subject"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdministrableProductDefinition"
    assert inst.resource[3].code == "AdverseEvent"
    assert inst.resource[4].code == "AllergyIntolerance"
    assert inst.resource[5].code == "Appointment"
    assert inst.resource[5].param[0] == "actor"
    assert inst.resource[6].code == "AppointmentResponse"
    assert inst.resource[6].param[0] == "actor"
    assert inst.resource[7].code == "AuditEvent"
    assert inst.resource[7].param[0] == "agent"
    assert inst.resource[8].code == "Basic"
    assert inst.resource[9].code == "Binary"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/device"}
        ).valueUri
    )
    assert inst.version == "4.3.0"


def test_compartmentdefinition_6(base_settings):
    """No. 6 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-device.json
    """
    filename = base_settings["unittest_data_dir"] / "compartmentdefinition-device.json"
    inst = compartmentdefinition.CompartmentDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "CompartmentDefinition" == inst.get_resource_type()

    impl_compartmentdefinition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CompartmentDefinition" == data["resourceType"]

    inst2 = compartmentdefinition.CompartmentDefinition(**data)
    impl_compartmentdefinition_6(inst2)
