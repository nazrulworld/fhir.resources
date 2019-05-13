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
from .. import immunization
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ImmunizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Immunization", js["resourceType"])
        return immunization.Immunization(js)
    
    def testImmunization1(self):
        inst = self.instantiate_from("immunization-example-refused.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization1(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization1(inst2)
    
    def implImmunization1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(force_bytes(inst.explanation.reasonNotGiven[0].coding[0].code), force_bytes("MEDPREC"))
        self.assertEqual(force_bytes(inst.explanation.reasonNotGiven[0].coding[0].display), force_bytes("medical precaution"))
        self.assertEqual(force_bytes(inst.explanation.reasonNotGiven[0].coding[0].system), force_bytes("http://hl7.org/fhir/v3/ActReason"))
        self.assertEqual(force_bytes(inst.id), force_bytes("notGiven"))
        self.assertTrue(inst.notGiven)
        self.assertTrue(inst.primarySource)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].code), force_bytes("01"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].display), force_bytes("DTP"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].system), force_bytes("http://hl7.org/fhir/sid/cvx"))
    
    def testImmunization2(self):
        inst = self.instantiate_from("immunization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization2(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization2(inst2)
    
    def implImmunization2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(force_bytes(inst.doseQuantity.code), force_bytes("mg"))
        self.assertEqual(force_bytes(inst.doseQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(inst.doseQuantity.value, 5)
        self.assertEqual(inst.expirationDate.date, FHIRDate("2015-02-15").date)
        self.assertEqual(inst.expirationDate.as_json(), "2015-02-15")
        self.assertEqual(force_bytes(inst.explanation.reason[0].coding[0].code), force_bytes("429060002"))
        self.assertEqual(force_bytes(inst.explanation.reason[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"))
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("AAJN11K"))
        self.assertFalse(inst.notGiven)
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Notes on adminstration of vaccine"))
        self.assertEqual(force_bytes(inst.practitioner[0].role.coding[0].code), force_bytes("OP"))
        self.assertEqual(force_bytes(inst.practitioner[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/v2/0443"))
        self.assertEqual(force_bytes(inst.practitioner[1].role.coding[0].code), force_bytes("AP"))
        self.assertEqual(force_bytes(inst.practitioner[1].role.coding[0].system), force_bytes("http://hl7.org/fhir/v2/0443"))
        self.assertTrue(inst.primarySource)
        self.assertEqual(inst.reaction[0].date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.reaction[0].date.as_json(), "2013-01-10")
        self.assertTrue(inst.reaction[0].reported)
        self.assertEqual(force_bytes(inst.route.coding[0].code), force_bytes("IM"))
        self.assertEqual(force_bytes(inst.route.coding[0].display), force_bytes("Injection, intramuscular"))
        self.assertEqual(force_bytes(inst.route.coding[0].system), force_bytes("http://hl7.org/fhir/v3/RouteOfAdministration"))
        self.assertEqual(force_bytes(inst.site.coding[0].code), force_bytes("LA"))
        self.assertEqual(force_bytes(inst.site.coding[0].display), force_bytes("left arm"))
        self.assertEqual(force_bytes(inst.site.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ActSite"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].description), force_bytes("Vaccination Protocol Sequence 1"))
        self.assertEqual(inst.vaccinationProtocol[0].doseSequence, 1)
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].doseStatus.coding[0].code), force_bytes("count"))
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].doseStatus.coding[0].display), force_bytes("Counts"))
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].doseStatus.coding[0].system), force_bytes("http://hl7.org/fhir/vaccination-protocol-dose-status"))
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].doseStatusReason.coding[0].code), force_bytes("coldchbrk"))
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].doseStatusReason.coding[0].display), force_bytes("Cold chain break"))
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].doseStatusReason.coding[0].system), force_bytes("http://hl7.org/fhir/vaccination-protocol-dose-status-reason"))
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].series), force_bytes("Vaccination Series 1"))
        self.assertEqual(inst.vaccinationProtocol[0].seriesDoses, 2)
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].targetDisease[0].coding[0].code), force_bytes("1857005"))
        self.assertEqual(force_bytes(inst.vaccinationProtocol[0].targetDisease[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].code), force_bytes("FLUVAX"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].system), force_bytes("urn:oid:1.2.36.1.2001.1005.17"))
        self.assertEqual(force_bytes(inst.vaccineCode.text), force_bytes("Fluvax (Influenza)"))
    
    def testImmunization3(self):
        inst = self.instantiate_from("immunization-example-historical.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization3(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization3(inst2)
    
    def implImmunization3(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-01-15").date)
        self.assertEqual(inst.date.as_json(), "2012-01-15")
        self.assertEqual(force_bytes(inst.id), force_bytes("historical"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"))
        self.assertFalse(inst.notGiven)
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Notes on adminstration of a historical vaccine"))
        self.assertFalse(inst.primarySource)
        self.assertEqual(force_bytes(inst.reportOrigin.coding[0].code), force_bytes("record"))
        self.assertEqual(force_bytes(inst.reportOrigin.coding[0].system), force_bytes("http://hl7.org/fhir/immunization-origin"))
        self.assertEqual(force_bytes(inst.reportOrigin.text), force_bytes("Written Record"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].code), force_bytes("GNFLU"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].system), force_bytes("urn:oid:1.2.36.1.2001.1005.17"))
        self.assertEqual(force_bytes(inst.vaccineCode.text), force_bytes("Influenza"))

