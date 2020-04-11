# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
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

from .. import operationdefinition
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class OperationDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("OperationDefinition", js["resourceType"])
        return operationdefinition.OperationDefinition(js)

    def testOperationDefinition1(self):
        inst = self.instantiate_from("operation-measure-data-requirements.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition1(inst2)

    def implOperationDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("data-requirements"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "The data-requirements operation aggregates and returns the parameters and data requirements for the measure and all its dependencies as a single module definition"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("Measure-data-requirements"))
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Data Requirements"))
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(
            force_bytes(inst.parameter[0].name), force_bytes("periodStart")
        )
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("date"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[1].documentation),
            force_bytes(
                "The end of the measurement period. The period will end at the end of the period implied by the supplied timestamp. E.g. a value of 2014 would set the period end to be 2014-12-31T23:59:59 inclusive"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 1)
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("periodEnd"))
        self.assertEqual(force_bytes(inst.parameter[1].type), force_bytes("date"))
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[2].documentation),
            force_bytes(
                "The result of the requirements gathering is a module-definition Library that describes the aggregate parameters, data requirements, and dependencies of the measure"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[2].max), force_bytes("1"))
        self.assertEqual(inst.parameter[2].min, 1)
        self.assertEqual(force_bytes(inst.parameter[2].name), force_bytes("return"))
        self.assertEqual(force_bytes(inst.parameter[2].type), force_bytes("Library"))
        self.assertEqual(force_bytes(inst.parameter[2].use), force_bytes("out"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.resource[0]), force_bytes("Measure"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertFalse(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/OperationDefinition/Measure-data-requirements"
            ),
        )

    def testOperationDefinition2(self):
        inst = self.instantiate_from("operation-conceptmap-translate.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition2(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition2(inst2)

    def implOperationDefinition2(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("translate"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("ConceptMap-translate"))
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Concept Translation"))
        self.assertEqual(
            force_bytes(inst.parameter[0].documentation),
            force_bytes(
                "The code that is to be translated. If a code is provided, a system must be provided"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 0)
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("code"))
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("code"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[1].documentation),
            force_bytes("The system for the code that is to be translated"),
        )
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 0)
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("system"))
        self.assertEqual(force_bytes(inst.parameter[1].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[2].documentation),
            force_bytes(
                "The version of the system, if one was provided in the source data"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[2].max), force_bytes("1"))
        self.assertEqual(inst.parameter[2].min, 0)
        self.assertEqual(force_bytes(inst.parameter[2].name), force_bytes("version"))
        self.assertEqual(force_bytes(inst.parameter[2].type), force_bytes("string"))
        self.assertEqual(force_bytes(inst.parameter[2].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[3].max), force_bytes("1"))
        self.assertEqual(inst.parameter[3].min, 0)
        self.assertEqual(force_bytes(inst.parameter[3].name), force_bytes("source"))
        self.assertEqual(force_bytes(inst.parameter[3].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.parameter[3].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[4].documentation),
            force_bytes("A coding to translate"),
        )
        self.assertEqual(force_bytes(inst.parameter[4].max), force_bytes("1"))
        self.assertEqual(inst.parameter[4].min, 0)
        self.assertEqual(force_bytes(inst.parameter[4].name), force_bytes("coding"))
        self.assertEqual(force_bytes(inst.parameter[4].type), force_bytes("Coding"))
        self.assertEqual(force_bytes(inst.parameter[4].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[5].documentation),
            force_bytes(
                "A full codeableConcept to validate. The server can translate any of the coding values (e.g. existing translations) as it chooses"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[5].max), force_bytes("1"))
        self.assertEqual(inst.parameter[5].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[5].name), force_bytes("codeableConcept")
        )
        self.assertEqual(
            force_bytes(inst.parameter[5].type), force_bytes("CodeableConcept")
        )
        self.assertEqual(force_bytes(inst.parameter[5].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[6].max), force_bytes("1"))
        self.assertEqual(inst.parameter[6].min, 0)
        self.assertEqual(force_bytes(inst.parameter[6].name), force_bytes("target"))
        self.assertEqual(force_bytes(inst.parameter[6].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.parameter[6].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[7].max), force_bytes("1"))
        self.assertEqual(inst.parameter[7].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[7].name), force_bytes("targetsystem")
        )
        self.assertEqual(force_bytes(inst.parameter[7].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.parameter[7].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[8].documentation),
            force_bytes("Another element that may help produce the correct mapping"),
        )
        self.assertEqual(force_bytes(inst.parameter[8].max), force_bytes("*"))
        self.assertEqual(inst.parameter[8].min, 0)
        self.assertEqual(force_bytes(inst.parameter[8].name), force_bytes("dependency"))
        self.assertEqual(
            force_bytes(inst.parameter[8].part[0].documentation),
            force_bytes("The element for this dependency"),
        )
        self.assertEqual(force_bytes(inst.parameter[8].part[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[8].part[0].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[8].part[0].name), force_bytes("element")
        )
        self.assertEqual(
            force_bytes(inst.parameter[8].part[0].type), force_bytes("uri")
        )
        self.assertEqual(force_bytes(inst.parameter[8].part[0].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[8].part[1].documentation),
            force_bytes("The value for this dependency"),
        )
        self.assertEqual(force_bytes(inst.parameter[8].part[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[8].part[1].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[8].part[1].name), force_bytes("concept")
        )
        self.assertEqual(
            force_bytes(inst.parameter[8].part[1].type), force_bytes("CodeableConcept")
        )
        self.assertEqual(force_bytes(inst.parameter[8].part[1].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[8].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[9].documentation),
            force_bytes(
                "if this is true, then the operation should return all the codes that might be mapped to this code. This parameter reverses the meaning of the source and target parameters"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[9].max), force_bytes("1"))
        self.assertEqual(inst.parameter[9].min, 0)
        self.assertEqual(force_bytes(inst.parameter[9].name), force_bytes("reverse"))
        self.assertEqual(force_bytes(inst.parameter[9].type), force_bytes("boolean"))
        self.assertEqual(force_bytes(inst.parameter[9].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.resource[0]), force_bytes("ConceptMap"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertTrue(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/OperationDefinition/ConceptMap-translate"),
        )

    def testOperationDefinition3(self):
        inst = self.instantiate_from("operation-valueset-expand.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition3(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition3(inst2)

    def implOperationDefinition3(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("expand"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("ValueSet-expand"))
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Value Set Expansion"))
        self.assertEqual(
            force_bytes(inst.parameter[0].documentation),
            force_bytes(
                "A canonical url for a value set. The server must know the value set (e.g. it is defined explicitly in the server's value sets, or it is defined implicitly by some code system known to the server"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 0)
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("url"))
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[1].documentation),
            force_bytes(
                "The value set is provided directly as part of the request. Servers may choose not to accept value sets in this fashion"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 0)
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("valueSet"))
        self.assertEqual(force_bytes(inst.parameter[1].type), force_bytes("ValueSet"))
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[2].max), force_bytes("1"))
        self.assertEqual(inst.parameter[2].min, 0)
        self.assertEqual(force_bytes(inst.parameter[2].name), force_bytes("context"))
        self.assertEqual(force_bytes(inst.parameter[2].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.parameter[2].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[3].max), force_bytes("1"))
        self.assertEqual(inst.parameter[3].min, 0)
        self.assertEqual(force_bytes(inst.parameter[3].name), force_bytes("filter"))
        self.assertEqual(force_bytes(inst.parameter[3].type), force_bytes("string"))
        self.assertEqual(force_bytes(inst.parameter[3].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[4].max), force_bytes("1"))
        self.assertEqual(inst.parameter[4].min, 0)
        self.assertEqual(force_bytes(inst.parameter[4].name), force_bytes("profile"))
        self.assertEqual(force_bytes(inst.parameter[4].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.parameter[4].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[5].max), force_bytes("1"))
        self.assertEqual(inst.parameter[5].min, 0)
        self.assertEqual(force_bytes(inst.parameter[5].name), force_bytes("date"))
        self.assertEqual(force_bytes(inst.parameter[5].type), force_bytes("dateTime"))
        self.assertEqual(force_bytes(inst.parameter[5].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[6].documentation),
            force_bytes(
                "Paging support - where to start if a subset is desired (default = 0). Offset is number of records (not number of pages)"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[6].max), force_bytes("1"))
        self.assertEqual(inst.parameter[6].min, 0)
        self.assertEqual(force_bytes(inst.parameter[6].name), force_bytes("offset"))
        self.assertEqual(force_bytes(inst.parameter[6].type), force_bytes("integer"))
        self.assertEqual(force_bytes(inst.parameter[6].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[7].max), force_bytes("1"))
        self.assertEqual(inst.parameter[7].min, 0)
        self.assertEqual(force_bytes(inst.parameter[7].name), force_bytes("count"))
        self.assertEqual(force_bytes(inst.parameter[7].type), force_bytes("integer"))
        self.assertEqual(force_bytes(inst.parameter[7].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[8].documentation),
            force_bytes(
                "Controls whether concept designations are to be included or excluded in value set expansions. Overrides the value in the expansion profile if there is one"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[8].max), force_bytes("1"))
        self.assertEqual(inst.parameter[8].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[8].name), force_bytes("includeDesignations")
        )
        self.assertEqual(force_bytes(inst.parameter[8].type), force_bytes("boolean"))
        self.assertEqual(force_bytes(inst.parameter[8].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[9].documentation),
            force_bytes(
                "Controls whether the value set definition is included or excluded in value set expansions. Overrides the value in the expansion profile if there is one"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[9].max), force_bytes("1"))
        self.assertEqual(inst.parameter[9].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[9].name), force_bytes("includeDefinition")
        )
        self.assertEqual(force_bytes(inst.parameter[9].type), force_bytes("boolean"))
        self.assertEqual(force_bytes(inst.parameter[9].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.resource[0]), force_bytes("ValueSet"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertTrue(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/OperationDefinition/ValueSet-expand"),
        )

    def testOperationDefinition4(self):
        inst = self.instantiate_from("operation-questionnaire-populate.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition4(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition4(inst2)

    def implOperationDefinition4(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("populate"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("Questionnaire-populate"))
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Populate Questionnaire"))
        self.assertEqual(
            force_bytes(inst.parameter[0].documentation),
            force_bytes(
                "A logical questionnaire identifier (i.e. ''Questionnaire.identifier''). The server must know the questionnaire or be able to retrieve it from other known repositories."
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 0)
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("identifier"))
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[1].documentation),
            force_bytes(
                "The [Questionnaire](questionnaire.html) is provided directly as part of the request. Servers may choose not to accept questionnaires in this fashion"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[1].name), force_bytes("questionnaire")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].type), force_bytes("Questionnaire")
        )
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[2].max), force_bytes("1"))
        self.assertEqual(inst.parameter[2].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[2].name), force_bytes("questionnaireRef")
        )
        self.assertEqual(force_bytes(inst.parameter[2].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[2].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[3].max), force_bytes("1"))
        self.assertEqual(inst.parameter[3].min, 1)
        self.assertEqual(force_bytes(inst.parameter[3].name), force_bytes("subject"))
        self.assertEqual(force_bytes(inst.parameter[3].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[3].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[4].max), force_bytes("*"))
        self.assertEqual(inst.parameter[4].min, 0)
        self.assertEqual(force_bytes(inst.parameter[4].name), force_bytes("content"))
        self.assertEqual(force_bytes(inst.parameter[4].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[4].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[5].documentation),
            force_bytes(
                "If specified and set to 'true' (and the server is capable), the server should use what resources and other knowledge it has about the referenced subject when pre-populating answers to questions."
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[5].max), force_bytes("1"))
        self.assertEqual(inst.parameter[5].min, 0)
        self.assertEqual(force_bytes(inst.parameter[5].name), force_bytes("local"))
        self.assertEqual(force_bytes(inst.parameter[5].type), force_bytes("boolean"))
        self.assertEqual(force_bytes(inst.parameter[5].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[6].documentation),
            force_bytes(
                "The partially (or fully)-populated set of answers for the specified Questionnaire"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[6].max), force_bytes("1"))
        self.assertEqual(inst.parameter[6].min, 1)
        self.assertEqual(
            force_bytes(inst.parameter[6].name), force_bytes("questionnaire")
        )
        self.assertEqual(
            force_bytes(inst.parameter[6].type), force_bytes("QuestionnaireResponse")
        )
        self.assertEqual(force_bytes(inst.parameter[6].use), force_bytes("out"))
        self.assertEqual(force_bytes(inst.parameter[7].max), force_bytes("1"))
        self.assertEqual(inst.parameter[7].min, 0)
        self.assertEqual(force_bytes(inst.parameter[7].name), force_bytes("issues"))
        self.assertEqual(
            force_bytes(inst.parameter[7].type), force_bytes("OperationOutcome")
        )
        self.assertEqual(force_bytes(inst.parameter[7].use), force_bytes("out"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.resource[0]), force_bytes("Questionnaire"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertTrue(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/OperationDefinition/Questionnaire-populate"
            ),
        )

    def testOperationDefinition5(self):
        inst = self.instantiate_from("operation-resource-meta-add.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition5(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition5(inst2)

    def implOperationDefinition5(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("meta-add"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("Resource-meta-add"))
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Add profiles, tags, and security labels to a resource"),
        )
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("meta"))
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("Meta"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[1].documentation),
            force_bytes("Resulting meta for the resource"),
        )
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 1)
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("return"))
        self.assertEqual(force_bytes(inst.parameter[1].type), force_bytes("Meta"))
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("out"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.resource[0]), force_bytes("Resource"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertFalse(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/OperationDefinition/Resource-meta-add"),
        )

    def testOperationDefinition6(self):
        inst = self.instantiate_from("operation-encounter-everything.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition6(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition6(inst2)

    def implOperationDefinition6(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("everything"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("Encounter-everything"))
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Fetch Encounter Record"))
        self.assertEqual(
            force_bytes(inst.parameter[0].documentation),
            force_bytes('The bundle type is "searchset"'),
        )
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("return"))
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("Bundle"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("out"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.resource[0]), force_bytes("Encounter"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertFalse(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/OperationDefinition/Encounter-everything"),
        )

    def testOperationDefinition7(self):
        inst = self.instantiate_from("operation-servicedefinition-evaluate.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition7(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition7(inst2)

    def implOperationDefinition7(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("evaluate"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "The evaluate operation requests clinical decision support guidance based on a specific decision support module"
            ),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("ServiceDefinition-evaluate")
        )
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Evaluate"))
        self.assertEqual(
            force_bytes(inst.parameter[0].documentation),
            force_bytes("An optional client-provided identifier to track the request."),
        )
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 0)
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("requestId"))
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("id"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[1].name), force_bytes("evaluateAtDateTime")
        )
        self.assertEqual(force_bytes(inst.parameter[1].type), force_bytes("dateTime"))
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[2].documentation),
            force_bytes(
                "The input parameters for a request, if any. These parameters are defined by the module that is the target of the evaluation, and typically supply patient-independent information to the module."
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[2].max), force_bytes("1"))
        self.assertEqual(inst.parameter[2].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[2].name), force_bytes("inputParameters")
        )
        self.assertEqual(force_bytes(inst.parameter[2].type), force_bytes("Parameters"))
        self.assertEqual(force_bytes(inst.parameter[2].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[3].documentation),
            force_bytes(
                "The input data for the request. These data are defined by the data requirements of the module and typically provide patient-dependent information."
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[3].max), force_bytes("*"))
        self.assertEqual(inst.parameter[3].min, 0)
        self.assertEqual(force_bytes(inst.parameter[3].name), force_bytes("inputData"))
        self.assertEqual(force_bytes(inst.parameter[3].type), force_bytes("Any"))
        self.assertEqual(force_bytes(inst.parameter[3].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[4].documentation),
            force_bytes("The patient in context, if any."),
        )
        self.assertEqual(force_bytes(inst.parameter[4].max), force_bytes("1"))
        self.assertEqual(inst.parameter[4].min, 0)
        self.assertEqual(force_bytes(inst.parameter[4].name), force_bytes("patient"))
        self.assertEqual(force_bytes(inst.parameter[4].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[4].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[5].documentation),
            force_bytes("The encounter in context, if any."),
        )
        self.assertEqual(force_bytes(inst.parameter[5].max), force_bytes("1"))
        self.assertEqual(inst.parameter[5].min, 0)
        self.assertEqual(force_bytes(inst.parameter[5].name), force_bytes("encounter"))
        self.assertEqual(force_bytes(inst.parameter[5].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[5].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[6].documentation),
            force_bytes("The organization initiating the request."),
        )
        self.assertEqual(force_bytes(inst.parameter[6].max), force_bytes("1"))
        self.assertEqual(inst.parameter[6].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[6].name), force_bytes("initiatingOrganization")
        )
        self.assertEqual(force_bytes(inst.parameter[6].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[6].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[7].documentation),
            force_bytes("The person initiating the request."),
        )
        self.assertEqual(force_bytes(inst.parameter[7].max), force_bytes("1"))
        self.assertEqual(inst.parameter[7].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[7].name), force_bytes("initiatingPerson")
        )
        self.assertEqual(force_bytes(inst.parameter[7].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[7].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[8].documentation),
            force_bytes(
                "The type of user initiating the request, e.g. patient, healthcare provider, or specific type of healthcare provider (physician, nurse, etc.)."
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[8].max), force_bytes("1"))
        self.assertEqual(inst.parameter[8].min, 0)
        self.assertEqual(force_bytes(inst.parameter[8].name), force_bytes("userType"))
        self.assertEqual(
            force_bytes(inst.parameter[8].type), force_bytes("CodeableConcept")
        )
        self.assertEqual(force_bytes(inst.parameter[8].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[9].documentation),
            force_bytes("Preferred language of the person using the system."),
        )
        self.assertEqual(force_bytes(inst.parameter[9].max), force_bytes("1"))
        self.assertEqual(inst.parameter[9].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[9].name), force_bytes("userLanguage")
        )
        self.assertEqual(
            force_bytes(inst.parameter[9].type), force_bytes("CodeableConcept")
        )
        self.assertEqual(force_bytes(inst.parameter[9].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(
            force_bytes(inst.resource[0]), force_bytes("ServiceDefinition")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertFalse(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/OperationDefinition/ServiceDefinition-evaluate"
            ),
        )

    def testOperationDefinition8(self):
        inst = self.instantiate_from("operation-resource-meta.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition8(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition8(inst2)

    def implOperationDefinition8(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("meta"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("Resource-meta"))
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Access a list of profiles, tags, and security labels"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].documentation),
            force_bytes("The meta returned by the operation"),
        )
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("return"))
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("Meta"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("out"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.resource[0]), force_bytes("Resource"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertTrue(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertTrue(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/OperationDefinition/Resource-meta"),
        )

    def testOperationDefinition9(self):
        inst = self.instantiate_from(
            "operation-servicedefinition-data-requirements.json"
        )
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition9(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition9(inst2)

    def implOperationDefinition9(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("data-requirements"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "The data-requirements operation aggregates and returns the parameters and data requirements for the service module and all its dependencies as a single module definition library."
            ),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("ServiceDefinition-data-requirements")
        )
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Data Requirements"))
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[0].name), force_bytes("evaluateAtDateTime")
        )
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("dateTime"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[1].documentation),
            force_bytes(
                "The result of the requirements gathering is a module-definition Library that describes the aggregate parameters, data requirements, and dependencies of the service."
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 1)
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("return"))
        self.assertEqual(force_bytes(inst.parameter[1].type), force_bytes("Library"))
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("out"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(
            force_bytes(inst.resource[0]), force_bytes("ServiceDefinition")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertFalse(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/OperationDefinition/ServiceDefinition-data-requirements"
            ),
        )

    def testOperationDefinition10(self):
        inst = self.instantiate_from("operation-measure-evaluate-measure.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a OperationDefinition instance"
        )
        self.implOperationDefinition10(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition10(inst2)

    def implOperationDefinition10(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("evaluate-measure"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "The evaluate-measure operation is used to invoke an eMeasure and obtain the results"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("Measure-evaluate-measure"))
        self.assertTrue(inst.instance)
        self.assertEqual(force_bytes(inst.kind), force_bytes("operation"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Evaluate Measure"))
        self.assertEqual(force_bytes(inst.parameter[0].max), force_bytes("1"))
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(
            force_bytes(inst.parameter[0].name), force_bytes("periodStart")
        )
        self.assertEqual(force_bytes(inst.parameter[0].type), force_bytes("date"))
        self.assertEqual(force_bytes(inst.parameter[0].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[1].documentation),
            force_bytes(
                "The end of the measurement period. The period will end at the end of the period implied by the supplied timestamp. E.g. a value of 2014 would set the period end to be 2014-12-31T23:59:59 inclusive"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[1].max), force_bytes("1"))
        self.assertEqual(inst.parameter[1].min, 1)
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("periodEnd"))
        self.assertEqual(force_bytes(inst.parameter[1].type), force_bytes("date"))
        self.assertEqual(force_bytes(inst.parameter[1].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[2].documentation),
            force_bytes(
                "The measure to evaluate. This parameter is only required when the operation is invoked on the resource type, it is not used when invoking the operation on a Measure instance"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[2].max), force_bytes("1"))
        self.assertEqual(inst.parameter[2].min, 0)
        self.assertEqual(force_bytes(inst.parameter[2].name), force_bytes("measure"))
        self.assertEqual(force_bytes(inst.parameter[2].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[2].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[3].documentation),
            force_bytes(
                "The type of measure report, patient, patient-list, or population. If not specified, a default value of patient will be used if the patient parameter is supplied, otherwise, population will be used"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[3].max), force_bytes("1"))
        self.assertEqual(inst.parameter[3].min, 0)
        self.assertEqual(force_bytes(inst.parameter[3].name), force_bytes("reportType"))
        self.assertEqual(force_bytes(inst.parameter[3].type), force_bytes("code"))
        self.assertEqual(force_bytes(inst.parameter[3].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[4].documentation),
            force_bytes(
                "Patient to evaluate against. If not specified, the measure will be evaluated for all patients that meet the requirements of the measure. If specified, only the referenced patient will be evaluated"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[4].max), force_bytes("1"))
        self.assertEqual(inst.parameter[4].min, 0)
        self.assertEqual(force_bytes(inst.parameter[4].name), force_bytes("patient"))
        self.assertEqual(force_bytes(inst.parameter[4].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[4].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[5].documentation),
            force_bytes(
                "Practitioner to evaluate. If specified, the measure will be evaluated only for patients whose primary practitioner is the identified practitioner"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[5].max), force_bytes("1"))
        self.assertEqual(inst.parameter[5].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[5].name), force_bytes("practitioner")
        )
        self.assertEqual(force_bytes(inst.parameter[5].type), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.parameter[5].use), force_bytes("in"))
        self.assertEqual(force_bytes(inst.parameter[6].max), force_bytes("1"))
        self.assertEqual(inst.parameter[6].min, 0)
        self.assertEqual(
            force_bytes(inst.parameter[6].name), force_bytes("lastReceivedOn")
        )
        self.assertEqual(force_bytes(inst.parameter[6].type), force_bytes("dateTime"))
        self.assertEqual(force_bytes(inst.parameter[6].use), force_bytes("in"))
        self.assertEqual(
            force_bytes(inst.parameter[7].documentation),
            force_bytes(
                "The results of the measure calculation. See the MeasureReport resource for a complete description of the output of this operation"
            ),
        )
        self.assertEqual(force_bytes(inst.parameter[7].max), force_bytes("1"))
        self.assertEqual(inst.parameter[7].min, 1)
        self.assertEqual(force_bytes(inst.parameter[7].name), force_bytes("return"))
        self.assertEqual(
            force_bytes(inst.parameter[7].type), force_bytes("MeasureReport")
        )
        self.assertEqual(force_bytes(inst.parameter[7].use), force_bytes("out"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.resource[0]), force_bytes("Measure"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertFalse(inst.system)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertTrue(inst.type)
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/OperationDefinition/Measure-evaluate-measure"
            ),
        )
