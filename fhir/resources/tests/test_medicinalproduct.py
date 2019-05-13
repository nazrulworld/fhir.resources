#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import medicinalproduct
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MedicinalProductTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProduct", js["resourceType"])
        return medicinalproduct.MedicinalProduct(js)
    
    def testMedicinalProduct1(self):
        inst = self.instantiate_from("medicinalproduct-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProduct instance")
        self.implMedicinalProduct1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProduct", js["resourceType"])
        inst2 = medicinalproduct.MedicinalProduct(js)
        self.implMedicinalProduct1(inst2)
    
    def implMedicinalProduct1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://ema.europa.eu/example/MPID"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("{mpid}"))
        self.assertEqual(force_bytes(inst.manufacturingBusinessOperation[0].authorisationReferenceNumber.system), force_bytes("http://ema.europa.eu/example/manufacturingAuthorisationReferenceNumber"))
        self.assertEqual(force_bytes(inst.manufacturingBusinessOperation[0].authorisationReferenceNumber.value), force_bytes("1324TZ"))
        self.assertEqual(inst.manufacturingBusinessOperation[0].effectiveDate.date, FHIRDate("2013-03-15").date)
        self.assertEqual(inst.manufacturingBusinessOperation[0].effectiveDate.as_json(), "2013-03-15")
        self.assertEqual(force_bytes(inst.manufacturingBusinessOperation[0].operationType.coding[0].code), force_bytes("Batchrelease"))
        self.assertEqual(force_bytes(inst.manufacturingBusinessOperation[0].operationType.coding[0].system), force_bytes("http://ema.europa.eu/example/manufacturingOperationType"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name[0].countryLanguage[0].country.coding[0].code), force_bytes("EU"))
        self.assertEqual(force_bytes(inst.name[0].countryLanguage[0].country.coding[0].system), force_bytes("http://ema.europa.eu/example/countryCode"))
        self.assertEqual(force_bytes(inst.name[0].countryLanguage[0].jurisdiction.coding[0].code), force_bytes("EU"))
        self.assertEqual(force_bytes(inst.name[0].countryLanguage[0].jurisdiction.coding[0].system), force_bytes("http://ema.europa.eu/example/jurisdictionCode"))
        self.assertEqual(force_bytes(inst.name[0].countryLanguage[0].language.coding[0].code), force_bytes("EN"))
        self.assertEqual(force_bytes(inst.name[0].countryLanguage[0].language.coding[0].system), force_bytes("http://ema.europa.eu/example/languageCode"))
        self.assertEqual(force_bytes(inst.name[0].namePart[0].part), force_bytes("Equilidem"))
        self.assertEqual(force_bytes(inst.name[0].namePart[0].type.code), force_bytes("INV"))
        self.assertEqual(force_bytes(inst.name[0].namePart[1].part), force_bytes("2.5 mg"))
        self.assertEqual(force_bytes(inst.name[0].namePart[1].type.code), force_bytes("STR"))
        self.assertEqual(force_bytes(inst.name[0].namePart[2].part), force_bytes("film-coated tablets"))
        self.assertEqual(force_bytes(inst.name[0].namePart[2].type.code), force_bytes("FRM"))
        self.assertEqual(force_bytes(inst.name[0].productName), force_bytes("Equilidem 2.5 mg film-coated tablets"))
        self.assertEqual(force_bytes(inst.productClassification[0].coding[0].code), force_bytes("WHOAnatomicalTherapeuticChemicalATCClassificationSystem|B01AF02"))
        self.assertEqual(force_bytes(inst.productClassification[0].coding[0].system), force_bytes("http://ema.europa.eu/example/WHOAnatomicalTherapeuticChemicalATCClassificationSystem"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

