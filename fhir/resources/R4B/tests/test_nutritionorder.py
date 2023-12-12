# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionOrder
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import nutritionorder


def impl_nutritionorder_1(inst):
    assert inst.allergyIntolerance[0].display == "Cashew Nuts"
    assert inst.allergyIntolerance[0].reference == "AllergyIntolerance/example"
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.encounter.display == "Inpatient"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.excludeFoodModifier[0].coding[0].code == "227493005"
    assert inst.excludeFoodModifier[0].coding[0].display == "Cashew Nut"
    assert inst.excludeFoodModifier[0].coding[0].system == "http://snomed.info/sct"
    assert inst.excludeFoodModifier[0].coding[0].version == "20140730"
    assert inst.foodPreferenceModifier[0].coding[0].code == "kosher"
    assert (
        inst.foodPreferenceModifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/diet"
    )
    assert inst.id == "diabeticsupplement"
    assert (
        inst.identifier[0].system == "http://goodhealthhospital.org/nutrition-requests"
    )
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert inst.supplement[0].productName == "Glucerna"
    assert inst.supplement[0].quantity.unit == "8 oz bottle"
    assert float(inst.supplement[0].quantity.value) == float(1)
    assert inst.supplement[0].schedule[
        0
    ].repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-02-10T15:00:00Z")
    assert inst.supplement[0].schedule[0].repeat.frequency == 1
    assert float(inst.supplement[0].schedule[0].repeat.period) == float(24)
    assert inst.supplement[0].schedule[0].repeat.periodUnit == "h"
    assert float(inst.supplement[0].schedule[1].repeat.duration) == float(1)
    assert inst.supplement[0].schedule[1].repeat.durationUnit == "h"
    assert inst.supplement[0].schedule[1].repeat.when[0] == "HS"
    assert inst.supplement[0].type.coding[0].code == "443051000124104"
    assert (
        inst.supplement[0].type.coding[0].display == "Adult diabetes specialty formula"
    )
    assert inst.supplement[0].type.coding[0].system == "http://snomed.info/sct"
    assert inst.supplement[0].type.coding[1].code == "1010"
    assert inst.supplement[0].type.coding[1].display == "Adult diabetic formula"
    assert (
        inst.supplement[0].type.coding[1].system
        == "http://goodhealthhospital.org/supplement-type-codes"
    )
    assert inst.supplement[0].type.text == "Adult diabetic formula"
    assert inst.text.status == "generated"


