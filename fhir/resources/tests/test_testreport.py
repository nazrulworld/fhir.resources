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
from .. import testreport
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class TestReportTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("TestReport", js["resourceType"])
        return testreport.TestReport(js)
    
    def testTestReport1(self):
        inst = self.instantiate_from("testreport-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestReport instance")
        self.implTestReport1(inst)
        
        js = inst.as_json()
        self.assertEqual("TestReport", js["resourceType"])
        inst2 = testreport.TestReport(js)
        self.implTestReport1(inst2)
    
    def implTestReport1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("testreport-example"))
        self.assertEqual(force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9878"))
        self.assertEqual(inst.issued.date, FHIRDate("2016-10-07T08:25:34-05:00").date)
        self.assertEqual(inst.issued.as_json(), "2016-10-07T08:25:34-05:00")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("TestReport Example for TestScript Example"))
        self.assertEqual(force_bytes(inst.participant[0].display), force_bytes("Crucible"))
        self.assertEqual(force_bytes(inst.participant[0].type), force_bytes("test-engine"))
        self.assertEqual(force_bytes(inst.participant[0].uri), force_bytes("http://projectcrucible.org"))
        self.assertEqual(force_bytes(inst.participant[1].display), force_bytes("HealthIntersections STU3"))
        self.assertEqual(force_bytes(inst.participant[1].type), force_bytes("server"))
        self.assertEqual(force_bytes(inst.participant[1].uri), force_bytes("http://fhir3.healthintersections.com.au/open"))
        self.assertEqual(force_bytes(inst.result), force_bytes("pass"))
        self.assertEqual(inst.score, 100.0)
        self.assertEqual(force_bytes(inst.setup.action[0].operation.detail), force_bytes("http://projectcrucible.org/permalink/1"))
        self.assertEqual(force_bytes(inst.setup.action[0].operation.message), force_bytes("DELETE Patient"))
        self.assertEqual(force_bytes(inst.setup.action[0].operation.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.setup.action[1].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/1"))
        self.assertEqual(force_bytes(inst.setup.action[1].assert_fhir.message), force_bytes("HTTP 204"))
        self.assertEqual(force_bytes(inst.setup.action[1].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.setup.action[2].operation.detail), force_bytes("http://projectcrucible.org/permalink/1"))
        self.assertEqual(force_bytes(inst.setup.action[2].operation.message), force_bytes("POST Patient/fixture-patient-create"))
        self.assertEqual(force_bytes(inst.setup.action[2].operation.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.setup.action[3].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/1"))
        self.assertEqual(force_bytes(inst.setup.action[3].assert_fhir.message), force_bytes("HTTP 201"))
        self.assertEqual(force_bytes(inst.setup.action[3].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.teardown.action[0].operation.detail), force_bytes("http://projectcrucible.org/permalink/3"))
        self.assertEqual(force_bytes(inst.teardown.action[0].operation.message), force_bytes("DELETE Patient/fixture-patient-create."))
        self.assertEqual(force_bytes(inst.teardown.action[0].operation.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[0].operation.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[0].operation.message), force_bytes("GET Patient/fixture-patient-create"))
        self.assertEqual(force_bytes(inst.test[0].action[0].operation.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[1].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[1].assert_fhir.message), force_bytes("HTTP 200"))
        self.assertEqual(force_bytes(inst.test[0].action[1].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[2].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[2].assert_fhir.message), force_bytes("Last-Modified Present"))
        self.assertEqual(force_bytes(inst.test[0].action[2].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[3].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[3].assert_fhir.message), force_bytes("Response is Patient"))
        self.assertEqual(force_bytes(inst.test[0].action[3].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[4].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[4].assert_fhir.message), force_bytes("Response validates"))
        self.assertEqual(force_bytes(inst.test[0].action[4].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[5].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[5].assert_fhir.message), force_bytes("Patient.name.family 'Chalmers'"))
        self.assertEqual(force_bytes(inst.test[0].action[5].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[6].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[6].assert_fhir.message), force_bytes("Patient.name.given 'Peter'"))
        self.assertEqual(force_bytes(inst.test[0].action[6].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[7].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[7].assert_fhir.message), force_bytes("Patient.name.family 'Chalmers'"))
        self.assertEqual(force_bytes(inst.test[0].action[7].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[8].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[8].assert_fhir.message), force_bytes("Patient.name.family 'Chalmers'"))
        self.assertEqual(force_bytes(inst.test[0].action[8].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].action[9].assert_fhir.detail), force_bytes("http://projectcrucible.org/permalink/2"))
        self.assertEqual(force_bytes(inst.test[0].action[9].assert_fhir.message), force_bytes("Patient expected values."))
        self.assertEqual(force_bytes(inst.test[0].action[9].assert_fhir.result), force_bytes("pass"))
        self.assertEqual(force_bytes(inst.test[0].description), force_bytes("Read a Patient and validate response."))
        self.assertEqual(force_bytes(inst.test[0].id), force_bytes("01-ReadPatient"))
        self.assertEqual(force_bytes(inst.test[0].name), force_bytes("Read Patient"))
        self.assertEqual(force_bytes(inst.tester), force_bytes("HL7 Execution Engine"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

