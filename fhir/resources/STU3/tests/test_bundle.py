# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
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

from .. import bundle
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class BundleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Bundle", js["resourceType"])
        return bundle.Bundle(js)

    def testBundle1(self):
        inst = self.instantiate_from("message-response-link.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle1(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle1(inst2)

    def implBundle1(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes("urn:uuid:d9d296d8-5afd-42e1-a0ce-3344e0e003ed"),
        )
        self.assertEqual(
            force_bytes(inst.entry[0].resource.id),
            force_bytes("caf609cf-c3a7-4be3-a3aa-356b9bb69d4f"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("urn:uuid:03f9aa7d-b395-47b9-84e0-053678b6e4e3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].resource.id),
            force_bytes("03f9aa7d-b395-47b9-84e0-053678b6e4e3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://acme.com/ehr/fhir/Patient/pat1"),
        )
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("pat1"))
        self.assertEqual(
            force_bytes(inst.entry[3].fullUrl),
            force_bytes("http://acme.com/ehr/fhir/Patient/pat12"),
        )
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("pat2"))
        self.assertEqual(
            force_bytes(inst.id), force_bytes("3a0707d3-549e-4467-b8b8-5a2ab3800efe")
        )
        self.assertEqual(force_bytes(inst.type), force_bytes("message"))

    def testBundle2(self):
        inst = self.instantiate_from("xds-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle2(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle2(inst2)

    def implBundle2(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes("urn:uuid:3fdc72f4-a11d-4a9d-9260-a9f745779e1d"),
        )
        self.assertEqual(force_bytes(inst.entry[0].request.method), force_bytes("POST"))
        self.assertEqual(
            force_bytes(inst.entry[0].request.url), force_bytes("DocumentReference")
        )
        self.assertEqual(
            inst.entry[0].resource.meta.lastUpdated.date,
            FHIRDate("2013-07-01T13:11:33Z").date,
        )
        self.assertEqual(
            inst.entry[0].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("http://localhost:9556/svc/fhir/Patient/a2"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].request.ifNoneExist),
            force_bytes("Patient?identifier=http://acme.org/xds/patients!89765a87b"),
        )
        self.assertEqual(force_bytes(inst.entry[1].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[1].request.url), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("a2"))
        self.assertEqual(
            inst.entry[1].resource.meta.lastUpdated.date,
            FHIRDate("2013-07-01T13:11:33Z").date,
        )
        self.assertEqual(
            inst.entry[1].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://localhost:9556/svc/fhir/Practitioner/a3"),
        )
        self.assertEqual(force_bytes(inst.entry[2].request.method), force_bytes("POST"))
        self.assertEqual(
            force_bytes(inst.entry[2].request.url), force_bytes("Practitioner")
        )
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("a3"))
        self.assertEqual(
            inst.entry[2].resource.meta.lastUpdated.date,
            FHIRDate("2013-07-01T13:11:33Z").date,
        )
        self.assertEqual(
            inst.entry[2].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[3].fullUrl),
            force_bytes("http://localhost:9556/svc/fhir/Practitioner/a4"),
        )
        self.assertEqual(force_bytes(inst.entry[3].request.method), force_bytes("POST"))
        self.assertEqual(
            force_bytes(inst.entry[3].request.url), force_bytes("Practitioner")
        )
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("a4"))
        self.assertEqual(
            inst.entry[3].resource.meta.lastUpdated.date,
            FHIRDate("2013-07-01T13:11:33Z").date,
        )
        self.assertEqual(
            inst.entry[3].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[4].fullUrl),
            force_bytes(
                "http://localhost:9556/svc/fhir/Binary/1e404af3-077f-4bee-b7a6-a9be97e1ce32"
            ),
        )
        self.assertEqual(force_bytes(inst.entry[4].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[4].request.url), force_bytes("Binary"))
        self.assertEqual(
            force_bytes(inst.entry[4].resource.id),
            force_bytes("1e404af3-077f-4bee-b7a6-a9be97e1ce32"),
        )
        self.assertEqual(
            inst.entry[4].resource.meta.lastUpdated.date,
            FHIRDate("2013-07-01T13:11:33Z").date,
        )
        self.assertEqual(
            inst.entry[4].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z"
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("xds"))
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date
        )
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(force_bytes(inst.type), force_bytes("transaction"))

    def testBundle3(self):
        inst = self.instantiate_from("search-parameters.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle3(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle3(inst2)

    def implBundle3(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/DomainResource-text"),
        )
        self.assertEqual(
            force_bytes(inst.entry[0].resource.id), force_bytes("DomainResource-text")
        )
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-content"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].resource.id), force_bytes("Resource-content")
        )
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-id"),
        )
        self.assertEqual(
            force_bytes(inst.entry[2].resource.id), force_bytes("Resource-id")
        )
        self.assertEqual(
            force_bytes(inst.entry[3].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-lastUpdated"),
        )
        self.assertEqual(
            force_bytes(inst.entry[3].resource.id), force_bytes("Resource-lastUpdated")
        )
        self.assertEqual(
            force_bytes(inst.entry[4].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-profile"),
        )
        self.assertEqual(
            force_bytes(inst.entry[4].resource.id), force_bytes("Resource-profile")
        )
        self.assertEqual(
            force_bytes(inst.entry[5].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-query"),
        )
        self.assertEqual(
            force_bytes(inst.entry[5].resource.id), force_bytes("Resource-query")
        )
        self.assertEqual(
            force_bytes(inst.entry[6].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-security"),
        )
        self.assertEqual(
            force_bytes(inst.entry[6].resource.id), force_bytes("Resource-security")
        )
        self.assertEqual(
            force_bytes(inst.entry[7].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/Resource-tag"),
        )
        self.assertEqual(
            force_bytes(inst.entry[7].resource.id), force_bytes("Resource-tag")
        )
        self.assertEqual(
            force_bytes(inst.entry[8].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-balance"),
        )
        self.assertEqual(
            force_bytes(inst.entry[8].resource.id), force_bytes("Account-balance")
        )
        self.assertEqual(
            force_bytes(inst.entry[9].fullUrl),
            force_bytes("http://hl7.org/fhir/SearchParameter/Account-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.entry[9].resource.id), force_bytes("Account-identifier")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("searchParams"))
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))

    def testBundle4(self):
        inst = self.instantiate_from("message-request-link.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle4(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle4(inst2)

    def implBundle4(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes("urn:uuid:267b18ce-3d37-4581-9baa-6fada338038b"),
        )
        self.assertEqual(
            force_bytes(inst.entry[0].resource.id),
            force_bytes("efdd254b-0e09-4164-883e-35cf3871715f"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("http://acme.com/ehr/fhir/Patient/pat1"),
        )
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("pat1"))
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://acme.com/ehr/fhir/Patient/pat12"),
        )
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("pat2"))
        self.assertEqual(
            force_bytes(inst.id), force_bytes("10bb101f-a121-4264-a920-67be9cb82c74")
        )
        self.assertEqual(force_bytes(inst.type), force_bytes("message"))

    def testBundle5(self):
        inst = self.instantiate_from("namingsystem-terminologies.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle5(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle5(inst2)

    def implBundle5(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-sct"),
        )
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("tx-sct"))
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-rxnorm"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].resource.id), force_bytes("tx-rxnorm")
        )
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-loinc"),
        )
        self.assertEqual(
            force_bytes(inst.entry[2].resource.id), force_bytes("tx-loinc")
        )
        self.assertEqual(
            force_bytes(inst.entry[3].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-ucum"),
        )
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("tx-ucum"))
        self.assertEqual(
            force_bytes(inst.entry[4].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-nci"),
        )
        self.assertEqual(force_bytes(inst.entry[4].resource.id), force_bytes("tx-nci"))
        self.assertEqual(
            force_bytes(inst.entry[5].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-cpt"),
        )
        self.assertEqual(force_bytes(inst.entry[5].resource.id), force_bytes("tx-cpt"))
        self.assertEqual(
            force_bytes(inst.entry[6].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-ndf-rt"),
        )
        self.assertEqual(
            force_bytes(inst.entry[6].resource.id), force_bytes("tx-ndf-rt")
        )
        self.assertEqual(
            force_bytes(inst.entry[7].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-unii"),
        )
        self.assertEqual(force_bytes(inst.entry[7].resource.id), force_bytes("tx-unii"))
        self.assertEqual(
            force_bytes(inst.entry[8].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-ndc"),
        )
        self.assertEqual(force_bytes(inst.entry[8].resource.id), force_bytes("tx-ndc"))
        self.assertEqual(
            force_bytes(inst.entry[9].fullUrl),
            force_bytes("http://hl7.org/fhir/NamingSystem/tx-cvx"),
        )
        self.assertEqual(force_bytes(inst.entry[9].resource.id), force_bytes("tx-cvx"))
        self.assertEqual(force_bytes(inst.id), force_bytes("terminologies"))
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))

    def testBundle6(self):
        inst = self.instantiate_from("extension-definitions.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle6(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle6(inst2)

    def implBundle6(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/valueset-history"),
        )
        self.assertEqual(
            force_bytes(inst.entry[0].resource.id), force_bytes("valueset-history")
        )
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/birthPlace"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].resource.id), force_bytes("birthPlace")
        )
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/valueset-map"),
        )
        self.assertEqual(
            force_bytes(inst.entry[2].resource.id), force_bytes("valueset-map")
        )
        self.assertEqual(
            force_bytes(inst.entry[3].fullUrl),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/observation-time-offset"
            ),
        )
        self.assertEqual(
            force_bytes(inst.entry[3].resource.id),
            force_bytes("observation-time-offset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[4].fullUrl),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/observation-geneticsInterpretation"
            ),
        )
        self.assertEqual(
            force_bytes(inst.entry[4].resource.id),
            force_bytes("observation-geneticsInterpretation"),
        )
        self.assertEqual(
            force_bytes(inst.entry[5].fullUrl),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/11179-de-administrative-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.entry[5].resource.id),
            force_bytes("11179-de-administrative-status"),
        )
        self.assertEqual(
            force_bytes(inst.entry[6].fullUrl),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/patient-cadavericDonor"
            ),
        )
        self.assertEqual(
            force_bytes(inst.entry[6].resource.id),
            force_bytes("patient-cadavericDonor"),
        )
        self.assertEqual(
            force_bytes(inst.entry[7].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/openEHR-management"),
        )
        self.assertEqual(
            force_bytes(inst.entry[7].resource.id), force_bytes("openEHR-management")
        )
        self.assertEqual(
            force_bytes(inst.entry[8].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/valueset-definition"),
        )
        self.assertEqual(
            force_bytes(inst.entry[8].resource.id), force_bytes("valueset-definition")
        )
        self.assertEqual(
            force_bytes(inst.entry[9].fullUrl),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/procedurerequest-reasonRejected"
            ),
        )
        self.assertEqual(
            force_bytes(inst.entry[9].resource.id),
            force_bytes("procedurerequest-reasonRejected"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("extensions"))
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))

    def testBundle7(self):
        inst = self.instantiate_from("conceptmaps.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle7(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle7(inst2)

    def implBundle7(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes(
                "http://hl7.org/fhir/ConceptMap/cm-observation-relationshiptypes-v3"
            ),
        )
        self.assertEqual(
            force_bytes(inst.entry[0].resource.id),
            force_bytes("cm-observation-relationshiptypes-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-address-use-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].resource.id), force_bytes("cm-address-use-v3")
        )
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[2].resource.id),
            force_bytes("cm-contact-point-use-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[3].fullUrl),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v2"),
        )
        self.assertEqual(
            force_bytes(inst.entry[3].resource.id),
            force_bytes("cm-contact-point-use-v2"),
        )
        self.assertEqual(
            force_bytes(inst.entry[4].fullUrl),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-administrative-gender-v2"),
        )
        self.assertEqual(
            force_bytes(inst.entry[4].resource.id),
            force_bytes("cm-administrative-gender-v2"),
        )
        self.assertEqual(
            force_bytes(inst.entry[5].fullUrl),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-address-type-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[5].resource.id), force_bytes("cm-address-type-v3")
        )
        self.assertEqual(
            force_bytes(inst.entry[6].fullUrl),
            force_bytes(
                "http://hl7.org/fhir/ConceptMap/cm-medication-request-status-v3"
            ),
        )
        self.assertEqual(
            force_bytes(inst.entry[6].resource.id),
            force_bytes("cm-medication-request-status-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[7].fullUrl),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-administrative-gender-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[7].resource.id),
            force_bytes("cm-administrative-gender-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[8].fullUrl),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-data-absent-reason-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[8].resource.id),
            force_bytes("cm-data-absent-reason-v3"),
        )
        self.assertEqual(
            force_bytes(inst.entry[9].fullUrl),
            force_bytes("http://hl7.org/fhir/ConceptMap/cm-name-use-v2"),
        )
        self.assertEqual(
            force_bytes(inst.entry[9].resource.id), force_bytes("cm-name-use-v2")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("conceptmaps"))
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))

    def offtestBundle8(self):
        inst = self.instantiate_from("profiles-types.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle8(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle8(inst2)

    def implBundle8(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/Element"),
        )
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("Element"))
        self.assertEqual(
            inst.entry[0].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[0].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/BackboneElement"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].resource.id), force_bytes("BackboneElement")
        )
        self.assertEqual(
            inst.entry[1].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[1].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/base64Binary"),
        )
        self.assertEqual(
            force_bytes(inst.entry[2].resource.id), force_bytes("base64Binary")
        )
        self.assertEqual(
            inst.entry[2].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[2].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[3].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/boolean"),
        )
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("boolean"))
        self.assertEqual(
            inst.entry[3].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[3].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[4].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/code"),
        )
        self.assertEqual(force_bytes(inst.entry[4].resource.id), force_bytes("code"))
        self.assertEqual(
            inst.entry[4].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[4].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[5].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/date"),
        )
        self.assertEqual(force_bytes(inst.entry[5].resource.id), force_bytes("date"))
        self.assertEqual(
            inst.entry[5].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[5].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[6].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/dateTime"),
        )
        self.assertEqual(
            force_bytes(inst.entry[6].resource.id), force_bytes("dateTime")
        )
        self.assertEqual(
            inst.entry[6].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[6].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[7].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/decimal"),
        )
        self.assertEqual(force_bytes(inst.entry[7].resource.id), force_bytes("decimal"))
        self.assertEqual(
            inst.entry[7].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[7].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[8].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/id"),
        )
        self.assertEqual(force_bytes(inst.entry[8].resource.id), force_bytes("id"))
        self.assertEqual(
            inst.entry[8].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[8].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[9].fullUrl),
            force_bytes("http://hl7.org/fhir/StructureDefinition/instant"),
        )
        self.assertEqual(force_bytes(inst.entry[9].resource.id), force_bytes("instant"))
        self.assertEqual(
            inst.entry[9].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[9].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("types"))
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))

    def testBundle9(self):
        inst = self.instantiate_from("v3-codesystems.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle9(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle9(inst2)

    def implBundle9(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes("http://hl7.org/fhir/ValueSet/v3-CalendarType"),
        )
        self.assertEqual(
            force_bytes(inst.entry[0].resource.id), force_bytes("v3-CalendarType")
        )
        self.assertEqual(
            inst.entry[0].resource.meta.lastUpdated.date,
            FHIRDate("2016-11-11T00:00:00.000+11:00").date,
        )
        self.assertEqual(
            inst.entry[0].resource.meta.lastUpdated.as_json(),
            "2016-11-11T00:00:00.000+11:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[0].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("http://hl7.org/fhir/ValueSet/v3-ManagedParticipationStatus"),
        )
        self.assertEqual(
            force_bytes(inst.entry[1].resource.id),
            force_bytes("v3-ManagedParticipationStatus"),
        )
        self.assertEqual(
            inst.entry[1].resource.meta.lastUpdated.date,
            FHIRDate("2016-11-11T00:00:00.000+11:00").date,
        )
        self.assertEqual(
            inst.entry[1].resource.meta.lastUpdated.as_json(),
            "2016-11-11T00:00:00.000+11:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[1].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://hl7.org/fhir/ValueSet/v3-ActConsentDirective"),
        )
        self.assertEqual(
            force_bytes(inst.entry[2].resource.id),
            force_bytes("v3-ActConsentDirective"),
        )
        self.assertEqual(
            inst.entry[2].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[2].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[2].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[3].fullUrl),
            force_bytes("http://hl7.org/fhir/ValueSet/v3-InformationSensitivityPolicy"),
        )
        self.assertEqual(
            force_bytes(inst.entry[3].resource.id),
            force_bytes("v3-InformationSensitivityPolicy"),
        )
        self.assertEqual(
            inst.entry[3].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[3].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[3].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[4].fullUrl),
            force_bytes("http://hl7.org/fhir/ValueSet/v3-RoleClass"),
        )
        self.assertEqual(
            force_bytes(inst.entry[4].resource.id), force_bytes("v3-RoleClass")
        )
        self.assertEqual(
            inst.entry[4].resource.meta.lastUpdated.date,
            FHIRDate("2016-11-11T00:00:00.000+11:00").date,
        )
        self.assertEqual(
            inst.entry[4].resource.meta.lastUpdated.as_json(),
            "2016-11-11T00:00:00.000+11:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[4].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[5].fullUrl),
            force_bytes(
                "http://hl7.org/fhir/ValueSet/v3-ConfidentialityClassification"
            ),
        )
        self.assertEqual(
            force_bytes(inst.entry[5].resource.id),
            force_bytes("v3-ConfidentialityClassification"),
        )
        self.assertEqual(
            inst.entry[5].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[5].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[5].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[6].fullUrl),
            force_bytes(
                "http://hl7.org/fhir/ValueSet/v3-ServiceDeliveryLocationRoleType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.entry[6].resource.id),
            force_bytes("v3-ServiceDeliveryLocationRoleType"),
        )
        self.assertEqual(
            inst.entry[6].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[6].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[6].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[7].fullUrl),
            force_bytes("http://hl7.org/fhir/ValueSet/v3-QueryResponse"),
        )
        self.assertEqual(
            force_bytes(inst.entry[7].resource.id), force_bytes("v3-QueryResponse")
        )
        self.assertEqual(
            inst.entry[7].resource.meta.lastUpdated.date,
            FHIRDate("2016-11-11T00:00:00.000+11:00").date,
        )
        self.assertEqual(
            inst.entry[7].resource.meta.lastUpdated.as_json(),
            "2016-11-11T00:00:00.000+11:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[7].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[8].fullUrl),
            force_bytes("http://hl7.org/fhir/ValueSet/v3-SecurityPolicy"),
        )
        self.assertEqual(
            force_bytes(inst.entry[8].resource.id), force_bytes("v3-SecurityPolicy")
        )
        self.assertEqual(
            inst.entry[8].resource.meta.lastUpdated.date,
            FHIRDate("2017-04-19T07:44:43.294+10:00").date,
        )
        self.assertEqual(
            inst.entry[8].resource.meta.lastUpdated.as_json(),
            "2017-04-19T07:44:43.294+10:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[8].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.entry[9].fullUrl),
            force_bytes("http://hl7.org/fhir/ValueSet/v3-TableCellHorizontalAlign"),
        )
        self.assertEqual(
            force_bytes(inst.entry[9].resource.id),
            force_bytes("v3-TableCellHorizontalAlign"),
        )
        self.assertEqual(
            inst.entry[9].resource.meta.lastUpdated.date,
            FHIRDate("2016-11-11T00:00:00.000+11:00").date,
        )
        self.assertEqual(
            inst.entry[9].resource.meta.lastUpdated.as_json(),
            "2016-11-11T00:00:00.000+11:00",
        )
        self.assertEqual(
            force_bytes(inst.entry[9].resource.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("v3-valuesets"))
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))

    def testBundle10(self):
        inst = self.instantiate_from("practitioner-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle10(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle10(inst2)

    def implBundle10(self, inst):
        self.assertEqual(
            force_bytes(inst.entry[0].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/1"),
        )
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.entry[1].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/13"),
        )
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("13"))
        self.assertEqual(
            inst.entry[1].resource.meta.lastUpdated.date,
            FHIRDate("2012-05-29T23:45:32Z").date,
        )
        self.assertEqual(
            inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[2].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/14"),
        )
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("14"))
        self.assertEqual(
            inst.entry[2].resource.meta.lastUpdated.date,
            FHIRDate("2012-05-29T23:45:32Z").date,
        )
        self.assertEqual(
            inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[3].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/15"),
        )
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("15"))
        self.assertEqual(
            inst.entry[3].resource.meta.lastUpdated.date,
            FHIRDate("2012-05-29T23:45:32Z").date,
        )
        self.assertEqual(
            inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[4].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/16"),
        )
        self.assertEqual(force_bytes(inst.entry[4].resource.id), force_bytes("16"))
        self.assertEqual(
            inst.entry[4].resource.meta.lastUpdated.date,
            FHIRDate("2012-05-29T23:45:32Z").date,
        )
        self.assertEqual(
            inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[5].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/17"),
        )
        self.assertEqual(force_bytes(inst.entry[5].resource.id), force_bytes("17"))
        self.assertEqual(
            inst.entry[5].resource.meta.lastUpdated.date,
            FHIRDate("2012-05-29T23:45:32Z").date,
        )
        self.assertEqual(
            inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[6].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/18"),
        )
        self.assertEqual(force_bytes(inst.entry[6].resource.id), force_bytes("18"))
        self.assertEqual(
            inst.entry[6].resource.meta.lastUpdated.date,
            FHIRDate("2012-05-29T23:45:32Z").date,
        )
        self.assertEqual(
            inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[7].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/19"),
        )
        self.assertEqual(force_bytes(inst.entry[7].resource.id), force_bytes("19"))
        self.assertEqual(
            inst.entry[7].resource.meta.lastUpdated.date,
            FHIRDate("2012-05-29T23:45:32Z").date,
        )
        self.assertEqual(
            inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[8].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/20"),
        )
        self.assertEqual(force_bytes(inst.entry[8].resource.id), force_bytes("20"))
        self.assertEqual(
            inst.entry[8].resource.meta.lastUpdated.date,
            FHIRDate("2012-05-29T23:45:32Z").date,
        )
        self.assertEqual(
            inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z"
        )
        self.assertEqual(
            force_bytes(inst.entry[9].fullUrl),
            force_bytes("http://hl7.org/fhir/Practitioner/21"),
        )
        self.assertEqual(force_bytes(inst.entry[9].resource.id), force_bytes("21"))
        self.assertEqual(
            inst.entry[9].resource.meta.lastUpdated.date,
            FHIRDate("2012-05-29T23:45:32Z").date,
        )
        self.assertEqual(
            inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z"
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("3ad0687e-f477-468c-afd5-fcc2bf897809")
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date
        )
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))
