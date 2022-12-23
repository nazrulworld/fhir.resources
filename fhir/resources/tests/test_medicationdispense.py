# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicationdispense


def impl_medicationdispense_1(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0316"
    assert inst.contained[0].id == "med0306"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg/kg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg/kg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1.8
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "255560000"
    assert inst.dosageInstruction[0].route.coding[0].display == "Intravenous"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
        "1.8 mg/kg IV infusion over 30 minutes every 3 weeks for 16 " "cycles"
    )
    assert inst.dosageInstruction[0].timing.repeat.count == 16
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(3)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "wk"
    assert inst.id == "meddisp0317"
    assert inst.medicationReference.display == "Brentixumab Vedotin (Adcetris)"
    assert inst.medicationReference.reference == "#med0306"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "415818005"
    assert inst.quantity.system == "http://snomed.info/sct"
    assert float(inst.quantity.value) == float(3)
    assert inst.status == "stopped"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "TF"
    assert inst.type.coding[0].display == "Trial Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate(
        "2015-06-26T07:13:00+05:00"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-06-25T07:13:00+05:00")


def test_medicationdispense_1(base_settings):
    """No. 1 tests collection for MedicationDispense.
    Test File: medicationdispense0317.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0317.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_1(inst2)


def impl_medicationdispense_2(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0318"
    assert inst.contained[0].id == "med0301"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(3)
    assert inst.destination.reference == "Location/ph"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        500
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].method.coding[0].code == "420620005"
    assert (
        inst.dosageInstruction[0].method.coding[0].display
        == "Push - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosageInstruction[0].method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].route.coding[0].code == "255560000"
    assert inst.dosageInstruction[0].route.coding[0].display == "Intravenous"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "500mg IV q6h x 3 days"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(6)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "meddisp0301"
    assert inst.location.display == "Pharmacy"
    assert inst.location.reference == "Location/ukp"
    assert inst.medicationReference.display == "Vancomycin Hydrochloride"
    assert inst.medicationReference.reference == "#med0301"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "733026001"
    assert inst.quantity.system == "http://snomed.info.sct"
    assert inst.quantity.unit == "Vial"
    assert float(inst.quantity.value) == float(12)
    assert inst.receiver[0].display == "Donald Duck"
    assert inst.receiver[0].reference == "Patient/pat1"
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.supportingInformation[0].reference == "Condition/f203"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "EM"
    assert inst.type.coding[0].display == "Emergency Supply"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_2(base_settings):
    """No. 2 tests collection for MedicationDispense.
    Test File: medicationdispense0301.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0301.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_2(inst2)


