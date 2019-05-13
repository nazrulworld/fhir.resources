#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import compartmentdefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class CompartmentDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CompartmentDefinition", js["resourceType"])
        return compartmentdefinition.CompartmentDefinition(js)
    
    def testCompartmentDefinition1(self):
        inst = self.instantiate_from("compartmentdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CompartmentDefinition instance")
        self.implCompartmentDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("CompartmentDefinition", js["resourceType"])
        inst2 = compartmentdefinition.CompartmentDefinition(js)
        self.implCompartmentDefinition1(inst2)
    
    def implCompartmentDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("Device"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("[string]"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(inst.date.date, FHIRDate("2017-02-24").date)
        self.assertEqual(inst.date.as_json(), "2017-02-24")
        self.assertEqual(force_bytes(inst.description), force_bytes("The set of resources associated with a particular Device (example with Communication and CommunicationRequest resourses only)."))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.name), force_bytes("EXAMPLE"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Health Level Seven International (FHIR Infrastructure)"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Provides an example of a FHIR compartment definition based on the Device resource type."))
        self.assertEqual(force_bytes(inst.resource[0].code), force_bytes("Communication"))
        self.assertEqual(force_bytes(inst.resource[0].documentation), force_bytes("The device used as the message sender and recipient"))
        self.assertEqual(force_bytes(inst.resource[0].param[0]), force_bytes("sender"))
        self.assertEqual(force_bytes(inst.resource[0].param[1]), force_bytes("recipient"))
        self.assertEqual(force_bytes(inst.resource[1].code), force_bytes("CommunicationRequest"))
        self.assertEqual(force_bytes(inst.resource[1].documentation), force_bytes("The device used as the message sender and recipient"))
        self.assertEqual(force_bytes(inst.resource[1].param[0]), force_bytes("sender"))
        self.assertEqual(force_bytes(inst.resource[1].param[1]), force_bytes("recipient"))
        self.assertTrue(inst.search)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/CompartmentDefinition/example"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("Device"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("http://hl7.org/fhir/resource-types"))

