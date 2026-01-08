# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from .. import codesystem
from .conftest import ExternalValidatorModel


def impl_codesystem_1(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "proposal"
    assert inst.concept[0].definition == (
        "The request is a suggestion made by someone/something that "
        "doesn't have an intention to ensure it occurs and without "
        "providing an authorization to act"
    )
    assert inst.concept[0].display == "Proposal"
    assert inst.concept[1].code == "plan"
    assert inst.concept[1].definition == (
        "The request represents an intension to ensure something "
        "occurs without providing an authorization for others to act"
    )
    assert inst.concept[1].display == "Plan"
    assert inst.concept[2].code == "order"
    assert inst.concept[2].concept[0].code == "original-order"
    assert (
        inst.concept[2].concept[0].definition
        == "The request represents an original authorization for action"
    )
    assert inst.concept[2].concept[0].display == "Original Order"
    assert inst.concept[2].concept[1].code == "reflex-order"
    assert inst.concept[2].concept[1].display == "Reflex Order"
    assert inst.concept[2].concept[2].code == "filler-order"
    assert inst.concept[2].concept[2].concept[0].code == "instance-order"
    assert inst.concept[2].concept[2].concept[0].definition == (
        "An order created in fulfillment of a broader order that "
        "represents the authorization for a single activity "
        "occurrence.  E.g. The administration of a single dose of a "
        "drug."
    )
    assert inst.concept[2].concept[2].concept[0].display == "Instance Order"
    assert inst.concept[2].concept[2].definition == (
        "The request represents the view of an authorization "
        "instantiated by a fulfilling system representing the details"
        " of the fulfiller's intention to act upon a submitted order"
    )
    assert inst.concept[2].concept[2].display == "Filler Order"
    assert inst.concept[2].definition == (
        "The request represents a request/demand and authorization " "for action"
    )
    assert inst.concept[2].display == "Order"
    assert inst.concept[3].code == "option"
    assert inst.concept[3].display == "Option"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "Codes indicating the degree of authority/intentionality "
        "associated with a request"
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 3
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "oo"
    assert inst.id == "request-intent"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.105"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert inst.name == "RequestIntent"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/request-intent"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/request-intent"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_codesystem_1(base_settings):
    """No. 1 tests collection for CodeSystem.
    Test File: codesystem-codesystem-request-intent(request-intent).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-request-intent(request-intent).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_1(inst2)


def impl_codesystem_2(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "as"
    assert inst.concept[0].definition == "Child Asthma Program"
    assert inst.concept[0].display == "Child Asthma"
    assert inst.concept[1].code == "hd"
    assert inst.concept[1].definition == "Heamodialisis Program."
    assert inst.concept[1].display == "Heamodialisis"
    assert inst.concept[2].code == "auscr"
    assert inst.concept[2].definition == "Autism Screening Program."
    assert inst.concept[2].display == "Autism Screening"
    assert inst.concept[3].code == "none"
    assert inst.concept[3].definition == "No program code applies."
    assert inst.concept[3].display == "None"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.content == "complete"
    assert inst.copyright == "This is an example set."
    assert (
        inst.description == "This value set includes sample Program Reason Span codes."
    )
    assert inst.experimental is True
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[0].valueCode == "fm"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueString == "Draft"
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "ex-program-code"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.569"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"}
        ).valueUri
    )
    assert inst.name == "Example Program Reason Codes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ex-programcode"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/ex-program-code"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_codesystem_2(base_settings):
    """No. 2 tests collection for CodeSystem.
    Test File: codesystem-codesystem-ex-program-code(ex-program-code).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-ex-program-code(ex-program-code).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_2(inst2)


def impl_codesystem_3(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "nilknown"
    assert inst.concept[0].display == "Nil Known"
    assert inst.concept[1].code == "notasked"
    assert inst.concept[1].definition == (
        "The investigation to find out whether there are items for "
        "this list has not occurred."
    )
    assert inst.concept[1].display == "Not Asked"
    assert inst.concept[2].code == "withheld"
    assert inst.concept[2].display == "Information Withheld"
    assert inst.concept[3].code == "unavailable"
    assert inst.concept[3].definition == (
        "Information to populate this list cannot be obtained; e.g. "
        "unconscious patient."
    )
    assert inst.concept[3].display == "Unavailable"
    assert inst.concept[4].code == "notstarted"
    assert (
        inst.concept[4].definition
        == "The work to populate this list has not yet begun."
    )
    assert inst.concept[4].display == "Not Started"
    assert inst.concept[5].code == "closed"
    assert inst.concept[5].definition == (
        "This list has now closed or has ceased to be relevant or " "useful."
    )
    assert inst.concept[5].display == "Closed"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.content == "complete"
    assert inst.description == (
        "General reasons for a list to be empty. Reasons are either "
        "related to a summary list (i.e. problem or medication list) "
        "or to a workflow related list (i.e. consultation list)."
    )
    assert inst.experimental is True
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 2
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "sd"
    assert inst.id == "list-empty-reason"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.314"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"}
        ).valueUri
    )
    assert inst.name == "List Empty Reasons"
    assert inst.publisher == "FHIR Project"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/list-empty-reason"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/list-empty-reason"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_codesystem_3(base_settings):
    """No. 3 tests collection for CodeSystem.
    Test File: codesystem-codesystem-list-empty-reason(list-empty-reason).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-list-empty-reason(list-empty-reason).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_3(inst2)


def impl_codesystem_4(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "complete"
    assert inst.concept[0].definition == "The report is complete and ready for use"
    assert inst.concept[0].display == "Complete"
    assert inst.concept[1].code == "pending"
    assert inst.concept[1].definition == "The report is currently being generated"
    assert inst.concept[1].display == "Pending"
    assert inst.concept[2].code == "error"
    assert (
        inst.concept[2].definition
        == "An error occurred attempting to generate the report"
    )
    assert inst.concept[2].display == "Error"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == "The status of the measure report"
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 2
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "cqi"
    assert inst.id == "measure-report-status"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.760"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert inst.name == "MeasureReportStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/measure-report-status"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/measure-report-status"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_codesystem_4(base_settings):
    """No. 4 tests collection for CodeSystem.
    Test File: codesystem-codesystem-measure-report-status(measure-report-status).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-measure-report-status(measure-report-status).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_4(inst2)


