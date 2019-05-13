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
from .. import servicedefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ServiceDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ServiceDefinition", js["resourceType"])
        return servicedefinition.ServiceDefinition(js)
    
    def testServiceDefinition1(self):
        inst = self.instantiate_from("servicedefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceDefinition instance")
        self.implServiceDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceDefinition", js["resourceType"])
        inst2 = servicedefinition.ServiceDefinition(js)
        self.implServiceDefinition1(inst2)
    
    def implServiceDefinition1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(force_bytes(inst.description), force_bytes("Guideline appropriate ordering is used to assess appropriateness of an order given a patient, a proposed order, and a set of clinical indications."))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("guildeline-appropriate-ordering"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Guideline Appropriate Ordering Module"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("Guideline Appropriate Ordering"))
        self.assertEqual(force_bytes(inst.topic[1].text), force_bytes("Appropriate Use Criteria"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

