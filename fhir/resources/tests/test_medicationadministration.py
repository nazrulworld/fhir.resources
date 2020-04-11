# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration
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

from .. import medicationadministration
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MedicationAdministrationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("MedicationAdministration", js["resourceType"])
        return medicationadministration.MedicationAdministration(js)

    def testMedicationAdministration1(self):
        inst = self.instantiate_from("medicationadministration0301.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration1(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration1(inst2)

    def implMedicationAdministration1(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0301"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("signature"))
        self.assertEqual(force_bytes(inst.dosage.dose.code), force_bytes("mg"))
        self.assertEqual(
            force_bytes(inst.dosage.dose.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.dosage.dose.unit), force_bytes("mg"))
        self.assertEqual(inst.dosage.dose.value, 500)
        self.assertEqual(force_bytes(inst.dosage.method.text), force_bytes("IV Push"))
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].code), force_bytes("47625008")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].display),
            force_bytes("Intravenous route (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.text), force_bytes("500mg IV q6h x 3 days")
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T14:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T14:30:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadmin0301"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("b")
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].display),
            force_bytes("Given as Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/reason-medication-given"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationAdministration2(self):
        inst = self.instantiate_from("medicationadministrationexample3.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration2(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration2(inst2)

    def implMedicationAdministration2(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0303"))
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2015-01-15T14:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2015-01-15T14:30:00+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T14:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T14:30:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadminexample03"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.note[0].text),
            force_bytes(
                "Patient started Bupropion this morning - will administer in a reduced dose tomorrow"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("on-hold"))
        self.assertEqual(
            force_bytes(inst.statusReason[0].coding[0].code), force_bytes("373147003")
        )
        self.assertEqual(
            force_bytes(inst.statusReason[0].coding[0].display),
            force_bytes(
                "Administration of medication not done due to a contraindication (situation)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.statusReason[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationAdministration3(self):
        inst = self.instantiate_from("medicationadministration0307.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration3(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration3(inst2)

    def implMedicationAdministration3(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0313"))
        self.assertEqual(force_bytes(inst.dosage.dose.code), force_bytes("mg"))
        self.assertEqual(
            force_bytes(inst.dosage.dose.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.dosage.dose.unit), force_bytes("mg"))
        self.assertEqual(inst.dosage.dose.value, 7)
        self.assertEqual(
            force_bytes(inst.dosage.method.coding[0].code), force_bytes("420620005")
        )
        self.assertEqual(
            force_bytes(inst.dosage.method.coding[0].display),
            force_bytes("Push - dosing instruction imperative (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.method.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.dosage.rateQuantity.code), force_bytes("min"))
        self.assertEqual(
            force_bytes(inst.dosage.rateQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.dosage.rateQuantity.unit), force_bytes("min"))
        self.assertEqual(inst.dosage.rateQuantity.value, 4)
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].code), force_bytes("255560000")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].display), force_bytes("Intravenous")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.text),
            force_bytes(
                "0.05 - 0.1mg/kg IV over 2-5 minutes every 15 minutes as needed"
            ),
        )
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2015-01-15T14:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2015-01-15T14:30:00+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T04:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T04:30:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadmin0307"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.performer[0].function.coding[0].code),
            force_bytes("performer"),
        )
        self.assertEqual(
            force_bytes(inst.performer[0].function.coding[0].display),
            force_bytes("Performer"),
        )
        self.assertEqual(
            force_bytes(inst.performer[0].function.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/med-admin-perform-function"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationAdministration4(self):
        inst = self.instantiate_from("medicationadministration0311.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration4(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration4(inst2)

    def implMedicationAdministration4(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0304"))
        self.assertEqual(force_bytes(inst.dosage.dose.code), force_bytes("TAB"))
        self.assertEqual(
            force_bytes(inst.dosage.dose.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(force_bytes(inst.dosage.dose.unit), force_bytes("TAB"))
        self.assertEqual(inst.dosage.dose.value, 1)
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].code), force_bytes("26643006")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].display), force_bytes("Oral Route")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.text),
            force_bytes(
                "0.25mg PO every 6-12 hours as needed for menses from Jan 15-20, 2015.  Do not exceed more than 4mg per day"
            ),
        )
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2015-01-16T02:03:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2015-01-16T02:03:00+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T22:03:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T22:03:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadmin0311"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("266599000")
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].display),
            force_bytes("Dysmenorrhea"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationAdministration5(self):
        inst = self.instantiate_from("medicationadministration0310.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration5(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration5(inst2)

    def implMedicationAdministration5(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0304"))
        self.assertEqual(force_bytes(inst.dosage.dose.code), force_bytes("mg"))
        self.assertEqual(
            force_bytes(inst.dosage.dose.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.dosage.dose.unit), force_bytes("mg"))
        self.assertEqual(inst.dosage.dose.value, 6)
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].code), force_bytes("26643006")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].display),
            force_bytes("Oral route (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.text),
            force_bytes(
                "6 mg PO daily for remission induction; adjust dosage to white blood cell (WBC) count.  With hold treatment if WBC is less than 15,000/µL; resume when WBC is greater than 50,000/µL"
            ),
        )
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2015-01-16T02:03:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2015-01-16T02:03:00+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T22:03:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T22:03:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadmin0310"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationAdministration6(self):
        inst = self.instantiate_from("medicationadministration0306.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration6(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration6(inst2)

    def implMedicationAdministration6(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0306"))
        self.assertEqual(force_bytes(inst.dosage.dose.code), force_bytes("TAB"))
        self.assertEqual(
            force_bytes(inst.dosage.dose.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(force_bytes(inst.dosage.dose.unit), force_bytes("TAB"))
        self.assertEqual(inst.dosage.dose.value, 2)
        self.assertEqual(
            force_bytes(inst.dosage.method.coding[0].code), force_bytes("421521009")
        )
        self.assertEqual(
            force_bytes(inst.dosage.method.coding[0].display),
            force_bytes("Swallow - dosing instruction imperative (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.method.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].code), force_bytes("26643006")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].display), force_bytes("Oral Route")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.text), force_bytes("Two tablets at once")
        )
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2015-01-15T14:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2015-01-15T14:30:00+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T04:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T04:30:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadmin0306"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.performer[0].function.coding[0].code),
            force_bytes("performer"),
        )
        self.assertEqual(
            force_bytes(inst.performer[0].function.coding[0].display),
            force_bytes("Performer"),
        )
        self.assertEqual(
            force_bytes(inst.performer[0].function.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/med-admin-perform-function"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationAdministration7(self):
        inst = self.instantiate_from("medicationadministration0309.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration7(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration7(inst2)

    def implMedicationAdministration7(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0318"))
        self.assertEqual(force_bytes(inst.dosage.dose.code), force_bytes("mL"))
        self.assertEqual(
            force_bytes(inst.dosage.dose.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.dosage.dose.unit), force_bytes("mL"))
        self.assertEqual(inst.dosage.dose.value, 1000)
        self.assertEqual(force_bytes(inst.dosage.method.text), force_bytes("PICC line"))
        self.assertEqual(
            force_bytes(inst.dosage.rateRatio.denominator.code), force_bytes("h")
        )
        self.assertEqual(
            force_bytes(inst.dosage.rateRatio.denominator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.rateRatio.denominator.unit), force_bytes("h")
        )
        self.assertEqual(inst.dosage.rateRatio.denominator.value, 1)
        self.assertEqual(
            force_bytes(inst.dosage.rateRatio.numerator.code), force_bytes("mL")
        )
        self.assertEqual(
            force_bytes(inst.dosage.rateRatio.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.rateRatio.numerator.unit), force_bytes("mL")
        )
        self.assertEqual(inst.dosage.rateRatio.numerator.value, 50)
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].code), force_bytes("255560000")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].display), force_bytes("Intravenous")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.site.coding[0].code), force_bytes("6073002")
        )
        self.assertEqual(
            force_bytes(inst.dosage.site.coding[0].display),
            force_bytes("Structure of ligament of left superior vena cava"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.site.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.text),
            force_bytes("1000mL infused at 50ml/hour for 4 hours - hung at 2200 hours"),
        )
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2015-01-16T02:03:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2015-01-16T02:03:00+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T22:03:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T22:03:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadmin0309"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.performer[0].function.coding[0].code),
            force_bytes("performer"),
        )
        self.assertEqual(
            force_bytes(inst.performer[0].function.coding[0].display),
            force_bytes("Performer"),
        )
        self.assertEqual(
            force_bytes(inst.performer[0].function.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/med-admin-perform-function"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationAdministration8(self):
        inst = self.instantiate_from("medicationadministration0313.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration8(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration8(inst2)

    def implMedicationAdministration8(self, inst):
        self.assertEqual(force_bytes(inst.dosage.dose.code), force_bytes("mg"))
        self.assertEqual(
            force_bytes(inst.dosage.dose.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.dosage.dose.unit), force_bytes("mg"))
        self.assertEqual(inst.dosage.dose.value, 240)
        self.assertEqual(
            force_bytes(inst.dosage.site.coding[0].code), force_bytes("34402009")
        )
        self.assertEqual(
            force_bytes(inst.dosage.site.coding[0].display),
            force_bytes("Rectum structure"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.site.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.text),
            force_bytes(
                "Insert one suppository rectally twice daily as needed for fever to a maximim of 3 per day"
            ),
        )
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2015-01-16T02:03:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2015-01-16T02:03:00+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T22:03:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T22:03:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadmin0313"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("322254008"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Paracetamol 240mg suppository (product)"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("c")
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].display), force_bytes("Emergency")
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/reason-medication-given"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationAdministration9(self):
        inst = self.instantiate_from("medicationadministration0305.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration9(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration9(inst2)

    def implMedicationAdministration9(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0306"))
        self.assertEqual(force_bytes(inst.dosage.dose.code), force_bytes("mg/kg"))
        self.assertEqual(
            force_bytes(inst.dosage.dose.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.dosage.dose.unit), force_bytes("mg/kg"))
        self.assertEqual(inst.dosage.dose.value, 1.8)
        self.assertEqual(force_bytes(inst.dosage.rateQuantity.code), force_bytes("min"))
        self.assertEqual(
            force_bytes(inst.dosage.rateQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.dosage.rateQuantity.unit), force_bytes("min"))
        self.assertEqual(inst.dosage.rateQuantity.value, 20)
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].code), force_bytes("255560000")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].display), force_bytes("Intravenous")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.text),
            force_bytes("1.8 mg/kg IV infusion over 30 minutes"),
        )
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2015-01-15T14:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2015-01-15T14:30:00+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T04:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T04:30:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadmin0305"))
        self.assertEqual(
            force_bytes(inst.instantiates[0]),
            force_bytes(
                "http://www.bccancer.bc.ca/chemotherapy-protocols-site/Documents/Lymphoma-Myeloma/ULYBRENTUX%20Protocol_1Jun2017.pdf"
            ),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationAdministration10(self):
        inst = self.instantiate_from("medicationadministration0304.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationAdministration instance"
        )
        self.implMedicationAdministration10(inst)

        js = inst.as_json()
        self.assertEqual("MedicationAdministration", js["resourceType"])
        inst2 = medicationadministration.MedicationAdministration(js)
        self.implMedicationAdministration10(inst2)

    def implMedicationAdministration10(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0303"))
        self.assertEqual(force_bytes(inst.dosage.dose.code), force_bytes("mg"))
        self.assertEqual(
            force_bytes(inst.dosage.dose.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.dosage.dose.unit), force_bytes("mg"))
        self.assertEqual(inst.dosage.dose.value, 3)
        self.assertEqual(
            force_bytes(inst.dosage.method.coding[0].code), force_bytes("422145002")
        )
        self.assertEqual(
            force_bytes(inst.dosage.method.coding[0].display),
            force_bytes("Inject - dosing instruction imperative (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.method.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].code), force_bytes("47625008")
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].display),
            force_bytes("Intravenous route (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage.text),
            force_bytes(
                "Rapid daily-dose escalation, until tolerated, from 3 mg/d, and then 10 mg/d, to the recommended maintenance dose of 30 mg IV over 120 min, 3 times per wk on alternate days for up to 12 wk"
            ),
        )
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2015-01-15T14:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2015-01-15T14:30:00+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2015-01-15T04:30:00+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2015-01-15T04:30:00+01:00"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medadmin0304"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
