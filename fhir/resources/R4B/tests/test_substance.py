# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Substance
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import substance


def impl_substance_1(inst):
    assert inst.category[0].coding[0].code == "chemical"
    assert inst.category[0].coding[0].display == "Chemical"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/substance-category"
    )
    assert inst.code.coding[0].code == "333346007"
    assert inst.code.coding[0].display == "Silver nitrate 20% solution (product)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.description == "Solution for silver nitrate stain"
    assert inst.id == "f204"
    assert inst.identifier[0].system == "http://acme.org/identifiers/substances"
    assert inst.identifier[0].value == "15970"
    assert inst.instance[0].expiry == fhirtypes.DateTime.validate("2018-01-01")
    assert (
        inst.instance[0].identifier.system
        == "http://acme.org/identifiers/substances/lot"
    )
    assert inst.instance[0].identifier.value == "AB94687"
    assert inst.instance[0].quantity.code == "mL"
    assert inst.instance[0].quantity.system == "http://unitsofmeasure.org"
    assert inst.instance[0].quantity.unit == "mL"
    assert float(inst.instance[0].quantity.value) == float(100)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_substance_1(base_settings):
    """No. 1 tests collection for Substance.
    Test File: substance-example-silver-nitrate-product.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "substance-example-silver-nitrate-product.json"
    )
    inst = substance.Substance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Substance" == inst.resource_type

    impl_substance_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Substance" == data["resourceType"]

    inst2 = substance.Substance(**data)
    impl_substance_1(inst2)


def impl_substance_2(inst):
    assert inst.category[0].coding[0].code == "drug"
    assert inst.category[0].coding[0].display == "Drug or Medicament"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/substance-category"
    )
    assert inst.code.coding[0].code == "392259005"
    assert inst.code.coding[0].display == (
        "Amoxicillin + clavulanate potassium 875mg/125mg tablet " "(product)"
    )
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].id == "ingr1"
    assert inst.contained[1].id == "ingr2"
    assert inst.description == "Augmentin 875"
    assert inst.id == "f205"
    assert inst.ingredient[0].quantity.denominator.code == "mg"
    assert inst.ingredient[0].quantity.denominator.system == "http://unitsofmeasure.org"
    assert inst.ingredient[0].quantity.denominator.unit == "mg"
    assert float(inst.ingredient[0].quantity.denominator.value) == float(1000)
    assert inst.ingredient[0].quantity.numerator.code == "mg"
    assert inst.ingredient[0].quantity.numerator.system == "http://unitsofmeasure.org"
    assert inst.ingredient[0].quantity.numerator.unit == "mg"
    assert float(inst.ingredient[0].quantity.numerator.value) == float(875)
    assert inst.ingredient[0].substanceReference.reference == "#ingr1"
    assert inst.ingredient[1].quantity.denominator.code == "mg"
    assert inst.ingredient[1].quantity.denominator.system == "http://unitsofmeasure.org"
    assert inst.ingredient[1].quantity.denominator.unit == "mg"
    assert float(inst.ingredient[1].quantity.denominator.value) == float(1000)
    assert inst.ingredient[1].quantity.numerator.code == "mg"
    assert inst.ingredient[1].quantity.numerator.system == "http://unitsofmeasure.org"
    assert inst.ingredient[1].quantity.numerator.unit == "mg"
    assert float(inst.ingredient[1].quantity.numerator.value) == float(125)
    assert inst.ingredient[1].substanceReference.reference == "#ingr2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_substance_2(base_settings):
    """No. 2 tests collection for Substance.
    Test File: substance-example-amoxicillin-clavulanate.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "substance-example-amoxicillin-clavulanate.json"
    )
    inst = substance.Substance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Substance" == inst.resource_type

    impl_substance_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Substance" == data["resourceType"]

    inst2 = substance.Substance(**data)
    impl_substance_2(inst2)


def impl_substance_3(inst):
    assert inst.category[0].coding[0].code == "chemical"
    assert inst.category[0].coding[0].display == "Chemical"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/substance-category"
    )
    assert inst.code.coding[0].code == "88480006"
    assert inst.code.coding[0].display == "Potassium"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "f203"
    assert inst.identifier[0].system == "http://acme.org/identifiers/substances"
    assert inst.identifier[0].value == "1234"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_substance_3(base_settings):
    """No. 3 tests collection for Substance.
    Test File: substance-example-f203-potassium.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "substance-example-f203-potassium.json"
    )
    inst = substance.Substance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Substance" == inst.resource_type

    impl_substance_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Substance" == data["resourceType"]

    inst2 = substance.Substance(**data)
    impl_substance_3(inst2)


def impl_substance_4(inst):
    assert inst.code.coding[0].code == "406466009"
    assert inst.code.coding[0].display == "House dust allergen"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "f201"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_substance_4(base_settings):
    """No. 4 tests collection for Substance.
    Test File: substance-example-f201-dust.json
    """
    filename = base_settings["unittest_data_dir"] / "substance-example-f201-dust.json"
    inst = substance.Substance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Substance" == inst.resource_type

    impl_substance_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Substance" == data["resourceType"]

    inst2 = substance.Substance(**data)
    impl_substance_4(inst2)


def impl_substance_5(inst):
    assert inst.category[0].coding[0].code == "allergen"
    assert inst.category[0].coding[0].display == "Allergen"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/substance-category"
    )
    assert inst.code.text == "apitoxin (Honey Bee Venom)"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://acme.org/identifiers/substances"
    assert inst.identifier[0].value == "1463"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_substance_5(base_settings):
    """No. 5 tests collection for Substance.
    Test File: substance-example.json
    """
    filename = base_settings["unittest_data_dir"] / "substance-example.json"
    inst = substance.Substance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Substance" == inst.resource_type

    impl_substance_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Substance" == data["resourceType"]

    inst2 = substance.Substance(**data)
    impl_substance_5(inst2)


def impl_substance_6(inst):
    assert inst.code.coding[0].code == "3092008"
    assert inst.code.coding[0].display == "Staphylococcus Aureus"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "f202"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_substance_6(base_settings):
    """No. 6 tests collection for Substance.
    Test File: substance-example-f202-staphylococcus.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "substance-example-f202-staphylococcus.json"
    )
    inst = substance.Substance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Substance" == inst.resource_type

    impl_substance_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Substance" == data["resourceType"]

    inst2 = substance.Substance(**data)
    impl_substance_6(inst2)
