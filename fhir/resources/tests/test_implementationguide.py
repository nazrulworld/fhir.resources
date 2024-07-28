# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import implementationguide
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_implementationguide_1(inst):
    assert inst.contact[0].name == "ONC"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://www.healthit.gov"
    assert inst.contact[1].name == "HL7"
    assert inst.contact[1].telecom[0].system == "url"
    assert inst.contact[1].telecom[0].value == "http://hl7.org/fhir"
    assert inst.copyright == "Published by ONC under the standard FHIR license (CC0)"
    assert inst.date == ExternalValidatorModel(valueDateTime="2015-01-01").valueDateTime
    assert (
        inst.definition.grouping[0].description
        == "Base package (not broken up into multiple packages)"
    )
    assert inst.definition.grouping[0].name == "test"
    assert inst.definition.page.generation == "html"
    assert (
        inst.definition.page.name
        == ExternalValidatorModel(valueUrl="patient-example.html").valueUrl
    )
    assert inst.definition.page.page[0].generation == "html"
    assert (
        inst.definition.page.page[0].name
        == ExternalValidatorModel(valueUrl="list.html").valueUrl
    )
    assert inst.definition.page.page[0].title == "Value Set Page"
    assert inst.definition.page.title == "Example Patient Page"
    assert inst.definition.parameter[0].code.code == "apply"
    assert (
        inst.definition.parameter[0].code.system
        == ExternalValidatorModel(
            valueUri="http://hl7.org/fhir/guide-parameter-code"
        ).valueUri
    )
    assert inst.definition.parameter[0].value == "version"
    assert (
        inst.definition.resource[0].description
        == "A test example to show how an implementation guide works"
    )
    assert inst.definition.resource[0].name == "Test Example"
    assert (
        inst.definition.resource[0].profile[0]
        == "http://hl7.org/fhir/us/core/StructureDefinition/patient"
    )
    assert inst.definition.resource[0].reference.reference == "Patient/test"
    assert inst.dependsOn[0].uri == "http://hl7.org/fhir/ImplementationGuide/uscore"
    assert inst.experimental is False
    assert inst.fhirVersion[0] == "5.0.0"
    assert (
        inst.global_fhir[0].profile
        == "http://hl7.org/fhir/us/core/StructureDefinition/patient"
    )
    assert inst.global_fhir[0].type == "Patient"
    assert inst.id == "example"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel(valueUri="urn:iso:std:iso:3166").valueUri
    )
    assert inst.license == "CC0-1.0"
    assert inst.manifest.image[0] == "fhir.png"
    assert inst.manifest.other[0] == "fhir.css"
    assert inst.manifest.page[0].anchor[0] == "patient-example"
    assert inst.manifest.page[0].anchor[1] == "tx"
    assert inst.manifest.page[0].anchor[2] == "uml"
    assert inst.manifest.page[0].name == "patient-example.html"
    assert inst.manifest.page[0].title == "Test Patient Example"
    assert (
        inst.manifest.rendering
        == ExternalValidatorModel(valueUrl="http://hl7.org/fhir/us/daf").valueUrl
    )
    assert (
        inst.manifest.resource[0].profile[0]
        == "http://hl7.org/fhir/us/core/StructureDefinition/patient"
    )
    assert inst.manifest.resource[0].reference.reference == "Patient/test"
    assert (
        inst.manifest.resource[0].relativePath
        == ExternalValidatorModel(valueUrl="patient-example.html").valueUrl
    )
    assert inst.name == "DataAccessFrameworkDAF"
    assert inst.packageId == "hl7.fhir.us.daf"
    assert inst.publisher == "ONC / HL7 Joint project"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Data Access Framework (DAF)"
    assert (
        inst.url
        == ExternalValidatorModel(valueUri="http://hl7.org/fhir/us/daf").valueUri
    )
    assert inst.version == "0"


def test_implementationguide_1(base_settings):
    """No. 1 tests collection for ImplementationGuide.
    Test File: implementationguide-example.json
    """
    filename = base_settings["unittest_data_dir"] / "implementationguide-example.json"
    inst = implementationguide.ImplementationGuide.model_validate_json(
        filename.read_bytes()
    )
    assert "ImplementationGuide" == inst.get_resource_type()

    impl_implementationguide_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ImplementationGuide" == data["resourceType"]

    inst2 = implementationguide.ImplementationGuide(**data)
    impl_implementationguide_1(inst2)
