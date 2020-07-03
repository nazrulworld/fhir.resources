# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from .. import fhirtypes  # noqa: F401
from .. import patient


def test_Patient_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-glossy-example.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_1(inst2)


def impl_Patient_1(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("1932-09-24")

    assert inst.extension[0].url == ("http://example.org/StructureDefinition/trials")
    assert inst.extension[0].valueCode == "renal"
    assert inst.gender == "male"
    assert inst.id == "glossy"
    assert inst.identifier[0].system == ("http://www.goodhealth.org/identifiers/mrn")
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == ("http://hl7.org/fhir/v2/0203")
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123456"
    assert inst.meta.lastUpdated == fhirtypes.DateTime.validate(
        "2014-11-13T11:41:00+11:00"
    )

    assert inst.name[0].family[0] == "Levin"
    assert inst.name[0].given[0] == "Henry"
    assert inst.name[0].suffix[0] == "The 7th"
    assert inst.text.status == "generated"


def test_Patient_2(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-example-animal.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_2(inst2)


def impl_Patient_2(inst):
    assert inst.active is True
    assert inst.animal.breed.coding[0].code == "58108001"
    assert inst.animal.breed.coding[0].display == "Golden retriever"
    assert inst.animal.breed.coding[0].system == "http://snomed.info/sct"
    assert inst.animal.breed.coding[1].code == "gret"
    assert inst.animal.breed.coding[1].display == "Golden Retriever"
    assert inst.animal.breed.coding[1].system == ("http://hl7.org/fhir/animal-breed")
    assert inst.animal.genderStatus.coding[0].code == "neutered"
    assert inst.animal.genderStatus.coding[0].system == (
        "http://hl7.org/fhir/animal-genderstatus"
    )
    assert inst.animal.species.coding[0].code == "canislf"
    assert inst.animal.species.coding[0].display == "Dog"
    assert inst.animal.species.coding[0].system == (
        "http://hl7.org/fhir/animal-species"
    )
    assert inst.birthDate == fhirtypes.Date.validate("2010-03-23")

    assert inst.contact[0].name.family[0] == "Chalmers"
    assert inst.contact[0].name.given[0] == "Peter"
    assert inst.contact[0].name.given[1] == "James"
    assert inst.contact[0].relationship[0].coding[0].code == "owner"
    assert inst.contact[0].relationship[0].coding[0].system == (
        "http://hl7.org/fhir/patient-contact-relationship"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "(03) 5555 6473"
    assert inst.gender == "female"
    assert inst.id == "animal"
    assert inst.identifier[0].period.start == fhirtypes.Date.validate("2010-05-31")

    assert inst.identifier[0].system == (
        "http://www.maroondah.vic.gov.au/AnimalRegFees.aspx"
    )
    assert inst.identifier[0].type.text == "Dog Tag"
    assert inst.identifier[0].value == "1234123"
    assert inst.name[0].given[0] == "Kenzi"
    assert inst.name[0].use == "usual"
    assert inst.text.status == "generated"


def test_Patient_3(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-example-f201-roel.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_3(inst2)


def impl_Patient_3(inst):
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
    assert inst.contact[0].relationship[0].coding[0].system == (
        "http://snomed.info/sct"
    )
    assert inst.contact[0].relationship[0].coding[1].code == "partner"
    assert inst.contact[0].relationship[0].coding[1].system == (
        "http://hl7.org/fhir/patient-contact-relationship"
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
    assert inst.maritalStatus.coding[0].code == "36629006"
    assert inst.maritalStatus.coding[0].display == "Legally married"
    assert inst.maritalStatus.coding[0].system == "http://snomed.info/sct"
    assert inst.maritalStatus.coding[1].code == "M"
    assert inst.maritalStatus.coding[1].system == (
        "http://hl7.org/fhir/v3/MaritalStatus"
    )
    assert inst.multipleBirthBoolean is False
    assert inst.name[0].family[0] == "Bor"
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


def test_Patient_4(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-example-us-extensions.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_4(inst2)


def impl_Patient_4(inst):
    assert inst.active is True
    assert inst.address[0].city == "PleasantVille"
    assert inst.address[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/us-core-county"
    )
    assert inst.address[0].extension[0].valueString == "Orange County"
    assert inst.address[0].line[0] == "534 Erewhon St"
    assert inst.address[0].postalCode == "3999"
    assert inst.address[0].state == "Vic"
    assert inst.address[0].use == "home"
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/us-core-race"
    )
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "1096-7"
    assert inst.extension[0].valueCodeableConcept.coding[0].system == (
        "http://hl7.org/fhir/v3/Race"
    )
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/us-core-ethnicity"
    )
    assert inst.extension[1].valueCodeableConcept.coding[0].code == "2162-6"
    assert inst.extension[1].valueCodeableConcept.coding[0].system == (
        "http://hl7.org/fhir/v3/Ethnicity"
    )
    assert inst.id == "us01"
    assert inst.name[0].family[0] == "Chalmers"
    assert inst.name[0].given[0] == "Peter"
    assert inst.name[0].given[1] == "James"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "(03) 5555 6473"
    assert inst.telecom[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/us-core-direct"
    )
    assert inst.telecom[1].extension[0].valueBoolean is True
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "person@example.org"
    assert inst.text.status == "generated"


def test_Patient_5(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-example-b.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_5(inst2)


def impl_Patient_5(inst):
    assert inst.active is True
    assert inst.gender == "other"
    assert inst.id == "pat2"
    assert inst.identifier[0].system == "urn:oid:0.1.2.3.4.5.6.7"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == ("http://hl7.org/fhir/v2/0203")
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "123456"
    assert inst.link[0].type == "seealso"
    assert inst.name[0].family[0] == "Donald"
    assert inst.name[0].given[0] == "Duck"
    assert inst.name[0].given[1] == "D"
    assert inst.name[0].use == "official"
    assert inst.photo[0].contentType == "image/gif"
    assert inst.text.status == "generated"


def test_Patient_6(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-example-proband.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_6(inst2)


def impl_Patient_6(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("1966-04-04")

    assert inst.deceasedBoolean is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/us-core-race"
    )
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "2106-3"
    assert inst.extension[0].valueCodeableConcept.coding[0].display == "white"
    assert inst.extension[0].valueCodeableConcept.coding[0].system == (
        "urn:oid:2.16.840.1.113883.6.238"
    )
    assert inst.gender == "female"
    assert inst.id == "proband"
    assert inst.identifier[0].system == "urn:oid:2.16.840.1.113883.6.117"
    assert inst.identifier[0].type.text == (
        "Computer-Stored Abulatory Records (COSTAR)"
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "999999999"
    assert inst.text.status == "generated"


def test_Patient_7(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-example-c.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_7(inst2)


def impl_Patient_7(inst):
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
    assert inst.name[0].family[0] == "Notsowell"
    assert inst.name[0].given[0] == "Simon"
    assert inst.name[0].use == "official"
    assert inst.text.status == "generated"


def offtest_Patient_8(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-example.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_8(inst2)


def impl_Patient_8(inst):
    assert inst.active is True
    assert inst.address[0].city == "PleasantVille"
    assert inst.address[0].district == "Rainbow"
    assert inst.address[0].line[0] == "534 Erewhon St"
    assert inst.address[0].period.start == fhirtypes.Date.validate("1974-12-25")

    assert inst.address[0].postalCode == "3999"
    assert inst.address[0].state == "Vic"
    assert inst.address[0].type == "both"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1974-12-25")

    assert inst.contact[0].gender == "female"
    assert inst.contact[0].name.family[0] == "du"
    assert inst.contact[0].name.family[1] == "Marché"
    assert inst.contact[0].name.given[0] == "Bénédicte"
    assert inst.contact[0].period.start == fhirtypes.Date.validate("2012")
    assert inst.contact[0].relationship[0].coding[0].code == "partner"
    assert inst.contact[0].relationship[0].coding[0].system == (
        "http://hl7.org/fhir/patient-contact-relationship"
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].value == "+33 (237) 998327"
    assert inst.deceasedBoolean is False
    assert inst.gender == "male"
    assert inst.id == "example"
    assert inst.identifier[0].period.start == fhirtypes.Date.validate("2001-05-06")

    assert inst.identifier[0].system == "urn:oid:1.2.36.146.595.217.0.1"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://hl7.org/fhir/v2/0203"

    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "12345"
    assert inst.name[0].family[0] == "Chalmers"
    assert inst.name[0].given[0] == "Peter"
    assert inst.name[0].given[1] == "James"
    assert inst.name[0].use == "official"
    assert inst.name[1].given[0] == "Jim"
    assert inst.name[1].use == "usual"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "(03) 5555 6473"
    assert inst.text.status == "generated"


def test_Patient_9(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-example-a.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_9(inst2)


def impl_Patient_9(inst):
    assert inst.active is True
    assert inst.contact[0].relationship[0].coding[0].code == "owner"
    assert inst.contact[0].relationship[0].coding[0].system == (
        "http://hl7.org/fhir/patient-contact-relationship"
    )
    assert inst.gender == "male"
    assert inst.id == "pat1"
    assert inst.identifier[0].system == "urn:oid:0.1.2.3.4.5.6.7"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert inst.identifier[0].type.coding[0].system == "http://hl7.org/fhir/v2/0203"

    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "654321"
    assert inst.link[0].type == "seealso"
    assert inst.name[0].family[0] == "Donald"
    assert inst.name[0].given[0] == "Duck"
    assert inst.name[0].use == "official"
    assert inst.photo[0].contentType == "image/gif"
    assert inst.text.status == "generated"


def test_Patient_10(base_settings):
    filename = base_settings["unittest_data_dir"] / "patient-example-dicom.json"
    inst = patient.Patient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Patient" == inst.resource_type
    impl_Patient_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Patient" == data["resourceType"]

    inst2 = patient.Patient(**data)
    impl_Patient_10(inst2)


def impl_Patient_10(inst):
    assert inst.active is True
    assert inst.extension[0].url == "http://nema.org/fhir/extensions#0010:1010"
    assert inst.extension[0].valueQuantity.unit == "Y"
    assert inst.extension[0].valueQuantity.value == 56
    assert inst.extension[1].url == "http://nema.org/fhir/extensions#0010:1020"
    assert inst.extension[1].valueQuantity.unit == "m"
    assert float(inst.extension[1].valueQuantity.value) == 1.83
    assert inst.extension[2].url == "http://nema.org/fhir/extensions#0010:1030"
    assert inst.extension[2].valueQuantity.unit == "kg"
    assert float(inst.extension[2].valueQuantity.value) == 72.58
    assert inst.gender == "male"
    assert inst.id == "dicom"
    assert inst.identifier[0].system == "http://nema.org/examples/patients"
    assert inst.identifier[0].value == "MINT1234"
    assert inst.name[0].family[0] == "MINT_TEST"
    assert inst.text.status == "generated"
