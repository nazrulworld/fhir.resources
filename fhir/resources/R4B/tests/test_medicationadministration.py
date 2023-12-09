# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicationadministration


def impl_medicationadministration_1(inst):
    assert inst.contained[0].id == "med0301"
    assert inst.contained[1].id == "signature"
    assert inst.context.display == "encounter who leads to this prescription"
    assert inst.context.reference == "Encounter/f001"
    assert inst.dosage.dose.code == "mg"
    assert inst.dosage.dose.system == "http://unitsofmeasure.org"
    assert inst.dosage.dose.unit == "mg"
    assert float(inst.dosage.dose.value) == float(500)
    assert inst.dosage.method.text == "IV Push"
    assert inst.dosage.route.coding[0].code == "47625008"
    assert inst.dosage.route.coding[0].display == "Intravenous route (qualifier value)"
    assert inst.dosage.route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.text == "500mg IV q6h x 3 days"
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T14:30:00+01:00"
    )
    assert inst.eventHistory[0].display == "Author's Signature"
    assert inst.eventHistory[0].reference == "#signature"
    assert inst.id == "medadmin0301"
    assert inst.medicationReference.reference == "#med0301"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Patrick Pump"
    assert inst.performer[0].actor.reference == "Practitioner/f007"
    assert inst.reasonCode[0].coding[0].code == "b"
    assert inst.reasonCode[0].coding[0].display == "Given as Ordered"
    assert inst.reasonCode[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/reason-medication-" "given"
    )
    assert inst.request.reference == "MedicationRequest/medrx0318"
    assert inst.status == "in-progress"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationadministration_1(base_settings):
    """No. 1 tests collection for MedicationAdministration.
    Test File: medicationadministration0301.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationadministration0301.json"
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_1(inst2)


def impl_medicationadministration_2(inst):
    assert inst.contained[0].id == "med0303"
    assert inst.context.reference == "Encounter/f001"
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2015-01-15T14:30:00+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T14:30:00+01:00"
    )
    assert inst.id == "medadminexample03"
    assert inst.medicationReference.reference == "#med0303"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == (
        "Patient started Bupropion this morning - will administer in "
        "a reduced dose tomorrow"
    )
    assert inst.request.reference == "MedicationRequest/medrx0317"
    assert inst.status == "on-hold"
    assert inst.statusReason[0].coding[0].code == "373147003"
    assert inst.statusReason[0].coding[0].display == (
        "Administration of medication not done due to a " "contraindication (situation)"
    )
    assert inst.statusReason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.supportingInformation[0].reference == "Condition/f204"
    assert inst.text.status == "generated"


def test_medicationadministration_2(base_settings):
    """No. 2 tests collection for MedicationAdministration.
    Test File: medicationadministrationexample3.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicationadministrationexample3.json"
    )
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_2(inst2)


