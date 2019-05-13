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
from .. import communication
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class CommunicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Communication", js["resourceType"])
        return communication.Communication(js)
    
    def testCommunication1(self):
        inst = self.instantiate_from("communication-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Communication instance")
        self.implCommunication1(inst)
        
        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication1(inst2)
    
    def implCommunication1(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("Alert"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://acme.org/messagetypes"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Alert"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:oid:1.3.4.5.6.7"))
        self.assertEqual(force_bytes(inst.identifier[0].type.text), force_bytes("Paging System"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("2345678901"))
        self.assertEqual(force_bytes(inst.medium[0].coding[0].code), force_bytes("WRITTEN"))
        self.assertEqual(force_bytes(inst.medium[0].coding[0].display), force_bytes("written"))
        self.assertEqual(force_bytes(inst.medium[0].coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationMode"))
        self.assertEqual(force_bytes(inst.medium[0].text), force_bytes("written"))
        self.assertEqual(force_bytes(inst.payload[0].contentString), force_bytes("Patient 1 has a very high serum potassium value (7.2 mmol/L on 2014-Dec-12 at 5:55 pm)"))
        self.assertEqual(inst.received.date, FHIRDate("2014-12-12T18:01:11-08:00").date)
        self.assertEqual(inst.received.as_json(), "2014-12-12T18:01:11-08:00")
        self.assertEqual(inst.sent.date, FHIRDate("2014-12-12T18:01:10-08:00").date)
        self.assertEqual(inst.sent.as_json(), "2014-12-12T18:01:10-08:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Patient has very high serum potassium</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testCommunication2(self):
        inst = self.instantiate_from("communication-example-fm-solicited-attachment.json")
        self.assertIsNotNone(inst, "Must have instantiated a Communication instance")
        self.implCommunication2(inst)
        
        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication2(inst2)
    
    def implCommunication2(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("SolicitedAttachment"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://acme.org/messagetypes"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("provider"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("payor"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("request"))
        self.assertEqual(force_bytes(inst.id), force_bytes("fm-solicited"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.providerco.com/communication"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.payload[0].contentAttachment.contentType), force_bytes("application/pdf"))
        self.assertEqual(inst.payload[0].contentAttachment.creation.date, FHIRDate("2010-02-01T11:50:23-05:00").date)
        self.assertEqual(inst.payload[0].contentAttachment.creation.as_json(), "2010-02-01T11:50:23-05:00")
        self.assertEqual(force_bytes(inst.payload[0].contentAttachment.data), force_bytes("SGVsbG8="))
        self.assertEqual(force_bytes(inst.payload[0].contentAttachment.title), force_bytes("accident notes 20100201.pdf"))
        self.assertEqual(force_bytes(inst.payload[1].contentAttachment.contentType), force_bytes("application/pdf"))
        self.assertEqual(inst.payload[1].contentAttachment.creation.date, FHIRDate("2010-02-01T10:57:34+01:00").date)
        self.assertEqual(inst.payload[1].contentAttachment.creation.as_json(), "2010-02-01T10:57:34+01:00")
        self.assertEqual(force_bytes(inst.payload[1].contentAttachment.hash), force_bytes("SGVsbG8gdGhlcmU="))
        self.assertEqual(inst.payload[1].contentAttachment.size, 104274)
        self.assertEqual(force_bytes(inst.payload[1].contentAttachment.url), force_bytes("http://happyvalley.com/docs/AB12345"))
        self.assertEqual(inst.sent.date, FHIRDate("2016-06-12T18:01:10-08:00").date)
        self.assertEqual(inst.sent.as_json(), "2016-06-12T18:01:10-08:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Attachment in response to a Request</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testCommunication3(self):
        inst = self.instantiate_from("communication-example-fm-attachment.json")
        self.assertIsNotNone(inst, "Must have instantiated a Communication instance")
        self.implCommunication3(inst)
        
        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication3(inst2)
    
    def implCommunication3(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("SolicitedAttachment"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://acme.org/messagetypes"))
        self.assertEqual(force_bytes(inst.id), force_bytes("fm-attachment"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.providerco.com/communication"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.payload[0].contentAttachment.contentType), force_bytes("application/pdf"))
        self.assertEqual(inst.payload[0].contentAttachment.creation.date, FHIRDate("2010-02-01T11:50:23-05:00").date)
        self.assertEqual(inst.payload[0].contentAttachment.creation.as_json(), "2010-02-01T11:50:23-05:00")
        self.assertEqual(force_bytes(inst.payload[0].contentAttachment.data), force_bytes("SGVsbG8="))
        self.assertEqual(force_bytes(inst.payload[0].contentAttachment.title), force_bytes("accident notes 20100201.pdf"))
        self.assertEqual(force_bytes(inst.payload[1].contentAttachment.contentType), force_bytes("application/pdf"))
        self.assertEqual(inst.payload[1].contentAttachment.creation.date, FHIRDate("2010-02-01T10:57:34+01:00").date)
        self.assertEqual(inst.payload[1].contentAttachment.creation.as_json(), "2010-02-01T10:57:34+01:00")
        self.assertEqual(force_bytes(inst.payload[1].contentAttachment.hash), force_bytes("SGVsbG8gdGhlcmU="))
        self.assertEqual(inst.payload[1].contentAttachment.size, 104274)
        self.assertEqual(force_bytes(inst.payload[1].contentAttachment.url), force_bytes("http://happyvalley.com/docs/AB12345"))
        self.assertEqual(inst.sent.date, FHIRDate("2016-06-12T18:01:10-08:00").date)
        self.assertEqual(inst.sent.as_json(), "2016-06-12T18:01:10-08:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Attachment which is unsolicited</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

