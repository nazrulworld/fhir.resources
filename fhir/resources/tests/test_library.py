# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Library
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
        inst = self.instantiate_from("library-omtk-modelinfo.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary1(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary1(inst2)

    def implLibrary1(self, inst):
        self.assertEqual(
            force_bytes(inst.author[0].name),
            force_bytes("Kensaku Kawamoto, MD, PhD, MHS"),
        )
        self.assertEqual(force_bytes(inst.author[1].name), force_bytes("Bryn Rhodes"))
        self.assertEqual(
            force_bytes(inst.author[2].name), force_bytes("Floyd Eisenberg, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.author[3].name), force_bytes("Robert McClure, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("application/xml")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("elm/OMTK-modelinfo-0.1.0.xml"),
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© CDC 2016+."))
        self.assertEqual(inst.date.date, FHIRDate("2017-05-05").date)
        self.assertEqual(inst.date.as_json(), "2017-05-05")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Opioid Management Terminology Knowledge Base Model Definition for use in implementing CDC Opioid Prescribing Guidelines."
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("omtk-modelinfo"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("OMTKModelInfo")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
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
            force_bytes(inst.publisher),
            force_bytes("Centers for Disease Control and Prevention (CDC)"),
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "This library defines the Opioid Management Terminology Knowledge Base model"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("OMTK Model Info"))
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Opioid Prescribing")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("model-definition")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/library-type"),
        )
        self.assertEqual(
            force_bytes(inst.usage),
            force_bytes(
                "This library is used to resolve data elements in the Opioid Management Terminology Knowledge Base model"
            ),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("182888003"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("Medication requested (situation)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code),
            force_bytes("82423001"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display),
            force_bytes("Chronic pain (finding)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("0.1.0"))

    def testLibrary2(self):
        inst = self.instantiate_from("library-hiv-indicators.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary2(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary2(inst2)

    def implLibrary2(self, inst):
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("text/cql")
        )
        self.assertEqual(
            force_bytes(inst.content[0].url),
            force_bytes("library-hiv-indicators-content.cql"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2018-08-03").date)
        self.assertEqual(inst.date.as_json(), "2018-08-03")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("HIV Indicators Reporting Example"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("hiv-indicators"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://ohie.org/Library/"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("hiv-indicators")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes("http://wiki.ihe.net/index.php/Aggregate_Data_Exchange_-_HIV"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("HIV Indicators"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Logic Library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/library-type"),
        )
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://ohie.org/Library/hiv-indicators")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("0.0.0"))

    def testLibrary3(self):
        inst = self.instantiate_from("library-quick-model-definition.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary3(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary3(inst2)

    def implLibrary3(self, inst):
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
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("QUICK Model Definition"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("QUICK"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("model-definition")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testLibrary4(self):
        inst = self.instantiate_from("library-opioidcds-recommendation-11.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary4(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary4(inst2)

    def implLibrary4(self, inst):
        self.assertEqual(
            force_bytes(inst.author[0].name),
            force_bytes("Kensaku Kawamoto, MD, PhD, MHS"),
        )
        self.assertEqual(force_bytes(inst.author[1].name), force_bytes("Bryn Rhodes"))
        self.assertEqual(
            force_bytes(inst.author[2].name), force_bytes("Floyd Eisenberg, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.author[3].name), force_bytes("Robert McClure, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("application/elm+xml")
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© CDC 2016+."))
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].path),
            force_bytes("medicationCodeableConcept"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].valueSet),
            force_bytes("http://example.org/fhir/ValueSet/benzodiazepines"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("MedicationRequest")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[0].path),
            force_bytes("medicationCodeableConcept"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[0].valueSet),
            force_bytes(
                "http://example.org/fhir/ValueSet/opioids-abused-in-ambulatory-care"
            ),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].type), force_bytes("MedicationRequest")
        )
        self.assertEqual(inst.date.date, FHIRDate("2018-03-25T13:49:09-06:00").date)
        self.assertEqual(inst.date.as_json(), "2018-03-25T13:49:09-06:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Opioid decision support logic to avoid prescribing opioid pain medication and benzodiazepines concurrently whenever possible."
            ),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("opioidcds-recommendation-11")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("OpioidCDS_REC_11")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
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
            force_bytes(inst.publisher),
            force_bytes("Centers for Disease Control and Prevention (CDC)"),
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "The purpose of this library is to determine whether opioid pain medication and benzodiazepines have been prescribed concurrently."
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes("CDC guideline for prescribing opioids for chronic pain"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("documentation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "https://guidelines.gov/summaries/summary/50153/cdc-guideline-for-prescribing-opioids-for-chronic-pain---united-states-2016#420"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].resource),
            force_bytes("Library/opioidcds-common"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("depends-on")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Opioid CDS Logic for recommendation #11"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Opioid Prescribing")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Logic Library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/library-type"),
        )
        self.assertEqual(
            force_bytes(inst.usage),
            force_bytes(
                "This library is used to notify the prescriber/user to avoid prescribing opioid pain medication and benzodiazepines concurrently."
            ),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("182888003"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("Medication requested (situation)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code),
            force_bytes("82423001"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display),
            force_bytes("Chronic pain (finding)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("0.1.0"))

    def testLibrary5(self):
        inst = self.instantiate_from("library-opioidcds-recommendation-07.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary5(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary5(inst2)

    def implLibrary5(self, inst):
        self.assertEqual(
            force_bytes(inst.author[0].name),
            force_bytes("Kensaku Kawamoto, MD, PhD, MHS"),
        )
        self.assertEqual(force_bytes(inst.author[1].name), force_bytes("Bryn Rhodes"))
        self.assertEqual(
            force_bytes(inst.author[2].name), force_bytes("Floyd Eisenberg, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.author[3].name), force_bytes("Robert McClure, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("application/elm+xml")
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© CDC 2016+."))
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].path),
            force_bytes("medicationCodeableConcept"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].valueSet),
            force_bytes(
                "http://example.org/fhir/ValueSet/opioids-indicating-end-of-life"
            ),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("MedicationRequest")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[0].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].type), force_bytes("Procedure")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[0].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].type), force_bytes("Procedure")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[0].path),
            force_bytes("medicationCodeableConcept"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[0].valueSet),
            force_bytes(
                "http://example.org/fhir/ValueSet/opioids-abused-in-ambulatory-care"
            ),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].type), force_bytes("MedicationRequest")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[4].type), force_bytes("Encounter")
        )
        self.assertEqual(inst.date.date, FHIRDate("2018-03-25T13:49:09-06:00").date)
        self.assertEqual(inst.date.as_json(), "2018-03-25T13:49:09-06:00")
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("opioidcds-recommendation-07")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("OpioidCDS_REC_07")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
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
            force_bytes(inst.publisher),
            force_bytes("Centers for Disease Control and Prevention (CDC)"),
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "The purpose of this library is to determine whether the patient has been evaluated for benefits and harms within 1 to 4 weeks of starting opioid therapy and every 3 months or more subsequently."
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes("CDC guideline for prescribing opioids for chronic pain"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("documentation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "https://guidelines.gov/summaries/summary/50153/cdc-guideline-for-prescribing-opioids-for-chronic-pain---united-states-2016#420"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].resource),
            force_bytes("Library/opioidcds-common"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("depends-on")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Opioid CDS Logic for recommendation #7"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Opioid Prescribing")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Logic Library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/library-type"),
        )
        self.assertEqual(
            force_bytes(inst.usage),
            force_bytes(
                "This library is used to notify the prescriber/user whether an evaluation for benefits and harms associated with opioid therapy is recommended for the patient."
            ),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("182888003"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("Medication requested (situation)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code),
            force_bytes("82423001"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display),
            force_bytes("Chronic pain (finding)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("0.1.0"))

    def testLibrary6(self):
        inst = self.instantiate_from("library-fhir-model-definition.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary6(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary6(inst2)

    def implLibrary6(self, inst):
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
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("FHIR Model Definition"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("FHIR"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("model-definition")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testLibrary7(self):
        inst = self.instantiate_from("library-predecessor-example.json")
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
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].resource),
            force_bytes("Library/fhir-model-definition"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].resource),
            force_bytes("Library/library-fhir-helpers"),
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

    def testLibrary8(self):
        inst = self.instantiate_from("library-opioidcds-recommendation-10.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary8(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary8(inst2)

    def implLibrary8(self, inst):
        self.assertEqual(
            force_bytes(inst.author[0].name),
            force_bytes("Kensaku Kawamoto, MD, PhD, MHS"),
        )
        self.assertEqual(force_bytes(inst.author[1].name), force_bytes("Bryn Rhodes"))
        self.assertEqual(
            force_bytes(inst.author[2].name), force_bytes("Floyd Eisenberg, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.author[3].name), force_bytes("Robert McClure, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("application/elm+xml")
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© CDC 2016+."))
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].path),
            force_bytes("medicationCodeableConcept"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].valueSet),
            force_bytes(
                "http://example.org/fhir/ValueSet/opioids-indicating-end-of-life"
            ),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("MedicationRequest")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[0].path),
            force_bytes("medicationCodeableConcept"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[0].valueSet),
            force_bytes(
                "http://example.org/fhir/ValueSet/opioids-abused-in-ambulatory-care"
            ),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].type), force_bytes("MedicationRequest")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[0].path),
            force_bytes("combo-code"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[0].valueSet),
            force_bytes(
                "http://example.org/fhir/ValueSet/illicit-drug-urine-screening"
            ),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].type), force_bytes("Observation")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[0].path),
            force_bytes("combo-code"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[0].valueSet),
            force_bytes("http://example.org/fhir/ValueSet/opioid-urine-screening"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].type), force_bytes("Observation")
        )
        self.assertEqual(inst.date.date, FHIRDate("2018-03-25T13:49:09-06:00").date)
        self.assertEqual(inst.date.as_json(), "2018-03-25T13:49:09-06:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Opioid decision support logic to evaluate whether the patient has had a urine screening in the past 12 months and provide analysis."
            ),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("opioidcds-recommendation-10")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("OpioidCDS_REC_10")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
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
            force_bytes(inst.publisher),
            force_bytes("Centers for Disease Control and Prevention (CDC)"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes("CDC guideline for prescribing opioids for chronic pain"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("documentation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "https://guidelines.gov/summaries/summary/50153/cdc-guideline-for-prescribing-opioids-for-chronic-pain---united-states-2016#420"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].resource),
            force_bytes("Library/opioidcds-common"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("depends-on")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Opioid CDS Logic for recommendation #10"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Opioid Prescribing")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Logic Library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/library-type"),
        )
        self.assertEqual(
            force_bytes(inst.usage),
            force_bytes(
                "This library is used to notify the prescriber/user whether the patient has had a urine screening in the past 12 months and to provide analysis if true."
            ),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("182888003"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("Medication requested (situation)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code),
            force_bytes("82423001"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display),
            force_bytes("Chronic pain (finding)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("0.1.0"))

    def testLibrary9(self):
        inst = self.instantiate_from("library-cms146-example.json")
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
            force_bytes("library-cms146-example-content.cql"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[0].code[0].code),
            force_bytes("diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[0].path),
            force_bytes("category"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[1].code[0].code),
            force_bytes("confirmed"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[1].path),
            force_bytes("clinicalStatus"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[2].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].codeFilter[2].valueSet),
            force_bytes("urn:oid:2.16.840.1.113883.3.464.1003.102.12.1011"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].type), force_bytes("Condition")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[0].code[0].code),
            force_bytes("diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[0].path),
            force_bytes("category"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[1].code[0].code),
            force_bytes("confirmed"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[1].path),
            force_bytes("clinicalStatus"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[2].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].codeFilter[2].valueSet),
            force_bytes("urn:oid:2.16.840.1.113883.3.464.1003.102.12.1012"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].type), force_bytes("Condition")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[0].code[0].code),
            force_bytes("finished"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[0].path),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[1].code[0].code),
            force_bytes("ambulatory"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[1].path),
            force_bytes("class"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[2].path), force_bytes("type")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].codeFilter[2].valueSet),
            force_bytes("urn:oid:2.16.840.1.113883.3.464.1003.101.12.1061"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[3].type), force_bytes("Encounter")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[4].codeFilter[0].path),
            force_bytes("diagnosis"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[4].codeFilter[0].valueSet),
            force_bytes("urn:oid:2.16.840.1.113883.3.464.1003.198.12.1012"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[4].type), force_bytes("DiagnosticReport")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[5].codeFilter[0].path), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[5].codeFilter[0].valueSet),
            force_bytes("urn:oid:2.16.840.1.113883.3.464.1003.196.12.1001"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[5].type), force_bytes("Medication")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].codeFilter[0].code[0].code),
            force_bytes("active"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].codeFilter[0].path),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].codeFilter[1].path),
            force_bytes("medication.code"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].codeFilter[1].valueSet),
            force_bytes("urn:oid:2.16.840.1.113883.3.464.1003.196.12.1001"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[6].type), force_bytes("MedicationRequest")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[7].codeFilter[0].code[0].code),
            force_bytes("completed"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[7].codeFilter[0].path),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[7].codeFilter[1].path),
            force_bytes("medication.code"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[7].codeFilter[1].valueSet),
            force_bytes("urn:oid:2.16.840.1.113883.3.464.1003.196.12.1001"),
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
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].resource),
            force_bytes("Library/library-quick-model-definition"),
        )
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

    def testLibrary10(self):
        inst = self.instantiate_from("library-opioidcds-recommendation-05.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary10(inst)

        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary10(inst2)

    def implLibrary10(self, inst):
        self.assertEqual(
            force_bytes(inst.author[0].name),
            force_bytes("Kensaku Kawamoto, MD, PhD, MHS"),
        )
        self.assertEqual(force_bytes(inst.author[1].name), force_bytes("Bryn Rhodes"))
        self.assertEqual(
            force_bytes(inst.author[2].name), force_bytes("Floyd Eisenberg, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.author[3].name), force_bytes("Robert McClure, MD, MPH")
        )
        self.assertEqual(
            force_bytes(inst.content[0].contentType), force_bytes("application/elm+xml")
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© CDC 2016+."))
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].code[0].code),
            force_bytes("active"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[0].path),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[1].code[0].code),
            force_bytes("outpatient"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[1].code[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/medicationrequest-category"
            ),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].codeFilter[1].path),
            force_bytes("category"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].id), force_bytes("medications")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("MedicationRequest")
        )
        self.assertEqual(inst.date.date, FHIRDate("2018-03-25T13:49:09-06:00").date)
        self.assertEqual(inst.date.as_json(), "2018-03-25T13:49:09-06:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Opioid Decision Support Logic for use in implementing CDC Opioid Prescribing Guidelines."
            ),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("opioidcds-recommendation-05")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("OpioidCDS_REC_05")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
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
            force_bytes(inst.publisher),
            force_bytes("Centers for Disease Control and Prevention (CDC)"),
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "This library works in concert with the OMTK logic library to provide decision support for Morphine Milligram Equivalence calculations and dynamic value resolution."
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes("CDC guideline for prescribing opioids for chronic pain"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("documentation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "https://guidelines.gov/summaries/summary/50153/cdc-guideline-for-prescribing-opioids-for-chronic-pain---united-states-2016#420"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].resource),
            force_bytes("Library/opioidcds-common"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("depends-on")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].display),
            force_bytes("MME Conversion Tables"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].type), force_bytes("documentation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].url),
            force_bytes(
                "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily_dose-a.pdf"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Opioid CDS Logic for recommendation #5"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Opioid Prescribing")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("logic-library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Logic Library")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/library-type"),
        )
        self.assertEqual(
            force_bytes(inst.usage),
            force_bytes(
                "This library is to notify the prescriber/user whether the current prescription exceeds the recommended MME."
            ),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("182888003"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("Medication requested (situation)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.display), force_bytes("Clinical Focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code),
            force_bytes("82423001"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display),
            force_bytes("Chronic pain (finding)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("0.1.0"))
