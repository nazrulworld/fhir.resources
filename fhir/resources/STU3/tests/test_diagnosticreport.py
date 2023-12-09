# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import diagnosticreport


def impl_diagnosticreport_1(inst):
    assert inst.basedOn[0].reference == "#req"
    assert inst.category.coding[0].code == "15220000"
    assert inst.category.coding[0].display == "Laboratory test"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "LAB"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "104177005"
    assert (
        inst.code.coding[0].display
        == "Blood culture for bacteria, including anaerobic screen"
    )
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.codedDiagnosis[0].coding[0].code == "428763004"
    assert (
        inst.codedDiagnosis[0].coding[0].display == "Bacteremia due to staphylococcus"
    )
    assert inst.codedDiagnosis[0].coding[0].system == "http://snomed.info/sct"
    assert inst.conclusion == "Blood culture tested positive on staphylococcus aureus"
    assert inst.contained[0].id == "req"
    assert inst.id == "f202"
    assert inst.issued == fhirtypes.Instant.validate("2013-03-11T10:28:00+01:00")
    assert inst.performer[0].actor.display == "AUMC"
    assert inst.performer[0].actor.reference == "Organization/f201"
    assert (
        inst.result[0].display
        == "Results for staphylococcus analysis on Roel's blood culture"
    )
    assert inst.result[0].reference == "Observation/f206"
    assert inst.status == "final"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_diagnosticreport_1(base_settings):
    """No. 1 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-f202-bloodculture.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "diagnosticreport-example-f202-bloodculture.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_1(inst2)


def impl_diagnosticreport_2(inst):
    assert inst.code.coding[0].code == "GHP"
    assert inst.code.coding[0].display == "General Health Profile"
    assert inst.code.coding[0].system == "http://acme.com/labs/reports"
    assert inst.contained[0].id == "rtt"
    assert inst.contained[1].id == "ltt"
    assert inst.contained[2].id == "urine"
    assert inst.contained[3].id == "p2"
    assert inst.contained[4].id == "r1"
    assert inst.contained[5].id == "r2"
    assert inst.contained[6].id == "r3"
    assert inst.contained[7].id == "r4"
    assert inst.contained[8].id == "r5"
    assert inst.contained[9].id == "r6"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2015-08-16T06:40:17Z")
    assert inst.id == "ghp"
    assert inst.identifier[0].system == "http://acme.com/lab/reports"
    assert inst.identifier[0].value == "ghp-example"
    assert inst.issued == fhirtypes.Instant.validate("2015-08-17T06:40:17Z")
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2015-08-16T10:35:23Z")
    assert inst.performer[0].actor.display == "Acme Laboratory, Inc"
    assert (
        inst.performer[0].actor.reference
        == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    )
    assert inst.result[0].display == "Chemistry Panel"
    assert inst.result[0].reference == "#p1"
    assert inst.result[1].display == "CBC"
    assert inst.result[1].reference == "#p2"
    assert inst.result[2].display == "Urinalysis"
    assert inst.result[2].reference == "#p3"
    assert inst.specimen[0].display == "Red Top Tube"
    assert inst.specimen[0].reference == "#rtt"
    assert inst.specimen[1].display == "Lavender Top Tube"
    assert inst.specimen[1].reference == "#ltt"
    assert inst.specimen[2].display == "Urine Sample"
    assert inst.specimen[2].reference == "#urine"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"


def test_diagnosticreport_2(base_settings):
    """No. 2 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-ghp.json
    """
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example-ghp.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_2(inst2)


def impl_diagnosticreport_3(inst):
    assert inst.category.coding[0].code == "HM"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "24331-1"
    assert inst.code.coding[0].display == "Lipid 1996 panel - Serum or Plasma"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Lipid Panel"
    assert inst.contained[0].id == "cholesterol"
    assert inst.contained[1].id == "triglyceride"
    assert inst.contained[2].id == "hdlcholesterol"
    assert inst.contained[3].id == "ldlcholesterol"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2011-03-04T08:30:00+11:00"
    )
    assert inst.id == "lipids"
    assert inst.identifier[0].system == "http://acme.com/lab/reports"
    assert inst.identifier[0].value == "5234342"
    assert inst.issued == fhirtypes.Instant.validate("2013-01-27T11:45:33+11:00")
    assert inst.performer[0].actor.display == "Acme Laboratory, Inc"
    assert (
        inst.performer[0].actor.reference
        == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    )
    assert inst.result[0].reference == "#cholesterol"
    assert inst.result[1].reference == "#triglyceride"
    assert inst.result[2].reference == "#hdlcholesterol"
    assert inst.result[3].reference == "#ldlcholesterol"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"


def test_diagnosticreport_3(base_settings):
    """No. 3 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-lipids.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-lipids.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_3(inst2)


