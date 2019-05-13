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
from .. import requestgroup
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class RequestGroupTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("RequestGroup", js["resourceType"])
        return requestgroup.RequestGroup(js)
    
    def testRequestGroup1(self):
        inst = self.instantiate_from("requestgroup-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RequestGroup instance")
        self.implRequestGroup1(inst)
        
        js = inst.as_json()
        self.assertEqual("RequestGroup", js["resourceType"])
        inst2 = requestgroup.RequestGroup(js)
        self.implRequestGroup1(inst2)
    
    def implRequestGroup1(self, inst):
        self.assertEqual(force_bytes(inst.action[0].action[0].description), force_bytes("Administer medication 1"))
        self.assertEqual(force_bytes(inst.action[0].action[0].id), force_bytes("medication-action-1"))
        self.assertEqual(force_bytes(inst.action[0].action[0].type.coding[0].code), force_bytes("create"))
        self.assertEqual(force_bytes(inst.action[0].action[1].description), force_bytes("Administer medication 2"))
        self.assertEqual(force_bytes(inst.action[0].action[1].id), force_bytes("medication-action-2"))
        self.assertEqual(force_bytes(inst.action[0].action[1].relatedAction[0].actionId), force_bytes("medication-action-1"))
        self.assertEqual(force_bytes(inst.action[0].action[1].relatedAction[0].offsetDuration.unit), force_bytes("h"))
        self.assertEqual(inst.action[0].action[1].relatedAction[0].offsetDuration.value, 1)
        self.assertEqual(force_bytes(inst.action[0].action[1].relatedAction[0].relationship), force_bytes("after-end"))
        self.assertEqual(force_bytes(inst.action[0].action[1].type.coding[0].code), force_bytes("create"))
        self.assertEqual(force_bytes(inst.action[0].cardinalityBehavior), force_bytes("single"))
        self.assertEqual(force_bytes(inst.action[0].description), force_bytes("Administer medications at the appropriate time"))
        self.assertEqual(force_bytes(inst.action[0].groupingBehavior), force_bytes("logical-group"))
        self.assertEqual(force_bytes(inst.action[0].precheckBehavior), force_bytes("yes"))
        self.assertEqual(force_bytes(inst.action[0].prefix), force_bytes("1"))
        self.assertEqual(force_bytes(inst.action[0].requiredBehavior), force_bytes("must"))
        self.assertEqual(force_bytes(inst.action[0].selectionBehavior), force_bytes("all"))
        self.assertEqual(force_bytes(inst.action[0].textEquivalent), force_bytes("Administer medication 1, followed an hour later by medication 2"))
        self.assertEqual(inst.action[0].timingDateTime.date, FHIRDate("2017-03-06T19:00:00Z").date)
        self.assertEqual(inst.action[0].timingDateTime.as_json(), "2017-03-06T19:00:00Z")
        self.assertEqual(force_bytes(inst.action[0].title), force_bytes("Administer Medications"))
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-06T17:31:00Z").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-06T17:31:00Z")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("medicationrequest-1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("medicationrequest-2"))
        self.assertEqual(force_bytes(inst.groupIdentifier.system), force_bytes("http://example.org/treatment-group"))
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("00001"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("requestgroup-1"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Additional notes about the request group"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("Treatment"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Example RequestGroup illustrating related actions to administer medications in sequence with time delay.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testRequestGroup2(self):
        inst = self.instantiate_from("requestgroup-kdn5-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RequestGroup instance")
        self.implRequestGroup2(inst)
        
        js = inst.as_json()
        self.assertEqual("RequestGroup", js["resourceType"])
        inst2 = requestgroup.RequestGroup(js)
        self.implRequestGroup2(inst2)
    
    def implRequestGroup2(self, inst):
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[0].url), force_bytes("day"))
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[0].valueInteger, 1)
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[1].url), force_bytes("day"))
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[1].valueInteger, 8)
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[0].extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[0].id), force_bytes("action-1"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[0].textEquivalent), force_bytes("Gemcitabine 1250 mg/m² IV over 30 minutes on days 1 and 8"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[1].extension[0].extension[0].url), force_bytes("day"))
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].extension[0].extension[0].valueInteger, 1)
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[1].extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[1].id), force_bytes("action-2"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].actionId), force_bytes("action-1"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].relationship), force_bytes("concurrent-with-start"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].action[1].textEquivalent), force_bytes("CARBOplatin AUC 5 IV over 30 minutes on Day 1"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].id), force_bytes("cycle-definition-1"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].textEquivalent), force_bytes("21-day cycle for 6 cycles"))
        self.assertEqual(inst.action[0].action[0].action[0].action[0].timingTiming.repeat.count, 6)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].timingTiming.repeat.duration, 21)
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].action[0].timingTiming.repeat.durationUnit), force_bytes("d"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].groupingBehavior), force_bytes("sentence-group"))
        self.assertEqual(force_bytes(inst.action[0].action[0].action[0].selectionBehavior), force_bytes("exactly-one"))
        self.assertEqual(force_bytes(inst.action[0].action[0].selectionBehavior), force_bytes("all"))
        self.assertEqual(force_bytes(inst.action[0].selectionBehavior), force_bytes("exactly-one"))
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-06T17:31:00Z").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-06T17:31:00Z")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("1111"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("2222"))
        self.assertEqual(force_bytes(inst.id), force_bytes("kdn5-example"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("requestgroup-kdn5"))
        self.assertEqual(force_bytes(inst.instantiatesCanonical[0]), force_bytes("PlanDefinition/KDN5"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Administer gemcitabine and carboplatin.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

