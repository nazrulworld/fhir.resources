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
from .. import consent
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ConsentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Consent", js["resourceType"])
        return consent.Consent(js)
    
    def testConsent1(self):
        inst = self.instantiate_from("consent-example-Emergency.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent1(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent1(inst2)
    
    def implConsent1(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].code), force_bytes("CST"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[0].purpose[0].code), force_bytes("ETREAT"))
        self.assertEqual(force_bytes(inst.except_fhir[0].purpose[0].system), force_bytes("http://hl7.org/fhir/v3/ActReason"))
        self.assertEqual(force_bytes(inst.except_fhir[0].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[1].actor[0].role.coding[0].code), force_bytes("CST"))
        self.assertEqual(force_bytes(inst.except_fhir[1].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[1].type), force_bytes("deny"))
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-Emergency"))
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://hl7.org/fhir/ConsentPolicy/opt-out"))
        self.assertEqual(force_bytes(inst.sourceAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testConsent2(self):
        inst = self.instantiate_from("consent-example-notThis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent2(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent2(inst2)
    
    def implConsent2(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.except_fhir[0].data[0].meaning), force_bytes("related"))
        self.assertEqual(force_bytes(inst.except_fhir[0].type), force_bytes("deny"))
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-notThis"))
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://hl7.org/fhir/ConsentPolicy/opt-in"))
        self.assertEqual(force_bytes(inst.sourceAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testConsent3(self):
        inst = self.instantiate_from("consent-example-pkb.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent3(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent3(inst2)
    
    def implConsent3(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2016-06-16").date)
        self.assertEqual(inst.dateTime.as_json(), "2016-06-16")
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[0].securityLabel[0].code), force_bytes("N"))
        self.assertEqual(force_bytes(inst.except_fhir[0].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/Confidentiality"))
        self.assertEqual(force_bytes(inst.except_fhir[0].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[1].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[1].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[1].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[1].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[1].securityLabel[0].code), force_bytes("PSY"))
        self.assertEqual(force_bytes(inst.except_fhir[1].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.except_fhir[1].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[2].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[2].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[2].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[2].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[2].securityLabel[0].code), force_bytes("SOC"))
        self.assertEqual(force_bytes(inst.except_fhir[2].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.except_fhir[2].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[3].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[3].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[3].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[3].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[3].securityLabel[0].code), force_bytes("N"))
        self.assertEqual(force_bytes(inst.except_fhir[3].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/Confidentiality"))
        self.assertEqual(force_bytes(inst.except_fhir[3].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[4].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[4].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[4].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[4].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[4].securityLabel[0].code), force_bytes("PSY"))
        self.assertEqual(force_bytes(inst.except_fhir[4].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.except_fhir[4].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[5].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[5].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[5].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[5].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[5].securityLabel[0].code), force_bytes("SOC"))
        self.assertEqual(force_bytes(inst.except_fhir[5].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.except_fhir[5].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[6].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[6].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[6].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[6].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[6].securityLabel[0].code), force_bytes("SEX"))
        self.assertEqual(force_bytes(inst.except_fhir[6].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.except_fhir[6].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[7].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[7].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[7].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[7].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[7].securityLabel[0].code), force_bytes("N"))
        self.assertEqual(force_bytes(inst.except_fhir[7].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/Confidentiality"))
        self.assertEqual(force_bytes(inst.except_fhir[7].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[8].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[8].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[8].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[8].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[8].securityLabel[0].code), force_bytes("PSY"))
        self.assertEqual(force_bytes(inst.except_fhir[8].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.except_fhir[8].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.except_fhir[9].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[9].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[9].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[9].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[9].securityLabel[0].code), force_bytes("SOC"))
        self.assertEqual(force_bytes(inst.except_fhir[9].securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.except_fhir[9].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-pkb"))
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://hl7.org/fhir/ConsentPolicy/opt-out"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testConsent4(self):
        inst = self.instantiate_from("consent-example-notThem.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent4(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent4(inst2)
    
    def implConsent4(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[0].action[1].coding[0].code), force_bytes("correct"))
        self.assertEqual(force_bytes(inst.except_fhir[0].action[1].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[0].type), force_bytes("deny"))
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-notThem"))
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://hl7.org/fhir/ConsentPolicy/opt-in"))
        self.assertEqual(force_bytes(inst.sourceAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testConsent5(self):
        inst = self.instantiate_from("consent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent5(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent5(inst2)
    
    def implConsent5(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2016-05-11").date)
        self.assertEqual(inst.dateTime.as_json(), "2016-05-11")
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-basic"))
        self.assertEqual(inst.period.end.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.period.end.as_json(), "2016-01-01")
        self.assertEqual(inst.period.start.date, FHIRDate("1964-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "1964-01-01")
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://goodhealth.org/consent/policy/opt-in"))
        self.assertEqual(force_bytes(inst.sourceAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testConsent6(self):
        inst = self.instantiate_from("consent-example-Out.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent6(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent6(inst2)
    
    def implConsent6(self, inst):
        self.assertEqual(force_bytes(inst.actor[0].role.coding[0].code), force_bytes("CST"))
        self.assertEqual(force_bytes(inst.actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-Out"))
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://hl7.org/fhir/ConsentPolicy/opt-out"))
        self.assertEqual(force_bytes(inst.sourceAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testConsent7(self):
        inst = self.instantiate_from("consent-example-notOrg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent7(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent7(inst2)
    
    def implConsent7(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[0].action[1].coding[0].code), force_bytes("correct"))
        self.assertEqual(force_bytes(inst.except_fhir[0].action[1].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[0].type), force_bytes("deny"))
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-notOrg"))
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://hl7.org/fhir/ConsentPolicy/opt-in"))
        self.assertEqual(force_bytes(inst.sourceAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testConsent8(self):
        inst = self.instantiate_from("consent-example-notTime.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent8(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent8(inst2)
    
    def implConsent8(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.except_fhir[0].period.end.date, FHIRDate("2015-02-01").date)
        self.assertEqual(inst.except_fhir[0].period.end.as_json(), "2015-02-01")
        self.assertEqual(inst.except_fhir[0].period.start.date, FHIRDate("2015-01-01").date)
        self.assertEqual(inst.except_fhir[0].period.start.as_json(), "2015-01-01")
        self.assertEqual(force_bytes(inst.except_fhir[0].type), force_bytes("deny"))
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-notTime"))
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://hl7.org/fhir/ConsentPolicy/opt-in"))
        self.assertEqual(force_bytes(inst.sourceAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testConsent9(self):
        inst = self.instantiate_from("consent-example-grantor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent9(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent9(inst2)
    
    def implConsent9(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].code), force_bytes("CST"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[1].role.coding[0].code), force_bytes("PRCP"))
        self.assertEqual(force_bytes(inst.except_fhir[0].actor[1].role.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(force_bytes(inst.except_fhir[0].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-grantor"))
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://hl7.org/fhir/ConsentPolicy/opt-out"))
        self.assertEqual(force_bytes(inst.sourceAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testConsent10(self):
        inst = self.instantiate_from("consent-example-smartonfhir.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent10(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent10(inst2)
    
    def implConsent10(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2016-06-23T17:02:33+10:00").date)
        self.assertEqual(inst.dateTime.as_json(), "2016-06-23T17:02:33+10:00")
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].code), force_bytes("access"))
        self.assertEqual(force_bytes(inst.except_fhir[0].action[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentaction"))
        self.assertEqual(force_bytes(inst.except_fhir[0].class_fhir[0].code), force_bytes("MedicationRequest"))
        self.assertEqual(force_bytes(inst.except_fhir[0].class_fhir[0].system), force_bytes("http://hl7.org/fhir/resource-types"))
        self.assertEqual(force_bytes(inst.except_fhir[0].type), force_bytes("permit"))
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-example-smartonfhir"))
        self.assertEqual(inst.period.end.date, FHIRDate("2016-06-23T17:32:33+10:00").date)
        self.assertEqual(inst.period.end.as_json(), "2016-06-23T17:32:33+10:00")
        self.assertEqual(inst.period.start.date, FHIRDate("2016-06-23T17:02:33+10:00").date)
        self.assertEqual(inst.period.start.as_json(), "2016-06-23T17:02:33+10:00")
        self.assertEqual(force_bytes(inst.policyRule), force_bytes("http://hl7.org/fhir/ConsentPolicy/opt-in"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

