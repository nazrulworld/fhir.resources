# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentReference
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import documentreference


def impl_documentreference_1(inst):
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2021-01-01T01:02:01+01:00"
    )
    assert inst.content[0].attachment.title == "Sample Genomic File"
    assert (
        inst.content[0].attachment.url
        == "http://www.somesystemabc.net/identifiers/files/11114"
    )
    assert inst.description == (
        "A sample Document Reference instance representing a generic "
        "genomic file that may ber used as input or output of a "
        "genomic analysis pipeline."
    )
    assert inst.docStatus == "preliminary"
    assert inst.id == "genomicFile4"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/files"
    assert inst.identifier[0].value == "11114"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.securityLabel[0].coding[0].code == "R"
    assert inst.securityLabel[0].coding[0].display == "Restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.status == "current"
    assert inst.subject.display == "Child Junior Doe"
    assert inst.subject.reference == "Patient/denovoChild"
    assert inst.text.status == "generated"


def test_documentreference_1(base_settings):
    """No. 1 tests collection for DocumentReference.
    Test File: DocumentReference-genomicFile4.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "DocumentReference-genomicFile4.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_1(inst2)


def impl_documentreference_2(inst):
    assert inst.author[0].display == "G.E. Medical Systems"
    assert inst.bodySite[0].concept.coding[0].code == "67734004"
    assert inst.bodySite[0].concept.coding[0].display == "Upper Trunk Structure"
    assert inst.bodySite[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.content[0].attachment.contentType == "application/dicom"
    assert inst.content[0].attachment.height == 480
    assert inst.content[0].attachment.width == 640
    assert inst.event[0].concept.coding[0].code == "399067008"
    assert inst.event[0].concept.coding[0].display == "Lateral projection"
    assert inst.event[0].concept.coding[0].system == "http://snomed.info/sct"
    assert inst.extension[0].url == "http://nema.org/fhir/extensions#0002-0010"
    assert inst.extension[0].valueUri == "urn:oid:1.2.840.10008.1.2.1"
    assert inst.id == "1.2.840.11361907579238403408700.3.1.04.19970327150033"
    assert inst.identifier[0].system == "http://acme-imaging.com/accession/2012"
    assert inst.identifier[0].type.text == "accessionNo"
    assert inst.identifier[0].value == "1234567"
    assert inst.identifier[1].system == "urn:dicom:uid"
    assert inst.identifier[1].type.text == "studyId"
    assert (
        inst.identifier[1].value
        == "urn:oid:1.2.840.113619.2.21.848.34082.0.538976288.3"
    )
    assert inst.identifier[2].system == "urn:dicom:uid"
    assert inst.identifier[2].type.text == "seriesId"
    assert (
        inst.identifier[2].value
        == "urn:oid:1.2.840.113619.2.21.3408.700.0.757923840.3.0"
    )
    assert inst.identifier[3].system == "urn:dicom:uid"
    assert inst.identifier[3].type.text == "InstanceUID"
    assert inst.identifier[3].use == "official"
    assert inst.identifier[3].value == (
        "urn:oid:1.2.840.11361907579238403408700.3.1.04.1997032715003" "3"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.modality[0].coding[0].code == "US"
    assert (
        inst.modality[0].coding[0].system
        == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_documentreference_2(base_settings):
    """No. 2 tests collection for DocumentReference.
    Test File: documentreference-example-dicom.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "documentreference-example-dicom.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_2(inst2)


def impl_documentreference_3(inst):
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2019-03-01T01:02:01+01:00"
    )
    assert inst.content[0].attachment.title == "CNVAnalysis_called"
    assert inst.content[0].attachment.url == (
        "https://chat.fhir.org/user_uploads/10155/Hnv3LtumKn-1QjeyS2K"
        "Vuw4R/CNVAnalysis_called.bed"
    )
    assert inst.description == (
        "CNVAnalysis_called: A sample Document Reference instance "
        "representing a BED file that may be used as input or output "
        "of a genomic analysis pipeline."
    )
    assert inst.docStatus == "preliminary"
    assert inst.id == "CNVAnalysis-called"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/files"
    assert inst.identifier[0].value == "11120"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.securityLabel[0].coding[0].code == "R"
    assert inst.securityLabel[0].coding[0].display == "Restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.status == "current"
    assert inst.text.status == "generated"


def test_documentreference_3(base_settings):
    """No. 3 tests collection for DocumentReference.
    Test File: DocumentReference-CNVAnalysis_called.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "DocumentReference-CNVAnalysis_called.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_3(inst2)


def impl_documentreference_4(inst):
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2021-01-01T01:01:01+01:00"
    )
    assert inst.content[0].attachment.title == "Sample Genomic File"
    assert (
        inst.content[0].attachment.url
        == "http://www.somesystemabc.net/identifiers/files/11113"
    )
    assert inst.description == (
        "A sample Document Reference instance representing a generic "
        "genomic file that may ber used as input or output of a "
        "genomic analysis pipeline."
    )
    assert inst.docStatus == "preliminary"
    assert inst.id == "genomicFileFather"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/files"
    assert inst.identifier[0].value == "111110"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.securityLabel[0].coding[0].code == "R"
    assert inst.securityLabel[0].coding[0].display == "Restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.status == "current"
    assert inst.subject.display == "John Doe"
    assert inst.subject.reference == "Patient/father"
    assert inst.text.status == "generated"


def test_documentreference_4(base_settings):
    """No. 4 tests collection for DocumentReference.
    Test File: DocumentReference-genomicFileFather.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "DocumentReference-genomicFileFather.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_4(inst2)


