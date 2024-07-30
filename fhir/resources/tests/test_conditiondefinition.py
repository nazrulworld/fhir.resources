# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConditionDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import conditiondefinition
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_conditiondefinition_1(inst):
    assert inst.code.coding[0].code == "55822004"
    assert inst.code.coding[0].display == "Hyperlipidemia (disorder)"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-05-26T10:44:00+10:00"}
        ).valueDateTime
    )
    assert (
        inst.definition[0]
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "https://med.stanford.edu/content/dam/sm/cerc/documents/Hyperlipidemia%20Management%20Protocol.pdf"
            }
        ).valueUri
    )
    assert inst.description == "Hyperlipidemia Status"
    assert inst.hasBodySite is False
    assert inst.hasSeverity is False
    assert inst.hasStage is False
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.25.1"
    assert inst.medication[0].code.coding[0].code == "203151"
    assert inst.medication[0].code.coding[0].display == "Gemfibrozil"
    assert (
        inst.medication[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.nlm.nih.gov/research/umls/rxnorm"}
        ).valueUri
    )
    assert inst.name == "Hyperlipidemia"
    assert inst.observation[0].code.coding[0].code == "24331-1"
    assert (
        inst.observation[0].code.coding[0].display
        == "Lipid 1996 panel - Serum or Plasma"
    )
    assert (
        inst.observation[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.observation[0].code.text == "Lipid Panel"
    assert inst.observation[1].code.coding[0].code == "35200-5"
    assert (
        inst.observation[1].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.observation[1].code.text == "Cholesterol"
    assert inst.observation[2].code.coding[0].code == "35217-9"
    assert (
        inst.observation[2].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.observation[2].code.text == "Triglyceride"
    assert inst.observation[3].code.coding[0].code == "2085-9"
    assert inst.observation[3].code.coding[0].display == "HDL Cholesterol"
    assert (
        inst.observation[3].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.observation[3].code.text == "Cholesterol in HDL"
    assert inst.observation[4].code.coding[0].code == "13457-7"
    assert inst.observation[4].code.coding[0].display == (
        "Cholesterol in LDL [Mass/volume] in Serum or Plasma by " "calculation"
    )
    assert (
        inst.observation[4].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.observation[4].code.text == "LDL Chol. (Calc)"
    assert inst.plan[0].reference.reference == (
        "http://acme.com/fhir/PlanDefinition/fd0e32d8-2ebd-4211-9e50-" "8983efddc2c6"
    )
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Hyperlipidemia Status"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ConditionDefinition/example"}
        ).valueUri
    )


def test_conditiondefinition_1(base_settings):
    """No. 1 tests collection for ConditionDefinition.
    Test File: conditiondefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "conditiondefinition-example.json"
    inst = conditiondefinition.ConditionDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "ConditionDefinition" == inst.get_resource_type()

    impl_conditiondefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConditionDefinition" == data["resourceType"]

    inst2 = conditiondefinition.ConditionDefinition(**data)
    impl_conditiondefinition_1(inst2)
