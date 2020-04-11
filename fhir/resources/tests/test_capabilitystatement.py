# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import capabilitystatement
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class CapabilityStatementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("CapabilityStatement", js["resourceType"])
        return capabilitystatement.CapabilityStatement(js)

    def testCapabilityStatement1(self):
        inst = self.instantiate_from("capabilitystatement-messagedefinition.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CapabilityStatement instance"
        )
        self.implCapabilityStatement1(inst)

        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement1(inst2)

    def implCapabilityStatement1(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].name), force_bytes("System Administrator")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("wile@acme.org")
        )
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.date.as_json(), "2012-01-04")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Sample capability statement showing new MessageDefinition structure"
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("4.0.1"))
        self.assertEqual(force_bytes(inst.format[0]), force_bytes("xml"))
        self.assertEqual(force_bytes(inst.format[1]), force_bytes("json"))
        self.assertEqual(force_bytes(inst.id), force_bytes("messagedefinition"))
        self.assertEqual(
            force_bytes(inst.implementation.description),
            force_bytes("Acme Message endpoint"),
        )
        self.assertEqual(
            force_bytes(inst.implementation.url),
            force_bytes("http://acem.com/fhir/message-drop"),
        )
        self.assertEqual(force_bytes(inst.kind), force_bytes("instance"))
        self.assertEqual(
            force_bytes(inst.messaging[0].documentation),
            force_bytes("ADT A08 equivalent for external system notifications"),
        )
        self.assertEqual(
            force_bytes(inst.messaging[0].endpoint[0].address),
            force_bytes("mllp:10.1.1.10:9234"),
        )
        self.assertEqual(
            force_bytes(inst.messaging[0].endpoint[0].protocol.code),
            force_bytes("mllp"),
        )
        self.assertEqual(
            force_bytes(inst.messaging[0].endpoint[0].protocol.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/message-transport"),
        )
        self.assertEqual(inst.messaging[0].reliableCache, 30)
        self.assertEqual(
            force_bytes(inst.messaging[0].supportedMessage[0].definition),
            force_bytes("MessageDefinition/example"),
        )
        self.assertEqual(
            force_bytes(inst.messaging[0].supportedMessage[0].mode),
            force_bytes("receiver"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("ACME Corporation"))
        self.assertEqual(force_bytes(inst.software.name), force_bytes("EHR"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCapabilityStatement2(self):
        inst = self.instantiate_from("capabilitystatement-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CapabilityStatement instance"
        )
        self.implCapabilityStatement2(inst)

        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement2(inst2)

    def implCapabilityStatement2(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].name), force_bytes("System Administrator")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("wile@acme.org")
        )
        self.assertEqual(
            force_bytes(inst.copyright),
            force_bytes("Copyright © Acme Healthcare and GoodCorp EHR Systems"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.date.as_json(), "2012-01-04")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "This is the FHIR capability statement for the main EHR at ACME for the private interface - it does not describe the public interface"
            ),
        )
        self.assertEqual(
            force_bytes(inst.document[0].documentation),
            force_bytes("Basic rules for all documents in the EHR system"),
        )
        self.assertEqual(force_bytes(inst.document[0].mode), force_bytes("consumer"))
        self.assertEqual(
            force_bytes(inst.document[0].profile),
            force_bytes(
                "http://fhir.hl7.org/base/Profilebc054d23-75e1-4dc6-aca5-838b6b1ac81d/_history/b5fdd9fc-b021-4ea1-911a-721a60663796"
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("4.0.1"))
        self.assertEqual(force_bytes(inst.format[0]), force_bytes("xml"))
        self.assertEqual(force_bytes(inst.format[1]), force_bytes("json"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.implementation.description),
            force_bytes("main EHR at ACME"),
        )
        self.assertEqual(
            force_bytes(inst.implementation.url), force_bytes("http://10.2.3.4/fhir")
        )
        self.assertEqual(
            force_bytes(inst.implementationGuide[0]),
            force_bytes("http://hl7.org/fhir/us/lab"),
        )
        self.assertEqual(
            force_bytes(inst.instantiates[0]),
            force_bytes("http://ihe.org/fhir/CapabilityStatement/pixm-client"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America (the)"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
        )
        self.assertEqual(force_bytes(inst.kind), force_bytes("instance"))
        self.assertEqual(
            force_bytes(inst.messaging[0].documentation),
            force_bytes("ADT A08 equivalent for external system notifications"),
        )
        self.assertEqual(
            force_bytes(inst.messaging[0].endpoint[0].address),
            force_bytes("mllp:10.1.1.10:9234"),
        )
        self.assertEqual(
            force_bytes(inst.messaging[0].endpoint[0].protocol.code),
            force_bytes("mllp"),
        )
        self.assertEqual(
            force_bytes(inst.messaging[0].endpoint[0].protocol.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/message-transport"),
        )
        self.assertEqual(inst.messaging[0].reliableCache, 30)
        self.assertEqual(
            force_bytes(inst.messaging[0].supportedMessage[0].definition),
            force_bytes("MessageDefinition/example"),
        )
        self.assertEqual(
            force_bytes(inst.messaging[0].supportedMessage[0].mode),
            force_bytes("receiver"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("ACME-EHR"))
        self.assertEqual(
            force_bytes(inst.patchFormat[0]), force_bytes("application/xml-patch+xml")
        )
        self.assertEqual(
            force_bytes(inst.patchFormat[1]), force_bytes("application/json-patch+json")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("ACME Corporation"))
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "Main EHR capability statement, published for contracting and operational support"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].compartment[0]),
            force_bytes("http://hl7.org/fhir/CompartmentDefinition/patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].documentation),
            force_bytes("Main FHIR endpoint for acem health"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[0].code), force_bytes("transaction")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[1].code), force_bytes("history-system")
        )
        self.assertEqual(force_bytes(inst.rest[0].mode), force_bytes("server"))
        self.assertTrue(inst.rest[0].resource[0].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].conditionalDelete),
            force_bytes("not-supported"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].conditionalRead),
            force_bytes("full-support"),
        )
        self.assertFalse(inst.rest[0].resource[0].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].documentation),
            force_bytes("This server does not let the clients create identities."),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].documentation),
            force_bytes("Only supported for patient records since 12-Dec 2012"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[3].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[4].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].profile),
            force_bytes(
                "http://registry.fhir.org/r4/StructureDefinition/7896271d-57f6-4231-89dc-dcc91eab2416"
            ),
        )
        self.assertTrue(inst.rest[0].resource[0].readHistory)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchInclude[0]),
            force_bytes("Organization"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Patient-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].documentation),
            force_bytes("Only supports search by institution MRN"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/Patient-general-practitioner"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].name),
            force_bytes("general-practitioner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchRevInclude[0]),
            force_bytes("Person"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].supportedProfile[0]),
            force_bytes(
                "http://registry.fhir.org/r4/StructureDefinition/00ab9e7a-06c7-4f77-9234-4154ca1e3347"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].type), force_bytes("Patient")
        )
        self.assertFalse(inst.rest[0].resource[0].updateCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].versioning),
            force_bytes("versioned-update"),
        )
        self.assertTrue(inst.rest[0].security.cors)
        self.assertEqual(
            force_bytes(inst.rest[0].security.description),
            force_bytes("See Smart on FHIR documentation"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].code),
            force_bytes("SMART-on-FHIR"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/restful-security-service"
            ),
        )
        self.assertEqual(force_bytes(inst.software.name), force_bytes("EHR"))
        self.assertEqual(inst.software.releaseDate.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.software.releaseDate.as_json(), "2012-01-04")
        self.assertEqual(
            force_bytes(inst.software.version), force_bytes("0.00.020.2134")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("ACME EHR capability statement")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("urn:uuid:68D043B5-9ECF-4559-A57A-396E0D452311"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("positive"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/variant-state"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("20130510"))

    def testCapabilityStatement3(self):
        inst = self.instantiate_from("capabilitystatement-measure-processor.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CapabilityStatement instance"
        )
        self.implCapabilityStatement3(inst)

        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement3(inst2)

    def implCapabilityStatement3(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR Project"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("other")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-09-16").date)
        self.assertEqual(inst.date.as_json(), "2016-09-16")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Basic conformance statement for a Measure Processor Service. A server can support more functionality    than defined here, but this is the minimum amount"
            ),
        )
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("4.0.1"))
        self.assertEqual(force_bytes(inst.format[0]), force_bytes("json"))
        self.assertEqual(force_bytes(inst.format[1]), force_bytes("xml"))
        self.assertEqual(force_bytes(inst.id), force_bytes("measure-processor"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("capability"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Measure Processor Service Conformance Statement"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7, Inc"))
        self.assertEqual(
            force_bytes(inst.rest[0].documentation),
            force_bytes("RESTful Measure Processor Service"),
        )
        self.assertEqual(force_bytes(inst.rest[0].mode), force_bytes("server"))
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].definition),
            force_bytes("OperationDefinition/Measure-evaluate-measure"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].name), force_bytes("evaluate-measure")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[1].definition),
            force_bytes("OperationDefinition/Measure-data-requirements"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[1].name),
            force_bytes("data-requirements"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].documentation),
            force_bytes(
                "Read allows clients to get the logical definitions of the measures"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].documentation),
            force_bytes(
                "Search allows clients to filter measures based on a provided search parameter"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].profile),
            force_bytes("StructureDefinition/Measure"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].name),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].name),
            force_bytes("version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].type), force_bytes("Measure")
        )
        self.assertTrue(inst.rest[0].security.cors)
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].code),
            force_bytes("Certificates"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/restful-security-service"
            ),
        )
        self.assertEqual(
            force_bytes(inst.software.name),
            force_bytes("ACME Measure Processor Service"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/measure-processor")
        )

    def testCapabilityStatement4(self):
        inst = self.instantiate_from("capabilitystatement-terminology-server.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CapabilityStatement instance"
        )
        self.implCapabilityStatement4(inst)

        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement4(inst2)

    def implCapabilityStatement4(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR Project"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-07-05").date)
        self.assertEqual(inst.date.as_json(), "2015-07-05")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Basic capability statement for a Terminology Server. A server can support more fucntionality than defined here, but this is the minimum amount"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-supported-system"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueUri), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("4.0.1"))
        self.assertEqual(force_bytes(inst.format[0]), force_bytes("json"))
        self.assertEqual(force_bytes(inst.format[1]), force_bytes("xml"))
        self.assertEqual(force_bytes(inst.id), force_bytes("terminology-server"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("capability"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Terminology Service Capability Statement"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7, Inc"))
        self.assertEqual(
            force_bytes(inst.rest[0].documentation),
            force_bytes("RESTful Terminology Server"),
        )
        self.assertEqual(force_bytes(inst.rest[0].mode), force_bytes("server"))
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].definition),
            force_bytes("OperationDefinition/ValueSet-expand"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].extension[0].valueCode),
            force_bytes("SHALL"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].name), force_bytes("expand")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[1].definition),
            force_bytes("OperationDefinition/CodeSystem-lookup"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[1].extension[0].valueCode),
            force_bytes("SHALL"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[1].name), force_bytes("lookup")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[2].definition),
            force_bytes("OperationDefinition/ValueSet-validate-code"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[2].extension[0].valueCode),
            force_bytes("SHALL"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[2].name), force_bytes("validate-code")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[3].definition),
            force_bytes("OperationDefinition/ConceptMap-translate"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[3].extension[0].valueCode),
            force_bytes("SHALL"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[3].name), force_bytes("translate")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[4].definition),
            force_bytes("OperationDefinition/ConceptMap-closure"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[4].extension[0].valueCode),
            force_bytes("SHOULD"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[4].name), force_bytes("closure")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].documentation),
            force_bytes(
                "Read allows clients to get the logical definitions of the value sets"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].extension[0].valueCode),
            force_bytes("SHALL"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].documentation),
            force_bytes("Search allows clients to find value sets on the server"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].extension[0].valueCode),
            force_bytes("SHALL"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].profile),
            force_bytes("StructureDefinition/ValueSet"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ValueSet-date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].name),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ValueSet-name"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].name),
            force_bytes("name"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ValueSet-reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].name),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ValueSet-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].name),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ValueSet-url"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].name),
            force_bytes("url"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].type),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ValueSet-version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].name),
            force_bytes("version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].type), force_bytes("ValueSet")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[0].documentation),
            force_bytes(
                "Read allows clients to get the logical definitions of the concept maps"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[0].extension[0].valueCode),
            force_bytes("SHALL"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[1].documentation),
            force_bytes("Search allows clients to find concept maps on the server"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[1].extension[0].valueCode),
            force_bytes("SHALL"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].profile),
            force_bytes("StructureDefinition/ConceptMap"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ConceptMap-date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].name),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ConceptMap-name"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].name),
            force_bytes("name"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ConceptMap-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].name),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ConceptMap-source"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].name),
            force_bytes("source"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].type),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ConceptMap-target"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].name),
            force_bytes("target"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].type),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ConceptMap-url"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].name),
            force_bytes("url"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].type),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ConceptMap-version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].name),
            force_bytes("version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].type), force_bytes("ConceptMap")
        )
        self.assertTrue(inst.rest[0].security.cors)
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].code),
            force_bytes("Certificates"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/restful-security-service"
            ),
        )
        self.assertEqual(
            force_bytes(inst.software.name), force_bytes("ACME Terminology Server")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/terminology-server")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCapabilityStatement5(self):
        inst = self.instantiate_from("capabilitystatement-base2.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CapabilityStatement instance"
        )
        self.implCapabilityStatement5(inst)

        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement5(inst2)

    def implCapabilityStatement5(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("4.0.1"))
        self.assertEqual(force_bytes(inst.format[0]), force_bytes("xml"))
        self.assertEqual(force_bytes(inst.format[1]), force_bytes("json"))
        self.assertEqual(force_bytes(inst.id), force_bytes("base2"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("capability"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Base FHIR Capability Statement (Empty)"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project Team"))
        self.assertEqual(
            force_bytes(inst.rest[0].documentation),
            force_bytes("An empty Capability Statement"),
        )
        self.assertEqual(force_bytes(inst.rest[0].mode), force_bytes("server"))
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].documentation),
            force_bytes("Read CapabilityStatement Resource"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].type),
            force_bytes("CapabilityStatement"),
        )
        self.assertTrue(inst.rest[0].security.cors)
        self.assertEqual(
            force_bytes(inst.rest[0].security.description),
            force_bytes(
                "This is the Capability Statement to declare that the server supports SMART-on-FHIR. See the SMART-on-FHIR docs for the extension that would go with such a server"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].code),
            force_bytes("SMART-on-FHIR"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].display),
            force_bytes("SMART-on-FHIR"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/restful-security-service"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].text),
            force_bytes("See http://docs.smarthealthit.org/"),
        )
        self.assertEqual(
            force_bytes(inst.software.name),
            force_bytes("Insert your software name here..."),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/CapabilityStatement/base2"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCapabilityStatement6(self):
        inst = self.instantiate_from("capabilitystatement-phr-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CapabilityStatement instance"
        )
        self.implCapabilityStatement6(inst)

        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement6(inst2)

    def implCapabilityStatement6(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2013-06-18").date)
        self.assertEqual(inst.date.as_json(), "2013-06-18")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Prototype Capability Statement for September 2013 Connectathon"
            ),
        )
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("4.0.1"))
        self.assertEqual(force_bytes(inst.format[0]), force_bytes("json"))
        self.assertEqual(force_bytes(inst.format[1]), force_bytes("xml"))
        self.assertEqual(force_bytes(inst.id), force_bytes("phr"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("capability"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("PHR Template"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project"))
        self.assertEqual(
            force_bytes(inst.rest[0].documentation),
            force_bytes(
                "Protoype server Capability Statement for September 2013 Connectathon"
            ),
        )
        self.assertEqual(force_bytes(inst.rest[0].mode), force_bytes("server"))
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].documentation),
            force_bytes(
                "When a client searches patients with no search criteria, they get a list of all patients they have access too. Servers may elect to offer additional search parameters, but this is not required"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].type), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].documentation),
            force_bytes(
                "_id parameter always supported. For the connectathon, servers may elect which search parameters are supported"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].name),
            force_bytes("_id"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].type), force_bytes("DocumentReference")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].documentation),
            force_bytes("Standard _id parameter"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].name),
            force_bytes("_id"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].type), force_bytes("Condition")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].documentation),
            force_bytes("Standard _id parameter"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].name),
            force_bytes("_id"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].documentation),
            force_bytes("which diagnostic discipline/department created the report"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].name),
            force_bytes("service"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].type), force_bytes("DiagnosticReport")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].text), force_bytes("OAuth")
        )
        self.assertEqual(
            force_bytes(inst.software.name), force_bytes("ACME PHR Server")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCapabilityStatement7(self):
        inst = self.instantiate_from("capabilitystatement-knowledge-repository.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CapabilityStatement instance"
        )
        self.implCapabilityStatement7(inst)

        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement7(inst2)

    def implCapabilityStatement7(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR Project"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("other")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-02-25").date)
        self.assertEqual(inst.date.as_json(), "2017-02-25")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Basic conformance statement for a Knowledge Repository Service. A server can support more functionality    than defined here, but this is the minimum amount"
            ),
        )
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("4.0.1"))
        self.assertEqual(force_bytes(inst.format[0]), force_bytes("json"))
        self.assertEqual(force_bytes(inst.format[1]), force_bytes("xml"))
        self.assertEqual(force_bytes(inst.id), force_bytes("knowledge-repository"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("capability"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Knowledge Repository Service Conformance Statement"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7, Inc"))
        self.assertEqual(
            force_bytes(inst.rest[0].documentation),
            force_bytes("RESTful Knowledge Repository Service"),
        )
        self.assertEqual(force_bytes(inst.rest[0].mode), force_bytes("server"))
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].definition),
            force_bytes("OperationDefinition/Library-data-requirements"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].name),
            force_bytes("data-requirements"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].documentation),
            force_bytes(
                "Read allows clients to get the logical definitions of the libraries"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].documentation),
            force_bytes(
                "Search allows clients to filter libraries based on a provided search parameter"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].profile),
            force_bytes("StructureDefinition/Library"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-description"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].name),
            force_bytes("description"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].name),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].name),
            force_bytes("title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-topic"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].name),
            force_bytes("topic"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].name),
            force_bytes("version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[6].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-composed-of"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[6].name),
            force_bytes("composed-of"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[6].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[7].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-depends-on"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[7].name),
            force_bytes("depends-on"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[7].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[8].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-derived-from"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[8].name),
            force_bytes("derived-from"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[8].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[9].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Library-predecessor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[9].name),
            force_bytes("predecessor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[9].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].type), force_bytes("Library")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[0].documentation),
            force_bytes(
                "Read allows clients to get the logical definitions of the plan definitions"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[1].documentation),
            force_bytes(
                "Search allows clients to filter plan definitions based on a provided search parameter"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].profile),
            force_bytes("StructureDefinition/PlanDefinition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/PlanDefinition-description"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].name),
            force_bytes("description"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/PlanDefinition-identifier"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/PlanDefinition-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].name),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/PlanDefinition-title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].name),
            force_bytes("title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/PlanDefinition-topic"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].name),
            force_bytes("topic"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/PlanDefinition-version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].name),
            force_bytes("version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/PlanDefinition-composed-of"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].name),
            force_bytes("composed-of"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[7].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/PlanDefinition-depends-on"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[7].name),
            force_bytes("depends-on"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[7].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[8].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/PlanDefinition-derived-from"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[8].name),
            force_bytes("derived-from"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[8].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[9].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/PlanDefinition-predecessor"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[9].name),
            force_bytes("predecessor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[9].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].type), force_bytes("PlanDefinition")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[0].documentation),
            force_bytes(
                "Read allows clients to get the logical definitions of the activity definitions"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[1].documentation),
            force_bytes(
                "Search allows clients to filter activity definitions based on a provided search parameter"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].profile),
            force_bytes("StructureDefinition/ActivityDefinition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-description"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].name),
            force_bytes("description"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[1].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-identifier"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[1].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[2].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[2].name),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[2].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ActivityDefinition-title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[3].name),
            force_bytes("title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[3].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ActivityDefinition-topic"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[4].name),
            force_bytes("topic"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[4].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[5].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-version"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[5].name),
            force_bytes("version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[5].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[6].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-composed-of"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[6].name),
            force_bytes("composed-of"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[6].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[7].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-depends-on"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[7].name),
            force_bytes("depends-on"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[7].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[8].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-derived-from"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[8].name),
            force_bytes("derived-from"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[8].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[9].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-predecessor"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[9].name),
            force_bytes("predecessor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[9].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].type),
            force_bytes("ActivityDefinition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[0].documentation),
            force_bytes(
                "Read allows clients to get the logical definitions of the measures"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[1].documentation),
            force_bytes(
                "Search allows clients to filter measures based on a provided search parameter"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].profile),
            force_bytes("StructureDefinition/Measure"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-description"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].name),
            force_bytes("description"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[2].name),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[2].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[3].name),
            force_bytes("title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[3].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-topic"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[4].name),
            force_bytes("topic"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[4].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[5].name),
            force_bytes("version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[5].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[6].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-composed-of"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[6].name),
            force_bytes("composed-of"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[6].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[7].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-depends-on"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[7].name),
            force_bytes("depends-on"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[7].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[8].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-derived-from"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[8].name),
            force_bytes("derived-from"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[8].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[9].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Measure-predecessor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[9].name),
            force_bytes("predecessor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[9].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].type), force_bytes("Measure")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[0].documentation),
            force_bytes(
                "Read allows clients to get the logical definitions of the measures"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[1].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[1].documentation),
            force_bytes(
                "Search allows clients to filter measures based on a provided search parameter"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].profile),
            force_bytes("StructureDefinition/Questionnaire"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Questionnaire-code"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[0].name),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[0].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Questionnaire-context"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[1].name),
            force_bytes("context"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Questionnaire-date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[2].name),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[2].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Questionnaire-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[3].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[3].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Questionnaire-publisher"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[4].name),
            force_bytes("publisher"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[4].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Questionnaire-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[5].name),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[5].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[6].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Questionnaire-title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[6].name),
            force_bytes("title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[6].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[7].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Questionnaire-version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[7].name),
            force_bytes("version"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[7].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].type), force_bytes("Questionnaire")
        )
        self.assertTrue(inst.rest[0].security.cors)
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].code),
            force_bytes("Certificates"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/restful-security-service"
            ),
        )
        self.assertEqual(
            force_bytes(inst.software.name),
            force_bytes("ACME Knowledge Repository Service"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/knowledge-repository"),
        )

    def testCapabilityStatement8(self):
        inst = self.instantiate_from("capabilitystatement-base.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CapabilityStatement instance"
        )
        self.implCapabilityStatement8(inst)

        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement8(inst2)

    def implCapabilityStatement8(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("4.0.1"))
        self.assertEqual(force_bytes(inst.format[0]), force_bytes("xml"))
        self.assertEqual(force_bytes(inst.format[1]), force_bytes("json"))
        self.assertEqual(force_bytes(inst.id), force_bytes("base"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("capability"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("Base FHIR Capability Statement (Full)")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project Team"))
        self.assertEqual(
            force_bytes(inst.rest[0].documentation),
            force_bytes("All the functionality defined in FHIR"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[0].code), force_bytes("transaction")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[1].code), force_bytes("batch")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[2].code), force_bytes("history-system")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[3].code), force_bytes("search-system")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(force_bytes(inst.rest[0].mode), force_bytes("server"))
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].definition),
            force_bytes("http://hl7.org/fhir/OperationDefinition/resource-validate"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[0].name), force_bytes("validate")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[1].definition),
            force_bytes("http://hl7.org/fhir/OperationDefinition/resource-meta"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[1].name), force_bytes("meta")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[2].definition),
            force_bytes("http://hl7.org/fhir/OperationDefinition/resource-meta-add"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[2].name), force_bytes("meta-add")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[3].definition),
            force_bytes("http://hl7.org/fhir/OperationDefinition/resource-meta-delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[3].name), force_bytes("meta-delete")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[4].definition),
            force_bytes("http://hl7.org/fhir/OperationDefinition/resource-convert"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[4].name), force_bytes("convert")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[5].definition),
            force_bytes("http://hl7.org/fhir/OperationDefinition/resource-graphql"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[5].name), force_bytes("graphql")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[6].definition),
            force_bytes("http://hl7.org/fhir/OperationDefinition/resource-graph"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[6].name), force_bytes("graph")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[7].definition),
            force_bytes(
                "http://hl7.org/fhir/OperationDefinition/activitydefinition-apply"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[7].name), force_bytes("apply")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[8].definition),
            force_bytes(
                "http://hl7.org/fhir/OperationDefinition/activitydefinition-data-requirements"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[8].name),
            force_bytes("data-requirements"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[9].definition),
            force_bytes(
                "http://hl7.org/fhir/OperationDefinition/capabilitystatement-subset"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].operation[9].name), force_bytes("subset")
        )
        self.assertTrue(inst.rest[0].resource[0].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[0].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].profile),
            force_bytes("http://hl7.org/fhir/StructureDefinition/Account"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchInclude[0]),
            force_bytes("Account.owner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchInclude[1]),
            force_bytes("Account.subject"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchInclude[2]),
            force_bytes("Account.patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-owner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].documentation),
            force_bytes("Entity managing the Account"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].name),
            force_bytes("owner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[0].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].documentation),
            force_bytes("Account number"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-period"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].documentation),
            force_bytes("Transaction window"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].name),
            force_bytes("period"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[2].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-subject"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].documentation),
            force_bytes("The entity that caused the expenses"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].name),
            force_bytes("subject"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[3].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].documentation),
            force_bytes("The entity that caused the expenses"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].name),
            force_bytes("patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[4].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-name"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].documentation),
            force_bytes("Human-readable label"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].name),
            force_bytes("name"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[5].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[6].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[6].documentation),
            force_bytes("E.g. patient, expense, depreciation"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[6].name),
            force_bytes("type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[6].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[7].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[7].documentation),
            force_bytes("active | inactive | entered-in-error | on-hold | unknown"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[7].name),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchParam[7].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchRevInclude[0]),
            force_bytes("ChargeItem.account"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchRevInclude[1]),
            force_bytes("Encounter.account"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].searchRevInclude[2]),
            force_bytes("Invoice.account"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[0].type), force_bytes("Account")
        )
        self.assertTrue(inst.rest[0].resource[1].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[1].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].profile),
            force_bytes("http://hl7.org/fhir/StructureDefinition/ActivityDefinition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchInclude[0]),
            force_bytes("ActivityDefinition.successor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchInclude[1]),
            force_bytes("ActivityDefinition.derived-from"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchInclude[2]),
            force_bytes("ActivityDefinition.predecessor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchInclude[3]),
            force_bytes("ActivityDefinition.composed-of"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchInclude[4]),
            force_bytes("ActivityDefinition.depends-on"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ActivityDefinition-date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].documentation),
            force_bytes("The activity definition publication date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].name),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[0].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-identifier"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].documentation),
            force_bytes("External identifier for the activity definition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-successor"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].documentation),
            force_bytes("What resource is being referenced"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].name),
            force_bytes("successor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[2].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-context-type-value"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].documentation),
            force_bytes(
                "A use context type and value assigned to the activity definition"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].name),
            force_bytes("context-type-value"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[3].type),
            force_bytes("composite"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-jurisdiction"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].documentation),
            force_bytes("Intended jurisdiction for the activity definition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].name),
            force_bytes("jurisdiction"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[4].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-description"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].documentation),
            force_bytes("The description of the activity definition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].name),
            force_bytes("description"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[5].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-derived-from"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].documentation),
            force_bytes("What resource is being referenced"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].name),
            force_bytes("derived-from"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[6].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[7].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-context-type"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[7].documentation),
            force_bytes("A type of use context assigned to the activity definition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[7].name),
            force_bytes("context-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[7].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[8].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/ActivityDefinition-predecessor"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[8].documentation),
            force_bytes("What resource is being referenced"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[8].name),
            force_bytes("predecessor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[8].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[9].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/ActivityDefinition-title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[9].documentation),
            force_bytes("The human-friendly name of the activity definition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[9].name),
            force_bytes("title"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchParam[9].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchRevInclude[0]),
            force_bytes("CarePlan.instantiates-canonical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchRevInclude[1]),
            force_bytes("Communication.instantiates-canonical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchRevInclude[2]),
            force_bytes("DeviceRequest.instantiates-canonical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchRevInclude[3]),
            force_bytes("FamilyMemberHistory.instantiates-canonical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchRevInclude[4]),
            force_bytes("MessageDefinition.parent"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchRevInclude[5]),
            force_bytes("NutritionOrder.instantiates-canonical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchRevInclude[6]),
            force_bytes("PlanDefinition.definition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchRevInclude[7]),
            force_bytes("Procedure.instantiates-canonical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].searchRevInclude[8]),
            force_bytes("ServiceRequest.instantiates-canonical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[1].type),
            force_bytes("ActivityDefinition"),
        )
        self.assertTrue(inst.rest[0].resource[2].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[2].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].profile),
            force_bytes("http://hl7.org/fhir/StructureDefinition/AdverseEvent"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchInclude[0]),
            force_bytes("AdverseEvent.recorder"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchInclude[1]),
            force_bytes("AdverseEvent.study"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchInclude[2]),
            force_bytes("AdverseEvent.subject"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchInclude[3]),
            force_bytes("AdverseEvent.resultingcondition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchInclude[4]),
            force_bytes("AdverseEvent.substance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchInclude[5]),
            force_bytes("AdverseEvent.location"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AdverseEvent-date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].documentation),
            force_bytes("When the event occurred"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].name),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[0].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AdverseEvent-severity"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[1].documentation),
            force_bytes("mild | moderate | severe"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[1].name),
            force_bytes("severity"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AdverseEvent-recorder"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[2].documentation),
            force_bytes("Who recorded the adverse event"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[2].name),
            force_bytes("recorder"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[2].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AdverseEvent-study"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[3].documentation),
            force_bytes("AdverseEvent.study"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[3].name),
            force_bytes("study"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[3].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AdverseEvent-actuality"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[4].documentation),
            force_bytes("actual | potential"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[4].name),
            force_bytes("actuality"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[4].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AdverseEvent-seriousness"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[5].documentation),
            force_bytes("Seriousness of the event"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[5].name),
            force_bytes("seriousness"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[5].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[6].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AdverseEvent-subject"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[6].documentation),
            force_bytes("Subject impacted by event"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[6].name),
            force_bytes("subject"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[6].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[7].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AdverseEvent-resultingcondition"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[7].documentation),
            force_bytes("Effect on the subject due to this event"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[7].name),
            force_bytes("resultingcondition"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[7].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[8].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AdverseEvent-substance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[8].documentation),
            force_bytes("Refers to the specific entity that caused the adverse event"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[8].name),
            force_bytes("substance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[8].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[9].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AdverseEvent-location"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[9].documentation),
            force_bytes("Location where adverse event occurred"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[9].name),
            force_bytes("location"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].searchParam[9].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[2].type), force_bytes("AdverseEvent")
        )
        self.assertTrue(inst.rest[0].resource[3].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[3].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].profile),
            force_bytes("http://hl7.org/fhir/StructureDefinition/AllergyIntolerance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchInclude[0]),
            force_bytes("AllergyIntolerance.recorder"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchInclude[1]),
            force_bytes("AllergyIntolerance.asserter"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchInclude[2]),
            force_bytes("AllergyIntolerance.patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-severity"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].documentation),
            force_bytes("mild | moderate | severe (of event as a whole)"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].name),
            force_bytes("severity"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[0].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/clinical-date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].documentation),
            force_bytes("Date first version of the resource instance was recorded"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].name),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[1].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/clinical-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[2].documentation),
            force_bytes("External ids for this item"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[2].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[2].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[3].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-manifestation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[3].documentation),
            force_bytes("Clinical symptoms/signs associated with the Event"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[3].name),
            force_bytes("manifestation"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[3].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[4].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-recorder"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[4].documentation),
            force_bytes("Who recorded the sensitivity"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[4].name),
            force_bytes("recorder"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[4].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/clinical-code"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[5].documentation),
            force_bytes("Code that identifies the allergy or intolerance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[5].name),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[5].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[6].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-verification-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[6].documentation),
            force_bytes("unconfirmed | confirmed | refuted | entered-in-error"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[6].name),
            force_bytes("verification-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[6].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[7].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-criticality"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[7].documentation),
            force_bytes("low | high | unable-to-assess"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[7].name),
            force_bytes("criticality"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[7].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[8].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-clinical-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[8].documentation),
            force_bytes("active | inactive | resolved"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[8].name),
            force_bytes("clinical-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[8].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[9].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/clinical-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[9].documentation),
            force_bytes("allergy | intolerance - Underlying mechanism (if known)"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[9].name),
            force_bytes("type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchParam[9].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].searchRevInclude[0]),
            force_bytes("ClinicalImpression.problem"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[3].type),
            force_bytes("AllergyIntolerance"),
        )
        self.assertTrue(inst.rest[0].resource[4].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[4].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].profile),
            force_bytes("http://hl7.org/fhir/StructureDefinition/Appointment"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchInclude[0]),
            force_bytes("Appointment.practitioner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchInclude[1]),
            force_bytes("Appointment.slot"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchInclude[2]),
            force_bytes("Appointment.actor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchInclude[3]),
            force_bytes("Appointment.based-on"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchInclude[4]),
            force_bytes("Appointment.patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchInclude[5]),
            force_bytes("Appointment.reason-reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchInclude[6]),
            force_bytes("Appointment.supporting-info"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchInclude[7]),
            force_bytes("Appointment.location"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Appointment-date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[0].documentation),
            force_bytes("Appointment date/time."),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[0].name),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[0].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Appointment-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[1].documentation),
            force_bytes("An Identifier of the Appointment"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[1].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Appointment-specialty"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[2].documentation),
            force_bytes(
                "The specialty of a practitioner that would be required to perform the service requested in this appointment"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[2].name),
            force_bytes("specialty"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[2].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[3].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/Appointment-service-category"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[3].documentation),
            force_bytes(
                "A broad categorization of the service that is to be performed during this appointment"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[3].name),
            force_bytes("service-category"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[3].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Appointment-practitioner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[4].documentation),
            force_bytes(
                "One of the individuals of the appointment is this practitioner"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[4].name),
            force_bytes("practitioner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[4].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Appointment-part-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[5].documentation),
            force_bytes(
                "The Participation status of the subject, or other participant on the appointment. Can be used to locate participants that have not responded to meeting requests."
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[5].name),
            force_bytes("part-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[5].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[6].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/Appointment-appointment-type"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[6].documentation),
            force_bytes(
                "The style of appointment or patient that has been booked in the slot (not service type)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[6].name),
            force_bytes("appointment-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[6].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[7].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Appointment-service-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[7].documentation),
            force_bytes(
                "The specific service that is to be performed during this appointment"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[7].name),
            force_bytes("service-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[7].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[8].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Appointment-slot"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[8].documentation),
            force_bytes("The slots that this appointment is filling"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[8].name),
            force_bytes("slot"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[8].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[9].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Appointment-reason-code"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[9].documentation),
            force_bytes("Coded reason this appointment is scheduled"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[9].name),
            force_bytes("reason-code"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchParam[9].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchRevInclude[0]),
            force_bytes("AppointmentResponse.appointment"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchRevInclude[1]),
            force_bytes("CarePlan.activity-reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchRevInclude[2]),
            force_bytes("Encounter.appointment"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].searchRevInclude[3]),
            force_bytes("ImagingStudy.basedon"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[4].type), force_bytes("Appointment")
        )
        self.assertTrue(inst.rest[0].resource[5].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[5].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].profile),
            force_bytes("http://hl7.org/fhir/StructureDefinition/AppointmentResponse"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchInclude[0]),
            force_bytes("AppointmentResponse.actor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchInclude[1]),
            force_bytes("AppointmentResponse.practitioner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchInclude[2]),
            force_bytes("AppointmentResponse.patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchInclude[3]),
            force_bytes("AppointmentResponse.appointment"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchInclude[4]),
            force_bytes("AppointmentResponse.location"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[0].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AppointmentResponse-actor"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[0].documentation),
            force_bytes(
                "The Person, Location/HealthcareService or Device that this appointment response replies for"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[0].name),
            force_bytes("actor"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[0].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[1].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AppointmentResponse-identifier"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[1].documentation),
            force_bytes("An Identifier in this appointment response"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[1].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[2].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AppointmentResponse-practitioner"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[2].documentation),
            force_bytes("This Response is for this Practitioner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[2].name),
            force_bytes("practitioner"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[2].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[3].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AppointmentResponse-part-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[3].documentation),
            force_bytes("The participants acceptance status for this appointment"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[3].name),
            force_bytes("part-status"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[3].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[4].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AppointmentResponse-patient"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[4].documentation),
            force_bytes("This Response is for this Patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[4].name),
            force_bytes("patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[4].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[5].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AppointmentResponse-appointment"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[5].documentation),
            force_bytes("The appointment that the response is attached to"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[5].name),
            force_bytes("appointment"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[5].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[6].definition),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/AppointmentResponse-location"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[6].documentation),
            force_bytes("This Response is for this Location"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[6].name),
            force_bytes("location"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchParam[6].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].searchRevInclude[0]),
            force_bytes("ImagingStudy.basedon"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[5].type),
            force_bytes("AppointmentResponse"),
        )
        self.assertTrue(inst.rest[0].resource[6].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[6].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].profile),
            force_bytes("http://hl7.org/fhir/StructureDefinition/AuditEvent"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchInclude[0]),
            force_bytes("AuditEvent.agent"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchInclude[1]),
            force_bytes("AuditEvent.source"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchInclude[2]),
            force_bytes("AuditEvent.patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchInclude[3]),
            force_bytes("AuditEvent.entity"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[0].documentation),
            force_bytes("Time when the event was recorded"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[0].name),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[0].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-entity-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[1].documentation),
            force_bytes("Type of entity involved"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[1].name),
            force_bytes("entity-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-agent"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[2].documentation),
            force_bytes("Identifier of who"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[2].name),
            force_bytes("agent"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[2].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-address"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[3].documentation),
            force_bytes("Identifier for the network access point of the user device"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[3].name),
            force_bytes("address"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[3].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-entity-role"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[4].documentation),
            force_bytes("What role the entity played"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[4].name),
            force_bytes("entity-role"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[4].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-source"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[5].documentation),
            force_bytes("The identity of source detecting the event"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[5].name),
            force_bytes("source"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[5].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[6].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[6].documentation),
            force_bytes("Type/identifier of event"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[6].name),
            force_bytes("type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[6].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[7].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-altid"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[7].documentation),
            force_bytes("Alternative User identity"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[7].name),
            force_bytes("altid"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[7].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[8].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-site"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[8].documentation),
            force_bytes("Logical source location within the enterprise"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[8].name),
            force_bytes("site"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[8].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[9].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/AuditEvent-agent-name"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[9].documentation),
            force_bytes("Human friendly name for the agent"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[9].name),
            force_bytes("agent-name"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].searchParam[9].type),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[6].type), force_bytes("AuditEvent")
        )
        self.assertTrue(inst.rest[0].resource[7].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[7].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].profile),
            force_bytes("http://hl7.org/fhir/StructureDefinition/Basic"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchInclude[0]),
            force_bytes("Basic.subject"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchInclude[1]),
            force_bytes("Basic.patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchInclude[2]),
            force_bytes("Basic.author"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Basic-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[0].documentation),
            force_bytes("Business identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[0].name),
            force_bytes("identifier"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[0].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Basic-code"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[1].documentation),
            force_bytes("Kind of Resource"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[1].name),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[1].type),
            force_bytes("token"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Basic-subject"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[2].documentation),
            force_bytes("Identifies the focus of this resource"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[2].name),
            force_bytes("subject"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[2].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Basic-created"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[3].documentation),
            force_bytes("When created"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[3].name),
            force_bytes("created"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[3].type),
            force_bytes("date"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Basic-patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[4].documentation),
            force_bytes("Identifies the focus of this resource"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[4].name),
            force_bytes("patient"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[4].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Basic-author"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[5].documentation),
            force_bytes("Who created"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[5].name),
            force_bytes("author"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].searchParam[5].type),
            force_bytes("reference"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[7].type), force_bytes("Basic")
        )
        self.assertTrue(inst.rest[0].resource[8].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[8].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].profile),
            force_bytes("http://hl7.org/fhir/StructureDefinition/Binary"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[8].type), force_bytes("Binary")
        )
        self.assertTrue(inst.rest[0].resource[9].conditionalCreate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].conditionalDelete),
            force_bytes("multiple"),
        )
        self.assertTrue(inst.rest[0].resource[9].conditionalUpdate)
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[0].code),
            force_bytes("read"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[0].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[1].code),
            force_bytes("vread"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[1].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[2].code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[2].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[3].code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[3].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[4].code),
            force_bytes("history-instance"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[4].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[5].code),
            force_bytes("history-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[5].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[6].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[6].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[7].code),
            force_bytes("search-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].interaction[7].documentation),
            force_bytes(
                "Implemented per the specification (or Insert other doco here)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].profile),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].referencePolicy[0]),
            force_bytes("literal"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].referencePolicy[1]),
            force_bytes("logical"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].resource[9].type),
            force_bytes("BiologicallyDerivedProduct"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[0].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/DomainResource-text"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[0].documentation),
            force_bytes("Search on the narrative of the resource"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[0].name), force_bytes("_text")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[0].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[1].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/id"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[1].documentation),
            force_bytes("some doco"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[1].name), force_bytes("something")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[2].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-list"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[2].documentation),
            force_bytes(
                "Retrieval of resources that are referenced by a List resource"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[2].name), force_bytes("_list")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[2].type), force_bytes("token")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[3].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-has"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[3].documentation),
            force_bytes("Provides support for reverse chaining"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[3].name), force_bytes("_has")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[3].type), force_bytes("composite")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[4].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-type"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[4].documentation),
            force_bytes("Type of resource (when doing cross-resource search"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[4].name), force_bytes("_type")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[4].type), force_bytes("token")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[5].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-source"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[5].documentation),
            force_bytes("How to sort the resources when returning"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[5].name), force_bytes("_sort")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[5].type), force_bytes("token")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[6].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-count"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[6].documentation),
            force_bytes("How many resources to return"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[6].name), force_bytes("_count")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[6].type), force_bytes("number")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[7].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-include"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[7].documentation),
            force_bytes("Control over returning additional resources (see spec)"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[7].name), force_bytes("_include")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[7].type), force_bytes("token")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[8].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-revinclude"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[8].documentation),
            force_bytes("Control over returning additional resources (see spec)"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[8].name), force_bytes("_revinclude")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[8].type), force_bytes("token")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[9].definition),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-summary"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[9].documentation),
            force_bytes("What kind of information to return"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[9].name), force_bytes("_summary")
        )
        self.assertEqual(
            force_bytes(inst.rest[0].searchParam[9].type), force_bytes("token")
        )
        self.assertTrue(inst.rest[0].security.cors)
        self.assertEqual(
            force_bytes(inst.rest[0].security.description),
            force_bytes(
                "This is the Capability Statement to declare that the server supports SMART-on-FHIR. See the SMART-on-FHIR docs for the extension that would go with such a server"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].code),
            force_bytes("SMART-on-FHIR"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].display),
            force_bytes("SMART-on-FHIR"),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/restful-security-service"
            ),
        )
        self.assertEqual(
            force_bytes(inst.rest[0].security.service[0].text),
            force_bytes("See http://docs.smarthealthit.org/"),
        )
        self.assertEqual(
            force_bytes(inst.software.name),
            force_bytes("Insert your software name here..."),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/CapabilityStatement/base"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))
