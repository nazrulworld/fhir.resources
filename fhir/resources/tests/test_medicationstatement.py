# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement
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

from .. import medicationstatement
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MedicationStatementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("MedicationStatement", js["resourceType"])
        return medicationstatement.MedicationStatement(js)

    def testMedicationStatement1(self):
        inst = self.instantiate_from("medicationstatementexample5.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationStatement instance"
        )
        self.implMedicationStatement1(inst)

        js = inst.as_json()
        self.assertEqual("MedicationStatement", js["resourceType"])
        inst2 = medicationstatement.MedicationStatement(js)
        self.implMedicationStatement1(inst2)

    def implMedicationStatement1(self, inst):
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2015-02-22").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2015-02-22")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2014-01-23").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2014-01-23")
        self.assertEqual(force_bytes(inst.id), force_bytes("example005"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("27658006"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Amoxicillin (product)"),
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
            force_bytes(inst.note[0].text),
            force_bytes(
                "Patient indicated that they thought it was Amoxicillin they were taking but it was really Erythromycin"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("entered-in-error"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationStatement2(self):
        inst = self.instantiate_from("medicationstatementexample4.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationStatement instance"
        )
        self.implMedicationStatement2(inst)

        js = inst.as_json()
        self.assertEqual("MedicationStatement", js["resourceType"])
        inst2 = medicationstatement.MedicationStatement(js)
        self.implMedicationStatement2(inst2)

    def implMedicationStatement2(self, inst):
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2015-02-22").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2015-02-22")
        self.assertFalse(inst.dosage[0].asNeededBoolean)
        self.assertEqual(
            force_bytes(inst.dosage[0].maxDosePerPeriod.denominator.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].maxDosePerPeriod.denominator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.dosage[0].maxDosePerPeriod.denominator.value, 1)
        self.assertEqual(
            force_bytes(inst.dosage[0].maxDosePerPeriod.numerator.code),
            force_bytes("385055001"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].maxDosePerPeriod.numerator.system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].maxDosePerPeriod.numerator.unit),
            force_bytes("capsules"),
        )
        self.assertEqual(inst.dosage[0].maxDosePerPeriod.numerator.value, 3)
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].code), force_bytes("260548002")
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].display), force_bytes("Oral")
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].text),
            force_bytes("one capsule three times daily"),
        )
        self.assertEqual(inst.dosage[0].timing.repeat.frequency, 3)
        self.assertEqual(inst.dosage[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosage[0].timing.repeat.periodUnit), force_bytes("d")
        )
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2014-01-23").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2014-01-23")
        self.assertEqual(force_bytes(inst.id), force_bytes("example004"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("27658006"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Amoxicillin (product)"),
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
            force_bytes(inst.note[0].text),
            force_bytes("Patient indicates they miss the occasional dose"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("65363002")
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].display),
            force_bytes("Otitis Media"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationStatement3(self):
        inst = self.instantiate_from("medicationstatementexample3.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationStatement instance"
        )
        self.implMedicationStatement3(inst)

        js = inst.as_json()
        self.assertEqual("MedicationStatement", js["resourceType"])
        inst2 = medicationstatement.MedicationStatement(js)
        self.implMedicationStatement3(inst2)

    def implMedicationStatement3(self, inst):
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2014-02-22").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2014-02-22")
        self.assertFalse(inst.dosage[0].asNeededBoolean)
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseQuantity.code),
            force_bytes("tab"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("tab"),
        )
        self.assertEqual(inst.dosage[0].doseAndRate[0].doseQuantity.value, 1)
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].display),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].maxDosePerPeriod.denominator.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].maxDosePerPeriod.denominator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.dosage[0].maxDosePerPeriod.denominator.value, 1)
        self.assertEqual(inst.dosage[0].maxDosePerPeriod.numerator.value, 1)
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].code), force_bytes("260548002")
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].display), force_bytes("Oral")
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosage[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosage[0].text), force_bytes("1 tablet per day")
        )
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2014-02-01").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2014-02-01")
        self.assertEqual(force_bytes(inst.id), force_bytes("example003"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.text),
            force_bytes("Little Pink Pill for water retention"),
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
            force_bytes(inst.note[0].text),
            force_bytes(
                "Patient cannot remember the name of the tablet, but takes it every day in the morning for water retention"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationStatement4(self):
        inst = self.instantiate_from("medicationstatementexample2.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationStatement instance"
        )
        self.implMedicationStatement4(inst)

        js = inst.as_json()
        self.assertEqual("MedicationStatement", js["resourceType"])
        inst2 = medicationstatement.MedicationStatement(js)
        self.implMedicationStatement4(inst2)

    def implMedicationStatement4(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0309"))
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2015-02-22").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2015-02-22")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2015-01-23").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2015-01-23")
        self.assertEqual(force_bytes(inst.id), force_bytes("example002"))
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
            force_bytes("Patient cannot take acetaminophen as per Dr instructions"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.statusReason[0].coding[0].code), force_bytes("166643006")
        )
        self.assertEqual(
            force_bytes(inst.statusReason[0].coding[0].display),
            force_bytes("Liver enzymes abnormal"),
        )
        self.assertEqual(
            force_bytes(inst.statusReason[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationStatement5(self):
        inst = self.instantiate_from("medicationstatementexample1.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationStatement instance"
        )
        self.implMedicationStatement5(inst)

        js = inst.as_json()
        self.assertEqual("MedicationStatement", js["resourceType"])
        inst2 = medicationstatement.MedicationStatement(js)
        self.implMedicationStatement5(inst2)

    def implMedicationStatement5(self, inst):
        self.assertEqual(
            force_bytes(inst.category.coding[0].code), force_bytes("inpatient")
        )
        self.assertEqual(
            force_bytes(inst.category.coding[0].display), force_bytes("Inpatient")
        )
        self.assertEqual(
            force_bytes(inst.category.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/medication-statement-category"
            ),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0309"))
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2015-02-22").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2015-02-22")
        self.assertEqual(
            force_bytes(inst.dosage[0].additionalInstruction[0].text),
            force_bytes("Taking at bedtime"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].asNeededCodeableConcept.coding[0].code),
            force_bytes("32914008"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].asNeededCodeableConcept.coding[0].display),
            force_bytes("Restless Legs"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].asNeededCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseRange.high.code),
            force_bytes("TAB"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseRange.high.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseRange.high.unit),
            force_bytes("TAB"),
        )
        self.assertEqual(inst.dosage[0].doseAndRate[0].doseRange.high.value, 2)
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseRange.low.code),
            force_bytes("TAB"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseRange.low.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseRange.low.unit),
            force_bytes("TAB"),
        )
        self.assertEqual(inst.dosage[0].doseAndRate[0].doseRange.low.value, 1)
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].display),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].code), force_bytes("26643006")
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].display),
            force_bytes("Oral Route"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosage[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosage[0].text),
            force_bytes(
                "1-2 tablets once daily at bedtime as needed for restless legs"
            ),
        )
        self.assertEqual(inst.dosage[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosage[0].timing.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.dosage[0].timing.repeat.periodUnit), force_bytes("d")
        )
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2015-01-23").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2015-01-23")
        self.assertEqual(force_bytes(inst.id), force_bytes("example001"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/portal/medstatements"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345689"))
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
            force_bytes("Patient indicates they miss the occasional dose"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("32914008")
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].display),
            force_bytes("Restless Legs"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationStatement6(self):
        inst = self.instantiate_from("medicationstatementexample7.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationStatement instance"
        )
        self.implMedicationStatement6(inst)

        js = inst.as_json()
        self.assertEqual("MedicationStatement", js["resourceType"])
        inst2 = medicationstatement.MedicationStatement(js)
        self.implMedicationStatement6(inst2)

    def implMedicationStatement6(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("med0315"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example007"))
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
                "patient plans to start using for seasonal allergies in the Spring when pollen is in the air"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedicationStatement7(self):
        inst = self.instantiate_from("medicationstatementexample6.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MedicationStatement instance"
        )
        self.implMedicationStatement7(inst)

        js = inst.as_json()
        self.assertEqual("MedicationStatement", js["resourceType"])
        inst2 = medicationstatement.MedicationStatement(js)
        self.implMedicationStatement7(inst2)

    def implMedicationStatement7(self, inst):
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2014-02-22").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2014-02-22")
        self.assertFalse(inst.dosage[0].asNeededBoolean)
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseQuantity.code),
            force_bytes("mL"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].doseQuantity.unit),
            force_bytes("mL"),
        )
        self.assertEqual(inst.dosage[0].doseAndRate[0].doseQuantity.value, 5)
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].code),
            force_bytes("ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].display),
            force_bytes("Ordered"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].maxDosePerPeriod.denominator.code),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].maxDosePerPeriod.denominator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.dosage[0].maxDosePerPeriod.denominator.value, 1)
        self.assertEqual(inst.dosage[0].maxDosePerPeriod.numerator.value, 3)
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].code), force_bytes("260548002")
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].display), force_bytes("Oral")
        )
        self.assertEqual(
            force_bytes(inst.dosage[0].route.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.dosage[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.dosage[0].text), force_bytes("5ml three times daily")
        )
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2014-02-01").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2014-02-01")
        self.assertEqual(force_bytes(inst.id), force_bytes("example006"))
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].code),
            force_bytes("27658006"),
        )
        self.assertEqual(
            force_bytes(inst.medicationCodeableConcept.coding[0].display),
            force_bytes("Amoxicillin (product)"),
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
            force_bytes(inst.note[0].text),
            force_bytes("Father indicates they miss the occasional dose"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
