# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest
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

from .. import medicationrequest
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MedicationRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("MedicationRequest", js["resourceType"])
        return medicationrequest.MedicationRequest(js)

    def testMedicationRequest1(self):
        inst = self.instantiate_from("medicationrequest0326.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest1(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest1(inst2)

    def implMedicationRequest1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.unit),
            force_bytes("days"),
        )
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.value, 30)
        self.assertEqual(inst.dispenseRequest.numberOfRepeatsAllowed, 3)
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.code), force_bytes("mL")
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.unit), force_bytes("mL")
        )
        self.assertEqual(inst.dispenseRequest.quantity.value, 30)
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.date, FHIRDate("2016-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.as_json(), "2016-01-15"
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2015-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.as_json(), "2015-01-15"
        )
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
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0326"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("746763"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Proventil HFA 90mcg/actuat metered dose inhaler, 200 actuat"),
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
        self.assertEqual(force_bytes(inst.status), force_bytes("on-hold"))
        self.assertTrue(inst.substitution.allowedBoolean)
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].code), force_bytes("FP")
        )
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].display),
            force_bytes("formulary policy"),
        )
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationRequest2(self):
        inst = self.instantiate_from("medicationrequest0330.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest2(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest2(inst2)

    def implMedicationRequest2(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0305"))
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.unit),
            force_bytes("days"),
        )
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.value, 30)
        self.assertEqual(inst.dispenseRequest.numberOfRepeatsAllowed, 1)
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.code), force_bytes("mL")
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.unit), force_bytes("mL")
        )
        self.assertEqual(inst.dispenseRequest.quantity.value, 10)
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.date, FHIRDate("2016-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.as_json(), "2016-01-15"
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2015-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.as_json(), "2015-01-15"
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("OPDROP"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("OPDROP"),
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
            force_bytes(inst.dosageInstruction[0].method.coding[0].code),
            force_bytes("421538008"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].method.coding[0].display),
            force_bytes("Instill - dosing instruction imperative (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].method.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].code),
            force_bytes("54485002"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].display),
            force_bytes("Ophthalmic route (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes("Instil one drop in each eye twice daily"),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 2)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0330"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertFalse(inst.substitution.allowedBoolean)
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].code), force_bytes("FP")
        )
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].display),
            force_bytes("formulary policy"),
        )
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationRequest3(self):
        inst = self.instantiate_from("medicationrequest0310.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest3(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest3(inst2)

    def implMedicationRequest3(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0309"))
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].additionalInstruction[0].text),
            force_bytes("Take at bedtime"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].code
            ),
            force_bytes("32914008"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].display
            ),
            force_bytes("Restless Legs"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].asNeededCodeableConcept.coding[0].system
            ),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseRange.high.code),
            force_bytes("TAB"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseRange.high.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseRange.high.unit),
            force_bytes("TAB"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].doseRange.high.value, 2
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseRange.low.code),
            force_bytes("TAB"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseRange.low.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseRange.low.unit),
            force_bytes("TAB"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].doseRange.low.value, 1
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
            force_bytes(
                "Take 1-2 tablets once daily at bedtime as needed for restless legs"
            ),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0310"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationRequest4(self):
        inst = self.instantiate_from("medicationrequest0306.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest4(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest4(inst2)

    def implMedicationRequest4(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0304"))
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
            force_bytes("Oral route (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes(
                "6 mg PO daily for remission induction; adjust dosage to white blood cell (WBC) count.  With hold treatment if WBC is less than 15,000/µL; resume when WBC is greater than 50,000/µL"
            ),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0306"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("92818009")
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].display),
            force_bytes("Chronic myeloid Leukemia (disorder)"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationRequest5(self):
        inst = self.instantiate_from("medicationrequest0307.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest5(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest5(inst2)

    def implMedicationRequest5(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0308"))
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.unit),
            force_bytes("days"),
        )
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.value, 10)
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.code), force_bytes("TAB")
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.unit), force_bytes("TAB")
        )
        self.assertEqual(inst.dispenseRequest.quantity.value, 30)
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.date, FHIRDate("2016-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.as_json(), "2016-01-15"
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2015-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.as_json(), "2015-01-15"
        )
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
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0307"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertTrue(inst.substitution.allowedBoolean)
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].code), force_bytes("FP")
        )
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].display),
            force_bytes("formulary policy"),
        )
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationRequest6(self):
        inst = self.instantiate_from("medicationrequest0331.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest6(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest6(inst2)

    def implMedicationRequest6(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0350"))
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.unit),
            force_bytes("days"),
        )
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.value, 30)
        self.assertEqual(inst.dispenseRequest.numberOfRepeatsAllowed, 3)
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.code), force_bytes("TAB")
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.unit), force_bytes("TAB")
        )
        self.assertEqual(inst.dispenseRequest.quantity.value, 30)
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.date, FHIRDate("2016-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.as_json(), "2016-01-15"
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2015-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.as_json(), "2015-01-15"
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
        self.assertEqual(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.value, 7)
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
            force_bytes(inst.dosageInstruction[0].text), force_bytes("7mg once daily")
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0331"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertTrue(inst.substitution.allowedBoolean)
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].code), force_bytes("FP")
        )
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].display),
            force_bytes("formulary policy"),
        )
        self.assertEqual(
            force_bytes(inst.substitution.reason.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationRequest7(self):
        inst = self.instantiate_from("medicationrequest0327.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest7(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest7(inst2)

    def implMedicationRequest7(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.unit),
            force_bytes("days"),
        )
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.value, 14)
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.code), force_bytes("patch")
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.unit), force_bytes("patch")
        )
        self.assertEqual(inst.dispenseRequest.quantity.value, 6)
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.date, FHIRDate("2016-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.as_json(), "2016-01-15"
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2015-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.as_json(), "2015-01-15"
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.code),
            force_bytes("patch"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("patch"),
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
            force_bytes("apply one patch three times per week"),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 3)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("wk"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0327"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("333919005"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Fentanyl 25micrograms/hour patch (product)"),
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
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationRequest8(self):
        inst = self.instantiate_from("medicationrequest0316.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest8(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest8(inst2)

    def implMedicationRequest8(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0306"))
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
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.code
            ),
            force_bytes("min"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.system
            ),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].rateRatio.denominator.value, 20
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.code
            ),
            force_bytes("mg/kg"),
        )
        self.assertEqual(
            force_bytes(
                inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.system
            ),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            inst.dosageInstruction[0].doseAndRate[0].rateRatio.numerator.value, 1.8
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
            force_bytes(inst.dosageInstruction[0].maxDosePerLifetime.code),
            force_bytes("mg"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].maxDosePerLifetime.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].maxDosePerLifetime.unit),
            force_bytes("mg"),
        )
        self.assertEqual(inst.dosageInstruction[0].maxDosePerLifetime.value, 400)
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
                "1.8 mg/kg IV infusion over 20 minutes every 3 weeks for 16 cycles"
            ),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.count, 16)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 3)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.periodUnit),
            force_bytes("wk"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0316"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(
            force_bytes(inst.instantiatesUri[0]),
            force_bytes(
                "http://www.bccancer.bc.ca/chemotherapy-protocols-site/Documents/Lymphoma-Myeloma/ULYBRENTUX%20Protocol_1Jun2017.pdf"
            ),
        )
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
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

    def testMedicationRequest9(self):
        inst = self.instantiate_from("medicationrequest0320.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest9(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest9(inst2)

    def implMedicationRequest9(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.expectedSupplyDuration.unit),
            force_bytes("days"),
        )
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.value, 30)
        self.assertEqual(inst.dispenseRequest.numberOfRepeatsAllowed, 6)
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.code), force_bytes("mL")
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dispenseRequest.quantity.unit), force_bytes("mL")
        )
        self.assertEqual(inst.dispenseRequest.quantity.value, 10)
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.date, FHIRDate("2016-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.end.as_json(), "2016-01-15"
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2015-01-15").date
        )
        self.assertEqual(
            inst.dispenseRequest.validityPeriod.start.as_json(), "2015-01-15"
        )
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
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0320"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
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
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("473189005")
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].display),
            force_bytes("On subcutaneous insulin for diabetes mellitus (finding)"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationRequest10(self):
        inst = self.instantiate_from("medicationrequest0336.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationRequest instance"
        )
        self.implMedicationRequest10(inst)

        js = inst.as_json()
        self.assertEqual("MedicationRequest", js["resourceType"])
        inst2 = medicationrequest.MedicationRequest(js)
        self.implMedicationRequest10(inst2)

    def implMedicationRequest10(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-01-15")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0336"))
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].rateQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].doseAndRate[0].rateQuantity.unit),
            force_bytes("ug/kg/min"),
        )
        self.assertEqual(inst.dosageInstruction[0].doseAndRate[0].rateQuantity.value, 4)
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
            force_bytes("47625008"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].display),
            force_bytes("Intravenous route (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosageInstruction[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].text),
            force_bytes("Dopamine 4mcg/kg/min"),
        )
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.duration, 33.33)
        self.assertEqual(
            force_bytes(inst.dosageInstruction[0].timing.repeat.durationUnit),
            force_bytes("h"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medrx0336"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/prescriptions"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
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
