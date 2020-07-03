# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from .. import fhirtypes  # noqa: F401
from .. import observation


def test_Observation_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "obs-genetics-example3-mutationlist-4.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_1(inst2)


def impl_Observation_1(inst):
    assert inst.code.coding[0].code == "49874-1"
    assert inst.code.coding[0].display == "ABCB4 gene mutation analysis"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.component[0].code.coding[0].code == "53037-8"
    assert inst.component[0].code.coding[0].display == (
        "Genetic disease sequence variation interpretation"
    )
    assert inst.component[0].code.coding[0].system == "http://loinc.org"
    assert inst.component[0].valueCodeableConcept.coding[0].code == "LA6675-8"

    assert inst.component[0].valueCodeableConcept.coding[0].display == "Benign"

    assert inst.component[0].valueCodeableConcept.coding[0].system == (
        "http://www.genenames.org"
    )

    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName"
    )
    assert inst.extension[0].valueString == "intron 26"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/geneticsVariationId"
    )

    assert inst.extension[1].valueCodeableConcept.coding[0].code == "31653"
    assert inst.extension[1].valueCodeableConcept.coding[0].display == "c.3487-16T>C"

    assert inst.extension[1].valueCodeableConcept.coding[0].system == (
        "http://www.ncbi.nlm.nih.gov/projects/SNP"
    )
    assert inst.id == "genetics-example3-mutationlist-4"
    assert inst.status == "final"
    assert inst.text.status == "generated"


def testObservation2(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "observation-example-f206-staphylococcus.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_2(inst2)


def impl_Observation_2(inst):
    assert inst.code.coding[0].code == "104177"
    assert inst.code.coding[0].display == "Blood culture"
    assert inst.code.coding[0].system == "http://acmelabs.org"
    assert inst.code.coding[1].code == "600-7"
    assert inst.code.coding[1].display == "Bacteria identified in Blood by Culture"
    assert inst.code.coding[1].system == "http://loinc.org"
    assert inst.id == "f206"
    assert inst.interpretation.coding[0].code == "POS"
    assert inst.interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.issued == fhirtypes.Instant.validate("2013-03-11T10:28:00+01:00")

    assert inst.method.coding[0].code == "104177005"
    assert inst.method.coding[0].display == (
        "Blood culture for bacteria, including anaerobic screen"
    )
    assert inst.method.coding[0].system == "http://snomed.info/sct"
    assert inst.status == "final"
    assert inst.text.status == "generated"
    assert inst.valueCodeableConcept.coding[0].code == "3092008"
    assert inst.valueCodeableConcept.coding[0].display == "Staphylococcus aureus"
    assert inst.valueCodeableConcept.coding[0].system == "http://snomed.info/sct"


def test_Observation_3(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-f202-temperature.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_3(inst2)


def impl_Observation_3(inst):
    assert inst.bodySite.coding[0].code == "74262004"
    assert inst.bodySite.coding[0].display == "Oral cavity"
    assert inst.bodySite.coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[0].code == "BT"
    assert inst.code.coding[0].display == "Body temperature"
    assert inst.code.coding[0].system == "http://acme.lab"
    assert inst.code.coding[1].code == "8310-5"
    assert inst.code.coding[1].display == "Body temperature"
    assert inst.code.coding[1].system == "http://loinc.org"
    assert inst.code.coding[2].code == "56342008"
    assert inst.code.coding[2].display == "Temperature taking"
    assert inst.code.coding[2].system == "http://snomed.info/sct"
    assert inst.code.text == "Body temperature"
    assert inst.id == "f202"
    assert inst.interpretation.coding[0].code == "H"
    assert inst.interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.issued == fhirtypes.Instant.validate("2013-04-04T13:27:00+01:00")

    assert inst.method.coding[0].code == "89003005"
    assert inst.method.coding[0].display == "Oral temperature taking"
    assert inst.method.coding[0].system == "http://snomed.info/sct"
    assert inst.referenceRange[0].low.unit == "degrees C"
    assert float(inst.referenceRange[0].low.value) == 37.5
    assert inst.status == "entered-in-error"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "258710007"
    assert inst.valueQuantity.system == "http://snomed.info/sct"
    assert inst.valueQuantity.unit == "degrees C"
    assert inst.valueQuantity.value == 39


def test_Observation_4(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-glasgow-qa.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_4(inst2)


def impl_Observation_4(inst):
    assert inst.code.coding[0].code == "9269-2"
    assert inst.code.coding[0].display == "Glasgow coma score total"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Glasgow Coma Scale , (GCS)"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2014-12-11T04:44:16Z")

    assert inst.id == "gcs-qa"
    assert inst.referenceRange[0].high.code == "{score}"
    assert inst.referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].high.value == 8
    assert inst.referenceRange[0].meaning.text == "Severe TBI"
    assert inst.referenceRange[1].high.code == "{score}"
    assert inst.referenceRange[1].high.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[1].high.value == 12
    assert inst.referenceRange[1].low.code == "{score}"
    assert inst.referenceRange[1].low.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[1].low.value == 9
    assert inst.referenceRange[1].meaning.text == "Moderate TBI"
    assert inst.referenceRange[2].low.code == "{score}"
    assert inst.referenceRange[2].low.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[2].low.value == 13
    assert inst.referenceRange[2].meaning.text == "Mild TBI"
    assert inst.related[0].type == "derived-from"
    assert inst.status == "final"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "{score}"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.value == 13


def test_Observation_5(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "obs-genetics-example3-mutationlist-1.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_5(inst2)


def impl_Observation_5(inst):
    assert inst.code.coding[0].code == "49874-1"
    assert inst.code.coding[0].display == "ABCB4 gene mutation analysis"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.component[0].code.coding[0].code == "53037-8"
    assert inst.component[0].code.coding[0].display == (
        "Genetic disease sequence variation interpretation"
    )
    assert inst.component[0].code.coding[0].system == "http://loinc.org"
    assert inst.component[0].valueCodeableConcept.coding[0].code == "LA6682-4"
    assert inst.component[0].valueCodeableConcept.coding[0].display == (
        "Unknown significance"
    )
    assert inst.component[0].valueCodeableConcept.coding[0].system == (
        "http://www.genenames.org"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/geneticsDNASequenceVariation"
    )
    assert inst.extension[0].valueString == "c.2708T>C"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName"
    )
    assert inst.extension[1].valueString == "Exon 23"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/geneticsAminoAcidChange"
    )
    assert inst.extension[2].valueString == "p.R969H"
    assert inst.id == "genetics-example3-mutationlist-1"
    assert inst.status == "final"
    assert inst.text.status == "generated"


