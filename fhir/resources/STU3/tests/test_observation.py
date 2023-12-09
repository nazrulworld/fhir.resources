# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import observation


def impl_observation_1(inst):
    assert inst.code.coding[0].code == "55233-1"
    assert inst.code.coding[0].display == (
        "Genetic analysis master panel-- This is the parent OBR for "
        "the panel holding all of the associated observations that "
        "can be reported with a molecular genetics analysis result."
    )
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-"
        "geneticsDNASequenceVariantName"
    )
    assert inst.extension[0].valueCodeableConcept.text == "NG_007726.3:g.146252T>G"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsGene"
    )
    assert inst.extension[1].valueCodeableConcept.coding[0].code == "3236"
    assert inst.extension[1].valueCodeableConcept.coding[0].display == "EGFR"
    assert (
        inst.extension[1].valueCodeableConcept.coding[0].system
        == "http://www.genenames.org"
    )
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsDNARegionName"
    )
    assert inst.extension[2].valueString == "Exon 21"
    assert inst.extension[3].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-"
        "geneticsGenomicSourceClass"
    )
    assert inst.extension[3].valueCodeableConcept.coding[0].code == "LA6684-0"
    assert inst.extension[3].valueCodeableConcept.coding[0].display == "somatic"
    assert inst.extension[3].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.id == "example-genetics-1"
    assert inst.issued == fhirtypes.Instant.validate("2013-04-03T15:30:10+01:00")
    assert inst.performer[0].display == "Molecular Diagnostics Laboratory"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.specimen.display == "Molecular Specimen ID: MLD45-Z4-1234"
    assert inst.specimen.reference == "Specimen/genetics-example1-somatic"
    assert inst.status == "final"
    assert inst.subject.display == "Molecular Lab Patient ID: HOSP-23456"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueCodeableConcept.coding[0].code == "10828004"
    assert inst.valueCodeableConcept.coding[0].display == "Positive"
    assert inst.valueCodeableConcept.coding[0].system == "http://snomed.info/sct"


def test_observation_1(base_settings):
    """No. 1 tests collection for Observation.
    Test File: observation-example-genetics-1.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-genetics-1.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_1(inst2)


def impl_observation_2(inst):
    assert inst.bodySite.coding[0].code == "71341001:272741003=7771000"
    assert inst.bodySite.coding[0].system == "http://snomed.info/sct"
    assert inst.bodySite.text == "Left Femur"
    assert inst.code.coding[0].code == "24701-5"
    assert inst.code.coding[0].display == "Femur DXA Bone density"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "BMD - Left Femur"
    assert inst.id == "bmd"
    assert inst.performer[0].display == "Acme Imaging Diagnostics"
    assert (
        inst.performer[0].reference
        == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "g/cm-2"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "g/cm²"
    assert float(inst.valueQuantity.value) == float(0.887)


def test_observation_2(base_settings):
    """No. 2 tests collection for Observation.
    Test File: observation-example-bmd.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-bmd.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_2(inst2)