def test_nutritionorder_1(base_settings):
    """No. 1 tests collection for NutritionOrder.
    Test File: nutritionorder-example-diabeticsupplement.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "nutritionorder-example-diabeticsupplement.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_1(inst2)


def impl_nutritionorder_2(inst):
    assert inst.allergyIntolerance[0].display == "Cashew Nuts"
    assert inst.allergyIntolerance[0].reference == "AllergyIntolerance/example"
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.encounter.display == "Inpatient"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.enteralFormula.additiveProductName == "Acme Lipid Additive"
    assert inst.enteralFormula.additiveType.coding[0].code == "lipid"
    assert inst.enteralFormula.additiveType.coding[0].display == "Lipid"
    assert (
        inst.enteralFormula.additiveType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/entformula-additive"
    )
    assert inst.enteralFormula.administrationInstruction == "240 mls every 4hrs"
    assert inst.enteralFormula.administration[0].quantity.code == "mL"
    assert (
        inst.enteralFormula.administration[0].quantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.enteralFormula.administration[0].quantity.unit == "milliliters"
    assert float(inst.enteralFormula.administration[0].quantity.value) == float(240)
    assert inst.enteralFormula.administration[
        0
    ].schedule.repeat.boundsPeriod.start == fhirtypes.DateTime.validate(
        "2014-09-17T16:00:00Z"
    )
    assert inst.enteralFormula.administration[0].schedule.repeat.frequency == 1
    assert float(inst.enteralFormula.administration[0].schedule.repeat.period) == float(
        4
    )
    assert inst.enteralFormula.administration[0].schedule.repeat.periodUnit == "h"
    assert inst.enteralFormula.baseFormulaProductName == "Acme High Protein Formula"
    assert inst.enteralFormula.baseFormulaType.coding[0].code == "442991000124104"
    assert (
        inst.enteralFormula.baseFormulaType.coding[0].display
        == "Adult high protein formula"
    )
    assert (
        inst.enteralFormula.baseFormulaType.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.enteralFormula.caloricDensity.code == "cal/mL"
    assert inst.enteralFormula.caloricDensity.system == "http://unitsofmeasure.org"
    assert inst.enteralFormula.caloricDensity.unit == "calories per milliliter"
    assert float(inst.enteralFormula.caloricDensity.value) == float(1.5)
    assert inst.enteralFormula.maxVolumeToDeliver.code == "mL/d"
    assert inst.enteralFormula.maxVolumeToDeliver.system == "http://unitsofmeasure.org"
    assert inst.enteralFormula.maxVolumeToDeliver.unit == "milliliter/day"
    assert float(inst.enteralFormula.maxVolumeToDeliver.value) == float(1440)
    assert inst.enteralFormula.routeofAdministration.coding[0].code == "GT"
    assert (
        inst.enteralFormula.routeofAdministration.coding[0].display
        == "Instillation, gastrostomy tube"
    )
    assert inst.enteralFormula.routeofAdministration.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministrati" "on"
    )
    assert inst.excludeFoodModifier[0].coding[0].code == "227493005"
    assert inst.excludeFoodModifier[0].coding[0].display == "Cashew Nut"
    assert inst.excludeFoodModifier[0].coding[0].system == "http://snomed.info/sct"
    assert inst.excludeFoodModifier[0].coding[0].version == "20140730"
    assert inst.foodPreferenceModifier[0].coding[0].code == "dairy-free"
    assert (
        inst.foodPreferenceModifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/diet"
    )
    assert inst.id == "enteralbolus"
    assert inst.identifier[0].system == "http://www.acme.org/nutritionorders"
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_nutritionorder_2(base_settings):
    """No. 2 tests collection for NutritionOrder.
    Test File: nutritionorder-example-enteralbolus.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "nutritionorder-example-enteralbolus.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_2(inst2)