def test_Observation_6(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-bloodpressure.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_6(inst2)


def impl_Observation_6(inst):
    assert inst.bodySite.coding[0].code == "368209003"
    assert inst.bodySite.coding[0].display == "Right arm"
    assert inst.bodySite.coding[0].system == "http://snomed.info/sct"
    assert inst.code.coding[0].code == "55284-4"
    assert inst.code.coding[0].display == "Blood pressure systolic & diastolic"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.component[0].code.coding[0].code == "8480-6"
    assert inst.component[0].code.coding[0].display == "Systolic blood pressure"
    assert inst.component[0].code.coding[0].system == "http://loinc.org"
    assert inst.component[0].code.coding[1].code == "271649006"
    assert inst.component[0].code.coding[1].display == "Systolic blood pressure"

    assert inst.component[0].code.coding[1].system == "http://snomed.info/sct"
    assert inst.component[0].code.coding[2].code == "bp-s"
    assert inst.component[0].code.coding[2].display == "Systolic Blood pressure"
    assert inst.component[0].code.coding[2].system == (
        "http://acme.org/devices/clinical-codes"
    )
    assert inst.component[0].valueQuantity.unit == "mm[Hg]"
    assert inst.component[0].valueQuantity.value == 107
    assert inst.component[1].code.coding[0].code == "8462-4"
    assert inst.component[1].code.coding[0].display == "Diastolic blood pressure"
    assert inst.component[1].code.coding[0].system == "http://loinc.org"
    assert inst.component[1].valueQuantity.unit == "mm[Hg]"
    assert inst.component[1].valueQuantity.value == 60
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2012-09-17")

    assert inst.id == "blood-pressure"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:uuid:187e0c12-8dd2-67e2-99b2-bf273c878281"
    assert inst.interpretation.coding[0].code == "L"
    assert inst.interpretation.coding[0].display == "Below low normal"
    assert inst.interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.interpretation.text == "low"
    assert inst.meta.lastUpdated == fhirtypes.DateTime.validate(
        "2014-01-30T22:35:23+11:00"
    )

    assert inst.status == "final"
    assert inst.text.status == "generated"


def test_Observation_7(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "obs-genetics-example3-mutationlist-3.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_7(inst2)


def impl_Observation_7(inst):
    assert inst.code.coding[0].code == "49874-1"
    assert inst.code.coding[0].display == "ABCB4 gene mutation analysis"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.component[0].code.coding[0].code == "53037-8"
    assert inst.component[0].code.coding[0].display == (
        "Genetic disease sequence variation interpretation"
    )
    assert inst.component[0].code.coding[0].system == "http://loinc.org"
    assert inst.component[0].valueCodeableConcept.coding[0].code == "LA6675-8"
    assert inst.component[0].valueCodeableConcept.coding[0].display == "Benign"
    assert inst.component[0].valueCodeableConcept.coding[0].system == (
        "http://www.genenames.org"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName"
    )
    assert inst.extension[0].valueString == "intron 16"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/geneticsVariationId"
    )
    assert inst.extension[1].valueCodeableConcept.coding[0].code == "31668"
    assert inst.extension[1].valueCodeableConcept.coding[0].display == "c.2211+16C>T"
    assert inst.extension[1].valueCodeableConcept.coding[0].system == (
        "http://www.ncbi.nlm.nih.gov/projects/SNP"
    )
    assert inst.id == "genetics-example3-mutationlist-3"
    assert inst.status == "final"
    assert inst.text.status == "generated"


def test_Observation_8(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-f005-hemoglobin.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_8(inst2)


def impl_Observation_8(inst):
    assert inst.code.coding[0].code == "718-7"
    assert inst.code.coding[0].display == "Hemoglobin [Mass/volume] in Blood"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2013-04-05T10:30:10+01:00"
    )

    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2013-04-02T10:30:10+01:00"
    )

    assert inst.id == "f005"
    assert inst.identifier[0].system == (
        "http://www.bmc.nl/zorgportal/identifiers/observations"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "6327"
    assert inst.interpretation.coding[0].code == "L"
    assert inst.interpretation.coding[0].display == "Below low normal"
    assert inst.interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.issued == fhirtypes.DateTime.validate("2013-04-03T15:30:10+01:00")

    assert inst.referenceRange[0].high.code == "g/dL"
    assert inst.referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].high.unit == "g/dl"
    assert inst.referenceRange[0].high.value == 10
    assert inst.referenceRange[0].low.code == "g/dL"
    assert inst.referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].low.unit == "g/dl"
    assert float(inst.referenceRange[0].low.value) == 7.5
    assert inst.status == "final"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "g/dL"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "g/dl"
    assert float(inst.valueQuantity.value) == 7.2


