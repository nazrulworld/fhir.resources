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
from .. import contract
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ContractTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Contract", js["resourceType"])
        return contract.Contract(js)
    
    def testContract1(self):
        inst = self.instantiate_from("pcd-example-notOrg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract1(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract1(inst2)
    
    def implContract1(self, inst):
        self.assertEqual(force_bytes(inst.friendly[0].contentAttachment.title), force_bytes("The terms of the consent in friendly consumer speak."))
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notOrg"))
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.legal[0].contentAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In"))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].display), force_bytes("Default Authorization with exceptions."))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].system), force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"))
        self.assertEqual(force_bytes(inst.term[0].text), force_bytes("Withhold this order and any results or related objects from any provider."))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].code), force_bytes("withhold-from"))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].display), force_bytes("Withhold all data from specified actor entity."))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].system), force_bytes("http://example.org/fhir/consent-term-type-codes"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org"))
    
    def testContract2(self):
        inst = self.instantiate_from("pcd-example-notLabs.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract2(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract2(inst2)
    
    def implContract2(self, inst):
        self.assertEqual(force_bytes(inst.friendly[0].contentAttachment.title), force_bytes("The terms of the consent in friendly consumer speak."))
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notLabs"))
        self.assertEqual(inst.issued.date, FHIRDate("2014-08-17").date)
        self.assertEqual(inst.issued.as_json(), "2014-08-17")
        self.assertEqual(force_bytes(inst.legal[0].contentAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In"))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].display), force_bytes("Default Authorization with exceptions."))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].system), force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"))
        self.assertEqual(force_bytes(inst.term[0].subType.coding[0].code), force_bytes("ProcedureRequest"))
        self.assertEqual(force_bytes(inst.term[0].subType.coding[0].system), force_bytes("http://hl7.org/fhir/resource-types"))
        self.assertEqual(force_bytes(inst.term[0].text), force_bytes("Withhold orders from any provider."))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].code), force_bytes("withhold-object-type"))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].system), force_bytes("http://example.org/fhir/consent-term-type-codes"))
        self.assertEqual(force_bytes(inst.term[1].subType.coding[0].code), force_bytes("DiagnosticReport"))
        self.assertEqual(force_bytes(inst.term[1].subType.coding[0].system), force_bytes("http://hl7.org/fhir/resource-types"))
        self.assertEqual(force_bytes(inst.term[1].text), force_bytes("Withhold order results from any provider."))
        self.assertEqual(force_bytes(inst.term[1].type.coding[0].code), force_bytes("withhold-object-type"))
        self.assertEqual(force_bytes(inst.term[1].type.coding[0].system), force_bytes("http://example.org/fhir/consent-term-type-codes"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org"))
    
    def testContract3(self):
        inst = self.instantiate_from("contract-example-42cfr-part2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract3(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract3(inst2)
    
    def implContract3(self, inst):
        self.assertEqual(force_bytes(inst.agent[0].role[0].coding[0].code), force_bytes("IR"))
        self.assertEqual(force_bytes(inst.agent[0].role[0].coding[0].display), force_bytes("Recipient"))
        self.assertEqual(force_bytes(inst.agent[0].role[0].coding[0].system), force_bytes("http://org.mdhhs.fhir.consent-actor-type"))
        self.assertEqual(force_bytes(inst.agent[0].role[0].text), force_bytes("Recipient of restricted health information"))
        self.assertEqual(force_bytes(inst.agent[1].role[0].coding[0].code), force_bytes("IS"))
        self.assertEqual(force_bytes(inst.agent[1].role[0].coding[0].display), force_bytes("Sender"))
        self.assertEqual(force_bytes(inst.agent[1].role[0].coding[0].system), force_bytes("http://org.mdhhs.fhir.consent-actor-type"))
        self.assertEqual(force_bytes(inst.agent[1].role[0].text), force_bytes("Sender of restricted health information"))
        self.assertEqual(force_bytes(inst.id), force_bytes("C-2121"))
        self.assertEqual(inst.issued.date, FHIRDate("2031-11-01T21:18:27-04:00").date)
        self.assertEqual(inst.issued.as_json(), "2031-11-01T21:18:27-04:00")
        self.assertEqual(force_bytes(inst.legal[0].contentAttachment.contentType), force_bytes("application/pdf"))
        self.assertEqual(force_bytes(inst.legal[0].contentAttachment.language), force_bytes("en-US"))
        self.assertEqual(force_bytes(inst.legal[0].contentAttachment.title), force_bytes("MDHHS-5515 Consent To Share Your Health Information"))
        self.assertEqual(force_bytes(inst.legal[0].contentAttachment.url), force_bytes("http://org.mihin.ecms/ConsentDirective-2121"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2016-07-19T18:18:42.108-04:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2016-07-19T18:18:42.108-04:00")
        self.assertEqual(force_bytes(inst.meta.versionId), force_bytes("1"))
        self.assertEqual(force_bytes(inst.securityLabel[0].code), force_bytes("R"))
        self.assertEqual(force_bytes(inst.securityLabel[0].display), force_bytes("Restricted"))
        self.assertEqual(force_bytes(inst.securityLabel[0].system), force_bytes("http://hl7.org/fhir/v3/Confidentiality"))
        self.assertEqual(force_bytes(inst.securityLabel[1].code), force_bytes("ETH"))
        self.assertEqual(force_bytes(inst.securityLabel[1].display), force_bytes("substance abuse information sensitivity"))
        self.assertEqual(force_bytes(inst.securityLabel[1].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.securityLabel[2].code), force_bytes("42CFRPart2"))
        self.assertEqual(force_bytes(inst.securityLabel[2].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.securityLabel[3].code), force_bytes("TREAT"))
        self.assertEqual(force_bytes(inst.securityLabel[3].display), force_bytes("treatment"))
        self.assertEqual(force_bytes(inst.securityLabel[3].system), force_bytes("http://hl7.org/fhir/v3/ActReason"))
        self.assertEqual(force_bytes(inst.securityLabel[4].code), force_bytes("HPAYMT"))
        self.assertEqual(force_bytes(inst.securityLabel[4].display), force_bytes("healthcare payment"))
        self.assertEqual(force_bytes(inst.securityLabel[4].system), force_bytes("http://hl7.org/fhir/v3/ActReason"))
        self.assertEqual(force_bytes(inst.securityLabel[5].code), force_bytes("HOPERAT"))
        self.assertEqual(force_bytes(inst.securityLabel[5].display), force_bytes("healthcare operations"))
        self.assertEqual(force_bytes(inst.securityLabel[5].system), force_bytes("http://hl7.org/fhir/v3/ActReason"))
        self.assertEqual(force_bytes(inst.securityLabel[6].code), force_bytes("PERSISTLABEL"))
        self.assertEqual(force_bytes(inst.securityLabel[6].display), force_bytes("persist security label"))
        self.assertEqual(force_bytes(inst.securityLabel[6].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.securityLabel[7].code), force_bytes("PRIVMARK"))
        self.assertEqual(force_bytes(inst.securityLabel[7].display), force_bytes("privacy mark"))
        self.assertEqual(force_bytes(inst.securityLabel[7].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.securityLabel[8].code), force_bytes("NORDSCLCD"))
        self.assertEqual(force_bytes(inst.securityLabel[8].display), force_bytes("no redisclosure without consent directive"))
        self.assertEqual(force_bytes(inst.securityLabel[8].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.signer[0].signature[0].type[0].code), force_bytes("1.2.840.10065.1.12.1.1"))
        self.assertEqual(force_bytes(inst.signer[0].signature[0].type[0].system), force_bytes("urn:iso-astm:E1762-95:2013"))
        self.assertEqual(inst.signer[0].signature[0].when.date, FHIRDate("2017-02-08T10:57:34+01:00").date)
        self.assertEqual(inst.signer[0].signature[0].when.as_json(), "2017-02-08T10:57:34+01:00")
        self.assertEqual(force_bytes(inst.signer[0].type.code), force_bytes("SELF"))
        self.assertEqual(force_bytes(inst.signer[0].type.system), force_bytes("http://org.mdhhs.fhir.consent-signer-type"))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].code), force_bytes("MDHHS-5515"))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].display), force_bytes("Michigan MDHHS-5515 Consent to Share Behavioral Health Information for Care Coordination Purposes"))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].system), force_bytes("http://hl7.org/fhir/consentcategorycodes"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("OPTIN"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://org.mdhhs.fhir.consentdirective-type"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("Opt-in consent directive"))
    
    def testContract4(self):
        inst = self.instantiate_from("contract-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract4(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract4(inst2)
    
    def implContract4(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("C-123"))
        self.assertEqual(force_bytes(inst.identifier.system), force_bytes("http://happyvalley.com/contract"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("12347"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the contract</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testContract5(self):
        inst = self.instantiate_from("pcd-example-notAuthor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract5(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract5(inst2)
    
    def implContract5(self, inst):
        self.assertEqual(force_bytes(inst.friendly[0].contentAttachment.title), force_bytes("The terms of the consent in friendly consumer speak."))
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notAuthor"))
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.legal[0].contentAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In"))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].display), force_bytes("Default Authorization with exceptions."))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].system), force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"))
        self.assertEqual(force_bytes(inst.term[0].text), force_bytes("Withhold all data authored by Good Health provider."))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].code), force_bytes("withhold-authored-by"))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].display), force_bytes("Withhold all data authored by specified actor entity."))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].system), force_bytes("http://example.org/fhir/consent-term-type-codes"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org"))
    
    def testContract6(self):
        inst = self.instantiate_from("pcd-example-notThem.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract6(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract6(inst2)
    
    def implContract6(self, inst):
        self.assertEqual(force_bytes(inst.friendly[0].contentAttachment.title), force_bytes("The terms of the consent in friendly consumer speak."))
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notThem"))
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.legal[0].contentAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.signer[0].signature[0].type[0].code), force_bytes("1.2.840.10065.1.12.1.1"))
        self.assertEqual(force_bytes(inst.signer[0].signature[0].type[0].system), force_bytes("urn:iso-astm:E1762-95:2013"))
        self.assertEqual(inst.signer[0].signature[0].when.date, FHIRDate("2013-06-08T10:57:34-07:00").date)
        self.assertEqual(inst.signer[0].signature[0].when.as_json(), "2013-06-08T10:57:34-07:00")
        self.assertEqual(force_bytes(inst.signer[0].type.code), force_bytes("COVPTY"))
        self.assertEqual(force_bytes(inst.signer[0].type.system), force_bytes("http://www.hl7.org/fhir/contractsignertypecodes"))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In"))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].display), force_bytes("Default Authorization with exceptions."))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].system), force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"))
        self.assertEqual(force_bytes(inst.term[0].text), force_bytes("Withhold this order and any results or related objects from specified nurse provider."))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].code), force_bytes("withhold-from"))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].display), force_bytes("Withhold all data from specified actor entity."))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].system), force_bytes("http://example.org/fhir/consent-term-type-codes"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org"))
    
    def testContract7(self):
        inst = self.instantiate_from("pcd-example-notThis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract7(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract7(inst2)
    
    def implContract7(self, inst):
        self.assertEqual(force_bytes(inst.friendly[0].contentAttachment.title), force_bytes("The terms of the consent in friendly consumer speak."))
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notThis"))
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(force_bytes(inst.legal[0].contentAttachment.title), force_bytes("The terms of the consent in lawyer speak."))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In"))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].display), force_bytes("Default Authorization with exceptions."))
        self.assertEqual(force_bytes(inst.subType[0].coding[0].system), force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"))
        self.assertEqual(force_bytes(inst.term[0].text), force_bytes("Withhold this order and any results or related objects from any provider."))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].code), force_bytes("withhold-identified-object-and-related"))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].display), force_bytes("Withhold the identified object and any other resources that are related to this object."))
        self.assertEqual(force_bytes(inst.term[0].type.coding[0].system), force_bytes("http://example.org/fhir/consent-term-type-codes"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org"))

