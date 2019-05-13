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
from .. import imagingstudy
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ImagingStudyTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImagingStudy", js["resourceType"])
        return imagingstudy.ImagingStudy(js)
    
    def testImagingStudy1(self):
        inst = self.instantiate_from("imagingstudy-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingStudy instance")
        self.implImagingStudy1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImagingStudy", js["resourceType"])
        inst2 = imagingstudy.ImagingStudy(js)
        self.implImagingStudy1(inst2)
    
    def implImagingStudy1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:dicom:uid"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430045"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.numberOfInstances, 1)
        self.assertEqual(inst.numberOfSeries, 1)
        self.assertEqual(force_bytes(inst.series[0].bodySite.code), force_bytes("67734004"))
        self.assertEqual(force_bytes(inst.series[0].bodySite.display), force_bytes("Upper Trunk Structure"))
        self.assertEqual(force_bytes(inst.series[0].bodySite.system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.series[0].description), force_bytes("CT Surview 180"))
        self.assertEqual(inst.series[0].instance[0].number, 1)
        self.assertEqual(force_bytes(inst.series[0].instance[0].sopClass.code), force_bytes("urn:oid:1.2.840.10008.5.1.4.1.1.2"))
        self.assertEqual(force_bytes(inst.series[0].instance[0].sopClass.system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.series[0].instance[0].uid), force_bytes("2.16.124.113543.6003.189642796.63084.16748.2599092903"))
        self.assertEqual(force_bytes(inst.series[0].modality.code), force_bytes("CT"))
        self.assertEqual(force_bytes(inst.series[0].modality.system), force_bytes("http://dicom.nema.org/resources/ontology/DCM"))
        self.assertEqual(inst.series[0].number, 3)
        self.assertEqual(inst.series[0].numberOfInstances, 1)
        self.assertEqual(force_bytes(inst.series[0].uid), force_bytes("2.16.124.113543.6003.2588828330.45298.17418.2723805630"))
        self.assertEqual(inst.started.date, FHIRDate("2011-01-01T11:01:20+03:00").date)
        self.assertEqual(inst.started.as_json(), "2011-01-01T11:01:20+03:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("available"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">CT Chest.  John Smith (MRN: 09236). Accession: W12342398. Performed: 2011-01-01. 3 series, 12 images.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testImagingStudy2(self):
        inst = self.instantiate_from("imagingstudy-example-xr.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingStudy instance")
        self.implImagingStudy2(inst)
        
        js = inst.as_json()
        self.assertEqual("ImagingStudy", js["resourceType"])
        inst2 = imagingstudy.ImagingStudy(js)
        self.implImagingStudy2(inst2)
    
    def implImagingStudy2(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example-xr"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:dicom:uid"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430046"))
        self.assertEqual(force_bytes(inst.identifier[1].type.coding[0].code), force_bytes("ACSN"))
        self.assertEqual(force_bytes(inst.identifier[1].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"))
        self.assertEqual(force_bytes(inst.identifier[1].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[1].value), force_bytes("W12342398"))
        self.assertEqual(force_bytes(inst.identifier[2].use), force_bytes("secondary"))
        self.assertEqual(force_bytes(inst.identifier[2].value), force_bytes("55551234"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.modality[0].code), force_bytes("DX"))
        self.assertEqual(force_bytes(inst.modality[0].system), force_bytes("http://dicom.nema.org/resources/ontology/DCM"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("XR Wrist 3+ Views"))
        self.assertEqual(inst.numberOfInstances, 2)
        self.assertEqual(inst.numberOfSeries, 1)
        self.assertEqual(force_bytes(inst.procedureCode[0].coding[0].code), force_bytes("RPID2589"))
        self.assertEqual(force_bytes(inst.procedureCode[0].coding[0].display), force_bytes("XR Wrist 3+ Views"))
        self.assertEqual(force_bytes(inst.procedureCode[0].coding[0].system), force_bytes("http://www.radlex.org"))
        self.assertEqual(force_bytes(inst.procedureCode[0].text), force_bytes("XR Wrist 3+ Views"))
        self.assertEqual(force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("357009"))
        self.assertEqual(force_bytes(inst.reasonCode[0].coding[0].display), force_bytes("Closed fracture of trapezoidal bone of wrist"))
        self.assertEqual(force_bytes(inst.reasonCode[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.series[0].bodySite.code), force_bytes("T-15460"))
        self.assertEqual(force_bytes(inst.series[0].bodySite.display), force_bytes("Wrist Joint"))
        self.assertEqual(force_bytes(inst.series[0].bodySite.system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.series[0].description), force_bytes("XR Wrist 3+ Views"))
        self.assertEqual(inst.series[0].instance[0].number, 1)
        self.assertEqual(force_bytes(inst.series[0].instance[0].sopClass.code), force_bytes("urn:oid:1.2.840.10008.5.1.4.1.1.2"))
        self.assertEqual(force_bytes(inst.series[0].instance[0].sopClass.system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.series[0].instance[0].title), force_bytes("PA VIEW"))
        self.assertEqual(force_bytes(inst.series[0].instance[0].uid), force_bytes("2.16.124.113543.6003.1154777499.30246.19789.3503430045.1.1"))
        self.assertEqual(inst.series[0].instance[1].number, 2)
        self.assertEqual(force_bytes(inst.series[0].instance[1].sopClass.code), force_bytes("urn:oid:1.2.840.10008.5.1.4.1.1.2"))
        self.assertEqual(force_bytes(inst.series[0].instance[1].sopClass.system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.series[0].instance[1].title), force_bytes("LL VIEW"))
        self.assertEqual(force_bytes(inst.series[0].instance[1].uid), force_bytes("2.16.124.113543.6003.1154777499.30246.19789.3503430045.1.2"))
        self.assertEqual(force_bytes(inst.series[0].laterality.code), force_bytes("419161000"))
        self.assertEqual(force_bytes(inst.series[0].laterality.display), force_bytes("Unilateral left"))
        self.assertEqual(force_bytes(inst.series[0].laterality.system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.series[0].modality.code), force_bytes("DX"))
        self.assertEqual(force_bytes(inst.series[0].modality.system), force_bytes("http://dicom.nema.org/resources/ontology/DCM"))
        self.assertEqual(inst.series[0].number, 3)
        self.assertEqual(inst.series[0].numberOfInstances, 2)
        self.assertEqual(force_bytes(inst.series[0].performer[0].function.coding[0].code), force_bytes("PRF"))
        self.assertEqual(force_bytes(inst.series[0].performer[0].function.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ParticipationType"))
        self.assertEqual(inst.series[0].started.date, FHIRDate("2011-01-01T11:01:20+03:00").date)
        self.assertEqual(inst.series[0].started.as_json(), "2011-01-01T11:01:20+03:00")
        self.assertEqual(force_bytes(inst.series[0].uid), force_bytes("2.16.124.113543.6003.1154777499.30246.19789.3503430045.1"))
        self.assertEqual(inst.started.date, FHIRDate("2017-01-01T11:01:20+03:00").date)
        self.assertEqual(inst.started.as_json(), "2017-01-01T11:01:20+03:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("available"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">XR Wrist 3+ Views. John Smith (MRN: 09236). Accession: W12342398. Performed: 2017-01-01. 1 series, 2 images.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