def impl_medicationadministration_3(inst):
    assert inst.contained[0].id == "med0313"
    assert inst.context.display == "encounter who leads to this prescription"
    assert inst.context.reference == "Encounter/f001"
    assert inst.device[0].reference == "Device/f001"
    assert inst.dosage.dose.code == "mg"
    assert inst.dosage.dose.system == "http://unitsofmeasure.org"
    assert inst.dosage.dose.unit == "mg"
    assert float(inst.dosage.dose.value) == float(7)
    assert inst.dosage.method.coding[0].code == "420620005"
    assert (
        inst.dosage.method.coding[0].display
        == "Push - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosage.method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.rateQuantity.code == "min"
    assert inst.dosage.rateQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosage.rateQuantity.unit == "min"
    assert float(inst.dosage.rateQuantity.value) == float(4)
    assert inst.dosage.route.coding[0].code == "255560000"
    assert inst.dosage.route.coding[0].display == "Intravenous"
    assert inst.dosage.route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.text == (
        "0.05 - 0.1mg/kg IV over 2-5 minutes every 15 minutes as " "needed"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2015-01-15T14:30:00+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T04:30:00+01:00"
    )
    assert inst.id == "medadmin0307"
    assert inst.medicationReference.reference == "#med0313"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Patrick Pump"
    assert inst.performer[0].actor.reference == "Practitioner/f007"
    assert inst.performer[0].function.coding[0].code == "performer"
    assert inst.performer[0].function.coding[0].display == "Performer"
    assert inst.performer[0].function.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/med-admin-perform-" "function"
    )
    assert inst.request.reference == "MedicationRequest/medrx0315"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationadministration_3(base_settings):
    """No. 3 tests collection for MedicationAdministration.
    Test File: medicationadministration0307.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationadministration0307.json"
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_3(inst2)


def impl_medicationadministration_4(inst):
    assert inst.contained[0].id == "med0304"
    assert inst.dosage.dose.code == "TAB"
    assert (
        inst.dosage.dose.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosage.dose.unit == "TAB"
    assert float(inst.dosage.dose.value) == float(1)
    assert inst.dosage.route.coding[0].code == "26643006"
    assert inst.dosage.route.coding[0].display == "Oral Route"
    assert inst.dosage.route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.text == (
        "0.25mg PO every 6-12 hours as needed for menses from Jan "
        "15-20, 2015.  Do not exceed more than 4mg per day"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2015-01-16T02:03:00+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T22:03:00+01:00"
    )
    assert inst.id == "medadmin0311"
    assert inst.medicationReference.reference == "#med0304"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Patrick Pump"
    assert inst.performer[0].actor.reference == "Practitioner/f007"
    assert inst.reasonCode[0].coding[0].code == "266599000"
    assert inst.reasonCode[0].coding[0].display == "Dysmenorrhea"
    assert inst.reasonCode[0].coding[0].system == "http://snomed.info/sct"
    assert inst.request.reference == "MedicationRequest/medrx0305"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationadministration_4(base_settings):
    """No. 4 tests collection for MedicationAdministration.
    Test File: medicationadministration0311.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationadministration0311.json"
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_4(inst2)


def impl_medicationadministration_5(inst):
    assert inst.contained[0].id == "med0304"
    assert inst.dosage.dose.code == "mg"
    assert inst.dosage.dose.system == "http://unitsofmeasure.org"
    assert inst.dosage.dose.unit == "mg"
    assert float(inst.dosage.dose.value) == float(6)
    assert inst.dosage.route.coding[0].code == "26643006"
    assert inst.dosage.route.coding[0].display == "Oral route (qualifier value)"
    assert inst.dosage.route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.text == (
        "6 mg PO daily for remission induction; adjust dosage to "
        "white blood cell (WBC) count.  With hold treatment if WBC is"
        " less than 15,000/µL; resume when WBC is greater than "
        "50,000/µL"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2015-01-16T02:03:00+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T22:03:00+01:00"
    )
    assert inst.id == "medadmin0310"
    assert inst.medicationReference.reference == "#med0304"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Patrick Pump"
    assert inst.performer[0].actor.reference == "Practitioner/f007"
    assert inst.request.reference == "MedicationRequest/medrx0306"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationadministration_5(base_settings):
    """No. 5 tests collection for MedicationAdministration.
    Test File: medicationadministration0310.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationadministration0310.json"
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_5(inst2)


def impl_medicationadministration_6(inst):
    assert inst.contained[0].id == "med0306"
    assert inst.context.display == "encounter who leads to this prescription"
    assert inst.context.reference == "Encounter/f001"
    assert inst.dosage.dose.code == "TAB"
    assert (
        inst.dosage.dose.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosage.dose.unit == "TAB"
    assert float(inst.dosage.dose.value) == float(2)
    assert inst.dosage.method.coding[0].code == "421521009"
    assert (
        inst.dosage.method.coding[0].display
        == "Swallow - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosage.method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.route.coding[0].code == "26643006"
    assert inst.dosage.route.coding[0].display == "Oral Route"
    assert inst.dosage.route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.text == "Two tablets at once"
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2015-01-15T14:30:00+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T04:30:00+01:00"
    )
    assert inst.id == "medadmin0306"
    assert inst.medicationReference.reference == "#med0306"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Patrick Pump"
    assert inst.performer[0].actor.reference == "Practitioner/f007"
    assert inst.performer[0].function.coding[0].code == "performer"
    assert inst.performer[0].function.coding[0].display == "Performer"
    assert inst.performer[0].function.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/med-admin-perform-" "function"
    )
    assert inst.request.reference == "MedicationRequest/medrx0302"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationadministration_6(base_settings):
    """No. 6 tests collection for MedicationAdministration.
    Test File: medicationadministration0306.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationadministration0306.json"
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_6(inst2)


