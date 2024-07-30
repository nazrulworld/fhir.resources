# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from .. import conceptmap
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_conceptmap_1(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
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
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/medication-dispense-status"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/ActStatus"}
        ).valueUri
    )
    assert inst.id == "cm-medication-dispense-status-v3"
    assert inst.name == "v3 map for MedicationDispenseStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/medication-dispense-status"
    )
    assert inst.status == "draft"
    assert inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v3-ActStatus"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/ConceptMap/cm-medication-dispense-status-v3"
            }
        ).valueUri
    )


def test_conceptmap_1(base_settings):
    """No. 1 tests collection for ConceptMap.
    Test File: conceptmap-cm-medication-dispense-status-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "conceptmap-cm-medication-dispense-status-v3.json"
    )
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_1(inst2)


def impl_conceptmap_2(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
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
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/medication-request-status"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/ActStatus"}
        ).valueUri
    )
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
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/ConceptMap/cm-medication-request-status-v3"
            }
        ).valueUri
    )


def test_conceptmap_2(base_settings):
    """No. 2 tests collection for ConceptMap.
    Test File: conceptmap-cm-medication-request-status-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "conceptmap-cm-medication-request-status-v3.json"
    )
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_2(inst2)


def impl_conceptmap_3(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
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
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/medication-admin-status"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/ActStatus"}
        ).valueUri
    )
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
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ConceptMap/cm-medication-admin-status-v3"}
        ).valueUri
    )


def test_conceptmap_3(base_settings):
    """No. 3 tests collection for ConceptMap.
    Test File: conceptmap-cm-medication-admin-status-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "conceptmap-cm-medication-admin-status-v3.json"
    )
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_3(inst2)


def impl_conceptmap_4(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.group[0].element[0].code == "phone"
    assert inst.group[0].element[0].target[0].code == "PH"
    assert inst.group[0].element[0].target[0].equivalence == "equivalent"
    assert inst.group[0].element[1].code == "fax"
    assert inst.group[0].element[1].target[0].code == "FX"
    assert inst.group[0].element[1].target[0].equivalence == "equivalent"
    assert inst.group[0].element[2].code == "email"
    assert inst.group[0].element[2].target[0].code == "Internet"
    assert inst.group[0].element[2].target[0].comment == "for email addresses"
    assert inst.group[0].element[2].target[0].equivalence == "narrower"
    assert inst.group[0].element[3].code == "pager"
    assert inst.group[0].element[3].target[0].code == "BP"
    assert inst.group[0].element[3].target[0].equivalence == "equivalent"
    assert inst.group[0].element[4].code == "url"
    assert inst.group[0].element[4].target[0].code == "Internet"
    assert (
        inst.group[0].element[4].target[0].comment == "for non-email kinds of addresses"
    )
    assert inst.group[0].element[4].target[0].equivalence == "narrower"
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/contact-point-system"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v2/0202"}
        ).valueUri
    )
    assert inst.id == "cm-contact-point-system-v2"
    assert inst.name == "v2 map for ContactPointSystem"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/contact-point-system"
    )
    assert inst.status == "draft"
    assert inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v2-0202"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ConceptMap/cm-contact-point-system-v2"}
        ).valueUri
    )


def test_conceptmap_4(base_settings):
    """No. 4 tests collection for ConceptMap.
    Test File: conceptmap-cm-contact-point-system-v2.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "conceptmap-cm-contact-point-system-v2.json"
    )
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_4(inst2)


def impl_conceptmap_5(inst):
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.group[0].element[0].code == "unknown"
    assert inst.group[0].element[0].target[0].code == "UNK"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "asked"
    assert inst.group[0].element[1].target[0].code == "ASKU"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "temp"
    assert inst.group[0].element[2].target[0].code == "NAV"
    assert inst.group[0].element[2].target[0].equivalence == "equal"
    assert inst.group[0].element[3].code == "not-asked"
    assert inst.group[0].element[3].target[0].code == "NASK"
    assert inst.group[0].element[3].target[0].equivalence == "equal"
    assert inst.group[0].element[4].code == "masked"
    assert inst.group[0].element[4].target[0].code == "MSK"
    assert inst.group[0].element[4].target[0].equivalence == "equal"
    assert inst.group[0].element[5].code == "unsupported"
    assert inst.group[0].element[5].target[0].code == "NA"
    assert inst.group[0].element[5].target[0].equivalence == "wider"
    assert inst.group[0].element[6].code == "error"
    assert inst.group[0].element[6].target[0].code == "NA"
    assert inst.group[0].element[6].target[0].equivalence == "wider"
    assert inst.group[0].element[7].code == "NaN"
    assert inst.group[0].element[7].target[0].code == "NA"
    assert inst.group[0].element[7].target[0].equivalence == "wider"
    assert inst.group[0].element[8].code == "not-performed"
    assert inst.group[0].element[8].target[0].code == "NA"
    assert inst.group[0].element[8].target[0].equivalence == "wider"
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/data-absent-reason"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/NullFlavor"}
        ).valueUri
    )
    assert inst.id == "cm-data-absent-reason-v3"
    assert inst.name == "v3 map for DataAbsentReason"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/data-absent-reason"
    )
    assert inst.status == "draft"
    assert (
        inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v3-NullFlavor"
    )
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ConceptMap/cm-data-absent-reason-v3"}
        ).valueUri
    )


