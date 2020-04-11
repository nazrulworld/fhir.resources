# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Observation
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

from .. import observation
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ObservationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Observation", js["resourceType"])
        return observation.Observation(js)

    def testObservation1(self):
        inst = self.instantiate_from("observation-example-genetics-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation1(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation1(inst2)

    def implObservation1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("55233-1"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes(
                "Genetic analysis master panel-- This is the parent OBR for the panel holding all of the associated observations that can be reported with a molecular genetics analysis result."
            ),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/observation-geneticsDNASequenceVariantName"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueCodeableConcept.text),
            force_bytes("NG_007726.3:g.146252T>G"),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/observation-geneticsGene"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].valueCodeableConcept.coding[0].code),
            force_bytes("3236"),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].valueCodeableConcept.coding[0].display),
            force_bytes("EGFR"),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].valueCodeableConcept.coding[0].system),
            force_bytes("http://www.genenames.org"),
        )
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/observation-geneticsDNARegionName"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[2].valueString), force_bytes("Exon 21")
        )
        self.assertEqual(
            force_bytes(inst.extension[3].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/observation-geneticsGenomicSourceClass"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[3].valueCodeableConcept.coding[0].code),
            force_bytes("LA6684-0"),
        )
        self.assertEqual(
            force_bytes(inst.extension[3].valueCodeableConcept.coding[0].display),
            force_bytes("somatic"),
        )
        self.assertEqual(
            force_bytes(inst.extension[3].valueCodeableConcept.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-genetics-1"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.valueCodeableConcept.coding[0].code),
            force_bytes("10828004"),
        )
        self.assertEqual(
            force_bytes(inst.valueCodeableConcept.coding[0].display),
            force_bytes("Positive"),
        )
        self.assertEqual(
            force_bytes(inst.valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )

    def testObservation2(self):
        inst = self.instantiate_from("observation-example-bmd.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation2(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation2(inst2)

    def implObservation2(self, inst):
        self.assertEqual(
            force_bytes(inst.bodySite.coding[0].code),
            force_bytes("71341001:272741003=7771000"),
        )
        self.assertEqual(
            force_bytes(inst.bodySite.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.bodySite.text), force_bytes("Left Femur"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("24701-5"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Femur DXA Bone density"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("BMD - Left Femur"))
        self.assertEqual(force_bytes(inst.id), force_bytes("bmd"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("g/cm-2"))
        self.assertEqual(
            force_bytes(inst.valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("g/cm²"))
        self.assertEqual(inst.valueQuantity.value, 0.887)

    def testObservation3(self):
        inst = self.instantiate_from("observation-example-respiratory-rate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation3(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation3(inst2)

    def implObservation3(self, inst):
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/observation-category"),
        )
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("9279-1"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Respiratory rate")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Respiratory rate"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("respiratory-rate"))
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/vitalsigns"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("/min"))
        self.assertEqual(
            force_bytes(inst.valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.valueQuantity.unit), force_bytes("breaths/minute")
        )
        self.assertEqual(inst.valueQuantity.value, 26)

    def testObservation4(self):
        inst = self.instantiate_from("observation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation4(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation4(inst2)

    def implObservation4(self, inst):
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/observation-category"),
        )
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("29463-7"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Body Weight")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.coding[1].code), force_bytes("3141-9"))
        self.assertEqual(
            force_bytes(inst.code.coding[1].display),
            force_bytes("Body weight Measured"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[1].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.coding[2].code), force_bytes("27113001"))
        self.assertEqual(
            force_bytes(inst.code.coding[2].display), force_bytes("Body weight")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[2].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[3].code), force_bytes("body-weight")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[3].display), force_bytes("Body Weight")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[3].system),
            force_bytes("http://acme.org/devices/clinical-codes"),
        )
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2016-03-28").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-03-28")
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("[lb_av]"))
        self.assertEqual(
            force_bytes(inst.valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("lbs"))
        self.assertEqual(inst.valueQuantity.value, 185)

    def testObservation5(self):
        inst = self.instantiate_from("observation-example-haplotype2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation5(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation5(inst2)

    def implObservation5(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("55233-1"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes(
                "Genetic analysis master panel-- This is the parent OBR for the panel holding all of the associated observations that can be reported with a molecular genetics analysis result."
            ),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/observation-geneticsGene"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueCodeableConcept.coding[0].code),
            force_bytes("2623"),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueCodeableConcept.coding[0].display),
            force_bytes("CYP2C9"),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://www.genenames.org"),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/observation-geneticsSequence"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/observation-geneticsSequence"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-haplotype2"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(force_bytes(inst.related[0].type), force_bytes("derived-from"))
        self.assertEqual(force_bytes(inst.related[1].type), force_bytes("derived-from"))
        self.assertEqual(force_bytes(inst.status), force_bytes("unknown"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.valueCodeableConcept.coding[0].code),
            force_bytes("PA16581679"),
        )
        self.assertEqual(
            force_bytes(inst.valueCodeableConcept.coding[0].display), force_bytes("*4")
        )
        self.assertEqual(
            force_bytes(inst.valueCodeableConcept.coding[0].system),
            force_bytes("http://pharmakb.org"),
        )

    def testObservation6(self):
        inst = self.instantiate_from("observation-example-mbp.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation6(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation6(inst2)

    def implObservation6(self, inst):
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/observation-category"),
        )
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8478-0"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Mean blood pressure")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(
            force_bytes(inst.code.text), force_bytes("Mean blood pressure")
        )
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("mbp"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("mm[Hg]"))
        self.assertEqual(
            force_bytes(inst.valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("mm[Hg]"))
        self.assertEqual(inst.valueQuantity.value, 80)

    def testObservation7(self):
        inst = self.instantiate_from("observation-example-bmi.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation7(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation7(inst2)

    def implObservation7(self, inst):
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/observation-category"),
        )
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("39156-5"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Body mass index (BMI) [Ratio]"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("BMI"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("bmi"))
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/vitalsigns"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("kg/m2"))
        self.assertEqual(
            force_bytes(inst.valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("kg/m2"))
        self.assertEqual(inst.valueQuantity.value, 16.2)

    def testObservation8(self):
        inst = self.instantiate_from("observation-example-body-height.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation8(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation8(inst2)

    def implObservation8(self, inst):
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/observation-category"),
        )
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8302-2"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Body height")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Body height"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("body-height"))
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/vitalsigns"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("[in_i]"))
        self.assertEqual(
            force_bytes(inst.valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("in"))
        self.assertEqual(inst.valueQuantity.value, 66.89999999999999)

    def testObservation9(self):
        inst = self.instantiate_from("observation-example-eye-color.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation9(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation9(inst2)

    def implObservation9(self, inst):
        self.assertEqual(force_bytes(inst.code.text), force_bytes("eye color"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2016-05-18").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-05-18")
        self.assertEqual(force_bytes(inst.id), force_bytes("eye-color"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueString), force_bytes("blue"))

    def testObservation10(self):
        inst = self.instantiate_from("observation-example-body-temperature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation10(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation10(inst2)

    def implObservation10(self, inst):
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/observation-category"),
        )
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8310-5"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display), force_bytes("Body temperature")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Body temperature"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("body-temperature"))
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/vitalsigns"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("Cel"))
        self.assertEqual(
            force_bytes(inst.valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("C"))
        self.assertEqual(inst.valueQuantity.value, 36.5)
