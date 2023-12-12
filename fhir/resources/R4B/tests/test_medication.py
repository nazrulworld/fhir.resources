# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medication


def impl_medication_1(inst):
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2019-10-31")
    assert inst.batch.lotNumber == "12345"
    assert inst.code.coding[0].code == "0169-7501-11"
    assert inst.code.coding[0].display == "Novolog 100u/ml"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "org3"
    assert inst.form.coding[0].code == "385219001"
    assert inst.form.coding[0].display == "Injection solution (qualifier value)"
    assert inst.form.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0307"
    assert inst.ingredient[0].itemCodeableConcept.coding[0].code == "325072002"
    assert (
        inst.ingredient[0].itemCodeableConcept.coding[0].display
        == "Insulin Aspart (substance)"
    )
    assert (
        inst.ingredient[0].itemCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.ingredient[0].strength.denominator.code == "mL"
    assert inst.ingredient[0].strength.denominator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.denominator.value) == float(1)
    assert inst.ingredient[0].strength.numerator.code == "U"
    assert inst.ingredient[0].strength.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.numerator.value) == float(100)
    assert inst.manufacturer.reference == "#org3"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_1(base_settings):
    """No. 1 tests collection for Medication.
    Test File: medicationexample0307.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0307.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_1(inst2)


def impl_medication_2(inst):
    assert inst.code.coding[0].code == "373994007"
    assert inst.code.coding[0].display == "Prednisone 5mg tablet (Product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "sub03"
    assert inst.form.coding[0].code == "385055001"
    assert inst.form.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.form.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0311"
    assert inst.ingredient[0].itemReference.reference == "#sub03"
    assert inst.ingredient[0].strength.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strength.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[0].strength.denominator.value) == float(1)
    assert inst.ingredient[0].strength.numerator.code == "mg"
    assert inst.ingredient[0].strength.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.numerator.value) == float(5)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_2(base_settings):
    """No. 2 tests collection for Medication.
    Test File: medicationexample0311.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0311.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_2(inst2)


def impl_medication_3(inst):
    assert inst.code.coding[0].code == "430127000"
    assert inst.code.coding[0].display == "Oral Form Oxycodone (product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "sub03"
    assert inst.form.coding[0].code == "385055001"
    assert inst.form.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.form.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0310"
    assert inst.ingredient[0].itemReference.reference == "#sub03"
    assert inst.ingredient[0].strength.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strength.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[0].strength.denominator.value) == float(1)
    assert inst.ingredient[0].strength.numerator.code == "mg"
    assert inst.ingredient[0].strength.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.numerator.value) == float(5)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_3(base_settings):
    """No. 3 tests collection for Medication.
    Test File: medicationexample0310.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0310.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_3(inst2)


def impl_medication_4(inst):
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2019-10-31")
    assert inst.batch.lotNumber == "12345"
    assert inst.code.coding[0].code == "51144-050-01"
    assert inst.code.coding[0].display == "Adcetris"
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "org3"
    assert inst.form.coding[0].code == "421637006"
    assert (
        inst.form.coding[0].display
        == "Lyophilized powder for injectable solution (qualifier value)"
    )
    assert inst.form.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0306"
    assert inst.manufacturer.reference == "#org3"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_4(base_settings):
    """No. 4 tests collection for Medication.
    Test File: medicationexample0306.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0306.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_4(inst2)


def impl_medication_5(inst):
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2017-05-22")
    assert inst.batch.lotNumber == "9494788"
    assert inst.code.coding[0].code == "0409-6531-02"
    assert (
        inst.code.coding[0].display
        == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    )
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "org4"
    assert inst.form.coding[0].code == "385219001"
    assert inst.form.coding[0].display == "Injection Solution (qualifier value)"
    assert inst.form.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0301"
    assert inst.ingredient[0].isActive is True
    assert inst.ingredient[0].itemCodeableConcept.coding[0].code == "66955"
    assert (
        inst.ingredient[0].itemCodeableConcept.coding[0].display
        == "Vancomycin Hydrochloride"
    )
    assert (
        inst.ingredient[0].itemCodeableConcept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[0].strength.denominator.code == "mL"
    assert inst.ingredient[0].strength.denominator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.denominator.value) == float(10)
    assert inst.ingredient[0].strength.numerator.code == "mg"
    assert inst.ingredient[0].strength.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.numerator.value) == float(500)
    assert inst.manufacturer.reference == "#org4"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_medication_5(base_settings):
    """No. 5 tests collection for Medication.
    Test File: medicationexample0301.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0301.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_5(inst2)


def impl_medication_6(inst):
    assert inst.form.coding[0].code == "385219001"
    assert inst.form.coding[0].display == "Injection Solution (qualifier value)"
    assert inst.form.coding[0].system == "http://snomed.info/sct"
    assert inst.form.text == "Injection Solution (qualifier value)"
    assert inst.id == "med0317"
    assert inst.ingredient[0].itemCodeableConcept.coding[0].code == "204520"
    assert (
        inst.ingredient[0].itemCodeableConcept.coding[0].display == "Potassium Chloride"
    )
    assert (
        inst.ingredient[0].itemCodeableConcept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[0].strength.denominator.code == "mL"
    assert inst.ingredient[0].strength.denominator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.denominator.value) == float(1)
    assert inst.ingredient[0].strength.numerator.code == "meq"
    assert inst.ingredient[0].strength.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.numerator.value) == float(2)
    assert inst.ingredient[1].itemCodeableConcept.coding[0].code == "313002"
    assert (
        inst.ingredient[1].itemCodeableConcept.coding[0].display
        == "Sodium Chloride 0.9% injectable solution"
    )
    assert (
        inst.ingredient[1].itemCodeableConcept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.ingredient[1].strength.denominator.code == "mL"
    assert inst.ingredient[1].strength.denominator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[1].strength.denominator.value) == float(100)
    assert inst.ingredient[1].strength.numerator.code == "g"
    assert inst.ingredient[1].strength.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[1].strength.numerator.value) == float(0.9)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_6(base_settings):
    """No. 6 tests collection for Medication.
    Test File: medicationexample0317.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0317.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_6(inst2)


