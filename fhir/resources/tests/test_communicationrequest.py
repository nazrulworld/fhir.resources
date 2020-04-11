# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest
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

from .. import communicationrequest
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class CommunicationRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("CommunicationRequest", js["resourceType"])
        return communicationrequest.CommunicationRequest(js)

    def testCommunicationRequest1(self):
        inst = self.instantiate_from("communicationrequest-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CommunicationRequest instance"
        )
        self.implCommunicationRequest1(inst)

        js = inst.as_json()
        self.assertEqual("CommunicationRequest", js["resourceType"])
        inst2 = communicationrequest.CommunicationRequest(js)
        self.implCommunicationRequest1(inst2)

    def implCommunicationRequest1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">To be filled out at a later time</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCommunicationRequest2(self):
        inst = self.instantiate_from(
            "communicationrequest-example-fm-solicit-attachment.json"
        )
        self.assertIsNotNone(
            inst, "Must have instantiated a CommunicationRequest instance"
        )
        self.implCommunicationRequest2(inst)

        js = inst.as_json()
        self.assertEqual("CommunicationRequest", js["resourceType"])
        inst2 = communicationrequest.CommunicationRequest(js)
        self.implCommunicationRequest2(inst2)

    def implCommunicationRequest2(self, inst):
        self.assertEqual(
            inst.authoredOn.date, FHIRDate("2016-06-10T11:01:10-08:00").date
        )
        self.assertEqual(inst.authoredOn.as_json(), "2016-06-10T11:01:10-08:00")
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code),
            force_bytes("SolicitedAttachmentRequest"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://acme.org/messagetypes"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("provider"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("payor"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("requester"))
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.id), force_bytes("fm-solicit"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.jurisdiction.com/insurer/123456"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("ABC123"))
        self.assertEqual(
            force_bytes(inst.medium[0].coding[0].code), force_bytes("WRITTEN")
        )
        self.assertEqual(
            force_bytes(inst.medium[0].coding[0].display), force_bytes("written")
        )
        self.assertEqual(
            force_bytes(inst.medium[0].coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ParticipationMode"),
        )
        self.assertEqual(force_bytes(inst.medium[0].text), force_bytes("written"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            inst.occurrenceDateTime.date, FHIRDate("2016-06-10T11:01:10-08:00").date
        )
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-06-10T11:01:10-08:00")
        self.assertEqual(
            force_bytes(inst.payload[0].contentString),
            force_bytes(
                "Please provide the accident report and any associated pictures to support your Claim# DEF5647."
            ),
        )
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Request for Accident Report</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
