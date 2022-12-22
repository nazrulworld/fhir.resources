# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicationstatement


def impl_medicationstatement_1(inst):
    assert inst.basedOn[0].reference == "CarePlan/gpvisit"
    assert inst.context.reference == "Encounter/f203"
    assert inst.dateAsserted == fhirtypes.DateTime.validate("2015-02-22")
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2014-01-23")
    assert inst.id == "example005"
    assert inst.informationSource.display == "Donald Duck"
    assert inst.informationSource.reference == "Patient/pat1"
    assert inst.medicationCodeableConcept.coding[0].code == "27658006"
    assert inst.medicationCodeableConcept.coding[0].display == "Amoxicillin (product)"
    assert inst.medicationCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == (
        "Patient indicated that they thought it was Amoxicillin they "
        "were taking but it was really Erythromycin"
    )
    assert inst.status == "entered-in-error"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_1(base_settings):
    """No. 1 tests collection for MedicationStatement.
    Test File: medicationstatementexample5.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample5.json"
    inst = medicationstatement.MedicationStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationStatement" == inst.resource_type

    impl_medicationstatement_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_1(inst2)


def impl_medicationstatement_2(inst):
    assert inst.dateAsserted == fhirtypes.DateTime.validate("2015-02-22")
    assert inst.dosage[0].asNeededBoolean is False
    assert inst.dosage[0].maxDosePerPeriod.denominator.code == "d"
    assert (
        inst.dosage[0].maxDosePerPeriod.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.dosage[0].maxDosePerPeriod.denominator.value) == float(1)
    assert inst.dosage[0].maxDosePerPeriod.numerator.code == "385055001"
    assert inst.dosage[0].maxDosePerPeriod.numerator.system == "http://snomed.info/sct"
    assert inst.dosage[0].maxDosePerPeriod.numerator.unit == "capsules"
    assert float(inst.dosage[0].maxDosePerPeriod.numerator.value) == float(3)
    assert inst.dosage[0].route.coding[0].code == "260548002"
    assert inst.dosage[0].route.coding[0].display == "Oral"
    assert inst.dosage[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage[0].text == "one capsule three times daily"
    assert inst.dosage[0].timing.repeat.frequency == 3
    assert float(inst.dosage[0].timing.repeat.period) == float(1)
    assert inst.dosage[0].timing.repeat.periodUnit == "d"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2014-01-23")
    assert inst.id == "example004"
    assert inst.informationSource.display == "Donald Duck"
    assert inst.informationSource.reference == "Patient/pat1"
    assert inst.medicationCodeableConcept.coding[0].code == "27658006"
    assert inst.medicationCodeableConcept.coding[0].display == "Amoxicillin (product)"
    assert inst.medicationCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Patient indicates they miss the occasional dose"
    assert inst.partOf[0].reference == "Observation/blood-pressure"
    assert inst.reasonCode[0].coding[0].code == "65363002"
    assert inst.reasonCode[0].coding[0].display == "Otitis Media"
    assert inst.reasonCode[0].coding[0].system == "http://snomed.info/sct"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_2(base_settings):
    """No. 2 tests collection for MedicationStatement.
    Test File: medicationstatementexample4.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample4.json"
    inst = medicationstatement.MedicationStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationStatement" == inst.resource_type

    impl_medicationstatement_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_2(inst2)


