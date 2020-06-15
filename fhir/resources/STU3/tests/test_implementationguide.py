# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import implementationguide


def impl_implementationguide_1(inst):
    assert inst.binary[0] == "http://h7.org/fhir/fhir.css"
    assert inst.contact[0].name == "ONC"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://www.healthit.gov"
    assert inst.contact[1].name == "HL7"
    assert inst.contact[1].telecom[0].system == "url"
    assert inst.contact[1].telecom[0].value == "http://hl7.org/fhir"
    assert inst.copyright == "Published by ONC under the standard FHIR license (CC0)"
    assert inst.date == fhirtypes.DateTime.validate("2015-01-01")
    assert inst.dependency[0].type == "reference"
    assert inst.dependency[0].uri == "http://hl7.org/fhir/ImplementationGuide/uscore"
    assert inst.experimental is False
    assert inst.fhirVersion == "1.0.0"
    assert inst.global_fhir[0].profile.reference == "StructureDefinition/daf-patient"
    assert inst.global_fhir[0].type == "Patient"
    assert inst.id == "example"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.name == "Data Access Framework (DAF)"
    assert (
        inst.package[0].description
        == "Base package (not broken up into multiple packages)"
    )
    assert inst.package[0].name == "test"
    assert inst.package[0].resource[0].acronym == "daf-tst"
    assert (
        inst.package[0].resource[0].description
        == "A test example to show how a package works"
    )
    assert inst.package[0].resource[0].example is True
    assert (
        inst.package[0].resource[0].exampleFor.reference
        == "StructureDefinition/daf-patient"
    )
    assert inst.package[0].resource[0].name == "Test Example"
    assert inst.package[0].resource[0].sourceUri == "test.html"
    assert inst.page.kind == "page"
    assert inst.page.page[0].format == "text/html"
    assert inst.page.page[0].kind == "list"
    assert inst.page.page[0].package[0] == "test"
    assert inst.page.page[0].source == "list.html"
    assert inst.page.page[0].title == "Value Set Page"
    assert inst.page.page[0].type[0] == "ValueSet"
    assert inst.page.source == "patient-example.html"
    assert inst.page.title == "Example Patient Page"
    assert inst.publisher == "ONC / HL7 Joint project"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/us/daf"
    assert inst.version == "0"


def test_implementationguide_1(base_settings):
    """No. 1 tests collection for ImplementationGuide.
    Test File: implementationguide-example.json
    """
    filename = base_settings["unittest_data_dir"] / "implementationguide-example.json"
    inst = implementationguide.ImplementationGuide.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImplementationGuide" == inst.resource_type

    impl_implementationguide_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImplementationGuide" == data["resourceType"]

    inst2 = implementationguide.ImplementationGuide(**data)
    impl_implementationguide_1(inst2)
