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
from .. import task
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class TaskTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Task", js["resourceType"])
        return task.Task(js)
    
    def testTask1(self):
        inst = self.instantiate_from("task-example6.json")
        self.assertIsNotNone(inst, "Must have instantiated a Task instance")
        self.implTask1(inst)
        
        js = inst.as_json()
        self.assertEqual("Task", js["resourceType"])
        inst2 = task.Task(js)
        self.implTask1(inst2)
    
    def implTask1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-10-31T08:25:05+10:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-10-31T08:25:05+10:00")
        self.assertEqual(force_bytes(inst.businessStatus.text), force_bytes("test completed and posted"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Lipid Panel"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Create order for getting specimen, Set up inhouse testing,  generate order for any sendouts and submit with specimen"))
        self.assertEqual(inst.executionPeriod.end.date, FHIRDate("2016-10-31T18:45:05+10:00").date)
        self.assertEqual(inst.executionPeriod.end.as_json(), "2016-10-31T18:45:05+10:00")
        self.assertEqual(inst.executionPeriod.start.date, FHIRDate("2016-10-31T08:25:05+10:00").date)
        self.assertEqual(inst.executionPeriod.start.as_json(), "2016-10-31T08:25:05+10:00")
        self.assertEqual(force_bytes(inst.groupIdentifier.system), force_bytes("http:/goodhealth.org/accession/identifiers"))
        self.assertEqual(force_bytes(inst.groupIdentifier.use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("G20170201-001"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example6"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http:/goodhealth.org/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("20170201-001"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(inst.lastModified.date, FHIRDate("2016-10-31T18:45:05+10:00").date)
        self.assertEqual(inst.lastModified.as_json(), "2016-10-31T18:45:05+10:00")
        self.assertEqual(force_bytes(inst.output[0].type.text), force_bytes("DiagnosticReport generated"))
        self.assertEqual(force_bytes(inst.output[1].type.text), force_bytes("collected specimen"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].code), force_bytes("performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].display), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].system), force_bytes("http://hl7.org/fhir/task-performer-type"))
        self.assertEqual(force_bytes(inst.performerType[0].text), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(force_bytes(inst.reason.text), force_bytes("The Task.reason should only be included if there is no Task.focus or if it differs from the reason indicated on the focus"))
        self.assertEqual(inst.restriction.period.end.date, FHIRDate("2016-11-02T09:45:05+10:00").date)
        self.assertEqual(inst.restriction.period.end.as_json(), "2016-11-02T09:45:05+10:00")
        self.assertEqual(inst.restriction.repetitions, 1)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testTask2(self):
        inst = self.instantiate_from("task-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Task instance")
        self.implTask2(inst)
        
        js = inst.as_json()
        self.assertEqual("Task", js["resourceType"])
        inst2 = task.Task(js)
        self.implTask2(inst2)
    
    def implTask2(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-10-31T08:45:05+10:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-10-31T08:45:05+10:00")
        self.assertEqual(force_bytes(inst.businessStatus.text), force_bytes("waiting for patient"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Specimen Collection"))
        self.assertEqual(inst.executionPeriod.start.date, FHIRDate("2016-10-31T08:45:05+10:00").date)
        self.assertEqual(inst.executionPeriod.start.as_json(), "2016-10-31T08:45:05+10:00")
        self.assertEqual(force_bytes(inst.groupIdentifier.system), force_bytes("http:/goodhealth.org/accession/identifiers"))
        self.assertEqual(force_bytes(inst.groupIdentifier.use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("G20170201-001"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example2"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http:/goodhealth.org/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("20170201-002"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("filler-order"))
        self.assertEqual(inst.lastModified.date, FHIRDate("2016-10-31T09:45:05+10:00").date)
        self.assertEqual(inst.lastModified.as_json(), "2016-10-31T09:45:05+10:00")
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].code), force_bytes("performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].display), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].system), force_bytes("http://hl7.org/fhir/task-performer-type"))
        self.assertEqual(force_bytes(inst.performerType[0].text), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(inst.restriction.period.end.date, FHIRDate("2016-11-01T09:45:05+10:00").date)
        self.assertEqual(inst.restriction.period.end.as_json(), "2016-11-01T09:45:05+10:00")
        self.assertEqual(inst.restriction.repetitions, 1)
        self.assertEqual(force_bytes(inst.status), force_bytes("accepted"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testTask3(self):
        inst = self.instantiate_from("task-example5.json")
        self.assertIsNotNone(inst, "Must have instantiated a Task instance")
        self.implTask3(inst)
        
        js = inst.as_json()
        self.assertEqual("Task", js["resourceType"])
        inst2 = task.Task(js)
        self.implTask3(inst2)
    
    def implTask3(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-10-31T08:25:05+10:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-10-31T08:25:05+10:00")
        self.assertEqual(force_bytes(inst.businessStatus.text), force_bytes("specimen received, test in progress"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Lipid Panel"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Create order for getting specimen, Set up inhouse testing,  generate order for any sendouts and submit with specimen"))
        self.assertEqual(inst.executionPeriod.start.date, FHIRDate("2016-10-31T08:25:05+10:00").date)
        self.assertEqual(inst.executionPeriod.start.as_json(), "2016-10-31T08:25:05+10:00")
        self.assertEqual(force_bytes(inst.groupIdentifier.system), force_bytes("http:/goodhealth.org/accession/identifiers"))
        self.assertEqual(force_bytes(inst.groupIdentifier.use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("G20170201-001"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example5"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http:/goodhealth.org/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("20170201-001"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(inst.lastModified.date, FHIRDate("2016-10-31T16:45:05+10:00").date)
        self.assertEqual(inst.lastModified.as_json(), "2016-10-31T16:45:05+10:00")
        self.assertEqual(force_bytes(inst.output[0].type.text), force_bytes("collected specimen"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].code), force_bytes("performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].display), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].system), force_bytes("http://hl7.org/fhir/task-performer-type"))
        self.assertEqual(force_bytes(inst.performerType[0].text), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(force_bytes(inst.reason.text), force_bytes("The Task.reason should only be included if there is no Task.focus or if it differs from the reason indicated on the focus"))
        self.assertEqual(inst.restriction.period.end.date, FHIRDate("2016-11-02T09:45:05+10:00").date)
        self.assertEqual(inst.restriction.period.end.as_json(), "2016-11-02T09:45:05+10:00")
        self.assertEqual(inst.restriction.repetitions, 1)
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testTask4(self):
        inst = self.instantiate_from("task-example1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Task instance")
        self.implTask4(inst)
        
        js = inst.as_json()
        self.assertEqual("Task", js["resourceType"])
        inst2 = task.Task(js)
        self.implTask4(inst2)
    
    def implTask4(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-10-31T08:25:05+10:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-10-31T08:25:05+10:00")
        self.assertEqual(force_bytes(inst.businessStatus.text), force_bytes("waiting for specimen"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Lipid Panel"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("signature"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Create order for getting specimen, Set up inhouse testing,  generate order for any sendouts and submit with specimen"))
        self.assertEqual(inst.executionPeriod.start.date, FHIRDate("2016-10-31T08:25:05+10:00").date)
        self.assertEqual(inst.executionPeriod.start.as_json(), "2016-10-31T08:25:05+10:00")
        self.assertEqual(force_bytes(inst.groupIdentifier.system), force_bytes("http:/goodhealth.org/accession/identifiers"))
        self.assertEqual(force_bytes(inst.groupIdentifier.use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("G20170201-001"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example1"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http:/goodhealth.org/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("20170201-001"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(inst.lastModified.date, FHIRDate("2016-10-31T09:45:05+10:00").date)
        self.assertEqual(inst.lastModified.as_json(), "2016-10-31T09:45:05+10:00")
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].code), force_bytes("performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].display), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].system), force_bytes("http://hl7.org/fhir/task-performer-type"))
        self.assertEqual(force_bytes(inst.performerType[0].text), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(force_bytes(inst.reason.text), force_bytes("The Task.reason should only be included if there is no Task.focus or if it differs from the reason indicated on the focus"))
        self.assertEqual(inst.restriction.period.end.date, FHIRDate("2016-11-02T09:45:05+10:00").date)
        self.assertEqual(inst.restriction.period.end.as_json(), "2016-11-02T09:45:05+10:00")
        self.assertEqual(inst.restriction.repetitions, 1)
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testTask5(self):
        inst = self.instantiate_from("task-example4.json")
        self.assertIsNotNone(inst, "Must have instantiated a Task instance")
        self.implTask5(inst)
        
        js = inst.as_json()
        self.assertEqual("Task", js["resourceType"])
        inst2 = task.Task(js)
        self.implTask5(inst2)
    
    def implTask5(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-10-31T08:45:05+10:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-10-31T08:45:05+10:00")
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Specimen Collection"))
        self.assertEqual(inst.executionPeriod.end.date, FHIRDate("2016-10-31T14:45:05+10:00").date)
        self.assertEqual(inst.executionPeriod.end.as_json(), "2016-10-31T14:45:05+10:00")
        self.assertEqual(inst.executionPeriod.start.date, FHIRDate("2016-10-31T08:45:05+10:00").date)
        self.assertEqual(inst.executionPeriod.start.as_json(), "2016-10-31T08:45:05+10:00")
        self.assertEqual(force_bytes(inst.groupIdentifier.system), force_bytes("http:/goodhealth.org/accession/identifiers"))
        self.assertEqual(force_bytes(inst.groupIdentifier.use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("G20170201-001"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example4"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http:/goodhealth.org/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("20170201-002"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("filler-order"))
        self.assertEqual(inst.lastModified.date, FHIRDate("2016-10-31T09:45:05+10:00").date)
        self.assertEqual(inst.lastModified.as_json(), "2016-10-31T09:45:05+10:00")
        self.assertEqual(force_bytes(inst.output[0].type.text), force_bytes("collected specimen"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].code), force_bytes("performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].display), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.performerType[0].coding[0].system), force_bytes("http://hl7.org/fhir/task-performer-type"))
        self.assertEqual(force_bytes(inst.performerType[0].text), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(inst.restriction.period.end.date, FHIRDate("2016-11-01T09:45:05+10:00").date)
        self.assertEqual(inst.restriction.period.end.as_json(), "2016-11-01T09:45:05+10:00")
        self.assertEqual(inst.restriction.repetitions, 1)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testTask6(self):
        inst = self.instantiate_from("task-example3.json")
        self.assertIsNotNone(inst, "Must have instantiated a Task instance")
        self.implTask6(inst)
        
        js = inst.as_json()
        self.assertEqual("Task", js["resourceType"])
        inst2 = task.Task(js)
        self.implTask6(inst2)
    
    def implTask6(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-03-10T22:39:32-04:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-03-10T22:39:32-04:00")
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Refill Request"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example3"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(inst.lastModified.date, FHIRDate("2016-03-10T22:39:32-04:00").date)
        self.assertEqual(inst.lastModified.as_json(), "2016-03-10T22:39:32-04:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

