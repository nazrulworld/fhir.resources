# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import condition
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_condition_1(inst):
    assert inst.asserter.display == "P. van de Heuvel"
    assert inst.asserter.reference == "Patient/f001"
    assert inst.bodySite[0].coding[0].code == "280193007"
    assert inst.bodySite[0].coding[0].display == "Entire retropharyngeal area"
    assert (
        inst.bodySite[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.category[0].coding[0].code == "439401001"
    assert inst.category[0].coding[0].display == "diagnosis"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.clinicalStatus.coding[0].code == "active"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.coding[0].code == "18099001"
    assert inst.code.coding[0].display == "Retropharyngeal abscess"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.encounter.reference == "Encounter/f003"
    assert inst.evidence[0].code[0].coding[0].code == "169068008"
    assert inst.evidence[0].code[0].coding[0].display == "CT of neck"
    assert (
        inst.evidence[0].code[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.id == "f003"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.onsetDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2012-02-27"}
        ).valueDateTime
    )
    assert (
        inst.recordedDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2012-02-20"}
        ).valueDateTime
    )
    assert inst.severity.coding[0].code == "371923003"
    assert inst.severity.coding[0].display == "Mild to moderate"
    assert (
        inst.severity.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert (
        inst.verificationStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-ver-status"}
        ).valueUri
    )


def test_condition_1(base_settings):
    """No. 1 tests collection for Condition.
    Test File: condition-example-f003-abscess.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-f003-abscess.json"
    )
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_1(inst2)


def impl_condition_2(inst):
    assert inst.asserter.reference == "Practitioner/f201"
    assert inst.bodySite[0].coding[0].code == "281158006"
    assert inst.bodySite[0].coding[0].display == "Pulmonary vascular structure"
    assert (
        inst.bodySite[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.category[0].coding[0].code == "55607006"
    assert inst.category[0].coding[0].display == "Problem"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.category[0].coding[1].code == "problem-list-item"
    assert (
        inst.category[0].coding[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-category"}
        ).valueUri
    )
    assert inst.clinicalStatus.coding[0].code == "active"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.coding[0].code == "10001005"
    assert inst.code.coding[0].display == "Bacterial sepsis"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.encounter.display == "Roel's encounter on March elevanth"
    assert inst.encounter.reference == "Encounter/f203"
    assert inst.evidence[0].detail[0].display == "Diagnostic report for Roel's sepsis"
    assert inst.evidence[0].detail[0].reference == "DiagnosticReport/f202"
    assert inst.id == "f203"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.onsetDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-03-08"}
        ).valueDateTime
    )
    assert (
        inst.recordedDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-03-11"}
        ).valueDateTime
    )
    assert inst.severity.coding[0].code == "371924009"
    assert inst.severity.coding[0].display == "Moderate to severe"
    assert (
        inst.severity.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert (
        inst.verificationStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-ver-status"}
        ).valueUri
    )


def test_condition_2(base_settings):
    """No. 2 tests collection for Condition.
    Test File: condition-example-f203-sepsis.json
    """
    filename = base_settings["unittest_data_dir"] / "condition-example-f203-sepsis.json"
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_2(inst2)


def impl_condition_3(inst):
    assert inst.category[0].coding[0].code == "encounter-diagnosis"
    assert inst.category[0].coding[0].display == "Encounter Diagnosis"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-category"}
        ).valueUri
    )
    assert inst.clinicalStatus.coding[0].code == "active"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.coding[0].code == "422504002"
    assert inst.code.coding[0].display == "Ischemic stroke (disorder)"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.code.text == "Stroke"
    assert inst.id == "stroke"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.onsetDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2010-07-18"}
        ).valueDateTime
    )
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Ischemic stroke,'
        " July 18, 2010</div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert (
        inst.verificationStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-ver-status"}
        ).valueUri
    )


def test_condition_3(base_settings):
    """No. 3 tests collection for Condition.
    Test File: condition-example-stroke.json
    """
    filename = base_settings["unittest_data_dir"] / "condition-example-stroke.json"
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_3(inst2)


def impl_condition_4(inst):
    assert inst.category[0].coding[0].code == "problem-list-item"
    assert inst.category[0].coding[0].display == "Problem List Item"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-category"}
        ).valueUri
    )
    assert inst.clinicalStatus.coding[0].code == "active"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.coding[0].code == "312824007"
    assert inst.code.coding[0].display == "Family history of cancer of colon"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.id == "family-history"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Family history '
        "of cancer of colon</div>"
    )
    assert inst.text.status == "generated"


def test_condition_4(base_settings):
    """No. 4 tests collection for Condition.
    Test File: condition-example-family-history.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-family-history.json"
    )
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_4(inst2)


