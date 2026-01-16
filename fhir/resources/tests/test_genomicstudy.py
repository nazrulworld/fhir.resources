# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GenomicStudy
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import genomicstudy
from .conftest import ExternalValidatorModel


def impl_genomicstudy_1(inst):
    assert (
        inst.analysis[0].date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-01-01T01:01:10-06:00"}
        ).valueDateTime
    )
    assert inst.analysis[0].device[0].device.reference == "Device/NGS-device"
    assert (
        inst.analysis[0].device[0].function.coding[0].display
        == "Next Generation Sequencing"
    )
    assert (
        inst.analysis[0].identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicAnalyses"}
        ).valueUri
    )
    assert inst.analysis[0].identifier[0].use == "temp"
    assert inst.analysis[0].identifier[0].value == "urn:uuid:1111-1111-1111-1111"
    assert inst.analysis[0].input[0].file.reference == "DocumentReference/genomicFile1"
    assert inst.analysis[0].input[0].type.coding[0].code == "vcf"
    assert inst.analysis[0].input[0].type.coding[0].display == "VCF"
    assert (
        inst.analysis[0].instantiatesUri
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://pubmed.ncbi.nlm.nih.gov/33927380/"}
        ).valueUri
    )
    assert (
        inst.analysis[0].note[0].text
        == "This is a next generation sequencing analysis of a proband."
    )
    assert (
        inst.analysis[0].performer[0].actor.reference == "Practitioner/practitioner02"
    )
    assert inst.analysis[0].performer[0].role.coding[0].code == "PRF"
    assert inst.analysis[0].performer[0].role.coding[0].display == "Performer"
    assert (
        inst.analysis[0].performer[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html"
            }
        ).valueUri
    )
    assert inst.analysis[0].specimen[0].reference == "Specimen/denovo-1"
    assert inst.analysis[0].title == (
        "Proband Sequence Variation Detection Using Next Generation " "Sequencing"
    )
    assert (
        inst.analysis[1].date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-01-01T01:01:10-06:00"}
        ).valueDateTime
    )
    assert inst.analysis[1].device[0].device.reference == "Device/NGS-device"
    assert inst.analysis[1].focus[0].reference == "Patient/denovoMother"
    assert (
        inst.analysis[1].identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicAnalyses"}
        ).valueUri
    )
    assert inst.analysis[1].identifier[0].use == "temp"
    assert inst.analysis[1].identifier[0].value == "urn:uuid:1111-1111-1111-1112"
    assert inst.analysis[1].input[0].file.reference == "DocumentReference/genomicFile2"
    assert inst.analysis[1].input[0].type.coding[0].code == "vcf"
    assert inst.analysis[1].input[0].type.coding[0].display == "VCF"
    assert (
        inst.analysis[1].instantiatesUri
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://pubmed.ncbi.nlm.nih.gov/33927380/"}
        ).valueUri
    )
    assert inst.analysis[1].note[0].text == (
        "This is a next generation sequencing analysis of a mother of" " a proband."
    )
    assert (
        inst.analysis[1].performer[0].actor.reference == "Practitioner/practitioner02"
    )
    assert inst.analysis[1].performer[0].role.coding[0].code == "PRF"
    assert inst.analysis[1].performer[0].role.coding[0].display == "Performer"
    assert (
        inst.analysis[1].performer[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html"
            }
        ).valueUri
    )
    assert inst.analysis[1].specimen[0].reference == "Specimen/denovo-2"
    assert inst.analysis[1].title == (
        "Maternal Sequence Variation Detection Using Next Generation " "Sequencing"
    )
    assert (
        inst.analysis[2].date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-01-01T01:01:10-06:00"}
        ).valueDateTime
    )
    assert inst.analysis[2].device[0].device.reference == "Device/NGS-device"
    assert inst.analysis[2].focus[0].reference == "Patient/denovoFather"
    assert (
        inst.analysis[2].identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicAnalyses"}
        ).valueUri
    )
    assert inst.analysis[2].identifier[0].use == "temp"
    assert inst.analysis[2].identifier[0].value == "urn:uuid:1111-1111-1111-1113"
    assert inst.analysis[2].input[0].file.reference == "DocumentReference/genomicFile3"
    assert inst.analysis[2].input[0].type.coding[0].code == "vcf"
    assert inst.analysis[2].input[0].type.coding[0].display == "VCF"
    assert (
        inst.analysis[2].instantiatesUri
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://pubmed.ncbi.nlm.nih.gov/33927380/"}
        ).valueUri
    )
    assert inst.analysis[2].note[0].text == (
        "This is a next generation sequencing analysis of a father of" " a proband."
    )
    assert (
        inst.analysis[2].performer[0].actor.reference == "Practitioner/practitioner02"
    )
    assert inst.analysis[2].performer[0].role.coding[0].code == "PRF"
    assert inst.analysis[2].performer[0].role.coding[0].display == "Performer"
    assert (
        inst.analysis[2].performer[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html"
            }
        ).valueUri
    )
    assert inst.analysis[2].specimen[0].reference == "Specimen/denovo-3"
    assert inst.analysis[2].title == (
        "Paternal Sequence Variation Detection Using Next Generation " "Sequencing"
    )
    assert (
        inst.analysis[3].date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-01-01T03:01:10-06:00"}
        ).valueDateTime
    )
    assert inst.analysis[3].device[0].device.reference == "Device/Triodenovo-SW"
    assert (
        inst.analysis[3].identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicAnalyses"}
        ).valueUri
    )
    assert inst.analysis[3].identifier[0].use == "temp"
    assert inst.analysis[3].identifier[0].value == "urn:uuid:1111-1111-1111-1114"
    assert inst.analysis[3].input[0].file.reference == "DocumentReference/genomicFile1"
    assert inst.analysis[3].input[0].type.coding[0].code == "vcf"
    assert inst.analysis[3].input[0].type.coding[0].display == "VCF"
    assert inst.analysis[3].input[1].file.reference == "DocumentReference/genomicFile2"
    assert inst.analysis[3].input[1].type.coding[0].code == "vcf"
    assert inst.analysis[3].input[1].type.coding[0].display == "VCF"
    assert inst.analysis[3].input[2].file.reference == "DocumentReference/genomicFile3"
    assert inst.analysis[3].input[2].type.coding[0].code == "vcf"
    assert inst.analysis[3].input[2].type.coding[0].display == "VCF"
    assert (
        inst.analysis[3].instantiatesUri
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6885382/"}
        ).valueUri
    )
    assert inst.analysis[3].note[0].text == (
        "This is a next generation sequencing analysis of the "
        "comparison analysis of proband and parents sequences."
    )
    assert (
        inst.analysis[3].performer[0].actor.reference == "Practitioner/practitioner02"
    )
    assert inst.analysis[3].performer[0].role.coding[0].code == "PRF"
    assert inst.analysis[3].performer[0].role.coding[0].display == "Performer"
    assert (
        inst.analysis[3].performer[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html"
            }
        ).valueUri
    )
    assert inst.analysis[3].title == "De Novo Mutation Detection and Interpretation"
    assert inst.basedOn[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.description == "De novo mutation study of the patient."
    assert inst.encounter.reference == "Encounter/denovoEncounter"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicstudies"}
        ).valueUri
    )
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "urn:uuid:1111-1111-1111-1111"
    assert inst.interpreter[0].reference == "Practitioner/practitioner02"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == (
        "This de novo mutation is urgent and important for "
        "establishing the treatment plan."
    )
    assert inst.reason[0].concept.coding[0].code == "267431006"
    assert (
        inst.reason[0].concept.coding[0].display
        == "Disorder of lipid metabolism (disorder)"
    )
    assert (
        inst.reason[0].concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.referrer.reference == "Practitioner/practitioner01"
    assert (
        inst.startDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-01-01"}
        ).valueDateTime
    )
    assert inst.status == "unknown"
    assert inst.subject.reference == "Patient/denovoChild"
    assert inst.text.status == "additional"
    assert inst.type[0].coding[0].code == "fam-var-segr"
    assert inst.type[0].coding[0].display == "Familial variant segregation"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/genomicstudy-type"}
        ).valueUri
    )


