# -*- coding: utf-8 -*-
from datetime import date
from decimal import Decimal

from .. import fhirtypes  # noqa: F401
from .. import condition


def test_Condition_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "condition-example-f001-heart.canonical.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_1(inst2)


def impl_Condition_1(inst):
    assert inst.asserter.display == "P. van de Heuvel"
    assert inst.asserter.reference == "Patient/f001"
    assert inst.bodySite[0].coding[0].code == "40768004"
    assert inst.bodySite[0].coding[0].display == "Left thorax"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite[0].text == "heart structure"
    assert inst.category.coding[0].code == "439401001"
    assert inst.category.coding[0].display == "diagnosis"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "368009"
    assert inst.code.coding[0].display == "Heart valve disorder"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.dateRecorded == date(2011, 10, 5)
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.evidence[0].code.coding[0].code == "426396005"
    assert inst.evidence[0].code.coding[0].display == "Cardiac chest pain"
    assert inst.evidence[0].code.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "f001"
    assert inst.onsetDateTime == date(2011, 8, 5)
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.severity.coding[0].code == "6736007"
    assert inst.severity.coding[0].display == "Moderate"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f001</p><p><b>patient</b>: <a>P. van de Heuvel</a></p><p><b>encounter</b>: <a>Encounter/f001</a></p><p><b>asserter</b>: <a>P. van de Heuvel</a></p><p><b>dateRecorded</b>: 05/10/2011</p><p><b>code</b>: Heart valve disorder <span>(Details : {SNOMED CT code '368009' = '368009', given as 'Heart valve disorder'})</span></p><p><b>category</b>: diagnosis <span>(Details : {SNOMED CT code '439401001' = '439401001', given as 'diagnosis'})</span></p><p><b>clinicalStatus</b>: active</p><p><b>verificationStatus</b>: confirmed</p><p><b>severity</b>: Moderate <span>(Details : {SNOMED CT code '6736007' = '6736007', given as 'Moderate'})</span></p><p><b>onset</b>: 05/08/2011</p><h3>Evidences</h3><table><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Cardiac chest pain <span>(Details : {SNOMED CT code '426396005' = '426396005', given as 'Cardiac chest pain'})</span></td></tr></table><p><b>bodySite</b>: heart structure <span>(Details : {SNOMED CT code '40768004' = '40768004', given as 'Left thorax'})</span></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "confirmed"


