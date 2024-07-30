# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import molecularsequence
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_molecularsequence_1(inst):
    assert inst.id == "breastcancer"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.relative[0].coordinateSystem.coding[0].code == "LA30100-4"
    assert (
        inst.relative[0].coordinateSystem.coding[0].display
        == "0-based interval counting"
    )
    assert (
        inst.relative[0].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[0].edit[0].end == 32316187
    assert inst.relative[0].edit[0].replacedSequence == "C"
    assert inst.relative[0].edit[0].replacementSequence == "A"
    assert inst.relative[0].edit[0].start == 32316186
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].code
        == "NM_000059.3"
    )
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].display
        == "Homo sapiens BRCA2, DNA repair associated (BRCA2), mRNA"
    )
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.ncbi.nlm.nih.gov/nuccore/"}
        ).valueUri
    )
    assert inst.relative[0].startingSequence.windowEnd == 101499444
    assert inst.relative[0].startingSequence.windowStart == 101488058
    assert inst.subject.reference == "Patient/brcapat"
    assert inst.text.status == "generated"
    assert inst.type == "rna"


def test_molecularsequence_1(base_settings):
    """No. 1 tests collection for MolecularSequence.
    Test File: sequence-genetics-example-breastcancer.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "sequence-genetics-example-breastcancer.json"
    )
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_1(inst2)


def impl_molecularsequence_2(inst):
    assert inst.device.display == "12 lead EKG Device Metric"
    assert inst.id == "sequence-complex-variant"
    assert inst.identifier[0].use == "official"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.performer.display == "HL7"
    assert inst.performer.reference == "Organization/hl7"
    assert inst.relative[0].coordinateSystem.coding[0].code == "LA30100-4"
    assert (
        inst.relative[0].coordinateSystem.coding[0].display
        == "0-based interval counting"
    )
    assert (
        inst.relative[0].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[0].edit[0].end == 128273736
    assert inst.relative[0].edit[0].replacedSequence == "CTCCATTGCATGCGTT"
    assert inst.relative[0].edit[0].replacementSequence == "CTCATTGT"
    assert inst.relative[0].edit[0].start == 128273724
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].code
        == "NC_000002.12"
    )
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.ncbi.nlm.nih.gov/nuccore"}
        ).valueUri
    )
    assert inst.relative[0].startingSequence.strand == "watson"
    assert inst.relative[0].startingSequence.windowEnd == 128273754
    assert inst.relative[0].startingSequence.windowStart == 128273724
    assert inst.specimen.display == "Molecular Specimen ID: MLD45-Z4-1234"
    assert inst.specimen.reference == "Specimen/genetics-example1-somatic"
    assert inst.text.status == "generated"
    assert inst.type == "dna"


def test_molecularsequence_2(base_settings):
    """No. 2 tests collection for MolecularSequence.
    Test File: sequence-complex-variant.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-complex-variant.json"
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_2(inst2)


def impl_molecularsequence_3(inst):
    assert inst.id == "example-TPMT-one"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.relative[0].coordinateSystem.coding[0].code == "LA30102-0"
    assert (
        inst.relative[0].coordinateSystem.coding[0].display
        == "1-based character counting"
    )
    assert (
        inst.relative[0].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[0].edit[0].end == 18139214
    assert inst.relative[0].edit[0].replacedSequence == "G"
    assert inst.relative[0].edit[0].replacementSequence == "A"
    assert inst.relative[0].edit[0].start == 18139214
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].code
        == "NT_007592.15"
    )
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.ncbi.nlm.nih.gov/nuccore"}
        ).valueUri
    )
    assert inst.relative[0].startingSequence.strand == "watson"
    assert inst.relative[0].startingSequence.windowEnd == 18143955
    assert inst.relative[0].startingSequence.windowStart == 18130918
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type == "dna"


def test_molecularsequence_3(base_settings):
    """No. 3 tests collection for MolecularSequence.
    Test File: sequence-example-TPMT-one.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-example-TPMT-one.json"
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_3(inst2)


def impl_molecularsequence_4(inst):
    assert inst.id == "example-pgx-2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.relative[0].coordinateSystem.coding[0].code == "LA30100-4"
    assert (
        inst.relative[0].coordinateSystem.coding[0].display
        == "0-based interval counting"
    )
    assert (
        inst.relative[0].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[0].edit[0].end == 55227979
    assert inst.relative[0].edit[0].replacedSequence == "T"
    assert inst.relative[0].edit[0].replacementSequence == "G"
    assert inst.relative[0].edit[0].start == 55227978
    assert inst.relative[0].startingSequence.orientation == "sense"
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].code
        == "NG_007726.3"
    )
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.ncbi.nlm.nih.gov/nuccore"}
        ).valueUri
    )
    assert inst.relative[0].startingSequence.strand == "watson"
    assert inst.relative[0].startingSequence.windowEnd == 55227980
    assert inst.relative[0].startingSequence.windowStart == 55227970
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type == "dna"


def test_molecularsequence_4(base_settings):
    """No. 4 tests collection for MolecularSequence.
    Test File: sequence-example-pgx-2.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-example-pgx-2.json"
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_4(inst2)


