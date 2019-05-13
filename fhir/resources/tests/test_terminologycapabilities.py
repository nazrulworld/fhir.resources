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
from .. import terminologycapabilities
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class TerminologyCapabilitiesTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("TerminologyCapabilities", js["resourceType"])
        return terminologycapabilities.TerminologyCapabilities(js)
    
    def testTerminologyCapabilities1(self):
        inst = self.instantiate_from("terminologycapabilities-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a TerminologyCapabilities instance")
        self.implTerminologyCapabilities1(inst)
        
        js = inst.as_json()
        self.assertEqual("TerminologyCapabilities", js["resourceType"])
        inst2 = terminologycapabilities.TerminologyCapabilities(js)
        self.implTerminologyCapabilities1(inst2)
    
    def implTerminologyCapabilities1(self, inst):
        self.assertEqual(force_bytes(inst.codeSearch), force_bytes("explicit"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("System Administrator"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("wile@acme.org"))
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.date.as_json(), "2012-01-04")
        self.assertEqual(force_bytes(inst.description), force_bytes("This is the FHIR capability statement for the main EHR at ACME for the private interface - it does not describe the public interface"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.implementation.description), force_bytes("Acme Terminology Server"))
        self.assertEqual(force_bytes(inst.implementation.url), force_bytes("http://example.org/tx"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("instance"))
        self.assertEqual(force_bytes(inst.name), force_bytes("ACME-EHR"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("ACME Corporation"))
        self.assertEqual(force_bytes(inst.software.name), force_bytes("TxServer"))
        self.assertEqual(force_bytes(inst.software.version), force_bytes("0.1.2"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("ACME EHR capability statement"))
        self.assertEqual(force_bytes(inst.url), force_bytes("urn:uuid:68D043B5-9ECF-4559-A57A-396E0D452311"))
        self.assertEqual(force_bytes(inst.version), force_bytes("20130510"))

