# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import conceptmap


def impl_conceptmap_1(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2023-03-26T15:21:02+11:00")
    assert inst.description == (
        'Canonical Mapping for "The lifecycle status of an ' 'artifact."'
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "draft"
    assert inst.group[0].element[0].target[0].code == "draft"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "active"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "retired"
    assert inst.group[0].element[2].target[0].code == "inactive"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "unknown"
    assert inst.group[0].element[3].target[0].code == "unknown"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/publication-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-publication-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "PublicationStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/publication-status"
    )
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "PublicationStatus"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-publication-status"
    assert inst.version == "5.0.0"


def test_conceptmap_1(base_settings):
    """No. 1 tests collection for ConceptMap.
    Test File: sc-valueset-publication-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-publication-status.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_1(inst2)


def impl_conceptmap_2(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2023-03-26T15:21:02+11:00")
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "home"
    assert inst.group[0].element[0].target[0].code == "H"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "work"
    assert inst.group[0].element[1].target[0].code == "WP"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "temp"
    assert inst.group[0].element[2].target[0].code == "TMP"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "old"
    assert inst.group[0].element[3].target[0].code == "OLD"
    assert inst.group[0].element[3].target[0].comment == "Bad or Old"
    assert (
        inst.group[0].element[3].target[0].relationship
        == "source-is-broader-than-target"
    )
    assert inst.group[0].element[3].target[1].code == "BAD"
    assert inst.group[0].element[3].target[1].comment == "Bad or Old"
    assert (
        inst.group[0].element[3].target[1].relationship
        == "source-is-broader-than-target"
    )
    assert inst.group[0].source == "http://hl7.org/fhir/address-use"
    assert inst.group[0].target == "http://terminology.hl7.org/CodeSystem/v3-AddressUse"
    assert inst.id == "cm-address-use-v3"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "v3.AddressUse"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/address-use"
    assert inst.status == "draft"
    assert (
        inst.targetScopeCanonical == "http://terminology.hl7.org/ValueSet/v3-AddressUse"
    )
    assert inst.text.status == "extensions"
    assert inst.title == "v3 map for AddressUse"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-address-use-v3"
    assert inst.version == "5.0.0"


def test_conceptmap_2(base_settings):
    """No. 2 tests collection for ConceptMap.
    Test File: cm-address-use-v3.json
    """
    filename = base_settings["unittest_data_dir"] / "cm-address-use-v3.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_2(inst2)


def impl_conceptmap_3(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == (
        'Canonical Mapping for "This value set includes Status ' 'codes."'
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "draft"
    assert inst.group[0].element[1].target[0].code == "draft"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "active"
    assert inst.group[0].element[2].target[0].code == "active"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].element[3].code == "cancelled"
    assert inst.group[0].element[3].target[0].code == "abandoned"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/fm-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-fm-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "FinancialResourceStatusCodesCanonicalMap"
    assert inst.publisher == "Financial Management"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/fm-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "Financial Resource Status Codes"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-fm-status"
    assert inst.version == "5.0.0"


def test_conceptmap_3(base_settings):
    """No. 3 tests collection for ConceptMap.
    Test File: sc-valueset-fm-status.json
    """
    filename = base_settings["unittest_data_dir"] / "sc-valueset-fm-status.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_3(inst2)


def impl_conceptmap_4(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == 'Canonical Mapping for "FormularyItem Status Codes"'
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "active"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "inactive"
    assert inst.group[0].element[2].target[0].code == "inactive"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/CodeSystem/formularyitem-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-formularyitem-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "FormularyItemStatusCodesCanonicalMap"
    assert inst.publisher == "FHIR Project team"
    assert (
        inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/formularyitem-status"
    )
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "FormularyItem Status Codes"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-formularyitem-status"
    assert inst.version == "5.0.0"


def test_conceptmap_4(base_settings):
    """No. 4 tests collection for ConceptMap.
    Test File: sc-valueset-formularyitem-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "sc-valueset-formularyitem-status.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_4(inst2)


def impl_conceptmap_5(inst):
    assert inst.date == fhirtypes.DateTime.validate("2020-12-24T21:13:15+00:00")
    assert inst.description == "v3 map for CompositionStatus"
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "preliminary"
    assert inst.group[0].element[0].target[0].code == "active"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "final"
    assert inst.group[0].element[1].target[0].code == "completed"
    assert (
        inst.group[0].element[1].target[0].relationship
        == "source-is-narrower-than-target"
    )
    assert inst.group[0].element[2].code == "amended"
    assert inst.group[0].element[2].target[0].code == "completed"
    assert (
        inst.group[0].element[2].target[0].relationship
        == "source-is-narrower-than-target"
    )
    assert inst.group[0].element[3].code == "entered-in-error"
    assert inst.group[0].element[3].target[0].code == "nullified"
    assert inst.group[0].element[3].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/composition-status"
    assert inst.group[0].target == "http://terminology.hl7.org/CodeSystem/v3-ActStatus"
    assert inst.id == "cm-composition-status-v3"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.14.9"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareableconceptmap"
    )
    assert inst.name == "V3CompositionStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert inst.title == "v3 map for CompositionStatus"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-composition-status-v3"
    assert inst.version == "5.0.0"


