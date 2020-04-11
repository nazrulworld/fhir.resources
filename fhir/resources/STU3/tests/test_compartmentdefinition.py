# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CompartmentDefinition
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

from .. import compartmentdefinition
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class CompartmentDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("CompartmentDefinition", js["resourceType"])
        return compartmentdefinition.CompartmentDefinition(js)

    def testCompartmentDefinition1(self):
        inst = self.instantiate_from("compartmentdefinition-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CompartmentDefinition instance"
        )
        self.implCompartmentDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("CompartmentDefinition", js["resourceType"])
        inst2 = compartmentdefinition.CompartmentDefinition(js)
        self.implCompartmentDefinition1(inst2)

    def implCompartmentDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("Device"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("[string]"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-02-24").date)
        self.assertEqual(inst.date.as_json(), "2017-02-24")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "The set of resources associated with a particular Device (example with Communication and CommunicationRequest resourses only)."
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
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
        self.assertEqual(force_bytes(inst.name), force_bytes("EXAMPLE"))
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (FHIR Infrastructure)"),
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "Provides an example of a FHIR compartment definition based on the Device resource type."
            ),
        )
        self.assertEqual(
            force_bytes(inst.resource[0].code), force_bytes("Communication")
        )
        self.assertEqual(
            force_bytes(inst.resource[0].documentation),
            force_bytes("The device used as the message sender and recipient"),
        )
        self.assertEqual(force_bytes(inst.resource[0].param[0]), force_bytes("sender"))
        self.assertEqual(
            force_bytes(inst.resource[0].param[1]), force_bytes("recipient")
        )
        self.assertEqual(
            force_bytes(inst.resource[1].code), force_bytes("CommunicationRequest")
        )
        self.assertEqual(
            force_bytes(inst.resource[1].documentation),
            force_bytes("The device used as the message sender and recipient"),
        )
        self.assertEqual(force_bytes(inst.resource[1].param[0]), force_bytes("sender"))
        self.assertEqual(
            force_bytes(inst.resource[1].param[1]), force_bytes("recipient")
        )
        self.assertTrue(inst.search)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Base FHIR compartment definition for Device(example)"),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/CompartmentDefinition/example"),
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
            force_bytes("Device"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://hl7.org/fhir/resource-types"),
        )

    def testCompartmentDefinition2(self):
        inst = self.instantiate_from("compartmentdefinition-relatedperson.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CompartmentDefinition instance"
        )
        self.implCompartmentDefinition2(inst)

        js = inst.as_json()
        self.assertEqual("CompartmentDefinition", js["resourceType"])
        inst2 = compartmentdefinition.CompartmentDefinition(js)
        self.implCompartmentDefinition2(inst2)

    def implCompartmentDefinition2(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("RelatedPerson"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("relatedPerson"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Base FHIR compartment definition for RelatedPerson"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project Team"))
        self.assertEqual(force_bytes(inst.resource[0].code), force_bytes("Account"))
        self.assertEqual(
            force_bytes(inst.resource[1].code), force_bytes("ActivityDefinition")
        )
        self.assertEqual(
            force_bytes(inst.resource[2].code), force_bytes("AdverseEvent")
        )
        self.assertEqual(
            force_bytes(inst.resource[2].param[0]), force_bytes("recorder")
        )
        self.assertEqual(
            force_bytes(inst.resource[3].code), force_bytes("AllergyIntolerance")
        )
        self.assertEqual(
            force_bytes(inst.resource[3].param[0]), force_bytes("asserter")
        )
        self.assertEqual(force_bytes(inst.resource[4].code), force_bytes("Appointment"))
        self.assertEqual(force_bytes(inst.resource[4].param[0]), force_bytes("actor"))
        self.assertEqual(
            force_bytes(inst.resource[5].code), force_bytes("AppointmentResponse")
        )
        self.assertEqual(force_bytes(inst.resource[5].param[0]), force_bytes("actor"))
        self.assertEqual(force_bytes(inst.resource[6].code), force_bytes("AuditEvent"))
        self.assertEqual(force_bytes(inst.resource[7].code), force_bytes("Basic"))
        self.assertEqual(force_bytes(inst.resource[7].param[0]), force_bytes("author"))
        self.assertEqual(force_bytes(inst.resource[8].code), force_bytes("Binary"))
        self.assertEqual(force_bytes(inst.resource[9].code), force_bytes("BodySite"))
        self.assertTrue(inst.search)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/CompartmentDefinition/relatedPerson"),
        )

    def testCompartmentDefinition3(self):
        inst = self.instantiate_from("compartmentdefinition-patient.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CompartmentDefinition instance"
        )
        self.implCompartmentDefinition3(inst)

        js = inst.as_json()
        self.assertEqual("CompartmentDefinition", js["resourceType"])
        inst2 = compartmentdefinition.CompartmentDefinition(js)
        self.implCompartmentDefinition3(inst2)

    def implCompartmentDefinition3(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("Patient"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("patient"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Base FHIR compartment definition for Patient"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project Team"))
        self.assertEqual(force_bytes(inst.resource[0].code), force_bytes("Account"))
        self.assertEqual(force_bytes(inst.resource[0].param[0]), force_bytes("subject"))
        self.assertEqual(
            force_bytes(inst.resource[1].code), force_bytes("ActivityDefinition")
        )
        self.assertEqual(
            force_bytes(inst.resource[2].code), force_bytes("AdverseEvent")
        )
        self.assertEqual(force_bytes(inst.resource[2].param[0]), force_bytes("subject"))
        self.assertEqual(
            force_bytes(inst.resource[3].code), force_bytes("AllergyIntolerance")
        )
        self.assertEqual(force_bytes(inst.resource[3].param[0]), force_bytes("patient"))
        self.assertEqual(
            force_bytes(inst.resource[3].param[1]), force_bytes("recorder")
        )
        self.assertEqual(
            force_bytes(inst.resource[3].param[2]), force_bytes("asserter")
        )
        self.assertEqual(force_bytes(inst.resource[4].code), force_bytes("Appointment"))
        self.assertEqual(force_bytes(inst.resource[4].param[0]), force_bytes("actor"))
        self.assertEqual(
            force_bytes(inst.resource[5].code), force_bytes("AppointmentResponse")
        )
        self.assertEqual(force_bytes(inst.resource[5].param[0]), force_bytes("actor"))
        self.assertEqual(force_bytes(inst.resource[6].code), force_bytes("AuditEvent"))
        self.assertEqual(force_bytes(inst.resource[6].param[0]), force_bytes("patient"))
        self.assertEqual(
            force_bytes(inst.resource[6].param[1]), force_bytes("agent.patient")
        )
        self.assertEqual(
            force_bytes(inst.resource[6].param[2]), force_bytes("entity.patient")
        )
        self.assertEqual(force_bytes(inst.resource[7].code), force_bytes("Basic"))
        self.assertEqual(force_bytes(inst.resource[7].param[0]), force_bytes("patient"))
        self.assertEqual(force_bytes(inst.resource[7].param[1]), force_bytes("author"))
        self.assertEqual(force_bytes(inst.resource[8].code), force_bytes("Binary"))
        self.assertEqual(force_bytes(inst.resource[9].code), force_bytes("BodySite"))
        self.assertEqual(force_bytes(inst.resource[9].param[0]), force_bytes("patient"))
        self.assertTrue(inst.search)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/CompartmentDefinition/patient"),
        )

    def testCompartmentDefinition4(self):
        inst = self.instantiate_from("compartmentdefinition-practitioner.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CompartmentDefinition instance"
        )
        self.implCompartmentDefinition4(inst)

        js = inst.as_json()
        self.assertEqual("CompartmentDefinition", js["resourceType"])
        inst2 = compartmentdefinition.CompartmentDefinition(js)
        self.implCompartmentDefinition4(inst2)

    def implCompartmentDefinition4(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("Practitioner"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("practitioner"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Base FHIR compartment definition for Practitioner"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project Team"))
        self.assertEqual(force_bytes(inst.resource[0].code), force_bytes("Account"))
        self.assertEqual(force_bytes(inst.resource[0].param[0]), force_bytes("subject"))
        self.assertEqual(
            force_bytes(inst.resource[1].code), force_bytes("ActivityDefinition")
        )
        self.assertEqual(
            force_bytes(inst.resource[2].code), force_bytes("AdverseEvent")
        )
        self.assertEqual(
            force_bytes(inst.resource[2].param[0]), force_bytes("recorder")
        )
        self.assertEqual(
            force_bytes(inst.resource[3].code), force_bytes("AllergyIntolerance")
        )
        self.assertEqual(
            force_bytes(inst.resource[3].param[0]), force_bytes("recorder")
        )
        self.assertEqual(
            force_bytes(inst.resource[3].param[1]), force_bytes("asserter")
        )
        self.assertEqual(force_bytes(inst.resource[4].code), force_bytes("Appointment"))
        self.assertEqual(force_bytes(inst.resource[4].param[0]), force_bytes("actor"))
        self.assertEqual(
            force_bytes(inst.resource[5].code), force_bytes("AppointmentResponse")
        )
        self.assertEqual(force_bytes(inst.resource[5].param[0]), force_bytes("actor"))
        self.assertEqual(force_bytes(inst.resource[6].code), force_bytes("AuditEvent"))
        self.assertEqual(force_bytes(inst.resource[6].param[0]), force_bytes("agent"))
        self.assertEqual(force_bytes(inst.resource[7].code), force_bytes("Basic"))
        self.assertEqual(force_bytes(inst.resource[7].param[0]), force_bytes("author"))
        self.assertEqual(force_bytes(inst.resource[8].code), force_bytes("Binary"))
        self.assertEqual(force_bytes(inst.resource[9].code), force_bytes("BodySite"))
        self.assertTrue(inst.search)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/CompartmentDefinition/practitioner"),
        )

    def testCompartmentDefinition5(self):
        inst = self.instantiate_from("compartmentdefinition-encounter.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CompartmentDefinition instance"
        )
        self.implCompartmentDefinition5(inst)

        js = inst.as_json()
        self.assertEqual("CompartmentDefinition", js["resourceType"])
        inst2 = compartmentdefinition.CompartmentDefinition(js)
        self.implCompartmentDefinition5(inst2)

    def implCompartmentDefinition5(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("Encounter"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("encounter"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Base FHIR compartment definition for Encounter"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project Team"))
        self.assertEqual(force_bytes(inst.resource[0].code), force_bytes("Account"))
        self.assertEqual(
            force_bytes(inst.resource[1].code), force_bytes("ActivityDefinition")
        )
        self.assertEqual(
            force_bytes(inst.resource[2].code), force_bytes("AdverseEvent")
        )
        self.assertEqual(
            force_bytes(inst.resource[3].code), force_bytes("AllergyIntolerance")
        )
        self.assertEqual(force_bytes(inst.resource[4].code), force_bytes("Appointment"))
        self.assertEqual(
            force_bytes(inst.resource[5].code), force_bytes("AppointmentResponse")
        )
        self.assertEqual(force_bytes(inst.resource[6].code), force_bytes("AuditEvent"))
        self.assertEqual(force_bytes(inst.resource[7].code), force_bytes("Basic"))
        self.assertEqual(force_bytes(inst.resource[8].code), force_bytes("Binary"))
        self.assertEqual(force_bytes(inst.resource[9].code), force_bytes("BodySite"))
        self.assertTrue(inst.search)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/CompartmentDefinition/encounter"),
        )

    def testCompartmentDefinition6(self):
        inst = self.instantiate_from("compartmentdefinition-device.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CompartmentDefinition instance"
        )
        self.implCompartmentDefinition6(inst)

        js = inst.as_json()
        self.assertEqual("CompartmentDefinition", js["resourceType"])
        inst2 = compartmentdefinition.CompartmentDefinition(js)
        self.implCompartmentDefinition6(inst2)

    def implCompartmentDefinition6(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("Device"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "There is an instance of the practitioner compartment for each Device resource, and the identity of the compartment is the same as the Device. The set of resources associated with a particular device"
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("device"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Base FHIR compartment definition for Device"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project Team"))
        self.assertEqual(force_bytes(inst.resource[0].code), force_bytes("Account"))
        self.assertEqual(force_bytes(inst.resource[0].param[0]), force_bytes("subject"))
        self.assertEqual(
            force_bytes(inst.resource[1].code), force_bytes("ActivityDefinition")
        )
        self.assertEqual(
            force_bytes(inst.resource[2].code), force_bytes("AdverseEvent")
        )
        self.assertEqual(
            force_bytes(inst.resource[3].code), force_bytes("AllergyIntolerance")
        )
        self.assertEqual(force_bytes(inst.resource[4].code), force_bytes("Appointment"))
        self.assertEqual(force_bytes(inst.resource[4].param[0]), force_bytes("actor"))
        self.assertEqual(
            force_bytes(inst.resource[5].code), force_bytes("AppointmentResponse")
        )
        self.assertEqual(force_bytes(inst.resource[5].param[0]), force_bytes("actor"))
        self.assertEqual(force_bytes(inst.resource[6].code), force_bytes("AuditEvent"))
        self.assertEqual(force_bytes(inst.resource[6].param[0]), force_bytes("agent"))
        self.assertEqual(force_bytes(inst.resource[7].code), force_bytes("Basic"))
        self.assertEqual(force_bytes(inst.resource[8].code), force_bytes("Binary"))
        self.assertEqual(force_bytes(inst.resource[9].code), force_bytes("BodySite"))
        self.assertTrue(inst.search)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/CompartmentDefinition/device"),
        )
