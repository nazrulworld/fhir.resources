# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Specimen
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import specimen
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_specimen_1(inst):
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:00Z").valueDateTime
    )
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert (
        inst.collection.method.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0488"
        ).valueUri
    )
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "denovo-2"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.somesystemabc.net/identifiers/specimens"
        ).valueUri
    )
    assert inst.identifier[0].value == "2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.receivedTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:01Z").valueDateTime
    )
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "Jane Doe"
    assert inst.subject.reference == "Patient/denovoMother"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_specimen_1(base_settings):
    """No. 1 tests collection for Specimen.
    Test File: Specimen-denovo-2.json
    """
    filename = base_settings["unittest_data_dir"] / "Specimen-denovo-2.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_1(inst2)


def impl_specimen_2(inst):
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:00Z").valueDateTime
    )
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert (
        inst.collection.method.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0488"
        ).valueUri
    )
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "denovo-3"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.somesystemabc.net/identifiers/specimens"
        ).valueUri
    )
    assert inst.identifier[0].value == "3"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.receivedTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:01Z").valueDateTime
    )
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "John Doe"
    assert inst.subject.reference == "Patient/denovoFather"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_specimen_2(base_settings):
    """No. 2 tests collection for Specimen.
    Test File: Specimen-denovo-3.json
    """
    filename = base_settings["unittest_data_dir"] / "Specimen-denovo-3.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_2(inst2)


def impl_specimen_3(inst):
    assert (
        inst.accessionIdentifier.system
        == ExternalValidatorModel(
            valueUri="http://lab.acme.org/specimens/2011"
        ).valueUri
    )
    assert inst.accessionIdentifier.value == "X352356-ISO1"
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2015-08-16T07:03:00Z").valueDateTime
    )
    assert inst.collection.collector.reference == "Practitioner/f202"
    assert inst.collection.method.coding[0].code == "BAP"
    assert (
        inst.collection.method.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0488"
        ).valueUri
    )
    assert inst.contained[0].id == "stool"
    assert inst.id == "isolate"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.note[0].text == "Patient dropped off specimen"
    assert inst.parent[0].reference == "#stool"
    assert (
        inst.receivedTime
        == ExternalValidatorModel(valueDateTime="2015-08-18T07:03:00Z").valueDateTime
    )
    assert inst.role[0].coding[0].code == "p"
    assert inst.role[0].coding[0].display == "Patient"
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "429951000124103"
    assert inst.type.coding[0].display == "Bacterial isolate specimen"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_specimen_3(base_settings):
    """No. 3 tests collection for Specimen.
    Test File: specimen-example-isolate.json
    """
    filename = base_settings["unittest_data_dir"] / "specimen-example-isolate.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_3(inst2)


def impl_specimen_4(inst):
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:00Z").valueDateTime
    )
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert (
        inst.collection.method.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0488"
        ).valueUri
    )
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "specimenMother"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.somesystemabc.net/identifiers/specimens"
        ).valueUri
    )
    assert inst.identifier[0].value == "6"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.receivedTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:01Z").valueDateTime
    )
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "Jane Doe"
    assert inst.subject.reference == "Patient/mother"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_specimen_4(base_settings):
    """No. 4 tests collection for Specimen.
    Test File: Specimen-specimenMother.json
    """
    filename = base_settings["unittest_data_dir"] / "Specimen-specimenMother.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_4(inst2)


def impl_specimen_5(inst):
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:00Z").valueDateTime
    )
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert (
        inst.collection.method.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0488"
        ).valueUri
    )
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "specimenProband"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.somesystemabc.net/identifiers/specimens"
        ).valueUri
    )
    assert inst.identifier[0].value == "5"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.receivedTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:01Z").valueDateTime
    )
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "Child Junior Doe"
    assert inst.subject.reference == "Patient/proband"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_specimen_5(base_settings):
    """No. 5 tests collection for Specimen.
    Test File: Specimen-specimenProband.json
    """
    filename = base_settings["unittest_data_dir"] / "Specimen-specimenProband.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_5(inst2)


def impl_specimen_6(inst):
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:00Z").valueDateTime
    )
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert (
        inst.collection.method.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0488"
        ).valueUri
    )
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "specimenFather"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.somesystemabc.net/identifiers/specimens"
        ).valueUri
    )
    assert inst.identifier[0].value == "7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.receivedTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:01Z").valueDateTime
    )
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "John Doe"
    assert inst.subject.reference == "Patient/father"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_specimen_6(base_settings):
    """No. 6 tests collection for Specimen.
    Test File: Specimen-specimenFather.json
    """
    filename = base_settings["unittest_data_dir"] / "Specimen-specimenFather.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_6(inst2)


