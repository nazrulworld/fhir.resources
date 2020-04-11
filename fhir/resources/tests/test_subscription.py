# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Subscription
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

from .. import subscription
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class SubscriptionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Subscription", js["resourceType"])
        return subscription.Subscription(js)

    def testSubscription1(self):
        inst = self.instantiate_from("subscription-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a Subscription instance")
        self.implSubscription1(inst)

        js = inst.as_json()
        self.assertEqual("Subscription", js["resourceType"])
        inst2 = subscription.Subscription(js)
        self.implSubscription1(inst2)

    def implSubscription1(self, inst):
        self.assertEqual(
            force_bytes(inst.channel.endpoint),
            force_bytes("https://biliwatch.com/customers/mount-auburn-miu/on-result"),
        )
        self.assertEqual(
            force_bytes(inst.channel.header[0]),
            force_bytes("Authorization: Bearer secret-token-abc-123"),
        )
        self.assertEqual(
            force_bytes(inst.channel.payload), force_bytes("application/fhir+json")
        )
        self.assertEqual(force_bytes(inst.channel.type), force_bytes("rest-hook"))
        self.assertEqual(force_bytes(inst.contact[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].value), force_bytes("ext 4123"))
        self.assertEqual(
            force_bytes(inst.criteria),
            force_bytes("Observation?code=http://loinc.org|1975-2"),
        )
        self.assertEqual(inst.end.date, FHIRDate("2021-01-01T00:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2021-01-01T00:00:00Z")
        self.assertEqual(
            force_bytes(inst.error),
            force_bytes("Socket Error 10060 - can't connect to host"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-error"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.reason), force_bytes("Monitor new neonatal function")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("error"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testSubscription2(self):
        inst = self.instantiate_from("subscription-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Subscription instance")
        self.implSubscription2(inst)

        js = inst.as_json()
        self.assertEqual("Subscription", js["resourceType"])
        inst2 = subscription.Subscription(js)
        self.implSubscription2(inst2)

    def implSubscription2(self, inst):
        self.assertEqual(
            force_bytes(inst.channel.endpoint),
            force_bytes("https://biliwatch.com/customers/mount-auburn-miu/on-result"),
        )
        self.assertEqual(
            force_bytes(inst.channel.header[0]),
            force_bytes("Authorization: Bearer secret-token-abc-123"),
        )
        self.assertEqual(
            force_bytes(inst.channel.payload), force_bytes("application/fhir+json")
        )
        self.assertEqual(force_bytes(inst.channel.type), force_bytes("rest-hook"))
        self.assertEqual(force_bytes(inst.contact[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].value), force_bytes("ext 4123"))
        self.assertEqual(
            force_bytes(inst.criteria),
            force_bytes("Observation?code=http://loinc.org|1975-2"),
        )
        self.assertEqual(inst.end.date, FHIRDate("2021-01-01T00:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2021-01-01T00:00:00Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.reason), force_bytes("Monitor new neonatal function")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("requested"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