def impl_medicationdispense_3(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0321"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(10)
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "418914006"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
        "Warning. May cause drowsiness. If affected do not drive or "
        "operate machinery. Avoid alcoholic drink (qualifier value)"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code == "203082005"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
        == "Fibromyalgia (disorder)"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "TAB"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "26643006"
    assert inst.dosageInstruction[0].route.coding[0].display == "Oral Route"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert (
        inst.dosageInstruction[0].text == "1 tablet every four hours as needed for pain"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(4)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "meddisp0321"
    assert inst.medicationCodeableConcept.coding[0].code == "0074-3043-13"
    assert (
        inst.medicationCodeableConcept.coding[0].display
        == "Vicodin 5mg Hydrocodone, 500mg Acetaminophen tablet"
    )
    assert (
        inst.medicationCodeableConcept.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "TAB"
    assert (
        inst.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.quantity.value) == float(30)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_3(base_settings):
    """No. 3 tests collection for MedicationDispense.
    Test File: medicationdispense0321.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0321.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_3(inst2)


def impl_medicationdispense_4(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0323"
    assert inst.contained[0].id == "med0318"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mL"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mL"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1000
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.code == "h"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.unit == "h"
    assert float(
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.value
    ) == float(1)
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.code == "mL"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.unit == "mL"
    assert float(
        inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.value
    ) == float(50)
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "255560000"
    assert inst.dosageInstruction[0].route.coding[0].display == "Intravenous"
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert (
        inst.dosageInstruction[0].text
        == "1000mL infused at 50ml/hour for 4 hours - hang at 2200 hours"
    )
    assert inst.dosageInstruction[0].timing.event[0] == fhirtypes.DateTime.validate(
        "2015-01-15T22:00:00+11:00"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(24)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "h"
    assert inst.id == "meddisp0320"
    assert inst.medicationReference.display == "TPN Solution"
    assert inst.medicationReference.reference == "#med0318"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "ml"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(1000)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.whenHandedOver == fhirtypes.DateTime.validate(
        "2015-03-17T17:13:00+05:00"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-03-16T17:13:00+05:00")


def test_medicationdispense_4(base_settings):
    """No. 4 tests collection for MedicationDispense.
    Test File: medicationdispense0320.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0320.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_4(inst2)


def impl_medicationdispense_5(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0320"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "U"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "U"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        20
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "263887005"
    assert (
        inst.dosageInstruction[0].route.coding[0].display
        == "Subcutaneous (qualifier value)"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "20 Units SC three times daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 3
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0316"
    assert inst.medicationCodeableConcept.coding[0].code == "285018"
    assert (
        inst.medicationCodeableConcept.coding[0].display
        == "Lantus 100 unit/ml injectable solution"
    )
    assert (
        inst.medicationCodeableConcept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "ml"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(10)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-06-25T07:13:00+05:00")


def test_medicationdispense_5(base_settings):
    """No. 5 tests collection for MedicationDispense.
    Test File: medicationdispense0316.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0316.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_5(inst2)


def impl_medicationdispense_6(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0321"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert inst.dosageInstruction[0].additionalInstruction[0].text == "Shake Well"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "ORINHL"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "ea"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        1
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Use two sprays twice daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0327"
    assert inst.medicationCodeableConcept.coding[0].code == "746763"
    assert inst.medicationCodeableConcept.coding[0].display == (
        "Proventil 0.09mg/actuat (Albuterol sulfate 0.108mg/actuat " "from mouthpiece)"
    )
    assert (
        inst.medicationCodeableConcept.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "ml"
    assert inst.quantity.system == "http://unitsofmeasure.org"
    assert float(inst.quantity.value) == float(30)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "TF"
    assert inst.type.coding[0].display == "Trial Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2015-01-15T16:20:00Z")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_6(base_settings):
    """No. 6 tests collection for MedicationDispense.
    Test File: medicationdispense0327.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0327.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_6(inst2)


def impl_medicationdispense_7(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0309"
    assert inst.contained[0].id == "medexample015"
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        500
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].route.coding[0].code == "394899003"
    assert (
        inst.dosageInstruction[0].route.coding[0].display
        == "oral administration of treatment"
    )
    assert inst.dosageInstruction[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(21)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp008"
    assert inst.medicationReference.reference == "#medexample015"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationdispense_7(base_settings):
    """No. 7 tests collection for MedicationDispense.
    Test File: medicationdispenseexample8.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispenseexample8.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_7(inst2)


def impl_medicationdispense_8(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0331"
    assert inst.contained[0].id == "med0352"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(1)
    assert inst.dosageInstruction[0].additionalInstruction[0].text == (
        "Take along with one 2mg Coumadin tablet for a total daily "
        "dose of 7mg as prescribed by physician"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        2
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].sequence == 1
    assert (
        inst.dosageInstruction[0].text
        == "7mg (=one 5mg tablet PLUS one 2mg tablet) once daily"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0331"
    assert inst.medicationReference.display == "Coumadin 2mg tablet"
    assert inst.medicationReference.reference == "#med0352"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "415818006"
    assert inst.quantity.system == "http://snomed.info/sct"
    assert float(inst.quantity.value) == float(1)
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "DF"
    assert inst.type.coding[0].display == "Daily Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_8(base_settings):
    """No. 8 tests collection for MedicationDispense.
    Test File: medicationdispense0331.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0331.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_8(inst2)


def impl_medicationdispense_9(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0324"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(10)
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].code == "418637003"
    )
    assert inst.dosageInstruction[0].additionalInstruction[0].coding[0].display == (
        "Do not take with any other paracetamol products (qualifier " "value)"
    )
    assert (
        inst.dosageInstruction[0].additionalInstruction[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code == "386661006"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
        == "Fever (finding)"
    )
    assert (
        inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        240
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].maxDosePerPeriod.denominator.code == "d"
    assert (
        inst.dosageInstruction[0].maxDosePerPeriod.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.dosageInstruction[0].maxDosePerPeriod.denominator.value) == float(
        1
    )
    assert inst.dosageInstruction[0].maxDosePerPeriod.numerator.code == "mg"
    assert (
        inst.dosageInstruction[0].maxDosePerPeriod.numerator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.dosageInstruction[0].maxDosePerPeriod.numerator.value) == float(
        720
    )
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == (
        "Insert two suppositories (240mg) rectally twice daily as "
        "needed for fever to a maximim of 6 per day"
    )
    assert inst.dosageInstruction[0].timing.repeat.frequency == 2
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0311"
    assert inst.medicationCodeableConcept.coding[0].code == "0713-0118"
    assert (
        inst.medicationCodeableConcept.coding[0].display
        == "Acetaminophen 120mg Suppository"
    )
    assert (
        inst.medicationCodeableConcept.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "RECSUPP"
    assert (
        inst.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.quantity.value) == float(60)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2015-01-15T16:20:00Z")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_9(base_settings):
    """No. 9 tests collection for MedicationDispense.
    Test File: medicationdispense0311.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0311.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_9(inst2)


def impl_medicationdispense_10(inst):
    assert inst.authorizingPrescription[0].reference == "MedicationRequest/medrx0306"
    assert inst.daysSupply.code == "d"
    assert inst.daysSupply.system == "http://unitsofmeasure.org"
    assert inst.daysSupply.unit == "Day"
    assert float(inst.daysSupply.value) == float(30)
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code == "mg"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit == "mg"
    assert float(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value) == float(
        6
    )
    assert inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code == "calculated"
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display == "Calculated"
    )
    assert (
        inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosageInstruction[0].sequence == 1
    assert inst.dosageInstruction[0].text == "Take 3 tablets (6mg) once daily"
    assert inst.dosageInstruction[0].timing.repeat.frequency == 1
    assert float(inst.dosageInstruction[0].timing.repeat.period) == float(1)
    assert inst.dosageInstruction[0].timing.repeat.periodUnit == "d"
    assert inst.id == "meddisp0307"
    assert inst.medicationCodeableConcept.coding[0].code == "76388-713-25"
    assert (
        inst.medicationCodeableConcept.coding[0].display
        == "Myleran 2mg tablet, film coated"
    )
    assert (
        inst.medicationCodeableConcept.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.reference == "Practitioner/f006"
    assert inst.quantity.code == "TAB"
    assert (
        inst.quantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert float(inst.quantity.value) == float(90)
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RFP"
    assert inst.type.coding[0].display == "Refill - Part Fill"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.whenHandedOver == fhirtypes.DateTime.validate("2015-01-15T16:20:00Z")
    assert inst.whenPrepared == fhirtypes.DateTime.validate("2015-01-15T10:20:00Z")


def test_medicationdispense_10(base_settings):
    """No. 10 tests collection for MedicationDispense.
    Test File: medicationdispense0307.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationdispense0307.json"
    inst = medicationdispense.MedicationDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationDispense" == inst.resource_type

    impl_medicationdispense_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationDispense" == data["resourceType"]

    inst2 = medicationdispense.MedicationDispense(**data)
    impl_medicationdispense_10(inst2)
