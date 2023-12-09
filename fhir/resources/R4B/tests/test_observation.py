# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import observation


def impl_observation_1(inst):
    assert inst.code.coding[0].code == "55233-1"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.device.reference == "Device/example"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2013-04-03T15:30:10+01:00"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsGene"
    )
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "3236"
    assert inst.extension[0].valueCodeableConcept.coding[0].display == "EGFR"
    assert (
        inst.extension[0].valueCodeableConcept.coding[0].system
        == "http://www.genenames.org"
    )
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsDNARegionName"
    )
    assert inst.extension[1].valueString == "Exon 21"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-"
        "geneticsGenomicSourceClass"
    )
    assert inst.extension[2].valueCodeableConcept.coding[0].code == "LA6684-0"
    assert inst.extension[2].valueCodeableConcept.coding[0].display == "somatic"
    assert inst.extension[2].valueCodeableConcept.coding[0].system == "http://loinc.org"
    assert inst.id == "example-genetics-1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.performer[0].display == "Molecular Diagnostics Laboratory"
    assert inst.performer[0].reference == "Practitioner/example"
    assert inst.status == "final"
    assert inst.subject.display == "Molecular Lab Patient ID: HOSP-23456"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "extensions"
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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "9279-1"
    assert inst.code.coding[0].display == "Respiratory rate"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Respiratory rate"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "respiratory-rate"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
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
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-03-28")
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.derivedFrom[0].reference == "MolecularSequence/example-pgx-1"
    assert inst.derivedFrom[1].reference == "MolecularSequence/example-pgx-2"
    assert inst.device.reference == "Device/example"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2013-04-03T15:30:10+01:00"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsGene"
    )
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "2623"
    assert inst.extension[0].valueCodeableConcept.coding[0].display == "CYP2C9"
    assert (
        inst.extension[0].valueCodeableConcept.coding[0].system
        == "http://www.genenames.org"
    )
    assert inst.id == "example-haplotype2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "unknown"
    assert inst.subject.display == "J*********** C***********"
    assert inst.subject.reference == "Patient/727127"
    assert inst.text.status == "extensions"
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
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "8478-0"
    assert inst.code.coding[0].display == "Mean blood pressure"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Mean blood pressure"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "mbp"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
    assert inst.code.coding[0].code == "59041-4"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.device.reference == "Device/example"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate(
        "2021-03-03T14:50:23-05:00"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsGene"
    )
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "KX470182.1"
    assert inst.extension[0].valueCodeableConcept.coding[0].display == "BRCA"
    assert (
        inst.extension[0].valueCodeableConcept.coding[0].system
        == "https://www.ncbi.nlm.nih.gov/nuccore"
    )
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-" "ethnicity"
    )
    assert inst.extension[1].valueCodeableConcept.coding[0].code == "413581001"
    assert (
        inst.extension[1].valueCodeableConcept.coding[0].display
        == "Unknown racial group"
    )
    assert (
        inst.extension[1].valueCodeableConcept.coding[0].system
        == "http://browser.ihtsdotools.org/"
    )
    assert inst.id == "example-genetics-brcapat"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.subject.display == "Patient1 with Breast Cancer FamilyHistory"
    assert inst.subject.reference == "Patient/brcapat"
    assert inst.text.status == "extensions"


def test_observation_7(base_settings):
    """No. 7 tests collection for Observation.
    Test File: observation-example-genetics-brcapat.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-genetics-brcapat.json"
    )
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
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "39156-5"
    assert inst.code.coding[0].display == "Body mass index (BMI) [Ratio]"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "BMI"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "bmi"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "kg/m2"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "kg/m2"
    assert float(inst.valueQuantity.value) == float(16.2)


def test_observation_8(base_settings):
    """No. 8 tests collection for Observation.
    Test File: observation-example-bmi.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-bmi.json"
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
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "8302-2"
    assert inst.code.coding[0].display == "Body height"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Body height"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("1999-07-02")
    assert inst.id == "body-height"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "[in_i]"
    assert inst.valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.valueQuantity.unit == "in"
    assert float(inst.valueQuantity.value) == float(66.89999999999999)


def test_observation_9(base_settings):
    """No. 9 tests collection for Observation.
    Test File: observation-example-body-height.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-body-height.json"
    )
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
    assert inst.code.text == "eye color"
    assert inst.effectiveDateTime == fhirtypes.DateTime.validate("2016-05-18")
    assert inst.id == "eye-color"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueString == "blue"


def test_observation_10(base_settings):
    """No. 10 tests collection for Observation.
    Test File: observation-example-eye-color.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-eye-color.json"
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
