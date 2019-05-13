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
from .. import eligibilityrequest
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class EligibilityRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EligibilityRequest", js["resourceType"])
        return eligibilityrequest.EligibilityRequest(js)
    
    def testEligibilityRequest1(self):
        inst = self.instantiate_from("eligibilityrequest-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityRequest instance")
        self.implEligibilityRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityRequest", js["resourceType"])
        inst2 = eligibilityrequest.EligibilityRequest(js)
        self.implEligibilityRequest1(inst2)
    
    def implEligibilityRequest1(self, inst):
        self.assertEqual(force_bytes(inst.benefitCategory.coding[0].code), force_bytes("medical"))
        self.assertEqual(force_bytes(inst.benefitCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.benefitSubCategory.coding[0].code), force_bytes("69"))
        self.assertEqual(force_bytes(inst.benefitSubCategory.coding[0].display), force_bytes("Maternity"))
        self.assertEqual(force_bytes(inst.benefitSubCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.businessArrangement), force_bytes("NB8742"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("52346"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/elegibilityrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("52346"))
        self.assertEqual(force_bytes(inst.priority.coding[0].code), force_bytes("normal"))
        self.assertEqual(inst.servicedDate.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.servicedDate.as_json(), "2014-09-17")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testEligibilityRequest2(self):
        inst = self.instantiate_from("eligibilityrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityRequest instance")
        self.implEligibilityRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityRequest", js["resourceType"])
        inst2 = eligibilityrequest.EligibilityRequest(js)
        self.implEligibilityRequest2(inst2)
    
    def implEligibilityRequest2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("52345"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/elegibilityrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("52345"))
        self.assertEqual(force_bytes(inst.priority.coding[0].code), force_bytes("normal"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

