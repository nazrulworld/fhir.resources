# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import patient
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_patient_1(inst):
    assert inst.active is True
    assert inst.address[0].city == "Metropolis"
    assert inst.address[0].country == "USA"
    assert inst.address[0].line[0] == "100 Main St"
    assert inst.address[0].postalCode == "44130"
    assert inst.address[0].state == "Il"
    assert (
        inst.birthDate
        == ExternalValidatorModel.model_validate({"valueDate": "1956-05-27"}).valueDate
    )
    assert inst.gender == "male"
    assert inst.id == "xds"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:1.2.3.4.5"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "89765a87b"
    assert inst.managingOrganization.reference == "Organization/2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name[0].family == "Doe"
    assert inst.name[0].given[0] == "John"
    assert inst.text.status == "generated"


def test_patient_1(base_settings):
    """No. 1 tests collection for Patient.
    Test File: patient-example-xds.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-xds.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_1(inst2)


def impl_patient_2(inst):
    assert inst.active is True
    assert inst.address[0].city == "Amsterdam"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Van Egmondkade 23"
    assert inst.address[0].postalCode == "1024 RJ"
    assert inst.address[0].use == "home"
    assert (
        inst.birthDate
        == ExternalValidatorModel.model_validate({"valueDate": "1944-11-17"}).valueDate
    )
    assert inst.communication[0].language.coding[0].code == "nl"
    assert inst.communication[0].language.coding[0].display == "Dutch"
    assert (
        inst.communication[0].language.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:bcp:47"}
        ).valueUri
    )
    assert inst.communication[0].language.text == "Nederlands"
    assert inst.communication[0].preferred is True
    assert inst.contact[0].name.family == "Abels"
    assert inst.contact[0].name.given[0] == "Sarah"
    assert inst.contact[0].name.use == "usual"
    assert inst.contact[0].relationship[0].coding[0].code == "C"
    assert (
        inst.contact[0].relationship[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0131"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "mobile"
    assert inst.contact[0].telecom[0].value == "0690383372"
    assert inst.deceasedBoolean is False
    assert inst.gender == "male"
    assert inst.id == "f001"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:2.16.840.1.113883.2.4.6.3"}
        ).valueUri
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "738472983"
    assert (
        inst.identifier[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:2.16.840.1.113883.2.4.6.3"}
        ).valueUri
    )
    assert inst.identifier[1].use == "usual"
    assert inst.managingOrganization.display == "Burgers University Medical Centre"
    assert inst.managingOrganization.reference == "Organization/f001"
    assert inst.maritalStatus.coding[0].code == "M"
    assert inst.maritalStatus.coding[0].display == "Married"
    assert (
        inst.maritalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"}
        ).valueUri
    )
    assert inst.maritalStatus.text == "Getrouwd"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.multipleBirthBoolean is True
    assert inst.name[0].family == "van de Heuvel"
    assert inst.name[0].given[0] == "Pieter"
    assert inst.name[0].suffix[0] == "MSc"
    assert inst.name[0].use == "usual"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "mobile"
    assert inst.telecom[0].value == "0648352638"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "home"
    assert inst.telecom[1].value == "p.heuvel@gmail.com"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Pieter van'
        " de Heuvel </b> male, DoB: 1944-11-17 ( id: 738472983 "
        "(USUAL))</p></div>"
    )
    assert inst.text.status == "generated"


def test_patient_2(base_settings):
    """No. 2 tests collection for Patient.
    Test File: patient-example-f001-pieter.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-f001-pieter.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_2(inst2)


def impl_patient_3(inst):
    assert inst.active is True
    assert (
        inst.birthDate
        == ExternalValidatorModel.model_validate({"valueDate": "1982-08-02"}).valueDate
    )
    assert inst.deceasedBoolean is True
    assert inst.gender == "female"
    assert inst.id == "pat4"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:0.1.2.3.4.5.6.7"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123458"
    assert inst.managingOrganization.display == "ACME Healthcare, Inc"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name[0].family == "Notsowell"
    assert inst.name[0].given[0] == "Sandy"
    assert inst.name[0].use == "official"
    assert inst.text.status == "generated"


