# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/List
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import list


def impl_list_1(inst):
    assert inst.code.coding[0].code == "182836005"
    assert inst.code.coding[0].display == "Review of medication"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Medication Review"
    assert inst.date == fhirtypes.DateTime.validate("2013-11-20T23:10:23+11:00")
    assert inst.entry[0].flag.coding[0].code == "01"
    assert inst.entry[0].flag.coding[0].display == "Prescribed"
    assert (
        inst.entry[0].flag.coding[0].system
        == "http://nehta.gov.au/codes/medications/changetype"
    )
    assert inst.entry[0].item.display == "hydroxocobalamin"
    assert inst.entry[1].deleted is True
    assert inst.entry[1].flag.coding[0].code == "02"
    assert inst.entry[1].flag.coding[0].display == "Cancelled"
    assert (
        inst.entry[1].flag.coding[0].system
        == "http://nehta.gov.au/codes/medications/changetype"
    )
    assert inst.entry[1].item.display == "Morphine Sulfate"
    assert inst.id == "med-list"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "changes"
    assert inst.source.reference == "Patient/example"
    assert inst.status == "current"
    assert inst.text.status == "generated"


def test_list_1(base_settings):
    """No. 1 tests collection for List.
    Test File: list-example-medlist.json
    """
    filename = base_settings["unittest_data_dir"] / "list-example-medlist.json"
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_1(inst2)


def impl_list_2(inst):
    assert inst.code.coding[0].code == "8670-2"
    assert inst.code.coding[0].display == "History of family member diseases"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.contained[0].id == "image"
    assert inst.contained[1].id == "1"
    assert inst.contained[2].id == "2"
    assert inst.contained[3].id == "3"
    assert inst.contained[4].id == "4"
    assert inst.contained[5].id == "5"
    assert inst.contained[6].id == "6"
    assert inst.contained[7].id == "7"
    assert inst.contained[8].id == "8"
    assert inst.contained[9].id == "9"
    assert inst.entry[0].item.reference == "#image"
    assert inst.entry[1].item.reference == "#2"
    assert inst.entry[2].item.reference == "#3"
    assert inst.entry[3].item.reference == "#4"
    assert inst.entry[4].item.reference == "#5"
    assert inst.entry[5].item.reference == "#6"
    assert inst.entry[6].item.reference == "#7"
    assert inst.entry[7].item.reference == "#8"
    assert inst.entry[8].item.reference == "#9"
    assert inst.entry[9].item.reference == "#10"
    assert inst.id == "prognosis"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "snapshot"
    assert inst.status == "current"
    assert inst.subject.display == "Annie Proband, female, born 1966"
    assert inst.subject.reference == "Patient/proband"
    assert inst.text.status == "generated"


def test_list_2(base_settings):
    """No. 2 tests collection for List.
    Test File: list-example-familyhistory-genetics-profile-annie.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "list-example-familyhistory-genetics-profile-annie.json"
    )
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_2(inst2)


def impl_list_3(inst):
    assert inst.code.coding[0].code == "346638"
    assert inst.code.coding[0].display == "Patient Admission List"
    assert inst.code.coding[0].system == "http://acme.com/list-codes"
    assert inst.date == fhirtypes.DateTime.validate("2016-07-14T11:54:05+10:00")
    assert inst.id == "example-simple-empty"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "snapshot"
    assert inst.status == "current"
    assert inst.text.status == "generated"


def test_list_3(base_settings):
    """No. 3 tests collection for List.
    Test File: list-example-simple-empty.json
    """
    filename = base_settings["unittest_data_dir"] / "list-example-simple-empty.json"
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_3(inst2)


def impl_list_4(inst):
    assert inst.code.coding[0].code == "182836005"
    assert inst.code.coding[0].display == "Review of medication"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Medication Review"
    assert inst.date == fhirtypes.DateTime.validate("2012-11-26T07:30:23+11:00")
    assert inst.emptyReason.coding[0].code == "nilknown"
    assert inst.emptyReason.coding[0].display == "Nil Known"
    assert (
        inst.emptyReason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/list-empty-reason"
    )
    assert inst.emptyReason.text == "The patient is not on any medications"
    assert inst.id == "example-empty"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "snapshot"
    assert inst.source.reference == "Patient/example"
    assert inst.status == "current"
    assert inst.text.status == "generated"


def test_list_4(base_settings):
    """No. 4 tests collection for List.
    Test File: list-example-empty.json
    """
    filename = base_settings["unittest_data_dir"] / "list-example-empty.json"
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_4(inst2)


def impl_list_5(inst):
    assert inst.code.coding[0].code == "8670-2"
    assert inst.code.coding[0].display == "History of family member diseases"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.contained[0].id == "1"
    assert inst.contained[1].id == "2"
    assert inst.contained[2].id == "3"
    assert inst.contained[3].id == "4"
    assert inst.contained[4].id == "5"
    assert inst.contained[5].id == "6"
    assert inst.contained[6].id == "7"
    assert inst.contained[7].id == "8"
    assert inst.entry[0].item.reference == "#1"
    assert inst.entry[1].item.reference == "#2"
    assert inst.entry[2].item.reference == "#3"
    assert inst.entry[3].item.reference == "#4"
    assert inst.entry[4].item.reference == "#5"
    assert inst.entry[5].item.reference == "#6"
    assert inst.entry[6].item.reference == "#7"
    assert inst.entry[7].item.reference == "#8"
    assert inst.entry[8].item.display == "Family history of cancer of colon"
    assert inst.entry[8].item.reference == "Condition/family-history"
    assert inst.id == "genetic"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "snapshot"
    assert inst.status == "current"
    assert inst.subject.display == "Peter Patient"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_list_5(base_settings):
    """No. 5 tests collection for List.
    Test File: list-example-familyhistory-genetics-profile.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "list-example-familyhistory-genetics-profile.json"
    )
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_5(inst2)


