# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import medicationstatement
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_medicationstatement_1(inst):
    assert (
        inst.dateAsserted
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-02-22"}
        ).valueDateTime
    )
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-01-23"}
        ).valueDateTime
    )
    assert inst.encounter.reference == "Encounter/f203"
    assert inst.id == "example005"
    assert inst.informationSource[0].display == "Donald Duck"
    assert inst.informationSource[0].reference == "Patient/pat1"
    assert inst.medication.concept.coding[0].code == "27658006"
    assert inst.medication.concept.coding[0].display == "Amoxicillin (product)"
    assert (
        inst.medication.concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
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
    inst = medicationstatement.MedicationStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationStatement" == inst.get_resource_type()

    impl_medicationstatement_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_1(inst2)


def impl_medicationstatement_2(inst):
    assert inst.contained[0].id == "med0315"
    assert (
        inst.dateAsserted
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-02-22"}
        ).valueDateTime
    )
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-01-23"}
        ).valueDateTime
    )
    assert inst.id == "example009"
    assert inst.informationSource[0].display == "Donald Duck"
    assert inst.informationSource[0].reference == "Patient/pat1"
    assert inst.medication.reference.reference == "#med0315"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.note[0].text
        == "Patient reports they used the medication patch on this day."
    )
    assert inst.partOf[0].reference == "MedicationStatement/example008"
    assert inst.status == "recorded"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_2(base_settings):
    """No. 2 tests collection for MedicationStatement.
    Test File: medicationstatementexample9.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample9.json"
    inst = medicationstatement.MedicationStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationStatement" == inst.get_resource_type()

    impl_medicationstatement_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_2(inst2)


def impl_medicationstatement_3(inst):
    assert inst.contained[0].id == "med0309"
    assert inst.dosage[0].doseAndRate[0].doseQuantity.code == "TPATH24"
    assert (
        inst.dosage[0].doseAndRate[0].doseQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"}
        ).valueUri
    )
    assert inst.dosage[0].doseAndRate[0].doseQuantity.unit == "patch"
    assert float(inst.dosage[0].doseAndRate[0].doseQuantity.value) == float(1)
    assert inst.id == "example008"
    assert inst.medication.reference.reference == "#med0309"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == (
        "Patient reports they used the given patches over the last 30" " days"
    )
    assert inst.status == "recorded"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_3(base_settings):
    """No. 3 tests collection for MedicationStatement.
    Test File: medicationstatementexample8.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample8.json"
    inst = medicationstatement.MedicationStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationStatement" == inst.get_resource_type()

    impl_medicationstatement_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_3(inst2)