def impl_molecularsequence_5(inst):
    assert inst.formatted[0].contentType == "application/json"
    assert inst.formatted[0].title == "GA4GH API"
    assert (
        inst.formatted[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUrl": "http://grch37.rest.ensembl.org/ga4gh/variants/3:rs1333049?content-type=application/json"
            }
        ).valueUrl
    )
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type == "dna"


def test_molecularsequence_5(base_settings):
    """No. 5 tests collection for MolecularSequence.
    Test File: molecularsequence-example.json
    """
    filename = base_settings["unittest_data_dir"] / "molecularsequence-example.json"
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_5(inst2)


def impl_molecularsequence_6(inst):
    assert inst.id == "coord-1-base"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.relative[0].coordinateSystem.coding[0].code == "LA30102-0"
    assert (
        inst.relative[0].coordinateSystem.coding[0].display
        == "1-based character counting"
    )
    assert (
        inst.relative[0].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[0].edit[0].end == 3
    assert inst.relative[0].edit[0].replacedSequence == "-"
    assert inst.relative[0].edit[0].replacementSequence == "ATG"
    assert inst.relative[0].edit[0].start == 2
    assert inst.relative[0].edit[1].end == 5
    assert inst.relative[0].edit[1].replacedSequence == "A"
    assert inst.relative[0].edit[1].replacementSequence == "T"
    assert inst.relative[0].edit[1].start == 5
    assert inst.relative[0].edit[2].end == 7
    assert inst.relative[0].edit[2].replacedSequence == "T"
    assert inst.relative[0].edit[2].replacementSequence == "-"
    assert inst.relative[0].edit[2].start == 7
    assert inst.relative[0].startingSequence.sequenceString == "ACGTAGTC"
    assert inst.relative[0].startingSequence.strand == "watson"
    assert inst.relative[0].startingSequence.windowEnd == 8
    assert inst.relative[0].startingSequence.windowStart == 1
    assert inst.text.status == "generated"
    assert inst.type == "dna"


def test_molecularsequence_6(base_settings):
    """No. 6 tests collection for MolecularSequence.
    Test File: coord-1base-example.json
    """
    filename = base_settings["unittest_data_dir"] / "coord-1base-example.json"
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_6(inst2)


def impl_molecularsequence_7(inst):
    assert inst.id == "example-TPMT-two"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.relative[0].coordinateSystem.coding[0].code == "LA30102-0"
    assert (
        inst.relative[0].coordinateSystem.coding[0].display
        == "1-based character counting"
    )
    assert (
        inst.relative[0].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[0].edit[0].end == 18131012
    assert inst.relative[0].edit[0].replacedSequence == "C"
    assert inst.relative[0].edit[0].replacementSequence == "T"
    assert inst.relative[0].edit[0].start == 18131012
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].code
        == "NT_007592.15"
    )
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.ncbi.nlm.nih.gov/nuccore"}
        ).valueUri
    )
    assert inst.relative[0].startingSequence.strand == "watson"
    assert inst.relative[0].startingSequence.windowEnd == 18143955
    assert inst.relative[0].startingSequence.windowStart == 18130918
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type == "dna"


def test_molecularsequence_7(base_settings):
    """No. 7 tests collection for MolecularSequence.
    Test File: sequence-example-TPMT-two.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-example-TPMT-two.json"
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_7(inst2)


def impl_molecularsequence_8(inst):
    assert inst.id == "example-pgx-1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.relative[0].coordinateSystem.coding[0].code == "LA30100-4"
    assert (
        inst.relative[0].coordinateSystem.coding[0].display
        == "0-based interval counting"
    )
    assert (
        inst.relative[0].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[0].edit[0].end == 55227977
    assert inst.relative[0].edit[0].replacedSequence == "T"
    assert inst.relative[0].edit[0].replacementSequence == "G"
    assert inst.relative[0].edit[0].start == 55227976
    assert inst.relative[0].startingSequence.orientation == "sense"
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].code
        == "NG_007726.3"
    )
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.ncbi.nlm.nih.gov/nuccore"}
        ).valueUri
    )
    assert inst.relative[0].startingSequence.strand == "watson"
    assert inst.relative[0].startingSequence.windowEnd == 55227980
    assert inst.relative[0].startingSequence.windowStart == 55227970
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type == "dna"


def test_molecularsequence_8(base_settings):
    """No. 8 tests collection for MolecularSequence.
    Test File: sequence-example-pgx-1.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-example-pgx-1.json"
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_8(inst2)


