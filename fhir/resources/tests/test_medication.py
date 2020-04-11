# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
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

from .. import medication
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MedicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Medication", js["resourceType"])
        return medication.Medication(js)

    def testMedication1(self):
        inst = self.instantiate_from("medicationexample0307.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication1(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication1(inst2)

    def implMedication1(self, inst):
        self.assertEqual(inst.batch.expirationDate.date, FHIRDate("2019-10-31").date)
        self.assertEqual(inst.batch.expirationDate.as_json(), "2019-10-31")
        self.assertEqual(force_bytes(inst.batch.lotNumber), force_bytes("12345"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("0169-7501-11")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Novolog 100u/ml")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/ndc"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("org3"))
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("385219001")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].display),
            force_bytes("Injection solution (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("med0307"))
        self.assertEqual(
            force_bytes(inst.ingredient[0].itemCodeableConcept.coding[0].code),
            force_bytes("325072002"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].itemCodeableConcept.coding[0].display),
            force_bytes("Insulin Aspart (substance)"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].itemCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.code), force_bytes("mL")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.denominator.value, 1)
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.code), force_bytes("U")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.numerator.value, 100)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedication2(self):
        inst = self.instantiate_from("medicationexample0311.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication2(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication2(inst2)

    def implMedication2(self, inst):
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("373994007")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Prednisone 5mg tablet (Product)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("sub03"))
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("385055001")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].display),
            force_bytes("Tablet dose form (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("med0311"))
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.code),
            force_bytes("TAB"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(inst.ingredient[0].strength.denominator.value, 1)
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.code), force_bytes("mg")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.numerator.value, 5)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedication3(self):
        inst = self.instantiate_from("medicationexample0310.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication3(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication3(inst2)

    def implMedication3(self, inst):
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("430127000")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Oral Form Oxycodone (product)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("sub03"))
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("385055001")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].display),
            force_bytes("Tablet dose form (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("med0310"))
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.code),
            force_bytes("TAB"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(inst.ingredient[0].strength.denominator.value, 1)
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.code), force_bytes("mg")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.numerator.value, 5)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedication4(self):
        inst = self.instantiate_from("medicationexample0306.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication4(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication4(inst2)

    def implMedication4(self, inst):
        self.assertEqual(inst.batch.expirationDate.date, FHIRDate("2019-10-31").date)
        self.assertEqual(inst.batch.expirationDate.as_json(), "2019-10-31")
        self.assertEqual(force_bytes(inst.batch.lotNumber), force_bytes("12345"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("51144-050-01")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Adcetris")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/ndc"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("org3"))
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("421637006")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].display),
            force_bytes(
                "Lyophilized powder for injectable solution (qualifier value) "
            ),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("med0306"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedication5(self):
        inst = self.instantiate_from("medicationexample0301.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication5(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication5(inst2)

    def implMedication5(self, inst):
        self.assertEqual(inst.batch.expirationDate.date, FHIRDate("2017-05-22").date)
        self.assertEqual(inst.batch.expirationDate.as_json(), "2017-05-22")
        self.assertEqual(force_bytes(inst.batch.lotNumber), force_bytes("9494788"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("0069-2587-10")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/ndc"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("org4"))
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("385219001")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].display),
            force_bytes("Injection Solution (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("med0301"))
        self.assertTrue(inst.ingredient[0].isActive)
        self.assertEqual(
            force_bytes(inst.ingredient[0].itemCodeableConcept.coding[0].code),
            force_bytes("66955"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].itemCodeableConcept.coding[0].display),
            force_bytes("Vancomycin Hydrochloride"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].itemCodeableConcept.coding[0].system),
            force_bytes("http://www.nlm.nih.gov/research/umls/rxnorm"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.code), force_bytes("mL")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.denominator.value, 10)
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.code), force_bytes("mg")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.numerator.value, 500)
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

    def testMedication6(self):
        inst = self.instantiate_from("medicationexample0317.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication6(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication6(inst2)

    def implMedication6(self, inst):
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("385219001")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].display),
            force_bytes("Injection Solution (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.form.text),
            force_bytes("Injection Solution (qualifier value)"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("med0317"))
        self.assertEqual(
            force_bytes(inst.ingredient[0].itemCodeableConcept.coding[0].code),
            force_bytes("204520"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].itemCodeableConcept.coding[0].display),
            force_bytes("Potassium Chloride"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].itemCodeableConcept.coding[0].system),
            force_bytes("http://www.nlm.nih.gov/research/umls/rxnorm"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.code), force_bytes("mL")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.denominator.value, 1)
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.code), force_bytes("meq")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.numerator.value, 2)
        self.assertEqual(
            force_bytes(inst.ingredient[1].itemCodeableConcept.coding[0].code),
            force_bytes("313002"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[1].itemCodeableConcept.coding[0].display),
            force_bytes("Sodium Chloride 0.9% injectable solution"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[1].itemCodeableConcept.coding[0].system),
            force_bytes("http://www.nlm.nih.gov/research/umls/rxnorm"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[1].strength.denominator.code), force_bytes("mL")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[1].strength.denominator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[1].strength.denominator.value, 100)
        self.assertEqual(
            force_bytes(inst.ingredient[1].strength.numerator.code), force_bytes("g")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[1].strength.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[1].strength.numerator.value, 0.9)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedication7(self):
        inst = self.instantiate_from("medicationexample1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication7(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication7(inst2)

    def implMedication7(self, inst):
        self.assertEqual(
            force_bytes(inst.code.text), force_bytes("Amoxicillin 250mg/5ml Suspension")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medicationexample1"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Amoxicillin 250mg/5ml Suspension</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedication8(self):
        inst = self.instantiate_from("medicationexample15.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication8(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication8(inst2)

    def implMedication8(self, inst):
        self.assertEqual(inst.batch.expirationDate.date, FHIRDate("2017-05-22").date)
        self.assertEqual(inst.batch.expirationDate.as_json(), "2017-05-22")
        self.assertEqual(force_bytes(inst.batch.lotNumber), force_bytes("9494788"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("213293"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Capecitabine 500mg oral tablet (Xeloda)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://www.nlm.nih.gov/research/umls/rxnorm"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("org2"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("sub04"))
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("385055001")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].display),
            force_bytes("Tablet dose form (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("medexample015"))
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.code),
            force_bytes("TAB"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(inst.ingredient[0].strength.denominator.value, 1)
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.code), force_bytes("mg")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.numerator.value, 500)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedication9(self):
        inst = self.instantiate_from("medicationexample0321.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication9(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication9(inst2)

    def implMedication9(self, inst):
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("108761006")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Capecitabine (product)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("sub03"))
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("385055001")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].display),
            force_bytes("Tablet dose form (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("med0321"))
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.code),
            force_bytes("385055001"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.unit),
            force_bytes("Tablet"),
        )
        self.assertEqual(inst.ingredient[0].strength.denominator.value, 1)
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.code), force_bytes("mg")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.numerator.value, 500)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testMedication10(self):
        inst = self.instantiate_from("medicationexample0320.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication10(inst)

        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication10(inst2)

    def implMedication10(self, inst):
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("324252006")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Azithromycin 250mg capsule (product)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("sub03"))
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("385055001")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].display),
            force_bytes("Tablet dose form (qualifier value)"),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("med0320"))
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.code),
            force_bytes("TAB"),
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.denominator.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm"),
        )
        self.assertEqual(inst.ingredient[0].strength.denominator.value, 1)
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.code), force_bytes("mg")
        )
        self.assertEqual(
            force_bytes(inst.ingredient[0].strength.numerator.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(inst.ingredient[0].strength.numerator.value, 250)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
