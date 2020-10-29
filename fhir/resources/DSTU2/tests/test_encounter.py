# -*- coding: utf-8 -*-
from datetime import datetime, timezone
from decimal import Decimal

from .. import fhirtypes  # noqa: F401
from .. import encounter


def test_Encounter_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "encounter-example-f001-heart.canonical.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type
    impl_Encounter_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_Encounter_1(inst2)


def impl_Encounter_1(inst):
    assert inst.hospitalization.admitSource.coding[0].code == "305956004"
    assert inst.hospitalization.admitSource.coding[0].display == "Referral by physician"
    assert inst.hospitalization.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.hospitalization.dischargeDisposition.coding[0].code == "306689006"
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].display
        == "Discharge to home"
    )
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.hospitalization.preAdmissionIdentifier.system
        == "http://www.amc.nl/zorgportal/identifiers/pre-admissions"
    )
    assert inst.hospitalization.preAdmissionIdentifier.use == "official"
    assert inst.hospitalization.preAdmissionIdentifier.value == "93042"
    assert inst.id == "f001"
    assert (
        inst.identifier[0].system == "http://www.amc.nl/zorgportal/identifiers/visits"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v1451"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "min"
    assert inst.length.value == Decimal("140")
    assert inst.participant[0].individual.display == "P. Voigt"
    assert inst.participant[0].individual.reference == "Practitioner/f002"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.priority.coding[0].code == "310361003"
    assert inst.priority.coding[0].display == "Non-urgent cardiological admission"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].coding[0].code == "34068001"
    assert inst.reason[0].coding[0].display == "Heart valve replacement"
    assert inst.reason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.serviceProvider.display == "Burgers University Medical Center"
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "finished"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f001</p><p><b>identifier</b>: v1451 (OFFICIAL)</p><p><b>status</b>: finished</p><p><b>class</b>: outpatient</p><p><b>type</b>: Patient-initiated encounter <span>(Details : {SNOMED CT code '270427003' = '270427003', given as 'Patient-initiated encounter'})</span></p><p><b>priority</b>: Non-urgent cardiological admission <span>(Details : {SNOMED CT code '310361003' = '310361003', given as 'Non-urgent cardiological admission'})</span></p><p><b>patient</b>: <a>P. van de Heuvel</a></p><h3>Participants</h3><table><tr><td>-</td><td><b>Individual</b></td></tr><tr><td>*</td><td><a>P. Voigt</a></td></tr></table><p><b>length</b>: 140 min<span> (Details: http://unitsofmeasure.org code min = '??')</span></p><p><b>reason</b>: Heart valve replacement <span>(Details : {SNOMED CT code '34068001' = '34068001', given as 'Heart valve replacement'})</span></p><h3>Hospitalizations</h3><table><tr><td>-</td><td><b>PreAdmissionIdentifier</b></td><td><b>AdmitSource</b></td><td><b>DischargeDisposition</b></td></tr><tr><td>*</td><td>93042 (OFFICIAL)</td><td>Referral by physician <span>(Details : {SNOMED CT code '305956004' = '305956004', given as 'Referral by physician'})</span></td><td>Discharge to home <span>(Details : {SNOMED CT code '306689006' = '306689006', given as 'Discharge to home'})</span></td></tr></table><p><b>serviceProvider</b>: <a>Burgers University Medical Center</a></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_Encounter_2(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "encounter-example-f002-lung.canonical.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type
    impl_Encounter_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_Encounter_2(inst2)


def impl_Encounter_2(inst):
    assert inst.hospitalization.admitSource.coding[0].code == "305997006"
    assert (
        inst.hospitalization.admitSource.coding[0].display == "Referral by radiologist"
    )
    assert inst.hospitalization.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.hospitalization.dischargeDisposition.coding[0].code == "306689006"
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].display
        == "Discharge to home"
    )
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.hospitalization.preAdmissionIdentifier.system
        == "http://www.bmc.nl/zorgportal/identifiers/pre-admissions"
    )
    assert inst.hospitalization.preAdmissionIdentifier.use == "official"
    assert inst.hospitalization.preAdmissionIdentifier.value == "98682"
    assert inst.id == "f002"
    assert (
        inst.identifier[0].system
        == "http://www.bmc.nl/zorgportal/identifiers/encounters"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v3251"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "min"
    assert inst.length.value == Decimal("140")
    assert inst.participant[0].individual.display == "M.I.M Versteegh"
    assert inst.participant[0].individual.reference == "Practitioner/f003"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.priority.coding[0].code == "103391001"
    assert inst.priority.coding[0].display == "Urgent"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].coding[0].code == "34068001"
    assert inst.reason[0].coding[0].display == "Partial lobectomy of lung"
    assert inst.reason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.serviceProvider.display == "BMC"
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "finished"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f002</p><p><b>identifier</b>: v3251 (OFFICIAL)</p><p><b>status</b>: finished</p><p><b>class</b>: outpatient</p><p><b>type</b>: Patient-initiated encounter <span>(Details : {SNOMED CT code '270427003' = '270427003', given as 'Patient-initiated encounter'})</span></p><p><b>priority</b>: Urgent <span>(Details : {SNOMED CT code '103391001' = '103391001', given as 'Urgent'})</span></p><p><b>patient</b>: <a>P. van de Heuvel</a></p><h3>Participants</h3><table><tr><td>-</td><td><b>Individual</b></td></tr><tr><td>*</td><td><a>M.I.M Versteegh</a></td></tr></table><p><b>length</b>: 140 min<span> (Details: http://unitsofmeasure.org code min = '??')</span></p><p><b>reason</b>: Partial lobectomy of lung <span>(Details : {SNOMED CT code '34068001' = '34068001', given as 'Partial lobectomy of lung'})</span></p><h3>Hospitalizations</h3><table><tr><td>-</td><td><b>PreAdmissionIdentifier</b></td><td><b>AdmitSource</b></td><td><b>DischargeDisposition</b></td></tr><tr><td>*</td><td>98682 (OFFICIAL)</td><td>Referral by radiologist <span>(Details : {SNOMED CT code '305997006' = '305997006', given as 'Referral by radiologist'})</span></td><td>Discharge to home <span>(Details : {SNOMED CT code '306689006' = '306689006', given as 'Discharge to home'})</span></td></tr></table><p><b>serviceProvider</b>: <a>BMC</a></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_Encounter_3(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "encounter-example-f003-abscess.canonical.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type
    impl_Encounter_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_Encounter_3(inst2)


def impl_Encounter_3(inst):
    assert inst.hospitalization.admitSource.coding[0].code == "305956004"
    assert inst.hospitalization.admitSource.coding[0].display == "Referral by physician"
    assert inst.hospitalization.admitSource.coding[0].system == "http://snomed.info/sct"
    assert inst.hospitalization.dischargeDisposition.coding[0].code == "306689006"
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].display
        == "Discharge to home"
    )
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.hospitalization.preAdmissionIdentifier.system
        == "http://www.bmc.nl/zorgportal/identifiers/pre-admissions"
    )
    assert inst.hospitalization.preAdmissionIdentifier.use == "official"
    assert inst.hospitalization.preAdmissionIdentifier.value == "93042"
    assert inst.id == "f003"
    assert (
        inst.identifier[0].system
        == "http://www.bmc.nl/zorgportal/identifiers/encounters"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v6751"
    assert inst.length.code == "min"
    assert inst.length.system == "http://unitsofmeasure.org"
    assert inst.length.unit == "min"
    assert inst.length.value == Decimal("90")
    assert inst.participant[0].individual.display == "E.M. van den Broek"
    assert inst.participant[0].individual.reference == "Practitioner/f001"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.priority.coding[0].code == "103391001"
    assert (
        inst.priority.coding[0].display == "Non-urgent ear, nose and throat admission"
    )
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert inst.reason[0].coding[0].code == "18099001"
    assert inst.reason[0].coding[0].display == "Retropharyngeal abscess"
    assert inst.reason[0].coding[0].system == "http://snomed.info/sct"
    assert (
        inst.reason[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/encounter-primaryDiagnosis"
    )
    assert inst.reason[0].extension[0].valueInteger == 1
    assert inst.serviceProvider.reference == "Organization/f001"
    assert inst.status == "finished"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f003</p><p><b>identifier</b>: v6751 (OFFICIAL)</p><p><b>status</b>: finished</p><p><b>class</b>: outpatient</p><p><b>type</b>: Patient-initiated encounter <span>(Details : {SNOMED CT code '270427003' = '270427003', given as 'Patient-initiated encounter'})</span></p><p><b>priority</b>: Non-urgent ear, nose and throat admission <span>(Details : {SNOMED CT code '103391001' = '103391001', given as 'Non-urgent ear, nose and throat admission'})</span></p><p><b>patient</b>: <a>P. van de Heuvel</a></p><h3>Participants</h3><table><tr><td>-</td><td><b>Individual</b></td></tr><tr><td>*</td><td><a>E.M. van den Broek</a></td></tr></table><p><b>length</b>: 90 min<span> (Details: http://unitsofmeasure.org code min = '??')</span></p><p><b>reason</b>: Retropharyngeal abscess <span>(Details : {SNOMED CT code '18099001' = '18099001', given as 'Retropharyngeal abscess'})</span></p><h3>Hospitalizations</h3><table><tr><td>-</td><td><b>PreAdmissionIdentifier</b></td><td><b>AdmitSource</b></td><td><b>DischargeDisposition</b></td></tr><tr><td>*</td><td>93042 (OFFICIAL)</td><td>Referral by physician <span>(Details : {SNOMED CT code '305956004' = '305956004', given as 'Referral by physician'})</span></td><td>Discharge to home <span>(Details : {SNOMED CT code '306689006' = '306689006', given as 'Discharge to home'})</span></td></tr></table><p><b>serviceProvider</b>: <a>Organization/f001</a></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "270427003"
    assert inst.type[0].coding[0].display == "Patient-initiated encounter"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_Encounter_4(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "encounter-example-f201-20130404.canonical.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type
    impl_Encounter_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_Encounter_4(inst2)


def impl_Encounter_4(inst):
    assert inst.id == "f201"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130404"
    assert inst.participant[0].individual.reference == "Practitioner/f201"
    assert inst.patient.display == "Roel"
    assert inst.patient.reference == "Patient/f201"
    assert inst.priority.coding[0].code == "17621005"
    assert inst.priority.coding[0].display == "Normal"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.reason[0].text
        == "The patient had fever peaks over the last couple of days. He is worried about these peaks."
    )
    assert inst.serviceProvider.reference == "Organization/f201"
    assert inst.status == "finished"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f201</p><p><b>identifier</b>: Encounter_Roel_20130404 (TEMP)</p><p><b>status</b>: finished</p><p><b>class</b>: outpatient</p><p><b>type</b>: Consultation <span>(Details : {SNOMED CT code '11429006' = '11429006', given as 'Consultation'})</span></p><p><b>priority</b>: Normal <span>(Details : {SNOMED CT code '17621005' = '17621005', given as 'Normal'})</span></p><p><b>patient</b>: <a>Roel</a></p><h3>Participants</h3><table><tr><td>-</td><td><b>Individual</b></td></tr><tr><td>*</td><td><a>Practitioner/f201</a></td></tr></table><p><b>reason</b>: The patient had fever peaks over the last couple of days. He is worried about these peaks. <span>(Details )</span></p><p><b>serviceProvider</b>: <a>Organization/f201</a></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "11429006"
    assert inst.type[0].coding[0].display == "Consultation"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_Encounter_5(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "encounter-example-f202-20130128.canonical.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type
    impl_Encounter_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_Encounter_5(inst2)


def impl_Encounter_5(inst):
    assert inst.id == "f202"
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "Encounter_Roel_20130128"
    assert inst.indication[0].display == "Roel's TPF chemotherapy on January 28th, 2013"
    assert (
        inst.indication[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/encounter-primaryDiagnosis"
    )
    assert inst.indication[0].extension[0].valueInteger == 1
    assert inst.indication[0].reference == "Procedure/f201"
    assert inst.length.code == "258701004"
    assert inst.length.system == "http://snomed.info/sct"
    assert inst.length.unit == "minutes"
    assert inst.length.value == Decimal("56")
    assert inst.participant[0].individual.reference == "Practitioner/f201"
    assert inst.patient.display == "Roel"
    assert inst.patient.reference == "Patient/f201"
    assert inst.priority.coding[0].code == "103391001"
    assert inst.priority.coding[0].display == "Urgent"
    assert inst.priority.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.reason[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/encounter-primaryDiagnosis"
    )
    assert inst.reason[0].extension[0].valueInteger == 2
    assert inst.reason[0].text == "The patient is treated for a tumor."
    assert inst.serviceProvider.reference == "Organization/f201"
    assert inst.status == "finished"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f202</p><p><b>identifier</b>: Encounter_Roel_20130128 (TEMP)</p><p><b>status</b>: finished</p><p><b>class</b>: outpatient</p><p><b>type</b>: Chemotherapy <span>(Details : {SNOMED CT code '367336001' = '367336001', given as 'Chemotherapy'})</span></p><p><b>priority</b>: Urgent <span>(Details : {SNOMED CT code '103391001' = '103391001', given as 'Urgent'})</span></p><p><b>patient</b>: <a>Roel</a></p><h3>Participants</h3><table><tr><td>-</td><td><b>Individual</b></td></tr><tr><td>*</td><td><a>Practitioner/f201</a></td></tr></table><p><b>length</b>: 56 minutes<span> (Details: SNOMED CT code 258701004 = '258701004')</span></p><p><b>reason</b>: The patient is treated for a tumor. <span>(Details )</span></p><p><b>indication</b>: <a>Roel's TPF chemotherapy on January 28th, 2013</a></p><p><b>serviceProvider</b>: <a>Organization/f201</a></p></div>"
    )
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "367336001"
    assert inst.type[0].coding[0].display == "Chemotherapy"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"


def test_Encounter_8(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "encounter-example-xcda.canonical.json"
    )
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type
    impl_Encounter_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_Encounter_8(inst2)


def impl_Encounter_8(inst):
    assert inst.id == "xcda"
    assert (
        inst.identifier[0].system
        == "http://healthcare.example.org/identifiers/enocunter"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "1234213.52345873"
    assert inst.participant[0].individual.reference == "Practitioner/xcda1"
    assert inst.patient.reference == "Patient/xcda"
    assert inst.reason[0].coding[0].code == "T-D8200"
    assert inst.reason[0].coding[0].display == "Arm"
    assert (
        inst.reason[0].coding[0].system == "http://ihe.net/xds/connectathon/eventCodes"
    )
    assert inst.status == "finished"
    assert (
        inst.text.div
        == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: xcda</p><p><b>identifier</b>: 1234213.52345873 (OFFICIAL)</p><p><b>status</b>: finished</p><p><b>class</b>: outpatient</p><p><b>patient</b>: <a>Patient/xcda</a></p><h3>Participants</h3><table><tr><td>-</td><td><b>Individual</b></td></tr><tr><td>*</td><td><a>Practitioner/xcda1</a></td></tr></table><p><b>reason</b>: Arm <span>(Details : {http://ihe.net/xds/connectathon/eventCodes code 'T-D8200' = '??', given as 'Arm'})</span></p></div>"
    )
    assert inst.text.status == "generated"


def test_Encounter_9(base_settings):
    filename = base_settings["unittest_data_dir"] / "encounter-example.canonical.json"
    inst = encounter.Encounter.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Encounter" == inst.resource_type
    impl_Encounter_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Encounter" == data["resourceType"]

    inst2 = encounter.Encounter(**data)
    impl_Encounter_9(inst2)


def impl_Encounter_9(inst):
    assert inst.extension[0].extension[0].url == "condition"
    assert inst.extension[0].extension[0].valueReference.reference == "Condition/qicore"
    assert inst.extension[0].extension[1].url == "role"
    assert (
        inst.extension[0].extension[1].valueCodeableConcept.coding[0].code == "8319008"
    )
    assert (
        inst.extension[0].extension[1].valueCodeableConcept.coding[0].display
        == "Principal diagnosis"
    )
    assert (
        inst.extension[0].extension[1].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert (
        inst.extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/encounter-relatedCondition"
    )
    assert inst.hospitalization.dischargeDisposition.coding[0].code == "home"
    assert inst.hospitalization.dischargeDisposition.coding[0].display == "Home"
    assert (
        inst.hospitalization.dischargeDisposition.coding[0].system
        == "http://hl7.org/fhir/discharge-disposition"
    )
    assert inst.id == "encounter-example"
    assert inst.patient.reference == "patient-example"
    assert inst.period.end == datetime(2015, 2, 20, 00, 00, 00, tzinfo=timezone.utc)
    assert inst.period.start == datetime(2015, 2, 9, 00, 00, 00, tzinfo=timezone.utc)
    assert inst.status == "finished"
    assert inst.text.div == "<div>Encounter with patient @qicore</div>"
    assert inst.text.status == "generated"
