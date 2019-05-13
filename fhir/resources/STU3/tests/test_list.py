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
from .. import list
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ListTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("List", js["resourceType"])
        return list.List(js)
    
    def testList1(self):
        inst = self.instantiate_from("list-example-empty.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList1(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList1(inst2)
    
    def implList1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("182836005"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Review of medication"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Medication Review"))
        self.assertEqual(inst.date.date, FHIRDate("2012-11-26T07:30:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-11-26T07:30:23+11:00")
        self.assertEqual(force_bytes(inst.emptyReason.coding[0].code), force_bytes("nilknown"))
        self.assertEqual(force_bytes(inst.emptyReason.coding[0].display), force_bytes("Nil Known"))
        self.assertEqual(force_bytes(inst.emptyReason.coding[0].system), force_bytes("http://hl7.org/fhir/list-empty-reason"))
        self.assertEqual(force_bytes(inst.emptyReason.text), force_bytes("The patient is not on any medications"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-empty"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("snapshot"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testList2(self):
        inst = self.instantiate_from("list-example-familyhistory-genetics-profile-annie.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList2(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList2(inst2)
    
    def implList2(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8670-2"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("History of family member diseases"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("image"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("1"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("2"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("3"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("4"))
        self.assertEqual(force_bytes(inst.contained[5].id), force_bytes("5"))
        self.assertEqual(force_bytes(inst.contained[6].id), force_bytes("6"))
        self.assertEqual(force_bytes(inst.contained[7].id), force_bytes("7"))
        self.assertEqual(force_bytes(inst.contained[8].id), force_bytes("8"))
        self.assertEqual(force_bytes(inst.contained[9].id), force_bytes("9"))
        self.assertEqual(force_bytes(inst.id), force_bytes("prognosis"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("snapshot"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testList3(self):
        inst = self.instantiate_from("list-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList3(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList3(inst2)
    
    def implList3(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-11-25T22:17:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-11-25T22:17:00+11:00")
        self.assertTrue(inst.entry[0].deleted)
        self.assertEqual(force_bytes(inst.entry[0].flag.text), force_bytes("Deleted due to error"))
        self.assertEqual(inst.entry[1].date.date, FHIRDate("2012-11-21").date)
        self.assertEqual(inst.entry[1].date.as_json(), "2012-11-21")
        self.assertEqual(force_bytes(inst.entry[1].flag.text), force_bytes("Added"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:uuid:a9fcea7c-fcdf-4d17-a5e0-f26dda030b59"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("23974652"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("changes"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testList4(self):
        inst = self.instantiate_from("list-example-double-cousin-relationship-pedigree.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList4(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList4(inst2)
    
    def implList4(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("80738-8"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("2"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("3"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("4"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("5"))
        self.assertEqual(force_bytes(inst.contained[5].id), force_bytes("6"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-double-cousin-relationship"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("snapshot"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testList5(self):
        inst = self.instantiate_from("list-example-simple-empty.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList5(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList5(inst2)
    
    def implList5(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("346638"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Patient Admission List"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://acme.com/list-codes"))
        self.assertEqual(inst.date.date, FHIRDate("2016-07-14T11:54:05+10:00").date)
        self.assertEqual(inst.date.as_json(), "2016-07-14T11:54:05+10:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("example-simple-empty"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("snapshot"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testList6(self):
        inst = self.instantiate_from("list-example-familyhistory-genetics-profile.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList6(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList6(inst2)
    
    def implList6(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8670-2"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("History of family member diseases"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("2"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("3"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("4"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("5"))
        self.assertEqual(force_bytes(inst.contained[5].id), force_bytes("6"))
        self.assertEqual(force_bytes(inst.contained[6].id), force_bytes("7"))
        self.assertEqual(force_bytes(inst.contained[7].id), force_bytes("8"))
        self.assertEqual(force_bytes(inst.id), force_bytes("genetic"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("snapshot"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testList7(self):
        inst = self.instantiate_from("list-example-familyhistory-f201-roel.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList7(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList7(inst2)
    
    def implList7(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8670-2"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("History of family member diseases"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("fmh-1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("fmh-2"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("snapshot"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Both parents, both brothers and both children (twin) are still alive."))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testList8(self):
        inst = self.instantiate_from("list-example-allergies.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList8(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList8(inst2)
    
    def implList8(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("52472-8"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Allergies and Adverse Drug Reactions"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Current Allergy List"))
        self.assertEqual(inst.date.date, FHIRDate("2015-07-14T23:10:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2015-07-14T23:10:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("current-allergies"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("working"))
        self.assertEqual(force_bytes(inst.orderedBy.coding[0].code), force_bytes("entry-date"))
        self.assertEqual(force_bytes(inst.orderedBy.coding[0].system), force_bytes("http://hl7.org/fhir/list-order"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Current Allergy List"))
    
    def testList9(self):
        inst = self.instantiate_from("list-example-medlist.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList9(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList9(inst2)
    
    def implList9(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("182836005"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Review of medication"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Medication Review"))
        self.assertEqual(inst.date.date, FHIRDate("2013-11-20T23:10:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2013-11-20T23:10:23+11:00")
        self.assertEqual(force_bytes(inst.entry[0].flag.coding[0].code), force_bytes("01"))
        self.assertEqual(force_bytes(inst.entry[0].flag.coding[0].display), force_bytes("Prescribed"))
        self.assertEqual(force_bytes(inst.entry[0].flag.coding[0].system), force_bytes("http://nehta.gov.au/codes/medications/changetype"))
        self.assertTrue(inst.entry[1].deleted)
        self.assertEqual(force_bytes(inst.entry[1].flag.coding[0].code), force_bytes("02"))
        self.assertEqual(force_bytes(inst.entry[1].flag.coding[0].display), force_bytes("Cancelled"))
        self.assertEqual(force_bytes(inst.entry[1].flag.coding[0].system), force_bytes("http://nehta.gov.au/codes/medications/changetype"))
        self.assertEqual(force_bytes(inst.id), force_bytes("med-list"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("changes"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

