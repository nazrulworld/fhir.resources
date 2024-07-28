# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodyStructure
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import bodystructure
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_bodystructure_1(inst):
    assert inst.description == "EDD 1/1/2017 confirmation by LMP"
    assert inst.id == "fetus"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://goodhealth.org/bodystructure/identifiers"
        ).valueUri
    )
    assert inst.identifier[0].value == "12345"
    assert inst.includedStructure[0].structure.coding[0].code == "83418008"
    assert (
        inst.includedStructure[0].structure.coding[0].display
        == "Entire fetus (body structure)"
    )
    assert (
        inst.includedStructure[0].structure.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.includedStructure[0].structure.text == "Fetus"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_bodystructure_1(base_settings):
    """No. 1 tests collection for BodyStructure.
    Test File: bodystructure-example-fetus.json
    """
    filename = base_settings["unittest_data_dir"] / "bodystructure-example-fetus.json"
    inst = bodystructure.BodyStructure.model_validate_json(filename.read_bytes())
    assert "BodyStructure" == inst.get_resource_type()

    impl_bodystructure_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "BodyStructure" == data["resourceType"]

    inst2 = bodystructure.BodyStructure(**data)
    impl_bodystructure_1(inst2)


def impl_bodystructure_2(inst):
    assert inst.description == "7 cm maximum diameter"
    assert inst.id == "tumor"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://goodhealth.org/bodystructure/identifiers"
        ).valueUri
    )
    assert inst.identifier[0].value == "12345"
    assert inst.image[0].contentType == "application/dicom"
    assert (
        inst.image[0].url
        == ExternalValidatorModel(
            valueUrl="http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details"
        ).valueUrl
    )
    assert inst.includedStructure[0].structure.coding[0].code == "78961009"
    assert (
        inst.includedStructure[0].structure.coding[0].display
        == "Splenic structure (body structure)"
    )
    assert (
        inst.includedStructure[0].structure.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.includedStructure[0].structure.text == "Spleen"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.morphology.coding[0].code == "4147007"
    assert inst.morphology.coding[0].display == "Mass (morphologic abnormality)"
    assert (
        inst.morphology.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.morphology.text == "Splenic mass"
    assert inst.patient.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_bodystructure_2(base_settings):
    """No. 2 tests collection for BodyStructure.
    Test File: bodystructure-example-tumor.json
    """
    filename = base_settings["unittest_data_dir"] / "bodystructure-example-tumor.json"
    inst = bodystructure.BodyStructure.model_validate_json(filename.read_bytes())
    assert "BodyStructure" == inst.get_resource_type()

    impl_bodystructure_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "BodyStructure" == data["resourceType"]

    inst2 = bodystructure.BodyStructure(**data)
    impl_bodystructure_2(inst2)


def impl_bodystructure_3(inst):
    assert inst.active is False
    assert inst.description == "inner surface (volar) of the left forearm"
    assert inst.id == "skin-patch"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://goodhealth.org/bodystructure/identifiers"
        ).valueUri
    )
    assert inst.identifier[0].value == "12345"
    assert inst.includedStructure[0].laterality.coding[0].code == "419161000"
    assert inst.includedStructure[0].laterality.coding[0].display == "Unilateral left"
    assert (
        inst.includedStructure[0].laterality.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.includedStructure[0].laterality.text == "Left"
    assert inst.includedStructure[0].qualifier[0].coding[0].code == "263929005"
    assert inst.includedStructure[0].qualifier[0].coding[0].display == "Volar"
    assert (
        inst.includedStructure[0].qualifier[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.includedStructure[0].qualifier[0].text == "Volar"
    assert inst.includedStructure[0].structure.coding[0].code == "14975008"
    assert inst.includedStructure[0].structure.coding[0].display == "Forearm"
    assert (
        inst.includedStructure[0].structure.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.includedStructure[0].structure.text == "Forearm"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.morphology.text == "Skin patch"
    assert inst.patient.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_bodystructure_3(base_settings):
    """No. 3 tests collection for BodyStructure.
    Test File: bodystructure-example-skin-patch.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "bodystructure-example-skin-patch.json"
    )
    inst = bodystructure.BodyStructure.model_validate_json(filename.read_bytes())
    assert "BodyStructure" == inst.get_resource_type()

    impl_bodystructure_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "BodyStructure" == data["resourceType"]

    inst2 = bodystructure.BodyStructure(**data)
    impl_bodystructure_3(inst2)
