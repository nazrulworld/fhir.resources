# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import molecularsequence


def impl_molecularsequence_1(inst):
    assert inst.coordinateSystem == 0
    assert inst.id == "breastcancer"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/brcapat"
    assert inst.referenceSeq.referenceSeqId.coding[0].code == "NM_000059.3"
    assert (
        inst.referenceSeq.referenceSeqId.coding[0].display
        == "Homo sapiens BRCA2, DNA repair associated (BRCA2), mRNA"
    )
    assert (
        inst.referenceSeq.referenceSeqId.coding[0].system
        == "http://www.ncbi.nlm.nih.gov/nuccore/"
    )
    assert inst.referenceSeq.windowEnd == 101499444
    assert inst.referenceSeq.windowStart == 101488058
    assert inst.text.status == "generated"
    assert inst.type == "rna"
    assert inst.variant[0].end == 32316187
    assert inst.variant[0].observedAllele == "A"
    assert inst.variant[0].referenceAllele == "C"
    assert inst.variant[0].start == 32316186


def test_molecularsequence_1(base_settings):
    """No. 1 tests collection for MolecularSequence.
    Test File: sequence-genetics-example-breastcancer.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "sequence-genetics-example-breastcancer.json"
    )
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_1(inst2)


def impl_molecularsequence_2(inst):
    assert inst.coordinateSystem == 0
    assert inst.id == "graphic-example-1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.pointer[0].reference == "MolecularSequence/graphic-example-2"
    assert inst.referenceSeq.referenceSeqId.coding[0].code == "NC_000002.12"
    assert (
        inst.referenceSeq.referenceSeqId.coding[0].system
        == "http://www.ncbi.nlm.nih.gov/nuccore"
    )
    assert inst.referenceSeq.strand == "watson"
    assert inst.referenceSeq.windowEnd == 128273732
    assert inst.referenceSeq.windowStart == 128273724
    assert inst.text.status == "generated"
    assert inst.type == "dna"
    assert inst.variant[0].cigar == "1M"
    assert inst.variant[0].end == 128273726
    assert inst.variant[0].observedAllele == "G"
    assert inst.variant[0].referenceAllele == "T"
    assert inst.variant[0].start == 128273725


def test_molecularsequence_2(base_settings):
    """No. 2 tests collection for MolecularSequence.
    Test File: sequence-graphic-example-1.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-graphic-example-1.json"
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_2(inst2)


def impl_molecularsequence_3(inst):
    assert inst.coordinateSystem == 1
    assert inst.id == "fda-vcfeval-comparison"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.quality[0].end == 101770080
    assert float(inst.quality[0].gtFP) == float(2186)
    assert inst.quality[0].method.coding[0].code == "app-BxfGF8j02pBZzZxbzZxP725P"
    assert inst.quality[0].method.coding[0].system == "https://precision.fda.gov/apps/"
    assert inst.quality[0].method.text == "Vcfeval + Hap.py Comparison"
    assert float(inst.quality[0].precision) == float(0.428005)
    assert float(inst.quality[0].queryFP) == float(10670)
    assert float(inst.quality[0].recall) == float(0.752111)
    assert (
        inst.quality[0].standardSequence.coding[0].code
        == "file-BkZxBZ00bpJVk2q6x43b1YBx"
    )
    assert (
        inst.quality[0].standardSequence.coding[0].system
        == "https://precision.fda.gov/files/"
    )
    assert inst.quality[0].start == 10453
    assert float(inst.quality[0].truthFN) == float(2554)
    assert float(inst.quality[0].truthTP) == float(7749)
    assert inst.quality[0].type == "indel"
    assert inst.quality[1].end == 101770080
    assert float(inst.quality[1].gtFP) == float(493)
    assert inst.quality[1].method.coding[0].code == "app-BxfGF8j02pBZzZxbzZxP725P"
    assert inst.quality[1].method.coding[0].system == "https://precision.fda.gov/apps/"
    assert inst.quality[1].method.text == "Vcfeval + Hap.py Comparison"
    assert float(inst.quality[1].precision) == float(0.808602)
    assert float(inst.quality[1].queryFP) == float(21744)
    assert float(inst.quality[1].recall) == float(0.986642)
    assert (
        inst.quality[1].standardSequence.coding[0].code
        == "file-BkZxBZ00bpJVk2q6x43b1YBx"
    )
    assert (
        inst.quality[1].standardSequence.coding[0].system
        == "https://precision.fda.gov/files/"
    )
    assert inst.quality[1].start == 10453
    assert float(inst.quality[1].truthFN) == float(1247)
    assert float(inst.quality[1].truthTP) == float(92106)
    assert inst.quality[1].type == "snp"
    assert inst.referenceSeq.referenceSeqId.coding[0].code == "NC_000001.11"
    assert (
        inst.referenceSeq.referenceSeqId.coding[0].system
        == "http://www.ncbi.nlm.nih.gov/nuccore"
    )
    assert inst.referenceSeq.strand == "watson"
    assert inst.referenceSeq.windowEnd == 101770080
    assert inst.referenceSeq.windowStart == 10453
    assert inst.repository[0].name == "FDA"
    assert inst.repository[0].type == "login"
    assert (
        inst.repository[0].url
        == "https://precision.fda.gov/jobs/job-ByxYPx809jFVy21KJG74Jg3Y"
    )
    assert inst.text.status == "generated"
    assert inst.variant[0].end == 13117
    assert inst.variant[0].observedAllele == "T"
    assert inst.variant[0].referenceAllele == "G"
    assert inst.variant[0].start == 13116