def impl_documentreference_5(inst):
    assert inst.attester[0].mode.coding[0].code == "professional"
    assert (
        inst.attester[0].mode.coding[0].system
        == "http://hl7.org/fhir/composition-attestation-mode"
    )
    assert inst.attester[0].party.reference == "#in-author"
    assert inst.author[0].reference == "#in-author"
    assert inst.category[0].coding[0].code == "11369-6"
    assert inst.category[0].coding[0].system == "http://loinc.org"
    assert inst.contained[0].id == "in-author"
    assert inst.contained[1].id == "in-patient"
    assert inst.content[0].attachment.contentType == "text/plain"
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2020-12-31T23:50:50-05:00"
    )
    assert inst.content[0].attachment.hash == bytes_validator(
        "OGEzOGYyNjMzMDA2ZmQ1MzUxNDljNDRhM2E3M2YzMTI0MzdiMzQ3OA=="
    )
    assert inst.content[0].attachment.language == "en"
    # Don't know how to create unit test
    # for "content[0].attachment.size",
    # which is a Integer64
    assert (
        inst.content[0].attachment.title
        == "DocumentReference for Comprehensive fully filled metadata"
    )
    assert inst.content[0].attachment.url == "http://example.com/nowhere.txt"
    assert inst.content[0].profile[0].valueCoding.code == "urn:ihe:iti:xds-sd:text:2008"
    assert inst.content[0].profile[0].valueCoding.system == (
        "http://ihe.net/fhir/ihe.formatcode.fhir/CodeSystem/formatcod" "e"
    )
    assert inst.date == fhirtypes.Instant.validate("2020-12-31T23:50:50-05:00")
    assert inst.description == (
        "Example of a Comprehensive DocumentReference resource. This "
        "is fully filled for all mandatory elements and all optional "
        "elements."
    )
    assert inst.event[0].concept.coding[0].code == "ACCTRECEIVABLE"
    assert (
        inst.event[0].concept.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.event[1].reference.identifier.system == "urn:ietf:rfc:3986"
    assert inst.event[1].reference.identifier.value == (
        "urn:oid:1.2.840.113556.1.8000.2554.17917.46600.21181.17878.3"
        "3419.62048.57128.2759"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/documentreference-" "sourcepatient"
    )
    assert inst.extension[0].valueReference.reference == "#in-patient"
    assert inst.facilityType.coding[0].code == "82242000"
    assert inst.facilityType.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "example-comprehensive"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == (
        "urn:oid:1.2.840.113556.1.8000.2554.58783.21864.3474.19410.44"
        "358.58254.41281.46340"
    )
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].value == "urn:uuid:0c287d32-01e3-4d87-9953-9fcc9404eb21"
    assert inst.meta.security[0].code == "HTEST"
    assert (
        inst.meta.security[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2020-12-31T23:50:50-05:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2020-12-31T23:50:50-05:00")
    assert inst.practiceSetting.coding[0].code == "408467006"
    assert inst.practiceSetting.coding[0].system == "http://snomed.info/sct"
    assert inst.relatesTo[0].code.coding[0].code == "appends"
    assert (
        inst.relatesTo[0].code.coding[0].system
        == "http://hl7.org/fhir/document-relationship-type"
    )
    assert inst.relatesTo[0].target.reference == "DocumentReference/example"
    assert inst.securityLabel[0].coding[0].code == "N"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.status == "extensions"
    assert inst.type.coding[0].code == "55107-7"
    assert inst.type.coding[0].system == "http://loinc.org"
    assert inst.version == "urn:uuid:0c287d32-01e3-4d87-9953-9fcc9404eb21"


def test_documentreference_5(base_settings):
    """No. 5 tests collection for DocumentReference.
    Test File: documentreference-example-comprehensive.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "documentreference-example-comprehensive.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_5(inst2)


def impl_documentreference_6(inst):
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2019-03-01T01:02:01+01:00"
    )
    assert inst.content[0].attachment.title == "Sample Genomic VCF File"
    assert (
        inst.content[0].attachment.url
        == "http://www.somesystemabc.net/identifiers/files/11114"
    )
    assert inst.description == (
        "A sample Document Reference instance representing a VCF file"
        " that may be used as input or output of a genomic analysis "
        "pipeline."
    )
    assert inst.docStatus == "preliminary"
    assert inst.id == "genomicVCFfile"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/files"
    assert inst.identifier[0].value == "11116"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.securityLabel[0].coding[0].code == "R"
    assert inst.securityLabel[0].coding[0].display == "Restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.status == "current"
    assert inst.text.status == "generated"


def test_documentreference_6(base_settings):
    """No. 6 tests collection for DocumentReference.
    Test File: DocumentReference-genomicVCFfile.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "DocumentReference-genomicVCFfile.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_6(inst2)


def impl_documentreference_7(inst):
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2019-03-01T01:02:01+01:00"
    )
    assert inst.content[0].attachment.title == "WES_FullSequencedRegion_GRCh38"
    assert inst.content[0].attachment.url == (
        "https://chat.fhir.org/user_uploads/10155/BILYJerATC59WlG15J3"
        "16BEf/WES_FullSequencedRegion_GRCh38.bed"
    )
    assert inst.description == (
        "WES_FullSequencedRegion_GRCh38: A sample Document Reference "
        "instance representing a BED file that may be used as input "
        "or output of a genomic analysis pipeline."
    )
    assert inst.docStatus == "preliminary"
    assert inst.id == "WES-FullSequencedRegion-GRCh38"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/files"
    assert inst.identifier[0].value == "11117"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.securityLabel[0].coding[0].code == "R"
    assert inst.securityLabel[0].coding[0].display == "Restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.status == "current"
    assert inst.text.status == "generated"


def test_documentreference_7(base_settings):
    """No. 7 tests collection for DocumentReference.
    Test File: DocumentReference-WES_FullSequencedRegion_GRCh38.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "DocumentReference-WES_FullSequencedRegion_GRCh38.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_7(inst2)


def impl_documentreference_8(inst):
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2019-03-01T01:02:01+01:00"
    )
    assert inst.content[0].attachment.title == "SimpleVariantAnalysis_called"
    assert inst.content[0].attachment.url == (
        "https://chat.fhir.org/user_uploads/10155/jQZWWKs4JO8ZfhfrbsC"
        "bbMUA/SimpleVariantAnalysis_called.bed"
    )
    assert inst.description == (
        "SimpleVariantAnalysis_called: A sample Document Reference "
        "instance representing a BED file that may be used as input "
        "or output of a genomic analysis pipeline."
    )
    assert inst.docStatus == "preliminary"
    assert inst.id == "SimpleVariantAnalysis-called"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/files"
    assert inst.identifier[0].value == "11118"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.securityLabel[0].coding[0].code == "R"
    assert inst.securityLabel[0].coding[0].display == "Restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.status == "current"
    assert inst.text.status == "generated"


def test_documentreference_8(base_settings):
    """No. 8 tests collection for DocumentReference.
    Test File: DocumentReference-SimpleVariantAnalysis_called.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "DocumentReference-SimpleVariantAnalysis_called.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_8(inst2)


def impl_documentreference_9(inst):
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2019-03-01T01:02:01+01:00"
    )
    assert inst.content[0].attachment.title == "genomicVCFfile_simple"
    assert inst.content[0].attachment.url == (
        "https://chat.fhir.org/user_uploads/10155/gdL90-np7lJjGwUxeAR"
        "apUHB/genomicVCFFile_simple.vcf"
    )
    assert inst.description == (
        "genomicVCFfile_simple: A sample Document Reference instance "
        "representing a VCF file that may be used as input or output "
        "of a genomic analysis pipeline."
    )
    assert inst.docStatus == "preliminary"
    assert inst.id == "genomicVCFfile-simple"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/files"
    assert inst.identifier[0].value == "11119"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.securityLabel[0].coding[0].code == "R"
    assert inst.securityLabel[0].coding[0].display == "Restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.status == "current"
    assert inst.text.status == "generated"