def impl_medication_7(inst):
    assert inst.code.text == "Amoxicillin 250mg/5ml Suspension"
    assert inst.id == "medicationexample1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Amoxicillin '
        "250mg/5ml Suspension</div>"
    )
    assert inst.text.status == "generated"


def test_medication_7(base_settings):
    """No. 7 tests collection for Medication.
    Test File: medicationexample1.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample1.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_7(inst2)


def impl_medication_8(inst):
    assert inst.batch.expirationDate == fhirtypes.DateTime.validate("2017-05-22")
    assert inst.batch.lotNumber == "9494788"
    assert inst.code.coding[0].code == "213293"
    assert inst.code.coding[0].display == "Capecitabine 500mg oral tablet (Xeloda)"
    assert inst.code.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.contained[0].id == "org2"
    assert inst.contained[1].id == "sub04"
    assert inst.form.coding[0].code == "385055001"
    assert inst.form.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.form.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "medexample015"
    assert inst.ingredient[0].itemReference.reference == "#sub04"
    assert inst.ingredient[0].strength.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strength.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[0].strength.denominator.value) == float(1)
    assert inst.ingredient[0].strength.numerator.code == "mg"
    assert inst.ingredient[0].strength.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.numerator.value) == float(500)
    assert inst.manufacturer.reference == "#org2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_8(base_settings):
    """No. 8 tests collection for Medication.
    Test File: medicationexample15.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample15.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_8(inst2)


def impl_medication_9(inst):
    assert inst.code.coding[0].code == "108761006"
    assert inst.code.coding[0].display == "Capecitabine (product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "sub03"
    assert inst.form.coding[0].code == "385055001"
    assert inst.form.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.form.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0321"
    assert inst.ingredient[0].itemReference.reference == "#sub03"
    assert inst.ingredient[0].strength.denominator.code == "385055001"
    assert inst.ingredient[0].strength.denominator.system == "http://snomed.info/sct"
    assert inst.ingredient[0].strength.denominator.unit == "Tablet"
    assert float(inst.ingredient[0].strength.denominator.value) == float(1)
    assert inst.ingredient[0].strength.numerator.code == "mg"
    assert inst.ingredient[0].strength.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.numerator.value) == float(500)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_9(base_settings):
    """No. 9 tests collection for Medication.
    Test File: medicationexample0321.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0321.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_9(inst2)


def impl_medication_10(inst):
    assert inst.code.coding[0].code == "324252006"
    assert inst.code.coding[0].display == "Azithromycin 250mg capsule (product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "sub03"
    assert inst.form.coding[0].code == "385055001"
    assert inst.form.coding[0].display == "Tablet dose form (qualifier value)"
    assert inst.form.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "med0320"
    assert inst.ingredient[0].itemReference.reference == "#sub03"
    assert inst.ingredient[0].strength.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strength.denominator.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.ingredient[0].strength.denominator.value) == float(1)
    assert inst.ingredient[0].strength.numerator.code == "mg"
    assert inst.ingredient[0].strength.numerator.system == "http://unitsofmeasure.org"
    assert float(inst.ingredient[0].strength.numerator.value) == float(250)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medication_10(base_settings):
    """No. 10 tests collection for Medication.
    Test File: medicationexample0320.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0320.json"
    inst = medication.Medication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Medication" == inst.resource_type

    impl_medication_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_10(inst2)