def impl_medicationstatement_3(inst):
    assert inst.dateAsserted == fhirtypes.DateTime.validate("2014-02-22")
    assert inst.dosage[0].asNeededBoolean is False
    assert inst.dosage[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosage[0].doseAndRate[0].doseQuantity.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosage[0].doseAndRate[0].doseQuantity.unit == "tab"
    assert float(inst.dosage[0].doseAndRate[0].doseQuantity.value) == float(1)
    assert inst.dosage[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosage[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosage[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosage[0].maxDosePerPeriod.denominator.code == "d"
    assert (
        inst.dosage[0].maxDosePerPeriod.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.dosage[0].maxDosePerPeriod.denominator.value) == float(1)
    assert float(inst.dosage[0].maxDosePerPeriod.numerator.value) == float(1)
    assert inst.dosage[0].route.coding[0].code == "260548002"
    assert inst.dosage[0].route.coding[0].display == "Oral"
    assert inst.dosage[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage[0].sequence == 1
    assert inst.dosage[0].text == "1 tablet per day"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2014-02-01")
    assert inst.id == "example003"
    assert inst.informationSource.display == "Donald Duck"
    assert inst.informationSource.reference == "Patient/pat1"
    assert inst.medicationCodeableConcept.text == "Little Pink Pill for water retention"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == (
        "Patient cannot remember the name of the tablet, but takes it"
        " every day in the morning for water retention"
    )
    assert inst.reasonReference[0].reference == "Observation/blood-pressure"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_3(base_settings):
    """No. 3 tests collection for MedicationStatement.
    Test File: medicationstatementexample3.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample3.json"
    inst = medicationstatement.MedicationStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationStatement" == inst.resource_type

    impl_medicationstatement_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_3(inst2)


def impl_medicationstatement_4(inst):
    assert inst.contained[0].id == "med0309"
    assert inst.dateAsserted == fhirtypes.DateTime.validate("2015-02-22")
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2015-01-23")
    assert inst.id == "example002"
    assert inst.informationSource.display == "Donald Duck"
    assert inst.informationSource.reference == "Patient/pat1"
    assert inst.medicationReference.reference == "#med0309"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.note[0].text == "Patient cannot take acetaminophen as per Dr instructions"
    )
    assert inst.status == "active"
    assert inst.statusReason[0].coding[0].code == "166643006"
    assert inst.statusReason[0].coding[0].display == "Liver enzymes abnormal"
    assert inst.statusReason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_4(base_settings):
    """No. 4 tests collection for MedicationStatement.
    Test File: medicationstatementexample2.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample2.json"
    inst = medicationstatement.MedicationStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationStatement" == inst.resource_type

    impl_medicationstatement_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_4(inst2)


def impl_medicationstatement_5(inst):
    assert inst.category.coding[0].code == "inpatient"
    assert inst.category.coding[0].display == "Inpatient"
    assert inst.category.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/medication-statement-" "category"
    )
    assert inst.contained[0].id == "med0309"
    assert inst.dateAsserted == fhirtypes.DateTime.validate("2015-02-22")
    assert inst.derivedFrom[0].reference == "MedicationRequest/medrx002"
    assert inst.dosage[0].additionalInstruction[0].text == "Taking at bedtime"
    assert inst.dosage[0].asNeededCodeableConcept.coding[0].code == "32914008"
    assert inst.dosage[0].asNeededCodeableConcept.coding[0].display == "Restless Legs"
    assert (
        inst.dosage[0].asNeededCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.dosage[0].doseAndRate[0].doseRange.high.code == "TAB"
    assert (
        inst.dosage[0].doseAndRate[0].doseRange.high.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosage[0].doseAndRate[0].doseRange.high.unit == "TAB"
    assert float(inst.dosage[0].doseAndRate[0].doseRange.high.value) == float(2)
    assert inst.dosage[0].doseAndRate[0].doseRange.low.code == "TAB"
    assert (
        inst.dosage[0].doseAndRate[0].doseRange.low.system
        == "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"
    )
    assert inst.dosage[0].doseAndRate[0].doseRange.low.unit == "TAB"
    assert float(inst.dosage[0].doseAndRate[0].doseRange.low.value) == float(1)
    assert inst.dosage[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosage[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosage[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosage[0].route.coding[0].code == "26643006"
    assert inst.dosage[0].route.coding[0].display == "Oral Route"
    assert inst.dosage[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage[0].sequence == 1
    assert inst.dosage[0].text == (
        "1-2 tablets once daily at bedtime as needed for restless " "legs"
    )
    assert inst.dosage[0].timing.repeat.frequency == 1
    assert float(inst.dosage[0].timing.repeat.period) == float(1)
    assert inst.dosage[0].timing.repeat.periodUnit == "d"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2015-01-23")
    assert inst.id == "example001"
    assert inst.identifier[0].system == "http://www.bmc.nl/portal/medstatements"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.informationSource.display == "Donald Duck"
    assert inst.informationSource.reference == "Patient/pat1"
    assert inst.medicationReference.reference == "#med0309"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Patient indicates they miss the occasional dose"
    assert inst.reasonCode[0].coding[0].code == "32914008"
    assert inst.reasonCode[0].coding[0].display == "Restless Legs"
    assert inst.reasonCode[0].coding[0].system == "http://snomed.info/sct"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_5(base_settings):
    """No. 5 tests collection for MedicationStatement.
    Test File: medicationstatementexample1.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample1.json"
    inst = medicationstatement.MedicationStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationStatement" == inst.resource_type

    impl_medicationstatement_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_5(inst2)


def impl_medicationstatement_6(inst):
    assert inst.contained[0].id == "med0315"
    assert inst.id == "example007"
    assert inst.informationSource.display == "Donald Duck"
    assert inst.informationSource.reference == "Patient/pat1"
    assert inst.medicationReference.reference == "#med0315"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == (
        "patient plans to start using for seasonal allergies in the "
        "Spring when pollen is in the air"
    )
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_6(base_settings):
    """No. 6 tests collection for MedicationStatement.
    Test File: medicationstatementexample7.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample7.json"
    inst = medicationstatement.MedicationStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationStatement" == inst.resource_type

    impl_medicationstatement_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_6(inst2)


def impl_medicationstatement_7(inst):
    assert inst.dateAsserted == fhirtypes.DateTime.validate("2014-02-22")
    assert inst.dosage[0].asNeededBoolean is False
    assert inst.dosage[0].doseAndRate[0].doseQuantity.code == "mL"
    assert (
        inst.dosage[0].doseAndRate[0].doseQuantity.system == "http://unitsofmeasure.org"
    )
    assert inst.dosage[0].doseAndRate[0].doseQuantity.unit == "mL"
    assert float(inst.dosage[0].doseAndRate[0].doseQuantity.value) == float(5)
    assert inst.dosage[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosage[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosage[0].doseAndRate[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/dose-rate-type"
    )
    assert inst.dosage[0].maxDosePerPeriod.denominator.code == "d"
    assert (
        inst.dosage[0].maxDosePerPeriod.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert float(inst.dosage[0].maxDosePerPeriod.denominator.value) == float(1)
    assert float(inst.dosage[0].maxDosePerPeriod.numerator.value) == float(3)
    assert inst.dosage[0].route.coding[0].code == "260548002"
    assert inst.dosage[0].route.coding[0].display == "Oral"
    assert inst.dosage[0].route.coding[0].system == "http://snomed.info/sct"
    assert inst.dosage[0].sequence == 1
    assert inst.dosage[0].text == "5ml three times daily"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2014-02-01")
    assert inst.id == "example006"
    assert inst.informationSource.display == "Peter Chalmers"
    assert inst.informationSource.reference == "RelatedPerson/peter"
    assert inst.medicationCodeableConcept.coding[0].code == "27658006"
    assert inst.medicationCodeableConcept.coding[0].display == "Amoxicillin (product)"
    assert inst.medicationCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Father indicates they miss the occasional dose"
    assert inst.status == "active"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_7(base_settings):
    """No. 7 tests collection for MedicationStatement.
    Test File: medicationstatementexample6.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample6.json"
    inst = medicationstatement.MedicationStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationStatement" == inst.resource_type

    impl_medicationstatement_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_7(inst2)