def test_documentreference_9(base_settings):
    """No. 9 tests collection for DocumentReference.
    Test File: DocumentReference-genomicVCFfile_simple.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "DocumentReference-genomicVCFfile_simple.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_9(inst2)


def impl_documentreference_10(inst):
    assert inst.content[0].attachment.creation == fhirtypes.DateTime.validate(
        "2021-01-01T01:01:01+01:00"
    )
    assert inst.content[0].attachment.title == "Sample Genomic File"
    assert (
        inst.content[0].attachment.url
        == "http://www.somesystemabc.net/identifiers/files/11112"
    )
    assert inst.description == (
        "A sample Document Reference instance representing a generic "
        "genomic file that may ber used as input or output of a "
        "genomic analysis pipeline."
    )
    assert inst.docStatus == "preliminary"
    assert inst.id == "genomicFile2"
    assert inst.identifier[0].system == "http://www.somesystemabc.net/identifiers/files"
    assert inst.identifier[0].value == "11112"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.securityLabel[0].coding[0].code == "R"
    assert inst.securityLabel[0].coding[0].display == "Restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"
    )
    assert inst.status == "current"
    assert inst.subject.display == "Jane Doe"
    assert inst.subject.reference == "Patient/denovoMother"
    assert inst.text.status == "generated"


def test_documentreference_10(base_settings):
    """No. 10 tests collection for DocumentReference.
    Test File: DocumentReference-genomicFile2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "DocumentReference-genomicFile2.json"
    )
    inst = documentreference.DocumentReference.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentReference" == inst.resource_type

    impl_documentreference_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_10(inst2)
