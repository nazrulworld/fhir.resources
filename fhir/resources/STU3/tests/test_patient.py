# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import patient


def impl_patient_1(inst):
    assert inst.active is True
    assert inst.address[0].city == "Metropolis"
    assert inst.address[0].country == "USA"
    assert inst.address[0].line[0] == "100 Main St"
    assert inst.address[0].postalCode == "44130"
    assert inst.address[0].state == "Il"
    assert inst.birthDate == fhirtypes.Date.validate("1956-05-27")
    assert inst.gender == "male"
    assert inst.id == "xds"
    assert inst.identifier[0].system == "urn:oid:1.2.3.4.5"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://hl7.org/fhir/v2/0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "89765a87b"
    assert inst.managingOrganization.reference == "Organization/2"
    assert inst.name[0].family == "Doe"
    assert inst.name[0].given[0] == "John"
    assert inst.text.status == "generated"


def test_patient_1(base_settings):
    """No. 1 tests collection for Patient.
    Test File: patient-example-xds.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-xds.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
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
    assert inst.birthDate == fhirtypes.Date.validate("1944-11-17")
    assert inst.communication[0].language.coding[0].code == "nl"
    assert inst.communication[0].language.coding[0].display == "Dutch"
    assert inst.communication[0].language.coding[0].system == "urn:ietf:bcp:47"
    assert inst.communication[0].language.text == "Nederlands"
    assert inst.communication[0].preferred is True
    assert inst.contact[0].name.family == "Abels"
    assert inst.contact[0].name.given[0] == "Sarah"
    assert inst.contact[0].name.use == "usual"
    assert inst.contact[0].relationship[0].coding[0].code == "C"
    assert (
        inst.contact[0].relationship[0].coding[0].system
        == "http://hl7.org/fhir/v2/0131"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "mobile"
    assert inst.contact[0].telecom[0].value == "0690383372"
    assert inst.deceasedBoolean is False
    assert inst.gender == "male"
    assert inst.id == "f001"
    assert inst.identifier[0].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "738472983"
    assert inst.identifier[1].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[1].use == "usual"
    assert inst.managingOrganization.display == "Burgers University Medical Centre"
    assert inst.managingOrganization.reference == "Organization/f001"
    assert inst.maritalStatus.coding[0].code == "M"
    assert inst.maritalStatus.coding[0].display == "Married"
    assert inst.maritalStatus.coding[0].system == "http://hl7.org/fhir/v3/MaritalStatus"
    assert inst.maritalStatus.text == "Getrouwd"
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
    assert inst.text.status == "generated"


def test_patient_2(base_settings):
    """No. 2 tests collection for Patient.
    Test File: patient-example-f001-pieter.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-f001-pieter.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_2(inst2)


