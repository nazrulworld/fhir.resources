# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import capabilitystatement


def impl_capabilitystatement_1(inst):
    assert inst.acceptUnknown == "both"
    assert inst.contact[0].name == "System Administrator"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "wile@acme.org"
    assert inst.date == fhirtypes.DateTime.validate("2012-01-04")
    assert inst.description == (
        "Sample capability statement showing new MessageDefinition " "structure"
    )
    assert inst.experimental is True
    assert inst.fhirVersion == "3.0.1"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "messagedefinition"
    assert inst.kind == "instance"
    assert (
        inst.messaging[0].documentation
        == "ADT A08 equivalent for external system notifications"
    )
    assert inst.messaging[0].endpoint[0].address == "mllp:10.1.1.10:9234"
    assert inst.messaging[0].endpoint[0].protocol.code == "mllp"
    assert (
        inst.messaging[0].endpoint[0].protocol.system
        == "http://hl7.org/fhir/message-transport"
    )
    assert inst.messaging[0].reliableCache == 30
    assert (
        inst.messaging[0].supportedMessage[0].definition.reference
        == "MessageDefinition/example"
    )
    assert inst.messaging[0].supportedMessage[0].mode == "receiver"
    assert inst.publisher == "ACME Corporation"
    assert inst.software.name == "EHR"
    assert inst.status == "draft"
    assert inst.text.status == "generated"


def test_capabilitystatement_1(base_settings):
    """No. 1 tests collection for CapabilityStatement.
    Test File: capabilitystatement-messagedefinition.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "capabilitystatement-messagedefinition.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_1(inst2)


def impl_capabilitystatement_2(inst):
    assert inst.acceptUnknown == "both"
    assert inst.contact[0].name == "System Administrator"
    assert inst.contact[0].telecom[0].system == "email"
    assert inst.contact[0].telecom[0].value == "wile@acme.org"
    assert inst.copyright == "Copyright © Acme Healthcare and GoodCorp EHR Systems"
    assert inst.date == fhirtypes.DateTime.validate("2012-01-04")
    assert inst.description == (
        "This is the FHIR capability statement for the main EHR at "
        "ACME for the private interface - it does not describe the "
        "public interface"
    )
    assert (
        inst.document[0].documentation
        == "Basic rules for all documents in the EHR system"
    )
    assert inst.document[0].mode == "consumer"
    assert inst.document[0].profile.reference == (
        "http://fhir.hl7.org/base/Profilebc054d23-75e1-4dc6-aca5-838b"
        "6b1ac81d/_history/b5fdd9fc-b021-4ea1-911a-721a60663796"
    )
    assert inst.experimental is True
    assert inst.fhirVersion == "1.0.0"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "example"
    assert inst.implementation.description == "main EHR at ACME"
    assert inst.implementation.url == "http://10.2.3.4/fhir"
    assert inst.implementationGuide[0] == "http://hl7.org/fhir/us/lab"
    assert inst.instantiates[0] == "http://ihe.org/fhir/CapabilityStatement/pixm-client"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].display == "United States of America (the)"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.kind == "instance"
    assert (
        inst.messaging[0].documentation
        == "ADT A08 equivalent for external system notifications"
    )
    assert inst.messaging[0].endpoint[0].address == "mllp:10.1.1.10:9234"
    assert inst.messaging[0].endpoint[0].protocol.code == "mllp"
    assert (
        inst.messaging[0].endpoint[0].protocol.system
        == "http://hl7.org/fhir/message-transport"
    )
    assert inst.messaging[0].event[0].category == "Consequence"
    assert inst.messaging[0].event[0].code.code == "admin-notify"
    assert (
        inst.messaging[0].event[0].code.system == "http://hl7.org/fhir/message-events"
    )
    assert inst.messaging[0].event[0].documentation == (
        "Notification of an update to a patient resource. changing "
        "the links is not supported"
    )
    assert inst.messaging[0].event[0].focus == "Patient"
    assert inst.messaging[0].event[0].mode == "receiver"
    assert inst.messaging[0].event[0].request.reference == "StructureDefinition/Patient"
    assert (
        inst.messaging[0].event[0].response.reference
        == "StructureDefinition/MessageHeader"
    )
    assert inst.messaging[0].reliableCache == 30
    assert inst.name == "ACME-EHR"
    assert inst.patchFormat[0] == "application/xml-patch+xml"
    assert inst.patchFormat[1] == "application/json-patch+json"
    assert inst.profile[0].reference == (
        "http://hl7.org/fhir/us/core/StructureDefinition/familymember" "history-genetic"
    )
    assert inst.publisher == "ACME Corporation"
    assert inst.purpose == (
        "Main EHR capability statement, published for contracting and"
        " operational support"
    )
    assert (
        inst.rest[0].compartment[0]
        == "http://hl7.org/fhir/CompartmentDefinition/patient"
    )
    assert inst.rest[0].documentation == "Main FHIR endpoint for acem health"
    assert inst.rest[0].interaction[0].code == "transaction"
    assert inst.rest[0].interaction[1].code == "history-system"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].resource[0].conditionalCreate is True
    assert inst.rest[0].resource[0].conditionalDelete == "not-supported"
    assert inst.rest[0].resource[0].conditionalRead == "full-support"
    assert inst.rest[0].resource[0].conditionalUpdate is False
    assert (
        inst.rest[0].resource[0].documentation
        == "This server does not let the clients create identities."
    )
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[1].code == "vread"
    assert (
        inst.rest[0].resource[0].interaction[1].documentation
        == "Only supported for patient records since 12-Dec 2012"
    )
    assert inst.rest[0].resource[0].interaction[2].code == "update"
    assert inst.rest[0].resource[0].interaction[3].code == "history-instance"
    assert inst.rest[0].resource[0].interaction[4].code == "create"
    assert inst.rest[0].resource[0].interaction[5].code == "history-type"
    assert inst.rest[0].resource[0].profile.reference == (
        "http://fhir.hl7.org/base/StructureDefinition/7896271d-57f6-4"
        "231-89dc-dcc91eab2416"
    )
    assert inst.rest[0].resource[0].readHistory is True
    assert inst.rest[0].resource[0].searchInclude[0] == "Organization"
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Patient-identifier"
    )
    assert (
        inst.rest[0].resource[0].searchParam[0].documentation
        == "Only supports search by institution MRN"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[0].type == "token"
    assert inst.rest[0].resource[0].searchParam[1].definition == (
        "http://hl7.org/fhir/SearchParameter/Patient-general-" "practitioner"
    )
    assert inst.rest[0].resource[0].searchParam[1].name == "general-practitioner"
    assert inst.rest[0].resource[0].searchParam[1].type == "reference"
    assert inst.rest[0].resource[0].searchRevInclude[0] == "Person"
    assert inst.rest[0].resource[0].type == "Patient"
    assert inst.rest[0].resource[0].updateCreate is False
    assert inst.rest[0].resource[0].versioning == "versioned-update"
    assert inst.rest[0].security.certificate[0].blob == bytes_validator(
        "IHRoaXMgYmxvYiBpcyBub3QgdmFsaWQ="
    )
    assert inst.rest[0].security.certificate[0].type == "application/jwt"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.description == "See Smart on FHIR documentation"
    assert inst.rest[0].security.service[0].coding[0].code == "SMART-on-FHIR"
    assert (
        inst.rest[0].security.service[0].coding[0].system
        == "http://hl7.org/fhir/restful-security-service"
    )
    assert inst.software.name == "EHR"
    assert inst.software.releaseDate == fhirtypes.DateTime.validate("2012-01-04")
    assert inst.software.version == "0.00.020.2134"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "ACME EHR capability statement"
    assert inst.url == "urn:uuid:68D043B5-9ECF-4559-A57A-396E0D452311"
    assert inst.useContext[0].code.code == "focus"
    assert inst.useContext[0].code.system == "http://hl7.org/fhir/usage-context-type"
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "positive"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/variant-state"
    )
    assert inst.version == "20130510"


def test_capabilitystatement_2(base_settings):
    """No. 2 tests collection for CapabilityStatement.
    Test File: capabilitystatement-example.json
    """
    filename = base_settings["unittest_data_dir"] / "capabilitystatement-example.json"
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_2(inst2)


def impl_capabilitystatement_3(inst):
    assert inst.acceptUnknown == "both"
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "other"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2016-09-16")
    assert inst.description == (
        "Basic conformance statement for a Measure Processor Service."
        " A server can support more functionality    than defined "
        "here, but this is the minimum amount"
    )
    assert inst.fhirVersion == "3.0.1"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "measure-processor"
    assert inst.kind == "capability"
    assert inst.name == "Measure Processor Service Conformance Statement"
    assert inst.publisher == "HL7, Inc"
    assert inst.rest[0].documentation == "RESTful Measure Processor Service"
    assert inst.rest[0].mode == "server"
    assert (
        inst.rest[0].operation[0].definition.reference
        == "OperationDefinition/Measure-evaluate-measure"
    )
    assert inst.rest[0].operation[0].name == "evaluate-measure"
    assert (
        inst.rest[0].operation[1].definition.reference
        == "OperationDefinition/Measure-data-requirements"
    )
    assert inst.rest[0].operation[1].name == "data-requirements"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "measures"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
        "Search allows clients to filter measures based on a provided"
        " search parameter"
    )
    assert inst.rest[0].resource[0].profile.reference == "StructureDefinition/Measure"
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-identifier"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-status"
    )
    assert inst.rest[0].resource[0].searchParam[1].name == "status"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-version"
    )
    assert inst.rest[0].resource[0].searchParam[2].name == "version"
    assert inst.rest[0].resource[0].searchParam[2].type == "string"
    assert inst.rest[0].resource[0].type == "Measure"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.service[0].coding[0].code == "Certificates"
    assert (
        inst.rest[0].security.service[0].coding[0].system
        == "http://hl7.org/fhir/restful-security-service"
    )
    assert inst.software.name == "ACME Measure Processor Service"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/measure-processor"


def test_capabilitystatement_3(base_settings):
    """No. 3 tests collection for CapabilityStatement.
    Test File: capabilitystatement-measure-processor.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "capabilitystatement-measure-processor.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_3(inst2)


