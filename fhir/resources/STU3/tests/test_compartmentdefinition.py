# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CompartmentDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from .. import compartmentdefinition
from .fixtures import ExternalValidatorModel


def impl_compartmentdefinition_1(inst):
    assert inst.code == "RelatedPerson"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.id == "relatedPerson"
    assert inst.name == "Base FHIR compartment definition for RelatedPerson"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdverseEvent"
    assert inst.resource[2].param[0] == "recorder"
    assert inst.resource[3].code == "AllergyIntolerance"
    assert inst.resource[3].param[0] == "asserter"
    assert inst.resource[4].code == "Appointment"
    assert inst.resource[4].param[0] == "actor"
    assert inst.resource[5].code == "AppointmentResponse"
    assert inst.resource[5].param[0] == "actor"
    assert inst.resource[6].code == "AuditEvent"
    assert inst.resource[7].code == "Basic"
    assert inst.resource[7].param[0] == "author"
    assert inst.resource[8].code == "Binary"
    assert inst.resource[9].code == "BodySite"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/relatedPerson"}
        ).valueUri
    )


def test_compartmentdefinition_1(base_settings):
    """No. 1 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-compartmentdefinition-relatedperson(relatedPerson).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "compartmentdefinition-compartmentdefinition-relatedperson(relatedPerson).json"
    )
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
    assert inst.code == "Patient"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.id == "patient"
    assert inst.name == "Base FHIR compartment definition for Patient"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[0].param[0] == "subject"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdverseEvent"
    assert inst.resource[2].param[0] == "subject"
    assert inst.resource[3].code == "AllergyIntolerance"
    assert inst.resource[3].param[0] == "patient"
    assert inst.resource[3].param[1] == "recorder"
    assert inst.resource[3].param[2] == "asserter"
    assert inst.resource[4].code == "Appointment"
    assert inst.resource[4].param[0] == "actor"
    assert inst.resource[5].code == "AppointmentResponse"
    assert inst.resource[5].param[0] == "actor"
    assert inst.resource[6].code == "AuditEvent"
    assert inst.resource[6].param[0] == "patient"
    assert inst.resource[6].param[1] == "agent.patient"
    assert inst.resource[6].param[2] == "entity.patient"
    assert inst.resource[7].code == "Basic"
    assert inst.resource[7].param[0] == "patient"
    assert inst.resource[7].param[1] == "author"
    assert inst.resource[8].code == "Binary"
    assert inst.resource[9].code == "BodySite"
    assert inst.resource[9].param[0] == "patient"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/patient"}
        ).valueUri
    )


def test_compartmentdefinition_2(base_settings):
    """No. 2 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-compartmentdefinition-patient(patient).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "compartmentdefinition-compartmentdefinition-patient(patient).json"
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
    assert inst.code == "Encounter"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.id == "encounter"
    assert inst.name == "Base FHIR compartment definition for Encounter"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdverseEvent"
    assert inst.resource[3].code == "AllergyIntolerance"
    assert inst.resource[4].code == "Appointment"
    assert inst.resource[5].code == "AppointmentResponse"
    assert inst.resource[6].code == "AuditEvent"
    assert inst.resource[7].code == "Basic"
    assert inst.resource[8].code == "Binary"
    assert inst.resource[9].code == "BodySite"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/encounter"}
        ).valueUri
    )


def test_compartmentdefinition_3(base_settings):
    """No. 3 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-compartmentdefinition-encounter(encounter).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "compartmentdefinition-compartmentdefinition-encounter(encounter).json"
    )
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
    assert inst.code == "Device"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "There is an instance of the practitioner compartment for "
        "each Device resource, and the identity of the compartment is"
        " the same as the Device. The set of resources associated "
        "with a particular device"
    )
    assert inst.experimental is True
    assert inst.id == "device"
    assert inst.name == "Base FHIR compartment definition for Device"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[0].param[0] == "subject"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdverseEvent"
    assert inst.resource[3].code == "AllergyIntolerance"
    assert inst.resource[4].code == "Appointment"
    assert inst.resource[4].param[0] == "actor"
    assert inst.resource[5].code == "AppointmentResponse"
    assert inst.resource[5].param[0] == "actor"
    assert inst.resource[6].code == "AuditEvent"
    assert inst.resource[6].param[0] == "agent"
    assert inst.resource[7].code == "Basic"
    assert inst.resource[8].code == "Binary"
    assert inst.resource[9].code == "BodySite"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/device"}
        ).valueUri
    )


def test_compartmentdefinition_4(base_settings):
    """No. 4 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-compartmentdefinition-device(device).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "compartmentdefinition-compartmentdefinition-device(device).json"
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
    assert inst.code == "Practitioner"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.id == "practitioner"
    assert inst.name == "Base FHIR compartment definition for Practitioner"
    assert inst.publisher == "FHIR Project Team"
    assert inst.resource[0].code == "Account"
    assert inst.resource[0].param[0] == "subject"
    assert inst.resource[1].code == "ActivityDefinition"
    assert inst.resource[2].code == "AdverseEvent"
    assert inst.resource[2].param[0] == "recorder"
    assert inst.resource[3].code == "AllergyIntolerance"
    assert inst.resource[3].param[0] == "recorder"
    assert inst.resource[3].param[1] == "asserter"
    assert inst.resource[4].code == "Appointment"
    assert inst.resource[4].param[0] == "actor"
    assert inst.resource[5].code == "AppointmentResponse"
    assert inst.resource[5].param[0] == "actor"
    assert inst.resource[6].code == "AuditEvent"
    assert inst.resource[6].param[0] == "agent"
    assert inst.resource[7].code == "Basic"
    assert inst.resource[7].param[0] == "author"
    assert inst.resource[8].code == "Binary"
    assert inst.resource[9].code == "BodySite"
    assert inst.search is True
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CompartmentDefinition/practitioner"}
        ).valueUri
    )


def test_compartmentdefinition_5(base_settings):
    """No. 5 tests collection for CompartmentDefinition.
    Test File: compartmentdefinition-compartmentdefinition-practitioner(practitioner).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "compartmentdefinition-compartmentdefinition-practitioner(practitioner).json"
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
