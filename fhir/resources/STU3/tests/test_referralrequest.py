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
from .. import referralrequest
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ReferralRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ReferralRequest", js["resourceType"])
        return referralrequest.ReferralRequest(js)
    
    def testReferralRequest1(self):
        inst = self.instantiate_from("referralrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ReferralRequest instance")
        self.implReferralRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ReferralRequest", js["resourceType"])
        inst2 = referralrequest.ReferralRequest(js)
        self.implReferralRequest1(inst2)
    
    def implReferralRequest1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.authoredOn.as_json(), "2014-02-14")
        self.assertEqual(force_bytes(inst.description), force_bytes("In the past 2 years Beverly has had 6 instances of r) sided Otitis media. She is     falling behind her peers at school, and displaying some learning difficulties."))
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("1234"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://orionhealth.com/fhir/apps/referralids"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("ret4421"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(inst.occurrencePeriod.end.date, FHIRDate("2014-03-14").date)
        self.assertEqual(inst.occurrencePeriod.end.as_json(), "2014-03-14")
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("For consideration of Grommets"))
        self.assertEqual(force_bytes(inst.serviceRequested[0].coding[0].code), force_bytes("172676009"))
        self.assertEqual(force_bytes(inst.serviceRequested[0].coding[0].display), force_bytes("Myringotomy and insertion of tympanic ventilation tube"))
        self.assertEqual(force_bytes(inst.serviceRequested[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.serviceRequested[0].text), force_bytes("Insertion of grommets"))
        self.assertEqual(force_bytes(inst.specialty.coding[0].code), force_bytes("ent"))
        self.assertEqual(force_bytes(inst.specialty.coding[0].display), force_bytes("ENT"))
        self.assertEqual(force_bytes(inst.specialty.coding[0].system), force_bytes("http://orionhealth.com/fhir/apps/specialties"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Referral to Dr Dave for Beverly weaver to have grommets inserted in her r) ear</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("103696004"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Patient referral to specialist"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://snomed.info/sct"))