def test_Condition_2(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "condition-example-f002-lung.canonical.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_2(inst2)


def impl_Condition_2(inst):
    assert inst.asserter.display == "P. van de Heuvel"
    assert inst.asserter.reference == "Patient/f001"
    assert inst.bodySite[0].coding[0].code == "51185008"
    assert inst.bodySite[0].coding[0].display == "Thorax"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[0].code == "439401001"
    assert inst.category.coding[0].display == "diagnosis"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "254637007"
    assert inst.code.coding[0].display == "NSCLC - Non-small cell lung cancer"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.dateRecorded == date(2012, 6, 3)
    assert inst.encounter.reference == "Encounter/f002"
    assert inst.evidence[0].code.coding[0].code == "169069000"
    assert inst.evidence[0].code.coding[0].display == "CT of thorax"
    assert inst.evidence[0].code.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "f002"
    assert inst.onsetDateTime == date(2011, 5, 5)
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.stage.summary.coding[0].code == "258219007"
    assert inst.stage.summary.coding[0].display == "stage II"
    assert inst.stage.summary.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f002</p><p><b>patient</b>: <a>P. van de Heuvel</a></p><p><b>encounter</b>: <a>Encounter/f002</a></p><p><b>asserter</b>: <a>P. van de Heuvel</a></p><p><b>dateRecorded</b>: 03/06/2012</p><p><b>code</b>: NSCLC - Non-small cell lung cancer <span>(Details : {SNOMED CT code '254637007' = '254637007', given as 'NSCLC - Non-small cell lung cancer'})</span></p><p><b>category</b>: diagnosis <span>(Details : {SNOMED CT code '439401001' = '439401001', given as 'diagnosis'})</span></p><p><b>clinicalStatus</b>: active</p><p><b>verificationStatus</b>: confirmed</p><p><b>severity</b>: Severe <span>(Details : {SNOMED CT code '24484000' = '24484000', given as 'Severe'})</span></p><p><b>onset</b>: 05/05/2011</p><h3>Stages</h3><table><tr><td>-</td><td><b>Summary</b></td></tr><tr><td>*</td><td>stage II <span>(Details : {SNOMED CT code '258219007' = '258219007', given as 'stage II'})</span></td></tr></table><h3>Evidences</h3><table><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>CT of thorax <span>(Details : {SNOMED CT code '169069000' = '169069000', given as 'CT of thorax'})</span></td></tr></table><p><b>bodySite</b>: Thorax <span>(Details : {SNOMED CT code '51185008' = '51185008', given as 'Thorax'})</span></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "confirmed"


def test_Condition_3(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "condition-example-f003-abscess.canonical.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_3(inst2)


def impl_Condition_3(inst):
    assert inst.asserter.display == "P. van de Heuvel"
    assert inst.asserter.reference == "Patient/f001"
    assert inst.bodySite[0].coding[0].code == "280193007"
    assert inst.bodySite[0].coding[0].display == "Entire retropharyngeal area"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[0].code == "439401001"
    assert inst.category.coding[0].display == "diagnosis"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "18099001"
    assert inst.code.coding[0].display == "Retropharyngeal abscess"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.dateRecorded == date(2012, 2, 20)
    assert inst.encounter.reference == "Encounter/f003"
    assert inst.evidence[0].code.coding[0].code == "169068008"
    assert inst.evidence[0].code.coding[0].display == "CT of neck"
    assert inst.evidence[0].code.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "f003"
    assert inst.onsetDateTime == date(2012, 2, 27)
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.severity.coding[0].code == "371923003"
    assert inst.severity.coding[0].display == "Mild to moderate"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f003</p><p><b>patient</b>: <a>P. van de Heuvel</a></p><p><b>encounter</b>: <a>Encounter/f003</a></p><p><b>asserter</b>: <a>P. van de Heuvel</a></p><p><b>dateRecorded</b>: 20/02/2012</p><p><b>code</b>: Retropharyngeal abscess <span>(Details : {SNOMED CT code '18099001' = '18099001', given as 'Retropharyngeal abscess'})</span></p><p><b>category</b>: diagnosis <span>(Details : {SNOMED CT code '439401001' = '439401001', given as 'diagnosis'})</span></p><p><b>clinicalStatus</b>: active</p><p><b>verificationStatus</b>: confirmed</p><p><b>severity</b>: Mild to moderate <span>(Details : {SNOMED CT code '371923003' = '371923003', given as 'Mild to moderate'})</span></p><p><b>onset</b>: 27/02/2012</p><h3>Evidences</h3><table><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>CT of neck <span>(Details : {SNOMED CT code '169068008' = '169068008', given as 'CT of neck'})</span></td></tr></table><p><b>bodySite</b>: Entire retropharyngeal area <span>(Details : {SNOMED CT code '280193007' = '280193007', given as 'Entire retropharyngeal area'})</span></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "confirmed"


def test_Condition_4(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "condition-example-f201-fever.canonical.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_4(inst2)


def impl_Condition_4(inst):
    assert inst.asserter.reference == "Practitioner/f201"
    assert inst.bodySite[0].coding[0].code == "38266002"
    assert inst.bodySite[0].coding[0].display == "Entire body as a whole"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[0].code == "55607006"
    assert inst.category.coding[0].display == "Problem"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "finding"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/condition-category"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "386661006"
    assert inst.code.coding[0].display == "Fever"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.dateRecorded == date(2013, 4, 4)
    assert inst.encounter.reference == "Encounter/f201"
    assert inst.evidence[0].code.coding[0].code == "258710007"
    assert inst.evidence[0].code.coding[0].display == "degrees C"
    assert inst.evidence[0].code.coding[0].system == "http://snomed.info/sct"
    assert inst.evidence[0].detail[0].display == "Temperature"
    assert inst.evidence[0].detail[0].reference == "Observation/f202"
    assert inst.id == "f201"
    assert inst.onsetDateTime == date(2013, 4, 2)
    assert inst.patient.display == "Roel"
    assert inst.patient.reference == "Patient/f201"
    assert inst.severity.coding[0].code == "255604002"
    assert inst.severity.coding[0].display == "Mild"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f201</p><p><b>patient</b>: <a>Roel</a></p><p><b>encounter</b>: <a>Encounter/f201</a></p><p><b>asserter</b>: <a>Practitioner/f201</a></p><p><b>dateRecorded</b>: 04/04/2013</p><p><b>code</b>: Fever <span>(Details : {SNOMED CT code '386661006' = '386661006', given as 'Fever'})</span></p><p><b>category</b>: Problem <span>(Details : {SNOMED CT code '55607006' = '55607006', given as 'Problem'}; {http://hl7.org/fhir/condition-category code 'finding' = 'Finding)</span></p><p><b>clinicalStatus</b>: active</p><p><b>verificationStatus</b>: confirmed</p><p><b>severity</b>: Mild <span>(Details : {SNOMED CT code '255604002' = '255604002', given as 'Mild'})</span></p><p><b>onset</b>: 02/04/2013</p><h3>Evidences</h3><table><tr><td>-</td><td><b>Code</b></td><td><b>Detail</b></td></tr><tr><td>*</td><td>degrees C <span>(Details : {SNOMED CT code '258710007' = '258710007', given as 'degrees C'})</span></td><td><a>Temperature</a></td></tr></table><p><b>bodySite</b>: Entire body as a whole <span>(Details : {SNOMED CT code '38266002' = '38266002', given as 'Entire body as a whole'})</span></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "confirmed"


def test_Condition_5(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "condition-example-f202-malignancy.canonical.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_5(inst2)


def impl_Condition_5(inst):
    assert inst.bodySite[0].coding[0].code == "361355005"
    assert inst.bodySite[0].coding[0].display == "Entire head and neck"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[0].code == "diagnosis"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/condition-category"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "363346000"
    assert inst.code.coding[0].display == "Malignant neoplastic disease"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.dateRecorded == date(2012, 12, 1)
    assert (
        inst.evidence[0].detail[0].display
        == "Erasmus' diagnostic report of Roel's tumor"
    )
    assert inst.evidence[0].detail[0].reference == "DiagnosticReport/f201"
    assert inst.id == "f202"
    assert inst.onsetQuantity.code == "258707000"
    assert inst.onsetQuantity.system == "http://snomed.info/sct"
    assert inst.onsetQuantity.unit == "years"
    assert inst.onsetQuantity.value == Decimal("52")
    assert inst.patient.display == "Roel"
    assert inst.patient.reference == "Patient/f201"
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f202</p><p><b>patient</b>: <a>Roel</a></p><p><b>dateRecorded</b>: 01/12/2012</p><p><b>code</b>: Malignant neoplastic disease <span>(Details : {SNOMED CT code '363346000' = '363346000', given as 'Malignant neoplastic disease'})</span></p><p><b>category</b>: Diagnosis <span>(Details : {http://hl7.org/fhir/condition-category code 'diagnosis' = 'Diagnosis)</span></p><p><b>clinicalStatus</b>: active</p><p><b>verificationStatus</b>: confirmed</p><p><b>severity</b>: Severe <span>(Details : {SNOMED CT code '24484000' = '24484000', given as 'Severe'})</span></p><p><b>onset</b>: 52 years<span> (Details: SNOMED CT code 258707000 = '258707000')</span></p><h3>Evidences</h3><table><tr><td>-</td><td><b>Detail</b></td></tr><tr><td>*</td><td><a>Erasmus' diagnostic report of Roel's tumor</a></td></tr></table><p><b>bodySite</b>: Entire head and neck <span>(Details : {SNOMED CT code '361355005' = '361355005', given as 'Entire head and neck'})</span></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "confirmed"


def test_Condition_6(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "condition-example-f203-sepsis.canonical.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_6(inst2)


def impl_Condition_6(inst):
    assert inst.asserter.reference == "Practitioner/f201"
    assert inst.bodySite[0].coding[0].code == "281158006"
    assert inst.bodySite[0].coding[0].display == "Pulmonary vascular structure"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[0].code == "55607006"
    assert inst.category.coding[0].display == "Problem"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "finding"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/condition-category"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "10001005"
    assert inst.code.coding[0].display == "Bacterial sepsis"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.dateRecorded == date(2013, 3, 11)
    assert inst.encounter.display == "Roel's encounter on March eleventh"
    assert inst.encounter.reference == "Encounter/f203"
    assert inst.evidence[0].detail[0].display == "Diagnostic report for Roel's sepsis"
    assert inst.evidence[0].detail[0].reference == "DiagnosticReport/f202"
    assert inst.id == "f203"
    assert inst.onsetDateTime == date(2013, 3, 8)
    assert inst.patient.display == "Roel"
    assert inst.patient.reference == "Patient/f201"
    assert inst.severity.coding[0].code == "371924009"
    assert inst.severity.coding[0].display == "Moderate to severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f203</p><p><b>patient</b>: <a>Roel</a></p><p><b>encounter</b>: <a>Roel's encounter on March eleventh</a></p><p><b>asserter</b>: <a>Practitioner/f201</a></p><p><b>dateRecorded</b>: 11/03/2013</p><p><b>code</b>: Bacterial sepsis <span>(Details : {SNOMED CT code '10001005' = '10001005', given as 'Bacterial sepsis'})</span></p><p><b>category</b>: Problem <span>(Details : {SNOMED CT code '55607006' = '55607006', given as 'Problem'}; {http://hl7.org/fhir/condition-category code 'finding' = 'Finding)</span></p><p><b>clinicalStatus</b>: active</p><p><b>verificationStatus</b>: confirmed</p><p><b>severity</b>: Moderate to severe <span>(Details : {SNOMED CT code '371924009' = '371924009', given as 'Moderate to severe'})</span></p><p><b>onset</b>: 08/03/2013</p><h3>Evidences</h3><table><tr><td>-</td><td><b>Detail</b></td></tr><tr><td>*</td><td><a>Diagnostic report for Roel's sepsis</a></td></tr></table><p><b>bodySite</b>: Pulmonary vascular structure <span>(Details : {SNOMED CT code '281158006' = '281158006', given as 'Pulmonary vascular structure'})</span></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "confirmed"


def test_Condition_7(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "condition-example-f204-renal.canonical.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_7(inst2)


def impl_Condition_7(inst):
    assert inst.abatementDateTime == date(2013, 3, 20)
    assert inst.asserter.reference == "Practitioner/f201"
    assert inst.bodySite[0].coding[0].code == "181414000"
    assert inst.bodySite[0].coding[0].display == "Kidney"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[0].code == "55607006"
    assert inst.category.coding[0].display == "Problem"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "finding"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/condition-category"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "36225005"
    assert (
        inst.code.coding[0].display
        == "Acute renal insufficiency specified as due to procedure"
    )
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.dateRecorded == date(2013, 3, 11)
    assert inst.encounter.display == "Roel's encounter on March eleventh"
    assert inst.encounter.reference == "Encounter/f203"
    assert inst.id == "f204"
    assert inst.onsetDateTime == date(2013, 3, 11)
    assert inst.patient.display == "Roel"
    assert inst.patient.reference == "Patient/f201"
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.stage.summary.coding[0].code == "14803004"
    assert inst.stage.summary.coding[0].display == "Temporary"
    assert inst.stage.summary.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f204</p><p><b>patient</b>: <a>Roel</a></p><p><b>encounter</b>: <a>Roel's encounter on March eleventh</a></p><p><b>asserter</b>: <a>Practitioner/f201</a></p><p><b>dateRecorded</b>: 11/03/2013</p><p><b>code</b>: Acute renal insufficiency specified as due to procedure <span>(Details : {SNOMED CT code '36225005' = '36225005', given as 'Acute renal insufficiency specified as due to procedure'})</span></p><p><b>category</b>: Problem <span>(Details : {SNOMED CT code '55607006' = '55607006', given as 'Problem'}; {http://hl7.org/fhir/condition-category code 'finding' = 'Finding)</span></p><p><b>clinicalStatus</b>: active</p><p><b>verificationStatus</b>: differential</p><p><b>severity</b>: Severe <span>(Details : {SNOMED CT code '24484000' = '24484000', given as 'Severe'})</span></p><p><b>onset</b>: 11/03/2013</p><p><b>abatement</b>: 20/03/2013</p><h3>Stages</h3><table><tr><td>-</td><td><b>Summary</b></td></tr><tr><td>*</td><td>Temporary <span>(Details : {SNOMED CT code '14803004' = '14803004', given as 'Temporary'})</span></td></tr></table><p><b>bodySite</b>: Kidney <span>(Details : {SNOMED CT code '181414000' = '181414000', given as 'Kidney'})</span></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "differential"


def test_Condition_8(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "condition-example-f205-infection.canonical.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_8(inst2)


def impl_Condition_8(inst):
    assert inst.asserter.reference == "Practitioner/f201"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "87628006"
    assert inst.code.coding[0].display == "Bacterial infectious disease"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.dateRecorded == date(2013, 4, 4)
    assert inst.id == "f205"
    assert inst.patient.display == "Roel"
    assert inst.patient.reference == "Patient/f201"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f205</p><p><b>patient</b>: <a>Roel</a></p><p><b>asserter</b>: <a>Practitioner/f201</a></p><p><b>dateRecorded</b>: 04/04/2013</p><p><b>code</b>: Bacterial infectious disease <span>(Details : {SNOMED CT code '87628006' = '87628006', given as 'Bacterial infectious disease'})</span></p><p><b>clinicalStatus</b>: active</p><p><b>verificationStatus</b>: differential</p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "differential"


def test_Condition_9(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "condition-example-stroke.canonical.json"
    )
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_9(inst2)


def impl_Condition_9(inst):
    assert inst.category.coding[0].code == "diagnosis"
    assert inst.category.coding[0].display == "Diagnosis"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/condition-category"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "422504002"
    assert inst.code.coding[0].display == "Ischemic stroke (disorder)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Stroke"
    assert inst.id == "stroke"
    assert inst.onsetDateTime == date(2010, 7, 18)
    assert inst.patient.reference == "Patient/example"
    assert inst.text.div == "<div>Ischemic stroke, July 18, 2010</div>"
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "confirmed"


def test_Condition_10(base_settings):
    filename = base_settings["unittest_data_dir"] / "condition-example.canonical.json"
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_10(inst2)


def impl_Condition_10(inst):
    assert inst.bodySite[0].coding[0].code == "49521004"
    assert inst.bodySite[0].coding[0].display == "Left external ear structure"
    assert inst.bodySite[0].coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite[0].text == "Left Ear"
    assert inst.category.coding[0].code == "diagnosis"
    assert inst.category.coding[0].display == "Diagnosis"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/condition-category"
    assert inst.category.coding[1].code == "439401001"
    assert inst.category.coding[1].display == "Diagnosis"
    assert inst.category.coding[1].system == "http://snomed.info/sct"
    assert inst.code.coding[0].code == "39065001"
    assert inst.code.coding[0].display == "Burn of ear"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Burnt Ear"
    assert (
        inst.extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/condition-criticality"
    )
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "399166001"
    assert inst.extension[0].valueCodeableConcept.coding[0].display == "Fatal"
    assert (
        inst.extension[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.id == "condition-example"
    assert inst.onsetDateTime == date(2012, 5, 24)
    assert inst.patient.reference == "Patient/example"
    assert inst.severity.coding[0].code == "24484000"
    assert inst.severity.coding[0].display == "Severe"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.text.div == "<div>Severe burn of left ear (Date: 24-May 2012)</div>"
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "confirmed"


def test_Condition_11(base_settings):
    filename = base_settings["unittest_data_dir"] / "condition-example2.canonical.json"
    inst = condition.Condition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Condition" == inst.resource_type
    impl_Condition_11(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Condition" == data["resourceType"]

    inst2 = condition.Condition(**data)
    impl_Condition_11(inst2)


def impl_Condition_11(inst):
    assert inst.category.coding[0].code == "finding"
    assert inst.category.coding[0].display == "Finding"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/condition-category"
    assert inst.clinicalStatus == "active"
    assert inst.code.text == "Asthma"
    assert inst.id == "example2"
    assert inst.onsetDateTime == date(2012, 11, 12)
    assert inst.patient.reference == "Patient/example"
    assert inst.severity.coding[0].code == "255604002"
    assert inst.severity.coding[0].display == "Mild"
    assert inst.severity.coding[0].system == "http://snomed.info/sct"
    assert inst.text.div == "<div>Mild Asthma (Date: 21-Nov 2012)</div>"
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "confirmed"
