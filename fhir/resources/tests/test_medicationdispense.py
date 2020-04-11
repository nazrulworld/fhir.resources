# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense
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

from .. import medicationdispense
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MedicationDispenseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("MedicationDispense", js["resourceType"])
        return medicationdispense.MedicationDispense(js)

    def testMedicationDispense1(self):
        inst = self.instantiate_from("medicationdispense0317.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense1(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense1(inst2)

    def implMedicationDispense1(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0306"))
        self.assertEqual(force_bytes(inst.daysSupply.code), force_bytes("d"))
        self.assertEqual(
            force_bytes(inst.daysSupply.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.daysSupply.unit), force_bytes("Day"))
        self.assertEqual(inst.daysSupply.value, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("mg/kg"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("mg/kg"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 1.8
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].code),
            force_bytes("255560000"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].display),
            force_bytes("Intravenous"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes(
                "1.8 mg/kg IV infusion over 30 minutes every 3 weeks for 16 cycles"
            ),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.count, 16)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 3)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("wk"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp0317"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.quantity.code), force_bytes("415818005"))
        self.assertEqual(
            force_bytes(inst.quantity.system), force_bytes("http://snomed.info/sct")
        )
        self.assertEqual(inst.quantity.value, 3)
        self.assertEqual(force_bytes(inst.status), force_bytes("stopped"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("TF"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Trial Fill")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(
            inst.whenHandedOver.date, FHIRDate("2015-06-26T07:13:00+05:00").date
        )
        self.assertEqual(inst.whenHandedOver.as_json(), "2015-06-26T07:13:00+05:00")
        self.assertEqual(
            inst.whenPrepared.date, FHIRDate("2015-06-25T07:13:00+05:00").date
        )
        self.assertEqual(inst.whenPrepared.as_json(), "2015-06-25T07:13:00+05:00")

    def testMedicationDispense2(self):
        inst = self.instantiate_from("medicationdispense0301.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense2(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense2(inst2)

    def implMedicationDispense2(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0301"))
        self.assertEqual(force_bytes(inst.daysSupply.code), force_bytes("d"))
        self.assertEqual(
            force_bytes(inst.daysSupply.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.daysSupply.unit), force_bytes("Day"))
        self.assertEqual(inst.daysSupply.value, 3)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("mg"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("mg"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 500
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].method.coding[0].code),
            force_bytes("420620005"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].method.coding[0].display),
            force_bytes("Push - dosing instruction imperative (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].method.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].code),
            force_bytes("255560000"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].display),
            force_bytes("Intravenous"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes("500mg IV q6h x 3 days"),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 6)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("h"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp0301"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.quantity.code), force_bytes("Vial"))
        self.assertEqual(
            force_bytes(inst.quantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(force_bytes(inst.quantity.unit), force_bytes("Vial"))
        self.assertEqual(inst.quantity.value, 12)
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("EM"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Emergency Supply")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(inst.whenPrepared.date, FHIRDate("2015-01-15T10:20:00Z").date)
        self.assertEqual(inst.whenPrepared.as_json(), "2015-01-15T10:20:00Z")

    def testMedicationDispense3(self):
        inst = self.instantiate_from("medicationdispense0321.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense3(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense3(inst2)

    def implMedicationDispense3(self, inst):
        self.assertEqual(force_bytes(inst.daysSupply.code), force_bytes("d"))
        self.assertEqual(
            force_bytes(inst.daysSupply.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.daysSupply.unit), force_bytes("Day"))
        self.assertEqual(inst.daysSupply.value, 10)
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].additionalInstruction[0].coding[0].code
            ),
            force_bytes("418914006"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].additionalInstruction[0].coding[0].display
            ),
            force_bytes(
                "Warning. May cause drowsiness. If affected do not drive or operate machinery. Avoid alcoholic drink (qualifier value)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].additionalInstruction[0].coding[0].system
            ),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code
            ),
            force_bytes("203082005"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
            ),
            force_bytes("Fibromyalgia (disorder)"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
            ),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("TAB"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("TAB"),
        )
        self.assertEqual(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].code),
            force_bytes("26643006"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].display),
            force_bytes("Oral Route"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes("1 tablet every four hours as needed for pain"),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 4)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("h"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp0321"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("49999-051-30"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Vicodin 5mg Hydrocodone, 500mg Acetaminophen tablet "),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/ndc"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.quantity.code), force_bytes("TAB"))
        self.assertEqual(
            force_bytes(inst.quantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(inst.quantity.value, 30)
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("RFP"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Refill - Part Fill")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(inst.whenPrepared.date, FHIRDate("2015-01-15T10:20:00Z").date)
        self.assertEqual(inst.whenPrepared.as_json(), "2015-01-15T10:20:00Z")

    def testMedicationDispense4(self):
        inst = self.instantiate_from("medicationdispense0320.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense4(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense4(inst2)

    def implMedicationDispense4(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0318"))
        self.assertEqual(force_bytes(inst.daysSupply.code), force_bytes("d"))
        self.assertEqual(
            force_bytes(inst.daysSupply.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.daysSupply.unit), force_bytes("Day"))
        self.assertEqual(inst.daysSupply.value, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("mL"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("mL"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 1000
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.code
            ),
            force_bytes("h"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.system
            ),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.unit
            ),
            force_bytes("h"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.value, 1
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.code
            ),
            force_bytes("mL"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.system
            ),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.unit
            ),
            force_bytes("mL"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.value, 50
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].code),
            force_bytes("255560000"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].display),
            force_bytes("Intravenous"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes("1000mL infused at 50ml/hour for 4 hours - hang at 2200 hours"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].timing.event[0].date,
            FHIRDate("2015-01-15T22:00:00+11:00").date,
        )
        self.assertEqual(
            inst.dosageInstruction[0].timing.event[0].as_json(),
            "2015-01-15T22:00:00+11:00",
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 24)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("h"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp0320"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.quantity.code), force_bytes("ml"))
        self.assertEqual(
            force_bytes(inst.quantity.system), force_bytes("http://unitsofmeasure.org")
        )
        self.assertEqual(inst.quantity.value, 1000)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            inst.whenHandedOver.date, FHIRDate("2015-03-17T17:13:00+05:00").date
        )
        self.assertEqual(inst.whenHandedOver.as_json(), "2015-03-17T17:13:00+05:00")
        self.assertEqual(
            inst.whenPrepared.date, FHIRDate("2015-03-16T17:13:00+05:00").date
        )
        self.assertEqual(inst.whenPrepared.as_json(), "2015-03-16T17:13:00+05:00")

    def testMedicationDispense5(self):
        inst = self.instantiate_from("medicationdispense0316.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense5(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense5(inst2)

    def implMedicationDispense5(self, inst):
        self.assertEqual(force_bytes(inst.daysSupply.code), force_bytes("d"))
        self.assertEqual(
            force_bytes(inst.daysSupply.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.daysSupply.unit), force_bytes("Day"))
        self.assertEqual(inst.daysSupply.value, 30)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("U"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("U"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 20
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].code),
            force_bytes("263887005"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].display),
            force_bytes("Subcutaneous (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes("20 Units SC three times daily"),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 3)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp0316"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("285018"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Lantus 100 unit/ml injectable solution"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].system),
            force_bytes("http://www.nlm.nih.gov/research/umls/rxnorm"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.quantity.code), force_bytes("ml"))
        self.assertEqual(
            force_bytes(inst.quantity.system), force_bytes("http://unitsofmeasure.org")
        )
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("RFP"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Refill - Part Fill")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(
            inst.whenPrepared.date, FHIRDate("2015-06-25T07:13:00+05:00").date
        )
        self.assertEqual(inst.whenPrepared.as_json(), "2015-06-25T07:13:00+05:00")

    def testMedicationDispense6(self):
        inst = self.instantiate_from("medicationdispense0327.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense6(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense6(inst2)

    def implMedicationDispense6(self, inst):
        self.assertEqual(force_bytes(inst.daysSupply.code), force_bytes("d"))
        self.assertEqual(
            force_bytes(inst.daysSupply.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.daysSupply.unit), force_bytes("Day"))
        self.assertEqual(inst.daysSupply.value, 30)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].additionalInstruction[0].text),
            force_bytes("Shake Well"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("ea"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("ea"),
        )
        self.assertEqual(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes("Use two sprays twice daily"),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 2)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp0327"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("746763"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes(
                "Proventil 0.09mg/actuat (Albuterol sulfate 0.108mg/actuat from mouthpiece)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].system),
            force_bytes("http://www.nlm.nih.gov/research/umls/rxnorm"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.quantity.code), force_bytes("ml"))
        self.assertEqual(
            force_bytes(inst.quantity.system), force_bytes("http://unitsofmeasure.org")
        )
        self.assertEqual(inst.quantity.value, 30)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("TF"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Trial Fill")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(
            inst.whenHandedOver.date, FHIRDate("2015-01-15T16:20:00Z").date
        )
        self.assertEqual(inst.whenHandedOver.as_json(), "2015-01-15T16:20:00Z")
        self.assertEqual(inst.whenPrepared.date, FHIRDate("2015-01-15T10:20:00Z").date)
        self.assertEqual(inst.whenPrepared.as_json(), "2015-01-15T10:20:00Z")

    def testMedicationDispense7(self):
        inst = self.instantiate_from("medicationdispenseexample8.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense7(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense7(inst2)

    def implMedicationDispense7(self, inst):
        self.assertEqual(
            force_bytes(inst.contained[0].id), force_bytes("medexample015")
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("mg"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("mg"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 500
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].code),
            force_bytes("394899003"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].display),
            force_bytes("oral administration of treatment"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 2)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 21)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp008"))
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

    def testMedicationDispense8(self):
        inst = self.instantiate_from("medicationdispense0331.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense8(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense8(inst2)

    def implMedicationDispense8(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0352"))
        self.assertEqual(force_bytes(inst.daysSupply.code), force_bytes("d"))
        self.assertEqual(
            force_bytes(inst.daysSupply.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.daysSupply.unit), force_bytes("Day"))
        self.assertEqual(inst.daysSupply.value, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].additionalInstruction[0].text),
            force_bytes(
                "Take along with one 2mg Coumadin tablet for a total daily dose of 7mg as prescribed by physician"
            ),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("mg"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("mg"),
        )
        self.assertEqual(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 2)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes("7mg (=one 5mg tablet PLUS one 2mg tablet) once daily"),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp0331"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.quantity.code), force_bytes("415818006"))
        self.assertEqual(
            force_bytes(inst.quantity.system), force_bytes("http://snomed.info/sct")
        )
        self.assertEqual(inst.quantity.value, 1)
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("DF"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Daily Fill")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(inst.whenPrepared.date, FHIRDate("2015-01-15T10:20:00Z").date)
        self.assertEqual(inst.whenPrepared.as_json(), "2015-01-15T10:20:00Z")

    def testMedicationDispense9(self):
        inst = self.instantiate_from("medicationdispense0311.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense9(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense9(inst2)

    def implMedicationDispense9(self, inst):
        self.assertEqual(force_bytes(inst.daysSupply.code), force_bytes("d"))
        self.assertEqual(
            force_bytes(inst.daysSupply.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.daysSupply.unit), force_bytes("Day"))
        self.assertEqual(inst.daysSupply.value, 10)
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].additionalInstruction[0].coding[0].code
            ),
            force_bytes("418637003"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].additionalInstruction[0].coding[0].display
            ),
            force_bytes(
                "Do not take with any other paracetamol products (qualifier value)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].additionalInstruction[0].coding[0].system
            ),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code
            ),
            force_bytes("386661006"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
            ),
            force_bytes("Fever (finding)"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
            ),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("mg"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("mg"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 240
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].maxDosePerPeriod.denominator.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].maxDosePerPeriod.denominator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].maxDosePerPeriod.denominator.value, 1
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].maxDosePerPeriod.numerator.code),
            force_bytes("mg"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].maxDosePerPeriod.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].maxDosePerPeriod.numerator.value, 720
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes(
                "Insert two suppositories (240mg) rectally twice daily as needed for fever to a maximim of 6 per day"
            ),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 2)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp0311"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("50090-0001"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Acetaminophen 120mg Suppository"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/ndc"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.quantity.code), force_bytes("RECSUPP"))
        self.assertEqual(
            force_bytes(inst.quantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(inst.quantity.value, 60)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("RFP"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Refill - Part Fill")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(
            inst.whenHandedOver.date, FHIRDate("2015-01-15T16:20:00Z").date
        )
        self.assertEqual(inst.whenHandedOver.as_json(), "2015-01-15T16:20:00Z")
        self.assertEqual(inst.whenPrepared.date, FHIRDate("2015-01-15T10:20:00Z").date)
        self.assertEqual(inst.whenPrepared.as_json(), "2015-01-15T10:20:00Z")

    def testMedicationDispense10(self):
        inst = self.instantiate_from("medicationdispense0307.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationDispense instance"
        )
        self.implMedicationDispense10(inst)

        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense10(inst2)

    def implMedicationDispense10(self, inst):
        self.assertEqual(force_bytes(inst.daysSupply.code), force_bytes("d"))
        self.assertEqual(
            force_bytes(inst.daysSupply.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.daysSupply.unit), force_bytes("Day"))
        self.assertEqual(inst.daysSupply.value, 30)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("mg"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("mg"),
        )
        self.assertEqual(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 6)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].code),
            force_bytes("calculated"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].type.coding[0].display
            ),
            force_bytes("Calculated"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes("Take 3 tablets (6mg) once daily"),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("meddisp0307"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("76388-713-25"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Myleran 2mg tablet, film coated"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/ndc"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.quantity.code), force_bytes("TAB"))
        self.assertEqual(
            force_bytes(inst.quantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(inst.quantity.value, 90)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("RFP"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Refill - Part Fill")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(
            inst.whenHandedOver.date, FHIRDate("2015-01-15T16:20:00Z").date
        )
        self.assertEqual(inst.whenHandedOver.as_json(), "2015-01-15T16:20:00Z")
        self.assertEqual(inst.whenPrepared.date, FHIRDate("2015-01-15T10:20:00Z").date)
        self.assertEqual(inst.whenPrepared.as_json(), "2015-01-15T10:20:00Z")