def impl_capabilitystatement_4(inst):
    assert inst.acceptUnknown == "both"
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2015-07-05")
    assert inst.description == (
        "Basic capability statement for a Terminology Server. A "
        "server can support more fucntionality than defined here, but"
        " this is the minimum amount"
    )
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/capabilitystatement-"
        "supported-system"
    )
    assert inst.extension[0].valueUri == "http://loinc.org"
    assert inst.fhirVersion == "3.0.1"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "terminology-server"
    assert inst.kind == "capability"
    assert inst.name == "Terminology Service Capability Statement"
    assert inst.publisher == "HL7, Inc"
    assert inst.rest[0].documentation == "RESTful Terminology Server"
    assert inst.rest[0].mode == "server"
    assert (
        inst.rest[0].operation[0].definition.reference
        == "OperationDefinition/ValueSet-expand"
    )
    assert inst.rest[0].operation[0].name == "expand"
    assert (
        inst.rest[0].operation[1].definition.reference
        == "OperationDefinition/CodeSystem-lookup"
    )
    assert inst.rest[0].operation[1].name == "lookup"
    assert (
        inst.rest[0].operation[2].definition.reference
        == "OperationDefinition/ValueSet-validate-code"
    )
    assert inst.rest[0].operation[2].name == "validate-code"
    assert (
        inst.rest[0].operation[3].definition.reference
        == "OperationDefinition/ConceptMap-translate"
    )
    assert inst.rest[0].operation[3].name == "translate"
    assert (
        inst.rest[0].operation[4].definition.reference
        == "OperationDefinition/ConceptMap-closure"
    )
    assert inst.rest[0].operation[4].name == "closure"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "value sets"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert (
        inst.rest[0].resource[0].interaction[1].documentation
        == "Search allows clients to find value sets on the server"
    )
    assert inst.rest[0].resource[0].profile.reference == "StructureDefinition/ValueSet"
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-date"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "date"
    assert inst.rest[0].resource[0].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[0].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-name"
    )
    assert inst.rest[0].resource[0].searchParam[1].name == "name"
    assert inst.rest[0].resource[0].searchParam[1].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-reference"
    )
    assert inst.rest[0].resource[0].searchParam[2].name == "reference"
    assert inst.rest[0].resource[0].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-status"
    )
    assert inst.rest[0].resource[0].searchParam[3].name == "status"
    assert inst.rest[0].resource[0].searchParam[3].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-url"
    )
    assert inst.rest[0].resource[0].searchParam[4].name == "url"
    assert inst.rest[0].resource[0].searchParam[4].type == "uri"
    assert (
        inst.rest[0].resource[0].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/ValueSet-version"
    )
    assert inst.rest[0].resource[0].searchParam[5].name == "version"
    assert inst.rest[0].resource[0].searchParam[5].type == "token"
    assert inst.rest[0].resource[0].type == "ValueSet"
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "concept maps"
    )
    assert inst.rest[0].resource[1].interaction[1].code == "search-type"
    assert (
        inst.rest[0].resource[1].interaction[1].documentation
        == "Search allows clients to find concept maps on the server"
    )
    assert (
        inst.rest[0].resource[1].profile.reference == "StructureDefinition/ConceptMap"
    )
    assert (
        inst.rest[0].resource[1].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-date"
    )
    assert inst.rest[0].resource[1].searchParam[0].name == "date"
    assert inst.rest[0].resource[1].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[1].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-name"
    )
    assert inst.rest[0].resource[1].searchParam[1].name == "name"
    assert inst.rest[0].resource[1].searchParam[1].type == "string"
    assert (
        inst.rest[0].resource[1].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-status"
    )
    assert inst.rest[0].resource[1].searchParam[2].name == "status"
    assert inst.rest[0].resource[1].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-source"
    )
    assert inst.rest[0].resource[1].searchParam[3].name == "source"
    assert inst.rest[0].resource[1].searchParam[3].type == "uri"
    assert (
        inst.rest[0].resource[1].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-target"
    )
    assert inst.rest[0].resource[1].searchParam[4].name == "target"
    assert inst.rest[0].resource[1].searchParam[4].type == "uri"
    assert (
        inst.rest[0].resource[1].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-url"
    )
    assert inst.rest[0].resource[1].searchParam[5].name == "url"
    assert inst.rest[0].resource[1].searchParam[5].type == "uri"
    assert (
        inst.rest[0].resource[1].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/ConceptMap-version"
    )
    assert inst.rest[0].resource[1].searchParam[6].name == "version"
    assert inst.rest[0].resource[1].searchParam[6].type == "token"
    assert inst.rest[0].resource[1].type == "ConceptMap"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.service[0].coding[0].code == "Certificates"
    assert (
        inst.rest[0].security.service[0].coding[0].system
        == "http://hl7.org/fhir/restful-security-service"
    )
    assert inst.software.name == "ACME Terminology Server"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/terminology-server"


def test_capabilitystatement_4(base_settings):
    """No. 4 tests collection for CapabilityStatement.
    Test File: capabilitystatement-terminology-server.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "capabilitystatement-terminology-server.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_4(inst2)


def impl_capabilitystatement_5(inst):
    assert inst.acceptUnknown == "no"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.experimental is True
    assert inst.fhirVersion == "3.0.1"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "base2"
    assert inst.kind == "capability"
    assert inst.name == "Base FHIR Capability Statement (Empty)"
    assert inst.publisher == "FHIR Project Team"
    assert inst.rest[0].documentation == "An empty Capability Statement"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert (
        inst.rest[0].resource[0].interaction[0].documentation
        == "Read CapabilityStatement Resource"
    )
    assert inst.rest[0].resource[0].type == "CapabilityStatement"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.description == (
        "This is the Capability Statement to declare that the server "
        "supports SMART-on-FHIR. See the SMART-on-FHIR docs for the "
        "extension that would go with such a server"
    )
    assert inst.rest[0].security.service[0].coding[0].code == "SMART-on-FHIR"
    assert inst.rest[0].security.service[0].coding[0].display == "SMART-on-FHIR"
    assert (
        inst.rest[0].security.service[0].coding[0].system
        == "http://hl7.org/fhir/restful-security-service"
    )
    assert inst.rest[0].security.service[0].text == "See http://docs.smarthealthit.org/"
    assert inst.software.name == "Insert your softwware name here..."
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/CapabilityStatement/base2"
    assert inst.version == "3.0.1-11917"


def test_capabilitystatement_5(base_settings):
    """No. 5 tests collection for CapabilityStatement.
    Test File: capabilitystatement-base2.json
    """
    filename = base_settings["unittest_data_dir"] / "capabilitystatement-base2.json"
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_5(inst2)


def impl_capabilitystatement_6(inst):
    assert inst.acceptUnknown == "no"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2013-06-18")
    assert inst.description == (
        "Prototype Capability Statement for September 2013 " "Connectathon"
    )
    assert inst.fhirVersion == "1.0.0"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "phr"
    assert inst.kind == "capability"
    assert inst.name == "PHR Template"
    assert inst.publisher == "FHIR Project"
    assert inst.rest[0].documentation == (
        "Protoype server Capability Statement for September 2013 " "Connectathon"
    )
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
        "When a client searches patients with no search criteria, "
        "they get a list of all patients they have access too. "
        "Servers may elect to offer additional search parameters, but"
        " this is not required"
    )
    assert inst.rest[0].resource[0].type == "Patient"
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[1].code == "search-type"
    assert inst.rest[0].resource[1].searchParam[0].documentation == (
        "_id parameter always supported. For the connectathon, "
        "servers may elect which search parameters are supported"
    )
    assert inst.rest[0].resource[1].searchParam[0].name == "_id"
    assert inst.rest[0].resource[1].searchParam[0].type == "token"
    assert inst.rest[0].resource[1].type == "DocumentReference"
    assert inst.rest[0].resource[2].interaction[0].code == "read"
    assert inst.rest[0].resource[2].interaction[1].code == "search-type"
    assert (
        inst.rest[0].resource[2].searchParam[0].documentation
        == "Standard _id parameter"
    )
    assert inst.rest[0].resource[2].searchParam[0].name == "_id"
    assert inst.rest[0].resource[2].searchParam[0].type == "token"
    assert inst.rest[0].resource[2].type == "Condition"
    assert inst.rest[0].resource[3].interaction[0].code == "read"
    assert inst.rest[0].resource[3].interaction[1].code == "search-type"
    assert (
        inst.rest[0].resource[3].searchParam[0].documentation
        == "Standard _id parameter"
    )
    assert inst.rest[0].resource[3].searchParam[0].name == "_id"
    assert inst.rest[0].resource[3].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[1].documentation
        == "which diagnostic discipline/department created the report"
    )
    assert inst.rest[0].resource[3].searchParam[1].name == "service"
    assert inst.rest[0].resource[3].searchParam[1].type == "token"
    assert inst.rest[0].resource[3].type == "DiagnosticReport"
    assert inst.rest[0].security.service[0].text == "OAuth"
    assert inst.software.name == "ACME PHR Server"
    assert inst.status == "draft"
    assert inst.text.status == "generated"


def test_capabilitystatement_6(base_settings):
    """No. 6 tests collection for CapabilityStatement.
    Test File: capabilitystatement-phr-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "capabilitystatement-phr-example.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_6(inst2)