def impl_codesystem_5(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "inactive"
    assert inst.concept[0].definition == (
        "True if the concept is not considered active - e.g. not a "
        "valid concept any more. Property type is boolean, default "
        "value is false"
    )
    assert inst.concept[0].display == "Inactive"
    assert inst.concept[1].code == "deprecated"
    assert inst.concept[1].display == "Deprecated"
    assert inst.concept[2].code == "notSelectable"
    assert inst.concept[2].display == "Not Selectable"
    assert inst.concept[3].code == "parent"
    assert inst.concept[3].definition == (
        "The concept identified in this property is a parent of the "
        "concept on which it is a property. The property type will be"
        " 'code'. The meaning of 'parent' is defined by the "
        "hierarchyMeaning attribute"
    )
    assert inst.concept[3].display == "Parent"
    assert inst.concept[4].code == "child"
    assert inst.concept[4].definition == (
        "The concept identified in this property is a child of the "
        "concept on which it is a property. The property type will be"
        " 'code'. The meaning of 'child' is defined by the "
        "hierarchyMeaning attribute"
    )
    assert inst.concept[4].display == "Child"
    assert inst.content == "complete"
    assert inst.description == (
        "A set of common concept properties for use on coded systems "
        "through out the FHIR eco-system."
    )
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 0
    assert inst.id == "concept-properties"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert inst.name == "FHIR Defined Concept Properties"
    assert inst.publisher == "FHIR Project"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/concept-properties"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/concept-properties"}
        ).valueUri
    )


def test_codesystem_5(base_settings):
    """No. 5 tests collection for CodeSystem.
    Test File: codesystem-codesystem-concept-properties(concept-properties).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-concept-properties(concept-properties).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_5(inst2)


def impl_codesystem_6(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "current"
    assert (
        inst.concept[0].definition == "This is the current reference for this document."
    )
    assert inst.concept[0].display == "Current"
    assert inst.concept[1].code == "superseded"
    assert (
        inst.concept[1].definition
        == "This reference has been superseded by another reference."
    )
    assert inst.concept[1].display == "Superseded"
    assert inst.concept[2].code == "entered-in-error"
    assert inst.concept[2].definition == "This reference was created in error."
    assert inst.concept[2].display == "Entered in Error"
    assert inst.content == "complete"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == "The status of the document reference."
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 3
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "sd"
    assert inst.id == "document-reference-status"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.8"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert inst.name == "DocumentReferenceStatus"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/document-reference-status"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/document-reference-status"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_codesystem_6(base_settings):
    """No. 6 tests collection for CodeSystem.
    Test File: codesystem-codesystem-document-reference-status(document-reference-status).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-document-reference-status(document-reference-status).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_6(inst2)


