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
from .. import healthcareservice
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class HealthcareServiceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("HealthcareService", js["resourceType"])
        return healthcareservice.HealthcareService(js)
    
    def testHealthcareService1(self):
        inst = self.instantiate_from("healthcareservice-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a HealthcareService instance")
        self.implHealthcareService1(inst)
        
        js = inst.as_json()
        self.assertEqual("HealthcareService", js["resourceType"])
        inst2 = healthcareservice.HealthcareService(js)
        self.implHealthcareService1(inst2)
    
    def implHealthcareService1(self, inst):
        self.assertTrue(inst.active)
        self.assertFalse(inst.appointmentRequired)
        self.assertEqual(force_bytes(inst.availabilityExceptions), force_bytes("Reduced capacity is available during the Christmas period"))
        self.assertTrue(inst.availableTime[0].allDay)
        self.assertEqual(force_bytes(inst.availableTime[0].daysOfWeek[0]), force_bytes("wed"))
        self.assertEqual(inst.availableTime[1].availableEndTime.date, FHIRDate("05:30:00").date)
        self.assertEqual(inst.availableTime[1].availableEndTime.as_json(), "05:30:00")
        self.assertEqual(inst.availableTime[1].availableStartTime.date, FHIRDate("08:30:00").date)
        self.assertEqual(inst.availableTime[1].availableStartTime.as_json(), "08:30:00")
        self.assertEqual(force_bytes(inst.availableTime[1].daysOfWeek[0]), force_bytes("mon"))
        self.assertEqual(force_bytes(inst.availableTime[1].daysOfWeek[1]), force_bytes("tue"))
        self.assertEqual(force_bytes(inst.availableTime[1].daysOfWeek[2]), force_bytes("thu"))
        self.assertEqual(force_bytes(inst.availableTime[1].daysOfWeek[3]), force_bytes("fri"))
        self.assertEqual(inst.availableTime[2].availableEndTime.date, FHIRDate("04:30:00").date)
        self.assertEqual(inst.availableTime[2].availableEndTime.as_json(), "04:30:00")
        self.assertEqual(inst.availableTime[2].availableStartTime.date, FHIRDate("09:30:00").date)
        self.assertEqual(inst.availableTime[2].availableStartTime.as_json(), "09:30:00")
        self.assertEqual(force_bytes(inst.availableTime[2].daysOfWeek[0]), force_bytes("sat"))
        self.assertEqual(force_bytes(inst.availableTime[2].daysOfWeek[1]), force_bytes("fri"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("8"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Counselling"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/service-category"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Counselling"))
        self.assertEqual(force_bytes(inst.characteristic[0].coding[0].display), force_bytes("Wheelchair access"))
        self.assertEqual(force_bytes(inst.comment), force_bytes("Providing Specialist psychology services to the greater Den Burg area, many years of experience dealing with PTSD issues"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("DenBurg"))
        self.assertEqual(force_bytes(inst.eligibility[0].code.coding[0].display), force_bytes("DVA Required"))
        self.assertEqual(force_bytes(inst.eligibility[0].comment), force_bytes("Evidence of application for DVA status may be sufficient for commencing assessment"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/shared-ids"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("HS-12"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Consulting psychologists and/or psychology services"))
        self.assertEqual(force_bytes(inst.notAvailable[0].description), force_bytes("Christmas/Boxing Day"))
        self.assertEqual(inst.notAvailable[0].during.end.date, FHIRDate("2015-12-26").date)
        self.assertEqual(inst.notAvailable[0].during.end.as_json(), "2015-12-26")
        self.assertEqual(inst.notAvailable[0].during.start.date, FHIRDate("2015-12-25").date)
        self.assertEqual(inst.notAvailable[0].during.start.as_json(), "2015-12-25")
        self.assertEqual(force_bytes(inst.notAvailable[1].description), force_bytes("New Years Day"))
        self.assertEqual(inst.notAvailable[1].during.end.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.notAvailable[1].during.end.as_json(), "2016-01-01")
        self.assertEqual(inst.notAvailable[1].during.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.notAvailable[1].during.start.as_json(), "2016-01-01")
        self.assertEqual(force_bytes(inst.program[0].text), force_bytes("PTSD outreach"))
        self.assertEqual(force_bytes(inst.referralMethod[0].coding[0].code), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.referralMethod[0].coding[0].display), force_bytes("Phone"))
        self.assertEqual(force_bytes(inst.referralMethod[1].coding[0].code), force_bytes("fax"))
        self.assertEqual(force_bytes(inst.referralMethod[1].coding[0].display), force_bytes("Fax"))
        self.assertEqual(force_bytes(inst.referralMethod[2].coding[0].code), force_bytes("elec"))
        self.assertEqual(force_bytes(inst.referralMethod[2].coding[0].display), force_bytes("Secure Messaging"))
        self.assertEqual(force_bytes(inst.referralMethod[3].coding[0].code), force_bytes("semail"))
        self.assertEqual(force_bytes(inst.referralMethod[3].coding[0].display), force_bytes("Secure Email"))
        self.assertEqual(force_bytes(inst.serviceProvisionCode[0].coding[0].code), force_bytes("cost"))
        self.assertEqual(force_bytes(inst.serviceProvisionCode[0].coding[0].display), force_bytes("Fees apply"))
        self.assertEqual(force_bytes(inst.serviceProvisionCode[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/service-provision-conditions"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("47505003"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("Posttraumatic stress disorder"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("(555) silent"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[1].value), force_bytes("directaddress@example.com"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].code), force_bytes("394913002"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].display), force_bytes("Psychotherapy"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.type[1].coding[0].code), force_bytes("394587001"))
        self.assertEqual(force_bytes(inst.type[1].coding[0].display), force_bytes("Psychiatry"))
        self.assertEqual(force_bytes(inst.type[1].coding[0].system), force_bytes("http://snomed.info/sct"))