def impl_condition_5(inst):
    assert inst.asserter.display == "P. van de Heuvel"
    assert inst.asserter.reference == "Patient/f001"
    assert inst.bodySite[0].coding[0].code == "51185008"
    assert inst.bodySite[0].coding[0].display == "Thorax"
    assert (
        inst.bodySite[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.category[0].coding[0].code == "439401001"
    assert inst.category[0].coding[0].display == "diagnosis"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.clinicalStatus.coding[0].code == "active"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.coding[0].code == "254637007"
    assert inst.code.coding[0].display == "NSCLC - Non-small cell lung cancer"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.encounter.reference == "Encounter/f002"
    assert inst.evidence[0].code[0].coding[0].code == "169069000"
    assert inst.evidence[0].code[0].coding[0].display == "CT of thorax"
    assert (
        inst.evidence[0].code[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.id == "f002"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.onsetDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2011-05-05"}
        ).valueDateTime
    )
    assert (
        inst.recordedDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2012-06-03"}
        ).valueDateTime
    )
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert (
        inst.severity.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.stage[0].summary.coding[0].code == "258219007"
    assert inst.stage[0].summary.coding[0].display == "stage II"
    assert (
        inst.stage[0].summary.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.stage[0].type.coding[0].code == "260998006"
    assert inst.stage[0].type.coding[0].display == "Clinical staging (qualifier value)"
    assert (
        inst.stage[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert (
        inst.verificationStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-ver-status"}
        ).valueUri
    )


def test_condition_5(base_settings):
    """No. 5 tests collection for Condition.
    Test File: condition-example-f002-lung.json
    """
    filename = base_settings["unittest_data_dir"] / "condition-example-f002-lung.json"
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_5(inst2)


def impl_condition_6(inst):
    assert inst.asserter.reference == "Practitioner/f201"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.coding[0].code == "87628006"
    assert inst.code.coding[0].display == "Bacterial infectious disease"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.id == "f205"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.recordedDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-04-04"}
        ).valueDateTime
    )
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "differential"
    assert (
        inst.verificationStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-ver-status"}
        ).valueUri
    )


def test_condition_6(base_settings):
    """No. 6 tests collection for Condition.
    Test File: condition-example-f205-infection.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-f205-infection.json"
    )
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_6(inst2)


def impl_condition_7(inst):
    assert (
        inst.abatementDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-03-20"}
        ).valueDateTime
    )
    assert inst.asserter.reference == "Practitioner/f201"
    assert inst.bodySite[0].coding[0].code == "181414000"
    assert inst.bodySite[0].coding[0].display == "Kidney"
    assert (
        inst.bodySite[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.category[0].coding[0].code == "55607006"
    assert inst.category[0].coding[0].display == "Problem"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.category[0].coding[1].code == "problem-list-item"
    assert (
        inst.category[0].coding[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-category"}
        ).valueUri
    )
    assert inst.clinicalStatus.coding[0].code == "inactive"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.coding[0].code == "36225005"
    assert (
        inst.code.coding[0].display
        == "Acute renal insufficiency specified as due to procedure"
    )
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.encounter.display == "Roel's encounter on March elevanth"
    assert inst.encounter.reference == "Encounter/f203"
    assert inst.id == "f204"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == "The patient is anuric."
    assert (
        inst.onsetDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-03-11"}
        ).valueDateTime
    )
    assert (
        inst.recordedDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-03-11"}
        ).valueDateTime
    )
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert (
        inst.severity.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.stage[0].assessment[0].display == "Genetic analysis master panel"
    assert inst.stage[0].summary.coding[0].code == "14803004"
    assert inst.stage[0].summary.coding[0].display == "Temporary"
    assert (
        inst.stage[0].summary.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "differential"
    assert (
        inst.verificationStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-ver-status"}
        ).valueUri
    )


def test_condition_7(base_settings):
    """No. 7 tests collection for Condition.
    Test File: condition-example-f204-renal.json
    """
    filename = base_settings["unittest_data_dir"] / "condition-example-f204-renal.json"
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_7(inst2)


def impl_condition_8(inst):
    assert inst.category[0].coding[0].code == "problem-list-item"
    assert inst.category[0].coding[0].display == "Problem List Item"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-category"}
        ).valueUri
    )
    assert inst.clinicalStatus.coding[0].code == "active"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.text == "Asthma"
    assert inst.id == "example2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.onsetString == "approximately November 2012"
    assert inst.severity.coding[0].code == "255604002"
    assert inst.severity.coding[0].display == "Mild"
    assert (
        inst.severity.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Mild Asthma '
        "(Date: 12-Nov 2012)</div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert (
        inst.verificationStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-ver-status"}
        ).valueUri
    )


def test_condition_8(base_settings):
    """No. 8 tests collection for Condition.
    Test File: condition-example2.json
    """
    filename = base_settings["unittest_data_dir"] / "condition-example2.json"
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_8(inst2)


def impl_condition_9(inst):
    assert inst.abatementAge.code == "a"
    assert (
        inst.abatementAge.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.abatementAge.unit == "years"
    assert float(inst.abatementAge.value) == float(54)
    assert inst.bodySite[0].coding[0].code == "361355005"
    assert inst.bodySite[0].coding[0].display == "Entire head and neck"
    assert (
        inst.bodySite[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.category[0].coding[0].code == "encounter-diagnosis"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-category"}
        ).valueUri
    )
    assert inst.clinicalStatus.coding[0].code == "resolved"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.coding[0].code == "363346000"
    assert inst.code.coding[0].display == "Malignant neoplastic disease"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert (
        inst.evidence[0].detail[0].display
        == "Erasmus' diagnostic report of Roel's tumor"
    )
    assert inst.evidence[0].detail[0].reference == "DiagnosticReport/f201"
    assert inst.id == "f202"
    assert inst.meta.security[0].code == "TBOO"
    assert inst.meta.security[0].display == "taboo"
    assert (
        inst.meta.security[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
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
    assert inst.onsetAge.code == "a"
    assert (
        inst.onsetAge.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.onsetAge.unit == "years"
    assert float(inst.onsetAge.value) == float(52)
    assert (
        inst.recordedDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2012-12-01"}
        ).valueDateTime
    )
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert (
        inst.severity.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert (
        inst.verificationStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-ver-status"}
        ).valueUri
    )


def test_condition_9(base_settings):
    """No. 9 tests collection for Condition.
    Test File: condition-example-f202-malignancy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-f202-malignancy.json"
    )
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_9(inst2)


