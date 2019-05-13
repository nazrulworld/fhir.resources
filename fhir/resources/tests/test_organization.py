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
from .. import organization
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class OrganizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Organization", js["resourceType"])
        return organization.Organization(js)
    
    def testOrganization1(self):
        inst = self.instantiate_from("organization-example-gastro.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization1(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization1(inst2)
    
    def implOrganization1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("1"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.acme.org.au/units"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("Gastro"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Gastroenterology"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("mobile"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("+1 555 234 3523"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[1].value), force_bytes("gastro@acme.org"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOrganization2(self):
        inst = self.instantiate_from("organization-example-mmanu.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization2(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization2(inst2)
    
    def implOrganization2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("Swizterland"))
        self.assertEqual(force_bytes(inst.id), force_bytes("mmanu"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Acme Corporation"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOrganization3(self):
        inst = self.instantiate_from("organization-example-f002-burgers-card.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization3(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization3(inst2)
    
    def implOrganization3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].line[0]), force_bytes("South Wing, floor 2"))
        self.assertEqual(force_bytes(inst.contact[0].address.line[0]), force_bytes("South Wing, floor 2"))
        self.assertEqual(force_bytes(inst.contact[0].name.text), force_bytes("mevr. D. de Haan"))
        self.assertEqual(force_bytes(inst.contact[0].purpose.coding[0].code), force_bytes("ADMIN"))
        self.assertEqual(force_bytes(inst.contact[0].purpose.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/contactentity-type"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("022-655 2321"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].value), force_bytes("cardio@burgersumc.nl"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[2].system), force_bytes("fax"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[2].value), force_bytes("022-655 2322"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Burgers UMC Cardiology unit"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("022-655 2320"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].code), force_bytes("dept"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].display), force_bytes("Hospital Department"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/organization-type"))
    
    def testOrganization4(self):
        inst = self.instantiate_from("organization-example-lab.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization4(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization4(inst2)
    
    def implOrganization4(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("1832473e-2fe0-452d-abe9-3cdb9879522f"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.acme.org.au/units"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("ClinLab"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Clinical Lab"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("+1 555 234 1234"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[1].value), force_bytes("contact@labs.acme.org"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOrganization5(self):
        inst = self.instantiate_from("organization-example-mihealth.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization5(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization5(inst2)
    
    def implOrganization5(self, inst):
        self.assertEqual(force_bytes(inst.alias[0]), force_bytes("Michigan State Department of Health"))
        self.assertEqual(force_bytes(inst.id), force_bytes("3"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://michigan.gov/state-dept-ids"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("25"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Michigan Health"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOrganization6(self):
        inst = self.instantiate_from("organization-example-f003-burgers-ENT.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization6(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization6(inst2)
    
    def implOrganization6(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].line[0]), force_bytes("West Wing, floor 5"))
        self.assertEqual(force_bytes(inst.contact[0].address.line[0]), force_bytes("West Wing, floor 5"))
        self.assertEqual(force_bytes(inst.contact[0].name.text), force_bytes("mr. F. de Hond"))
        self.assertEqual(force_bytes(inst.contact[0].purpose.coding[0].code), force_bytes("ADMIN"))
        self.assertEqual(force_bytes(inst.contact[0].purpose.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/contactentity-type"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("022-655 7654"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].value), force_bytes("KNO@burgersumc.nl"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[2].system), force_bytes("fax"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[2].value), force_bytes("022-655 0998"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f003"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Burgers UMC Ear,Nose,Throat unit"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("022-655 6780"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].code), force_bytes("dept"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].display), force_bytes("Hospital Department"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/organization-type"))
    
    def testOrganization7(self):
        inst = self.instantiate_from("organization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization7(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization7(inst2)
    
    def implOrganization7(self, inst):
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Ann Arbor"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("USA"))
        self.assertEqual(force_bytes(inst.address[0].line[0]), force_bytes("3300 Washtenaw Avenue, Suite 227"))
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("48104"))
        self.assertEqual(force_bytes(inst.address[0].state), force_bytes("MI"))
        self.assertEqual(force_bytes(inst.alias[0]), force_bytes("HL7 International"))
        self.assertEqual(force_bytes(inst.id), force_bytes("hl7"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Health Level Seven International"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("(+1) 734-677-7777"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("fax"))
        self.assertEqual(force_bytes(inst.telecom[1].value), force_bytes("(+1) 734-677-6622"))
        self.assertEqual(force_bytes(inst.telecom[2].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[2].value), force_bytes("hq@HL7.org"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOrganization8(self):
        inst = self.instantiate_from("organization-example-f001-burgers.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization8(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization8(inst2)
    
    def implOrganization8(self, inst):
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Den Burg"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("NLD"))
        self.assertEqual(force_bytes(inst.address[0].line[0]), force_bytes("Galapagosweg 91"))
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("9105 PZ"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.address[1].city), force_bytes("Den Burg"))
        self.assertEqual(force_bytes(inst.address[1].country), force_bytes("NLD"))
        self.assertEqual(force_bytes(inst.address[1].line[0]), force_bytes("PO Box 2311"))
        self.assertEqual(force_bytes(inst.address[1].postalCode), force_bytes("9100 AA"))
        self.assertEqual(force_bytes(inst.address[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.contact[0].purpose.coding[0].code), force_bytes("PRESS"))
        self.assertEqual(force_bytes(inst.contact[0].purpose.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/contactentity-type"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("022-655 2334"))
        self.assertEqual(force_bytes(inst.contact[1].purpose.coding[0].code), force_bytes("PATINF"))
        self.assertEqual(force_bytes(inst.contact[1].purpose.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/contactentity-type"))
        self.assertEqual(force_bytes(inst.contact[1].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[1].telecom[0].value), force_bytes("022-655 2335"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f001"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:oid:2.16.528.1"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("91654"))
        self.assertEqual(force_bytes(inst.identifier[1].system), force_bytes("urn:oid:2.16.840.1.113883.2.4.6.1"))
        self.assertEqual(force_bytes(inst.identifier[1].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[1].value), force_bytes("17-0112278"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Burgers University Medical Center"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("022-655 2300"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].code), force_bytes("V6"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].display), force_bytes("University Medical Hospital"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].system), force_bytes("urn:oid:2.16.840.1.113883.2.4.15.1060"))
        self.assertEqual(force_bytes(inst.type[0].coding[1].code), force_bytes("prov"))
        self.assertEqual(force_bytes(inst.type[0].coding[1].display), force_bytes("Healthcare Provider"))
        self.assertEqual(force_bytes(inst.type[0].coding[1].system), force_bytes("http://terminology.hl7.org/CodeSystem/organization-type"))
    
    def testOrganization9(self):
        inst = self.instantiate_from("organization-example-insurer.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization9(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization9(inst2)
    
    def implOrganization9(self, inst):
        self.assertEqual(force_bytes(inst.alias[0]), force_bytes("ABC Insurance"))
        self.assertEqual(force_bytes(inst.id), force_bytes("2"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:oid:2.16.840.1.113883.3.19.2.3"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("666666"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("XYZ Insurance"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOrganization10(self):
        inst = self.instantiate_from("organization-example-good-health-care.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization10(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization10(inst2)
    
    def implOrganization10(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("2.16.840.1.113883.19.5"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("2.16.840.1.113883.19.5"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Good Health Clinic"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