def impl_codesystem_7(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "ampoule"
    assert inst.concept[0].definition == "A sealed glass capsule containing a liquid"
    assert inst.concept[0].display == "Ampoule"
    assert inst.concept[1].code == "bottle"
    assert inst.concept[1].definition == (
        "A container, typically made of glass or plastic and with a "
        "narrow neck, used for storing liquids."
    )
    assert inst.concept[1].display == "Bottle"
    assert inst.concept[2].code == "box"
    assert inst.concept[2].definition == (
        "A container with a flat base and sides, typically square or "
        "rectangular and having a lid."
    )
    assert inst.concept[2].display == "Box"
    assert inst.concept[3].code == "cartridge"
    assert inst.concept[3].definition == (
        "A device of various configuration and composition used with "
        "a syringe for the application of anesthetic or other "
        "materials to a patient."
    )
    assert inst.concept[3].display == "Cartridge"
    assert inst.concept[4].code == "container"
    assert inst.concept[4].definition == "A package intended to store pharmaceuticals."
    assert inst.concept[4].display == "Container"
    assert inst.concept[5].code == "tube"
    assert inst.concept[5].definition == (
        "A long, hollow cylinder of metal, plastic, glass, etc., for "
        "holding medications, typically creams or ointments"
    )
    assert inst.concept[5].display == "Tube"
    assert inst.concept[6].code == "unitdose"
    assert inst.concept[6].definition == (
        "A dose of medicine prepared in an individual package for "
        "convenience, safety or monitoring."
    )
    assert inst.concept[6].display == "Unit Dose Blister"
    assert inst.concept[7].code == "vial"
    assert inst.concept[7].definition == (
        "A small container, typically cylindrical and made of glass, "
        "used especially for holding liquid medications."
    )
    assert inst.concept[7].display == "Vial"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "A coded concept defining the kind of container a medication "
        "package is packaged in"
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 1
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "phx"
    assert inst.id == "medication-package-form"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.362"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert inst.name == "MedicationContainer"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/medication-package-form"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/medication-package-form"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_codesystem_7(base_settings):
    """No. 7 tests collection for CodeSystem.
    Test File: codesystem-codesystem-medication-package-form(medication-package-form).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-medication-package-form(medication-package-form).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_7(inst2)


def impl_codesystem_8(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "unlikely"
    assert inst.concept[0].definition == (
        "There is a low level of clinical certainty that the reaction"
        " was caused by the identified substance."
    )
    assert inst.concept[0].display == "Unlikely"
    assert inst.concept[1].code == "likely"
    assert inst.concept[1].definition == (
        "There is a high level of clinical certainty that the "
        "reaction was caused by the identified substance."
    )
    assert inst.concept[1].display == "Likely"
    assert inst.concept[2].code == "confirmed"
    assert inst.concept[2].definition == (
        "There is a very high level of clinical certainty that the "
        "reaction was due to the identified substance, which may "
        "include clinical evidence by testing or rechallenge."
    )
    assert inst.concept[2].display == "Confirmed"
    assert inst.concept[3].code == "unknown"
    assert inst.concept[3].definition == (
        "The clinical certainty that the reaction was caused by the "
        "identified substance is unknown.  It is an explicit "
        "assertion that certainty is not known."
    )
    assert inst.concept[3].display == "Unknown"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "Statement about the degree of clinical certainty that a "
        "specific substance was the cause of the manifestation in a "
        "reaction event."
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 0
    assert inst.id == "reaction-event-certainty"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.860"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert inst.name == "AllergyIntoleranceCertainty"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/reaction-event-certainty"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/reaction-event-certainty"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_codesystem_8(base_settings):
    """No. 8 tests collection for CodeSystem.
    Test File: codesystem-codesystem-reaction-event-certainty(reaction-event-certainty).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-reaction-event-certainty(reaction-event-certainty).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_8(inst2)


def impl_codesystem_9(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "311405"
    assert inst.concept[0].definition == "Dentist General Practitioner (DDS, DDM)."
    assert inst.concept[0].display == "Dentist"
    assert inst.concept[1].code == "604215"
    assert inst.concept[1].definition == "Ophthalmologist."
    assert inst.concept[1].display == "Ophthalmologist"
    assert inst.concept[2].code == "604210"
    assert inst.concept[2].definition == "Optometrist."
    assert inst.concept[2].display == "Optometrist"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.content == "complete"
    assert inst.copyright == "This is an example set."
    assert (
        inst.description
        == "This value set includes sample Provider Qualification codes."
    )
    assert inst.experimental is True
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[0].valueCode == "fm"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueString == "Draft"
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "provider-qualification"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.563"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"}
        ).valueUri
    )
    assert inst.name == "Example Provider Qualification Codes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ex-providerqualification"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/provider-qualification"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_codesystem_9(base_settings):
    """No. 9 tests collection for CodeSystem.
    Test File: codesystem-codesystem-provider-qualification(provider-qualification).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-provider-qualification(provider-qualification).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_9(inst2)


def impl_codesystem_10(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "in-progress"
    assert inst.concept[0].definition == "Supply has been requested, but not delivered."
    assert inst.concept[0].display == "In Progress"
    assert inst.concept[1].code == "completed"
    assert inst.concept[1].definition == 'Supply has been delivered ("completed").'
    assert inst.concept[1].display == "Delivered"
    assert inst.concept[2].code == "abandoned"
    assert inst.concept[2].definition == "Delivery was not completed."
    assert inst.concept[2].display == "Abandoned"
    assert inst.concept[3].code == "entered-in-error"
    assert inst.concept[3].display == "Entered In Error"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == "Status of the supply delivery."
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 1
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "oo"
    assert inst.id == "supplydelivery-status"
    assert (
        inst.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.687"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert inst.name == "SupplyDeliveryStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/supplydelivery-status"}
        ).valueUri
    )
    assert (
        inst.valueSet
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/supplydelivery-status"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_codesystem_10(base_settings):
    """No. 10 tests collection for CodeSystem.
    Test File: codesystem-codesystem-supplydelivery-status(supplydelivery-status).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-supplydelivery-status(supplydelivery-status).json"
    )
    inst = codesystem.CodeSystem.model_validate_json(filename.read_bytes())
    assert "CodeSystem" == inst.get_resource_type()

    impl_codesystem_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_10(inst2)
