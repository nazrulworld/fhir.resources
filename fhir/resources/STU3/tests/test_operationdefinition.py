#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import operationdefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class OperationDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OperationDefinition", js["resourceType"])
        return operationdefinition.OperationDefinition(js)
    
    def testOperationDefinition1(self):
        inst = self.instantiate_from("operationdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationDefinition instance")
        self.implOperationDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition1(inst2)
    
    def implOperationDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("populate"))
        self.assertEqual(force_bytes(inst.comment), force_bytes("Only implemented for Labs and Medications so far"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("System Administrator"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("beep@coyote.acme.com"))
        self.assertEqual(inst.date.date, FHIRDate("2015-08-04").date)
        self.assertEqual(inst.date.as_json(), "2015-08-04")
        self.assertEqual(force_bytes(inst.description), force_bytes("Limited implementation of the Populate Questionnaire implemenation"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("GB"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].display), force_bytes("United Kingdom of Great Britain and Northern Ireland (the)"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Populate Questionnaire"))
        self.assertEqual(force_bytes(inst.overload[0].parameterName[0]), force_bytes("subject"))
        self.assertEqual(force_bytes(inst.overload[0].parameterName[1]), force_bytes("local"))
        self.assertEqual(force_bytes(inst.overload[1].comment), force_bytes("local defaults to false when not passed as a parameter"))
        self.assertEqual(force_bytes(inst.overload[1].parameterName[0]), force_bytes("subject"))
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("subject"))
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[1].documentation), force_bytes("If the *local* parameter is set to true, server information about the specified subject will be used to populate the instance."))
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 0)
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("local"))
        self.assertEqual(force_bytes(inst.parameter[1].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[2].documentation), force_bytes("The partially (or fully)-populated set of answers for the specified Questionnaire"))
        self.assertEqual(force_bytes(inst.parameter[2].max), force_bytes("1"))
        self.assertEqual(inst.parameter[2].min, 1)
        self.assertEqual(force_bytes(inst.parameter[2].name), force_bytes("return"))
        self.assertEqual(force_bytes(inst.parameter[2].type), force_bytes("QuestionnaireResponse"))
        self.assertEqual(force_bytes(inst.parameter[2].use), force_bytes("out"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Acme Healthcare Services"))
        self.assertEqual(force_bytes(inst.resource[0]), force_bytes("Questionnaire"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertFalse(inst.type)
        self.assertEqual(force_bytes(inst.url), force_bytes("http://h7.org/fhir/OperationDefinition/example"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("venue"))
        self.assertEqual(force_bytes(inst.useContext[0].code.display), force_bytes("Clinical Venue"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://build.fhir.org/codesystem-usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("IMP"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display), force_bytes("inpatient encounter"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.version), force_bytes("B"))