def impl_capabilitystatement_7(inst):
    assert inst.acceptUnknown == "both"
    assert inst.contact[0].name == "FHIR Project"
    assert inst.contact[0].telecom[0].system == "other"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2017-02-25")
    assert inst.description == (
        "Basic conformance statement for a Knowledge Repository "
        "Service. A server can support more functionality    than "
        "defined here, but this is the minimum amount"
    )
    assert inst.fhirVersion == "3.0.1"
    assert inst.format[0] == "json"
    assert inst.format[1] == "xml"
    assert inst.id == "knowledge-repository"
    assert inst.kind == "capability"
    assert inst.name == "Knowledge Repository Service Conformance Statement"
    assert inst.publisher == "HL7, Inc"
    assert inst.rest[0].documentation == "RESTful Knowledge Repository Service"
    assert inst.rest[0].mode == "server"
    assert (
        inst.rest[0].operation[0].definition.reference
        == "OperationDefinition/Library-data-requirements"
    )
    assert inst.rest[0].operation[0].name == "data-requirements"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "libraries"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "search-type"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
        "Search allows clients to filter libraries based on a "
        "provided search parameter"
    )
    assert inst.rest[0].resource[0].profile.reference == "StructureDefinition/Library"
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Library-description"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "description"
    assert inst.rest[0].resource[0].searchParam[0].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Library-identifier"
    )
    assert inst.rest[0].resource[0].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Library-status"
    )
    assert inst.rest[0].resource[0].searchParam[2].name == "status"
    assert inst.rest[0].resource[0].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Library-title"
    )
    assert inst.rest[0].resource[0].searchParam[3].name == "title"
    assert inst.rest[0].resource[0].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/Library-topic"
    )
    assert inst.rest[0].resource[0].searchParam[4].name == "topic"
    assert inst.rest[0].resource[0].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Library-version"
    )
    assert inst.rest[0].resource[0].searchParam[5].name == "version"
    assert inst.rest[0].resource[0].searchParam[5].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/Library-composed-of"
    )
    assert inst.rest[0].resource[0].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[0].searchParam[6].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/Library-depends-on"
    )
    assert inst.rest[0].resource[0].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[0].searchParam[7].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[8].definition
        == "http://hl7.org/fhir/SearchParameter/Library-derived-from"
    )
    assert inst.rest[0].resource[0].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[0].searchParam[8].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[9].definition
        == "http://hl7.org/fhir/SearchParameter/Library-predecessor"
    )
    assert inst.rest[0].resource[0].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[0].searchParam[9].type == "reference"
    assert inst.rest[0].resource[0].type == "Library"
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "plan definitions"
    )
    assert inst.rest[0].resource[1].interaction[1].code == "search-type"
    assert inst.rest[0].resource[1].interaction[1].documentation == (
        "Search allows clients to filter plan definitions based on a "
        "provided search parameter"
    )
    assert (
        inst.rest[0].resource[1].profile.reference
        == "StructureDefinition/PlanDefinition"
    )
    assert inst.rest[0].resource[1].searchParam[0].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-" "description"
    )
    assert inst.rest[0].resource[1].searchParam[0].name == "description"
    assert inst.rest[0].resource[1].searchParam[0].type == "string"
    assert inst.rest[0].resource[1].searchParam[1].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-" "identifier"
    )
    assert inst.rest[0].resource[1].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[1].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/PlanDefinition-status"
    )
    assert inst.rest[0].resource[1].searchParam[2].name == "status"
    assert inst.rest[0].resource[1].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/PlanDefinition-title"
    )
    assert inst.rest[0].resource[1].searchParam[3].name == "title"
    assert inst.rest[0].resource[1].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[1].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/PlanDefinition-topic"
    )
    assert inst.rest[0].resource[1].searchParam[4].name == "topic"
    assert inst.rest[0].resource[1].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/PlanDefinition-version"
    )
    assert inst.rest[0].resource[1].searchParam[5].name == "version"
    assert inst.rest[0].resource[1].searchParam[5].type == "string"
    assert inst.rest[0].resource[1].searchParam[6].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-composed-" "of"
    )
    assert inst.rest[0].resource[1].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[1].searchParam[6].type == "reference"
    assert inst.rest[0].resource[1].searchParam[7].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-depends-" "on"
    )
    assert inst.rest[0].resource[1].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[1].searchParam[7].type == "reference"
    assert inst.rest[0].resource[1].searchParam[8].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-derived-" "from"
    )
    assert inst.rest[0].resource[1].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[1].searchParam[8].type == "reference"
    assert inst.rest[0].resource[1].searchParam[9].definition == (
        "http://hl7.org/fhir/SearchParameter/PlanDefinition-" "predecessor"
    )
    assert inst.rest[0].resource[1].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[1].searchParam[9].type == "reference"
    assert inst.rest[0].resource[1].type == "PlanDefinition"
    assert inst.rest[0].resource[2].interaction[0].code == "read"
    assert inst.rest[0].resource[2].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the "
        "activity definitions"
    )
    assert inst.rest[0].resource[2].interaction[1].code == "search-type"
    assert inst.rest[0].resource[2].interaction[1].documentation == (
        "Search allows clients to filter activity definitions based "
        "on a provided search parameter"
    )
    assert (
        inst.rest[0].resource[2].profile.reference
        == "StructureDefinition/ActivityDefinition"
    )
    assert inst.rest[0].resource[2].searchParam[0].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "description"
    )
    assert inst.rest[0].resource[2].searchParam[0].name == "description"
    assert inst.rest[0].resource[2].searchParam[0].type == "string"
    assert inst.rest[0].resource[2].searchParam[1].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "identifier"
    )
    assert inst.rest[0].resource[2].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[2].searchParam[1].type == "token"
    assert inst.rest[0].resource[2].searchParam[2].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "status"
    )
    assert inst.rest[0].resource[2].searchParam[2].name == "status"
    assert inst.rest[0].resource[2].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[2].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/ActivityDefinition-title"
    )
    assert inst.rest[0].resource[2].searchParam[3].name == "title"
    assert inst.rest[0].resource[2].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[2].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/ActivityDefinition-topic"
    )
    assert inst.rest[0].resource[2].searchParam[4].name == "topic"
    assert inst.rest[0].resource[2].searchParam[4].type == "token"
    assert inst.rest[0].resource[2].searchParam[5].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "version"
    )
    assert inst.rest[0].resource[2].searchParam[5].name == "version"
    assert inst.rest[0].resource[2].searchParam[5].type == "string"
    assert inst.rest[0].resource[2].searchParam[6].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "composed-of"
    )
    assert inst.rest[0].resource[2].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[2].searchParam[6].type == "reference"
    assert inst.rest[0].resource[2].searchParam[7].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "depends-on"
    )
    assert inst.rest[0].resource[2].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[2].searchParam[7].type == "reference"
    assert inst.rest[0].resource[2].searchParam[8].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "derived-from"
    )
    assert inst.rest[0].resource[2].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[2].searchParam[8].type == "reference"
    assert inst.rest[0].resource[2].searchParam[9].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "predecessor"
    )
    assert inst.rest[0].resource[2].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[2].searchParam[9].type == "reference"
    assert inst.rest[0].resource[2].type == "ActivityDefinition"
    assert inst.rest[0].resource[3].interaction[0].code == "read"
    assert inst.rest[0].resource[3].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "measures"
    )
    assert inst.rest[0].resource[3].interaction[1].code == "search-type"
    assert inst.rest[0].resource[3].interaction[1].documentation == (
        "Search allows clients to filter measures based on a provided"
        " search parameter"
    )
    assert inst.rest[0].resource[3].profile.reference == "StructureDefinition/Measure"
    assert (
        inst.rest[0].resource[3].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-description"
    )
    assert inst.rest[0].resource[3].searchParam[0].name == "description"
    assert inst.rest[0].resource[3].searchParam[0].type == "string"
    assert (
        inst.rest[0].resource[3].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-identifier"
    )
    assert inst.rest[0].resource[3].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[3].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-status"
    )
    assert inst.rest[0].resource[3].searchParam[2].name == "status"
    assert inst.rest[0].resource[3].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-title"
    )
    assert inst.rest[0].resource[3].searchParam[3].name == "title"
    assert inst.rest[0].resource[3].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[3].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-topic"
    )
    assert inst.rest[0].resource[3].searchParam[4].name == "topic"
    assert inst.rest[0].resource[3].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-version"
    )
    assert inst.rest[0].resource[3].searchParam[5].name == "version"
    assert inst.rest[0].resource[3].searchParam[5].type == "string"
    assert (
        inst.rest[0].resource[3].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-composed-of"
    )
    assert inst.rest[0].resource[3].searchParam[6].name == "composed-of"
    assert inst.rest[0].resource[3].searchParam[6].type == "reference"
    assert (
        inst.rest[0].resource[3].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-depends-on"
    )
    assert inst.rest[0].resource[3].searchParam[7].name == "depends-on"
    assert inst.rest[0].resource[3].searchParam[7].type == "reference"
    assert (
        inst.rest[0].resource[3].searchParam[8].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-derived-from"
    )
    assert inst.rest[0].resource[3].searchParam[8].name == "derived-from"
    assert inst.rest[0].resource[3].searchParam[8].type == "reference"
    assert (
        inst.rest[0].resource[3].searchParam[9].definition
        == "http://hl7.org/fhir/SearchParameter/Measure-predecessor"
    )
    assert inst.rest[0].resource[3].searchParam[9].name == "predecessor"
    assert inst.rest[0].resource[3].searchParam[9].type == "reference"
    assert inst.rest[0].resource[3].type == "Measure"
    assert inst.rest[0].resource[4].interaction[0].code == "read"
    assert inst.rest[0].resource[4].interaction[0].documentation == (
        "Read allows clients to get the logical definitions of the " "measures"
    )
    assert inst.rest[0].resource[4].interaction[1].code == "search-type"
    assert inst.rest[0].resource[4].interaction[1].documentation == (
        "Search allows clients to filter measures based on a provided"
        " search parameter"
    )
    assert (
        inst.rest[0].resource[4].profile.reference
        == "StructureDefinition/Questionnaire"
    )
    assert (
        inst.rest[0].resource[4].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-code"
    )
    assert inst.rest[0].resource[4].searchParam[0].name == "code"
    assert inst.rest[0].resource[4].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-context"
    )
    assert inst.rest[0].resource[4].searchParam[1].name == "context"
    assert inst.rest[0].resource[4].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-date"
    )
    assert inst.rest[0].resource[4].searchParam[2].name == "date"
    assert inst.rest[0].resource[4].searchParam[2].type == "date"
    assert (
        inst.rest[0].resource[4].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-identifier"
    )
    assert inst.rest[0].resource[4].searchParam[3].name == "identifier"
    assert inst.rest[0].resource[4].searchParam[3].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-publisher"
    )
    assert inst.rest[0].resource[4].searchParam[4].name == "publisher"
    assert inst.rest[0].resource[4].searchParam[4].type == "string"
    assert (
        inst.rest[0].resource[4].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-status"
    )
    assert inst.rest[0].resource[4].searchParam[5].name == "status"
    assert inst.rest[0].resource[4].searchParam[5].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-title"
    )
    assert inst.rest[0].resource[4].searchParam[6].name == "title"
    assert inst.rest[0].resource[4].searchParam[6].type == "string"
    assert (
        inst.rest[0].resource[4].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/Questionnaire-version"
    )
    assert inst.rest[0].resource[4].searchParam[7].name == "version"
    assert inst.rest[0].resource[4].searchParam[7].type == "string"
    assert inst.rest[0].resource[4].type == "Questionnaire"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.service[0].coding[0].code == "Certificates"
    assert (
        inst.rest[0].security.service[0].coding[0].system
        == "http://hl7.org/fhir/restful-security-service"
    )
    assert inst.software.name == "ACME Knowledge Repository Service"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/knowledge-repository"