def impl_medicationadministration_7(inst):
    assert inst.contained[0].id == "med0318"
    assert inst.device[0].reference == "Device/f001"
    assert inst.dosage.dose.code == "mL"
    assert inst.dosage.dose.system == "http://unitsofmeasure.org"
    assert inst.dosage.dose.unit == "mL"
    assert float(inst.dosage.dose.value) == float(1000)
    assert inst.dosage.method.text == "PICC line"
    assert inst.dosage.rateRatio.denominator.code == "h"
    assert inst.dosage.rateRatio.denominator.system == "http://unitsofmeasure.org"
    assert inst.dosage.rateRatio.denominator.unit == "h"
    assert float(inst.dosage.rateRatio.denominator.value) == float(1)
    assert inst.dosage.rateRatio.numerator.code == "mL"
    assert inst.dosage.rateRatio.numerator.system == "http://unitsofmeasure.org"
    assert inst.dosage.rateRatio.numerator.unit == "mL"
    assert float(inst.dosage.rateRatio.numerator.value) == float(50)
    assert inst.dosage.route.coding[0].code == "255560000"
    assert inst.dosage.route.coding[0].display == "Intravenous"
    assert inst.dosage.route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.site.coding[0].code == "6073002"
    assert (
        inst.dosage.site.coding[0].display
        == "Structure of ligament of left superior vena cava"
    )
    assert inst.dosage.site.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.dosage.text
        == "1000mL infused at 50ml/hour for 4 hours - hung at 2200 hours"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2015-01-16T02:03:00+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T22:03:00+01:00"
    )
    assert inst.id == "medadmin0309"
    assert inst.medicationReference.reference == "#med0318"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Patrick Pump"
    assert inst.performer[0].actor.reference == "Practitioner/f007"
    assert inst.performer[0].function.coding[0].code == "performer"
    assert inst.performer[0].function.coding[0].display == "Performer"
    assert inst.performer[0].function.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/med-admin-perform-" "function"
    )
    assert inst.request.reference == "MedicationRequest/medrx0323"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationadministration_7(base_settings):
    """No. 7 tests collection for MedicationAdministration.
    Test File: medicationadministration0309.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationadministration0309.json"
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_7(inst2)


def impl_medicationadministration_8(inst):
    assert inst.dosage.dose.code == "mg"
    assert inst.dosage.dose.system == "http://unitsofmeasure.org"
    assert inst.dosage.dose.unit == "mg"
    assert float(inst.dosage.dose.value) == float(240)
    assert inst.dosage.site.coding[0].code == "34402009"
    assert inst.dosage.site.coding[0].display == "Rectum structure"
    assert inst.dosage.site.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.text == (
        "Insert one suppository rectally twice daily as needed for "
        "fever to a maximim of 3 per day"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2015-01-16T02:03:00+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T22:03:00+01:00"
    )
    assert inst.id == "medadmin0313"
    assert inst.medicationCodeableConcept.coding[0].code == "322254008"
    assert (
        inst.medicationCodeableConcept.coding[0].display
        == "Paracetamol 240mg suppository (product)"
    )
    assert inst.medicationCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Patrick Pump"
    assert inst.performer[0].actor.reference == "Practitioner/f007"
    assert inst.reasonCode[0].coding[0].code == "c"
    assert inst.reasonCode[0].coding[0].display == "Emergency"
    assert inst.reasonCode[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/reason-medication-" "given"
    )
    assert inst.request.reference == "MedicationRequest/medrx0324"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationadministration_8(base_settings):
    """No. 8 tests collection for MedicationAdministration.
    Test File: medicationadministration0313.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationadministration0313.json"
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_8(inst2)


