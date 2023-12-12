# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Specimen
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import specimen


def impl_specimen_1(inst):
    assert inst.accessionIdentifier.system == "http://lab.acme.org/specimens/2011"
    assert inst.accessionIdentifier.value == "X352356-ISO1"
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate(
        "2015-08-16T07:03:00Z"
    )
    assert inst.collection.collector.reference == "Practitioner/f202"
    assert inst.collection.method.coding[0].code == "BAP"
    assert (
        inst.collection.method.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0488"
    )
    assert inst.contained[0].id == "stool"
    assert inst.id == "isolate"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Patient dropped off specimen"
    assert inst.parent[0].reference == "#stool"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2015-08-18T07:03:00Z")
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "429951000124103"
    assert inst.type.coding[0].display == "Bacterial isolate specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_1(base_settings):
    """No. 1 tests collection for Specimen.
    Test File: specimen-example-isolate.json
    """
    filename = base_settings["unittest_data_dir"] / "specimen-example-isolate.json"
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_1(inst2)


def impl_specimen_2(inst):
    assert inst.accessionIdentifier.system == "https://vetmed.iastate.edu/vdl"
    assert inst.accessionIdentifier.value == "20171120-1234"
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate(
        "2017-11-14"
    )
    assert inst.collection.collector.display == "James Herriot, FRCVS"
    assert inst.container[0].type.coding[0].code == "RTT"
    assert inst.container[0].type.coding[0].display == "Red Top Tube"
    assert inst.container[0].type.coding[0].system == "https://vetmed.iastate.edu/vdl"
    assert inst.container[0].type.text == "Red Top Blood Collection Tube"
    assert inst.id == "pooled-serum"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Pooled serum sample from 30 individuals"
    assert inst.subject.reference == "Group/herd1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "Serum sample, pooled"
    assert inst.type.coding[0].display == "Serum sample, pooled"
    assert inst.type.coding[0].system == "https://vetmed.iastate.edu/vdl"
    assert inst.type.text == "Pooled serum sample"


def test_specimen_2(base_settings):
    """No. 2 tests collection for Specimen.
    Test File: specimen-example-pooled-serum.json
    """
    filename = base_settings["unittest_data_dir"] / "specimen-example-pooled-serum.json"
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_2(inst2)


def impl_specimen_3(inst):
    assert inst.accessionIdentifier.system == "http://lab.acme.org/specimens/2015"
    assert inst.accessionIdentifier.value == "X352356"
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate(
        "2015-08-18T07:03:00Z"
    )
    assert inst.collection.collector.reference == "Practitioner/f202"
    assert inst.container[0].capacity.unit == "mls"
    assert float(inst.container[0].capacity.value) == float(50)
    assert inst.container[0].specimenQuantity.unit == "mls"
    assert float(inst.container[0].specimenQuantity.value) == float(10)
    assert inst.container[0].type.text == "Non-sterile specimen container"
    assert inst.id == "vma-urine"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.processing[0].additive[0].display == "6 N HCl"
    assert inst.processing[0].description == "Acidify to pH < 3.0 with 6 N HCl."
    assert inst.processing[0].procedure.coding[0].code == "ACID"
    assert (
        inst.processing[0].procedure.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0373"
    )
    assert inst.processing[0].timeDateTime == fhirtypes.DateTime.validate(
        "2015-08-18T08:10:00Z"
    )
    assert inst.receivedTime == fhirtypes.DateTime.validate("2015-08-18T07:03:00Z")
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "RANDU"
    assert inst.type.coding[0].display == "Urine, Random"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0487"


def test_specimen_3(base_settings):
    """No. 3 tests collection for Specimen.
    Test File: specimen-example-urine.json
    """
    filename = base_settings["unittest_data_dir"] / "specimen-example-urine.json"
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_3(inst2)


def impl_specimen_4(inst):
    assert inst.accessionIdentifier.system == "http://acme.com/labs/accession-ids"
    assert inst.accessionIdentifier.value == "20150816-00124"
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate(
        "2015-08-16T06:40:17Z"
    )
    assert inst.collection.collector.reference == "Practitioner/f202"
    assert inst.container[0].type.coding[0].code == "SST"
    assert inst.container[0].type.coding[0].display == "Serum Separator Tube"
    assert inst.container[0].type.coding[0].system == "http://acme.com/labs"
    assert inst.id == "sst"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.request[0].reference == "ServiceRequest/ft4"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "119364003"
    assert inst.type.coding[0].display == "Serum sample"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_4(base_settings):
    """No. 4 tests collection for Specimen.
    Test File: specimen-example-serum.json
    """
    filename = base_settings["unittest_data_dir"] / "specimen-example-serum.json"
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_4(inst2)


def impl_specimen_5(inst):
    assert inst.accessionIdentifier.system == "http://lab.acme.org/specimens/2011"
    assert inst.accessionIdentifier.value == "X352356"
    assert inst.collection.bodySite.coding[0].code == "49852007"
    assert (
        inst.collection.bodySite.coding[0].display
        == "Structure of median cubital vein (body structure)"
    )
    assert inst.collection.bodySite.coding[0].system == "http://snomed.info/sct"
    assert inst.collection.bodySite.text == "Right median cubital vein"
    assert inst.collection.collectedDateTime == fhirtypes.DateTime.validate(
        "2011-05-30T06:15:00Z"
    )
    assert inst.collection.collector.reference == "Practitioner/example"
    assert inst.collection.method.coding[0].code == "LNV"
    assert (
        inst.collection.method.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0488"
    )
    assert inst.collection.quantity.unit == "mL"
    assert float(inst.collection.quantity.value) == float(6)
    assert inst.contained[0].id == "hep"
    assert inst.container[0].additiveReference.reference == "#hep"
    assert inst.container[0].capacity.unit == "mL"
    assert float(inst.container[0].capacity.value) == float(10)
    assert inst.container[0].description == "Green Gel tube"
    assert inst.container[0].identifier[0].value == "48736-15394-75465"
    assert inst.container[0].specimenQuantity.unit == "mL"
    assert float(inst.container[0].specimenQuantity.value) == float(6)
    assert inst.container[0].type.text == "Vacutainer"
    assert inst.id == "101"
    assert inst.identifier[0].system == "http://ehr.acme.org/identifiers/collections"
    assert inst.identifier[0].value == "23234352356"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Specimen is grossly lipemic"
    assert inst.receivedTime == fhirtypes.DateTime.validate("2011-03-04T07:03:00Z")
    assert inst.request[0].reference == "ServiceRequest/example"
    assert inst.status == "available"
    assert inst.subject.display == "Peter Patient"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_specimen_5(base_settings):
    """No. 5 tests collection for Specimen.
    Test File: specimen-example.json
    """
    filename = base_settings["unittest_data_dir"] / "specimen-example.json"
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type

    impl_specimen_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_specimen_5(inst2)