def test_molecularsequence_3(base_settings):
    """No. 3 tests collection for MolecularSequence.
    Test File: sequence-example-fda-vcfeval.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-example-fda-vcfeval.json"
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_3(inst2)


def impl_molecularsequence_4(inst):
    assert inst.coordinateSystem == 1
    assert inst.device.display == "12 lead EKG Device Metric"
    assert inst.id == "sequence-complex-variant"
    assert inst.identifier[0].use == "official"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer.display == "HL7"
    assert inst.performer.reference == "Organization/hl7"
    assert float(inst.quantity.value) == float(25)
    assert inst.readCoverage == 1
    assert inst.referenceSeq.referenceSeqId.coding[0].code == "NC_000002.12"
    assert (
        inst.referenceSeq.referenceSeqId.coding[0].system
        == "http://www.ncbi.nlm.nih.gov/nuccore"
    )
    assert inst.referenceSeq.strand == "watson"
    assert inst.referenceSeq.windowEnd == 128273754
    assert inst.referenceSeq.windowStart == 128273724
    assert inst.repository[0].datasetId == "Ensembl"
    assert inst.repository[0].readsetId == "v1beta2"
    assert inst.repository[0].type == "other"
    assert inst.specimen.display == "Molecular Specimen ID: MLD45-Z4-1234"
    assert inst.specimen.reference == "Specimen/genetics-example1-somatic"
    assert inst.text.status == "generated"
    assert inst.type == "dna"
    assert inst.variant[0].cigar == "3M1D4M6N2M"
    assert inst.variant[0].end == 128273736
    assert inst.variant[0].observedAllele == "CTCATTGT"
    assert inst.variant[0].referenceAllele == "CTCCATTGCATGCGTT"
    assert inst.variant[0].start == 128273724


def test_molecularsequence_4(base_settings):
    """No. 4 tests collection for MolecularSequence.
    Test File: sequence-complex-variant.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-complex-variant.json"
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_4(inst2)


def impl_molecularsequence_5(inst):
    assert inst.coordinateSystem == 1
    assert inst.id == "example-TPMT-one"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.observedSeq == "T-C-C-C-A-C-C-C"
    assert inst.patient.reference == "Patient/example"
    assert inst.referenceSeq.referenceSeqId.coding[0].code == "NT_007592.15"
    assert (
        inst.referenceSeq.referenceSeqId.coding[0].system
        == "http://www.ncbi.nlm.nih.gov/nuccore"
    )
    assert inst.referenceSeq.strand == "watson"
    assert inst.referenceSeq.windowEnd == 18143955
    assert inst.referenceSeq.windowStart == 18130918
    assert inst.text.status == "generated"
    assert inst.type == "dna"
    assert inst.variant[0].end == 18139214
    assert inst.variant[0].observedAllele == "A"
    assert inst.variant[0].referenceAllele == "G"
    assert inst.variant[0].start == 18139214


