# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import conceptmap


def impl_conceptmap_1(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.group[0].element[0].code == "home"
    assert inst.group[0].element[0].target[0].code == "H"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "work"
    assert inst.group[0].element[1].target[0].code == "WP"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "temp"
    assert inst.group[0].element[2].target[0].code == "TMP"
    assert inst.group[0].element[2].target[0].equivalence == "equal"
    assert inst.group[0].element[3].code == "old"
    assert inst.group[0].element[3].target[0].code == "OLD"
    assert inst.group[0].element[3].target[0].comment == "Bad or Old"
    assert inst.group[0].element[3].target[0].equivalence == "narrower"
    assert inst.group[0].element[3].target[1].code == "BAD"
    assert inst.group[0].element[3].target[1].comment == "Bad or Old"
    assert inst.group[0].element[3].target[1].equivalence == "narrower"
    assert inst.group[0].source == "http://hl7.org/fhir/address-use"
    assert inst.group[0].target == "http://hl7.org/fhir/v3/AddressUse"
    assert inst.id == "cm-address-use-v3"
    assert inst.name == "v3 map for AddressUse"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceReference.reference == "http://hl7.org/fhir/ValueSet/address-use"
    assert inst.status == "draft"
    assert (
        inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v3-AddressUse"
    )
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-address-use-v3"


def test_conceptmap_1(base_settings):
    """No. 1 tests collection for ConceptMap.
    Test File: cm-address-use-v3.json
    """
    filename = base_settings["unittest_data_dir"] / "cm-address-use-v3.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.group[0].element[0].code == "in-progress"
    assert inst.group[0].element[0].target[0].code == "active"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "on-hold"
    assert inst.group[0].element[1].target[0].code == "suspended"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "completed"
    assert inst.group[0].element[2].target[0].code == "completed"
    assert inst.group[0].element[2].target[0].equivalence == "equal"
    assert inst.group[0].element[3].code == "entered-in-error"
    assert inst.group[0].element[3].target[0].code == "nullified"
    assert inst.group[0].element[3].target[0].equivalence == "equal"
    assert inst.group[0].element[4].code == "stopped"
    assert inst.group[0].element[4].target[0].code == "aborted"
    assert inst.group[0].element[4].target[0].equivalence == "equal"
    assert inst.group[0].source == "http://hl7.org/fhir/medication-admin-status"
    assert inst.group[0].target == "http://hl7.org/fhir/v3/ActStatus"
    assert inst.id == "cm-medication-admin-status-v3"
    assert inst.name == "v3 map for MedicationAdministrationStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/medication-admin-status"
    )
    assert inst.status == "draft"
    assert inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v3-ActStatus"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-medication-admin-status-v3"


def test_conceptmap_2(base_settings):
    """No. 2 tests collection for ConceptMap.
    Test File: cm-medication-admin-status-v3.json
    """
    filename = base_settings["unittest_data_dir"] / "cm-medication-admin-status-v3.json"
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
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.group[0].element[0].code == "active"
    assert inst.group[0].element[0].target[0].code == "active"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "on-hold"
    assert inst.group[0].element[1].target[0].code == "suspended"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "cancelled"
    assert inst.group[0].element[2].target[0].code == "cancelled"
    assert inst.group[0].element[2].target[0].equivalence == "equal"
    assert inst.group[0].element[3].code == "completed"
    assert inst.group[0].element[3].target[0].code == "completed"
    assert inst.group[0].element[3].target[0].equivalence == "equal"
    assert inst.group[0].element[4].code == "entered-in-error"
    assert inst.group[0].element[4].target[0].code == "nullified"
    assert inst.group[0].element[4].target[0].equivalence == "equal"
    assert inst.group[0].element[5].code == "stopped"
    assert inst.group[0].element[5].target[0].code == "aborted"
    assert inst.group[0].element[5].target[0].equivalence == "equal"
    assert inst.group[0].element[6].code == "draft"
    assert inst.group[0].element[6].target[0].code == "new"
    assert inst.group[0].element[6].target[0].equivalence == "equal"
    assert inst.group[0].source == "http://hl7.org/fhir/medication-request-status"
    assert inst.group[0].target == "http://hl7.org/fhir/v3/ActStatus"
    assert inst.id == "cm-medication-request-status-v3"
    assert inst.name == "v3 map for MedicationRequestStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/medication-request-status"
    )
    assert inst.status == "draft"
    assert inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v3-ActStatus"
    assert inst.text.status == "generated"
    assert inst.url == (
        "http://hl7.org/fhir/ConceptMap/cm-medication-request-" "status-v3"
    )


