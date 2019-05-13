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
from .. import appointment
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class AppointmentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Appointment", js["resourceType"])
        return appointment.Appointment(js)
    
    def testAppointment1(self):
        inst = self.instantiate_from("appointment-example2doctors.json")
        self.assertIsNotNone(inst, "Must have instantiated a Appointment instance")
        self.implAppointment1(inst)
        
        js = inst.as_json()
        self.assertEqual("Appointment", js["resourceType"])
        inst2 = appointment.Appointment(js)
        self.implAppointment1(inst2)
    
    def implAppointment1(self, inst):
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].code), force_bytes("WALKIN"))
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].display), force_bytes("A previously unscheduled walk-in visit"))
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0276"))
        self.assertEqual(force_bytes(inst.comment), force_bytes("Clarify the results of the MRI to ensure context of test was correct"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Discussion about Peter Chalmers MRI results"))
        self.assertEqual(inst.end.date, FHIRDate("2013-12-09T11:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-09T11:00:00Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("2docs"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.participant[0].required), force_bytes("information-only"))
        self.assertEqual(force_bytes(inst.participant[0].status), force_bytes("accepted"))
        self.assertEqual(force_bytes(inst.participant[1].required), force_bytes("required"))
        self.assertEqual(force_bytes(inst.participant[1].status), force_bytes("accepted"))
        self.assertEqual(force_bytes(inst.participant[2].required), force_bytes("required"))
        self.assertEqual(force_bytes(inst.participant[2].status), force_bytes("accepted"))
        self.assertEqual(force_bytes(inst.participant[3].required), force_bytes("information-only"))
        self.assertEqual(force_bytes(inst.participant[3].status), force_bytes("accepted"))
        self.assertEqual(inst.priority, 5)
        self.assertEqual(force_bytes(inst.serviceCategory[0].coding[0].code), force_bytes("gp"))
        self.assertEqual(force_bytes(inst.serviceCategory[0].coding[0].display), force_bytes("General Practice"))
        self.assertEqual(force_bytes(inst.serviceCategory[0].coding[0].system), force_bytes("http://example.org/service-category"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].code), force_bytes("52"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].display), force_bytes("General Discussion"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("394814009"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("General practice"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(inst.start.date, FHIRDate("2013-12-09T09:00:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-09T09:00:00Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("booked"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Brian MRI results discussion</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testAppointment2(self):
        inst = self.instantiate_from("appointment-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Appointment instance")
        self.implAppointment2(inst)
        
        js = inst.as_json()
        self.assertEqual("Appointment", js["resourceType"])
        inst2 = appointment.Appointment(js)
        self.implAppointment2(inst2)
    
    def implAppointment2(self, inst):
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].code), force_bytes("FOLLOWUP"))
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].display), force_bytes("A follow up visit from a previous appointment"))
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0276"))
        self.assertEqual(force_bytes(inst.comment), force_bytes("Further expand on the results of the MRI and determine the next actions that may be appropriate."))
        self.assertEqual(inst.created.date, FHIRDate("2013-10-10").date)
        self.assertEqual(inst.created.as_json(), "2013-10-10")
        self.assertEqual(force_bytes(inst.description), force_bytes("Discussion on the results of your recent MRI"))
        self.assertEqual(inst.end.date, FHIRDate("2013-12-10T11:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-10T11:00:00Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.participant[0].required), force_bytes("required"))
        self.assertEqual(force_bytes(inst.participant[0].status), force_bytes("accepted"))
        self.assertEqual(force_bytes(inst.participant[1].required), force_bytes("required"))
        self.assertEqual(force_bytes(inst.participant[1].status), force_bytes("accepted"))
        self.assertEqual(force_bytes(inst.participant[1].type[0].coding[0].code), force_bytes("ATND"))
        self.assertEqual(force_bytes(inst.participant[1].type[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ParticipationType"))
        self.assertEqual(force_bytes(inst.participant[2].required), force_bytes("required"))
        self.assertEqual(force_bytes(inst.participant[2].status), force_bytes("accepted"))
        self.assertEqual(inst.priority, 5)
        self.assertEqual(force_bytes(inst.serviceCategory[0].coding[0].code), force_bytes("gp"))
        self.assertEqual(force_bytes(inst.serviceCategory[0].coding[0].display), force_bytes("General Practice"))
        self.assertEqual(force_bytes(inst.serviceCategory[0].coding[0].system), force_bytes("http://example.org/service-category"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].code), force_bytes("52"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].display), force_bytes("General Discussion"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("394814009"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("General practice"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(inst.start.date, FHIRDate("2013-12-10T09:00:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-10T09:00:00Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("booked"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Brian MRI results discussion</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testAppointment3(self):
        inst = self.instantiate_from("appointment-example-request.json")
        self.assertIsNotNone(inst, "Must have instantiated a Appointment instance")
        self.implAppointment3(inst)
        
        js = inst.as_json()
        self.assertEqual("Appointment", js["resourceType"])
        inst2 = appointment.Appointment(js)
        self.implAppointment3(inst2)
    
    def implAppointment3(self, inst):
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].code), force_bytes("WALKIN"))
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].display), force_bytes("A previously unscheduled walk-in visit"))
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0276"))
        self.assertEqual(force_bytes(inst.comment), force_bytes("Further expand on the results of the MRI and determine the next actions that may be appropriate."))
        self.assertEqual(inst.created.date, FHIRDate("2015-12-02").date)
        self.assertEqual(inst.created.as_json(), "2015-12-02")
        self.assertEqual(force_bytes(inst.description), force_bytes("Discussion on the results of your recent MRI"))
        self.assertEqual(force_bytes(inst.id), force_bytes("examplereq"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/sampleappointment-identifier"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.minutesDuration, 15)
        self.assertEqual(force_bytes(inst.participant[0].required), force_bytes("required"))
        self.assertEqual(force_bytes(inst.participant[0].status), force_bytes("needs-action"))
        self.assertEqual(force_bytes(inst.participant[1].required), force_bytes("required"))
        self.assertEqual(force_bytes(inst.participant[1].status), force_bytes("needs-action"))
        self.assertEqual(force_bytes(inst.participant[1].type[0].coding[0].code), force_bytes("ATND"))
        self.assertEqual(force_bytes(inst.participant[1].type[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ParticipationType"))
        self.assertEqual(force_bytes(inst.participant[2].required), force_bytes("required"))
        self.assertEqual(force_bytes(inst.participant[2].status), force_bytes("accepted"))
        self.assertEqual(inst.priority, 5)
        self.assertEqual(force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("413095006"))
        self.assertEqual(force_bytes(inst.reasonCode[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("Clinical Review"))
        self.assertEqual(inst.requestedPeriod[0].end.date, FHIRDate("2016-06-09").date)
        self.assertEqual(inst.requestedPeriod[0].end.as_json(), "2016-06-09")
        self.assertEqual(inst.requestedPeriod[0].start.date, FHIRDate("2016-06-02").date)
        self.assertEqual(inst.requestedPeriod[0].start.as_json(), "2016-06-02")
        self.assertEqual(force_bytes(inst.serviceCategory[0].coding[0].code), force_bytes("gp"))
        self.assertEqual(force_bytes(inst.serviceCategory[0].coding[0].display), force_bytes("General Practice"))
        self.assertEqual(force_bytes(inst.serviceCategory[0].coding[0].system), force_bytes("http://example.org/service-category"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("394814009"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("General practice"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.status), force_bytes("proposed"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Brian MRI results discussion</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