def impl_medicationadministration_9(inst):
    assert inst.contained[0].id == "med0306"
    assert inst.context.display == "encounter who leads to this prescription"
    assert inst.context.reference == "Encounter/f001"
    assert inst.dosage.dose.code == "mg/kg"
    assert inst.dosage.dose.system == "http://unitsofmeasure.org"
    assert inst.dosage.dose.unit == "mg/kg"
    assert float(inst.dosage.dose.value) == float(1.8)
    assert inst.dosage.rateQuantity.code == "min"
    assert inst.dosage.rateQuantity.system == "http://unitsofmeasure.org"
    assert inst.dosage.rateQuantity.unit == "min"
    assert float(inst.dosage.rateQuantity.value) == float(20)
    assert inst.dosage.route.coding[0].code == "255560000"
    assert inst.dosage.route.coding[0].display == "Intravenous"
    assert inst.dosage.route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.text == "1.8 mg/kg IV infusion over 30 minutes"
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2015-01-15T14:30:00+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T04:30:00+01:00"
    )
    assert inst.id == "medadmin0305"
    assert inst.instantiates[0] == (
        "http://www.bccancer.bc.ca/chemotherapy-protocols-"
        "site/Documents/Lymphoma-"
        "Myeloma/ULYBRENTUX%20Protocol_1Jun2017.pdf"
    )
    assert inst.medicationReference.reference == "#med0306"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Patrick Pump"
    assert inst.performer[0].actor.reference == "Practitioner/f007"
    assert inst.request.reference == "MedicationRequest/medrx0316"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationadministration_9(base_settings):
    """No. 9 tests collection for MedicationAdministration.
    Test File: medicationadministration0305.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationadministration0305.json"
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_9(inst2)


def impl_medicationadministration_10(inst):
    assert inst.contained[0].id == "med0303"
    assert inst.context.display == "encounter who leads to this prescription"
    assert inst.context.reference == "Encounter/f001"
    assert inst.dosage.dose.code == "mg"
    assert inst.dosage.dose.system == "http://unitsofmeasure.org"
    assert inst.dosage.dose.unit == "mg"
    assert float(inst.dosage.dose.value) == float(3)
    assert inst.dosage.method.coding[0].code == "422145002"
    assert (
        inst.dosage.method.coding[0].display
        == "Inject - dosing instruction imperative (qualifier value)"
    )
    assert inst.dosage.method.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.route.coding[0].code == "47625008"
    assert inst.dosage.route.coding[0].display == "Intravenous route (qualifier value)"
    assert inst.dosage.route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage.text == (
        "Rapid daily-dose escalation, until tolerated, from 3 mg/d, "
        "and then 10 mg/d, to the recommended maintenance dose of 30 "
        "mg IV over 120 min, 3 times per wk on alternate days for up "
        "to 12 wk"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2015-01-15T14:30:00+01:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2015-01-15T04:30:00+01:00"
    )
    assert inst.id == "medadmin0304"
    assert inst.medicationReference.reference == "#med0303"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].actor.display == "Patrick Pump"
    assert inst.performer[0].actor.reference == "Practitioner/f007"
    assert inst.reasonReference[0].reference == "Condition/f202"
    assert inst.request.reference == "MedicationRequest/medrx0319"
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationadministration_10(base_settings):
    """No. 10 tests collection for MedicationAdministration.
    Test File: medicationadministration0304.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationadministration0304.json"
    inst = medicationadministration.MedicationAdministration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationAdministration" == inst.resource_type

    impl_medicationadministration_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationAdministration" == data["resourceType"]

    inst2 = medicationadministration.MedicationAdministration(**data)
    impl_medicationadministration_10(inst2)