def impl_medicationstatement_4(inst):
    assert inst.adherence.code.coding[0].code == "not-taking"
    assert inst.adherence.code.coding[0].display == "Not Taking"
    assert (
        inst.adherence.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/CodeSystem/medication-statement-adherence"
            }
        ).valueUri
    )
    assert inst.adherence.reason.coding[0].code == "266710000"
    assert inst.adherence.reason.coding[0].display == "Drugs not taken/completed"
    assert (
        inst.adherence.reason.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert (
        inst.dateAsserted
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-02-22"}
        ).valueDateTime
    )
    assert inst.dosage[0].asNeeded is False
    assert inst.dosage[0].maxDosePerPeriod[0].denominator.code == "d"
    assert (
        inst.dosage[0].maxDosePerPeriod[0].denominator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert float(inst.dosage[0].maxDosePerPeriod[0].denominator.value) == float(1)
    assert inst.dosage[0].maxDosePerPeriod[0].numerator.code == "385055001"
    assert (
        inst.dosage[0].maxDosePerPeriod[0].numerator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.dosage[0].maxDosePerPeriod[0].numerator.unit == "capsules"
    assert float(inst.dosage[0].maxDosePerPeriod[0].numerator.value) == float(3)
    assert inst.dosage[0].route.coding[0].code == "260548002"
    assert inst.dosage[0].route.coding[0].display == "Oral"
    assert (
        inst.dosage[0].route.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.dosage[0].text == "one capsule three times daily"
    assert inst.dosage[0].timing.repeat.frequency == 3
    assert float(inst.dosage[0].timing.repeat.period) == float(1)
    assert inst.dosage[0].timing.repeat.periodUnit == "d"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-01-23"}
        ).valueDateTime
    )
    assert inst.id == "example004"
    assert inst.informationSource[0].display == "Donald Duck"
    assert inst.informationSource[0].reference == "Patient/pat1"
    assert inst.medication.concept.coding[0].code == "27658006"
    assert inst.medication.concept.coding[0].display == "Amoxicillin (product)"
    assert (
        inst.medication.concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == "Patient indicates they miss the occasional dose"
    assert inst.status == "recorded"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_4(base_settings):
    """No. 4 tests collection for MedicationStatement.
    Test File: medicationstatementexample4.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample4.json"
    inst = medicationstatement.MedicationStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationStatement" == inst.get_resource_type()

    impl_medicationstatement_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_4(inst2)


def impl_medicationstatement_5(inst):
    assert (
        inst.dateAsserted
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-02-22"}
        ).valueDateTime
    )
    assert inst.dosage[0].asNeeded is False
    assert inst.dosage[0].doseAndRate[0].doseQuantity.code == "TAB"
    assert (
        inst.dosage[0].doseAndRate[0].doseQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"}
        ).valueUri
    )
    assert inst.dosage[0].doseAndRate[0].doseQuantity.unit == "tab"
    assert float(inst.dosage[0].doseAndRate[0].doseQuantity.value) == float(1)
    assert inst.dosage[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosage[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosage[0].doseAndRate[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/dose-rate-type"}
        ).valueUri
    )
    assert inst.dosage[0].maxDosePerPeriod[0].denominator.code == "d"
    assert (
        inst.dosage[0].maxDosePerPeriod[0].denominator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert float(inst.dosage[0].maxDosePerPeriod[0].denominator.value) == float(1)
    assert float(inst.dosage[0].maxDosePerPeriod[0].numerator.value) == float(1)
    assert inst.dosage[0].route.coding[0].code == "260548002"
    assert inst.dosage[0].route.coding[0].display == "Oral"
    assert (
        inst.dosage[0].route.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.dosage[0].sequence == 1
    assert inst.dosage[0].text == "1 tablet per day"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-02-01"}
        ).valueDateTime
    )
    assert inst.id == "example003"
    assert inst.informationSource[0].display == "Donald Duck"
    assert inst.informationSource[0].reference == "Patient/pat1"
    assert inst.medication.concept.text == "Little Pink Pill for water retention"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == (
        "Patient cannot remember the name of the tablet, but takes it"
        " every day in the morning for water retention"
    )
    assert inst.reason[0].reference.reference == "Observation/blood-pressure"
    assert inst.status == "recorded"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_5(base_settings):
    """No. 5 tests collection for MedicationStatement.
    Test File: medicationstatementexample3.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample3.json"
    inst = medicationstatement.MedicationStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationStatement" == inst.get_resource_type()

    impl_medicationstatement_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_5(inst2)


def impl_medicationstatement_6(inst):
    assert inst.adherence.code.coding[0].code == "not-taking"
    assert inst.adherence.code.coding[0].display == "Not Taking"
    assert (
        inst.adherence.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/CodeSystem/medication-statement-adherence"
            }
        ).valueUri
    )
    assert inst.adherence.reason.coding[0].code == "266710000"
    assert inst.adherence.reason.coding[0].display == "Drugs not taken/completed"
    assert (
        inst.adherence.reason.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.contained[0].id == "med0309"
    assert (
        inst.dateAsserted
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-02-22"}
        ).valueDateTime
    )
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-01-23"}
        ).valueDateTime
    )
    assert inst.id == "example002"
    assert inst.informationSource[0].display == "Donald Duck"
    assert inst.informationSource[0].reference == "Patient/pat1"
    assert inst.medication.reference.reference == "#med0309"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.note[0].text == "Patient cannot take acetaminophen as per Dr instructions"
    )
    assert inst.reason[0].concept.coding[0].code == "166643006"
    assert inst.reason[0].concept.coding[0].display == "Liver enzymes abnormal"
    assert (
        inst.reason[0].concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.status == "recorded"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_6(base_settings):
    """No. 6 tests collection for MedicationStatement.
    Test File: medicationstatementexample2.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample2.json"
    inst = medicationstatement.MedicationStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationStatement" == inst.get_resource_type()

    impl_medicationstatement_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_6(inst2)


def impl_medicationstatement_7(inst):
    assert inst.category[0].coding[0].code == "inpatient"
    assert inst.category[0].coding[0].display == "Inpatient"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/medication-statement-category"
            }
        ).valueUri
    )
    assert inst.contained[0].id == "med0309"
    assert (
        inst.dateAsserted
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-02-22"}
        ).valueDateTime
    )
    assert inst.derivedFrom[0].reference == "MedicationRequest/medrx002"
    assert inst.dosage[0].additionalInstruction[0].text == "Taking at bedtime"
    assert inst.dosage[0].asNeededFor[0].coding[0].code == "32914008"
    assert inst.dosage[0].asNeededFor[0].coding[0].display == "Restless Legs"
    assert (
        inst.dosage[0].asNeededFor[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.dosage[0].doseAndRate[0].doseRange.high.code == "TAB"
    assert (
        inst.dosage[0].doseAndRate[0].doseRange.high.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"}
        ).valueUri
    )
    assert inst.dosage[0].doseAndRate[0].doseRange.high.unit == "TAB"
    assert float(inst.dosage[0].doseAndRate[0].doseRange.high.value) == float(2)
    assert inst.dosage[0].doseAndRate[0].doseRange.low.code == "TAB"
    assert (
        inst.dosage[0].doseAndRate[0].doseRange.low.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"}
        ).valueUri
    )
    assert inst.dosage[0].doseAndRate[0].doseRange.low.unit == "TAB"
    assert float(inst.dosage[0].doseAndRate[0].doseRange.low.value) == float(1)
    assert inst.dosage[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosage[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosage[0].doseAndRate[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/dose-rate-type"}
        ).valueUri
    )
    assert inst.dosage[0].route.coding[0].code == "26643006"
    assert inst.dosage[0].route.coding[0].display == "Oral Route"
    assert (
        inst.dosage[0].route.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.dosage[0].sequence == 1
    assert inst.dosage[0].text == (
        "1-2 tablets once daily at bedtime as needed for restless " "legs"
    )
    assert inst.dosage[0].timing.repeat.frequency == 1
    assert float(inst.dosage[0].timing.repeat.period) == float(1)
    assert inst.dosage[0].timing.repeat.periodUnit == "d"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-01-23"}
        ).valueDateTime
    )
    assert inst.id == "example001"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.bmc.nl/portal/medstatements"}
        ).valueUri
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345689"
    assert inst.informationSource[0].display == "Donald Duck"
    assert inst.informationSource[0].reference == "Patient/pat1"
    assert inst.medication.reference.reference == "#med0309"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == "Patient indicates they miss the occasional dose"
    assert inst.reason[0].concept.coding[0].code == "32914008"
    assert inst.reason[0].concept.coding[0].display == "Restless Legs"
    assert (
        inst.reason[0].concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.status == "recorded"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_7(base_settings):
    """No. 7 tests collection for MedicationStatement.
    Test File: medicationstatementexample1.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample1.json"
    inst = medicationstatement.MedicationStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationStatement" == inst.get_resource_type()

    impl_medicationstatement_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_7(inst2)


def impl_medicationstatement_8(inst):
    assert inst.contained[0].id == "med0315"
    assert inst.id == "example007"
    assert inst.informationSource[0].display == "Donald Duck"
    assert inst.informationSource[0].reference == "Patient/pat1"
    assert inst.medication.reference.reference == "#med0315"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == (
        "patient plans to start using for seasonal allergies in the "
        "Spring when pollen is in the air"
    )
    assert inst.status == "recorded"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_8(base_settings):
    """No. 8 tests collection for MedicationStatement.
    Test File: medicationstatementexample7.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample7.json"
    inst = medicationstatement.MedicationStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationStatement" == inst.get_resource_type()

    impl_medicationstatement_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_8(inst2)


def impl_medicationstatement_9(inst):
    assert (
        inst.dateAsserted
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-02-22"}
        ).valueDateTime
    )
    assert inst.dosage[0].asNeeded is False
    assert inst.dosage[0].doseAndRate[0].doseQuantity.code == "mL"
    assert (
        inst.dosage[0].doseAndRate[0].doseQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.dosage[0].doseAndRate[0].doseQuantity.unit == "mL"
    assert float(inst.dosage[0].doseAndRate[0].doseQuantity.value) == float(5)
    assert inst.dosage[0].doseAndRate[0].type.coding[0].code == "ordered"
    assert inst.dosage[0].doseAndRate[0].type.coding[0].display == "Ordered"
    assert (
        inst.dosage[0].doseAndRate[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/dose-rate-type"}
        ).valueUri
    )
    assert inst.dosage[0].maxDosePerPeriod[0].denominator.code == "d"
    assert (
        inst.dosage[0].maxDosePerPeriod[0].denominator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert float(inst.dosage[0].maxDosePerPeriod[0].denominator.value) == float(1)
    assert float(inst.dosage[0].maxDosePerPeriod[0].numerator.value) == float(3)
    assert inst.dosage[0].route.coding[0].code == "260548002"
    assert inst.dosage[0].route.coding[0].display == "Oral"
    assert (
        inst.dosage[0].route.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.dosage[0].sequence == 1
    assert inst.dosage[0].text == "5ml three times daily"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-02-01"}
        ).valueDateTime
    )
    assert inst.id == "example006"
    assert inst.informationSource[0].display == "Peter Chalmers"
    assert inst.informationSource[0].reference == "RelatedPerson/peter"
    assert inst.medication.concept.coding[0].code == "27658006"
    assert inst.medication.concept.coding[0].display == "Amoxicillin (product)"
    assert (
        inst.medication.concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == "Father indicates they miss the occasional dose"
    assert inst.status == "recorded"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.status == "generated"


def test_medicationstatement_9(base_settings):
    """No. 9 tests collection for MedicationStatement.
    Test File: medicationstatementexample6.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationstatementexample6.json"
    inst = medicationstatement.MedicationStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationStatement" == inst.get_resource_type()

    impl_medicationstatement_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationStatement" == data["resourceType"]

    inst2 = medicationstatement.MedicationStatement(**data)
    impl_medicationstatement_9(inst2)