def impl_patient_3(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("1982-08-02")
    assert inst.deceasedBoolean is True
    assert inst.gender == "female"
    assert inst.id == "pat4"
    assert inst.identifier[0].system == "urn:oid:0.1.2.3.4.5.6.7"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://hl7.org/fhir/v2/0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123458"
    assert inst.managingOrganization.display == "ACME Healthcare, Inc"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.name[0].family == "Notsowell"
    assert inst.name[0].given[0] == "Sandy"
    assert inst.name[0].use == "official"
    assert inst.text.status == "generated"


def test_patient_3(base_settings):
    """No. 3 tests collection for Patient.
    Test File: patient-example-d.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-d.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_3(inst2)


def impl_patient_4(inst):
    assert inst.active is True
    assert inst.address[0].line[0] == "2222 Home Street"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1973-05-31")
    assert inst.gender == "female"
    assert inst.id == "genetics-example1"
    assert inst.identifier[0].system == "http://hl7.org/fhir/sid/us-ssn"
    assert inst.identifier[0].type.coding[0].code == "SS"
    assert inst.identifier[0].type.coding[0].system == "http://hl7.org/fhir/v2/0203"
    assert inst.identifier[0].value == "444222222"
    assert inst.managingOrganization.reference == "Organization/hl7"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2012-05-29T23:45:32Z")
    assert inst.name[0].family == "Everywoman"
    assert inst.name[0].given[0] == "Eve"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "555-555-2003"
    assert inst.text.status == "generated"


def test_patient_4(base_settings):
    """No. 4 tests collection for Patient.
    Test File: patient-genetics-example1.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-genetics-example1.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_4(inst2)


def impl_patient_5(inst):
    assert inst.active is True
    assert inst.gender == "other"
    assert inst.id == "pat2"
    assert inst.identifier[0].system == "urn:oid:0.1.2.3.4.5.6.7"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://hl7.org/fhir/v2/0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123456"
    assert inst.link[0].other.reference == "Patient/pat1"
    assert inst.link[0].type == "seealso"
    assert inst.managingOrganization.display == "ACME Healthcare, Inc"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.name[0].family == "Donald"
    assert inst.name[0].given[0] == "Duck"
    assert inst.name[0].given[1] == "D"
    assert inst.name[0].use == "official"
    assert inst.photo[0].contentType == "image/gif"
    assert inst.text.status == "generated"


def test_patient_5(base_settings):
    """No. 5 tests collection for Patient.
    Test File: patient-example-b.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-b.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_5(inst2)


def impl_patient_6(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("1982-01-23")
    assert inst.deceasedDateTime == fhirtypes.DateTime.validate(
        "2015-02-14T13:42:00+10:00"
    )
    assert inst.gender == "male"
    assert inst.id == "pat3"
    assert inst.identifier[0].system == "urn:oid:0.1.2.3.4.5.6.7"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://hl7.org/fhir/v2/0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123457"
    assert inst.managingOrganization.display == "ACME Healthcare, Inc"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.name[0].family == "Notsowell"
    assert inst.name[0].given[0] == "Simon"
    assert inst.name[0].use == "official"
    assert inst.text.status == "generated"


def test_patient_6(base_settings):
    """No. 6 tests collection for Patient.
    Test File: patient-example-c.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-c.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_6(inst2)


def impl_patient_7(inst):
    assert inst.active is True
    assert inst.id == "ihe-pcd"
    assert inst.identifier[0].type.text == "Internal Identifier"
    assert inst.identifier[0].value == "AB60001"
    assert inst.name[0].family == "BROOKS"
    assert inst.name[0].given[0] == "ALBERT"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Albert Brooks, ' "Id: AB60001</div>"
    )
    assert inst.text.status == "generated"


def test_patient_7(base_settings):
    """No. 7 tests collection for Patient.
    Test File: patient-example-ihe-pcd.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-ihe-pcd.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_7(inst2)


def impl_patient_8(inst):
    assert inst.active is True
    assert inst.address[0].city == "PleasantVille"
    assert inst.address[0].district == "Rainbow"
    assert inst.address[0].line[0] == "534 Erewhon St"
    assert inst.address[0].period.start == fhirtypes.DateTime.validate("1974-12-25")
    assert inst.address[0].postalCode == "3999"
    assert inst.address[0].state == "Vic"
    assert inst.address[0].text == "534 Erewhon St PeasantVille, Rainbow, Vic  3999"
    assert inst.address[0].type == "both"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1974-12-25")
    assert inst.contact[0].address.city == "PleasantVille"
    assert inst.contact[0].address.district == "Rainbow"
    assert inst.contact[0].address.line[0] == "534 Erewhon St"
    assert inst.contact[0].address.period.start == fhirtypes.DateTime.validate(
        "1974-12-25"
    )
    assert inst.contact[0].address.postalCode == "3999"
    assert inst.contact[0].address.state == "Vic"
    assert inst.contact[0].address.type == "both"
    assert inst.contact[0].address.use == "home"
    assert inst.contact[0].gender == "female"
    assert inst.contact[0].name.family == "du Marché"
    assert inst.contact[0].name.given[0] == "Bénédicte"
    assert inst.contact[0].period.start == fhirtypes.DateTime.validate("2012")
    assert inst.contact[0].relationship[0].coding[0].code == "N"
    assert (
        inst.contact[0].relationship[0].coding[0].system
        == "http://hl7.org/fhir/v2/0131"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "+33 (237) 998327"
    assert inst.deceasedBoolean is False
    assert inst.gender == "male"
    assert inst.id == "example"
    assert inst.identifier[0].assigner.display == "Acme Healthcare"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2001-05-06")
    assert inst.identifier[0].system == "urn:oid:1.2.36.146.595.217.0.1"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://hl7.org/fhir/v2/0203"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "12345"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.name[0].family == "Chalmers"
    assert inst.name[0].given[0] == "Peter"
    assert inst.name[0].given[1] == "James"
    assert inst.name[0].use == "official"
    assert inst.name[1].given[0] == "Jim"
    assert inst.name[1].use == "usual"
    assert inst.name[2].family == "Windsor"
    assert inst.name[2].given[0] == "Peter"
    assert inst.name[2].given[1] == "James"
    assert inst.name[2].period.end == fhirtypes.DateTime.validate("2002")
    assert inst.name[2].use == "maiden"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[1].rank == 1
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "(03) 5555 6473"
    assert inst.telecom[2].rank == 2
    assert inst.telecom[2].system == "phone"
    assert inst.telecom[2].use == "mobile"
    assert inst.telecom[2].value == "(03) 3410 5613"
    assert inst.telecom[3].period.end == fhirtypes.DateTime.validate("2014")
    assert inst.telecom[3].system == "phone"
    assert inst.telecom[3].use == "old"
    assert inst.telecom[3].value == "(03) 5555 8834"
    assert inst.text.status == "generated"


def test_patient_8(base_settings):
    """No. 8 tests collection for Patient.
    Test File: patient-example.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_8(inst2)