def impl_observation_3(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system == "http://hl7.org/fhir/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "9279-1"
    assert inst.code.coding[0].display == "Respiratory rate"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Respiratory rate"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "respiratory-rate"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "/min"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "breaths/minute"
    assert float(inst.valueQuantity.value) == float(26)


def test_observation_3(base_settings):
    """No. 3 tests collection for Observation.
    Test File: observation-example-respiratory-rate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-respiratory-rate.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_3(inst2)


def impl_observation_4(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system == "http://hl7.org/fhir/observation-category"
    )
    assert inst.code.coding[0].code == "29463-7"
    assert inst.code.coding[0].display == "Body Weight"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.coding[1].code == "3141-9"
    assert inst.code.coding[1].display == "Body weight Measured"
    assert inst.code.coding[1].system == "http://loinc.org"
    assert inst.code.coding[2].code == "27113001"
    assert inst.code.coding[2].display == "Body weight"
    assert inst.code.coding[2].system == "http://snomed.info/sct"
    assert inst.code.coding[3].code == "body-weight"
    assert inst.code.coding[3].display == "Body Weight"
    assert inst.code.coding[3].system == "http://acme.org/devices/clinical-codes"
    assert inst.context.reference == "Encounter/example"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-03-28")
    assert inst.id == "example"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "[lb_av]"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "lbs"
    assert float(inst.valueQuantity.value) == float(185)


def test_observation_4(base_settings):
    """No. 4 tests collection for Observation.
    Test File: observation-example.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_4(inst2)


def impl_observation_5(inst):
    assert inst.code.coding[0].code == "55233-1"
    assert inst.code.coding[0].display == (
        "Genetic analysis master panel-- This is the parent OBR for "
        "the panel holding all of the associated observations that "
        "can be reported with a molecular genetics analysis result."
    )
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsGene"
    )
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "2623"
    assert inst.extension[0].valueCodeableConcept.coding[0].display == "CYP2C9"
    assert (
        inst.extension[0].valueCodeableConcept.coding[0].system
        == "http://www.genenames.org"
    )
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsSequence"
    )
    assert inst.extension[1].valueReference.reference == "Sequence/example-sequence1"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsSequence"
    )
    assert inst.extension[2].valueReference.reference == "Sequence/example-sequence2"
    assert inst.id == "example-haplotype2"
    assert inst.issued == fhirtypes.Instant.validate("2013-04-03T15:30:10+01:00")
    assert inst.related[0].target.reference == "Sequence/example-pgx-1"
    assert inst.related[0].type == "derived-from"
    assert inst.related[1].target.reference == "Sequence/example-pgx-2"
    assert inst.related[1].type == "derived-from"
    assert inst.specimen.display == "Molecular Specimen ID: MLD45-Z4-1234"
    assert inst.specimen.reference == "Specimen/genetics-example1-somatic"
    assert inst.status == "unknown"
    assert inst.subject.display == "J*********** C***********"
    assert inst.subject.reference == "Patient/727127"
    assert inst.text.status == "generated"
    assert inst.valueCodeableConcept.coding[0].code == "PA16581679"
    assert inst.valueCodeableConcept.coding[0].display == "*4"
    assert inst.valueCodeableConcept.coding[0].system == "http://pharmakb.org"


def test_observation_5(base_settings):
    """No. 5 tests collection for Observation.
    Test File: observation-example-haplotype2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-haplotype2.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_5(inst2)


def impl_observation_6(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system == "http://hl7.org/fhir/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "8478-0"
    assert inst.code.coding[0].display == "Mean blood pressure"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Mean blood pressure"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "mbp"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "mm[Hg]"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "mm[Hg]"
    assert float(inst.valueQuantity.value) == float(80)


def test_observation_6(base_settings):
    """No. 6 tests collection for Observation.
    Test File: observation-example-mbp.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-mbp.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_6(inst2)


def impl_observation_7(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system == "http://hl7.org/fhir/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "39156-5"
    assert inst.code.coding[0].display == "Body mass index (BMI) [Ratio]"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "BMI"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "bmi"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "kg/m2"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "kg/m2"
    assert float(inst.valueQuantity.value) == float(16.2)


def test_observation_7(base_settings):
    """No. 7 tests collection for Observation.
    Test File: observation-example-bmi.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-bmi.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_7(inst2)


def impl_observation_8(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system == "http://hl7.org/fhir/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "8302-2"
    assert inst.code.coding[0].display == "Body height"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Body height"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "body-height"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "[in_i]"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "in"
    assert float(inst.valueQuantity.value) == float(66.89999999999999)


def test_observation_8(base_settings):
    """No. 8 tests collection for Observation.
    Test File: observation-example-body-height.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-body-height.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_8(inst2)


def impl_observation_9(inst):
    assert inst.code.text == "eye color"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-05-18")
    assert inst.id == "eye-color"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueString == "blue"


def test_observation_9(base_settings):
    """No. 9 tests collection for Observation.
    Test File: observation-example-eye-color.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-eye-color.json"
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_9(inst2)


def impl_observation_10(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system == "http://hl7.org/fhir/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "8310-5"
    assert inst.code.coding[0].display == "Body temperature"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Body temperature"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "body-temperature"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "Cel"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "C"
    assert float(inst.valueQuantity.value) == float(36.5)


def test_observation_10(base_settings):
    """No. 10 tests collection for Observation.
    Test File: observation-example-body-temperature.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-body-temperature.json"
    )
    inst = observation.Observation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Observation" == inst.resource_type

    impl_observation_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_10(inst2)
