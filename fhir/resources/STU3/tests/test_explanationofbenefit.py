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
from .. import explanationofbenefit
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ExplanationOfBenefitTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        return explanationofbenefit.ExplanationOfBenefit(js)
    
    def testExplanationOfBenefit1(self):
        inst = self.instantiate_from("explanationofbenefit-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ExplanationOfBenefit instance")
        self.implExplanationOfBenefit1(inst)
        
        js = inst.as_json()
        self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        inst2 = explanationofbenefit.ExplanationOfBenefit(js)
        self.implExplanationOfBenefit1(inst2)
    
    def implExplanationOfBenefit1(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.disposition), force_bytes("Claim settled as per contract."))
        self.assertEqual(force_bytes(inst.id), force_bytes("EB3500"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/explanationofbenefit"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("987654321"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[0].amount.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[0].amount.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 120.0)
        self.assertEqual(force_bytes(inst.item[0].adjudication[0].category.coding[0].code), force_bytes("eligible"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[1].category.coding[0].code), force_bytes("eligpercent"))
        self.assertEqual(inst.item[0].adjudication[1].value, 0.8)
        self.assertEqual(force_bytes(inst.item[0].adjudication[2].amount.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.item[0].adjudication[2].amount.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.item[0].adjudication[2].amount.value, 96.0)
        self.assertEqual(force_bytes(inst.item[0].adjudication[2].category.coding[0].code), force_bytes("benefit"))
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(force_bytes(inst.item[0].service.coding[0].code), force_bytes("1200"))
        self.assertEqual(force_bytes(inst.item[0].service.coding[0].system), force_bytes("http://hl7.org/fhir/service-uscls"))
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.item[0].unitPrice.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/remittance-outcome"))
        self.assertEqual(force_bytes(inst.payee.type.coding[0].code), force_bytes("provider"))
        self.assertEqual(force_bytes(inst.payee.type.coding[0].system), force_bytes("http://hl7.org/fhir/payeetype"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ExplanationOfBenefit</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.totalBenefit.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.totalBenefit.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.totalBenefit.value, 96.0)
        self.assertEqual(force_bytes(inst.totalCost.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.totalCost.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.totalCost.value, 135.57)
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://hl7.org/fhir/ex-claimtype"))

