# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import observation
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_observation_1(inst):
    assert inst.bodySite.coding[0].code == "71341001:272741003=7771000"
    assert (
        inst.bodySite.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.bodySite.text == "Left Femur"
    assert inst.code.coding[0].code == "24701-5"
    assert inst.code.coding[0].display == "Femur DXA Bone density"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert inst.code.text == "BMD - Left Femur"
    assert inst.id == "bmd"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
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
    assert (
        inst.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.valueQuantity.unit == "g/cm²"
    assert float(inst.valueQuantity.value) == float(0.887)


def test_observation_1(base_settings):
    """No. 1 tests collection for Observation.
    Test File: observation-example-bmd.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-bmd.json"
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_1(inst2)


def impl_observation_2(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/observation-category"
        ).valueUri
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "9279-1"
    assert inst.code.coding[0].display == "Respiratory rate"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert inst.code.text == "Respiratory rate"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel(valueDateTime="1999-07-02").valueDateTime
    )
    assert inst.id == "respiratory-rate"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "/min"
    assert (
        inst.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.valueQuantity.unit == "breaths/minute"
    assert float(inst.valueQuantity.value) == float(26)


def test_observation_2(base_settings):
    """No. 2 tests collection for Observation.
    Test File: observation-example-respiratory-rate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-respiratory-rate.json"
    )
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_2(inst2)


def impl_observation_3(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/observation-category"
        ).valueUri
    )
    assert inst.code.coding[0].code == "29463-7"
    assert inst.code.coding[0].display == "Body Weight"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert inst.code.coding[1].code == "3141-9"
    assert inst.code.coding[1].display == "Body weight Measured"
    assert (
        inst.code.coding[1].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert inst.code.coding[2].code == "27113001"
    assert inst.code.coding[2].display == "Body weight"
    assert (
        inst.code.coding[2].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.code.coding[3].code == "body-weight"
    assert inst.code.coding[3].display == "Body Weight"
    assert (
        inst.code.coding[3].system
        == ExternalValidatorModel(
            valueUri="http://acme.org/devices/clinical-codes"
        ).valueUri
    )
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel(valueDateTime="2016-03-28").valueDateTime
    )
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "[lb_av]"
    assert (
        inst.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.valueQuantity.unit == "lbs"
    assert float(inst.valueQuantity.value) == float(185)


def test_observation_3(base_settings):
    """No. 3 tests collection for Observation.
    Test File: observation-example.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example.json"
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_3(inst2)


def impl_observation_4(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/observation-category"
        ).valueUri
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "8478-0"
    assert inst.code.coding[0].display == "Mean blood pressure"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert inst.code.text == "Mean blood pressure"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel(valueDateTime="1999-07-02").valueDateTime
    )
    assert inst.id == "mbp"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "mm[Hg]"
    assert (
        inst.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.valueQuantity.unit == "mm[Hg]"
    assert float(inst.valueQuantity.value) == float(80)


def test_observation_4(base_settings):
    """No. 4 tests collection for Observation.
    Test File: observation-example-mbp.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-mbp.json"
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_4(inst2)


def impl_observation_5(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/observation-category"
        ).valueUri
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "39156-5"
    assert inst.code.coding[0].display == "Body mass index (BMI) [Ratio]"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert inst.code.text == "BMI"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel(valueDateTime="1999-07-02").valueDateTime
    )
    assert inst.id == "bmi"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "kg/m2"
    assert (
        inst.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.valueQuantity.unit == "kg/m2"
    assert float(inst.valueQuantity.value) == float(16.2)


def test_observation_5(base_settings):
    """No. 5 tests collection for Observation.
    Test File: observation-example-bmi.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-bmi.json"
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_5(inst2)


def impl_observation_6(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/observation-category"
        ).valueUri
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "8302-2"
    assert inst.code.coding[0].display == "Body height"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert inst.code.text == "Body height"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel(valueDateTime="1999-07-02").valueDateTime
    )
    assert inst.id == "body-height"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "[in_i]"
    assert (
        inst.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.valueQuantity.unit == "in"
    assert float(inst.valueQuantity.value) == float(66.89999999999999)


def test_observation_6(base_settings):
    """No. 6 tests collection for Observation.
    Test File: observation-example-body-height.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-body-height.json"
    )
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_6(inst2)


def impl_observation_7(inst):
    assert inst.code.text == "eye color"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel(valueDateTime="2016-05-18").valueDateTime
    )
    assert inst.id == "eye-color"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueString == "blue"


