#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import paymentreconciliation
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class PaymentReconciliationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PaymentReconciliation", js["resourceType"])
        return paymentreconciliation.PaymentReconciliation(js)
    
    def testPaymentReconciliation1(self):
        inst = self.instantiate_from("paymentreconciliation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PaymentReconciliation instance")
        self.implPaymentReconciliation1(inst)
        
        js = inst.as_json()
        self.assertEqual("PaymentReconciliation", js["resourceType"])
        inst2 = paymentreconciliation.PaymentReconciliation(js)
        self.implPaymentReconciliation1(inst2)
    
    def implPaymentReconciliation1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.detail[0].amount.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.detail[0].amount.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.detail[0].amount.value, 1000.0)
        self.assertEqual(inst.detail[0].date.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.detail[0].date.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.detail[0].type.coding[0].code), force_bytes("payment"))
        self.assertEqual(force_bytes(inst.detail[0].type.coding[0].system), force_bytes("http://hl7.org/fhir/payment-type"))
        self.assertEqual(force_bytes(inst.detail[1].amount.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.detail[1].amount.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.detail[1].amount.value, 4000.0)
        self.assertEqual(inst.detail[1].date.date, FHIRDate("2014-08-12").date)
        self.assertEqual(inst.detail[1].date.as_json(), "2014-08-12")
        self.assertEqual(force_bytes(inst.detail[1].type.coding[0].code), force_bytes("payment"))
        self.assertEqual(force_bytes(inst.detail[1].type.coding[0].system), force_bytes("http://hl7.org/fhir/payment-type"))
        self.assertEqual(force_bytes(inst.detail[2].amount.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.detail[2].amount.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.detail[2].amount.value, -1500.0)
        self.assertEqual(inst.detail[2].date.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.detail[2].date.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.detail[2].type.coding[0].code), force_bytes("advance"))
        self.assertEqual(force_bytes(inst.detail[2].type.coding[0].system), force_bytes("http://hl7.org/fhir/payment-type"))
        self.assertEqual(force_bytes(inst.disposition), force_bytes("2014 August mid-month settlement."))
        self.assertEqual(force_bytes(inst.form.coding[0].code), force_bytes("PAYREC/2016/01B"))
        self.assertEqual(force_bytes(inst.form.coding[0].system), force_bytes("http://ncforms.org/formid"))
        self.assertEqual(force_bytes(inst.id), force_bytes("ER2500"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/enrollmentresponse"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("781234"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/remittance-outcome"))
        self.assertEqual(inst.period.end.date, FHIRDate("2014-08-31").date)
        self.assertEqual(inst.period.end.as_json(), "2014-08-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.period.start.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.processNote[0].text), force_bytes("Due to the year end holiday the cutoff for submissions for December will be the 28th."))
        self.assertEqual(force_bytes(inst.processNote[0].type.coding[0].code), force_bytes("display"))
        self.assertEqual(force_bytes(inst.processNote[0].type.coding[0].system), force_bytes("http://hl7.org/fhir/note-type"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the PaymentReconciliation</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.total.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.total.value, 3500.0)

