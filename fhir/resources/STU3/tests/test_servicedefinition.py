# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ServiceDefinition
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

from .. import servicedefinition
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ServiceDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ServiceDefinition", js["resourceType"])
        return servicedefinition.ServiceDefinition(js)

    def testServiceDefinition1(self):
        inst = self.instantiate_from("servicedefinition-infobutton.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a ServiceDefinition instance"
        )
        self.implServiceDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("ServiceDefinition", js["resourceType"])
        inst2 = servicedefinition.ServiceDefinition(js)
        self.implServiceDefinition1(inst2)

    def implServiceDefinition1(self, inst):
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].mustSupport[0]), force_bytes("gender")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].mustSupport[1]),
            force_bytes("birthDate"),
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[0].type), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[1].type), force_bytes("Condition")
        )
        self.assertEqual(
            force_bytes(inst.dataRequirement[2].type),
            force_bytes("MedicationStatement"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-07-05").date)
        self.assertEqual(inst.date.as_json(), "2016-07-05")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "The InfoButton specification defines a mechanism for retrieving relevant clinical context based a particular set of search criteria.."
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("infobutton"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("infobutton")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("InfoButton Module"))
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("InfoButton Module")
        )
        self.assertEqual(force_bytes(inst.topic[1].text), force_bytes("InfoButton"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testServiceDefinition2(self):
        inst = self.instantiate_from("servicedefinition-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a ServiceDefinition instance"
        )
        self.implServiceDefinition2(inst)

        js = inst.as_json()
        self.assertEqual("ServiceDefinition", js["resourceType"])
        inst2 = servicedefinition.ServiceDefinition(js)
        self.implServiceDefinition2(inst2)

    def implServiceDefinition2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Guideline appropriate ordering is used to assess appropriateness of an order given a patient, a proposed order, and a set of clinical indications."
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("guildeline-appropriate-ordering"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Guideline Appropriate Ordering Module"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text),
            force_bytes("Guideline Appropriate Ordering"),
        )
        self.assertEqual(
            force_bytes(inst.topic[1].text), force_bytes("Appropriate Use Criteria")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))