def test_patient_3(base_settings):
    """No. 3 tests collection for Patient.
    Test File: patient-example-d.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-d.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_3(inst2)


def impl_patient_4(inst):
    assert (
        inst.birthDate
        == ExternalValidatorModel.model_validate({"valueDate": "2017-05-15"}).valueDate
    )
    assert inst.contact[0].name.family == "Organa"
    assert inst.contact[0].name.given[0] == "Leia"
    assert inst.contact[0].name.use == "maiden"
    assert inst.contact[0].relationship[0].coding[0].code == "72705000"
    assert inst.contact[0].relationship[0].coding[0].display == "Mother"
    assert (
        inst.contact[0].relationship[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.contact[0].relationship[0].coding[1].code == "N"
    assert (
        inst.contact[0].relationship[0].coding[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0131"}
        ).valueUri
    )
    assert inst.contact[0].relationship[0].coding[2].code == "MTH"
    assert (
        inst.contact[0].relationship[0].coding[2].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "mobile"
    assert inst.contact[0].telecom[0].value == "+31201234567"
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Organa"
    assert inst.gender == "female"
    assert inst.id == "infant-twin-1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://coruscanthealth.org/main-hospital/patient-identifier"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.identifier[0].value == "MRN7465737865"
    assert (
        inst.identifier[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://new-republic.gov/galactic-citizen-identifier"}
        ).valueUri
    )
    assert inst.identifier[1].value == "7465737865"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.multipleBirthInteger == 1
    assert inst.name[0].family == "Solo"
    assert inst.name[0].given[0] == "Jaina"
    assert inst.name[0].use == "official"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Jaina Solo'
        " (OFFICIAL)</b> female, DoB: 2017-05-15 ( Medical record "
        "number: MRN7465737865)</p></div>"
    )
    assert inst.text.status == "generated"


def test_patient_4(base_settings):
    """No. 4 tests collection for Patient.
    Test File: patient-example-infant-twin-1.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-infant-twin-1.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_4(inst2)


def impl_patient_5(inst):
    assert (
        inst.birthDate
        == ExternalValidatorModel.model_validate({"valueDate": "1995-10-12"}).valueDate
    )
    assert inst.gender == "female"
    assert inst.generalPractitioner[0].display == "Too-Onebee"
    assert inst.generalPractitioner[0].reference == "Practitioner/21B"
    assert inst.id == "infant-mom"
    assert inst.maritalStatus.coding[0].code == "M"
    assert inst.maritalStatus.coding[0].display == "Married"
    assert (
        inst.maritalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"}
        ).valueUri
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name[0].family == "Solo"
    assert inst.name[0].given[0] == "Leia"
    assert inst.name[0].use == "official"
    assert inst.name[1].family == "Organa"
    assert inst.name[1].given[0] == "Leia"
    assert inst.name[1].use == "maiden"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Leia Solo '
        "(OFFICIAL)</b> female, DoB: 1995-10-12</p></div>"
    )
    assert inst.text.status == "generated"


def test_patient_5(base_settings):
    """No. 5 tests collection for Patient.
    Test File: patient-example-infant-mom.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-infant-mom.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_5(inst2)


def impl_patient_6(inst):
    assert (
        inst.birthDate
        == ExternalValidatorModel.model_validate({"valueDate": "2017-09-05"}).valueDate
    )
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Everywoman"
    assert inst.gender == "male"
    assert inst.id == "newborn"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.multipleBirthInteger == 2
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Anonymous '
        "Patient</b> male, DoB: 2017-09-05</p></div>"
    )
    assert inst.text.status == "generated"


def test_patient_6(base_settings):
    """No. 6 tests collection for Patient.
    Test File: patient-example-newborn.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-newborn.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_6(inst2)


