# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Library
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

from .. import library
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class LibraryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Library", js["resourceType"])
        return library.Library(js)

    def testLibrary1(self):
        inst = self.instantiate_from("library-quick-model-definition.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary1(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary1(inst2)

    def implLibrary1(self, inst):
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("application/xml")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("http://cqlrepository.org/quick-modelinfo.xml"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-07-08").date)
        self.assertEqual(inst.date.as_json(), "2016-07-08")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Model definition for the QUICK Logical Model"),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("library-quick-model-definition")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("QUICK"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("QUICK Model Definition"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("QUICK"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("model-definition")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testLibrary2(self):
        inst = self.instantiate_from("library-fhir-model-definition.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary2(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary2(inst2)

    def implLibrary2(self, inst):
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("application/xml")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("http://cqlrepository.org/fhirmodel-modelinfo.xml"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-07-08").date)
        self.assertEqual(inst.date.as_json(), "2016-07-08")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Model definition for the FHIR Model"),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("library-fhir-model-definition")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("FHIR"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("FHIR Model Definition"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("FHIR"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("model-definition")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testLibrary3(self):
        inst = self.instantiate_from("library-predecessor-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary3(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary3(inst2)

    def implLibrary3(self, inst):
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("text/cql")
        )
        self.assertEqual(
            force_bytes(inst.content[0].title), force_bytes("FHIR Helpers")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("library-fhir-helpers-content.cql"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-11-14").date)
        self.assertEqual(inst.date.as_json(), "2016-11-14")
        self.assertEqual(force_bytes(inst.description), force_bytes("FHIR Helpers"))
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("library-fhir-helpers-predecessor")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("FHIRHelpers")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("successor")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("FHIR Helpers"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("FHIR Helpers"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.6"))

    def testLibrary4(self):
        inst = self.instantiate_from("library-cms146-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary4(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary4(inst2)

    def implLibrary4(self, inst):
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("text/cql")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("library-cms146-example-content.cql"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[0].path),
            force_bytes("category"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[0].valueCode[0]),
            force_bytes("diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[1].path),
            force_bytes("clinicalStatus"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[1].valueCode[0]),
            force_bytes("confirmed"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[2].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[2].valueSetString),
            force_bytes("2.16.840.1.113883.3.464.1003.102.12.1011"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].type), force_bytes("Condition")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[0].path),
            force_bytes("category"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[0].valueCode[0]),
            force_bytes("diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[1].path),
            force_bytes("clinicalStatus"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[1].valueCode[0]),
            force_bytes("confirmed"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[2].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[2].valueSetString),
            force_bytes("2.16.840.1.113883.3.464.1003.102.12.1012"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].type), force_bytes("Condition")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[0].path),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[0].valueCode[0]),
            force_bytes("finished"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[1].path),
            force_bytes("class"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[1].valueCode[0]),
            force_bytes("ambulatory"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[2].path), force_bytes("type")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[2].valueSetString),
            force_bytes("2.16.840.1.113883.3.464.1003.101.12.1061"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].type), force_bytes("Encounter")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[4].codeFilter[0].path),
            force_bytes("diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[4].codeFilter[0].valueSetString),
            force_bytes("2.16.840.1.113883.3.464.1003.198.12.1012"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[4].type), force_bytes("DiagnosticReport")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[5].codeFilter[0].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[5].codeFilter[0].valueSetString),
            force_bytes("2.16.840.1.113883.3.464.1003.196.12.1001"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[5].type), force_bytes("Medication")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].codeFilter[0].path),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].codeFilter[0].valueCode[0]),
            force_bytes("active"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].codeFilter[1].path),
            force_bytes("medication.code"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].codeFilter[1].valueSetString),
            force_bytes("2.16.840.1.113883.3.464.1003.196.12.1001"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].type), force_bytes("MedicationRequest")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[7].codeFilter[0].path),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[7].codeFilter[0].valueCode[0]),
            force_bytes("completed"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[7].codeFilter[1].path),
            force_bytes("medication.code"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[7].codeFilter[1].valueSetString),
            force_bytes("2.16.840.1.113883.3.464.1003.196.12.1001"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[7].type),
            force_bytes("MedicationStatement"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Logic for CMS 146: Appropriate Testing for Children with Pharyngitis"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("library-cms146-example"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("CMS146"))
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Appropriate Testing for Children with Pharyngitis"),
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("2.0.0"))

    def testLibrary5(self):
        inst = self.instantiate_from("library-exclusive-breastfeeding-cqm-logic.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary5(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary5(inst2)

    def implLibrary5(self, inst):
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("text/cql")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("http://cqlrepository.org/CMS9v4_CQM.cql"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].valueSetString),
            force_bytes("Single Live Birth"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("Condition")
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-03-08").date)
        self.assertEqual(inst.date.as_json(), "2016-03-08")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Quality measure logic for measuring outcomes for exclusive breastmilk feeding of newborns"
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id),
            force_bytes("library-exclusive-breastfeeding-cqm-logic"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("Exclusive_Breastfeeding_CQM_Logic"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Exclusive Breastfeeding CQM Logic")
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Exclusive Breastfeeding")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testLibrary6(self):
        inst = self.instantiate_from("library-mmi-suiciderisk-orderset-logic.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary6(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary6(inst2)

    def implLibrary6(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-03-12").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-03-12")
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("415-362-4007")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("info@motivemi.com"),
        )
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("text/cql")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("library-mmi-suiciderisk-orderset-logic-content.cql"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[0].system),
            force_bytes("phone"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[0].use),
            force_bytes("work"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[0].value),
            force_bytes("415-362-4007"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[1].system),
            force_bytes("email"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[1].use),
            force_bytes("work"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[1].value),
            force_bytes("info@motivemi.com"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].name),
            force_bytes("Motive Medical Intelligence"),
        )
        self.assertEqual(force_bytes(inst.contributor[0].type), force_bytes("author"))
        self.assertEqual(
            force_bytes(inst.copyright),
            force_bytes(
                "© Copyright 2016 Motive Medical Intelligence. All rights reserved."
            ),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].valueSetString),
            force_bytes("Suicide Risk Assessment"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("RiskAssessment")
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Logic for Suicide Risk Order Sets"),
        )
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2016-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("suiciderisk-orderset-logic")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://motivemi.com/artifacts"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("mmi:suiciderisk-orderset-logic"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
        )
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-08-15").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-08-15")
        self.assertEqual(
            force_bytes(inst.name), force_bytes("SuicideRiskOrderSetLogic")
        )
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 1)
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("Encounter"))
        self.assertEqual(force_bytes(inst.parameter[1].type), force_bytes("Encounter"))
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[2].max), force_bytes("1"))
        self.assertEqual(inst.parameter[2].min, 1)
        self.assertEqual(
            force_bytes(inst.parameter[2].name), force_bytes("Practitioner")
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].type), force_bytes("Practitioner")
        )
        self.assertEqual(force_bytes(inst.parameter[2].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Motive Medical Intelligence")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes(
                "Practice Guideline for the Treatment of Patients with Major Depressive Disorder"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("citation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("depends-on")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].type), force_bytes("depends-on")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[3].type), force_bytes("depends-on")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[4].type), force_bytes("depends-on")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Suicide Risk Order Set Logic")
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Suicide Risk Order Set Logic")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://motivemi.com/artifacts/Library/suiciderisk-orderset-logic"
            ),
        )
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("age"))
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("D000328"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("Adult"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("https://meshb.nlm.nih.gov"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code),
            force_bytes("87512008"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display),
            force_bytes("Mild major depression"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].code),
            force_bytes("40379007"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].display),
            force_bytes("Major depression, recurrent, mild"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].code),
            force_bytes("225444004"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].display),
            force_bytes("At risk for suicide (finding)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.useContext[4].code.code), force_bytes("user"))
        self.assertEqual(
            force_bytes(inst.useContext[4].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].code),
            force_bytes("309343006"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].display),
            force_bytes("Physician"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].code.code), force_bytes("venue")
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].code),
            force_bytes("440655000"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].display),
            force_bytes("Outpatient environment"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testLibrary7(self):
        inst = self.instantiate_from("library-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary7(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary7(inst2)

    def implLibrary7(self, inst):
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("text/cql")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url), force_bytes("library-example-content.cql")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].valueSetString),
            force_bytes("Other Female Reproductive Conditions"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("Condition")
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Common Logic for adherence to Chlamydia Screening guidelines"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("ChalmydiaScreening_Common"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Chlamydia Screening Common Library")
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Chlamydia Screening")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("2.0.0"))

    def testLibrary8(self):
        inst = self.instantiate_from("library-composition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary8(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary8(inst2)

    def implLibrary8(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2017-03-10").date)
        self.assertEqual(inst.date.as_json(), "2017-03-10")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Artifacts required for implementation of Zika Virus Management"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("composition-example"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("http://example.org")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("Zika Artifacts")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("composed-of")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("composed-of")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].type), force_bytes("composed-of")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[3].type), force_bytes("composed-of")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[4].type), force_bytes("composed-of")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[5].type), force_bytes("composed-of")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[6].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[6].url),
            force_bytes(
                "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm6539e1_w"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Zika Artifacts"))
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Zika Virus Management")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("asset-collection")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testLibrary9(self):
        inst = self.instantiate_from("library-exclusive-breastfeeding-cds-logic.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary9(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary9(inst2)

    def implLibrary9(self, inst):
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("text/cql")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("http://cqlrepository.org/CMS9v4_CDS.cql"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].valueSetString),
            force_bytes("Single Live Birth"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("Condition")
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-03-08").date)
        self.assertEqual(inst.date.as_json(), "2016-03-08")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Decision support logic for improving outcomes for exclusive breastmilk feeding of newborns"
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id),
            force_bytes("library-exclusive-breastfeeding-cds-logic"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("Exclusive_Breastfeeding_CDS_Logic"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("derived-from")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Exclusive Breastfeeding CDS Logic")
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Exclusive Breastfeeding")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testLibrary10(self):
        inst = self.instantiate_from("library-fhir-helpers.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary10(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary10(inst2)

    def implLibrary10(self, inst):
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("text/cql")
        )
        self.assertEqual(
            force_bytes(inst.content[0].title), force_bytes("FHIR Helpers")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("library-fhir-helpers-content.cql"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-11-14").date)
        self.assertEqual(inst.date.as_json(), "2016-11-14")
        self.assertEqual(force_bytes(inst.description), force_bytes("FHIR Helpers"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("library-fhir-helpers"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("FHIRHelpers")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("predecessor")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("FHIR Helpers"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("FHIR Helpers"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.8"))
