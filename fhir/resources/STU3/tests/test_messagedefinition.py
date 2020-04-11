# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import messagedefinition
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MessageDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("MessageDefinition", js["resourceType"])
        return messagedefinition.MessageDefinition(js)

    def testMessageDefinition1(self):
        inst = self.instantiate_from("messagedefinition-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MessageDefinition instance"
        )
        self.implMessageDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("MessageDefinition", js["resourceType"])
        inst2 = messagedefinition.MessageDefinition(js)
        self.implMessageDefinition1(inst2)

    def implMessageDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.category), force_bytes("Notification"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org")
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-11-09").date)
        self.assertEqual(inst.date.as_json(), "2016-11-09")
        self.assertEqual(
            force_bytes(inst.event.code), force_bytes("communication-request")
        )
        self.assertEqual(
            force_bytes(inst.event.system),
            force_bytes("http://hl7.org/fhir/message-events"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.name), force_bytes("EXAMPLE"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Health Level Seven, Int'l")
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes("Defines a base example for other MessageDefintion instances."),
        )
        self.assertFalse(inst.responseRequired)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Message definition base example</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Message definition base example")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/MessageDefinition/example"),
        )

    def testMessageDefinition2(self):
        inst = self.instantiate_from("messagedefinition-patient-link-notification.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MessageDefinition instance"
        )
        self.implMessageDefinition2(inst)

        js = inst.as_json()
        self.assertEqual("MessageDefinition", js["resourceType"])
        inst2 = messagedefinition.MessageDefinition(js)
        self.implMessageDefinition2(inst2)

    def implMessageDefinition2(self, inst):
        self.assertEqual(
            force_bytes(inst.allowedResponse[0].situation),
            force_bytes(
                "Optional response message that may provide additional information"
            ),
        )
        self.assertEqual(force_bytes(inst.category), force_bytes("Notification"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org")
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("� HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-02-03").date)
        self.assertEqual(inst.date.as_json(), "2017-02-03")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Notification of two patient records that represent the same individual that require an established linkage."
            ),
        )
        self.assertEqual(force_bytes(inst.event.code), force_bytes("patient-link"))
        self.assertEqual(
            force_bytes(inst.event.system),
            force_bytes("http://hl7.org/fhir/message-events"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.focus[0].code), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.focus[0].max), force_bytes("2"))
        self.assertEqual(inst.focus[0].min, 2)
        self.assertEqual(force_bytes(inst.id), force_bytes("patient-link-notification"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9878"),
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
        self.assertEqual(
            force_bytes(inst.name), force_bytes("PATIENT-LINK-NOTIFICATION")
        )
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Health Level Seven, Int'l")
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "Notifies recipient systems that two patients have been 'linked' - meaning they represent the same individual"
            ),
        )
        self.assertFalse(inst.responseRequired)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Link Patients Notification</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Link Patients Notification")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/MessageDefinition/patient-link-notification"
            ),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("positive"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://hl7.org/fhir/variant-state"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1"))

    def testMessageDefinition3(self):
        inst = self.instantiate_from("messagedefinition-patient-link-response.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MessageDefinition instance"
        )
        self.implMessageDefinition3(inst)

        js = inst.as_json()
        self.assertEqual("MessageDefinition", js["resourceType"])
        inst2 = messagedefinition.MessageDefinition(js)
        self.implMessageDefinition3(inst2)

    def implMessageDefinition3(self, inst):
        self.assertEqual(force_bytes(inst.category), force_bytes("Consequence"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org")
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("� HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-02-03").date)
        self.assertEqual(inst.date.as_json(), "2017-02-03")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Optional response to a patient link notification."),
        )
        self.assertEqual(force_bytes(inst.event.code), force_bytes("patient-link"))
        self.assertEqual(
            force_bytes(inst.event.system),
            force_bytes("http://hl7.org/fhir/message-events"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.focus[0].code), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.focus[0].max), force_bytes("2"))
        self.assertEqual(inst.focus[0].min, 2)
        self.assertEqual(force_bytes(inst.id), force_bytes("patient-link-response"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9879"),
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
        self.assertEqual(force_bytes(inst.name), force_bytes("PATIENT-LINK-RESPONSE"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Health Level Seven, Int'l")
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "Optional response message that may provide additional information on the outcome of the patient link operation."
            ),
        )
        self.assertFalse(inst.responseRequired)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Link Patients Response</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Link Patients Response"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/MessageDefinition/patient-link-response"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("positive"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://hl7.org/fhir/variant-state"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1"))