def test_molecularsequence_5(base_settings):
    """No. 5 tests collection for MolecularSequence.
    Test File: sequence-example-TPMT-one.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-example-TPMT-one.json"
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_5(inst2)


def impl_molecularsequence_6(inst):
    assert inst.coordinateSystem == 0
    assert inst.id == "example-pgx-2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.referenceSeq.orientation == "sense"
    assert inst.referenceSeq.referenceSeqId.coding[0].code == "NG_007726.3"
    assert (
        inst.referenceSeq.referenceSeqId.coding[0].system
        == "http://www.ncbi.nlm.nih.gov/nuccore"
    )
    assert inst.referenceSeq.strand == "watson"
    assert inst.referenceSeq.windowEnd == 55227980
    assert inst.referenceSeq.windowStart == 55227970
    assert inst.text.status == "generated"
    assert inst.type == "dna"
    assert inst.variant[0].end == 55227979
    assert inst.variant[0].observedAllele == "G"
    assert inst.variant[0].referenceAllele == "T"
    assert inst.variant[0].start == 55227978
    assert inst.variant[0].variantPointer.display == "Target Haplotype Observation"
    assert inst.variant[0].variantPointer.reference == "Observation/example-haplotype2"


def test_molecularsequence_6(base_settings):
    """No. 6 tests collection for MolecularSequence.
    Test File: sequence-example-pgx-2.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-example-pgx-2.json"
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_6(inst2)


def impl_molecularsequence_7(inst):
    assert inst.coordinateSystem == 0
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.referenceSeq.referenceSeqId.coding[0].code == "NC_000009.11"
    assert (
        inst.referenceSeq.referenceSeqId.coding[0].system
        == "http://www.ncbi.nlm.nih.gov/nuccore"
    )
    assert inst.referenceSeq.strand == "watson"
    assert inst.referenceSeq.windowEnd == 22125510
    assert inst.referenceSeq.windowStart == 22125500
    assert inst.repository[0].name == "GA4GH API"
    assert inst.repository[0].type == "openapi"
    assert inst.repository[0].url == (
        "http://grch37.rest.ensembl.org/ga4gh/variants/3:rs1333049?co"
        "ntent-type=application/json"
    )
    assert inst.repository[0].variantsetId == "3:rs1333049"
    assert inst.text.status == "generated"
    assert inst.type == "dna"
    assert inst.variant[0].end == 22125504
    assert inst.variant[0].observedAllele == "C"
    assert inst.variant[0].referenceAllele == "G"
    assert inst.variant[0].start == 22125503


def test_molecularsequence_7(base_settings):
    """No. 7 tests collection for MolecularSequence.
    Test File: molecularsequence-example.json
    """
    filename = base_settings["unittest_data_dir"] / "molecularsequence-example.json"
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_7(inst2)


