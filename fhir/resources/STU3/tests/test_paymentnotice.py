# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice
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

from .. import paymentnotice
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class PaymentNoticeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("PaymentNotice", js["resourceType"])
        return paymentnotice.PaymentNotice(js)

    def testPaymentNotice1(self):
        inst = self.instantiate_from("paymentnotice-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PaymentNotice instance")
        self.implPaymentNotice1(inst)

        js = inst.as_json()
        self.assertEqual("PaymentNotice", js["resourceType"])
        inst2 = paymentnotice.PaymentNotice(js)
        self.implPaymentNotice1(inst2)

    def implPaymentNotice1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("77654"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://benefitsinc.com/paymentnotice"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("776543"))
        self.assertEqual(
            force_bytes(inst.paymentStatus.coding[0].code), force_bytes("paid")
        )
        self.assertEqual(
            force_bytes(inst.paymentStatus.coding[0].system),
            force_bytes("http://hl7.org/fhir/paymentstatus"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(inst.statusDate.date, FHIRDate("2014-08-15").date)
        self.assertEqual(inst.statusDate.as_json(), "2014-08-15")
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the PaymentNotice</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