def impl_diagnosticreport_4(inst):
    assert inst.basedOn[0].reference == "#req"
    assert inst.category.coding[0].code == "252275004"
    assert inst.category.coding[0].display == "Haematology test"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "HM"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "58410-2"
    assert inst.code.coding[0].display == (
        "Complete blood count (hemogram) panel - Blood by Automated " "count"
    )
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.conclusion == "Core lab"
    assert inst.contained[0].id == "req"
    assert inst.id == "f001"
    assert (
        inst.identifier[0].system == "http://www.bmc.nl/zorgportal/identifiers/reports"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "nr1239044"
    assert inst.issued == fhirtypes.Instant.validate("2013-05-15T19:32:52+01:00")
    assert inst.performer[0].actor.display == "Burgers University Medical Centre"
    assert inst.performer[0].actor.reference == "Organization/f001"
    assert inst.result[0].reference == "Observation/f001"
    assert inst.result[1].reference == "Observation/f002"
    assert inst.result[2].reference == "Observation/f003"
    assert inst.result[3].reference == "Observation/f004"
    assert inst.result[4].reference == "Observation/f005"
    assert inst.status == "final"
    assert inst.subject.display == "P. van den Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_diagnosticreport_4(base_settings):
    """No. 4 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-f001-bloodexam.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "diagnosticreport-example-f001-bloodexam.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_4(inst2)


def impl_diagnosticreport_5(inst):
    assert inst.category.coding[0].code == "394914008"
    assert inst.category.coding[0].display == "Radiology"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "RAD"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "45036003"
    assert inst.code.coding[0].display == "Ultrasonography of abdomen"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Abdominal Ultrasound"
    assert inst.conclusion == "Unremarkable study"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2012-12-01T12:00:00+01:00"
    )
    assert inst.id == "ultrasound"
    assert inst.image[0].comment == "A comment about the image"
    assert inst.image[0].link.display == "WADO example image"
    assert (
        inst.image[0].link.reference
        == "Media/1.2.840.11361907579238403408700.3.0.14.19970327150033"
    )
    assert inst.issued == fhirtypes.Instant.validate("2012-12-01T12:00:00+01:00")
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_diagnosticreport_5(base_settings):
    """No. 5 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-ultrasound.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-ultrasound.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_5(inst2)


def impl_diagnosticreport_6(inst):
    assert inst.category.coding[0].code == "394914008"
    assert inst.category.coding[0].display == "Radiology"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "RAD"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "429858000"
    assert inst.code.coding[0].display == "Computed tomography (CT) of head and neck"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "CT of head-neck"
    assert inst.codedDiagnosis[0].coding[0].code == "188340000"
    assert (
        inst.codedDiagnosis[0].coding[0].display
        == "Malignant tumor of craniopharyngeal duct"
    )
    assert inst.codedDiagnosis[0].coding[0].system == "http://snomed.info/sct"
    assert inst.conclusion == "CT brains: large tumor sphenoid/clivus."
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2012-12-01T12:00:00+01:00"
    )
    assert inst.id == "f201"
    assert inst.imagingStudy[0].display == "HEAD and NECK CT DICOM imaging study"
    assert inst.issued == fhirtypes.Instant.validate("2012-12-01T12:00:00+01:00")
    assert inst.performer[0].actor.display == "Blijdorp MC"
    assert inst.performer[0].actor.reference == "Organization/f203"
    assert inst.status == "final"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_diagnosticreport_6(base_settings):
    """No. 6 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-f201-brainct.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "diagnosticreport-example-f201-brainct.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_6(inst2)


def impl_diagnosticreport_7(inst):
    assert inst.category.coding[0].code == "15220000"
    assert inst.category.coding[0].display == "Laboratory test"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "LAB"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "55233-1"
    assert inst.code.coding[0].display == "Genetic analysis master panel"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.contained[0].id == "f1-genetics"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2015-05-26T15:30:10+01:00"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/DiagnosticReport-"
        "geneticsFamilyMemberHistory"
    )
    assert inst.extension[0].valueReference.reference == "#f1-genetics"
    assert inst.id == "dg2"
    assert inst.issued == fhirtypes.Instant.validate("2014-05-16T10:28:00+01:00")
    assert inst.performer[0].actor.display == "Molecular Diagnostic Laboratory"
    assert inst.performer[0].actor.reference == "Practitioner/genetics-example2"
    assert inst.result[0].display == "Genetic analysis for BRAC -1"
    assert inst.result[0].reference == "Observation/ob-genetics-3-1"
    assert inst.result[1].display == "Genetic analysis for BRAC -2"
    assert inst.result[1].reference == "Observation/ob-genetics-3-2"
    assert inst.specimen[0].display == "Molecular Specimen ID: MLD45-Z4-1234"
    assert inst.specimen[0].reference == "Specimen/genetics-example2"
    assert inst.status == "final"
    assert inst.subject.display == "Peter James Chalmers(MRN: 12345)"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_diagnosticreport_7(base_settings):
    """No. 7 tests collection for DiagnosticReport.
    Test File: diagnosticreport-genetics-example-2-familyhistory.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "diagnosticreport-genetics-example-2-familyhistory.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_7(inst2)


