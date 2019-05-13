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
from .. import goal
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class GoalTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Goal", js["resourceType"])
        return goal.Goal(js)
    
    def testGoal1(self):
        inst = self.instantiate_from("goal-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Goal instance")
        self.implGoal1(inst)
        
        js = inst.as_json()
        self.assertEqual("Goal", js["resourceType"])
        inst2 = goal.Goal(js)
        self.implGoal1(inst2)
    
    def implGoal1(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("dietary"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://hl7.org/fhir/goal-category"))
        self.assertEqual(force_bytes(inst.description.text), force_bytes("Target weight is 160 to 180 lbs."))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.priority.coding[0].code), force_bytes("high-priority"))
        self.assertEqual(force_bytes(inst.priority.coding[0].display), force_bytes("High Priority"))
        self.assertEqual(force_bytes(inst.priority.coding[0].system), force_bytes("http://hl7.org/fhir/goal-priority"))
        self.assertEqual(force_bytes(inst.priority.text), force_bytes("high"))
        self.assertEqual(inst.startDate.date, FHIRDate("2015-04-05").date)
        self.assertEqual(inst.startDate.as_json(), "2015-04-05")
        self.assertEqual(force_bytes(inst.status), force_bytes("on-hold"))
        self.assertEqual(inst.statusDate.date, FHIRDate("2016-02-14").date)
        self.assertEqual(inst.statusDate.as_json(), "2016-02-14")
        self.assertEqual(force_bytes(inst.statusReason), force_bytes("Patient wants to defer weight loss until after honeymoon."))
        self.assertEqual(force_bytes(inst.target.detailRange.high.code), force_bytes("[lb_av]"))
        self.assertEqual(force_bytes(inst.target.detailRange.high.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.target.detailRange.high.unit), force_bytes("lbs"))
        self.assertEqual(inst.target.detailRange.high.value, 180)
        self.assertEqual(force_bytes(inst.target.detailRange.low.code), force_bytes("[lb_av]"))
        self.assertEqual(force_bytes(inst.target.detailRange.low.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.target.detailRange.low.unit), force_bytes("lbs"))
        self.assertEqual(inst.target.detailRange.low.value, 160)
        self.assertEqual(inst.target.dueDate.date, FHIRDate("2016-04-05").date)
        self.assertEqual(inst.target.dueDate.as_json(), "2016-04-05")
        self.assertEqual(force_bytes(inst.target.measure.coding[0].code), force_bytes("3141-9"))
        self.assertEqual(force_bytes(inst.target.measure.coding[0].display), force_bytes("Weight Measured"))
        self.assertEqual(force_bytes(inst.target.measure.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
    
    def testGoal2(self):
        inst = self.instantiate_from("goal-example-stop-smoking.json")
        self.assertIsNotNone(inst, "Must have instantiated a Goal instance")
        self.implGoal2(inst)
        
        js = inst.as_json()
        self.assertEqual("Goal", js["resourceType"])
        inst2 = goal.Goal(js)
        self.implGoal2(inst2)
    
    def implGoal2(self, inst):
        self.assertEqual(force_bytes(inst.description.text), force_bytes("Stop smoking"))
        self.assertEqual(force_bytes(inst.id), force_bytes("stop-smoking"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.outcomeCode[0].coding[0].code), force_bytes("8517006"))
        self.assertEqual(force_bytes(inst.outcomeCode[0].coding[0].display), force_bytes("Ex-smoker (finding)"))
        self.assertEqual(force_bytes(inst.outcomeCode[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.outcomeCode[0].text), force_bytes("Former smoker"))
        self.assertEqual(inst.startDate.date, FHIRDate("2015-04-05").date)
        self.assertEqual(inst.startDate.as_json(), "2015-04-05")
        self.assertEqual(force_bytes(inst.status), force_bytes("achieved"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))