def test_conceptmap_3(base_settings):
    """No. 3 tests collection for ConceptMap.
    Test File: cm-medication-request-status-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "cm-medication-request-status-v3.json"
    )
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
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.group[0].element[0].code == "has-member"
    assert inst.group[0].element[0].target[0].code == "MBR"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "derived-from"
    assert inst.group[0].element[1].target[0].code == "DRIV"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "sequel-to"
    assert inst.group[0].element[2].target[0].code == "SEQL"
    assert inst.group[0].element[2].target[0].equivalence == "equal"
    assert inst.group[0].element[3].code == "replaces"
    assert inst.group[0].element[3].target[0].code == "RPLC"
    assert inst.group[0].element[3].target[0].equivalence == "equal"
    assert inst.group[0].element[4].code == "qualified-by"
    assert inst.group[0].element[4].target[0].code == "QUALF"
    assert inst.group[0].element[4].target[0].equivalence == "equal"
    assert inst.group[0].element[5].code == "interfered-by"
    assert inst.group[0].element[5].target[0].code == "INTF"
    assert inst.group[0].element[5].target[0].equivalence == "equal"
    assert inst.group[0].source == "http://hl7.org/fhir/observation-relationshiptypes"
    assert inst.group[0].target == "http://hl7.org/fhir/v3/ActRelationshipType"
    assert inst.id == "cm-observation-relationshiptypes-v3"
    assert inst.name == "v3 map for ObservationRelationshipType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/observation-relationshiptypes"
    )
    assert inst.status == "draft"
    assert (
        inst.targetReference.reference
        == "http://hl7.org/fhir/ValueSet/v3-ActRelationshipType"
    )
    assert inst.text.status == "generated"
    assert inst.url == (
        "http://hl7.org/fhir/ConceptMap/cm-observation-" "relationshiptypes-v3"
    )


def test_conceptmap_4(base_settings):
    """No. 4 tests collection for ConceptMap.
    Test File: cm-observation-relationshiptypes-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "cm-observation-relationshiptypes-v3.json"
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
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.group[0].element[0].code == "preliminary"
    assert inst.group[0].element[0].target[0].code == "active"
    assert inst.group[0].element[0].target[0].equivalence == "equivalent"
    assert inst.group[0].element[1].code == "final"
    assert inst.group[0].element[1].target[0].code == "completed"
    assert inst.group[0].element[1].target[0].equivalence == "wider"
    assert inst.group[0].element[2].code == "amended"
    assert inst.group[0].element[2].target[0].code == "completed"
    assert inst.group[0].element[2].target[0].equivalence == "wider"
    assert inst.group[0].element[3].code == "entered-in-error"
    assert inst.group[0].element[3].target[0].code == "nullified"
    assert inst.group[0].element[3].target[0].equivalence == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/composition-status"
    assert inst.group[0].target == "http://hl7.org/fhir/v3/ActStatus"
    assert inst.id == "cm-composition-status-v3"
    assert inst.name == "v3 map for CompositionStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/composition-status"
    )
    assert inst.status == "draft"
    assert inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v3-ActStatus"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-composition-status-v3"


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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.group[0].element[0].code == "home"
    assert inst.group[0].element[0].target[0].code == "PRN"
    assert inst.group[0].element[0].target[0].equivalence == "wider"
    assert inst.group[0].element[0].target[1].code == "ORN"
    assert inst.group[0].element[0].target[1].equivalence == "wider"
    assert inst.group[0].element[0].target[2].code == "VHN"
    assert inst.group[0].element[0].target[2].equivalence == "wider"
    assert inst.group[0].element[1].code == "work"
    assert inst.group[0].element[1].target[0].code == "WPN"
    assert inst.group[0].element[1].target[0].equivalence == "equivalent"
    assert inst.group[0].element[2].code == "mobile"
    assert inst.group[0].element[2].target[0].code == "PRS"
    assert inst.group[0].element[2].target[0].equivalence == "equivalent"
    assert inst.group[0].source == "http://hl7.org/fhir/contact-point-use"
    assert inst.group[0].target == "http://hl7.org/fhir/v2/0201"
    assert inst.id == "cm-contact-point-use-v2"
    assert inst.name == "v2 map for ContactPointUse"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/contact-point-use"
    )
    assert inst.status == "draft"
    assert inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v2-0201"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v2"


