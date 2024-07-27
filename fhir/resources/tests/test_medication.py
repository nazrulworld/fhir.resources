# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import medication
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_medication_1(inst):
    assert (
        inst.batch.expirationDate
        == ExternalValidatorModel(valueDateTime="2019-10-31").valueDateTime
    )
    assert inst.batch.lotNumber == "12345"
    assert inst.code.coding[0].code == "0169-7501-11"
    assert inst.code.coding[0].display == "Novolog 100u/ml"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://hl7.org/fhir/sid/ndc").valueUri
    )
    assert inst.contained[0].id == "mmanu"
    assert inst.doseForm.coding[0].code == "385219001"
    assert inst.doseForm.coding[0].display == "Injection solution (qualifier value)"
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "med0307"
    assert inst.ingredient[0].item.concept.coding[0].code == "325072002"
    assert (
        inst.ingredient[0].item.concept.coding[0].display
        == "Insulin Aspart (substance)"
    )
    assert (
        inst.ingredient[0].item.concept.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.ingredient[0].strengthRatio.denominator.code == "mL"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "U"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(100)
    assert inst.marketingAuthorizationHolder.reference == "#mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_medication_1(base_settings):
    """No. 1 tests collection for Medication.
    Test File: medicationexample0307.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0307.json"
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_1(inst2)


def impl_medication_2(inst):
    assert inst.code.coding[0].code == "373994007"
    assert inst.code.coding[0].display == "Prednisone 5mg tablet (Product)"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.contained[0].id == "sub03"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "med0311"
    assert inst.ingredient[0].item.reference.reference == "#sub03"
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
        ).valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(5)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_medication_2(base_settings):
    """No. 2 tests collection for Medication.
    Test File: medicationexample0311.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0311.json"
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_2(inst2)


def impl_medication_3(inst):
    assert inst.code.coding[0].code == "430127000"
    assert inst.code.coding[0].display == "Oral Form Oxycodone (product)"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.contained[0].id == "sub03"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "med0310"
    assert inst.ingredient[0].item.reference.reference == "#sub03"
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
        ).valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(5)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_medication_3(base_settings):
    """No. 3 tests collection for Medication.
    Test File: medicationexample0310.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0310.json"
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_3(inst2)


def impl_medication_4(inst):
    assert (
        inst.batch.expirationDate
        == ExternalValidatorModel(valueDateTime="2019-10-31").valueDateTime
    )
    assert inst.batch.lotNumber == "12345"
    assert inst.code.coding[0].code == "51144-050-01"
    assert inst.code.coding[0].display == "Adcetris"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://hl7.org/fhir/sid/ndc").valueUri
    )
    assert inst.contained[0].id == "mmanu"
    assert inst.doseForm.coding[0].code == "421637006"
    assert inst.doseForm.coding[0].display == (
        "Lyophilized powder for injectable solution (qualifier value)" " "
    )
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "med0306"
    assert inst.marketingAuthorizationHolder.reference == "#mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_medication_4(base_settings):
    """No. 4 tests collection for Medication.
    Test File: medicationexample0306.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0306.json"
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_4(inst2)