def test_conceptmap_5(base_settings):
    """No. 5 tests collection for ConceptMap.
    Test File: cm-composition-status-v3.json
    """
    filename = base_settings["unittest_data_dir"] / "cm-composition-status-v3.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_5(inst2)


def impl_conceptmap_6(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
        'Canonical Mapping for "Indicates whether this flag is '
        "active and needs to be displayed to a user, or whether it is"
        ' no longer needed or was entered in error."'
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "active"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "inactive"
    assert inst.group[0].element[2].target[0].code == "inactive"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/flag-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-flag-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "FlagStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/flag-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "Flag Status"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-flag-status"
    assert inst.version == "5.0.0"


def test_conceptmap_6(base_settings):
    """No. 6 tests collection for ConceptMap.
    Test File: sc-valueset-flag-status.json
    """
    filename = base_settings["unittest_data_dir"] / "sc-valueset-flag-status.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_6(inst2)


def impl_conceptmap_7(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert (
        inst.description == 'Canonical Mapping for "The status of the Device record."'
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "active"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "inactive"
    assert inst.group[0].element[2].target[0].code == "inactive"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/device-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-device-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "FHIRDeviceStatusCanonicalMap"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/device-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "FHIR Device Status"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-device-status"
    assert inst.version == "5.0.0"


def test_conceptmap_7(base_settings):
    """No. 7 tests collection for ConceptMap.
    Test File: sc-valueset-device-status.json
    """
    filename = base_settings["unittest_data_dir"] / "sc-valueset-device-status.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_7(inst2)


def impl_conceptmap_8(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2023-03-26T15:21:02+11:00")
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "home"
    assert inst.group[0].element[0].target[0].code == "PRN"
    assert (
        inst.group[0].element[0].target[0].comment
        == "FHIR doesn't distinguish types of homes for contacts"
    )
    assert (
        inst.group[0].element[0].target[0].relationship
        == "source-is-broader-than-target"
    )
    assert inst.group[0].element[0].target[1].code == "ORN"
    assert (
        inst.group[0].element[0].target[1].comment
        == "FHIR doesn't distinguish types of homes for contacts"
    )
    assert (
        inst.group[0].element[0].target[1].relationship
        == "source-is-broader-than-target"
    )
    assert inst.group[0].element[0].target[2].code == "VHN"
    assert (
        inst.group[0].element[0].target[2].comment
        == "FHIR doesn't distinguish types of homes for contacts"
    )
    assert (
        inst.group[0].element[0].target[2].relationship
        == "source-is-broader-than-target"
    )
    assert inst.group[0].element[1].code == "work"
    assert inst.group[0].element[1].target[0].code == "WPN"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "mobile"
    assert inst.group[0].element[2].target[0].code == "PRS"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/contact-point-use"
    assert inst.group[0].target == "http://terminology.hl7.org/CodeSystem/v2-0201"
    assert inst.id == "cm-contact-point-use-v2"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "v2.ContactPointUse"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/contact-point-use"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://terminology.hl7.org/ValueSet/v2-0201"
    assert inst.text.status == "extensions"
    assert inst.title == "v2 map for ContactPointUse"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v2"
    assert inst.version == "5.0.0"


def test_conceptmap_8(base_settings):
    """No. 8 tests collection for ConceptMap.
    Test File: cm-contact-point-use-v2.json
    """
    filename = base_settings["unittest_data_dir"] / "cm-contact-point-use-v2.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_8(inst2)


def impl_conceptmap_9(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == (
        'Canonical Mapping for "Preferred value set for '
        'AllergyIntolerance Clinical Status."'
    )
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "active"
    assert inst.group[0].element[0].target[0].code == "active"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "inactive"
    assert inst.group[0].element[1].target[0].code == "inactive"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "resolved"
    assert inst.group[0].element[2].target[0].code == "resolved"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "clinical"
    )
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-allergyintolerance-clinical"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "AllergyIntoleranceClinicalStatusCodesCanonicalMap"
    assert inst.publisher == "FHIR Project team"
    assert (
        inst.sourceScopeCanonical
        == "http://hl7.org/fhir/ValueSet/allergyintolerance-clinical"
    )
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == (
        'Canonical Mapping for "AllergyIntolerance Clinical Status ' 'Codes"'
    )
    assert inst.url == (
        "http://hl7.org/fhir/ConceptMap/sc-allergyintolerance-" "clinical"
    )
    assert inst.version == "5.0.0"


def test_conceptmap_9(base_settings):
    """No. 9 tests collection for ConceptMap.
    Test File: sc-valueset-allergyintolerance-clinical.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "sc-valueset-allergyintolerance-clinical.json"
    )
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_9(inst2)


def impl_conceptmap_10(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == 'Canonical Mapping for "Medication Status Codes"'
    assert inst.experimental is False
    assert inst.group[0].element[0].code == "entered-in-error"
    assert inst.group[0].element[0].target[0].code == "error"
    assert inst.group[0].element[0].target[0].relationship == "equivalent"
    assert inst.group[0].element[1].code == "active"
    assert inst.group[0].element[1].target[0].code == "active"
    assert inst.group[0].element[1].target[0].relationship == "equivalent"
    assert inst.group[0].element[2].code == "inactive"
    assert inst.group[0].element[2].target[0].code == "inactive"
    assert inst.group[0].element[2].target[0].relationship == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/CodeSystem/medication-status"
    assert inst.group[0].target == "http://hl7.org/fhir/resource-status"
    assert inst.id == "sc-medication-status"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "MedicationStatusCodesCanonicalMap"
    assert inst.publisher == "FHIR Project team"
    assert inst.sourceScopeCanonical == "http://hl7.org/fhir/ValueSet/medication-status"
    assert inst.status == "draft"
    assert inst.targetScopeCanonical == "http://hl7.org/fhir/ValueSet/resource-status"
    assert inst.text.status == "extensions"
    assert inst.title == 'Canonical Mapping for "Medication Status Codes"'
    assert inst.url == "http://hl7.org/fhir/ConceptMap/sc-medication-status"
    assert inst.version == "5.0.0"


def test_conceptmap_10(base_settings):
    """No. 10 tests collection for ConceptMap.
    Test File: sc-valueset-medication-status.json
    """
    filename = base_settings["unittest_data_dir"] / "sc-valueset-medication-status.json"
    inst = conceptmap.ConceptMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ConceptMap" == inst.resource_type

    impl_conceptmap_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_10(inst2)