def impl_molecularsequence_8(inst):
    assert inst.coordinateSystem == 1
    assert inst.id == "fda-example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.quality[0].end == 101770080
    assert float(inst.quality[0].fScore) == float(0.545551)
    assert float(inst.quality[0].gtFP) == float(2186)
    assert inst.quality[0].method.coding[0].code == "job-ByxYPx809jFVy21KJG74Jg3Y"
    assert inst.quality[0].method.coding[0].system == "https://precision.fda.gov/jobs/"
    assert inst.quality[0].method.text == "Vcfeval + Hap.py Comparison"
    assert float(inst.quality[0].precision) == float(0.428005)
    assert float(inst.quality[0].queryFP) == float(10670)
    assert float(inst.quality[0].queryTP) == float(7984)
    assert float(inst.quality[0].recall) == float(0.752111)
    assert (
        inst.quality[0].standardSequence.coding[0].code
        == "file-Bk50V4Q0qVb65P0v2VPbfYPZ"
    )
    assert (
        inst.quality[0].standardSequence.coding[0].system
        == "https://precision.fda.gov/files/"
    )
    assert inst.quality[0].start == 10453
    assert float(inst.quality[0].truthFN) == float(2554)
    assert float(inst.quality[0].truthTP) == float(7749)
    assert inst.quality[0].type == "snp"
    assert inst.referenceSeq.referenceSeqId.coding[0].code == "NC_000001.11"
    assert (
        inst.referenceSeq.referenceSeqId.coding[0].system
        == "http://www.ncbi.nlm.nih.gov/nuccore"
    )
    assert inst.referenceSeq.strand == "watson"
    assert inst.referenceSeq.windowEnd == 101770080
    assert inst.referenceSeq.windowStart == 10453
    assert inst.repository[0].name == "FDA"
    assert inst.repository[0].type == "login"
    assert inst.repository[0].url == (
        "https://precision.fda.gov/files/file-" "Bx37ZK009P4bX5g3qjkFZV38"
    )
    assert inst.repository[0].variantsetId == "file-Bx37ZK009P4bX5g3qjkFZV38"
    assert inst.text.status == "generated"
    assert inst.type == "dna"
    assert inst.variant[0].end == 13117
    assert inst.variant[0].observedAllele == "T"
    assert inst.variant[0].referenceAllele == "G"
    assert inst.variant[0].start == 13116


def test_molecularsequence_8(base_settings):
    """No. 8 tests collection for MolecularSequence.
    Test File: sequence-example-fda.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-example-fda.json"
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_8(inst2)


def impl_molecularsequence_9(inst):
    assert inst.coordinateSystem == 1
    assert inst.id == "coord-1-base"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.observedSeq == "ACATGGTAGC"
    assert inst.referenceSeq.referenceSeqString == "ACGTAGTC"
    assert inst.referenceSeq.strand == "watson"
    assert inst.referenceSeq.windowEnd == 8
    assert inst.referenceSeq.windowStart == 1
    assert inst.text.status == "generated"
    assert inst.type == "dna"
    assert inst.variant[0].cigar == "3I"
    assert inst.variant[0].end == 3
    assert inst.variant[0].observedAllele == "ATG"
    assert inst.variant[0].referenceAllele == "-"
    assert inst.variant[0].start == 2
    assert inst.variant[1].cigar == "3I"
    assert inst.variant[1].end == 5
    assert inst.variant[1].observedAllele == "T"
    assert inst.variant[1].referenceAllele == "A"
    assert inst.variant[1].start == 5
    assert inst.variant[2].cigar == "1D"
    assert inst.variant[2].end == 7
    assert inst.variant[2].observedAllele == "-"
    assert inst.variant[2].referenceAllele == "T"
    assert inst.variant[2].start == 7


def test_molecularsequence_9(base_settings):
    """No. 9 tests collection for MolecularSequence.
    Test File: coord-1base-example.json
    """
    filename = base_settings["unittest_data_dir"] / "coord-1base-example.json"
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_9(inst2)


def impl_molecularsequence_10(inst):
    assert inst.coordinateSystem == 0
    assert inst.id == "graphic-example-4"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.referenceSeq.chromosome.coding[0].code == "2"
    assert inst.referenceSeq.chromosome.coding[0].display == "chromosome 2"
    assert (
        inst.referenceSeq.chromosome.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/chromosome-human"
    )
    assert inst.referenceSeq.genomeBuild == "GRCh 38"
    assert inst.referenceSeq.strand == "watson"
    assert inst.referenceSeq.windowEnd == 128273740
    assert inst.referenceSeq.windowStart == 128273736
    assert inst.text.status == "generated"
    assert inst.type == "dna"


def test_molecularsequence_10(base_settings):
    """No. 10 tests collection for MolecularSequence.
    Test File: sequence-graphic-example-4.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-graphic-example-4.json"
    inst = molecularsequence.MolecularSequence.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MolecularSequence" == inst.resource_type

    impl_molecularsequence_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_10(inst2)