def test_conceptmap_5(base_settings):
    """No. 5 tests collection for ConceptMap.
    Test File: conceptmap-cm-data-absent-reason-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "conceptmap-cm-data-absent-reason-v3.json"
    )
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_5(inst2)


def impl_conceptmap_6(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
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
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/composition-status"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/ActStatus"}
        ).valueUri
    )
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
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ConceptMap/cm-composition-status-v3"}
        ).valueUri
    )


def test_conceptmap_6(base_settings):
    """No. 6 tests collection for ConceptMap.
    Test File: conceptmap-cm-composition-status-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "conceptmap-cm-composition-status-v3.json"
    )
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_6(inst2)


def impl_conceptmap_7(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.group[0].element[0].code == "high"
    assert inst.group[0].element[0].target[0].code == "H"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "moderate"
    assert inst.group[0].element[1].target[0].code == "M"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "low"
    assert inst.group[0].element[2].target[0].code == "L"
    assert inst.group[0].element[2].target[0].equivalence == "equal"
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/detectedissue-severity"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/ObservationValue"}
        ).valueUri
    )
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
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ConceptMap/cm-detectedissue-severity-v3"}
        ).valueUri
    )


def test_conceptmap_7(base_settings):
    """No. 7 tests collection for ConceptMap.
    Test File: conceptmap-cm-detectedissue-severity-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "conceptmap-cm-detectedissue-severity-v3.json"
    )
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_7(inst2)


def impl_conceptmap_8(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.group[0].element[0].code == "postal"
    assert inst.group[0].element[0].target[0].code == "PHYS"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "physical"
    assert inst.group[0].element[1].target[0].code == "PST"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/address-type"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/AddressUse"}
        ).valueUri
    )
    assert inst.id == "cm-address-type-v3"
    assert inst.name == "v3 map for AddressType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.sourceReference.reference == "http://hl7.org/fhir/ValueSet/address-type"
    assert inst.status == "draft"
    assert (
        inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v3-AddressUse"
    )
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ConceptMap/cm-address-type-v3"}
        ).valueUri
    )


def test_conceptmap_8(base_settings):
    """No. 8 tests collection for ConceptMap.
    Test File: conceptmap-cm-address-type-v3.json
    """
    filename = base_settings["unittest_data_dir"] / "conceptmap-cm-address-type-v3.json"
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_8(inst2)


def impl_conceptmap_9(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.group[0].element[0].code == "active"
    assert inst.group[0].element[0].target[0].code == "active"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "completed"
    assert inst.group[0].element[1].target[0].code == "completed"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "entered-in-error"
    assert inst.group[0].element[2].target[0].code == "nullified"
    assert inst.group[0].element[2].target[0].equivalence == "equal"
    assert inst.group[0].element[3].code == "stopped"
    assert inst.group[0].element[3].target[0].code == "aborted"
    assert inst.group[0].element[3].target[0].equivalence == "equal"
    assert inst.group[0].element[4].code == "on-hold"
    assert inst.group[0].element[4].target[0].code == "suspended"
    assert inst.group[0].element[4].target[0].equivalence == "equal"
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/medication-statement-status"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/ActStatus"}
        ).valueUri
    )
    assert inst.id == "cm-medication-statement-status-v3"
    assert inst.name == "v3 map for MedicationStatementStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/medication-statement-status"
    )
    assert inst.status == "draft"
    assert inst.targetReference.reference == "http://hl7.org/fhir/ValueSet/v3-ActStatus"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/ConceptMap/cm-medication-statement-status-v3"
            }
        ).valueUri
    )


def test_conceptmap_9(base_settings):
    """No. 9 tests collection for ConceptMap.
    Test File: conceptmap-cm-medication-statement-status-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "conceptmap-cm-medication-statement-status-v3.json"
    )
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_9(inst2)


def impl_conceptmap_10(inst):
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.group[0].element[0].code == "male"
    assert inst.group[0].element[0].target[0].code == "M"
    assert inst.group[0].element[0].target[0].equivalence == "equal"
    assert inst.group[0].element[1].code == "female"
    assert inst.group[0].element[1].target[0].code == "F"
    assert inst.group[0].element[1].target[0].equivalence == "equal"
    assert inst.group[0].element[2].code == "other"
    assert inst.group[0].element[2].target[0].code == "UN"
    assert inst.group[0].element[2].target[0].equivalence == "wider"
    assert inst.group[0].element[3].code == "unknown"
    assert inst.group[0].element[3].target[0].code == "UNK"
    assert inst.group[0].element[3].target[0].equivalence == "equal"
    assert (
        inst.group[0].source
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/administrative-gender"}
        ).valueUri
    )
    assert (
        inst.group[0].target
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/AdministrativeGender"}
        ).valueUri
    )
    assert inst.id == "cm-administrative-gender-v3"
    assert inst.name == "v3 map for AdministrativeGender"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert (
        inst.sourceReference.reference
        == "http://hl7.org/fhir/ValueSet/administrative-gender"
    )
    assert inst.status == "draft"
    assert (
        inst.targetReference.reference
        == "http://hl7.org/fhir/ValueSet/v3-AdministrativeGender"
    )
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ConceptMap/cm-administrative-gender-v3"}
        ).valueUri
    )


def test_conceptmap_10(base_settings):
    """No. 10 tests collection for ConceptMap.
    Test File: conceptmap-cm-administrative-gender-v3.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "conceptmap-cm-administrative-gender-v3.json"
    )
    inst = conceptmap.ConceptMap.model_validate_json(filename.read_bytes())
    assert "ConceptMap" == inst.get_resource_type()

    impl_conceptmap_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ConceptMap" == data["resourceType"]

    inst2 = conceptmap.ConceptMap(**data)
    impl_conceptmap_10(inst2)
