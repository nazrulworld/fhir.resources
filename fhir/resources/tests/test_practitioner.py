# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Practitioner
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

from .. import practitioner
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class PractitionerTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Practitioner", js["resourceType"])
        return practitioner.Practitioner(js)

    def testPractitioner1(self):
        inst = self.instantiate_from("practitioner-example-f203-jvg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner1(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner1(inst2)

    def implPractitioner1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Den helder"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("NLD"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("Walvisbaai 3")
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("2333ZA"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("work"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1983-04-20").date)
        self.assertEqual(inst.birthDate.as_json(), "1983-04-20")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f203"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.528.1.1007.3.1"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("UZI-nummer")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("12345678903")
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].system),
            force_bytes("https://www.bigregister.nl/"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].type.text), force_bytes("BIG-nummer")
        )
        self.assertEqual(force_bytes(inst.identifier[1].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[1].value), force_bytes("12345678903")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].text), force_bytes("Juri van Gelder"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("+31715269111")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPractitioner2(self):
        inst = self.instantiate_from("practitioner-example-f201-ab.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner2(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner2(inst2)

    def implPractitioner2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Den helder"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("NLD"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("Walvisbaai 3")
        )
        self.assertEqual(
            force_bytes(inst.address[0].line[1]), force_bytes("C4 - Automatisering")
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("2333ZA"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("work"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1956-12-24").date)
        self.assertEqual(inst.birthDate.as_json(), "1956-12-24")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.528.1.1007.3.1"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("UZI-nummer")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("12345678901")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Bronsig"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Arend"))
        self.assertEqual(force_bytes(inst.name[0].prefix[0]), force_bytes("Dr."))
        self.assertEqual(force_bytes(inst.name[0].text), force_bytes("Dokter Bronsig"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.qualification[0].code.coding[0].code),
            force_bytes("41672002"),
        )
        self.assertEqual(
            force_bytes(inst.qualification[0].code.coding[0].display),
            force_bytes("Pulmonologist"),
        )
        self.assertEqual(
            force_bytes(inst.qualification[0].code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("+31715269111")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPractitioner3(self):
        inst = self.instantiate_from("practitioner-example-f202-lm.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner3(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner3(inst2)

    def implPractitioner3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Den helder"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("NLD"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("Walvisbaai 3")
        )
        self.assertEqual(
            force_bytes(inst.address[0].line[1]), force_bytes("C4 - Automatisering")
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("2333ZA"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("work"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1960-06-12").date)
        self.assertEqual(inst.birthDate.as_json(), "1960-06-12")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f202"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.528.1.1007.3.1"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("UZI-nummer")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("12345678902")
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].system),
            force_bytes("https://www.bigregister.nl/"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].type.text), force_bytes("BIG-nummer")
        )
        self.assertEqual(force_bytes(inst.identifier[1].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[1].value), force_bytes("12345678902")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Maas"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Luigi"))
        self.assertEqual(force_bytes(inst.name[0].prefix[0]), force_bytes("Dr."))
        self.assertEqual(force_bytes(inst.name[0].text), force_bytes("Luigi Maas"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("+31715269111")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPractitioner4(self):
        inst = self.instantiate_from("practitioner-example-xcda-author.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner4(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner4(inst2)

    def implPractitioner4(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("xcda-author"))
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
        self.assertEqual(force_bytes(inst.name[0].suffix[0]), force_bytes("MD"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPractitioner5(self):
        inst = self.instantiate_from("practitioner-example-f003-mv.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner5(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner5(inst2)

    def implPractitioner5(self, inst):
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Amsterdam"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("NLD"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("Galapagosweg 91")
        )
        self.assertEqual(
            force_bytes(inst.address[0].postalCode), force_bytes("1105 AZ")
        )
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("work"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1963-07-01").date)
        self.assertEqual(inst.birthDate.as_json(), "1963-07-01")
        self.assertEqual(
            force_bytes(inst.communication[0].coding[0].code), force_bytes("nl")
        )
        self.assertEqual(
            force_bytes(inst.communication[0].coding[0].display), force_bytes("Dutch")
        )
        self.assertEqual(
            force_bytes(inst.communication[0].coding[0].system),
            force_bytes("urn:ietf:bcp:47"),
        )
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f003"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.528.1.1007.3.1"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("846100293")
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].system),
            force_bytes("urn:oid:2.16.840.1.113883.2.4.6.3"),
        )
        self.assertEqual(force_bytes(inst.identifier[1].use), force_bytes("usual"))
        self.assertEqual(
            force_bytes(inst.identifier[1].value), force_bytes("243HID3RT938")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Versteegh"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Marc"))
        self.assertEqual(force_bytes(inst.name[0].suffix[0]), force_bytes("MD"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("0205562431"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[1].value), force_bytes("m.versteegh@bmc.nl")
        )
        self.assertEqual(force_bytes(inst.telecom[2].system), force_bytes("fax"))
        self.assertEqual(force_bytes(inst.telecom[2].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[2].value), force_bytes("0205662948"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPractitioner6(self):
        inst = self.instantiate_from("practitioner-example-f002-pv.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner6(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner6(inst2)

    def implPractitioner6(self, inst):
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Den Burg"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("NLD"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("Galapagosweg 91")
        )
        self.assertEqual(
            force_bytes(inst.address[0].postalCode), force_bytes("9105 PZ")
        )
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("work"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1979-04-29").date)
        self.assertEqual(inst.birthDate.as_json(), "1979-04-29")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.528.1.1007.3.1"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("730291637")
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].system),
            force_bytes("urn:oid:2.16.840.1.113883.2.4.6.3"),
        )
        self.assertEqual(force_bytes(inst.identifier[1].use), force_bytes("usual"))
        self.assertEqual(
            force_bytes(inst.identifier[1].value), force_bytes("174BIP3JH438")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Voigt"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Pieter"))
        self.assertEqual(force_bytes(inst.name[0].suffix[0]), force_bytes("MD"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("0205569336"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[1].value), force_bytes("p.voigt@bmc.nl")
        )
        self.assertEqual(force_bytes(inst.telecom[2].system), force_bytes("fax"))
        self.assertEqual(force_bytes(inst.telecom[2].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[2].value), force_bytes("0205669382"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPractitioner7(self):
        inst = self.instantiate_from("practitioner-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner7(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner7(inst2)

    def implPractitioner7(self, inst):
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
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.acme.org/practitioners"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("23"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Careful"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Adam"))
        self.assertEqual(force_bytes(inst.name[0].prefix[0]), force_bytes("Dr"))
        self.assertEqual(
            force_bytes(inst.qualification[0].code.coding[0].code), force_bytes("BS")
        )
        self.assertEqual(
            force_bytes(inst.qualification[0].code.coding[0].display),
            force_bytes("Bachelor of Science"),
        )
        self.assertEqual(
            force_bytes(inst.qualification[0].code.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0360/2.7"),
        )
        self.assertEqual(
            force_bytes(inst.qualification[0].code.text),
            force_bytes("Bachelor of Science"),
        )
        self.assertEqual(
            force_bytes(inst.qualification[0].identifier[0].system),
            force_bytes("http://example.org/UniversityIdentifier"),
        )
        self.assertEqual(
            force_bytes(inst.qualification[0].identifier[0].value), force_bytes("12345")
        )
        self.assertEqual(inst.qualification[0].period.start.date, FHIRDate("1995").date)
        self.assertEqual(inst.qualification[0].period.start.as_json(), "1995")
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPractitioner8(self):
        inst = self.instantiate_from("practitioner-example-f007-sh.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner8(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner8(inst2)

    def implPractitioner8(self, inst):
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Den Burg"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("NLD"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("Galapagosweg 91")
        )
        self.assertEqual(
            force_bytes(inst.address[0].postalCode), force_bytes("9105 PZ")
        )
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("work"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1971-11-07").date)
        self.assertEqual(inst.birthDate.as_json(), "1971-11-07")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f007"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.528.1.1007.3.1"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("874635264")
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].system),
            force_bytes("urn:oid:2.16.840.1.113883.2.4.6.3"),
        )
        self.assertEqual(force_bytes(inst.identifier[1].use), force_bytes("usual"))
        self.assertEqual(
            force_bytes(inst.identifier[1].value), force_bytes("567IUI51C154")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Heps"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Simone"))
        self.assertEqual(force_bytes(inst.name[0].suffix[0]), force_bytes("MD"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("020556936"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[1].value), force_bytes("S.M.Heps@bmc.nl")
        )
        self.assertEqual(force_bytes(inst.telecom[2].system), force_bytes("fax"))
        self.assertEqual(force_bytes(inst.telecom[2].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[2].value), force_bytes("0205669283"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPractitioner9(self):
        inst = self.instantiate_from("practitioner-example-f204-ce.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner9(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner9(inst2)

    def implPractitioner9(self, inst):
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Den helder"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("NLD"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("Walvisbaai 3")
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("2333ZA"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("work"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1967-11-05").date)
        self.assertEqual(inst.birthDate.as_json(), "1967-11-05")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f204"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.528.1.1007.3.1"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("UZI-nummer")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("12345678904")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].text), force_bytes("Carla Espinosa"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("+31715262169")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPractitioner10(self):
        inst = self.instantiate_from("practitioner-example-xcda1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner10(inst)

        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner10(inst2)

    def implPractitioner10(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("xcda1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://healthcare.example.org/identifiers/staff"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("D234123"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Dopplemeyer"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Sherry"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("email"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value),
            force_bytes("john.doe@healthcare.example.org"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
