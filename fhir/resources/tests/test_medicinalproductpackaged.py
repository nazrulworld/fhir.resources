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
from .. import medicinalproductpackaged
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MedicinalProductPackagedTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductPackaged", js["resourceType"])
        return medicinalproductpackaged.MedicinalProductPackaged(js)
    
    def testMedicinalProductPackaged1(self):
        inst = self.instantiate_from("medicinalproductpackaged-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductPackaged instance")
        self.implMedicinalProductPackaged1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductPackaged", js["resourceType"])
        inst2 = medicinalproductpackaged.MedicinalProductPackaged(js)
        self.implMedicinalProductPackaged1(inst2)
    
    def implMedicinalProductPackaged1(self, inst):
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.period.end.date, FHIRDate("2016-06-06").date)
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.period.end.as_json(), "2016-06-06")
        self.assertEqual(force_bytes(inst.batchIdentifier[0].outerPackaging.system), force_bytes("http://ema.europa.eu/example/baid1"))
        self.assertEqual(force_bytes(inst.batchIdentifier[0].outerPackaging.value), force_bytes("AAF5699"))
        self.assertEqual(force_bytes(inst.description), force_bytes("ALU-PVC/PVDC BLISTERS. CARTONS OF 10 FILM-COATED TABLETS. "))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://ema.europa.eu/example/pcid"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("{PCID}"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.packageItem[0].material[0].coding[0].code), force_bytes("PVC"))
        self.assertEqual(force_bytes(inst.packageItem[0].material[0].coding[0].system), force_bytes("http://ema.europa.eu/example/packageItemContainerMaterial"))
        self.assertEqual(force_bytes(inst.packageItem[0].material[1].coding[0].code), force_bytes("PVDC"))
        self.assertEqual(force_bytes(inst.packageItem[0].material[1].coding[0].system), force_bytes("http://ema.europa.eu/example/packageItemContainerMaterial"))
        self.assertEqual(force_bytes(inst.packageItem[0].material[2].coding[0].code), force_bytes("alu"))
        self.assertEqual(force_bytes(inst.packageItem[0].material[2].coding[0].system), force_bytes("http://ema.europa.eu/example/packageItemContainerMaterial"))
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].material[0].coding[0].code), force_bytes("Paperboard"))
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].material[0].coding[0].system), force_bytes("http://ema.europa.eu/example/packageItemContainerMaterial"))
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].physicalCharacteristics.height.unit), force_bytes("mm"))
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.height.value, 125)
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].physicalCharacteristics.width.unit), force_bytes("mm"))
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.width.value, 45)
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].quantity.unit), force_bytes("1"))
        self.assertEqual(inst.packageItem[0].packageItem[0].quantity.value, 1)
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].period.unit), force_bytes("a"))
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].period.value, 3)
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].code), force_bytes("Thismedicinalproductdoesnotrequireanyspecialstoragecondition."))
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].system), force_bytes("http://ema.europa.eu/example/specialprecautionsforstorage"))
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].code), force_bytes("ShelfLifeofPackagedMedicinalProduct"))
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].system), force_bytes("http://ema.europa.eu/example/shelfLifeTypePlaceHolder"))
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].type.coding[0].code), force_bytes("Blister"))
        self.assertEqual(force_bytes(inst.packageItem[0].packageItem[0].type.coding[0].system), force_bytes("http://ema.europa.eu/example/packageitemcontainertype"))
        self.assertEqual(force_bytes(inst.packageItem[0].physicalCharacteristics.depth.unit), force_bytes("mm"))
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.depth.value, 23.5)
        self.assertEqual(force_bytes(inst.packageItem[0].physicalCharacteristics.height.unit), force_bytes("mm"))
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.height.value, 50)
        self.assertEqual(force_bytes(inst.packageItem[0].physicalCharacteristics.width.unit), force_bytes("mm"))
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.width.value, 136)
        self.assertEqual(force_bytes(inst.packageItem[0].quantity.unit), force_bytes("1"))
        self.assertEqual(inst.packageItem[0].quantity.value, 1)
        self.assertEqual(force_bytes(inst.packageItem[0].type.coding[0].code), force_bytes("Carton"))
        self.assertEqual(force_bytes(inst.packageItem[0].type.coding[0].system), force_bytes("http://ema.europa.eu/example/packageitemcontainertype"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