def impl_nutritionorder_3(inst):
    assert inst.allergyIntolerance[0].display == "Cashew Nuts"
    assert inst.allergyIntolerance[0].reference == "AllergyIntolerance/example"
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.encounter.display == "Inpatient"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.excludeFoodModifier[0].coding[0].code == "227493005"
    assert inst.excludeFoodModifier[0].coding[0].display == "Cashew Nut"
    assert inst.excludeFoodModifier[0].coding[0].system == "http://snomed.info/sct"
    assert inst.excludeFoodModifier[0].coding[0].version == "20140730"
    assert inst.foodPreferenceModifier[0].coding[0].code == "dairy-free"
    assert (
        inst.foodPreferenceModifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/diet"
    )
    assert inst.id == "fiberrestricteddiet"
    assert (
        inst.identifier[0].system == "http://goodhealthhospital.org/nutrition-requests"
    )
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.oralDiet.nutrient[0].amount.code == "g"
    assert inst.oralDiet.nutrient[0].amount.system == "http://unitsofmeasure.org"
    assert inst.oralDiet.nutrient[0].amount.unit == "grams"
    assert float(inst.oralDiet.nutrient[0].amount.value) == float(50)
    assert inst.oralDiet.nutrient[0].modifier.coding[0].code == "256674009"
    assert inst.oralDiet.nutrient[0].modifier.coding[0].display == "Fat"
    assert (
        inst.oralDiet.nutrient[0].modifier.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.oralDiet.schedule[
        0
    ].repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-02-10")
    assert inst.oralDiet.schedule[0].repeat.frequency == 3
    assert float(inst.oralDiet.schedule[0].repeat.period) == float(1)
    assert inst.oralDiet.schedule[0].repeat.periodUnit == "d"
    assert inst.oralDiet.type[0].coding[0].code == "15108003"
    assert inst.oralDiet.type[0].coding[0].display == "Restricted fiber diet"
    assert inst.oralDiet.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.oralDiet.type[0].coding[1].code == "1000"
    assert inst.oralDiet.type[0].coding[1].display == "Fiber restricted"
    assert (
        inst.oralDiet.type[0].coding[1].system
        == "http://goodhealthhospital.org/diet-type-codes"
    )
    assert inst.oralDiet.type[0].text == "Fiber restricted diet"
    assert inst.oralDiet.type[1].coding[0].code == "16208003"
    assert inst.oralDiet.type[1].coding[0].display == "Low fat diet"
    assert inst.oralDiet.type[1].coding[0].system == "http://snomed.info/sct"
    assert inst.oralDiet.type[1].coding[1].code == "1100"
    assert inst.oralDiet.type[1].coding[1].display == "Low Fat"
    assert (
        inst.oralDiet.type[1].coding[1].system
        == "http://goodhealthhospital.org/diet-type-codes"
    )
    assert inst.oralDiet.type[1].text == "Low fat diet"
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_nutritionorder_3(base_settings):
    """No. 3 tests collection for NutritionOrder.
    Test File: nutritionorder-example-fiberrestricteddiet.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "nutritionorder-example-fiberrestricteddiet.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_3(inst2)


def impl_nutritionorder_4(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.id == "texturemodified"
    assert (
        inst.identifier[0].system == "http://goodhealthhospital.org/nutrition-requests"
    )
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.oralDiet.schedule[
        0
    ].repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-02-10")
    assert inst.oralDiet.schedule[0].repeat.frequency == 3
    assert float(inst.oralDiet.schedule[0].repeat.period) == float(1)
    assert inst.oralDiet.schedule[0].repeat.periodUnit == "d"
    assert inst.oralDiet.texture[0].foodType.coding[0].code == "28647000"
    assert inst.oralDiet.texture[0].foodType.coding[0].display == "Meat"
    assert (
        inst.oralDiet.texture[0].foodType.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.oralDiet.texture[0].foodType.text == "Regular, Chopped Meat"
    assert inst.oralDiet.texture[0].modifier.coding[0].code == "228049004"
    assert inst.oralDiet.texture[0].modifier.coding[0].display == "Chopped food"
    assert (
        inst.oralDiet.texture[0].modifier.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.oralDiet.texture[0].modifier.text == "Regular, Chopped Meat"
    assert inst.oralDiet.type[0].coding[0].code == "435801000124108"
    assert inst.oralDiet.type[0].coding[0].display == "Texture modified diet"
    assert inst.oralDiet.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.oralDiet.type[0].coding[1].code == "1010"
    assert inst.oralDiet.type[0].coding[1].display == "Texture modified diet"
    assert (
        inst.oralDiet.type[0].coding[1].system
        == "http://goodhealthhospital.org/diet-type-codes"
    )
    assert inst.oralDiet.type[0].text == "Texture modified diet"
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_nutritionorder_4(base_settings):
    """No. 4 tests collection for NutritionOrder.
    Test File: nutritionorder-example-texture-modified.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "nutritionorder-example-texture-modified.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_4(inst2)


def impl_nutritionorder_5(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.id == "pureeddiet-simple"
    assert (
        inst.identifier[0].system == "http://goodhealthhospital.org/nutrition-requests"
    )
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.oralDiet.fluidConsistencyType[0].coding[0].code == "439021000124105"
    assert (
        inst.oralDiet.fluidConsistencyType[0].coding[0].display
        == "Dietary liquid consistency - nectar thick liquid"
    )
    assert (
        inst.oralDiet.fluidConsistencyType[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.oralDiet.fluidConsistencyType[0].text == "Nectar thick liquids"
    assert inst.oralDiet.schedule[
        0
    ].repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-02-10")
    assert inst.oralDiet.schedule[0].repeat.frequency == 3
    assert float(inst.oralDiet.schedule[0].repeat.period) == float(1)
    assert inst.oralDiet.schedule[0].repeat.periodUnit == "d"
    assert inst.oralDiet.texture[0].modifier.coding[0].code == "228055009"
    assert inst.oralDiet.texture[0].modifier.coding[0].display == "Liquidized food"
    assert (
        inst.oralDiet.texture[0].modifier.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.oralDiet.texture[0].modifier.text == "Pureed"
    assert inst.oralDiet.type[0].coding[0].code == "226211001"
    assert inst.oralDiet.type[0].coding[0].display == "Pureed diet"
    assert inst.oralDiet.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.oralDiet.type[0].coding[1].code == "1010"
    assert inst.oralDiet.type[0].coding[1].display == "Pureed diet"
    assert (
        inst.oralDiet.type[0].coding[1].system
        == "http://goodhealthhospital.org/diet-type-codes"
    )
    assert inst.oralDiet.type[0].text == "Pureed diet"
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert (
        inst.supplement[0].instruction == "Ensure Pudding at breakfast, lunch, supper"
    )
    assert inst.supplement[0].productName == "Ensure Pudding 4 oz container"
    assert inst.supplement[0].type.coding[0].code == "442971000124100"
    assert inst.supplement[0].type.coding[0].display == "Adult high energy formula"
    assert inst.supplement[0].type.coding[0].system == "http://snomed.info/sct"
    assert inst.supplement[0].type.coding[1].code == "1040"
    assert inst.supplement[0].type.coding[1].display == "Adult high energy pudding"
    assert (
        inst.supplement[0].type.coding[1].system
        == "http://goodhealthhospital.org/supplement-type-codes"
    )
    assert inst.supplement[0].type.text == "Adult high energy pudding"
    assert inst.text.status == "generated"


def test_nutritionorder_5(base_settings):
    """No. 5 tests collection for NutritionOrder.
    Test File: nutritionorder-example-pureeddiet-simple.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "nutritionorder-example-pureeddiet-simple.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_5(inst2)


def impl_nutritionorder_6(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.encounter.display == "Inpatient"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.enteralFormula.additiveProductName == "Acme High Carbohydrate Additive"
    assert inst.enteralFormula.additiveType.coding[0].code == "carbohydrate"
    assert inst.enteralFormula.additiveType.coding[0].display == "Carbohydrate"
    assert (
        inst.enteralFormula.additiveType.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/entformula-additive"
    )
    assert inst.enteralFormula.administrationInstruction == (
        "Add high calorie high carbohydrate additive to increase "
        "cal/oz from 24 cal/oz to 27 cal/oz."
    )
    assert inst.enteralFormula.administration[0].quantity.code == "[foz_us]"
    assert (
        inst.enteralFormula.administration[0].quantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.enteralFormula.administration[0].quantity.unit == "ounces"
    assert float(inst.enteralFormula.administration[0].quantity.value) == float(4)
    assert inst.enteralFormula.administration[
        0
    ].schedule.repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.enteralFormula.administration[0].schedule.repeat.frequency == 1
    assert float(inst.enteralFormula.administration[0].schedule.repeat.period) == float(
        3
    )
    assert inst.enteralFormula.administration[0].schedule.repeat.periodUnit == "h"
    assert inst.enteralFormula.baseFormulaProductName == "Acme Infant Formula + Iron"
    assert inst.enteralFormula.baseFormulaType.coding[0].code == "412414007"
    assert (
        inst.enteralFormula.baseFormulaType.coding[0].display == "infant formula + iron"
    )
    assert (
        inst.enteralFormula.baseFormulaType.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.enteralFormula.caloricDensity.code == "cal/[foz_us]"
    assert inst.enteralFormula.caloricDensity.system == "http://unitsofmeasure.org"
    assert inst.enteralFormula.caloricDensity.unit == "calories per ounce"
    assert float(inst.enteralFormula.caloricDensity.value) == float(20)
    assert inst.enteralFormula.maxVolumeToDeliver.code == "[foz_us]"
    assert inst.enteralFormula.maxVolumeToDeliver.system == "http://unitsofmeasure.org"
    assert inst.enteralFormula.maxVolumeToDeliver.unit == "ounces"
    assert float(inst.enteralFormula.maxVolumeToDeliver.value) == float(32)
    assert inst.enteralFormula.routeofAdministration.coding[0].code == "PO"
    assert (
        inst.enteralFormula.routeofAdministration.coding[0].display == "Swallow, oral"
    )
    assert inst.enteralFormula.routeofAdministration.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministrati" "on"
    )
    assert inst.enteralFormula.routeofAdministration.coding[0].userSelected is True
    assert inst.id == "infantenteral"
    assert inst.identifier[0].system == "http://www.acme.org/nutritionorders"
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_nutritionorder_6(base_settings):
    """No. 6 tests collection for NutritionOrder.
    Test File: nutritionorder-example-infantenteral.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "nutritionorder-example-infantenteral.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_6(inst2)


def impl_nutritionorder_7(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.encounter.display == "Inpatient"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.enteralFormula.administrationInstruction == (
        "Hold feedings from 7 pm to 7 am. Add MCT oil to increase "
        "calories from 1.0 cal/mL to 1.5 cal/mL"
    )
    assert inst.enteralFormula.administration[0].rateQuantity.code == "mL/h"
    assert (
        inst.enteralFormula.administration[0].rateQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.enteralFormula.administration[0].rateQuantity.unit == "ml/hr"
    assert float(inst.enteralFormula.administration[0].rateQuantity.value) == float(60)
    assert inst.enteralFormula.administration[
        0
    ].schedule.repeat.boundsPeriod.start == fhirtypes.DateTime.validate(
        "2014-09-17T07:00:00Z"
    )
    assert inst.enteralFormula.administration[1].rateQuantity.code == "mL/h"
    assert (
        inst.enteralFormula.administration[1].rateQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.enteralFormula.administration[1].rateQuantity.unit == "ml/hr"
    assert float(inst.enteralFormula.administration[1].rateQuantity.value) == float(80)
    assert inst.enteralFormula.administration[
        1
    ].schedule.repeat.boundsPeriod.start == fhirtypes.DateTime.validate(
        "2014-09-17T11:00:00Z"
    )
    assert inst.enteralFormula.administration[2].rateQuantity.code == "mL/h"
    assert (
        inst.enteralFormula.administration[2].rateQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.enteralFormula.administration[2].rateQuantity.unit == "ml/hr"
    assert float(inst.enteralFormula.administration[2].rateQuantity.value) == float(100)
    assert inst.enteralFormula.administration[
        2
    ].schedule.repeat.boundsPeriod.start == fhirtypes.DateTime.validate(
        "2014-09-17T15:00:00Z"
    )
    assert inst.enteralFormula.baseFormulaProductName == " Acme Diabetes Formula"
    assert inst.enteralFormula.baseFormulaType.coding[0].code == "6547210000124112"
    assert (
        inst.enteralFormula.baseFormulaType.coding[0].display
        == "Diabetic specialty enteral formula"
    )
    assert (
        inst.enteralFormula.baseFormulaType.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.enteralFormula.caloricDensity.code == "cal/mL"
    assert inst.enteralFormula.caloricDensity.system == "http://unitsofmeasure.org"
    assert inst.enteralFormula.caloricDensity.unit == "calories per milliliter"
    assert float(inst.enteralFormula.caloricDensity.value) == float(1)
    assert inst.enteralFormula.maxVolumeToDeliver.code == "mL/d"
    assert inst.enteralFormula.maxVolumeToDeliver.system == "http://unitsofmeasure.org"
    assert inst.enteralFormula.maxVolumeToDeliver.unit == "milliliter/day"
    assert float(inst.enteralFormula.maxVolumeToDeliver.value) == float(880)
    assert inst.enteralFormula.routeofAdministration.coding[0].code == "NGT"
    assert (
        inst.enteralFormula.routeofAdministration.coding[0].display
        == "Instillation, nasogastric tube"
    )
    assert inst.enteralFormula.routeofAdministration.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministrati" "on"
    )
    assert inst.id == "enteralcontinuous"
    assert inst.identifier[0].system == "http://www.acme.org/nutritionorders"
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_nutritionorder_7(base_settings):
    """No. 7 tests collection for NutritionOrder.
    Test File: nutritionorder-example-enteralcontinuous.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "nutritionorder-example-enteralcontinuous.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_7(inst2)


def impl_nutritionorder_8(inst):
    assert inst.allergyIntolerance[0].display == "Cashew Nuts"
    assert inst.allergyIntolerance[0].reference == "AllergyIntolerance/example"
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.encounter.display == "Inpatient"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.excludeFoodModifier[0].coding[0].code == "227493005"
    assert inst.excludeFoodModifier[0].coding[0].display == "Cashew Nut"
    assert inst.excludeFoodModifier[0].coding[0].system == "http://snomed.info/sct"
    assert inst.excludeFoodModifier[0].coding[0].version == "20140730"
    assert inst.foodPreferenceModifier[0].coding[0].code == "dairy-free"
    assert (
        inst.foodPreferenceModifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/diet"
    )
    assert inst.id == "cardiacdiet"
    assert (
        inst.identifier[0].system == "http://goodhealthhospital.org/nutrition-requests"
    )
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.oralDiet.instruction
        == "Starting on 2/10 breakfast, maximum 400 ml fluids per meal"
    )
    assert inst.oralDiet.nutrient[0].amount.code == "g"
    assert inst.oralDiet.nutrient[0].amount.system == "http://unitsofmeasure.org"
    assert inst.oralDiet.nutrient[0].amount.unit == "grams"
    assert float(inst.oralDiet.nutrient[0].amount.value) == float(2)
    assert inst.oralDiet.nutrient[0].modifier.coding[0].code == "39972003"
    assert inst.oralDiet.nutrient[0].modifier.coding[0].display == "Sodium"
    assert (
        inst.oralDiet.nutrient[0].modifier.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.oralDiet.nutrient[1].amount.code == "mL"
    assert inst.oralDiet.nutrient[1].amount.system == "http://unitsofmeasure.org"
    assert inst.oralDiet.nutrient[1].amount.unit == "milliliter"
    assert float(inst.oralDiet.nutrient[1].amount.value) == float(1500)
    assert inst.oralDiet.nutrient[1].modifier.coding[0].code == "33463005"
    assert inst.oralDiet.nutrient[1].modifier.coding[0].display == "Fluid"
    assert (
        inst.oralDiet.nutrient[1].modifier.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.oralDiet.type[0].coding[0].code == "386619000"
    assert inst.oralDiet.type[0].coding[0].display == "Low sodium diet"
    assert inst.oralDiet.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.oralDiet.type[0].coding[1].code == "1040"
    assert inst.oralDiet.type[0].coding[1].display == "Low Sodium Diet"
    assert (
        inst.oralDiet.type[0].coding[1].system
        == "http://goodhealthhospital.org/diet-type-codes"
    )
    assert inst.oralDiet.type[0].text == "Low sodium diet"
    assert inst.oralDiet.type[1].coding[0].code == "226208002"
    assert inst.oralDiet.type[1].coding[0].display == "Fluid restricted diet"
    assert inst.oralDiet.type[1].coding[0].system == "http://snomed.info/sct"
    assert inst.oralDiet.type[1].coding[1].code == "1040"
    assert inst.oralDiet.type[1].coding[1].display == "Fluid restricted diet"
    assert (
        inst.oralDiet.type[1].coding[1].system
        == "http://goodhealthhospital.org/diet-type-codes"
    )
    assert inst.oralDiet.type[1].text == "Fluid restricted diet"
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_nutritionorder_8(base_settings):
    """No. 8 tests collection for NutritionOrder.
    Test File: nutritionorder-example-cardiacdiet.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "nutritionorder-example-cardiacdiet.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_8(inst2)


def impl_nutritionorder_9(inst):
    assert inst.allergyIntolerance[0].display == "Cashew Nuts"
    assert inst.allergyIntolerance[0].reference == "AllergyIntolerance/example"
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.encounter.display == "Inpatient"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.excludeFoodModifier[0].coding[0].code == "227493005"
    assert inst.excludeFoodModifier[0].coding[0].display == "Cashew Nut"
    assert inst.excludeFoodModifier[0].coding[0].system == "http://snomed.info/sct"
    assert inst.excludeFoodModifier[0].coding[0].version == "20140730"
    assert inst.foodPreferenceModifier[0].coding[0].code == "dairy-free"
    assert (
        inst.foodPreferenceModifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/diet"
    )
    assert inst.id == "pureeddiet"
    assert (
        inst.identifier[0].system == "http://goodhealthhospital.org/nutrition-requests"
    )
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.oralDiet.fluidConsistencyType[0].coding[0].code == "439021000124105"
    assert (
        inst.oralDiet.fluidConsistencyType[0].coding[0].display
        == "Dietary liquid consistency - nectar thick liquid"
    )
    assert (
        inst.oralDiet.fluidConsistencyType[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.oralDiet.fluidConsistencyType[0].text == "Nectar thick liquids"
    assert inst.oralDiet.schedule[
        0
    ].repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-02-10")
    assert inst.oralDiet.schedule[0].repeat.frequency == 3
    assert float(inst.oralDiet.schedule[0].repeat.period) == float(1)
    assert inst.oralDiet.schedule[0].repeat.periodUnit == "d"
    assert inst.oralDiet.texture[0].modifier.coding[0].code == "228055009"
    assert inst.oralDiet.texture[0].modifier.coding[0].display == "Liquidized food"
    assert (
        inst.oralDiet.texture[0].modifier.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.oralDiet.texture[0].modifier.text == "Pureed"
    assert inst.oralDiet.type[0].coding[0].code == "226211001"
    assert inst.oralDiet.type[0].coding[0].display == "Pureed diet"
    assert inst.oralDiet.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.oralDiet.type[0].coding[1].code == "1010"
    assert inst.oralDiet.type[0].coding[1].display == "Pureed diet"
    assert (
        inst.oralDiet.type[0].coding[1].system
        == "http://goodhealthhospital.org/diet-type-codes"
    )
    assert inst.oralDiet.type[0].text == "Pureed diet"
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_nutritionorder_9(base_settings):
    """No. 9 tests collection for NutritionOrder.
    Test File: nutritionorder-example-pureeddiet.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "nutritionorder-example-pureeddiet.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_9(inst2)


def impl_nutritionorder_10(inst):
    assert inst.allergyIntolerance[0].display == "Cashew Nuts"
    assert inst.allergyIntolerance[0].reference == "AllergyIntolerance/example"
    assert inst.dateTime == fhirtypes.DateTime.validate("2014-09-17")
    assert inst.encounter.display == "Inpatient"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.excludeFoodModifier[0].coding[0].code == "227493005"
    assert inst.excludeFoodModifier[0].coding[0].display == "Cashew Nut"
    assert inst.excludeFoodModifier[0].coding[0].system == "http://snomed.info/sct"
    assert inst.excludeFoodModifier[0].coding[0].version == "20140730"
    assert inst.foodPreferenceModifier[0].coding[0].code == "dairy-free"
    assert (
        inst.foodPreferenceModifier[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/diet"
    )
    assert inst.id == "diabeticdiet"
    assert (
        inst.identifier[0].system == "http://goodhealthhospital.org/nutrition-requests"
    )
    assert inst.identifier[0].value == "123"
    assert inst.intent == "order"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.oralDiet.nutrient[0].amount.code == "g"
    assert inst.oralDiet.nutrient[0].amount.system == "http://unitsofmeasure.org"
    assert inst.oralDiet.nutrient[0].amount.unit == "grams"
    assert float(inst.oralDiet.nutrient[0].amount.value) == float(75)
    assert inst.oralDiet.nutrient[0].modifier.coding[0].code == "2331003"
    assert inst.oralDiet.nutrient[0].modifier.coding[0].display == "Carbohydrate"
    assert (
        inst.oralDiet.nutrient[0].modifier.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.oralDiet.schedule[
        0
    ].repeat.boundsPeriod.start == fhirtypes.DateTime.validate("2015-02-10")
    assert inst.oralDiet.schedule[0].repeat.frequency == 3
    assert float(inst.oralDiet.schedule[0].repeat.period) == float(1)
    assert inst.oralDiet.schedule[0].repeat.periodUnit == "d"
    assert inst.oralDiet.type[0].coding[0].code == "160670007"
    assert inst.oralDiet.type[0].coding[0].display == "Diabetic diet"
    assert inst.oralDiet.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.oralDiet.type[0].coding[1].code == "1030"
    assert inst.oralDiet.type[0].coding[1].display == "DD - Diabetic diet"
    assert (
        inst.oralDiet.type[0].coding[1].system
        == "http://goodhealthhospital.org/diet-type-codes"
    )
    assert inst.oralDiet.type[0].text == "DD - Diabetic diet"
    assert inst.orderer.display == "Dr Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.patient.display == "Peter Chalmers"
    assert inst.patient.reference == "Patient/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_nutritionorder_10(base_settings):
    """No. 10 tests collection for NutritionOrder.
    Test File: nutritionorder-example-diabeticdiet.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "nutritionorder-example-diabeticdiet.json"
    )
    inst = nutritionorder.NutritionOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NutritionOrder" == inst.resource_type

    impl_nutritionorder_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NutritionOrder" == data["resourceType"]

    inst2 = nutritionorder.NutritionOrder(**data)
    impl_nutritionorder_10(inst2)
