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
from .. import location
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class LocationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Location", js["resourceType"])
        return location.Location(js)
    
    def testLocation1(self):
        inst = self.instantiate_from("location-example-room.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation1(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation1(inst2)
    
    def implLocation1(self, inst):
        self.assertEqual(force_bytes(inst.alias[0]), force_bytes("South Wing OR 5"))
        self.assertEqual(force_bytes(inst.alias[1]), force_bytes("Main Wing OR 2"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Old South Wing, Neuro Radiology Operation Room 1 on second floor"))
        self.assertEqual(force_bytes(inst.id), force_bytes("2"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("B1-S.F2.1.00"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("instance"))
        self.assertEqual(force_bytes(inst.name), force_bytes("South Wing Neuro OR 1"))
        self.assertEqual(force_bytes(inst.operationalStatus.code), force_bytes("H"))
        self.assertEqual(force_bytes(inst.operationalStatus.display), force_bytes("Housekeeping"))
        self.assertEqual(force_bytes(inst.operationalStatus.system), force_bytes("http://hl7.org/fhir/v2/0116"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].code), force_bytes("ro"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].display), force_bytes("Room"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].system), force_bytes("http://hl7.org/fhir/location-physical-type"))
        self.assertEqual(force_bytes(inst.status), force_bytes("suspended"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("2329"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Burgers UMC, South Wing, second floor, Neuro Radiology Operation Room 1</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("RNEU"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Neuroradiology unit"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://hl7.org/fhir/v3/RoleCode"))
    
    def testLocation2(self):
        inst = self.instantiate_from("location-example-hl7hq.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation2(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation2(inst2)
    
    def implLocation2(self, inst):
        self.assertEqual(force_bytes(inst.address.city), force_bytes("Ann Arbor"))
        self.assertEqual(force_bytes(inst.address.country), force_bytes("USA"))
        self.assertEqual(force_bytes(inst.address.line[0]), force_bytes("3300 Washtenaw Avenue, Suite 227"))
        self.assertEqual(force_bytes(inst.address.postalCode), force_bytes("48104"))
        self.assertEqual(force_bytes(inst.address.state), force_bytes("MI"))
        self.assertEqual(force_bytes(inst.description), force_bytes("HL7 Headquarters"))
        self.assertEqual(force_bytes(inst.id), force_bytes("hl7"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("instance"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Health Level Seven International"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].code), force_bytes("bu"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].display), force_bytes("Building"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].system), force_bytes("http://hl7.org/fhir/location-physical-type"))
        self.assertEqual(inst.position.latitude, -83.69471)
        self.assertEqual(inst.position.longitude, 42.2565)
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("(+1) 734-677-7777"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("fax"))
        self.assertEqual(force_bytes(inst.telecom[1].value), force_bytes("(+1) 734-677-6622"))
        self.assertEqual(force_bytes(inst.telecom[2].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[2].value), force_bytes("hq@HL7.org"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("SLEEP"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Sleep disorders unit"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://hl7.org/fhir/v3/RoleCode"))
    
    def testLocation3(self):
        inst = self.instantiate_from("location-example-ambulance.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation3(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation3(inst2)
    
    def implLocation3(self, inst):
        self.assertEqual(force_bytes(inst.description), force_bytes("Ambulance provided by Burgers University Medical Center"))
        self.assertEqual(force_bytes(inst.id), force_bytes("amb"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("kind"))
        self.assertEqual(force_bytes(inst.name), force_bytes("BUMC Ambulance"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].code), force_bytes("ve"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].display), force_bytes("Vehicle"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].system), force_bytes("http://hl7.org/fhir/location-physical-type"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("mobile"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("2329"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Mobile Clinic</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("AMB"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Ambulance"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://hl7.org/fhir/v3/RoleCode"))
    
    def testLocation4(self):
        inst = self.instantiate_from("location-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation4(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation4(inst2)
    
    def implLocation4(self, inst):
        self.assertEqual(force_bytes(inst.address.city), force_bytes("Den Burg"))
        self.assertEqual(force_bytes(inst.address.country), force_bytes("NLD"))
        self.assertEqual(force_bytes(inst.address.line[0]), force_bytes("Galapagosweg 91, Building A"))
        self.assertEqual(force_bytes(inst.address.postalCode), force_bytes("9105 PZ"))
        self.assertEqual(force_bytes(inst.address.use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Second floor of the Old South Wing, formerly in use by Psychiatry"))
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/location-alias"))
        self.assertEqual(force_bytes(inst.extension[0].valueString), force_bytes("Burgers University Medical Center, South Wing, second floor"))
        self.assertEqual(force_bytes(inst.extension[1].url), force_bytes("http://hl7.org/fhir/StructureDefinition/location-alias"))
        self.assertEqual(force_bytes(inst.extension[1].valueString), force_bytes("BU MC, SW, F2"))
        self.assertEqual(force_bytes(inst.id), force_bytes("1"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("B1-S.F2"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("instance"))
        self.assertEqual(force_bytes(inst.name), force_bytes("South Wing, second floor"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].code), force_bytes("wi"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].display), force_bytes("Wing"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].system), force_bytes("http://hl7.org/fhir/location-physical-type"))
        self.assertEqual(inst.position.altitude, 0)
        self.assertEqual(inst.position.latitude, 42.25475478)
        self.assertEqual(inst.position.longitude, -83.6945691)
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("2328"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("fax"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[1].value), force_bytes("2329"))
        self.assertEqual(force_bytes(inst.telecom[2].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[2].value), force_bytes("second wing admissions"))
        self.assertEqual(force_bytes(inst.telecom[3].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.telecom[3].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[3].value), force_bytes("http://sampleorg.com/southwing"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Burgers UMC, South Wing, second floor</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testLocation5(self):
        inst = self.instantiate_from("location-example-patients-home.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation5(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation5(inst2)
    
    def implLocation5(self, inst):
        self.assertEqual(force_bytes(inst.description), force_bytes("Patient's Home"))
        self.assertEqual(force_bytes(inst.id), force_bytes("ph"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("kind"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Patient's Home"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].code), force_bytes("ho"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].display), force_bytes("House"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].system), force_bytes("http://hl7.org/fhir/location-physical-type"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Patient's Home</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("PTRES"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Patient's Residence"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://hl7.org/fhir/v3/RoleCode"))
    
    def testLocation6(self):
        inst = self.instantiate_from("location-example-ukpharmacy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation6(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation6(inst2)
    
    def implLocation6(self, inst):
        self.assertEqual(force_bytes(inst.description), force_bytes("All Pharmacies in the United Kingdom covered by the National Pharmacy Association"))
        self.assertEqual(force_bytes(inst.id), force_bytes("ukp"))
        self.assertEqual(force_bytes(inst.mode), force_bytes("kind"))
        self.assertEqual(force_bytes(inst.name), force_bytes("UK Pharmacies"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].code), force_bytes("jdn"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].display), force_bytes("Jurisdiction"))
        self.assertEqual(force_bytes(inst.physicalType.coding[0].system), force_bytes("http://hl7.org/fhir/location-physical-type"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">UK Pharmacies</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("PHARM"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Pharmacy"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://hl7.org/fhir/v3/RoleCode"))