def impl_molecularsequence_9(inst):
    assert inst.id == "coord-0-base"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.relative[0].coordinateSystem.coding[0].code == "LA30101-2"
    assert (
        inst.relative[0].coordinateSystem.coding[0].display
        == "0-based character counting"
    )
    assert (
        inst.relative[0].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[0].edit[0].end == 2
    assert inst.relative[0].edit[0].replacedSequence == "-"
    assert inst.relative[0].edit[0].replacementSequence == "ATG"
    assert inst.relative[0].edit[0].start == 2
    assert inst.relative[0].edit[1].end == 5
    assert inst.relative[0].edit[1].replacedSequence == "A"
    assert inst.relative[0].edit[1].replacementSequence == "T"
    assert inst.relative[0].edit[1].start == 4
    assert inst.relative[0].edit[2].end == 7
    assert inst.relative[0].edit[2].replacedSequence == "T"
    assert inst.relative[0].edit[2].replacementSequence == "-"
    assert inst.relative[0].edit[2].start == 6
    assert inst.relative[0].startingSequence.sequenceString == "ACGTAGTC"
    assert inst.relative[0].startingSequence.strand == "watson"
    assert inst.relative[0].startingSequence.windowEnd == 8
    assert inst.relative[0].startingSequence.windowStart == 0
    assert inst.text.status == "generated"
    assert inst.type == "dna"


def test_molecularsequence_9(base_settings):
    """No. 9 tests collection for MolecularSequence.
    Test File: coord-0base-example.json
    """
    filename = base_settings["unittest_data_dir"] / "coord-0base-example.json"
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_9(inst2)


def impl_molecularsequence_10(inst):
    assert inst.id == "seq-ordinal"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.relative[0].coordinateSystem.coding[0].code == "LA30102-0"
    assert (
        inst.relative[0].coordinateSystem.coding[0].display
        == "1-based character counting"
    )
    assert (
        inst.relative[0].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[0].ordinalPosition == 1
    assert float(inst.relative[0].sequenceRange.high.value) == float(2194)
    assert float(inst.relative[0].sequenceRange.low.value) == float(1)
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].code
        == "NM_000141.5"
    )
    assert (
        inst.relative[0].startingSequence.sequenceCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.ncbi.nlm.nih.gov/nuccore/"}
        ).valueUri
    )
    assert inst.relative[0].startingSequence.windowEnd == 2194
    assert inst.relative[0].startingSequence.windowStart == 1
    assert inst.relative[1].coordinateSystem.coding[0].code == "LA30102-0"
    assert (
        inst.relative[1].coordinateSystem.coding[0].display
        == "1-based character counting"
    )
    assert (
        inst.relative[1].coordinateSystem.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.relative[1].ordinalPosition == 2
    assert float(inst.relative[1].sequenceRange.high.value) == float(4899)
    assert float(inst.relative[1].sequenceRange.low.value) == float(2194)
    assert (
        inst.relative[1].startingSequence.sequenceCodeableConcept.coding[0].code
        == "NM_000245.4"
    )
    assert (
        inst.relative[1].startingSequence.sequenceCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.ncbi.nlm.nih.gov/nuccore/"}
        ).valueUri
    )
    assert inst.relative[1].startingSequence.windowEnd == 6822
    assert inst.relative[1].startingSequence.windowStart == 1923
    assert inst.text.status == "generated"
    assert inst.type == "rna"


def test_molecularsequence_10(base_settings):
    """No. 10 tests collection for MolecularSequence.
    Test File: sequence-example-ordinal.json
    """
    filename = base_settings["unittest_data_dir"] / "sequence-example-ordinal.json"
    inst = molecularsequence.MolecularSequence.model_validate_json(
        filename.read_bytes()
    )
    assert "MolecularSequence" == inst.get_resource_type()

    impl_molecularsequence_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = molecularsequence.MolecularSequence(**data)
    impl_molecularsequence_10(inst2)