def impl_specimen_7(inst):
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2019-03-01T01:01:00Z").valueDateTime
    )
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "129314006"
    assert inst.collection.method.coding[0].display == "Biopsy - action"
    assert (
        inst.collection.method.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.collection.quantity.unit == "mm2"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "genomicSpecimen"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.somesystemabc.net/identifiers/specimens"
        ).valueUri
    )
    assert inst.identifier[0].value == "4"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.receivedTime
        == ExternalValidatorModel(valueDateTime="2019-03-01T01:01:01Z").valueDateTime
    )
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "John Doe"
    assert inst.subject.reference == "Patient/genomicPatient"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122610009"
    assert (
        inst.type.coding[0].display
        == "Specimen from lung obtained by biopsy (specimen)"
    )
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_specimen_7(base_settings):
    """No. 7 tests collection for Specimen.
    Test File: Specimen-genomicSpecimen.json
    """
    filename = base_settings["unittest_data_dir"] / "Specimen-genomicSpecimen.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_7(inst2)


def impl_specimen_8(inst):
    assert (
        inst.accessionIdentifier.system
        == ExternalValidatorModel(valueUri="https://vetmed.iastate.edu/vdl").valueUri
    )
    assert inst.accessionIdentifier.value == "20171120-1234"
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2017-11-14").valueDateTime
    )
    assert inst.collection.collector.display == "James Herriot, FRCVS"
    assert inst.combined == "pooled"
    assert (
        inst.container[0].device.reference
        == "Device/device-example-specimen-container-red-top-vacutainer"
    )
    assert inst.id == "pooled-serum"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.note[0].text == "Pooled serum sample from 30 individuals"
    assert inst.subject.reference == "Group/herd1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "Serum sample, pooled"
    assert inst.type.coding[0].display == "Serum sample, pooled"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(valueUri="https://vetmed.iastate.edu/vdl").valueUri
    )
    assert inst.type.text == "Pooled serum sample"


def test_specimen_8(base_settings):
    """No. 8 tests collection for Specimen.
    Test File: specimen-example-pooled-serum.json
    """
    filename = base_settings["unittest_data_dir"] / "specimen-example-pooled-serum.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_8(inst2)


def impl_specimen_9(inst):
    assert (
        inst.accessionIdentifier.system
        == ExternalValidatorModel(
            valueUri="http://lab.acme.org/specimens/2015"
        ).valueUri
    )
    assert inst.accessionIdentifier.value == "X352356"
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2015-08-18T07:03:00Z").valueDateTime
    )
    assert inst.collection.collector.reference == "Practitioner/f202"
    assert (
        inst.container[0].device.reference
        == "Device/device-example-specimen-container-polycup"
    )
    assert inst.container[0].specimenQuantity.unit == "mls"
    assert float(inst.container[0].specimenQuantity.value) == float(10)
    assert inst.id == "vma-urine"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.processing[0].additive[0].display == "6 N HCl"
    assert inst.processing[0].description == "Acidify to pH < 3.0 with 6 N HCl."
    assert inst.processing[0].method.coding[0].code == "ACID"
    assert (
        inst.processing[0].method.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0373"
        ).valueUri
    )
    assert (
        inst.processing[0].timeDateTime
        == ExternalValidatorModel(valueDateTime="2015-08-18T08:10:00Z").valueDateTime
    )
    assert (
        inst.receivedTime
        == ExternalValidatorModel(valueDateTime="2015-08-18T07:03:00Z").valueDateTime
    )
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RANDU"
    assert inst.type.coding[0].display == "Urine, Random"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0487"
        ).valueUri
    )


def test_specimen_9(base_settings):
    """No. 9 tests collection for Specimen.
    Test File: specimen-example-urine.json
    """
    filename = base_settings["unittest_data_dir"] / "specimen-example-urine.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_9(inst2)


def impl_specimen_10(inst):
    assert (
        inst.collection.collectedDateTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:00Z").valueDateTime
    )
    assert inst.collection.collector.reference == "Practitioner/practitioner01"
    assert inst.collection.method.coding[0].code == "LNV"
    assert (
        inst.collection.method.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0488"
        ).valueUri
    )
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(1)
    assert inst.id == "denovo-1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.somesystemabc.net/identifiers/specimens"
        ).valueUri
    )
    assert inst.identifier[0].value == "1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.receivedTime
        == ExternalValidatorModel(valueDateTime="2021-01-01T01:01:01Z").valueDateTime
    )
    assert inst.request[0].reference == "ServiceRequest/genomicServiceRequest"
    assert inst.status == "available"
    assert inst.subject.display == "Child Junior Doe"
    assert inst.subject.reference == "Patient/denovoChild"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )


def test_specimen_10(base_settings):
    """No. 10 tests collection for Specimen.
    Test File: Specimen-denovo-1.json
    """
    filename = base_settings["unittest_data_dir"] / "Specimen-denovo-1.json"
    inst = specimen.Specimen.model_validate_json(Path(filename).read_bytes())
    assert "Specimen" == inst.get_resource_type()

    impl_specimen_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_10(inst2)