def impl_condition_10(inst):
    assert inst.abatementString == "around April 9, 2013"
    assert inst.asserter.reference == "Practitioner/f201"
    assert inst.bodySite[0].coding[0].code == "38266002"
    assert inst.bodySite[0].coding[0].display == "Entire body as a whole"
    assert (
        inst.bodySite[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.category[0].coding[0].code == "55607006"
    assert inst.category[0].coding[0].display == "Problem"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.category[0].coding[1].code == "problem-list-item"
    assert (
        inst.category[0].coding[1].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-category"}
        ).valueUri
    )
    assert inst.clinicalStatus.coding[0].code == "resolved"
    assert (
        inst.clinicalStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-clinical"}
        ).valueUri
    )
    assert inst.code.coding[0].code == "386661006"
    assert inst.code.coding[0].display == "Fever"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.encounter.reference == "Encounter/f201"
    assert inst.evidence[0].code[0].coding[0].code == "258710007"
    assert inst.evidence[0].code[0].coding[0].display == "degrees C"
    assert (
        inst.evidence[0].code[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.evidence[0].detail[0].display == "Temperature"
    assert inst.evidence[0].detail[0].reference == "Observation/f202"
    assert inst.id == "f201"
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.onsetDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-04-02"}
        ).valueDateTime
    )
    assert (
        inst.recordedDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-04-04"}
        ).valueDateTime
    )
    assert inst.recorder.reference == "Practitioner/f201"
    assert inst.severity.coding[0].code == "255604002"
    assert inst.severity.coding[0].display == "Mild"
    assert (
        inst.severity.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert (
        inst.verificationStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/condition-ver-status"}
        ).valueUri
    )


def test_condition_10(base_settings):
    """No. 10 tests collection for Condition.
    Test File: condition-example-f201-fever.json
    """
    filename = base_settings["unittest_data_dir"] / "condition-example-f201-fever.json"
    inst = condition.Condition.model_validate_json(filename.read_bytes())
    assert "Condition" == inst.get_resource_type()

    impl_condition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_condition_10(inst2)