def impl_diagnosticreport_8(inst):
    assert inst.basedOn[0].reference == "#req"
    assert inst.category.coding[0].code == "MB"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "632-0"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Culture, MRSA"
    assert inst.contained[0].id == "obx1-4"
    assert inst.contained[1].id == "obx1-5"
    assert inst.contained[2].id == "obx2-1"
    assert inst.contained[3].id == "obx2-2"
    assert inst.contained[4].id == "obx2-4"
    assert inst.contained[5].id == "obx2-6"
    assert inst.contained[6].id == "obx2-8"
    assert inst.contained[7].id == "obx2-10"
    assert inst.contained[8].id == "obx2-12"
    assert inst.contained[9].id == "obx2-14"
    assert inst.id == "micro"
    assert inst.identifier[0].system == "http://hnam.org/identifiers/orders"
    assert inst.identifier[0].value == "290741144"
    assert inst.issued == fhirtypes.Instant.validate("2009-08-10T08:25:44+10:00")
    assert inst.performer[0].actor.display == "Todd Ashby"
    assert inst.result[0].reference == "#org1"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_diagnosticreport_8(base_settings):
    """No. 8 tests collection for DiagnosticReport.
    Test File: diagnosticreport-micro1.json
    """
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-micro1.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_8(inst2)


def impl_diagnosticreport_9(inst):
    assert inst.category.coding[0].code == "HM"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "58410-2"
    assert inst.code.coding[0].display == (
        "Complete blood count (hemogram) panel - Blood by Automated " "count"
    )
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.coding[1].code == "CBC"
    assert inst.code.coding[1].display == "MASTER FULL BLOOD COUNT"
    assert inst.code.text == "Complete Blood Count"
    assert inst.contained[0].id == "r1"
    assert inst.contained[1].id == "r2"
    assert inst.contained[2].id == "r3"
    assert inst.contained[3].id == "r4"
    assert inst.contained[4].id == "r5"
    assert inst.contained[5].id == "r6"
    assert inst.contained[6].id == "r7"
    assert inst.contained[7].id == "r8"
    assert inst.contained[8].id == "r9"
    assert inst.contained[9].id == "r10"
    assert inst.context.reference == "Encounter/example"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2011-03-04T08:30:00+11:00"
    )
    assert inst.id == "101"
    assert inst.identifier[0].system == "http://acme.com/lab/reports"
    assert inst.identifier[0].value == "5234342"
    assert inst.issued == fhirtypes.Instant.validate("2011-03-04T11:45:33+11:00")
    assert inst.meta.tag[0].code == "01"
    assert inst.meta.tag[0].display == "Needs Review"
    assert (
        inst.meta.tag[0].system == "http://example.org/fhir/CodeSystem/workflow-codes"
    )
    assert inst.performer[0].actor.display == "Acme Laboratory, Inc"
    assert (
        inst.performer[0].actor.reference
        == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    )
    assert inst.presentedForm[0].contentType == "application/pdf"
    assert inst.presentedForm[0].language == "en-AU"
    assert inst.presentedForm[0].title == "HTML Report"
    assert inst.result[0].reference == "#r1"
    assert inst.result[1].reference == "#r2"
    assert inst.result[2].reference == "#r3"
    assert inst.result[3].reference == "#r4"
    assert inst.result[4].reference == "#r5"
    assert inst.result[5].reference == "#r6"
    assert inst.result[6].reference == "#r7"
    assert inst.result[7].reference == "#r8"
    assert inst.result[8].reference == "#r9"
    assert inst.result[9].reference == "#r10"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"


def test_diagnosticreport_9(base_settings):
    """No. 9 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example.json
    """
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_9(inst2)


def impl_diagnosticreport_10(inst):
    assert inst.code.coding[0].code == "47527-7"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2013-02-11T10:33:33+11:00"
    )
    assert inst.id == "pap"
    assert inst.issued == fhirtypes.Instant.validate("2013-02-13T11:45:33+11:00")
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/b248b1b2-1686-4b94-9936-37d7a5f94b51"
    assert inst.text.status == "additional"


def test_diagnosticreport_10(base_settings):
    """No. 10 tests collection for DiagnosticReport.
    Test File: diagnosticreport-example-papsmear.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "diagnosticreport-example-papsmear.json"
    )
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type

    impl_diagnosticreport_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_diagnosticreport_10(inst2)