def test_capabilitystatement_7(base_settings):
    """No. 7 tests collection for CapabilityStatement.
    Test File: capabilitystatement-knowledge-repository.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "capabilitystatement-knowledge-repository.json"
    )
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_7(inst2)


def impl_capabilitystatement_8(inst):
    assert inst.acceptUnknown == "both"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.experimental is True
    assert inst.fhirVersion == "3.0.1"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "base"
    assert inst.kind == "capability"
    assert inst.name == "Base FHIR Capability Statement (Full)"
    assert inst.publisher == "FHIR Project Team"
    assert inst.rest[0].documentation == "All the functionality defined in FHIR"
    assert inst.rest[0].interaction[0].code == "transaction"
    assert inst.rest[0].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].interaction[1].code == "batch"
    assert inst.rest[0].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].interaction[2].code == "history-system"
    assert inst.rest[0].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].interaction[3].code == "search-system"
    assert inst.rest[0].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].mode == "server"
    assert (
        inst.rest[0].operation[0].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/resource-validate"
    )
    assert inst.rest[0].operation[0].name == "validate"
    assert (
        inst.rest[0].operation[1].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/resource-meta"
    )
    assert inst.rest[0].operation[1].name == "meta"
    assert (
        inst.rest[0].operation[2].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/resource-meta-add"
    )
    assert inst.rest[0].operation[2].name == "meta-add"
    assert (
        inst.rest[0].operation[3].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/resource-meta-delete"
    )
    assert inst.rest[0].operation[3].name == "meta-delete"
    assert inst.rest[0].operation[4].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/activitydefinition-" "apply"
    )
    assert inst.rest[0].operation[4].name == "apply"
    assert inst.rest[0].operation[5].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/activitydefinition-"
        "data-requirements"
    )
    assert inst.rest[0].operation[5].name == "data-requirements"
    assert inst.rest[0].operation[6].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/capabilitystatement-" "subset"
    )
    assert inst.rest[0].operation[6].name == "subset"
    assert inst.rest[0].operation[7].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/capabilitystatement-" "implements"
    )
    assert inst.rest[0].operation[7].name == "implements"
    assert inst.rest[0].operation[8].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/capabilitystatement-" "conforms"
    )
    assert inst.rest[0].operation[8].name == "conforms"
    assert (
        inst.rest[0].operation[9].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/codesystem-lookup"
    )
    assert inst.rest[0].operation[9].name == "lookup"
    assert inst.rest[0].resource[0].conditionalCreate is True
    assert inst.rest[0].resource[0].conditionalDelete == "multiple"
    assert inst.rest[0].resource[0].conditionalUpdate is True
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "vread"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[2].code == "update"
    assert inst.rest[0].resource[0].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[3].code == "delete"
    assert inst.rest[0].resource[0].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[0].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[5].code == "history-type"
    assert inst.rest[0].resource[0].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[6].code == "create"
    assert inst.rest[0].resource[0].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[7].code == "search-type"
    assert inst.rest[0].resource[0].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[0].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Account"
    )
    assert inst.rest[0].resource[0].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[0].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[0].searchInclude[0] == "Account.owner"
    assert inst.rest[0].resource[0].searchInclude[1] == "Account.subject"
    assert inst.rest[0].resource[0].searchInclude[2] == "Account.patient"
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Account-owner"
    )
    assert (
        inst.rest[0].resource[0].searchParam[0].documentation == "Who is responsible?"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "owner"
    assert inst.rest[0].resource[0].searchParam[0].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Account-identifier"
    )
    assert inst.rest[0].resource[0].searchParam[1].documentation == "Account number"
    assert inst.rest[0].resource[0].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Account-period"
    )
    assert inst.rest[0].resource[0].searchParam[2].documentation == "Transaction window"
    assert inst.rest[0].resource[0].searchParam[2].name == "period"
    assert inst.rest[0].resource[0].searchParam[2].type == "date"
    assert (
        inst.rest[0].resource[0].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Account-balance"
    )
    assert (
        inst.rest[0].resource[0].searchParam[3].documentation
        == "How much is in account?"
    )
    assert inst.rest[0].resource[0].searchParam[3].name == "balance"
    assert inst.rest[0].resource[0].searchParam[3].type == "quantity"
    assert (
        inst.rest[0].resource[0].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/Account-subject"
    )
    assert (
        inst.rest[0].resource[0].searchParam[4].documentation
        == "What is account tied to?"
    )
    assert inst.rest[0].resource[0].searchParam[4].name == "subject"
    assert inst.rest[0].resource[0].searchParam[4].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Account-patient"
    )
    assert (
        inst.rest[0].resource[0].searchParam[5].documentation
        == "What is account tied to?"
    )
    assert inst.rest[0].resource[0].searchParam[5].name == "patient"
    assert inst.rest[0].resource[0].searchParam[5].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/Account-name"
    )
    assert (
        inst.rest[0].resource[0].searchParam[6].documentation == "Human-readable label"
    )
    assert inst.rest[0].resource[0].searchParam[6].name == "name"
    assert inst.rest[0].resource[0].searchParam[6].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/Account-type"
    )
    assert (
        inst.rest[0].resource[0].searchParam[7].documentation
        == "E.g. patient, expense, depreciation"
    )
    assert inst.rest[0].resource[0].searchParam[7].name == "type"
    assert inst.rest[0].resource[0].searchParam[7].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[8].definition
        == "http://hl7.org/fhir/SearchParameter/Account-status"
    )
    assert (
        inst.rest[0].resource[0].searchParam[8].documentation
        == "active | inactive | entered-in-error"
    )
    assert inst.rest[0].resource[0].searchParam[8].name == "status"
    assert inst.rest[0].resource[0].searchParam[8].type == "token"
    assert inst.rest[0].resource[0].searchRevInclude[0] == "ChargeItem.account"
    assert inst.rest[0].resource[0].type == "Account"
    assert inst.rest[0].resource[1].conditionalCreate is True
    assert inst.rest[0].resource[1].conditionalDelete == "multiple"
    assert inst.rest[0].resource[1].conditionalUpdate is True
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[1].code == "vread"
    assert inst.rest[0].resource[1].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[2].code == "update"
    assert inst.rest[0].resource[1].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[3].code == "delete"
    assert inst.rest[0].resource[1].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[1].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[5].code == "history-type"
    assert inst.rest[0].resource[1].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[6].code == "create"
    assert inst.rest[0].resource[1].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[7].code == "search-type"
    assert inst.rest[0].resource[1].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[1].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/ActivityDefinition"
    )
    assert inst.rest[0].resource[1].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[1].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[1].searchInclude[0] == "ActivityDefinition.successor"
    assert (
        inst.rest[0].resource[1].searchInclude[1] == "ActivityDefinition.derived-from"
    )
    assert inst.rest[0].resource[1].searchInclude[2] == "ActivityDefinition.predecessor"
    assert inst.rest[0].resource[1].searchInclude[3] == "ActivityDefinition.composed-of"
    assert inst.rest[0].resource[1].searchInclude[4] == "ActivityDefinition.depends-on"
    assert (
        inst.rest[0].resource[1].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/ActivityDefinition-date"
    )
    assert (
        inst.rest[0].resource[1].searchParam[0].documentation
        == "The activity definition publication date"
    )
    assert inst.rest[0].resource[1].searchParam[0].name == "date"
    assert inst.rest[0].resource[1].searchParam[0].type == "date"
    assert inst.rest[0].resource[1].searchParam[1].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "identifier"
    )
    assert (
        inst.rest[0].resource[1].searchParam[1].documentation
        == "External identifier for the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[1].searchParam[1].type == "token"
    assert inst.rest[0].resource[1].searchParam[2].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "successor"
    )
    assert (
        inst.rest[0].resource[1].searchParam[2].documentation
        == "What resource is being referenced"
    )
    assert inst.rest[0].resource[1].searchParam[2].name == "successor"
    assert inst.rest[0].resource[1].searchParam[2].type == "reference"
    assert inst.rest[0].resource[1].searchParam[3].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "jurisdiction"
    )
    assert (
        inst.rest[0].resource[1].searchParam[3].documentation
        == "Intended jurisdiction for the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[3].name == "jurisdiction"
    assert inst.rest[0].resource[1].searchParam[3].type == "token"
    assert inst.rest[0].resource[1].searchParam[4].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "description"
    )
    assert (
        inst.rest[0].resource[1].searchParam[4].documentation
        == "The description of the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[4].name == "description"
    assert inst.rest[0].resource[1].searchParam[4].type == "string"
    assert inst.rest[0].resource[1].searchParam[5].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "derived-from"
    )
    assert (
        inst.rest[0].resource[1].searchParam[5].documentation
        == "What resource is being referenced"
    )
    assert inst.rest[0].resource[1].searchParam[5].name == "derived-from"
    assert inst.rest[0].resource[1].searchParam[5].type == "reference"
    assert inst.rest[0].resource[1].searchParam[6].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "predecessor"
    )
    assert (
        inst.rest[0].resource[1].searchParam[6].documentation
        == "What resource is being referenced"
    )
    assert inst.rest[0].resource[1].searchParam[6].name == "predecessor"
    assert inst.rest[0].resource[1].searchParam[6].type == "reference"
    assert (
        inst.rest[0].resource[1].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/ActivityDefinition-title"
    )
    assert (
        inst.rest[0].resource[1].searchParam[7].documentation
        == "The human-friendly name of the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[7].name == "title"
    assert inst.rest[0].resource[1].searchParam[7].type == "string"
    assert inst.rest[0].resource[1].searchParam[8].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "composed-of"
    )
    assert (
        inst.rest[0].resource[1].searchParam[8].documentation
        == "What resource is being referenced"
    )
    assert inst.rest[0].resource[1].searchParam[8].name == "composed-of"
    assert inst.rest[0].resource[1].searchParam[8].type == "reference"
    assert inst.rest[0].resource[1].searchParam[9].definition == (
        "http://hl7.org/fhir/SearchParameter/ActivityDefinition-" "version"
    )
    assert (
        inst.rest[0].resource[1].searchParam[9].documentation
        == "The business version of the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[9].name == "version"
    assert inst.rest[0].resource[1].searchParam[9].type == "token"
    assert inst.rest[0].resource[1].searchRevInclude[0] == "Communication.definition"
    assert inst.rest[0].resource[1].searchRevInclude[1] == "DeviceRequest.definition"
    assert inst.rest[0].resource[1].searchRevInclude[2] == "Procedure.definition"
    assert inst.rest[0].resource[1].searchRevInclude[3] == "ProcedureRequest.definition"
    assert inst.rest[0].resource[1].searchRevInclude[4] == "ReferralRequest.definition"
    assert inst.rest[0].resource[1].type == "ActivityDefinition"
    assert inst.rest[0].resource[2].conditionalCreate is True
    assert inst.rest[0].resource[2].conditionalDelete == "multiple"
    assert inst.rest[0].resource[2].conditionalUpdate is True
    assert inst.rest[0].resource[2].interaction[0].code == "read"
    assert inst.rest[0].resource[2].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[1].code == "vread"
    assert inst.rest[0].resource[2].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[2].code == "update"
    assert inst.rest[0].resource[2].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[3].code == "delete"
    assert inst.rest[0].resource[2].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[2].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[5].code == "history-type"
    assert inst.rest[0].resource[2].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[6].code == "create"
    assert inst.rest[0].resource[2].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[7].code == "search-type"
    assert inst.rest[0].resource[2].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[2].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/AdverseEvent"
    )
    assert inst.rest[0].resource[2].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[2].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[2].searchInclude[0] == "AdverseEvent.recorder"
    assert inst.rest[0].resource[2].searchInclude[1] == "AdverseEvent.study"
    assert inst.rest[0].resource[2].searchInclude[2] == "AdverseEvent.reaction"
    assert inst.rest[0].resource[2].searchInclude[3] == "AdverseEvent.subject"
    assert inst.rest[0].resource[2].searchInclude[4] == "AdverseEvent.substance"
    assert inst.rest[0].resource[2].searchInclude[5] == "AdverseEvent.location"
    assert (
        inst.rest[0].resource[2].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-date"
    )
    assert (
        inst.rest[0].resource[2].searchParam[0].documentation
        == "When the event occurred"
    )
    assert inst.rest[0].resource[2].searchParam[0].name == "date"
    assert inst.rest[0].resource[2].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[2].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-recorder"
    )
    assert (
        inst.rest[0].resource[2].searchParam[1].documentation
        == "Who recorded the adverse event"
    )
    assert inst.rest[0].resource[2].searchParam[1].name == "recorder"
    assert inst.rest[0].resource[2].searchParam[1].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-study"
    )
    assert inst.rest[0].resource[2].searchParam[2].documentation == "AdverseEvent.study"
    assert inst.rest[0].resource[2].searchParam[2].name == "study"
    assert inst.rest[0].resource[2].searchParam[2].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-reaction"
    )
    assert (
        inst.rest[0].resource[2].searchParam[3].documentation
        == "Adverse Reaction Events linked to exposure to substance"
    )
    assert inst.rest[0].resource[2].searchParam[3].name == "reaction"
    assert inst.rest[0].resource[2].searchParam[3].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-seriousness"
    )
    assert (
        inst.rest[0].resource[2].searchParam[4].documentation
        == "Mild | Moderate | Severe"
    )
    assert inst.rest[0].resource[2].searchParam[4].name == "seriousness"
    assert inst.rest[0].resource[2].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[2].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-subject"
    )
    assert (
        inst.rest[0].resource[2].searchParam[5].documentation
        == "Subject or group impacted by event"
    )
    assert inst.rest[0].resource[2].searchParam[5].name == "subject"
    assert inst.rest[0].resource[2].searchParam[5].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-substance"
    )
    assert (
        inst.rest[0].resource[2].searchParam[6].documentation
        == "Refers to the specific entity that caused the adverse event"
    )
    assert inst.rest[0].resource[2].searchParam[6].name == "substance"
    assert inst.rest[0].resource[2].searchParam[6].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-location"
    )
    assert (
        inst.rest[0].resource[2].searchParam[7].documentation
        == "Location where adverse event occurred"
    )
    assert inst.rest[0].resource[2].searchParam[7].name == "location"
    assert inst.rest[0].resource[2].searchParam[7].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[8].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-category"
    )
    assert inst.rest[0].resource[2].searchParam[8].name == "category"
    assert inst.rest[0].resource[2].searchParam[8].type == "token"
    assert (
        inst.rest[0].resource[2].searchParam[9].definition
        == "http://hl7.org/fhir/SearchParameter/AdverseEvent-type"
    )
    assert inst.rest[0].resource[2].searchParam[9].documentation == "actual | potential"
    assert inst.rest[0].resource[2].searchParam[9].name == "type"
    assert inst.rest[0].resource[2].searchParam[9].type == "token"
    assert inst.rest[0].resource[2].type == "AdverseEvent"
    assert inst.rest[0].resource[3].conditionalCreate is True
    assert inst.rest[0].resource[3].conditionalDelete == "multiple"
    assert inst.rest[0].resource[3].conditionalUpdate is True
    assert inst.rest[0].resource[3].interaction[0].code == "read"
    assert inst.rest[0].resource[3].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[1].code == "vread"
    assert inst.rest[0].resource[3].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[2].code == "update"
    assert inst.rest[0].resource[3].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[3].code == "delete"
    assert inst.rest[0].resource[3].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[3].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[5].code == "history-type"
    assert inst.rest[0].resource[3].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[6].code == "create"
    assert inst.rest[0].resource[3].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[7].code == "search-type"
    assert inst.rest[0].resource[3].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[3].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/AllergyIntolerance"
    )
    assert inst.rest[0].resource[3].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[3].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[3].searchInclude[0] == "AllergyIntolerance.recorder"
    assert inst.rest[0].resource[3].searchInclude[1] == "AllergyIntolerance.asserter"
    assert inst.rest[0].resource[3].searchInclude[2] == "AllergyIntolerance.patient"
    assert inst.rest[0].resource[3].searchParam[0].definition == (
        "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-" "severity"
    )
    assert (
        inst.rest[0].resource[3].searchParam[0].documentation
        == "mild | moderate | severe (of event as a whole)"
    )
    assert inst.rest[0].resource[3].searchParam[0].name == "severity"
    assert inst.rest[0].resource[3].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/clinical-date"
    )
    assert (
        inst.rest[0].resource[3].searchParam[1].documentation
        == "Date record was believed accurate"
    )
    assert inst.rest[0].resource[3].searchParam[1].name == "date"
    assert inst.rest[0].resource[3].searchParam[1].type == "date"
    assert (
        inst.rest[0].resource[3].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/clinical-identifier"
    )
    assert (
        inst.rest[0].resource[3].searchParam[2].documentation
        == "External ids for this item"
    )
    assert inst.rest[0].resource[3].searchParam[2].name == "identifier"
    assert inst.rest[0].resource[3].searchParam[2].type == "token"
    assert inst.rest[0].resource[3].searchParam[3].definition == (
        "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-" "manifestation"
    )
    assert (
        inst.rest[0].resource[3].searchParam[3].documentation
        == "Clinical symptoms/signs associated with the Event"
    )
    assert inst.rest[0].resource[3].searchParam[3].name == "manifestation"
    assert inst.rest[0].resource[3].searchParam[3].type == "token"
    assert inst.rest[0].resource[3].searchParam[4].definition == (
        "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-" "recorder"
    )
    assert (
        inst.rest[0].resource[3].searchParam[4].documentation
        == "Who recorded the sensitivity"
    )
    assert inst.rest[0].resource[3].searchParam[4].name == "recorder"
    assert inst.rest[0].resource[3].searchParam[4].type == "reference"
    assert (
        inst.rest[0].resource[3].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/clinical-code"
    )
    assert (
        inst.rest[0].resource[3].searchParam[5].documentation
        == "Code that identifies the allergy or intolerance"
    )
    assert inst.rest[0].resource[3].searchParam[5].name == "code"
    assert inst.rest[0].resource[3].searchParam[5].type == "token"
    assert inst.rest[0].resource[3].searchParam[6].definition == (
        "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-" "verification-status"
    )
    assert (
        inst.rest[0].resource[3].searchParam[6].documentation
        == "unconfirmed | confirmed | refuted | entered-in-error"
    )
    assert inst.rest[0].resource[3].searchParam[6].name == "verification-status"
    assert inst.rest[0].resource[3].searchParam[6].type == "token"
    assert inst.rest[0].resource[3].searchParam[7].definition == (
        "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-" "criticality"
    )
    assert (
        inst.rest[0].resource[3].searchParam[7].documentation
        == "low | high | unable-to-assess"
    )
    assert inst.rest[0].resource[3].searchParam[7].name == "criticality"
    assert inst.rest[0].resource[3].searchParam[7].type == "token"
    assert inst.rest[0].resource[3].searchParam[8].definition == (
        "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-" "clinical-status"
    )
    assert (
        inst.rest[0].resource[3].searchParam[8].documentation
        == "active | inactive | resolved"
    )
    assert inst.rest[0].resource[3].searchParam[8].name == "clinical-status"
    assert inst.rest[0].resource[3].searchParam[8].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[9].definition
        == "http://hl7.org/fhir/SearchParameter/clinical-type"
    )
    assert (
        inst.rest[0].resource[3].searchParam[9].documentation
        == "allergy | intolerance - Underlying mechanism (if known)"
    )
    assert inst.rest[0].resource[3].searchParam[9].name == "type"
    assert inst.rest[0].resource[3].searchParam[9].type == "token"
    assert inst.rest[0].resource[3].searchRevInclude[0] == "ClinicalImpression.problem"
    assert (
        inst.rest[0].resource[3].searchRevInclude[1]
        == "ImmunizationRecommendation.information"
    )
    assert inst.rest[0].resource[3].type == "AllergyIntolerance"
    assert inst.rest[0].resource[4].conditionalCreate is True
    assert inst.rest[0].resource[4].conditionalDelete == "multiple"
    assert inst.rest[0].resource[4].conditionalUpdate is True
    assert inst.rest[0].resource[4].interaction[0].code == "read"
    assert inst.rest[0].resource[4].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[1].code == "vread"
    assert inst.rest[0].resource[4].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[2].code == "update"
    assert inst.rest[0].resource[4].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[3].code == "delete"
    assert inst.rest[0].resource[4].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[4].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[5].code == "history-type"
    assert inst.rest[0].resource[4].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[6].code == "create"
    assert inst.rest[0].resource[4].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[7].code == "search-type"
    assert inst.rest[0].resource[4].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[4].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Appointment"
    )
    assert inst.rest[0].resource[4].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[4].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[4].searchInclude[0] == "Appointment.actor"
    assert inst.rest[0].resource[4].searchInclude[1] == "Appointment.practitioner"
    assert inst.rest[0].resource[4].searchInclude[2] == "Appointment.incomingreferral"
    assert inst.rest[0].resource[4].searchInclude[3] == "Appointment.patient"
    assert inst.rest[0].resource[4].searchInclude[4] == "Appointment.location"
    assert (
        inst.rest[0].resource[4].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Appointment-date"
    )
    assert (
        inst.rest[0].resource[4].searchParam[0].documentation
        == "Appointment date/time."
    )
    assert inst.rest[0].resource[4].searchParam[0].name == "date"
    assert inst.rest[0].resource[4].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[4].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Appointment-actor"
    )
    assert (
        inst.rest[0].resource[4].searchParam[1].documentation
        == "Any one of the individuals participating in the appointment"
    )
    assert inst.rest[0].resource[4].searchParam[1].name == "actor"
    assert inst.rest[0].resource[4].searchParam[1].type == "reference"
    assert (
        inst.rest[0].resource[4].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Appointment-identifier"
    )
    assert (
        inst.rest[0].resource[4].searchParam[2].documentation
        == "An Identifier of the Appointment"
    )
    assert inst.rest[0].resource[4].searchParam[2].name == "identifier"
    assert inst.rest[0].resource[4].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Appointment-practitioner"
    )
    assert inst.rest[0].resource[4].searchParam[3].documentation == (
        "One of the individuals of the appointment is this " "practitioner"
    )
    assert inst.rest[0].resource[4].searchParam[3].name == "practitioner"
    assert inst.rest[0].resource[4].searchParam[3].type == "reference"
    assert inst.rest[0].resource[4].searchParam[4].definition == (
        "http://hl7.org/fhir/SearchParameter/Appointment-" "incomingreferral"
    )
    assert inst.rest[0].resource[4].searchParam[4].documentation == (
        "The ReferralRequest provided as information to allocate to " "the Encounter"
    )
    assert inst.rest[0].resource[4].searchParam[4].name == "incomingreferral"
    assert inst.rest[0].resource[4].searchParam[4].type == "reference"
    assert (
        inst.rest[0].resource[4].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Appointment-part-status"
    )
    assert inst.rest[0].resource[4].searchParam[5].documentation == (
        "The Participation status of the subject, or other "
        "participant on the appointment. Can be used to locate "
        "participants that have not responded to meeting requests."
    )
    assert inst.rest[0].resource[4].searchParam[5].name == "part-status"
    assert inst.rest[0].resource[4].searchParam[5].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/Appointment-patient"
    )
    assert (
        inst.rest[0].resource[4].searchParam[6].documentation
        == "One of the individuals of the appointment is this patient"
    )
    assert inst.rest[0].resource[4].searchParam[6].name == "patient"
    assert inst.rest[0].resource[4].searchParam[6].type == "reference"
    assert inst.rest[0].resource[4].searchParam[7].definition == (
        "http://hl7.org/fhir/SearchParameter/Appointment-appointment-" "type"
    )
    assert inst.rest[0].resource[4].searchParam[7].documentation == (
        "The style of appointment or patient that has been booked in "
        "the slot (not service type)"
    )
    assert inst.rest[0].resource[4].searchParam[7].name == "appointment-type"
    assert inst.rest[0].resource[4].searchParam[7].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[8].definition
        == "http://hl7.org/fhir/SearchParameter/Appointment-service-type"
    )
    assert inst.rest[0].resource[4].searchParam[8].documentation == (
        "The specific service that is to be performed during this " "appointment"
    )
    assert inst.rest[0].resource[4].searchParam[8].name == "service-type"
    assert inst.rest[0].resource[4].searchParam[8].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[9].definition
        == "http://hl7.org/fhir/SearchParameter/Appointment-location"
    )
    assert inst.rest[0].resource[4].searchParam[9].documentation == (
        "This location is listed in the participants of the " "appointment"
    )
    assert inst.rest[0].resource[4].searchParam[9].name == "location"
    assert inst.rest[0].resource[4].searchParam[9].type == "reference"
    assert (
        inst.rest[0].resource[4].searchRevInclude[0]
        == "AppointmentResponse.appointment"
    )
    assert inst.rest[0].resource[4].searchRevInclude[1] == "CarePlan.activity-reference"
    assert inst.rest[0].resource[4].searchRevInclude[2] == "ClinicalImpression.action"
    assert inst.rest[0].resource[4].searchRevInclude[3] == "Encounter.appointment"
    assert inst.rest[0].resource[4].type == "Appointment"
    assert inst.rest[0].resource[5].conditionalCreate is True
    assert inst.rest[0].resource[5].conditionalDelete == "multiple"
    assert inst.rest[0].resource[5].conditionalUpdate is True
    assert inst.rest[0].resource[5].interaction[0].code == "read"
    assert inst.rest[0].resource[5].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[1].code == "vread"
    assert inst.rest[0].resource[5].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[2].code == "update"
    assert inst.rest[0].resource[5].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[3].code == "delete"
    assert inst.rest[0].resource[5].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[5].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[5].code == "history-type"
    assert inst.rest[0].resource[5].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[6].code == "create"
    assert inst.rest[0].resource[5].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[7].code == "search-type"
    assert inst.rest[0].resource[5].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[5].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/AppointmentResponse"
    )
    assert inst.rest[0].resource[5].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[5].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[5].searchInclude[0] == "AppointmentResponse.actor"
    assert (
        inst.rest[0].resource[5].searchInclude[1] == "AppointmentResponse.practitioner"
    )
    assert inst.rest[0].resource[5].searchInclude[2] == "AppointmentResponse.patient"
    assert (
        inst.rest[0].resource[5].searchInclude[3] == "AppointmentResponse.appointment"
    )
    assert inst.rest[0].resource[5].searchInclude[4] == "AppointmentResponse.location"
    assert inst.rest[0].resource[5].searchParam[0].definition == (
        "http://hl7.org/fhir/SearchParameter/AppointmentResponse-" "actor"
    )
    assert inst.rest[0].resource[5].searchParam[0].documentation == (
        "The Person, Location/HealthcareService or Device that this "
        "appointment response replies for"
    )
    assert inst.rest[0].resource[5].searchParam[0].name == "actor"
    assert inst.rest[0].resource[5].searchParam[0].type == "reference"
    assert inst.rest[0].resource[5].searchParam[1].definition == (
        "http://hl7.org/fhir/SearchParameter/AppointmentResponse-" "identifier"
    )
    assert (
        inst.rest[0].resource[5].searchParam[1].documentation
        == "An Identifier in this appointment response"
    )
    assert inst.rest[0].resource[5].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[5].searchParam[1].type == "token"
    assert inst.rest[0].resource[5].searchParam[2].definition == (
        "http://hl7.org/fhir/SearchParameter/AppointmentResponse-" "practitioner"
    )
    assert (
        inst.rest[0].resource[5].searchParam[2].documentation
        == "This Response is for this Practitioner"
    )
    assert inst.rest[0].resource[5].searchParam[2].name == "practitioner"
    assert inst.rest[0].resource[5].searchParam[2].type == "reference"
    assert inst.rest[0].resource[5].searchParam[3].definition == (
        "http://hl7.org/fhir/SearchParameter/AppointmentResponse-" "part-status"
    )
    assert (
        inst.rest[0].resource[5].searchParam[3].documentation
        == "The participants acceptance status for this appointment"
    )
    assert inst.rest[0].resource[5].searchParam[3].name == "part-status"
    assert inst.rest[0].resource[5].searchParam[3].type == "token"
    assert inst.rest[0].resource[5].searchParam[4].definition == (
        "http://hl7.org/fhir/SearchParameter/AppointmentResponse-" "patient"
    )
    assert (
        inst.rest[0].resource[5].searchParam[4].documentation
        == "This Response is for this Patient"
    )
    assert inst.rest[0].resource[5].searchParam[4].name == "patient"
    assert inst.rest[0].resource[5].searchParam[4].type == "reference"
    assert inst.rest[0].resource[5].searchParam[5].definition == (
        "http://hl7.org/fhir/SearchParameter/AppointmentResponse-" "appointment"
    )
    assert (
        inst.rest[0].resource[5].searchParam[5].documentation
        == "The appointment that the response is attached to"
    )
    assert inst.rest[0].resource[5].searchParam[5].name == "appointment"
    assert inst.rest[0].resource[5].searchParam[5].type == "reference"
    assert inst.rest[0].resource[5].searchParam[6].definition == (
        "http://hl7.org/fhir/SearchParameter/AppointmentResponse-" "location"
    )
    assert (
        inst.rest[0].resource[5].searchParam[6].documentation
        == "This Response is for this Location"
    )
    assert inst.rest[0].resource[5].searchParam[6].name == "location"
    assert inst.rest[0].resource[5].searchParam[6].type == "reference"
    assert inst.rest[0].resource[5].type == "AppointmentResponse"
    assert inst.rest[0].resource[6].conditionalCreate is True
    assert inst.rest[0].resource[6].conditionalDelete == "multiple"
    assert inst.rest[0].resource[6].conditionalUpdate is True
    assert inst.rest[0].resource[6].interaction[0].code == "read"
    assert inst.rest[0].resource[6].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[1].code == "vread"
    assert inst.rest[0].resource[6].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[2].code == "update"
    assert inst.rest[0].resource[6].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[3].code == "delete"
    assert inst.rest[0].resource[6].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[6].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[5].code == "history-type"
    assert inst.rest[0].resource[6].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[6].code == "create"
    assert inst.rest[0].resource[6].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[7].code == "search-type"
    assert inst.rest[0].resource[6].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[6].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/AuditEvent"
    )
    assert inst.rest[0].resource[6].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[6].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[6].searchInclude[0] == "AuditEvent.agent"
    assert inst.rest[0].resource[6].searchInclude[1] == "AuditEvent.patient"
    assert inst.rest[0].resource[6].searchInclude[2] == "AuditEvent.entity"
    assert (
        inst.rest[0].resource[6].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-date"
    )
    assert (
        inst.rest[0].resource[6].searchParam[0].documentation
        == "Time when the event occurred on source"
    )
    assert inst.rest[0].resource[6].searchParam[0].name == "date"
    assert inst.rest[0].resource[6].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[6].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-entity-type"
    )
    assert (
        inst.rest[0].resource[6].searchParam[1].documentation
        == "Type of entity involved"
    )
    assert inst.rest[0].resource[6].searchParam[1].name == "entity-type"
    assert inst.rest[0].resource[6].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-agent"
    )
    assert (
        inst.rest[0].resource[6].searchParam[2].documentation
        == "Direct reference to resource"
    )
    assert inst.rest[0].resource[6].searchParam[2].name == "agent"
    assert inst.rest[0].resource[6].searchParam[2].type == "reference"
    assert (
        inst.rest[0].resource[6].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-address"
    )
    assert (
        inst.rest[0].resource[6].searchParam[3].documentation
        == "Identifier for the network access point of the user device"
    )
    assert inst.rest[0].resource[6].searchParam[3].name == "address"
    assert inst.rest[0].resource[6].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[6].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-entity-role"
    )
    assert (
        inst.rest[0].resource[6].searchParam[4].documentation
        == "What role the entity played"
    )
    assert inst.rest[0].resource[6].searchParam[4].name == "entity-role"
    assert inst.rest[0].resource[6].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-source"
    )
    assert (
        inst.rest[0].resource[6].searchParam[5].documentation
        == "The identity of source detecting the event"
    )
    assert inst.rest[0].resource[6].searchParam[5].name == "source"
    assert inst.rest[0].resource[6].searchParam[5].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-type"
    )
    assert (
        inst.rest[0].resource[6].searchParam[6].documentation
        == "Type/identifier of event"
    )
    assert inst.rest[0].resource[6].searchParam[6].name == "type"
    assert inst.rest[0].resource[6].searchParam[6].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-altid"
    )
    assert (
        inst.rest[0].resource[6].searchParam[7].documentation
        == "Alternative User id e.g. authentication"
    )
    assert inst.rest[0].resource[6].searchParam[7].name == "altid"
    assert inst.rest[0].resource[6].searchParam[7].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[8].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-site"
    )
    assert (
        inst.rest[0].resource[6].searchParam[8].documentation
        == "Logical source location within the enterprise"
    )
    assert inst.rest[0].resource[6].searchParam[8].name == "site"
    assert inst.rest[0].resource[6].searchParam[8].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[9].definition
        == "http://hl7.org/fhir/SearchParameter/AuditEvent-agent-name"
    )
    assert (
        inst.rest[0].resource[6].searchParam[9].documentation
        == "Human-meaningful name for the agent"
    )
    assert inst.rest[0].resource[6].searchParam[9].name == "agent-name"
    assert inst.rest[0].resource[6].searchParam[9].type == "string"
    assert inst.rest[0].resource[6].type == "AuditEvent"
    assert inst.rest[0].resource[7].conditionalCreate is True
    assert inst.rest[0].resource[7].conditionalDelete == "multiple"
    assert inst.rest[0].resource[7].conditionalUpdate is True
    assert inst.rest[0].resource[7].interaction[0].code == "read"
    assert inst.rest[0].resource[7].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[1].code == "vread"
    assert inst.rest[0].resource[7].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[2].code == "update"
    assert inst.rest[0].resource[7].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[3].code == "delete"
    assert inst.rest[0].resource[7].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[7].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[5].code == "history-type"
    assert inst.rest[0].resource[7].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[6].code == "create"
    assert inst.rest[0].resource[7].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[7].code == "search-type"
    assert inst.rest[0].resource[7].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[7].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Basic"
    )
    assert inst.rest[0].resource[7].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[7].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[7].searchInclude[0] == "Basic.subject"
    assert inst.rest[0].resource[7].searchInclude[1] == "Basic.patient"
    assert inst.rest[0].resource[7].searchInclude[2] == "Basic.author"
    assert (
        inst.rest[0].resource[7].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Basic-identifier"
    )
    assert (
        inst.rest[0].resource[7].searchParam[0].documentation == "Business identifier"
    )
    assert inst.rest[0].resource[7].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[7].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[7].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Basic-code"
    )
    assert inst.rest[0].resource[7].searchParam[1].documentation == "Kind of Resource"
    assert inst.rest[0].resource[7].searchParam[1].name == "code"
    assert inst.rest[0].resource[7].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[7].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Basic-subject"
    )
    assert (
        inst.rest[0].resource[7].searchParam[2].documentation
        == "Identifies the focus of this resource"
    )
    assert inst.rest[0].resource[7].searchParam[2].name == "subject"
    assert inst.rest[0].resource[7].searchParam[2].type == "reference"
    assert (
        inst.rest[0].resource[7].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Basic-created"
    )
    assert inst.rest[0].resource[7].searchParam[3].documentation == "When created"
    assert inst.rest[0].resource[7].searchParam[3].name == "created"
    assert inst.rest[0].resource[7].searchParam[3].type == "date"
    assert (
        inst.rest[0].resource[7].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/Basic-patient"
    )
    assert (
        inst.rest[0].resource[7].searchParam[4].documentation
        == "Identifies the focus of this resource"
    )
    assert inst.rest[0].resource[7].searchParam[4].name == "patient"
    assert inst.rest[0].resource[7].searchParam[4].type == "reference"
    assert (
        inst.rest[0].resource[7].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Basic-author"
    )
    assert inst.rest[0].resource[7].searchParam[5].documentation == "Who created"
    assert inst.rest[0].resource[7].searchParam[5].name == "author"
    assert inst.rest[0].resource[7].searchParam[5].type == "reference"
    assert inst.rest[0].resource[7].type == "Basic"
    assert inst.rest[0].resource[8].conditionalCreate is True
    assert inst.rest[0].resource[8].conditionalDelete == "multiple"
    assert inst.rest[0].resource[8].conditionalUpdate is True
    assert inst.rest[0].resource[8].interaction[0].code == "read"
    assert inst.rest[0].resource[8].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[1].code == "vread"
    assert inst.rest[0].resource[8].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[2].code == "update"
    assert inst.rest[0].resource[8].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[3].code == "delete"
    assert inst.rest[0].resource[8].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[8].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[5].code == "history-type"
    assert inst.rest[0].resource[8].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[6].code == "create"
    assert inst.rest[0].resource[8].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[7].code == "search-type"
    assert inst.rest[0].resource[8].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[8].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Binary"
    )
    assert inst.rest[0].resource[8].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[8].referencePolicy[1] == "logical"
    assert (
        inst.rest[0].resource[8].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/Binary-contenttype"
    )
    assert (
        inst.rest[0].resource[8].searchParam[0].documentation
        == "MimeType of the binary content"
    )
    assert inst.rest[0].resource[8].searchParam[0].name == "contenttype"
    assert inst.rest[0].resource[8].searchParam[0].type == "token"
    assert inst.rest[0].resource[8].type == "Binary"
    assert inst.rest[0].resource[9].conditionalCreate is True
    assert inst.rest[0].resource[9].conditionalDelete == "multiple"
    assert inst.rest[0].resource[9].conditionalUpdate is True
    assert inst.rest[0].resource[9].interaction[0].code == "read"
    assert inst.rest[0].resource[9].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[1].code == "vread"
    assert inst.rest[0].resource[9].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[2].code == "update"
    assert inst.rest[0].resource[9].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[3].code == "delete"
    assert inst.rest[0].resource[9].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[9].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[5].code == "history-type"
    assert inst.rest[0].resource[9].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[6].code == "create"
    assert inst.rest[0].resource[9].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[7].code == "search-type"
    assert inst.rest[0].resource[9].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[9].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/BodySite"
    )
    assert inst.rest[0].resource[9].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[9].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[9].searchInclude[0] == "BodySite.patient"
    assert (
        inst.rest[0].resource[9].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/BodySite-identifier"
    )
    assert (
        inst.rest[0].resource[9].searchParam[0].documentation
        == "Identifier for this instance of the anatomical location"
    )
    assert inst.rest[0].resource[9].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[9].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[9].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/BodySite-code"
    )
    assert (
        inst.rest[0].resource[9].searchParam[1].documentation
        == "Named anatomical location"
    )
    assert inst.rest[0].resource[9].searchParam[1].name == "code"
    assert inst.rest[0].resource[9].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[9].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/BodySite-patient"
    )
    assert (
        inst.rest[0].resource[9].searchParam[2].documentation
        == "Patient to whom bodysite belongs"
    )
    assert inst.rest[0].resource[9].searchParam[2].name == "patient"
    assert inst.rest[0].resource[9].searchParam[2].type == "reference"
    assert inst.rest[0].resource[9].type == "BodySite"
    assert (
        inst.rest[0].searchParam[0].definition
        == "http://hl7.org/fhir/SearchParameter/DomainResource-text"
    )
    assert (
        inst.rest[0].searchParam[0].documentation
        == "Search on the narrative of the resource"
    )
    assert inst.rest[0].searchParam[0].name == "_text"
    assert inst.rest[0].searchParam[0].type == "string"
    assert (
        inst.rest[0].searchParam[1].definition
        == "http://hl7.org/fhir/SearchParameter/Resource-query"
    )
    assert inst.rest[0].searchParam[1].documentation == (
        "A custom search profile that describes a specific defined " "query operation"
    )
    assert inst.rest[0].searchParam[1].name == "_query"
    assert inst.rest[0].searchParam[1].type == "token"
    assert (
        inst.rest[0].searchParam[2].definition
        == "http://hl7.org/fhir/SearchParameter/Resource-profile"
    )
    assert (
        inst.rest[0].searchParam[2].documentation
        == "Profiles this resource claims to conform to"
    )
    assert inst.rest[0].searchParam[2].name == "_profile"
    assert inst.rest[0].searchParam[2].type == "uri"
    assert (
        inst.rest[0].searchParam[3].definition
        == "http://hl7.org/fhir/SearchParameter/Resource-lastUpdated"
    )
    assert (
        inst.rest[0].searchParam[3].documentation
        == "When the resource version last changed"
    )
    assert inst.rest[0].searchParam[3].name == "_lastUpdated"
    assert inst.rest[0].searchParam[3].type == "date"
    assert (
        inst.rest[0].searchParam[4].definition
        == "http://hl7.org/fhir/SearchParameter/Resource-tag"
    )
    assert inst.rest[0].searchParam[4].documentation == "Tags applied to this resource"
    assert inst.rest[0].searchParam[4].name == "_tag"
    assert inst.rest[0].searchParam[4].type == "token"
    assert (
        inst.rest[0].searchParam[5].definition
        == "http://hl7.org/fhir/SearchParameter/Resource-security"
    )
    assert (
        inst.rest[0].searchParam[5].documentation
        == "Security Labels applied to this resource"
    )
    assert inst.rest[0].searchParam[5].name == "_security"
    assert inst.rest[0].searchParam[5].type == "token"
    assert (
        inst.rest[0].searchParam[6].definition
        == "http://hl7.org/fhir/SearchParameter/Resource-id"
    )
    assert inst.rest[0].searchParam[6].documentation == "Logical id of this artifact"
    assert inst.rest[0].searchParam[6].name == "_id"
    assert inst.rest[0].searchParam[6].type == "token"
    assert (
        inst.rest[0].searchParam[7].definition
        == "http://hl7.org/fhir/SearchParameter/Resource-content"
    )
    assert (
        inst.rest[0].searchParam[7].documentation
        == "Search on the entire content of the resource"
    )
    assert inst.rest[0].searchParam[7].name == "_content"
    assert inst.rest[0].searchParam[7].type == "string"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.description == (
        "This is the Capability Statement to declare that the server "
        "supports SMART-on-FHIR. See the SMART-on-FHIR docs for the "
        "extension that would go with such a server"
    )
    assert inst.rest[0].security.service[0].coding[0].code == "SMART-on-FHIR"
    assert inst.rest[0].security.service[0].coding[0].display == "SMART-on-FHIR"
    assert (
        inst.rest[0].security.service[0].coding[0].system
        == "http://hl7.org/fhir/restful-security-service"
    )
    assert inst.rest[0].security.service[0].text == "See http://docs.smarthealthit.org/"
    assert inst.software.name == "Insert your softwware name here..."
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/CapabilityStatement/base"
    assert inst.version == "3.0.1-11917"


def test_capabilitystatement_8(base_settings):
    """No. 8 tests collection for CapabilityStatement.
    Test File: capabilitystatement-base.json
    """
    filename = base_settings["unittest_data_dir"] / "capabilitystatement-base.json"
    inst = capabilitystatement.CapabilityStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CapabilityStatement" == inst.resource_type

    impl_capabilitystatement_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_8(inst2)
