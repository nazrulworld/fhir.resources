# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import devicerequest
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class DeviceRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("DeviceRequest", js["resourceType"])
        return devicerequest.DeviceRequest(js)

    def testDeviceRequest1(self):
        inst = self.instantiate_from("devicerequest-example-insulinpump.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceRequest instance")
        self.implDeviceRequest1(inst)

        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest1(inst2)

    def implDeviceRequest1(self, inst):
        self.assertEqual(
            inst.authoredOn.date, FHIRDate("2013-05-08T09:33:27+07:00").date
        )
        self.assertEqual(inst.authoredOn.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(
            force_bytes(inst.codeCodeableConcept.coding[0].code), force_bytes("43148-6")
        )
        self.assertEqual(
            force_bytes(inst.codeCodeableConcept.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(
            force_bytes(inst.codeCodeableConcept.text),
            force_bytes("Insulin delivery device panel"),
        )
        self.assertEqual(
            force_bytes(inst.groupIdentifier.value), force_bytes("ip_request1")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("insulinpump"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("ip_request1.1")
        )
        self.assertEqual(
            force_bytes(inst.instantiatesCanonical[0]),
            force_bytes(
                "http://motivemi.com/artifacts/PlanDefinition/low-suicide-risk-order-set"
            ),
        )
        self.assertEqual(force_bytes(inst.intent), force_bytes("instance-order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.note[0].text),
            force_bytes("this is the right device brand and model"),
        )
        self.assertEqual(
            inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date
        )
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(
            force_bytes(inst.performerType.coding[0].display),
            force_bytes("Qualified nurse"),
        )
        self.assertEqual(force_bytes(inst.performerType.text), force_bytes("Nurse"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(
            force_bytes(inst.reasonCode[0].text), force_bytes("gastroparesis")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDeviceRequest2(self):
        inst = self.instantiate_from("devicerequest-left-lens.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceRequest instance")
        self.implDeviceRequest2(inst)

        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest2(inst2)

    def implDeviceRequest2(self, inst):
        self.assertEqual(
            force_bytes(inst.codeCodeableConcept.coding[0].code), force_bytes("lens")
        )
        self.assertEqual(
            force_bytes(inst.codeCodeableConcept.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct"
            ),
        )
        self.assertEqual(
            force_bytes(inst.groupIdentifier.system), force_bytes("http://acme.org")
        )
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("15013"))
        self.assertEqual(force_bytes(inst.id), force_bytes("left-lens"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.happysight.com/prescription"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("15013L"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("original-order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-06-15")
        self.assertEqual(
            force_bytes(inst.parameter[0].code.coding[0].code), force_bytes("28842-3")
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].code.coding[0].display),
            force_bytes("Sphere distance Glasses prescription.lens - left"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].code.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].code.text), force_bytes("sphere, left lens")
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].valueQuantity.code), force_bytes("[diop]")
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].valueQuantity.unit), force_bytes("Diopter")
        )
        self.assertEqual(inst.parameter[0].valueQuantity.value, -1.0)
        self.assertEqual(
            force_bytes(inst.parameter[1].code.coding[0].code), force_bytes("28843-1")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].code.coding[0].display),
            force_bytes("Cylinder base distance Glasses prescription.lens - left"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].code.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].code.text), force_bytes("cylinder, left lens")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].valueQuantity.code), force_bytes("[diop]")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].valueQuantity.unit), force_bytes("Diopter")
        )
        self.assertEqual(inst.parameter[1].valueQuantity.value, -0.5)
        self.assertEqual(
            force_bytes(inst.parameter[2].code.coding[0].code), force_bytes("28844-9")
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].code.coding[0].display),
            force_bytes(" Axis distance Glasses prescription.lens - left"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].code.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].code.text), force_bytes("axis, left lens")
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].valueQuantity.code), force_bytes("deg")
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].valueQuantity.unit), force_bytes("Degrees")
        )
        self.assertEqual(inst.parameter[2].valueQuantity.value, 180)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDeviceRequest3(self):
        inst = self.instantiate_from("devicerequest-right-lens.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceRequest instance")
        self.implDeviceRequest3(inst)

        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest3(inst2)

    def implDeviceRequest3(self, inst):
        self.assertEqual(
            force_bytes(inst.codeCodeableConcept.coding[0].code), force_bytes("lens")
        )
        self.assertEqual(
            force_bytes(inst.codeCodeableConcept.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct"
            ),
        )
        self.assertEqual(
            force_bytes(inst.groupIdentifier.system), force_bytes("http://acme.org")
        )
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("15013"))
        self.assertEqual(force_bytes(inst.id), force_bytes("right-lens"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.happysight.com/prescription"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("15013R"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("original-order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-06-15")
        self.assertEqual(
            force_bytes(inst.parameter[0].code.coding[0].code), force_bytes("28826-6")
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].code.coding[0].display),
            force_bytes("Sphere distance Glasses prescription.lens - right"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].code.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].code.text), force_bytes("sphere, right lens")
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].valueQuantity.code), force_bytes("[diop]")
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[0].valueQuantity.unit), force_bytes("Diopter")
        )
        self.assertEqual(inst.parameter[0].valueQuantity.value, -2.0)
        self.assertEqual(
            force_bytes(inst.parameter[1].code.coding[0].code), force_bytes("28829-0")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].code.coding[0].display),
            force_bytes("Prism base distance Glasses prescription.lens - right"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].code.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].code.text), force_bytes("prisms, right lens")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].valueQuantity.code), force_bytes("[diop]")
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[1].valueQuantity.unit), force_bytes("Diopter")
        )
        self.assertEqual(inst.parameter[1].valueQuantity.value, -2.0)
        self.assertEqual(
            force_bytes(inst.parameter[2].code.coding[0].code), force_bytes("28810-0")
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].code.coding[0].display),
            force_bytes("Add 1 LM glasses lens - right"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].code.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].code.text), force_bytes("add, right lens")
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].valueQuantity.code), force_bytes("[diop]")
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].valueQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.parameter[2].valueQuantity.unit), force_bytes("Diopter")
        )
        self.assertEqual(inst.parameter[2].valueQuantity.value, 2.0)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDeviceRequest4(self):
        inst = self.instantiate_from("devicerequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceRequest instance")
        self.implDeviceRequest4(inst)

        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest4(inst2)

    def implDeviceRequest4(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("original-order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
