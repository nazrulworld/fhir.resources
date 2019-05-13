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
from .. import dataelement
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DataElementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DataElement", js["resourceType"])
        return dataelement.DataElement(js)
    
    def testDataElement1(self):
        inst = self.instantiate_from("dataelement-labtestmaster-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DataElement instance")
        self.implDataElement1(inst)
        
        js = inst.as_json()
        self.assertEqual("DataElement", js["resourceType"])
        inst2 = dataelement.DataElement(js)
        self.implDataElement1(inst2)
    
    def implDataElement1(self, inst):
        self.assertEqual(force_bytes(inst.element[0].alias[0]), force_bytes("Protime, PT"))
        self.assertEqual(force_bytes(inst.element[0].comment), force_bytes("Used to screen the integrity of the extrinsic and common pathways of coagulation and to monitor warfarin anticoagulation. "))
        self.assertEqual(force_bytes(inst.element[0].definition), force_bytes("The PT test evaluates the extrinsic and common pathways of the coagulation cascade."))
        self.assertEqual(force_bytes(inst.element[0].example[0].label), force_bytes("Simple"))
        self.assertEqual(inst.element[0].example[0].valueDecimal, 10.0)
        self.assertEqual(force_bytes(inst.element[0].extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/elementdefinition-allowedUnits"))
        self.assertEqual(force_bytes(inst.element[0].extension[0].valueCodeableConcept.coding[0].code), force_bytes("s"))
        self.assertEqual(force_bytes(inst.element[0].extension[0].valueCodeableConcept.coding[0].display), force_bytes("second"))
        self.assertEqual(force_bytes(inst.element[0].extension[0].valueCodeableConcept.coding[0].system), force_bytes("http://unitsofmeasure.org"))
        self.assertTrue(inst.element[0].extension[0].valueCodeableConcept.coding[0].userSelected)
        self.assertEqual(force_bytes(inst.element[0].extension[0].valueCodeableConcept.coding[0].version), force_bytes("1.9"))
        self.assertEqual(force_bytes(inst.element[0].extension[0].valueCodeableConcept.text), force_bytes("second"))
        self.assertEqual(force_bytes(inst.element[0].mapping[0].identity), force_bytes("loinc"))
        self.assertEqual(force_bytes(inst.element[0].mapping[0].map), force_bytes("5964-2"))
        self.assertEqual(force_bytes(inst.element[0].path), force_bytes("prothrombin"))
        self.assertEqual(force_bytes(inst.element[0].requirements), force_bytes("This test is orderable. A plasma specimen in a 3.2% sodium citrate blue top tube is required."))
        self.assertEqual(force_bytes(inst.element[0].type[0].code), force_bytes("decimal"))
        self.assertEqual(force_bytes(inst.id), force_bytes("prothrombin"))
        self.assertEqual(inst.identifier[0].period.start.date, FHIRDate("2011-05-19").date)
        self.assertEqual(inst.identifier[0].period.start.as_json(), "2011-05-19")
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.CenturyHospital/Laboratory/DirectoryofServices"))
        self.assertEqual(force_bytes(inst.identifier[0].type.text), force_bytes("Prothrombin Time, PT"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("11"))
        self.assertEqual(force_bytes(inst.mapping[0].comment), force_bytes("Version 2.48 or later"))
        self.assertEqual(force_bytes(inst.mapping[0].identity), force_bytes("loinc"))
        self.assertEqual(force_bytes(inst.mapping[0].name), force_bytes("LOINC"))
        self.assertEqual(force_bytes(inst.mapping[0].uri), force_bytes("http://loinc.org/"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Prothrombin Time"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDataElement2(self):
        inst = self.instantiate_from("dataelement-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DataElement instance")
        self.implDataElement2(inst)
        
        js = inst.as_json()
        self.assertEqual("DataElement", js["resourceType"])
        inst2 = dataelement.DataElement(js)
        self.implDataElement2(inst2)
    
    def implDataElement2(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("2179414"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("2179414-permitted"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("2179414-cm"))
        self.assertEqual(inst.date.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.date.as_json(), "2016-01-01")
        self.assertEqual(force_bytes(inst.element[0].binding.strength), force_bytes("required"))
        self.assertEqual(force_bytes(inst.element[0].code[0].code), force_bytes("46098-0"))
        self.assertEqual(force_bytes(inst.element[0].code[0].display), force_bytes("Sex"))
        self.assertEqual(force_bytes(inst.element[0].code[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.element[0].definition), force_bytes("The code representing the gender of a person."))
        self.assertEqual(force_bytes(inst.element[0].extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/minLength"))
        self.assertEqual(inst.element[0].extension[0].valueInteger, 1)
        self.assertEqual(force_bytes(inst.element[0].extension[1].url), force_bytes("http://hl7.org/fhir/StructureDefinition/elementdefinition-question"))
        self.assertEqual(force_bytes(inst.element[0].extension[1].valueString), force_bytes("Gender"))
        self.assertEqual(force_bytes(inst.element[0].mapping[0].identity), force_bytes("fhir"))
        self.assertEqual(force_bytes(inst.element[0].mapping[0].language), force_bytes("application/xquery"))
        self.assertEqual(force_bytes(inst.element[0].mapping[0].map), force_bytes("return f:/Patient/f:gender"))
        self.assertEqual(inst.element[0].maxLength, 13)
        self.assertEqual(force_bytes(inst.element[0].path), force_bytes("Gender"))
        self.assertEqual(force_bytes(inst.element[0].type[0].code), force_bytes("CodeableConcept"))
        self.assertEqual(force_bytes(inst.id), force_bytes("gender"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("2179650"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.mapping[0].identity), force_bytes("fhir"))
        self.assertEqual(force_bytes(inst.mapping[0].name), force_bytes("Fast Healthcare Interoperable Resources (FHIR)"))
        self.assertEqual(force_bytes(inst.mapping[0].uri), force_bytes("http://hl7.org/fhir/api"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Gender Code"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("DCP"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Administrative gender"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0"))

