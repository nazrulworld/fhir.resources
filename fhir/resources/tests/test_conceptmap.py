# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
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
        inst = self.instantiate_from("sc-valueset-publication-status.json")
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes('Canonical Mapping for "The lifecycle status of an artifact."'),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("entered-in-error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("draft")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("draft")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].code), force_bytes("retired")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code),
            force_bytes("inactive"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].code), force_bytes("unknown")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].code), force_bytes("unknown")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[4].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/publication-status"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/resource-status"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("sc-publication-status"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("PublicationStatusCanonicalMap")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/publication-status"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/resource-status"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes('Canonical Mapping for "PublicationStatus"'),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/sc-publication-status"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testConceptMap2(self):
        inst = self.instantiate_from("cm-address-use-v3.json")
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
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
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-AddressUse"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("cm-address-use-v3"))
        self.assertEqual(force_bytes(inst.name), force_bytes("v3.AddressUse"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/address-use"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://terminology.hl7.org/ValueSet/v3-AddressUse"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("v3 map for AddressUse"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-address-use-v3"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testConceptMap3(self):
        inst = self.instantiate_from("sc-valueset-fm-status.json")
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                'Canonical Mapping for "This value set includes Status codes."'
            ),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("entered-in-error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("draft")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("draft")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].code), force_bytes("cancelled")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code),
            force_bytes("abandoned"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/fm-status"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/resource-status"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("sc-fm-status"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("FinancialResourceStatusCodesCanonicalMap"),
        )
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Financial Management")
        )
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/fm-status"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/resource-status"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes('Canonical Mapping for "Financial Resource Status Codes"'),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/sc-fm-status"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testConceptMap4(self):
        inst = self.instantiate_from("cm-composition-status-v3.json")
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
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
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActStatus"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("cm-composition-status-v3"))
        self.assertEqual(force_bytes(inst.name), force_bytes("v3.CompositionStatus"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/composition-status"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://terminology.hl7.org/ValueSet/v3-ActStatus"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("v3 map for CompositionStatus")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-composition-status-v3"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testConceptMap5(self):
        inst = self.instantiate_from("sc-valueset-flag-status.json")
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                'Canonical Mapping for "Indicates whether this flag is active and needs to be displayed to a user, or whether it is no longer needed or was entered in error."'
            ),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("entered-in-error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("inactive")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code),
            force_bytes("inactive"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/flag-status"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/resource-status"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("sc-flag-status"))
        self.assertEqual(force_bytes(inst.name), force_bytes("FlagStatusCanonicalMap"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/flag-status"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/resource-status"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes('Canonical Mapping for "FlagStatus"')
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/sc-flag-status"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testConceptMap6(self):
        inst = self.instantiate_from("sc-valueset-device-status.json")
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                'Canonical Mapping for "The availability status of the device."'
            ),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("entered-in-error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("inactive")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code),
            force_bytes("inactive"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].code), force_bytes("unknown")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].code), force_bytes("unknown")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[3].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/device-status"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/resource-status"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("sc-device-status"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("FHIRDeviceStatusCanonicalMap")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/device-status"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/resource-status"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes('Canonical Mapping for "FHIRDeviceStatus"'),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/sc-device-status"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testConceptMap7(self):
        inst = self.instantiate_from("cm-contact-point-use-v2.json")
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
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
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0201"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("cm-contact-point-use-v2"))
        self.assertEqual(force_bytes(inst.name), force_bytes("v2.ContactPointUse"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/contact-point-use"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://terminology.hl7.org/ValueSet/v2-0201"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("v2 map for ContactPointUse")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v2"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testConceptMap8(self):
        inst = self.instantiate_from("sc-valueset-allergyintolerance-clinical.json")
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                'Canonical Mapping for "Preferred value set for AllergyIntolerance Clinical Status."'
            ),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("inactive")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code),
            force_bytes("inactive"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("resolved")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code),
            force_bytes("resolved"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical"
            ),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/resource-status"),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("sc-allergyintolerance-clinical")
        )
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("AllergyIntoleranceClinicalStatusCodesCanonicalMap"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project team"))
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/allergyintolerance-clinical"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/resource-status"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes(
                'Canonical Mapping for "AllergyIntolerance Clinical Status Codes"'
            ),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/ConceptMap/sc-allergyintolerance-clinical"
            ),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testConceptMap9(self):
        inst = self.instantiate_from("sc-valueset-medication-status.json")
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes('Canonical Mapping for "Medication Status Codes"'),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("entered-in-error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("error")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("inactive")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code),
            force_bytes("inactive"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/CodeSystem/medication-status"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/resource-status"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("sc-medication-status"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("Medication Status CodesCanonicalMap")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project team"))
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/medication-status"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/resource-status"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes('Canonical Mapping for "Medication  status  codes"'),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/sc-medication-status"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testConceptMap10(self):
        inst = self.instantiate_from("sc-valueset-location-status.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap10(inst)

        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap10(inst2)

    def implConceptMap10(self, inst):
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                'Canonical Mapping for "Indicates whether the location is still in use."'
            ),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].code), force_bytes("active")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[0].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].code), force_bytes("suspended")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].code),
            force_bytes("suspended"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[1].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].code), force_bytes("inactive")
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].code),
            force_bytes("inactive"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].element[2].target[0].equivalence),
            force_bytes("equivalent"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].source),
            force_bytes("http://hl7.org/fhir/location-status"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].target),
            force_bytes("http://hl7.org/fhir/resource-status"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("sc-location-status"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("LocationStatusCanonicalMap")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(
            force_bytes(inst.sourceCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/location-status"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.targetCanonical),
            force_bytes("http://hl7.org/fhir/ValueSet/resource-status"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes('Canonical Mapping for "LocationStatus"'),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ConceptMap/sc-location-status"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))
