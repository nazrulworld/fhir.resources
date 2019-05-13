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
from .. import observationdefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ObservationDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ObservationDefinition", js["resourceType"])
        return observationdefinition.ObservationDefinition(js)
    
    def testObservationDefinition1(self):
        inst = self.instantiate_from("observationdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ObservationDefinition instance")
        self.implObservationDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ObservationDefinition", js["resourceType"])
        inst2 = observationdefinition.ObservationDefinition(js)
        self.implObservationDefinition1(inst2)
    
    def implObservationDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("15074-8"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Glucose [Moles/volume] in Blood"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

