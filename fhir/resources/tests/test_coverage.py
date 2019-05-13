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
from .. import coverage
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class CoverageTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Coverage", js["resourceType"])
        return coverage.Coverage(js)
    
    def testCoverage1(self):
        inst = self.instantiate_from("coverage-example-selfpay.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage1(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage1(inst2)
    
    def implCoverage1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("SP1234"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://hospitalx.com/selfpayagreement"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("SP12345678"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-17").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(force_bytes(inst.relationship.coding[0].code), force_bytes("self"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of a Self Pay Agreement.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("pay"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("PAY"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-selfpay"))
    
    def testCoverage2(self):
        inst = self.instantiate_from("coverage-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage2(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage2(inst2)
    
    def implCoverage2(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir[0].name), force_bytes("Western Airlines"))
        self.assertEqual(force_bytes(inst.class_fhir[0].type.coding[0].code), force_bytes("group"))
        self.assertEqual(force_bytes(inst.class_fhir[0].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[0].value), force_bytes("WESTAIR"))
        self.assertEqual(force_bytes(inst.class_fhir[1].name), force_bytes("Full Coverage: Medical, Dental, Pharmacy, Vision, EHC"))
        self.assertEqual(force_bytes(inst.class_fhir[1].type.coding[0].code), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.class_fhir[1].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[1].value), force_bytes("BG4352"))
        self.assertEqual(force_bytes(inst.class_fhir[2].name), force_bytes("Platinum"))
        self.assertEqual(force_bytes(inst.class_fhir[2].type.coding[0].code), force_bytes("subplan"))
        self.assertEqual(force_bytes(inst.class_fhir[2].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[2].value), force_bytes("D15C9"))
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.end.date, FHIRDate("2018-12-31").date)
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.end.as_json(), "2018-12-31")
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.start.date, FHIRDate("2018-01-01").date)
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.start.as_json(), "2018-01-01")
        self.assertEqual(force_bytes(inst.costToBeneficiary[0].exception[0].type.coding[0].code), force_bytes("retired"))
        self.assertEqual(force_bytes(inst.costToBeneficiary[0].exception[0].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception"))
        self.assertEqual(force_bytes(inst.costToBeneficiary[0].type.coding[0].code), force_bytes("gpvisit"))
        self.assertEqual(force_bytes(inst.costToBeneficiary[0].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-copay-type"))
        self.assertEqual(force_bytes(inst.costToBeneficiary[0].valueMoney.currency), force_bytes("USD"))
        self.assertEqual(inst.costToBeneficiary[0].valueMoney.value, 20.0)
        self.assertEqual(force_bytes(inst.dependent), force_bytes("1"))
        self.assertEqual(force_bytes(inst.id), force_bytes("7546D"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://xyz.com/codes/identifier"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("AB98761"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.network), force_bytes("5"))
        self.assertEqual(inst.order, 2)
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-17").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-03-17").date)
        self.assertEqual(inst.period.start.as_json(), "2011-03-17")
        self.assertEqual(force_bytes(inst.relationship.coding[0].code), force_bytes("self"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.subscriberId), force_bytes("AB9876"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("EHCPOL"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("extended healthcare"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"))
    
    def testCoverage3(self):
        inst = self.instantiate_from("coverage-example-ehic.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage3(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage3(inst2)
    
    def implCoverage3(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("7547E"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://ehic.com/insurer/123456789/member"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("A123456780"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-17").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(force_bytes(inst.relationship.coding[0].code), force_bytes("self"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the European Health Insurance Card</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("EHCPOL"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("extended healthcare"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"))
    
    def testCoverage4(self):
        inst = self.instantiate_from("coverage-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage4(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage4(inst2)
    
    def implCoverage4(self, inst):
        self.assertEqual(force_bytes(inst.class_fhir[0].name), force_bytes("Corporate Baker's Inc. Local #35"))
        self.assertEqual(force_bytes(inst.class_fhir[0].type.coding[0].code), force_bytes("group"))
        self.assertEqual(force_bytes(inst.class_fhir[0].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[0].value), force_bytes("CB135"))
        self.assertEqual(force_bytes(inst.class_fhir[1].name), force_bytes("Trainee Part-time Benefits"))
        self.assertEqual(force_bytes(inst.class_fhir[1].type.coding[0].code), force_bytes("subgroup"))
        self.assertEqual(force_bytes(inst.class_fhir[1].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[1].value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.class_fhir[2].name), force_bytes("Full Coverage: Medical, Dental, Pharmacy, Vision, EHC"))
        self.assertEqual(force_bytes(inst.class_fhir[2].type.coding[0].code), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.class_fhir[2].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[2].value), force_bytes("B37FC"))
        self.assertEqual(force_bytes(inst.class_fhir[3].name), force_bytes("Includes afterlife benefits"))
        self.assertEqual(force_bytes(inst.class_fhir[3].type.coding[0].code), force_bytes("subplan"))
        self.assertEqual(force_bytes(inst.class_fhir[3].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[3].value), force_bytes("P7"))
        self.assertEqual(force_bytes(inst.class_fhir[4].name), force_bytes("Silver: Family Plan spouse only"))
        self.assertEqual(force_bytes(inst.class_fhir[4].type.coding[0].code), force_bytes("class"))
        self.assertEqual(force_bytes(inst.class_fhir[4].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[4].value), force_bytes("SILVER"))
        self.assertEqual(force_bytes(inst.class_fhir[5].name), force_bytes("Low deductable, max $20 copay"))
        self.assertEqual(force_bytes(inst.class_fhir[5].type.coding[0].code), force_bytes("subclass"))
        self.assertEqual(force_bytes(inst.class_fhir[5].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[5].value), force_bytes("Tier2"))
        self.assertEqual(force_bytes(inst.class_fhir[6].type.coding[0].code), force_bytes("sequence"))
        self.assertEqual(force_bytes(inst.class_fhir[6].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[6].value), force_bytes("9"))
        self.assertEqual(force_bytes(inst.class_fhir[7].type.coding[0].code), force_bytes("rxid"))
        self.assertEqual(force_bytes(inst.class_fhir[7].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[7].value), force_bytes("MDF12345"))
        self.assertEqual(force_bytes(inst.class_fhir[8].type.coding[0].code), force_bytes("rxbin"))
        self.assertEqual(force_bytes(inst.class_fhir[8].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[8].value), force_bytes("987654"))
        self.assertEqual(force_bytes(inst.class_fhir[9].type.coding[0].code), force_bytes("rxgroup"))
        self.assertEqual(force_bytes(inst.class_fhir[9].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/coverage-class"))
        self.assertEqual(force_bytes(inst.class_fhir[9].value), force_bytes("M35PT"))
        self.assertEqual(force_bytes(inst.dependent), force_bytes("0"))
        self.assertEqual(force_bytes(inst.id), force_bytes("9876B1"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://benefitsinc.com/certificate"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.period.end.date, FHIRDate("2012-05-23").date)
        self.assertEqual(inst.period.end.as_json(), "2012-05-23")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-05-23").date)
        self.assertEqual(inst.period.start.as_json(), "2011-05-23")
        self.assertEqual(force_bytes(inst.relationship.coding[0].code), force_bytes("self"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("EHCPOL"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("extended healthcare"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"))