def test_conceptmap_6(base_settings):
    """No. 6 tests collection for ConceptMap.
    Test File: cm-contact-point-use-v2.json
    """
    filename = base_settings["unittest_data_dir"] / "cm-contact-point-use-v2.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.group[0].element[0].code == "home"
    assert inst.group[0].element[0].target[0].code == "H"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "work"
    assert inst.group[0].element[1].target[0].code == "WP"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "temp"
    assert inst.group[0].element[2].target[0].code == "TMP"
    assert inst.group[0].element[2].target[0].equivalence == "equal"
    assert inst.group[0].element[3].code == "old"
    assert inst.group[0].element[3].target[0].code == "OLD"
    assert inst.group[0].element[3].target[0].comment == "Old and Bad"
    assert inst.group[0].element[3].target[0].equivalence == "narrower"
    assert inst.group[0].element[3].target[1].code == "BAD"
    assert inst.group[0].element[3].target[1].comment == "Old and Bad"
    assert inst.group[0].element[3].target[1].equivalence == "narrower"
    assert inst.group[0].element[4].code == "mobile"
    assert inst.group[0].element[4].target[0].code == "MC"
    assert inst.group[0].element[4].target[0].equivalence == "equal"
    assert inst.group[0].source == "http://hl7.org/fhir/contact-point-use"
    assert inst.group[0].target == "http://hl7.org/fhir/v3/AddressUse"
    assert inst.id == "cm-contact-point-use-v3"
    assert inst.name == "v3 map for ContactPointUse"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/contact-point-use"
    )
    assert inst.status == "draft"
    assert (
        inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v3-AddressUse"
    )
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v3"


def test_conceptmap_7(base_settings):
    """No. 7 tests collection for ConceptMap.
    Test File: cm-contact-point-use-v3.json
    """
    filename = base_settings["unittest_data_dir"] / "cm-contact-point-use-v3.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.group[0].element[0].code == "home"
    assert inst.group[0].element[0].target[0].code == "H"
    assert inst.group[0].element[0].target[0].equivalence == "equivalent"
    assert inst.group[0].element[1].code == "work"
    assert inst.group[0].element[1].target[0].code == "O"
    assert inst.group[0].element[1].target[0].equivalence == "equivalent"
    assert inst.group[0].element[2].code == "temp"
    assert inst.group[0].element[2].target[0].code == "C"
    assert inst.group[0].element[2].target[0].equivalence == "equivalent"
    assert inst.group[0].element[3].code == "old"
    assert inst.group[0].element[3].target[0].code == "BA"
    assert inst.group[0].element[3].target[0].comment == "unclear about old addresses"
    assert inst.group[0].element[3].target[0].equivalence == "wider"
    assert inst.group[0].source == "http://hl7.org/fhir/address-use"
    assert inst.group[0].target == "http://hl7.org/fhir/v2/0190"
    assert inst.id == "cm-address-use-v2"
    assert inst.name == "v2 map for AddressUse"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceReference.reference == "http://hl7.org/fhir/ValueSet/address-use"
    assert inst.status == "draft"
    assert inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v2-0190"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-address-use-v2"