def impl_list_6(inst):
    assert inst.code.coding[0].code == "8670-2"
    assert inst.code.coding[0].display == "History of family member diseases"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.contained[0].id == "fmh-1"
    assert inst.contained[1].id == "fmh-2"
    assert inst.entry[0].item.reference == "#fmh-1"
    assert inst.entry[1].item.reference == "#fmh-2"
    assert inst.id == "f201"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "snapshot"
    assert inst.note[0].text == (
        "Both parents, both brothers and both children (twin) are " "still alive."
    )
    assert inst.status == "current"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_list_6(base_settings):
    """No. 6 tests collection for List.
    Test File: list-example-familyhistory-f201-roel.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "list-example-familyhistory-f201-roel.json"
    )
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_6(inst2)


def impl_list_7(inst):
    assert inst.date == fhirtypes.DateTime.validate("2012-11-25T22:17:00+11:00")
    assert inst.encounter.reference == "Encounter/example"
    assert inst.entry[0].deleted is True
    assert inst.entry[0].flag.text == "Deleted due to error"
    assert inst.entry[0].item.reference == "Condition/example"
    assert inst.entry[1].flag.text == "Added"
    assert inst.entry[1].item.reference == "Condition/example2"
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:uuid:a9fcea7c-fcdf-4d17-a5e0-f26dda030b59"
    assert inst.identifier[0].value == "23974652"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "changes"
    assert inst.source.reference == "Patient/example"
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_list_7(base_settings):
    """No. 7 tests collection for List.
    Test File: list-example.json
    """
    filename = base_settings["unittest_data_dir"] / "list-example.json"
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_7(inst2)


def impl_list_8(inst):
    assert inst.code.coding[0].code == "52472-8"
    assert inst.code.coding[0].display == "Allergies and Adverse Drug Reactions"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Current Allergy List"
    assert inst.date == fhirtypes.DateTime.validate("2015-07-14T23:10:23+11:00")
    assert inst.entry[0].item.reference == "AllergyIntolerance/example"
    assert inst.entry[1].item.reference == "AllergyIntolerance/medication"
    assert inst.id == "current-allergies"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "working"
    assert inst.orderedBy.coding[0].code == "entry-date"
    assert (
        inst.orderedBy.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/list-order"
    )
    assert inst.source.reference == "Patient/example"
    assert inst.status == "current"
    assert inst.text.status == "generated"
    assert inst.title == "Current Allergy List"


def test_list_8(base_settings):
    """No. 8 tests collection for List.
    Test File: list-example-allergies.json
    """
    filename = base_settings["unittest_data_dir"] / "list-example-allergies.json"
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_8(inst2)


def impl_list_9(inst):
    assert inst.code.coding[0].code == "80738-8"
    assert inst.code.coding[0].display == (
        "TPMT gene mutations found [Identifier] in Blood or Tissue by"
        " Sequencing Nominal"
    )
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == (
        "TPMT gene mutations found [Identifier] in Blood or Tissue by"
        " Sequencing Nominal"
    )
    assert inst.contained[0].id == "1"
    assert inst.contained[1].id == "2"
    assert inst.contained[2].id == "3"
    assert inst.contained[3].id == "4"
    assert inst.contained[4].id == "5"
    assert inst.contained[5].id == "6"
    assert inst.entry[0].item.reference == "#1"
    assert inst.entry[1].item.reference == "#2"
    assert inst.entry[2].item.reference == "#3"
    assert inst.entry[3].item.reference == "#4"
    assert inst.entry[4].item.reference == "#5"
    assert inst.entry[5].item.reference == "#6"
    assert inst.id == "example-double-cousin-relationship"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "snapshot"
    assert inst.status == "current"
    assert inst.subject.display == "Pam Taylor"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_list_9(base_settings):
    """No. 9 tests collection for List.
    Test File: list-example-double-cousin-relationship-pedigree.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "list-example-double-cousin-relationship-pedigree.json"
    )
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_9(inst2)


def impl_list_10(inst):
    assert inst.date == fhirtypes.DateTime.validate("2018-02-21T12:17:00+11:00")
    assert inst.entry[0].item.reference == "Patient/example"
    assert inst.entry[1].item.reference == "Patient/pat1"
    assert inst.entry[2].item.reference == "Patient/pat2"
    assert inst.entry[3].item.reference == "Patient/pat3"
    assert inst.entry[4].item.reference == "Patient/pat4"
    assert inst.entry[5].item.reference == "Patient/1"
    assert inst.entry[6].item.reference == "Patient/2"
    assert inst.entry[7].item.reference == "Patient/3"
    assert inst.entry[8].item.reference == "Patient/4"
    assert inst.entry[9].item.reference == "Patient/5"
    assert inst.id == "long"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mode == "changes"
    assert inst.status == "current"
    assert inst.text.status == "generated"


def test_list_10(base_settings):
    """No. 10 tests collection for List.
    Test File: list-example-long.json
    """
    filename = base_settings["unittest_data_dir"] / "list-example-long.json"
    inst = list.List.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "List" == inst.resource_type

    impl_list_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "List" == data["resourceType"]

    inst2 = list.List(**data)
    impl_list_10(inst2)