def impl_patient_9(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("1966-04-04")
    assert inst.deceasedBoolean is False
    assert inst.gender == "female"
    assert inst.id == "proband"
    assert (
        inst.identifier[0].assigner.display == "Boston Massachesetts General Hospital"
    )
    assert inst.identifier[0].system == "urn:oid:2.16.840.1.113883.6.117"
    assert inst.identifier[0].type.text == "Computer-Stored Abulatory Records (COSTAR)"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "999999999"
    assert inst.text.status == "generated"


def test_patient_9(base_settings):
    """No. 9 tests collection for Patient.
    Test File: patient-example-proband.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-proband.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_9(inst2)


def impl_patient_10(inst):
    assert inst.active is True
    assert inst.address[0].city == "Amsterdam"
    assert inst.address[0].country == "NLD"
    assert inst.address[0].line[0] == "Bos en Lommerplein 280"
    assert inst.address[0].postalCode == "1055RW"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1960-03-13")
    assert inst.communication[0].language.coding[0].code == "nl-NL"
    assert inst.communication[0].language.coding[0].display == "Dutch"
    assert inst.communication[0].language.coding[0].system == "urn:ietf:bcp:47"
    assert inst.communication[0].preferred is True
    assert inst.contact[0].name.text == "Ariadne Bor-Jansma"
    assert inst.contact[0].name.use == "usual"
    assert inst.contact[0].relationship[0].coding[0].code == "127850001"
    assert inst.contact[0].relationship[0].coding[0].display == "Wife"
    assert inst.contact[0].relationship[0].coding[0].system == "http://snomed.info/sct"
    assert inst.contact[0].relationship[0].coding[1].code == "N"
    assert (
        inst.contact[0].relationship[0].coding[1].system
        == "http://hl7.org/fhir/v2/0131"
    )
    assert inst.contact[0].relationship[0].coding[2].code == "WIFE"
    assert (
        inst.contact[0].relationship[0].coding[2].system
        == "http://hl7.org/fhir/v3/RoleCode"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "home"
    assert inst.contact[0].telecom[0].value == "+31201234567"
    assert inst.deceasedBoolean is False
    assert inst.gender == "male"
    assert inst.id == "f201"
    assert inst.identifier[0].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[0].type.text == "BSN"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "123456789"
    assert inst.identifier[1].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[1].type.text == "BSN"
    assert inst.identifier[1].use == "official"
    assert inst.identifier[1].value == "123456789"
    assert inst.managingOrganization.display == "AUMC"
    assert inst.managingOrganization.reference == "Organization/f201"
    assert inst.maritalStatus.coding[0].code == "36629006"
    assert inst.maritalStatus.coding[0].display == "Legally married"
    assert inst.maritalStatus.coding[0].system == "http://snomed.info/sct"
    assert inst.maritalStatus.coding[1].code == "M"
    assert inst.maritalStatus.coding[1].system == "http://hl7.org/fhir/v3/MaritalStatus"
    assert inst.multipleBirthBoolean is False
    assert inst.name[0].family == "Bor"
    assert inst.name[0].given[0] == "Roelof Olaf"
    assert inst.name[0].prefix[0] == "Drs."
    assert inst.name[0].suffix[0] == "PDEng."
    assert inst.name[0].text == "Roel"
    assert inst.name[0].use == "official"
    assert inst.photo[0].contentType == "image/jpeg"
    assert inst.photo[0].url == "Binary/f006"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "mobile"
    assert inst.telecom[0].value == "+31612345678"
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "home"
    assert inst.telecom[1].value == "+31201234567"
    assert inst.text.status == "generated"


def test_patient_10(base_settings):
    """No. 10 tests collection for Patient.
    Test File: patient-example-f201-roel.json
    """
    filename = base_settings["unittest_data_dir"] / "patient-example-f201-roel.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type

    impl_patient_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_patient_10(inst2)