def test_genomicstudy_1(base_settings):
    """No. 1 tests collection for GenomicStudy.
    Test File: genomicstudy-example.json
    """
    filename = base_settings["unittest_data_dir"] / "genomicstudy-example.json"
    inst = genomicstudy.GenomicStudy.model_validate_json(filename.read_bytes())
    assert "GenomicStudy" == inst.get_resource_type()

    impl_genomicstudy_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "GenomicStudy" == data["resourceType"]

    inst2 = genomicstudy.GenomicStudy(**data)
    impl_genomicstudy_1(inst2)


def impl_genomicstudy_2(inst):
    assert (
        inst.analysis[0].date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-07-01T01:01:10-06:00"}
        ).valueDateTime
    )
    assert inst.analysis[0].device[0].device.reference == "Device/NGS-device"
    assert inst.analysis[0].focus[0].reference == "Patient/mother"
    assert (
        inst.analysis[0].identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicAnalyses"}
        ).valueUri
    )
    assert inst.analysis[0].identifier[0].use == "temp"
    assert inst.analysis[0].identifier[0].value == "urn:uuid:1111-1111-1111-1112"
    assert (
        inst.analysis[0].instantiatesUri
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://pubmed.ncbi.nlm.nih.gov/33927380/"}
        ).valueUri
    )
    assert inst.analysis[0].note[0].text == (
        "This is a next generation sequencing analysis of a mother of" " a proband."
    )
    assert (
        inst.analysis[0].performer[0].actor.reference == "Practitioner/practitioner02"
    )
    assert inst.analysis[0].performer[0].role.coding[0].code == "PRF"
    assert inst.analysis[0].performer[0].role.coding[0].display == "Performer"
    assert (
        inst.analysis[0].performer[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html"
            }
        ).valueUri
    )
    assert inst.analysis[0].specimen[0].reference == "Specimen/specimenMother"
    assert inst.analysis[0].title == (
        "Maternal Sequence Variation Detection Using Next Generation " "Sequencing"
    )
    assert (
        inst.analysis[1].date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-07-01T01:01:10-06:00"}
        ).valueDateTime
    )
    assert inst.analysis[1].device[0].device.reference == "Device/NGS-device"
    assert inst.analysis[1].focus[0].reference == "Patient/father"
    assert (
        inst.analysis[1].identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicAnalyses"}
        ).valueUri
    )
    assert inst.analysis[1].identifier[0].use == "temp"
    assert inst.analysis[1].identifier[0].value == "urn:uuid:1111-1111-1111-1113"
    assert (
        inst.analysis[1].instantiatesUri
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://pubmed.ncbi.nlm.nih.gov/33927380/"}
        ).valueUri
    )
    assert inst.analysis[1].note[0].text == (
        "This is a next generation sequencing analysis of a father of" " a proband."
    )
    assert (
        inst.analysis[1].performer[0].actor.reference == "Practitioner/practitioner02"
    )
    assert inst.analysis[1].performer[0].role.coding[0].code == "PRF"
    assert inst.analysis[1].performer[0].role.coding[0].display == "Performer"
    assert (
        inst.analysis[1].performer[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html"
            }
        ).valueUri
    )
    assert inst.analysis[1].specimen[0].reference == "Specimen/specimenFather"
    assert inst.analysis[1].title == (
        "Paternal Sequence Variation Detection Using Next Generation " "Sequencing"
    )
    assert (
        inst.analysis[2].date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-07-01T03:01:10-06:00"}
        ).valueDateTime
    )
    assert inst.analysis[2].device[0].device.reference == "Device/Triodenovo-SW"
    assert inst.analysis[2].focus[0].reference == "Patient/denovoChild"
    assert (
        inst.analysis[2].focus[1].reference == "RelatedPerson/relatedPersonDenovoFather"
    )
    assert (
        inst.analysis[2].focus[2].reference == "RelatedPerson/relatedPersonDenovoMother"
    )
    assert (
        inst.analysis[2].identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicAnalyses"}
        ).valueUri
    )
    assert inst.analysis[2].identifier[0].use == "temp"
    assert inst.analysis[2].identifier[0].value == "urn:uuid:1111-1111-1111-1114"
    assert (
        inst.analysis[2].input[0].file.reference
        == "DocumentReference/genomicFileProband"
    )
    assert inst.analysis[2].input[0].type.coding[0].code == "bam"
    assert inst.analysis[2].input[0].type.coding[0].display == "BAM"
    assert (
        inst.analysis[2].input[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/genomicstudy-dataformat"}
        ).valueUri
    )
    assert (
        inst.analysis[2].input[1].file.reference
        == "DocumentReference/genomicFileMother"
    )
    assert inst.analysis[2].input[1].type.coding[0].code == "bam"
    assert inst.analysis[2].input[1].type.coding[0].display == "BAM"
    assert (
        inst.analysis[2].input[1].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/genomicstudy-dataformat"}
        ).valueUri
    )
    assert (
        inst.analysis[2].input[2].file.reference
        == "DocumentReference/genomicFileFather"
    )
    assert inst.analysis[2].input[2].type.coding[0].code == "bam"
    assert inst.analysis[2].input[2].type.coding[0].display == "BAM"
    assert (
        inst.analysis[2].input[2].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/genomicstudy-dataformat"}
        ).valueUri
    )
    assert (
        inst.analysis[2].instantiatesUri
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6885382/"}
        ).valueUri
    )
    assert inst.analysis[2].note[0].text == (
        "This is a next generation sequencing analysis of the "
        "comparison analysis of proband and parents sequences."
    )
    assert (
        inst.analysis[2].output[0].file.reference
        == "DocumentReference/genomicFileGroupAsSubject"
    )
    assert inst.analysis[2].output[0].type.coding[0].code == "vcf"
    assert inst.analysis[2].output[0].type.coding[0].display == "VCF"
    assert (
        inst.analysis[2].output[0].type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/genomicstudy-dataformat"}
        ).valueUri
    )
    assert (
        inst.analysis[2].performer[0].actor.reference == "Practitioner/practitioner02"
    )
    assert inst.analysis[2].performer[0].role.coding[0].code == "PRF"
    assert inst.analysis[2].performer[0].role.coding[0].display == "Performer"
    assert (
        inst.analysis[2].performer[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html"
            }
        ).valueUri
    )
    assert inst.analysis[2].title == "De Novo Mutation Detection and Interpretation"
    assert inst.basedOn[0].reference == "ServiceRequest/genomicSRProband"
    assert inst.basedOn[1].reference == "ServiceRequest/genomicSRMother"
    assert inst.basedOn[2].reference == "ServiceRequest/genomicSRFather"
    assert inst.encounter.reference == "Encounter/denovoEncounter"
    assert inst.id == "example-trio2"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicstudies"}
        ).valueUri
    )
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "urn:uuid:1111-1111-1111-1113"
    assert inst.interpreter[0].reference == "Practitioner/practitioner02"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == (
        "This de novo mutation is urgent and important for "
        "establishing the treatment plan."
    )
    assert inst.reason[0].concept.coding[0].code == "67799006"
    assert (
        inst.reason[0].concept.coding[0].display
        == "Cystic fibrosis, prenatal detection (procedure) |"
    )
    assert (
        inst.reason[0].concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.referrer.reference == "Practitioner/practitioner01"
    assert (
        inst.startDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-05-01"}
        ).valueDateTime
    )
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/proband"
    assert inst.text.status == "additional"
    assert inst.type[0].coding[0].code == "trio"
    assert inst.type[0].coding[0].display == "Trio-analysis"