def test_conceptmap_8(base_settings):
    """No. 8 tests collection for ConceptMap.
    Test File: cm-address-use-v2.json
    """
    filename = base_settings["unittest_data_dir"] / "cm-address-use-v2.json"
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
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.group[0].element[0].code == "high"
    assert inst.group[0].element[0].target[0].code == "H"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "moderate"
    assert inst.group[0].element[1].target[0].code == "M"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "low"
    assert inst.group[0].element[2].target[0].code == "L"
    assert inst.group[0].element[2].target[0].equivalence == "equal"
    assert inst.group[0].source == "http://hl7.org/fhir/detectedissue-severity"
    assert inst.group[0].target == "http://hl7.org/fhir/v3/ObservationValue"
    assert inst.id == "cm-detectedissue-severity-v3"
    assert inst.name == "v3 map for DetectedIssueSeverity"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/detectedissue-severity"
    )
    assert inst.status == "draft"
    assert (
        inst.targetReference.reference
        == "http://hl7.org/fhir/ValueSet/v3-SeverityObservation"
    )
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/cm-detectedissue-severity-v3"


def test_conceptmap_9(base_settings):
    """No. 9 tests collection for ConceptMap.
    Test File: cm-detectedissue-severity-v3.json
    """
    filename = base_settings["unittest_data_dir"] / "cm-detectedissue-severity-v3.json"
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
    assert inst.contact[0].name == "FHIR project team (example)"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.copyright == "Creative Commons 0"
    assert inst.date == fhirtypes.DateTime.validate("2012-06-13")
    assert inst.description == (
        "A mapping between the FHIR and HL7 v3 AddressUse Code " "systems"
    )
    assert inst.experimental is True
    assert inst.group[0].element[0].code == "home"
    assert inst.group[0].element[0].display == "home"
    assert inst.group[0].element[0].target[0].code == "H"
    assert inst.group[0].element[0].target[0].display == "home"
    assert inst.group[0].element[1].code == "work"
    assert inst.group[0].element[1].display == "work"
    assert inst.group[0].element[1].target[0].code == "WP"
    assert inst.group[0].element[1].target[0].display == "work place"
    assert inst.group[0].element[2].code == "temp"
    assert inst.group[0].element[2].display == "temp"
    assert inst.group[0].element[2].target[0].code == "TMP"
    assert inst.group[0].element[2].target[0].display == "temporary address"
    assert inst.group[0].element[3].code == "old"
    assert inst.group[0].element[3].display == "old"
    assert inst.group[0].element[3].target[0].code == "BAD"
    assert inst.group[0].element[3].target[0].comment == (
        "In the HL7 v3 AD, old is handled by the usablePeriod "
        "element, but you have to provide a time, there's no simple "
        "equivalent of flagging an address as old"
    )
    assert inst.group[0].element[3].target[0].display == "bad address"
    assert inst.group[0].element[3].target[0].equivalence == "disjoint"
    assert inst.group[0].source == "http://hl7.org/fhir/address-use"
    assert inst.group[0].target == "http://hl7.org/fhir/v3/AddressUse"
    assert inst.group[0].unmapped.code == "temp"
    assert inst.group[0].unmapped.display == "temp"
    assert inst.group[0].unmapped.mode == "fixed"
    assert inst.id == "101"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:uuid:53cd62ee-033e-414c-9f58-3ca97b5ffc3b"
    assert inst.name == "FHIR-v3-Address-Use"
    assert inst.publisher == "HL7, Inc"
    assert inst.purpose == "To help implementers map from HL7 v3/CDA to FHIR"
    assert inst.sourceUri == "http://hl7.org/fhir/ValueSet/address-use"
    assert inst.status == "draft"
    assert inst.targetUri == "http://hl7.org/fhir/ValueSet/v3-AddressUse"
    assert inst.text.status == "generated"
    assert inst.title == "FHIR/v3 Address Use Mapping"
    assert inst.url == "http://hl7.org/fhir/ConceptMap/101"
    assert inst.useContext[0].code.code == "venue"
    assert inst.useContext[0].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.text == "for CDA Usage"
    assert inst.version == "20120613"


def test_conceptmap_10(base_settings):
    """No. 10 tests collection for ConceptMap.
    Test File: conceptmap-example.json
    """
    filename = base_settings["unittest_data_dir"] / "conceptmap-example.json"
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
