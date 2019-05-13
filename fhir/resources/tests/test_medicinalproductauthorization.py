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
from .. import medicinalproductauthorization
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MedicinalProductAuthorizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductAuthorization", js["resourceType"])
        return medicinalproductauthorization.MedicinalProductAuthorization(js)
    
    def testMedicinalProductAuthorization1(self):
        inst = self.instantiate_from("medicinalproductauthorization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductAuthorization instance")
        self.implMedicinalProductAuthorization1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductAuthorization", js["resourceType"])
        inst2 = medicinalproductauthorization.MedicinalProductAuthorization(js)
        self.implMedicinalProductAuthorization1(inst2)
    
    def implMedicinalProductAuthorization1(self, inst):
        self.assertEqual(force_bytes(inst.country[0].coding[0].code), force_bytes("EU"))
        self.assertEqual(force_bytes(inst.country[0].coding[0].system), force_bytes("http://ema.europa.eu/example/country"))
        self.assertEqual(inst.dataExclusivityPeriod.end.date, FHIRDate("2020-08-15").date)
        self.assertEqual(inst.dataExclusivityPeriod.end.as_json(), "2020-08-15")
        self.assertEqual(inst.dataExclusivityPeriod.start.date, FHIRDate("2010-08-15").date)
        self.assertEqual(inst.dataExclusivityPeriod.start.as_json(), "2010-08-15")
        self.assertEqual(inst.dateOfFirstAuthorization.date, FHIRDate("2010-08-15").date)
        self.assertEqual(inst.dateOfFirstAuthorization.as_json(), "2010-08-15")
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://ema.europa.eu/example/marketingAuthorisationNumber"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("EU/1/11/999/001"))
        self.assertEqual(inst.internationalBirthDate.date, FHIRDate("2010-08-15").date)
        self.assertEqual(inst.internationalBirthDate.as_json(), "2010-08-15")
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[0].country.coding[0].code), force_bytes("NO"))
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[0].country.coding[0].system), force_bytes("http://ema.europa.eu/example/countryCode"))
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[0].id), force_bytes("1"))
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[0].identifier[0].system), force_bytes("http://ema.europa.eu/example/marketingauthorisationnumber"))
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[0].identifier[0].value), force_bytes("123-456-789"))
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[1].country.coding[0].code), force_bytes("NO"))
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[1].country.coding[0].system), force_bytes("http://ema.europa.eu/example/countryCode"))
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[1].id), force_bytes("2"))
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[1].identifier[0].system), force_bytes("http://ema.europa.eu/example/marketingauthorisationnumber"))
        self.assertEqual(force_bytes(inst.jurisdictionalAuthorization[1].identifier[0].value), force_bytes("123-456-123"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.procedure.application[0].dateDateTime.date, FHIRDate("2015-08-01").date)
        self.assertEqual(inst.procedure.application[0].dateDateTime.as_json(), "2015-08-01")
        self.assertEqual(force_bytes(inst.procedure.application[0].identifier.system), force_bytes("http://ema.europa.eu/example/applicationidentifier-number"))
        self.assertEqual(force_bytes(inst.procedure.application[0].identifier.value), force_bytes("IA38G"))
        self.assertEqual(force_bytes(inst.procedure.application[0].type.coding[0].code), force_bytes("GroupTypeIAVariationNotification"))
        self.assertEqual(force_bytes(inst.procedure.application[0].type.coding[0].system), force_bytes("http://ema.europa.eu/example/marketingAuthorisationApplicationType"))
        self.assertEqual(inst.procedure.datePeriod.end.date, FHIRDate("2015-08-21").date)
        self.assertEqual(inst.procedure.datePeriod.end.as_json(), "2015-08-21")
        self.assertEqual(inst.procedure.datePeriod.start.date, FHIRDate("2015-08-02").date)
        self.assertEqual(inst.procedure.datePeriod.start.as_json(), "2015-08-02")
        self.assertEqual(force_bytes(inst.procedure.identifier.system), force_bytes("http://ema.europa.eu/example/procedureidentifier-number"))
        self.assertEqual(force_bytes(inst.procedure.identifier.value), force_bytes("EMEA/H/C/009999/IA/0099/G"))
        self.assertEqual(force_bytes(inst.procedure.type.coding[0].code), force_bytes("VariationTypeIA"))
        self.assertEqual(force_bytes(inst.procedure.type.coding[0].system), force_bytes("http://ema.europa.eu/example/marketingAuthorisationProcedureType"))
        self.assertEqual(force_bytes(inst.status.coding[0].code), force_bytes("active"))
        self.assertEqual(force_bytes(inst.status.coding[0].system), force_bytes("http://ema.europa.eu/example/authorisationstatus"))
        self.assertEqual(inst.statusDate.date, FHIRDate("2015-01-14").date)
        self.assertEqual(inst.statusDate.as_json(), "2015-01-14")
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(inst.validityPeriod.end.date, FHIRDate("2020-05-20").date)
        self.assertEqual(inst.validityPeriod.end.as_json(), "2020-05-20")
        self.assertEqual(inst.validityPeriod.start.date, FHIRDate("2015-08-16").date)
        self.assertEqual(inst.validityPeriod.start.as_json(), "2015-08-16")