def test_Observation_9(base_settings):
    filename = base_settings["unittest_data_dir"] / "observation-example-glasgow.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_9(inst2)


def impl_Observation_9(inst):
    assert inst.code.coding[0].code == "9269-2"
    assert inst.code.coding[0].display == "Glasgow coma score total"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Glasgow Coma Scale , (GCS)"
    assert inst.contained[0].id == "motor"
    assert inst.contained[1].id == "verbal"
    assert inst.contained[2].id == "eyes"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2014-12-11T04:44:16Z")

    assert inst.id == "glasgow"
    assert inst.referenceRange[0].high.code == "{score}"
    assert inst.referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[0].high.value == 8
    assert inst.referenceRange[0].meaning.text == "Severe TBI"
    assert inst.referenceRange[1].high.code == "{score}"
    assert inst.referenceRange[1].high.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[1].high.value == 12
    assert inst.referenceRange[1].low.code == "{score}"
    assert inst.referenceRange[1].low.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[1].low.value == 9
    assert inst.referenceRange[1].meaning.text == "Moderate TBI"
    assert inst.referenceRange[2].low.code == "{score}"
    assert inst.referenceRange[2].low.system == "http://unitsofmeasure.org"
    assert inst.referenceRange[2].low.value == 13
    assert inst.referenceRange[2].meaning.text == "Mild TBI"
    assert inst.related[0].type == "derived-from"
    assert inst.related[1].type == "derived-from"
    assert inst.related[2].type == "derived-from"
    assert inst.status == "final"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "{score}"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.value == 13


def offtest_Observation_10(base_settings):
    filename = base_settings["unittest_data_dir"] / "observation-example.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type
    impl_Observation_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_Observation_10(inst2)


def impl_Observation_10(inst):
    assert inst.category.coding[0].code == "vital-signs"
    assert inst.category.coding[0].display == "Vital Signs"
    assert inst.category.coding[0].system == (
        "http://hl7.org/fhir/observation-category"
    )
    assert inst.code.coding[0].code == "3141-9"
    assert inst.code.coding[0].display == "Weight Measured"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.coding[1].code == "27113001"
    assert inst.code.coding[1].display == "Body weight"
    assert inst.code.coding[1].system == "http://snomed.info/sct"
    assert inst.code.coding[2].code == "body-weight"
    assert inst.code.coding[2].display == "Body Weight"
    assert inst.code.coding[2].system == "http://acme.org/devices/clinical-codes"
    assert inst.id == "example"
    assert inst.status == "final"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "[lb_av]"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "lbs"
    assert inst.valueQuantity.value == 185
