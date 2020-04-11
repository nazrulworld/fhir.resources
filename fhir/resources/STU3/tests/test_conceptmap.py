# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import conceptmap
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ConceptMapTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ConceptMap", js["resourceType"])
        return conceptmap.ConceptMap(js)

    def testConceptMap1(self):
        inst = self.instantiate_from("cm-address-use-v3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap1(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap1(inst2)

    def implConceptMap1(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("home")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("H")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("WP")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("temp")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code), force_bytes("TMP")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(force_bytes(inst.group[0].element[3].code), force_bytes("old"))
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code), force_bytes("OLD")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].comment),
            force_bytes("Bad or Old"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("narrower"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[1].code), force_bytes("BAD")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[1].comment),
            force_bytes("Bad or Old"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[1].equivalence),
            force_bytes("narrower"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/address-use"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v3/AddressUse"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("cm-address-use-v3"))
        self.assertEqual(force_bytes(inst.name), force_bytes("v3 map for AddressUse"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-address-use-v3"),
        )

    def testConceptMap2(self):
        inst = self.instantiate_from("cm-medication-admin-status-v3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap2(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap2(inst2)

    def implConceptMap2(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("in-progress")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("on-hold")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code),
            force_bytes("suspended"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("completed")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code),
            force_bytes("completed"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].code), force_bytes("entered-in-error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code),
            force_bytes("nullified"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].code), force_bytes("stopped")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].code), force_bytes("aborted")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/medication-admin-status"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v3/ActStatus"),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("cm-medication-admin-status-v3")
        )
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("v3 map for MedicationAdministrationStatus"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-medication-admin-status-v3"),
        )

    def testConceptMap3(self):
        inst = self.instantiate_from("cm-medication-request-status-v3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap3(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap3(inst2)

    def implConceptMap3(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("on-hold")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code),
            force_bytes("suspended"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("cancelled")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code),
            force_bytes("cancelled"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].code), force_bytes("completed")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code),
            force_bytes("completed"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].code), force_bytes("entered-in-error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].code),
            force_bytes("nullified"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[5].code), force_bytes("stopped")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[5].target[0].code), force_bytes("aborted")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[5].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[6].code), force_bytes("draft")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[6].target[0].code), force_bytes("new")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[6].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/medication-request-status"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v3/ActStatus"),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("cm-medication-request-status-v3")
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("v3 map for MedicationRequestStatus")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/ConceptMap/cm-medication-request-status-v3"
            ),
        )

    def testConceptMap4(self):
        inst = self.instantiate_from("cm-observation-relationshiptypes-v3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap4(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap4(inst2)

    def implConceptMap4(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("has-member")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("MBR")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("DRIV")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("sequel-to")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code), force_bytes("SEQL")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].code), force_bytes("replaces")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code), force_bytes("RPLC")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].code), force_bytes("qualified-by")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].code), force_bytes("QUALF")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[5].code), force_bytes("interfered-by")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[5].target[0].code), force_bytes("INTF")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[5].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/observation-relationshiptypes"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v3/ActRelationshipType"),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("cm-observation-relationshiptypes-v3")
        )
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("v3 map for ObservationRelationshipType"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/ConceptMap/cm-observation-relationshiptypes-v3"
            ),
        )

    def testConceptMap5(self):
        inst = self.instantiate_from("cm-composition-status-v3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap5(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap5(inst2)

    def implConceptMap5(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("preliminary")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("final")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code),
            force_bytes("completed"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("wider"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("amended")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code),
            force_bytes("completed"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("wider"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].code), force_bytes("entered-in-error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code),
            force_bytes("nullified"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/composition-status"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v3/ActStatus"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("cm-composition-status-v3"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("v3 map for CompositionStatus")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-composition-status-v3"),
        )

    def testConceptMap6(self):
        inst = self.instantiate_from("cm-contact-point-use-v2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap6(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap6(inst2)

    def implConceptMap6(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("home")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("PRN")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("wider"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[1].code), force_bytes("ORN")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[1].equivalence),
            force_bytes("wider"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[2].code), force_bytes("VHN")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[2].equivalence),
            force_bytes("wider"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("WPN")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("mobile")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code), force_bytes("PRS")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/contact-point-use"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v2/0201"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("cm-contact-point-use-v2"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("v2 map for ContactPointUse")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v2"),
        )

    def testConceptMap7(self):
        inst = self.instantiate_from("cm-contact-point-use-v3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap7(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap7(inst2)

    def implConceptMap7(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("home")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("H")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("WP")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("temp")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code), force_bytes("TMP")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(force_bytes(inst.group[0].element[3].code), force_bytes("old"))
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code), force_bytes("OLD")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].comment),
            force_bytes("Old and Bad"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("narrower"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[1].code), force_bytes("BAD")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[1].comment),
            force_bytes("Old and Bad"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[1].equivalence),
            force_bytes("narrower"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].code), force_bytes("mobile")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].code), force_bytes("MC")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/contact-point-use"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v3/AddressUse"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("cm-contact-point-use-v3"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("v3 map for ContactPointUse")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v3"),
        )

    def testConceptMap8(self):
        inst = self.instantiate_from("cm-address-use-v2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap8(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap8(inst2)

    def implConceptMap8(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("home")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("H")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("O")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("temp")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code), force_bytes("C")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(force_bytes(inst.group[0].element[3].code), force_bytes("old"))
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code), force_bytes("BA")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].comment),
            force_bytes("unclear about old addresses"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("wider"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/address-use"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v2/0190"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("cm-address-use-v2"))
        self.assertEqual(force_bytes(inst.name), force_bytes("v2 map for AddressUse"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-address-use-v2"),
        )

    def testConceptMap9(self):
        inst = self.instantiate_from("cm-detectedissue-severity-v3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap9(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap9(inst2)

    def implConceptMap9(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("high")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("H")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("moderate")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("M")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(force_bytes(inst.group[0].element[2].code), force_bytes("low"))
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code), force_bytes("L")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equal"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/detectedissue-severity"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v3/ObservationValue"),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("cm-detectedissue-severity-v3")
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("v3 map for DetectedIssueSeverity")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-detectedissue-severity-v3"),
        )

    def testConceptMap10(self):
        inst = self.instantiate_from("conceptmap-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap10(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap10(inst2)

    def implConceptMap10(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].name),
            force_bytes("FHIR project team (example)"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("Creative Commons 0"))
        self.assertEqual(inst.date.date, FHIRDate("2012-06-13").date)
        self.assertEqual(inst.date.as_json(), "2012-06-13")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "A mapping between the FHIR and HL7 v3 AddressUse Code systems"
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("home")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].display), force_bytes("home")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("H")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].display), force_bytes("home")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].display), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("WP")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].display),
            force_bytes("work place"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("temp")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].display), force_bytes("temp")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code), force_bytes("TMP")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].display),
            force_bytes("temporary address"),
        )
        self.assertEqual(force_bytes(inst.group[0].element[3].code), force_bytes("old"))
        self.assertEqual(
            force_bytes(inst.group[0].element[3].display), force_bytes("old")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code), force_bytes("BAD")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].comment),
            force_bytes(
                "In the HL7 v3 AD, old is handled by the usablePeriod element, but you have to provide a time, there's no simple equivalent of flagging an address as old"
            ),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].display),
            force_bytes("bad address"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("disjoint"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/address-use"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/v3/AddressUse"),
        )
        self.assertEqual(force_bytes(inst.group[0].unmapped.code), force_bytes("temp"))
        self.assertEqual(
            force_bytes(inst.group[0].unmapped.display), force_bytes("temp")
        )
        self.assertEqual(force_bytes(inst.group[0].unmapped.mode), force_bytes("fixed"))
        self.assertEqual(force_bytes(inst.id), force_bytes("101"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:uuid:53cd62ee-033e-414c-9f58-3ca97b5ffc3b"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("FHIR-v3-Address-Use"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7, Inc"))
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes("To help implementers map from HL7 v3/CDA to FHIR"),
        )
        self.assertEqual(
            force_bytes(inst.sourceUri),
            force_bytes("http://hl7.org/fhir/ValueSet/address-use"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetUri),
            force_bytes("http://hl7.org/fhir/ValueSet/v3-AddressUse"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("FHIR/v3 Address Use Mapping")
        )
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/ConceptMap/101")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("venue")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.text),
            force_bytes("for CDA Usage"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("20120613"))
