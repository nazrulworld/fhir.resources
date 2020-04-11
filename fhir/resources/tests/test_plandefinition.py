# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
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

from .. import plandefinition
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class PlanDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("PlanDefinition", js["resourceType"])
        return plandefinition.PlanDefinition(js)

    def testPlanDefinition1(self):
        inst = self.instantiate_from("plandefinition-example-kdn5-simplified.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition1(inst2)

    def implPlanDefinition1(self, inst):
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[0]
                .definitionCanonical
            ),
            force_bytes("#1111"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[0]
                .extension[0]
                .extension[0]
                .url
            ),
            force_bytes("day"),
        )
        self.assertEqual(
            inst.action[0]
            .action[0]
            .action[0]
            .action[0]
            .action[0]
            .extension[0]
            .extension[0]
            .valueInteger,
            1,
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[0]
                .extension[0]
                .extension[1]
                .url
            ),
            force_bytes("day"),
        )
        self.assertEqual(
            inst.action[0]
            .action[0]
            .action[0]
            .action[0]
            .action[0]
            .extension[0]
            .extension[1]
            .valueInteger,
            8,
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].action[0].action[0].extension[0].url
            ),
            force_bytes("http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].action[0].action[0].id),
            force_bytes("action-1"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].action[0].action[0].textEquivalent
            ),
            force_bytes("Gemcitabine 1250 mg/m² IV over 30 minutes on days 1 and 8"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[1]
                .definitionCanonical
            ),
            force_bytes("#2222"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[1]
                .extension[0]
                .extension[0]
                .url
            ),
            force_bytes("day"),
        )
        self.assertEqual(
            inst.action[0]
            .action[0]
            .action[0]
            .action[0]
            .action[1]
            .extension[0]
            .extension[0]
            .valueInteger,
            1,
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].action[0].action[1].extension[0].url
            ),
            force_bytes("http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].action[0].action[1].id),
            force_bytes("action-2"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[1]
                .relatedAction[0]
                .actionId
            ),
            force_bytes("action-1"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[1]
                .relatedAction[0]
                .relationship
            ),
            force_bytes("concurrent-with-start"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].action[0].action[1].textEquivalent
            ),
            force_bytes("CARBOplatin AUC 5 IV over 30 minutes on Day 1"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].action[0].id),
            force_bytes("cycle-definition-1"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].action[0].textEquivalent),
            force_bytes("21-day cycle for 6 cycles"),
        )
        self.assertEqual(
            inst.action[0].action[0].action[0].action[0].timingTiming.repeat.count, 6
        )
        self.assertEqual(
            inst.action[0].action[0].action[0].action[0].timingTiming.repeat.duration,
            21,
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .timingTiming.repeat.durationUnit
            ),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].groupingBehavior),
            force_bytes("sentence-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].selectionBehavior),
            force_bytes("exactly-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].selectionBehavior), force_bytes("all")
        )
        self.assertEqual(
            force_bytes(inst.action[0].selectionBehavior), force_bytes("exactly-one")
        )
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-07-27").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-07-27")
        self.assertEqual(
            force_bytes(inst.author[0].name), force_bytes("Lee Surprenant")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("1111"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("2222"))
        self.assertEqual(
            force_bytes(inst.copyright), force_bytes("All rights reserved.")
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("KDN5"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://example.org/ordertemplates"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("KDN5"))
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-07-27").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-07-27")
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
            force_bytes("National Comprehensive Cancer Network, Inc."),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes("NCCN Guidelines for Kidney Cancer. V.2.2016"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "http://www.example.org/professionals/physician_gls/PDF/kidney.pdf"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].citation),
            force_bytes("Oudard S, et al. J Urol. 2007;177(5):1698-702"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("citation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].url),
            force_bytes("http://www.ncbi.nlm.nih.gov/pubmed/17437788"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Gemcitabine/CARBOplatin")
        )
        self.assertEqual(
            force_bytes(inst.type.text), force_bytes("Chemotherapy Order Template")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code),
            force_bytes("treamentSetting-or-diseaseStatus"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://example.org/fhir/CodeSystem/indications"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].extension[0].valueString), force_bytes("A")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.text),
            force_bytes("Metastatic"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.code),
            force_bytes("disease-or-histology"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.system),
            force_bytes("http://example.org/fhir/CodeSystem/indications"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].extension[0].valueString), force_bytes("A")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.text),
            force_bytes("Collecting Duct/Medullary Subtypes"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].extension[0].valueString), force_bytes("A")
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].valueCodeableConcept.text),
            force_bytes("Kidney Cancer"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].code.code),
            force_bytes("treatmentSetting-or-diseaseStatus"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].code.system),
            force_bytes("http://example.org/fhir/CodeSystem/indications"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].extension[0].valueString), force_bytes("B")
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.text),
            force_bytes("Relapsed"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].code.code),
            force_bytes("disease-or-histology"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].code.system),
            force_bytes("http://example.org/fhir/CodeSystem/indications"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].extension[0].valueString), force_bytes("B")
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.text),
            force_bytes("Collecting Duct/Medullary Subtypes"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].extension[0].valueString), force_bytes("B")
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.text),
            force_bytes(
                "Kidney Cancer – Collecting Duct/Medullary Subtypes - Metastatic"
            ),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1"))

    def testPlanDefinition2(self):
        inst = self.instantiate_from("plandefinition-options-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition2(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition2(inst2)

    def implPlanDefinition2(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].definitionCanonical),
            force_bytes("#activitydefinition-medicationrequest-1"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].id), force_bytes("medication-action-1")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Administer Medication 1"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].definitionCanonical),
            force_bytes("#activitydefinition-medicationrequest-2"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].id), force_bytes("medication-action-2")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].relatedAction[0].actionId),
            force_bytes("medication-action-1"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].relatedAction[0].offsetDuration.unit),
            force_bytes("h"),
        )
        self.assertEqual(
            inst.action[0].action[1].relatedAction[0].offsetDuration.value, 1
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].relatedAction[0].relationship),
            force_bytes("after-end"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].title),
            force_bytes("Administer Medication 2"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].groupingBehavior), force_bytes("logical-group")
        )
        self.assertEqual(
            force_bytes(inst.action[0].selectionBehavior), force_bytes("all")
        )
        self.assertEqual(
            force_bytes(inst.contained[0].id),
            force_bytes("activitydefinition-medicationrequest-1"),
        )
        self.assertEqual(
            force_bytes(inst.contained[1].id),
            force_bytes("activitydefinition-medicationrequest-2"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("options-example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("This example illustrates relationships between actions."),
        )

    def testPlanDefinition3(self):
        inst = self.instantiate_from(
            "plandefinition-exclusive-breastfeeding-intervention-02.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition3(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition3(inst2)

    def implPlanDefinition3(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].expression.expression),
            force_bytes("Communication Request to Provider"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].path), force_bytes("/")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].textEquivalent),
            force_bytes(
                "A Breastfeeding Readiness Assessment is recommended, please authorize or reject the order."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Notify the provider to sign the order."),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].type.coding[0].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.expression),
            force_bytes("Should Notify Provider to Sign Assessment Order"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes(
                "Mother should be administered a breastfeeding readiness assessment."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].name), force_bytes("Admission")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].type), force_bytes("named-event")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[1].name), force_bytes("Birth")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[1].type), force_bytes("named-event")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[2].name),
            force_bytes("Infant Transfer to Recovery"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[2].type), force_bytes("named-event")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[3].name),
            force_bytes("Transfer to Post-Partum"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[3].type), force_bytes("named-event")
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-03-08").date)
        self.assertEqual(inst.date.as_json(), "2015-03-08")
        self.assertEqual(
            force_bytes(inst.id), force_bytes("exclusive-breastfeeding-intervention-02")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("exclusive-breastfeeding-intervention-02"),
        )
        self.assertEqual(
            force_bytes(inst.library[0]),
            force_bytes("Library/library-exclusive-breastfeeding-cds-logic"),
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
            force_bytes("Measure/measure-exclusive-breastfeeding"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Exclusive Breastfeeding Intervention-02"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Exclusive Breastfeeding")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testPlanDefinition4(self):
        inst = self.instantiate_from(
            "plandefinition-exclusive-breastfeeding-intervention-03.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition4(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition4(inst2)

    def implPlanDefinition4(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].expression.expression),
            force_bytes("Communication Request to Charge Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].path), force_bytes("/")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].textEquivalent),
            force_bytes(
                "A Breastfeeding Readiness Assessment is recommended, please administer the assessment."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Notify the charge nurse to perform the assessment."),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].type.coding[0].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].dynamicValue[0].expression.expression),
            force_bytes("Communication Request to Bedside Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].dynamicValue[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].dynamicValue[0].path), force_bytes("/")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].textEquivalent),
            force_bytes(
                "A Breastfeeding Readiness Assessment is recommended, please administer the assessment."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].title),
            force_bytes("Notify the bedside nurse to perform the assessment."),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].type.coding[0].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.expression),
            force_bytes("Should Notify Nurse to Perform Assessment"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes(
                "Mother should be administered a breastfeeding readiness assessment."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].name), force_bytes("Admission")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].type), force_bytes("named-event")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[1].name), force_bytes("Birth")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[1].type), force_bytes("named-event")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[2].name),
            force_bytes("Infant Transfer to Recovery"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[2].type), force_bytes("named-event")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[3].name),
            force_bytes("Transfer to Post-Partum"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[3].type), force_bytes("named-event")
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-03-08").date)
        self.assertEqual(inst.date.as_json(), "2015-03-08")
        self.assertEqual(
            force_bytes(inst.id), force_bytes("exclusive-breastfeeding-intervention-03")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("exclusive-breastfeeding-intervention-03"),
        )
        self.assertEqual(
            force_bytes(inst.library[0]),
            force_bytes("Library/library-exclusive-breastfeeding-cds-logic"),
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
            force_bytes("Measure/measure-exclusive-breastfeeding"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Exclusive Breastfeeding Intervention-03"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Exclusive Breastfeeding")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testPlanDefinition5(self):
        inst = self.instantiate_from("plandefinition-example-cardiology-os.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition5(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition5(inst2)

    def implPlanDefinition5(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].definitionCanonical),
            force_bytes("#referralToCardiologyConsult"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[0].expression.expression
            ),
            force_bytes("Now()"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[0].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[0].path),
            force_bytes("timing.event"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[1].expression.expression
            ),
            force_bytes(
                "Code '261QM0850X' from CardiologyChestPainLogic.\"NUCC Provider Taxonomy\" display 'Adult Mental Health'"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[1].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[1].path),
            force_bytes("specialty"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[2].expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.ServiceRequestFulfillmentTime"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[2].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[2].path),
            force_bytes("occurrenceDateTime"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[3].expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[3].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[3].path),
            force_bytes("subject"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[4].expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Practitioner"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[4].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[4].path),
            force_bytes("requester.agent"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[5].expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.CardiologyReferralReason"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[5].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[5].path),
            force_bytes("reasonCode"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[6].expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.RiskAssessment"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[6].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[6].path),
            force_bytes("reasonReference"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].textEquivalent),
            force_bytes("Referral to cardiology to evaluate chest pain (routine)"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[1].definitionCanonical),
            force_bytes("#CollectReferralReason"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[1].title),
            force_bytes("Reason for cardiology consultation"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[2].definitionCanonical),
            force_bytes("#CardiologyConsultationGoal"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[2].title),
            force_bytes("Goal of cardiology consultation"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].selectionBehavior), force_bytes("any")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Consults and Referrals"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].selectionBehavior),
            force_bytes("at-most-one"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[0].definitionCanonical
            ),
            force_bytes("#metoprololTartrate25Prescription"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[0]
                .dynamicValue[0]
                .expression.expression
            ),
            force_bytes("'draft'"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[0]
                .dynamicValue[0]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[0].dynamicValue[0].path
            ),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[0]
                .dynamicValue[1]
                .expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[0]
                .dynamicValue[1]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[0].dynamicValue[1].path
            ),
            force_bytes("patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[0]
                .dynamicValue[2]
                .expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Practitioner"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[0]
                .dynamicValue[2]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[0].dynamicValue[2].path
            ),
            force_bytes("prescriber"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[1].action[0].textEquivalent),
            force_bytes("metoprolol tartrate 25 mg tablet 1 tablet oral 2 time daily"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[1].definitionCanonical
            ),
            force_bytes("#metoprololTartrate50Prescription"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[1]
                .dynamicValue[0]
                .expression.expression
            ),
            force_bytes("'draft'"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[1]
                .dynamicValue[0]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[1].dynamicValue[0].path
            ),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[1]
                .dynamicValue[1]
                .expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[1]
                .dynamicValue[1]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[1].dynamicValue[1].path
            ),
            force_bytes("patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[1]
                .dynamicValue[2]
                .expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Practitioner"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[1]
                .dynamicValue[2]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[1].dynamicValue[2].path
            ),
            force_bytes("prescriber"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[1].action[1].textEquivalent),
            force_bytes("metoprolol tartrate 50 mg tablet 1 tablet oral 2 time daily"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[2].definitionCanonical
            ),
            force_bytes("#amlodipinePrescription"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[2]
                .dynamicValue[0]
                .expression.expression
            ),
            force_bytes("'draft'"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[2]
                .dynamicValue[0]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[2].dynamicValue[0].path
            ),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[2]
                .dynamicValue[1]
                .expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[2]
                .dynamicValue[1]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[2].dynamicValue[1].path
            ),
            force_bytes("patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[2]
                .dynamicValue[2]
                .expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Practitioner"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[1]
                .action[2]
                .dynamicValue[2]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[1].action[2].dynamicValue[2].path
            ),
            force_bytes("prescriber"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[1].action[2].textEquivalent),
            force_bytes("amlodipine 5  tablet 1 tablet oral  daily"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[1].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[1].selectionBehavior),
            force_bytes("at-most-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[1].title),
            force_bytes("Antianginal Therapy"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[2].action[0].definitionCanonical
            ),
            force_bytes("#nitroglycerinPrescription"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[2]
                .action[0]
                .dynamicValue[0]
                .expression.expression
            ),
            force_bytes("'draft'"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[2]
                .action[0]
                .dynamicValue[0]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[2].action[0].dynamicValue[0].path
            ),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[2]
                .action[0]
                .dynamicValue[1]
                .expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[2]
                .action[0]
                .dynamicValue[1]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[2].action[0].dynamicValue[1].path
            ),
            force_bytes("patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[2]
                .action[0]
                .dynamicValue[2]
                .expression.expression
            ),
            force_bytes("CardiologyChestPainLogic.Practitioner"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[2]
                .action[0]
                .dynamicValue[2]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[2].action[0].dynamicValue[2].path
            ),
            force_bytes("prescriber"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[2].action[0].textEquivalent),
            force_bytes(
                "nitroglycerin 0.4 mg tablet sub-lingual every 5 minutes as needed for chest pain; maximum 3 tablets"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[2].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[2].selectionBehavior),
            force_bytes("at-most-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[2].title),
            force_bytes("Nitroglycerin"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].description),
            force_bytes(
                "Consider the following medications for stable patients to be initiated prior to the cardiology consultation."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].title), force_bytes("Medications")
        )
        self.assertEqual(force_bytes(inst.author[0].name), force_bytes("Bruce Bray MD"))
        self.assertEqual(force_bytes(inst.author[1].name), force_bytes("Scott Wall MD"))
        self.assertEqual(
            force_bytes(inst.author[2].name), force_bytes("Aiden Abidov MD, PhD")
        )
        self.assertEqual(
            force_bytes(inst.contained[0].id), force_bytes("cardiology-chestPain-logic")
        )
        self.assertEqual(
            force_bytes(inst.contained[1].id),
            force_bytes("referralToCardiologyConsult"),
        )
        self.assertEqual(
            force_bytes(inst.contained[2].id),
            force_bytes("metoprololTartrate25Prescription"),
        )
        self.assertEqual(
            force_bytes(inst.contained[3].id),
            force_bytes("metoprololTartrate25Medication"),
        )
        self.assertEqual(
            force_bytes(inst.contained[4].id),
            force_bytes("metoprololTartrate25Substance"),
        )
        self.assertEqual(
            force_bytes(inst.contained[5].id),
            force_bytes("metoprololTartrate50Prescription"),
        )
        self.assertEqual(
            force_bytes(inst.contained[6].id),
            force_bytes("metoprololTartrate50Medication"),
        )
        self.assertEqual(
            force_bytes(inst.contained[7].id),
            force_bytes("metoprololTartrate50Substance"),
        )
        self.assertEqual(
            force_bytes(inst.contained[8].id), force_bytes("nitroglycerinPrescription")
        )
        self.assertEqual(
            force_bytes(inst.contained[9].id), force_bytes("nitroglycerinMedication")
        )
        self.assertEqual(
            force_bytes(inst.copyright),
            force_bytes(
                "© Copyright Cognitive Medical Systems, Inc. 9444 Waples Street Suite 300 San Diego, CA 92121"
            ),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-08-29").date)
        self.assertEqual(inst.date.as_json(), "2017-08-29")
        self.assertEqual(force_bytes(inst.id), force_bytes("example-cardiology-os"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:va.gov:kbs:knart:artifact:r1"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("bb7ccea6-9744-4743-854a-bcffd87191f6"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].system),
            force_bytes(
                "urn:va.gov:kbs:contract:VA118-16-D-1008:to:VA-118-16-F-1008-0007"
            ),
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].value), force_bytes("CLIN0004AG")
        )
        self.assertEqual(
            force_bytes(inst.identifier[2].system),
            force_bytes("urn:cognitivemedicine.com:lab:jira"),
        )
        self.assertEqual(force_bytes(inst.identifier[2].value), force_bytes("KP-914"))
        self.assertEqual(
            force_bytes(inst.library[0]), force_bytes("#cardiology-chestPain-logic")
        )
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("ChestPainCoronaryArteryDiseaseOrderSetKNART"),
        )
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Department of Veterans Affairs")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes(
                "Cardiology: Chest Pain (CP) / Coronary Artery Disease (CAD) Clinical Content White Paper"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url), force_bytes("NEED-A-URL-HERE")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].display),
            force_bytes(
                "Outcome CVD (coronary death, myocardial infarction, coronary insufficiency, angina, ischemic stroke, hemorrhagic stroke, transient ischemic attack, peripheral artery disease, heart failure)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("justification")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].url),
            force_bytes(
                "https://www.framinghamheartstudy.org/risk-functions/cardiovascular-disease/10-year-risk.php"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].display),
            force_bytes(
                "General cardiovascular risk profile for use in primary care: the Framingham Heart Study"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].type), force_bytes("justification")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].url),
            force_bytes(
                "https://www.framinghamheartstudy.org/risk-functions/cardiovascular-disease/10-year-risk.php"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[3].type), force_bytes("justification")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[3].url), force_bytes("NEED-A-URL-HERE")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[4].type), force_bytes("justification")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[4].url), force_bytes("NEED-A-URL-HERE")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[5].display),
            force_bytes("LABEL: ASPIRIN 81 MG- aspirin tablet, coated"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[5].type), force_bytes("justification")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[5].url),
            force_bytes(
                "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b4064039-2345-4227-b83d-54dc13a838d3"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[6].display),
            force_bytes(
                "LABEL: CLOPIDOGREL- clopidogrel bisulfate tablet, film coated"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[6].type), force_bytes("justification")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[6].url),
            force_bytes(
                "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7fe85155-bc00-406b-b097-e8aece187a8a"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[7].display),
            force_bytes("LABEL: LIPITOR- atorvastatin calcium tablet, film coated"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[7].type), force_bytes("justification")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[7].url),
            force_bytes(
                "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7fe85155-bc00-406b-b097-e8aece187a8a"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[8].display),
            force_bytes(
                "LABEL: METOPROLOL SUCCINATE EXTENDED-RELEASE - metoprolol succinate tablet, film coated, extended release"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[8].type), force_bytes("justification")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[8].url),
            force_bytes(
                "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2d948600-35d8-4490-983b-918bdce488c8"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[9].display),
            force_bytes("LABEL: NITROGLYCERIN- nitroglycerin tablet"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[9].type), force_bytes("justification")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[9].url),
            force_bytes(
                "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=67bf2a15-b115-47ac-ae28-ce2dafd6b5c9"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes(
                "Chest Pain (CP) - Coronary Artery Disease (CAD) Order Set KNART"
            ),
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("order-set")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Order Set")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/plan-definition-type"),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://va.gov/kas/orderset/B5-Cardiology-ChestPainCAD-OS"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("look up value"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("appropriate snomed condition"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("0.1"))

    def testPlanDefinition6(self):
        inst = self.instantiate_from("plandefinition-protocol-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition6(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition6(inst2)

    def implPlanDefinition6(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].cardinalityBehavior), force_bytes("single")
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.expression),
            force_bytes(
                "exists ([Condition: Obesity]) or not exists ([Observation: BMI] O where O.effectiveDateTime 2 years or less before Today())"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].definitionCanonical), force_bytes("#procedure")
        )
        self.assertEqual(
            force_bytes(inst.action[0].description),
            force_bytes("Measure, Weight, Height, Waist, Circumference; Calculate BMI"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].goalId[0]), force_bytes("reduce-bmi-ratio")
        )
        self.assertEqual(
            force_bytes(inst.action[0].requiredBehavior),
            force_bytes("must-unless-documented"),
        )
        self.assertEqual(force_bytes(inst.action[0].title), force_bytes("Measure BMI"))
        self.assertEqual(
            force_bytes(inst.author[0].name),
            force_bytes("National Heart, Lung, and Blood Institute"),
        )
        self.assertEqual(
            force_bytes(inst.author[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.author[0].telecom[0].value),
            force_bytes("https://www.nhlbi.nih.gov/health-pro/guidelines"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("procedure"))
        self.assertEqual(
            force_bytes(inst.goal[0].addresses[0].coding[0].code),
            force_bytes("414916001"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].addresses[0].coding[0].display),
            force_bytes("Obesity (disorder)"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].addresses[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].category.text), force_bytes("Treatment")
        )
        self.assertEqual(
            force_bytes(inst.goal[0].description.text),
            force_bytes("Reduce BMI to below 25"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].documentation[0].display),
            force_bytes("Evaluation and Treatment Strategy"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].documentation[0].type),
            force_bytes("justification"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].documentation[0].url),
            force_bytes(
                "https://www.nhlbi.nih.gov/health-pro/guidelines/current/obesity-guidelines/e_textbook/txgd/42.htm"
            ),
        )
        self.assertEqual(force_bytes(inst.goal[0].id), force_bytes("reduce-bmi-ratio"))
        self.assertEqual(
            force_bytes(inst.goal[0].priority.text), force_bytes("medium-priority")
        )
        self.assertEqual(
            force_bytes(inst.goal[0].start.text),
            force_bytes("When the patient's BMI Ratio is at or above 25"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].target[0].detailRange.high.unit),
            force_bytes("kg/m2"),
        )
        self.assertEqual(inst.goal[0].target[0].detailRange.high.value, 24.9)
        self.assertEqual(force_bytes(inst.goal[0].target[0].due.unit), force_bytes("a"))
        self.assertEqual(inst.goal[0].target[0].due.value, 1)
        self.assertEqual(
            force_bytes(inst.goal[0].target[0].measure.coding[0].code),
            force_bytes("39156-5"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].target[0].measure.coding[0].display),
            force_bytes("Body mass index (BMI) [Ratio]"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].target[0].measure.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("protocol-example"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("http://acme.org")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("example-1")
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
            force_bytes(inst.purpose),
            force_bytes(
                "Example of A medical algorithm for assessment and treatment of overweight and obesity"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes("Overweight and Obesity Treatment Guidelines"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "http://www.nhlbi.nih.gov/health-pro/guidelines/current/obesity-guidelines/e_textbook/txgd/algorthm/algorthm.htm"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Obesity Assessment Protocol")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("clinical-protocol")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("414916001"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("Obesity (disorder)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )

    def testPlanDefinition7(self):
        inst = self.instantiate_from("plandefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition7(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition7(inst2)

    def implPlanDefinition7(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].definitionCanonical),
            force_bytes("#referralToMentalHealthCare"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[0].expression.expression
            ),
            force_bytes("Now()"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[0].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[0].path),
            force_bytes("timing.event"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[1].expression.expression
            ),
            force_bytes(
                "Code '261QM0850X' from SuicideRiskLogic.\"NUCC Provider Taxonomy\" display 'Adult Mental Health'"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[1].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[1].path),
            force_bytes("specialty"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[2].expression.expression
            ),
            force_bytes("SuicideRiskLogic.ServiceRequestFulfillmentTime"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[2].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[2].path),
            force_bytes("occurrenceDateTime"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[3].expression.expression
            ),
            force_bytes("SuicideRiskLogic.Patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[3].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[3].path),
            force_bytes("subject"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[4].expression.expression
            ),
            force_bytes("SuicideRiskLogic.Practitioner"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[4].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[4].path),
            force_bytes("requester.agent"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[5].expression.expression
            ),
            force_bytes("SuicideRiskLogic.RiskAssessmentScore"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[5].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[5].path),
            force_bytes("reasonCode"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[6].expression.expression
            ),
            force_bytes("SuicideRiskLogic.RiskAssessment"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].dynamicValue[6].expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[6].path),
            force_bytes("reasonReference"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].textEquivalent),
            force_bytes(
                "Refer to outpatient mental health program for evaluation and treatment of mental health conditions now"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].selectionBehavior), force_bytes("any")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Consults and Referrals"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .definitionCanonical
            ),
            force_bytes("#citalopramPrescription"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[0]
                .expression.expression
            ),
            force_bytes("'draft'"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[0]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[0]
                .path
            ),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[1]
                .expression.expression
            ),
            force_bytes("SuicideRiskLogic.Patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[1]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[1]
                .path
            ),
            force_bytes("patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[2]
                .expression.expression
            ),
            force_bytes("SuicideRiskLogic.Practitioner"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[2]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[2]
                .path
            ),
            force_bytes("prescriber"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[3]
                .expression.expression
            ),
            force_bytes("SuicideRiskLogic.RiskAssessmentScore"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[3]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[3]
                .path
            ),
            force_bytes("reasonCode"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[4]
                .expression.expression
            ),
            force_bytes("SuicideRiskLogic.RiskAssessment"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[4]
                .expression.language
            ),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[4]
                .path
            ),
            force_bytes("reasonReference"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[0].textEquivalent
            ),
            force_bytes(
                "citalopram 20 mg tablet 1 tablet oral 1 time daily now (30 table; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[1].textEquivalent
            ),
            force_bytes(
                "escitalopram 10 mg tablet 1 tablet oral 1 time daily now (30 tablet; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[2].textEquivalent
            ),
            force_bytes(
                "fluoxetine 20 mg capsule 1 capsule oral 1 time daily now (30 tablet; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[3].textEquivalent
            ),
            force_bytes(
                "paroxetine 20 mg tablet 1 tablet oral 1 time daily now (30 tablet; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[4].textEquivalent
            ),
            force_bytes(
                "sertraline 50 mg tablet 1 tablet oral 1 time daily now (30 tablet; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .documentation[0]
                .document.contentType
            ),
            force_bytes("text/html"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .documentation[0]
                .document.title
            ),
            force_bytes(
                "National Library of Medicine. DailyMed website. CITALOPRAM- citalopram hydrobromide tablet, film coated."
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .documentation[0]
                .document.url
            ),
            force_bytes(
                "http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6daeb45c-451d-b135-bf8f-2d6dff4b6b01"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].documentation[0].type
            ),
            force_bytes("citation"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[0].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[0].selectionBehavior),
            force_bytes("at-most-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[0].title),
            force_bytes(
                "Selective Serotonin Reuptake Inhibitors (Choose a mazimum of one or document reasons for exception)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[1].textEquivalent),
            force_bytes(
                "Dopamine Norepinephrine Reuptake Inhibitors (Choose a maximum of one or document reasons for exception)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[2].textEquivalent),
            force_bytes(
                "Serotonin Norepinephrine Reuptake Inhibitors (Choose a maximum of one or doument reasons for exception)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[3].textEquivalent),
            force_bytes(
                "Norepinephrine-Serotonin Modulators (Choose a maximum of one or document reasons for exception)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].documentation[0].document.contentType
            ),
            force_bytes("text/html"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .documentation[0]
                .document.extension[0]
                .url
            ),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/cqf-qualityOfEvidence"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("high"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://terminology.hl7.org/CodeSystem/evidence-quality"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.text
            ),
            force_bytes("High Quality"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].documentation[0].document.title
            ),
            force_bytes(
                "Practice Guideline for the Treatment of Patients with Major Depressive Disorder"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].documentation[0].document.url
            ),
            force_bytes(
                "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].documentation[0].type),
            force_bytes("citation"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].selectionBehavior),
            force_bytes("at-most-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].title),
            force_bytes("First-Line Antidepressants"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].selectionBehavior),
            force_bytes("at-most-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].title), force_bytes("Medications")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes("Suicide Risk Assessment and Outpatient Management"),
        )
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-03-12").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-03-12")
        self.assertEqual(
            force_bytes(inst.author[0].name), force_bytes("Motive Medical Intelligence")
        )
        self.assertEqual(
            force_bytes(inst.author[0].telecom[0].system), force_bytes("phone")
        )
        self.assertEqual(
            force_bytes(inst.author[0].telecom[0].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.author[0].telecom[0].value), force_bytes("415-362-4007")
        )
        self.assertEqual(
            force_bytes(inst.author[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.author[0].telecom[1].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.author[0].telecom[1].value),
            force_bytes("info@motivemi.com"),
        )
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
            force_bytes(inst.contained[0].id), force_bytes("referralToMentalHealthCare")
        )
        self.assertEqual(
            force_bytes(inst.contained[1].id), force_bytes("citalopramPrescription")
        )
        self.assertEqual(
            force_bytes(inst.contained[2].id), force_bytes("citalopramMedication")
        )
        self.assertEqual(
            force_bytes(inst.contained[3].id), force_bytes("citalopramSubstance")
        )
        self.assertEqual(
            force_bytes(inst.copyright),
            force_bytes(
                "© Copyright 2016 Motive Medical Intelligence. All rights reserved."
            ),
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-08-15").date)
        self.assertEqual(inst.date.as_json(), "2015-08-15")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Orders to be applied to a patient characterized as low suicide risk."
            ),
        )
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2016-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("low-suicide-risk-order-set")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://motivemi.com/artifacts"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("mmi:low-suicide-risk-order-set"),
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
            force_bytes(inst.library[0]),
            force_bytes("Library/suiciderisk-orderset-logic"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("LowSuicideRiskOrderSet"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Motive Medical Intelligence")
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "This order set helps ensure consistent application of appropriate orders for the care of low suicide risk patients."
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes(
                "Practice Guideline for the Treatment of Patients with Major Depressive Disorder"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].resource),
            force_bytes("ActivityDefinition/referralPrimaryCareMentalHealth"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("composed-of")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].resource),
            force_bytes("ActivityDefinition/citalopramPrescription"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].type), force_bytes("composed-of")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Low Suicide Risk Order Set")
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Suicide risk assessment")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://motivemi.com/artifacts/PlanDefinition/low-suicide-risk-order-set"
            ),
        )
        self.assertEqual(
            force_bytes(inst.usage),
            force_bytes(
                "This order set should be applied after assessing a patient for suicide risk, when the findings of that assessment indicate the patient has low suicide risk."
            ),
        )
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("age"))
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
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
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
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
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
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
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].code),
            force_bytes("394687007"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].display),
            force_bytes("Low suicide risk"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].code),
            force_bytes("225337009"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].display),
            force_bytes("Suicide risk assessment"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.useContext[5].code.code), force_bytes("user"))
        self.assertEqual(
            force_bytes(inst.useContext[5].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].code),
            force_bytes("309343006"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].display),
            force_bytes("Physician"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].code.code), force_bytes("venue")
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].code),
            force_bytes("440655000"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].display),
            force_bytes("Outpatient environment"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testPlanDefinition8(self):
        inst = self.instantiate_from("plandefinition-opioidcds-08.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition8(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition8(inst2)

    def implPlanDefinition8(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].description),
            force_bytes("Will offer Naloxone instead"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].description),
            force_bytes(
                "Risk of overdose carefully considered and outweighed by benefit; snooze 3 mo"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[2].description),
            force_bytes("N/A - see comment; snooze 3 mo"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.expression),
            force_bytes("Inclusion Criteria"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].description),
            force_bytes(
                "Checking if the trigger prescription meets the inclusion criteria for recommendation #8 workflow."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].documentation[0].document.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/cqf-strengthOfRecommendation"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("strong"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Strong"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/recommendation-strength"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].documentation[0].document.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/cqf-qualityOfEvidence"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[1]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("low"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[1]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Low quality"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[1]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://terminology.hl7.org/CodeSystem/evidence-quality"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].documentation[0].type),
            force_bytes("documentation"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[0].expression.expression),
            force_bytes("Get Detail"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[0].path),
            force_bytes("action.description"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[1].expression.expression),
            force_bytes("Get Summary"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[1].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[1].path),
            force_bytes("action.title"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[2].expression.expression),
            force_bytes("Get Indicator"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[2].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[2].path),
            force_bytes("action.extension"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].groupingBehavior), force_bytes("visual-group")
        )
        self.assertEqual(
            force_bytes(inst.action[0].selectionBehavior), force_bytes("exactly-one")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes(
                "Existing patient exhibits risk factors for opioid-related harms."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].name),
            force_bytes("medication-prescribe"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].type), force_bytes("named-event")
        )
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
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© CDC 2016+."))
        self.assertEqual(inst.date.date, FHIRDate("2018-03-19").date)
        self.assertEqual(inst.date.as_json(), "2018-03-19")
        self.assertEqual(force_bytes(inst.id), force_bytes("opioidcds-08"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("cdc-opioid-guidance")
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
        self.assertEqual(
            force_bytes(inst.library[0]),
            force_bytes("Library/opioidcds-recommendation-08"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("cdc-opioid-08"))
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
            force_bytes(inst.relatedArtifact[1].display),
            force_bytes("MME Conversion Tables"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("documentation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].url),
            force_bytes(
                "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily_dose-a.pdf"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("CDC Opioid Prescribing Guideline Recommendation #8"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Opioid Prescribing")
        )
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("eca-rule"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("ECA Rule")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/plan-definition-type"),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/ig/opioid-cds/PlanDefinition/opioidcds-08"
            ),
        )
        self.assertEqual(
            force_bytes(inst.usage),
            force_bytes(
                "Before starting and periodically during continuation of opioid therapy, clinicians should evaluate risk factors for opioid-related harms."
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

    def testPlanDefinition9(self):
        inst = self.instantiate_from(
            "plandefinition-exclusive-breastfeeding-intervention-04.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition9(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition9(inst2)

    def implPlanDefinition9(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].expression.expression),
            force_bytes("Create Lactation Consult Request"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].path), force_bytes("/")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].textEquivalent),
            force_bytes("Create a lactation consult request"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Create a lactation consult request."),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].type.coding[0].code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.expression),
            force_bytes("Should Create Lactation Consult"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes(
                "Mother should be referred to a lactation specialist for consultation."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].name), force_bytes("Admission")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].type), force_bytes("named-event")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[1].name), force_bytes("Birth")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[1].type), force_bytes("named-event")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[2].name),
            force_bytes("Infant Transfer to Recovery"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[2].type), force_bytes("named-event")
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[3].name),
            force_bytes("Transfer to Post-Partum"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[3].type), force_bytes("named-event")
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-03-08").date)
        self.assertEqual(inst.date.as_json(), "2015-03-08")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Exclusive breastfeeding intervention intended to improve outcomes for exclusive breastmilk feeding of newborns by creating a lactation consult for the mother if appropriate."
            ),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("exclusive-breastfeeding-intervention-04")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("exclusive-breastfeeding-intervention-04"),
        )
        self.assertEqual(
            force_bytes(inst.library[0]),
            force_bytes("Library/library-exclusive-breastfeeding-cds-logic"),
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
            force_bytes("Measure/measure-exclusive-breastfeeding"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Exclusive Breastfeeding Intervention-04"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Exclusive Breastfeeding")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testPlanDefinition10(self):
        inst = self.instantiate_from("plandefinition-opioidcds-04.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition10(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition10(inst2)

    def implPlanDefinition10(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].description),
            force_bytes("Will precribe immediate release"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].description),
            force_bytes(
                "Risk of overdose carefully considered and outweighed by benefit; snooze 3 mo"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[2].description),
            force_bytes("N/A - see comment; snooze 3 mo"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.description),
            force_bytes(
                "Check whether the opioid prescription for the existing patient is extended-release without any opioids-with-abuse-potential prescribed in the past 90 days."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.expression),
            force_bytes("Inclusion Criteria"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].description),
            force_bytes(
                "Checking if the trigger prescription meets the inclusion criteria for recommendation #4 workflow."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].documentation[0].document.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/cqf-strengthOfRecommendation"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("strong"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Strong"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/recommendation-strength"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].documentation[0].document.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/cqf-qualityOfEvidence"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[1]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("low"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[1]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Low quality"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .documentation[0]
                .document.extension[1]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://terminology.hl7.org/CodeSystem/evidence-quality"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].documentation[0].type),
            force_bytes("documentation"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[0].expression.expression),
            force_bytes("Get Summary"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[0].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[0].path),
            force_bytes("action.title"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[1].expression.expression),
            force_bytes("Get Detail"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[1].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[1].path),
            force_bytes("action.description"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[2].expression.expression),
            force_bytes("Get Indicator"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[2].expression.language),
            force_bytes("text/cql"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[2].path),
            force_bytes("activity.extension"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].groupingBehavior), force_bytes("visual-group")
        )
        self.assertEqual(
            force_bytes(inst.action[0].selectionBehavior), force_bytes("exactly-one")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes("Extended-release opioid prescription triggered."),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].name),
            force_bytes("medication-prescribe"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].trigger[0].type), force_bytes("named-event")
        )
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
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© CDC 2016+."))
        self.assertEqual(inst.date.date, FHIRDate("2018-03-19").date)
        self.assertEqual(inst.date.as_json(), "2018-03-19")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "When starting opioid therapy for chronic pain, clinicians should prescribe immediate-release opioids instead of extended-release/long-acting (ER/LA) opioids."
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("opioidcds-04"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("cdc-opioid-guidance")
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
        self.assertEqual(
            force_bytes(inst.library[0]),
            force_bytes("Library/opioidcds-recommendation-04"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("cdc-opioid-04"))
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
            force_bytes(inst.relatedArtifact[1].display),
            force_bytes("MME Conversion Tables"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("documentation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].url),
            force_bytes(
                "https://www.cdc.gov/drugoverdose/pdf/calculating_total_daily_dose-a.pdf"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("CDC Opioid Prescribing Guideline Recommendation #4"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Opioid Prescribing")
        )
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("eca-rule"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("ECA Rule")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/plan-definition-type"),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/ig/opioid-cds/PlanDefinition/opioidcds-04"
            ),
        )
        self.assertEqual(
            force_bytes(inst.usage),
            force_bytes(
                "Providers should use caution when prescribing extended-release/long-acting (ER/LA) opioids as they carry a higher risk and negligible benefit compared to immediate-release opioids."
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