def impl_medication_5(inst):
    assert (
        inst.batch.expirationDate
        == ExternalValidatorModel(valueDateTime="2017-05-22").valueDateTime
    )
    assert inst.batch.lotNumber == "9494788"
    assert inst.code.coding[0].code == "0409-6531-02"
    assert (
        inst.code.coding[0].display
        == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    )
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://hl7.org/fhir/sid/ndc").valueUri
    )
    assert inst.contained[0].id == "mmanu"
    assert inst.doseForm.coding[0].code == "385219001"
    assert inst.doseForm.coding[0].display == "Injection Solution (qualifier value)"
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "med0301"
    assert inst.identifier[0].id == "123456789"
    assert inst.ingredient[0].isActive is True
    assert inst.ingredient[0].item.concept.coding[0].code == "66955"
    assert (
        inst.ingredient[0].item.concept.coding[0].display == "Vancomycin Hydrochloride"
    )
    assert (
        inst.ingredient[0].item.concept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://www.nlm.nih.gov/research/umls/rxnorm"
        ).valueUri
    )
    assert inst.ingredient[0].strengthRatio.denominator.code == "mL"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(10)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(500)
    assert inst.marketingAuthorizationHolder.reference == "#mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_medication_5(base_settings):
    """No. 5 tests collection for Medication.
    Test File: medicationexample0301.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0301.json"
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_5(inst2)


def impl_medication_6(inst):
    assert inst.doseForm.coding[0].code == "385219001"
    assert inst.doseForm.coding[0].display == "Injection Solution (qualifier value)"
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.doseForm.text == "Injection Solution (qualifier value)"
    assert inst.id == "med0317"
    assert inst.ingredient[0].item.concept.coding[0].code == "8591"
    assert inst.ingredient[0].item.concept.coding[0].display == "Potassium Chloride"
    assert (
        inst.ingredient[0].item.concept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://www.nlm.nih.gov/research/umls/rxnorm"
        ).valueUri
    )
    assert inst.ingredient[0].strengthRatio.denominator.code == "mL"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1000)
    assert inst.ingredient[0].strengthRatio.numerator.code == "meq"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(20)
    assert inst.ingredient[1].item.concept.coding[0].code == "313002"
    assert (
        inst.ingredient[1].item.concept.coding[0].display
        == "1000 ml glucost 50mg/ml Injection"
    )
    assert (
        inst.ingredient[1].item.concept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://www.nlm.nih.gov/research/umls/rxnorm"
        ).valueUri
    )
    assert inst.ingredient[1].strengthRatio.denominator.code == "mL"
    assert (
        inst.ingredient[1].strengthRatio.denominator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[1].strengthRatio.denominator.value) == float(100)
    assert inst.ingredient[1].strengthRatio.numerator.code == "g"
    assert (
        inst.ingredient[1].strengthRatio.numerator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[1].strengthRatio.numerator.value) == float(5)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_medication_6(base_settings):
    """No. 6 tests collection for Medication.
    Test File: medicationexample0317.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0317.json"
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_6(inst2)


def impl_medication_7(inst):
    assert inst.code.text == "Amoxicillin 250mg/5ml Suspension"
    assert inst.id == "medicationexample1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
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
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_7(inst2)


def impl_medication_8(inst):
    assert (
        inst.batch.expirationDate
        == ExternalValidatorModel(valueDateTime="2017-05-22").valueDateTime
    )
    assert inst.batch.lotNumber == "9494788"
    assert inst.code.coding[0].code == "213293"
    assert inst.code.coding[0].display == "Capecitabine 500mg oral tablet (Xeloda)"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://www.nlm.nih.gov/research/umls/rxnorm"
        ).valueUri
    )
    assert inst.contained[0].id == "mmanu"
    assert inst.contained[1].id == "sub04"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "medexample015"
    assert inst.ingredient[0].item.reference.reference == "#sub04"
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
        ).valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(500)
    assert inst.marketingAuthorizationHolder.reference == "#mmanu"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_medication_8(base_settings):
    """No. 8 tests collection for Medication.
    Test File: medicationexample15.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample15.json"
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_8(inst2)


def impl_medication_9(inst):
    assert inst.code.coding[0].code == "108761006"
    assert inst.code.coding[0].display == "Capecitabine (product)"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.contained[0].id == "sub03"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "med0321"
    assert inst.ingredient[0].item.reference.reference == "#sub03"
    assert inst.ingredient[0].strengthRatio.denominator.code == "385055001"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.ingredient[0].strengthRatio.denominator.unit == "Tablet"
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(500)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_medication_9(base_settings):
    """No. 9 tests collection for Medication.
    Test File: medicationexample0321.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0321.json"
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_9(inst2)


def impl_medication_10(inst):
    assert inst.code.coding[0].code == "324252006"
    assert inst.code.coding[0].display == "Azithromycin 250mg capsule (product)"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.contained[0].id == "sub03"
    assert inst.doseForm.coding[0].code == "385055001"
    assert inst.doseForm.coding[0].display == "Tablet dose form (qualifier value)"
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "med0320"
    assert inst.ingredient[0].item.reference.reference == "#sub03"
    assert inst.ingredient[0].strengthRatio.denominator.code == "TAB"
    assert (
        inst.ingredient[0].strengthRatio.denominator.system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
        ).valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.denominator.value) == float(1)
    assert inst.ingredient[0].strengthRatio.numerator.code == "mg"
    assert (
        inst.ingredient[0].strengthRatio.numerator.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.ingredient[0].strengthRatio.numerator.value) == float(250)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_medication_10(base_settings):
    """No. 10 tests collection for Medication.
    Test File: medicationexample0320.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationexample0320.json"
    inst = medication.Medication.model_validate_json(Path(filename).read_bytes())
    assert "Medication" == inst.get_resource_type()

    impl_medication_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Medication" == data["resourceType"]

    inst2 = medication.Medication(**data)
    impl_medication_10(inst2)