def test_observation_7(base_settings):
    """No. 7 tests collection for Observation.
    Test File: observation-example-eye-color.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-eye-color.json"
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_7(inst2)


def impl_observation_8(inst):
    assert inst.category[0].coding[0].code == "vital-signs"
    assert inst.category[0].coding[0].display == "Vital Signs"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/observation-category"
        ).valueUri
    )
    assert inst.category[0].text == "Vital Signs"
    assert inst.code.coding[0].code == "8310-5"
    assert inst.code.coding[0].display == "Body temperature"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert inst.code.text == "Body temperature"
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel(valueDateTime="1999-07-02").valueDateTime
    )
    assert inst.id == "body-temperature"
    assert inst.meta.profile[0] == "http://hl7.org/fhir/StructureDefinition/vitalsigns"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "Cel"
    assert (
        inst.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.valueQuantity.unit == "C"
    assert float(inst.valueQuantity.value) == float(36.5)


def test_observation_8(base_settings):
    """No. 8 tests collection for Observation.
    Test File: observation-example-body-temperature.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-body-temperature.json"
    )
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_8(inst2)


def impl_observation_9(inst):
    assert inst.category[0].coding[0].code == "exam"
    assert inst.category[0].coding[0].display == "Exam"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/observation-category"
        ).valueUri
    )
    assert inst.category[0].text == "Exam"
    assert inst.code.coding[0].code == "410211008"
    assert inst.code.coding[0].display == "Tracheostomy care assessment (procedure)"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel(
            valueDateTime="2018-03-11T16:07:54+00:00"
        ).valueDateTime
    )
    assert inst.focus[0].reference == "Patient/infant-mom"
    assert inst.id == "trachcare"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/infant"
    assert inst.text.status == "generated"
    assert (
        inst.valueString == "Mother is trained to change her child's tracheostomy tube"
    )


def test_observation_9(base_settings):
    """No. 9 tests collection for Observation.
    Test File: observation-example-trachcare.json
    """
    filename = base_settings["unittest_data_dir"] / "observation-example-trachcare.json"
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_9(inst2)


def impl_observation_10(inst):
    assert inst.code.coding[0].code == "11555-0"
    assert inst.code.coding[0].display == "Base excess in Blood by calculation"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://loinc.org").valueUri
    )
    assert (
        inst.effectiveDateTime
        == ExternalValidatorModel(
            valueDateTime="2013-04-02T10:30:10+01:00"
        ).valueDateTime
    )
    assert inst.id == "f002"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.bmc.nl/zorgportal/identifiers/observations"
        ).valueUri
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "6324"
    assert inst.interpretation[0].coding[0].code == "H"
    assert inst.interpretation[0].coding[0].display == "High"
    assert (
        inst.interpretation[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation"
        ).valueUri
    )
    assert (
        inst.issued
        == ExternalValidatorModel(valueInstant="2013-04-03T15:30:10+01:00").valueInstant
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.performer[0].display == "A. Langeveld"
    assert inst.performer[0].reference == "Practitioner/f005"
    assert inst.referenceRange[0].high.code == "mmol/L"
    assert (
        inst.referenceRange[0].high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.referenceRange[0].high.unit == "mmol/l"
    assert float(inst.referenceRange[0].high.value) == float(11.2)
    assert inst.referenceRange[0].low.code == "mmol/L"
    assert (
        inst.referenceRange[0].low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.referenceRange[0].low.unit == "mmol/l"
    assert float(inst.referenceRange[0].low.value) == float(7.1)
    assert inst.status == "final"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"
    assert inst.valueQuantity.code == "mmol/L"
    assert (
        inst.valueQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.valueQuantity.unit == "mmol/l"
    assert float(inst.valueQuantity.value) == float(12.6)


def test_observation_10(base_settings):
    """No. 10 tests collection for Observation.
    Test File: observation-example-f002-excess.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "observation-example-f002-excess.json"
    )
    inst = observation.Observation.model_validate_json(filename.read_bytes())
    assert "Observation" == inst.get_resource_type()

    impl_observation_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Observation" == data["resourceType"]

    inst2 = observation.Observation(**data)
    impl_observation_10(inst2)