def impl_patient_7(inst):
    assert inst.contact[0].name.family == "Organa"
    assert inst.contact[0].name.given[0] == "Leia"
    assert inst.contact[0].name.use == "maiden"
    assert inst.contact[0].relationship[0].coding[0].code == "72705000"
    assert inst.contact[0].relationship[0].coding[0].display == "Mother"
    assert (
        inst.contact[0].relationship[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.contact[0].relationship[0].coding[1].code == "N"
    assert (
        inst.contact[0].relationship[0].coding[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0131"}
        ).valueUri
    )
    assert inst.contact[0].relationship[0].coding[2].code == "MTH"
    assert (
        inst.contact[0].relationship[0].coding[2].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "mobile"
    assert inst.contact[0].telecom[0].value == "+31201234567"
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Organa"
    assert inst.gender == "male"
    assert inst.id == "infant-fetal"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://coruscanthealth.org/main-hospital/patient-identifier"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.identifier[0].value == "MRN657865757378"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Anonymous '
        "Patient</b> male, DoB Unknown ( Medical record number: "
        "MRN657865757378)</p></div>"
    )
    assert inst.text.status == "generated"


def test_patient_7(base_settings):
    """No. 7 tests collection for Patient.
    Test File: patient-example-infant-fetal.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-infant-fetal.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_7(inst2)


def impl_patient_8(inst):
    assert inst.active is True
    assert inst.address[0].line[0] == "2222 Home Street"
    assert inst.address[0].use == "home"
    assert (
        inst.birthDate
        == ExternalValidatorModel.model_validate({"valueDate": "1973-05-31"}).valueDate
    )
    assert inst.gender == "female"
    assert inst.id == "genetics-example1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/sid/us-ssn"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "SS"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.identifier[0].value == "444222222"
    assert inst.managingOrganization.reference == "Organization/hl7"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2012-05-29T23:45:32Z"}
        ).valueInstant
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name[0].family == "Everywoman"
    assert inst.name[0].given[0] == "Eve"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "555-555-2003"
    assert inst.text.status == "generated"


def test_patient_8(base_settings):
    """No. 8 tests collection for Patient.
    Test File: patient-genetics-example1.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-genetics-example1.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_8(inst2)


def impl_patient_9(inst):
    assert inst.active is True
    assert inst.gender == "other"
    assert inst.id == "pat2"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:0.1.2.3.4.5.6.7"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123456"
    assert inst.link[0].other.reference == "Patient/pat1"
    assert inst.link[0].type == "seealso"
    assert inst.managingOrganization.display == "ACME Healthcare, Inc"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name[0].family == "Donald"
    assert inst.name[0].given[0] == "Duck"
    assert inst.name[0].given[1] == "D"
    assert inst.name[0].use == "official"
    assert inst.photo[0].contentType == "image/gif"
    assert inst.text.status == "generated"


def test_patient_9(base_settings):
    """No. 9 tests collection for Patient.
    Test File: patient-example-b.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-b.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_9(inst2)


def impl_patient_10(inst):
    assert inst.active is True
    assert (
        inst.birthDate
        == ExternalValidatorModel.model_validate({"valueDate": "1982-01-23"}).valueDate
    )
    assert (
        inst.deceasedDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-02-14T13:42:00+10:00"}
        ).valueDateTime
    )
    assert inst.gender == "male"
    assert inst.id == "pat3"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:0.1.2.3.4.5.6.7"}
        ).valueUri
    )
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123457"
    assert inst.managingOrganization.display == "ACME Healthcare, Inc"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name[0].family == "Notsowell"
    assert inst.name[0].given[0] == "Simon"
    assert inst.name[0].use == "official"
    assert inst.text.status == "generated"


def test_patient_10(base_settings):
    """No. 10 tests collection for Patient.
    Test File: patient-example-c.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-c.json"
    inst = patient.Patient.model_validate_json(filename.read_bytes())
    assert "Patient" == inst.get_resource_type()

    impl_patient_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_10(inst2)
