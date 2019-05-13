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
from .. import claimresponse
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ClaimResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ClaimResponse", js["resourceType"])
        return claimresponse.ClaimResponse(js)
    
    def testClaimResponse1(self):
        inst = self.instantiate_from("claimresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse1(inst2)
    
    def implClaimResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.disposition), force_bytes("Claim settled as per contract."))
        self.assertEqual(force_bytes(inst.id), force_bytes("R3500"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/remittance"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("R3500"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[0].amount.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[0].amount.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 135.57)
        self.assertEqual(force_bytes(inst.item[0].adjudication[0].category.coding[0].code), force_bytes("eligible"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[1].amount.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[1].amount.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.item[0].adjudication[1].amount.value, 10.0)
        self.assertEqual(force_bytes(inst.item[0].adjudication[1].category.coding[0].code), force_bytes("copay"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[2].category.coding[0].code), force_bytes("eligpercent"))
        self.assertEqual(inst.item[0].adjudication[2].value, 80.0)
        self.assertEqual(force_bytes(inst.item[0].adjudication[3].amount.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[3].amount.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.item[0].adjudication[3].amount.value, 100.47)
        self.assertEqual(force_bytes(inst.item[0].adjudication[3].category.coding[0].code), force_bytes("benefit"))
        self.assertEqual(inst.item[0].sequenceLinkId, 1)
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/remittance-outcome"))
        self.assertEqual(force_bytes(inst.payeeType.coding[0].code), force_bytes("provider"))
        self.assertEqual(force_bytes(inst.payeeType.coding[0].system), force_bytes("http://hl7.org/fhir/payeetype"))
        self.assertEqual(force_bytes(inst.payment.amount.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.payment.amount.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.payment.amount.value, 100.47)
        self.assertEqual(inst.payment.date.date, FHIRDate("2014-08-31").date)
        self.assertEqual(inst.payment.date.as_json(), "2014-08-31")
        self.assertEqual(force_bytes(inst.payment.identifier.system), force_bytes("http://www.BenefitsInc.com/fhir/paymentidentifier"))
        self.assertEqual(force_bytes(inst.payment.identifier.value), force_bytes("201408-2-1569478"))
        self.assertEqual(force_bytes(inst.payment.type.coding[0].code), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.payment.type.coding[0].system), force_bytes("http://hl7.org/fhir/ex-paymenttype"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ClaimResponse</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.totalBenefit.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.totalBenefit.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.totalBenefit.value, 100.47)
        self.assertEqual(force_bytes(inst.totalCost.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.totalCost.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.totalCost.value, 135.57)