def test_genomicstudy_2(base_settings):
    """No. 2 tests collection for GenomicStudy.
    Test File: genomicstudy-example-trio2.json
    """
    filename = base_settings["unittest_data_dir"] / "genomicstudy-example-trio2.json"
    inst = genomicstudy.GenomicStudy.model_validate_json(filename.read_bytes())
    assert "GenomicStudy" == inst.get_resource_type()

    impl_genomicstudy_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "GenomicStudy" == data["resourceType"]

    inst2 = genomicstudy.GenomicStudy(**data)
    impl_genomicstudy_2(inst2)


def impl_genomicstudy_3(inst):
    assert inst.analysis[0].changeType[0].coding[0].code == "SO:0001483"
    assert inst.analysis[0].changeType[0].coding[0].display == "SNV"
    assert (
        inst.analysis[0].changeType[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://sequenceontology.org"}
        ).valueUri
    )
    assert inst.analysis[0].changeType[1].coding[0].code == "SO:0002007"
    assert inst.analysis[0].changeType[1].coding[0].display == "MNV"
    assert (
        inst.analysis[0].changeType[1].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://sequenceontology.org"}
        ).valueUri
    )
    assert inst.analysis[0].changeType[2].coding[0].code == "SO:1000032"
    assert inst.analysis[0].changeType[2].coding[0].display == "delins"
    assert (
        inst.analysis[0].changeType[2].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://sequenceontology.org"}
        ).valueUri
    )
    assert (
        inst.analysis[0].date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-03-01T01:01:10-06:00"}
        ).valueDateTime
    )
    assert inst.analysis[0].device[0].device.reference == "Device/NGS-device"
    assert (
        inst.analysis[0].device[0].function.coding[0].display
        == "Next Generation Sequencing"
    )
    assert inst.analysis[0].genomeBuild.coding[0].code == "LA26806-2"
    assert inst.analysis[0].genomeBuild.coding[0].display == "GRCh38"
    assert (
        inst.analysis[0].genomeBuild.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert (
        inst.analysis[0].identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicAnalyses"}
        ).valueUri
    )
    assert inst.analysis[0].identifier[0].use == "official"
    assert inst.analysis[0].identifier[0].value == "urn:uuid:1111-1111-1111-1112"
    assert inst.analysis[0].methodType[0].coding[0].code == "117040002"
    assert (
        inst.analysis[0].methodType[0].coding[0].display
        == "Nucleic acid sequencing (procedure)"
    )
    assert (
        inst.analysis[0].methodType[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.analysis[0].note[0].text == (
        "For technical reasons, PIK3CB was deemed uncallable using " "this method."
    )
    assert (
        inst.analysis[0].output[0].file.reference
        == "DocumentReference/genomicVCFfile_simple"
    )
    assert inst.analysis[0].output[0].type.coding[0].code == "vcf"
    assert inst.analysis[0].output[0].type.coding[0].display == "VCF"
    assert (
        inst.analysis[0].performer[0].actor.reference == "Practitioner/practitioner02"
    )
    assert inst.analysis[0].performer[0].role.coding[0].code == "PRF"
    assert inst.analysis[0].performer[0].role.coding[0].display == "Performer"
    assert (
        inst.analysis[0].performer[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html"
            }
        ).valueUri
    )
    assert (
        inst.analysis[0].regionsCalled[0].reference
        == "DocumentReference/SimpleVariantAnalysis_called"
    )
    assert (
        inst.analysis[0].regionsStudied[0].reference
        == "DocumentReference/WES_FullSequencedRegion_GRCh38"
    )
    assert inst.analysis[0].specimen[0].reference == "Specimen/genomicSpecimen"
    assert inst.analysis[0].title == "Simple variant analysis"
    assert inst.analysis[1].changeType[0].coding[0].code == "SO:0001019"
    assert inst.analysis[1].changeType[0].coding[0].display == "CNV"
    assert (
        inst.analysis[1].changeType[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://sequenceontology.org"}
        ).valueUri
    )
    assert (
        inst.analysis[1].date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-03-01T01:01:10-06:00"}
        ).valueDateTime
    )
    assert inst.analysis[1].genomeBuild.coding[0].code == "LA26806-2"
    assert inst.analysis[1].genomeBuild.coding[0].display == "GRCh38"
    assert (
        inst.analysis[1].genomeBuild.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert (
        inst.analysis[1].identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicAnalyses"}
        ).valueUri
    )
    assert inst.analysis[1].identifier[0].use == "official"
    assert inst.analysis[1].identifier[0].value == "urn:uuid:1111-1111-1111-1115"
    assert inst.analysis[1].methodType[0].coding[0].code == "117040002"
    assert (
        inst.analysis[1].methodType[0].coding[0].display
        == "Nucleic acid sequencing (procedure)"
    )
    assert (
        inst.analysis[1].methodType[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.analysis[1].note[0].text == (
        "For technical reasons, PIK3CB was deemed uncallable using " "this method."
    )
    assert (
        inst.analysis[1].output[0].file.reference
        == "DocumentReference/genomicVCFfile_cnv"
    )
    assert inst.analysis[1].output[0].type.coding[0].code == "vcf"
    assert inst.analysis[1].output[0].type.coding[0].display == "VCF"
    assert (
        inst.analysis[1].performer[0].actor.reference == "Practitioner/practitioner02"
    )
    assert inst.analysis[1].performer[0].role.coding[0].code == "PRF"
    assert inst.analysis[1].performer[0].role.coding[0].display == "Performer"
    assert (
        inst.analysis[1].performer[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html"
            }
        ).valueUri
    )
    assert (
        inst.analysis[1].regionsCalled[0].reference
        == "DocumentReference/CNVAnalysis_called"
    )
    assert (
        inst.analysis[1].regionsStudied[0].reference
        == "DocumentReference/WES_FullSequencedRegion_GRCh38"
    )
    assert inst.analysis[1].specimen[0].reference == "Specimen/genomicSpecimen"
    assert inst.analysis[1].title == "CNV analysis"
    assert inst.basedOn[0].reference == "ServiceRequest/genomicServiceRequest2"
    assert inst.description == (
        "Whole exome sequencing of lung biopsy. 300 genes are "
        "examined for simple variants (SNV, MNV, InDel), and 170 "
        "genes are also examined for CNVs. For technical reasons, "
        "PIK3CB was deemed uncallable."
    )
    assert inst.encounter.reference == "Encounter/genomicEncounter"
    assert inst.id == "example-lungMass"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.somesystemabc.net/identifiers/genomicstudies"}
        ).valueUri
    )
    assert inst.identifier[0].use == "temp"
    assert inst.identifier[0].value == "urn:uuid:1111-1111-1111-1112"
    assert inst.interpreter[0].reference == "Practitioner/practitioner02"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.note[0].text == "For technical reasons, PIK3CB was deemed uncallable."
    assert inst.reason[0].concept.coding[0].code == "309529002"
    assert inst.reason[0].concept.coding[0].display == "Lung mass (finding) "
    assert (
        inst.reason[0].concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.referrer.reference == "Practitioner/practitioner01"
    assert (
        inst.startDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-03-01"}
        ).valueDateTime
    )
    assert inst.status == "registered"
    assert inst.subject.reference == "Patient/genomicPatient"
    assert inst.text.status == "additional"
    assert inst.type[0].coding[0].code == "443968007"
    assert inst.type[0].coding[0].display == (
        "Whole Exome Sequencing - Sequencing of entire coding region "
        "of gene (procedure)"
    )
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )


def test_genomicstudy_3(base_settings):
    """No. 3 tests collection for GenomicStudy.
    Test File: genomicstudy-example-lungMass.json
    """
    filename = base_settings["unittest_data_dir"] / "genomicstudy-example-lungMass.json"
    inst = genomicstudy.GenomicStudy.model_validate_json(filename.read_bytes())
    assert "GenomicStudy" == inst.get_resource_type()

    impl_genomicstudy_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "GenomicStudy" == data["resourceType"]

    inst2 = genomicstudy.GenomicStudy(**data)
    impl_genomicstudy_3(inst2)
