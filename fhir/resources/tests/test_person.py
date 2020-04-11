# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Person
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import person
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class PersonTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Person", js["resourceType"])
        return person.Person(js)

    def testPerson1(self):
        inst = self.instantiate_from("person-patient-portal.json")
        self.assertIsNotNone(inst, "Must have instantiated a Person instance")
        self.implPerson1(inst)

        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson1(inst2)

    def implPerson1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Sandusky"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("USA"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("2086 College St")
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("44870"))
        self.assertEqual(force_bytes(inst.address[0].state), force_bytes("OH"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1974-03-07").date)
        self.assertEqual(inst.birthDate.as_json(), "1974-03-07")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("pp"))
        self.assertEqual(
            inst.identifier[0].period.start.date, FHIRDate("2041-09-23").date
        )
        self.assertEqual(inst.identifier[0].period.start.as_json(), "2041-09-23")
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.840.1.113883.4.3.39"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("DL")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text),
            force_bytes("Ohio driver license"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("TL545786"))
        self.assertEqual(force_bytes(inst.link[0].assurance), force_bytes("level3"))
        self.assertEqual(force_bytes(inst.link[1].assurance), force_bytes("level2"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Everywoman"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Eve"))
        self.assertEqual(force_bytes(inst.name[0].given[1]), force_bytes("Marie"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("home"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("(621)-479-9743")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPerson2(self):
        inst = self.instantiate_from("person-example-f002-ariadne.json")
        self.assertIsNotNone(inst, "Must have instantiated a Person instance")
        self.implPerson2(inst)

        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson2(inst2)

    def implPerson2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.birthDate.date, FHIRDate("1963").date)
        self.assertEqual(inst.birthDate.as_json(), "1963")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.name[0].text), force_bytes("Ariadne Bor-Jansma")
        )
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.photo.contentType), force_bytes("image/jpeg"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("home"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("+31201234567")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPerson3(self):
        inst = self.instantiate_from("person-provider-directory.json")
        self.assertIsNotNone(inst, "Must have instantiated a Person instance")
        self.implPerson3(inst)

        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson3(inst2)

    def implPerson3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Northfield"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("1003 Healthcare Drive")
        )
        self.assertEqual(force_bytes(inst.address[0].state), force_bytes("MN"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1959-04-22").date)
        self.assertEqual(inst.birthDate.as_json(), "1959-04-22")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("pd"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://hl7.org/fhir/sid/us-ssn"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("SS")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("444444444")
        )
        self.assertEqual(force_bytes(inst.link[0].assurance), force_bytes("level2"))
        self.assertEqual(force_bytes(inst.link[1].assurance), force_bytes("level2"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Hippocrates"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Harold"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("555-555-1003")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPerson4(self):
        inst = self.instantiate_from("person-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Person instance")
        self.implPerson4(inst)

        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson4(inst2)

    def implPerson4(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(
            force_bytes(inst.address[0].city), force_bytes("PleasantVille")
        )
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("534 Erewhon St")
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("3999"))
        self.assertEqual(force_bytes(inst.address[0].state), force_bytes("Vic"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1974-12-25").date)
        self.assertEqual(inst.birthDate.as_json(), "1974-12-25")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            inst.identifier[0].period.start.date, FHIRDate("2001-05-06").date
        )
        self.assertEqual(inst.identifier[0].period.start.as_json(), "2001-05-06")
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:1.2.36.146.595.217.0.1"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("MR")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Chalmers"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Peter"))
        self.assertEqual(force_bytes(inst.name[0].given[1]), force_bytes("James"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.name[1].given[0]), force_bytes("Jim"))
        self.assertEqual(force_bytes(inst.name[1].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("home"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[1].value), force_bytes("(03) 5555 6473")
        )
        self.assertEqual(force_bytes(inst.telecom[2].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[2].use), force_bytes("home"))
        self.assertEqual(
            force_bytes(inst.telecom[2].value), force_bytes("Jim@example.org")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPerson5(self):
        inst = self.instantiate_from("person-grahame.json")
        self.assertIsNotNone(inst, "Must have instantiated a Person instance")
        self.implPerson5(inst)

        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson5(inst2)

    def implPerson5(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(
            force_bytes(inst.address[0].city), force_bytes("PleasantVille")
        )
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("534 Erewhon St")
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("3999"))
        self.assertEqual(force_bytes(inst.address[0].state), force_bytes("Vic"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1974-12-25").date)
        self.assertEqual(inst.birthDate.as_json(), "1974-12-25")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("grahame"))
        self.assertEqual(
            inst.identifier[0].period.start.date, FHIRDate("2001-05-06").date
        )
        self.assertEqual(inst.identifier[0].period.start.as_json(), "2001-05-06")
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:1.2.36.146.595.217.0.1"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("MR")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Chalmers"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Peter"))
        self.assertEqual(force_bytes(inst.name[0].given[1]), force_bytes("James"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.name[1].given[0]), force_bytes("Jim"))
        self.assertEqual(force_bytes(inst.name[1].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("home"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[1].value), force_bytes("(03) 5555 6473")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
