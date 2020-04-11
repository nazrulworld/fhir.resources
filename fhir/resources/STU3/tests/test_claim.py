# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import claim
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ClaimTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Claim", js["resourceType"])
        return claim.Claim(js)

    def testClaim1(self):
        inst = self.instantiate_from("claim-example-institutional-rich.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim1(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim1(inst2)

    def implClaim1(self, inst):
        self.assertEqual(inst.accident.date.date, FHIRDate("2014-07-09").date)
        self.assertEqual(inst.accident.date.as_json(), "2014-07-09")
        self.assertEqual(
            force_bytes(inst.accident.locationAddress.text),
            force_bytes("Grouse Mountain Ski Hill"),
        )
        self.assertEqual(
            force_bytes(inst.accident.type.coding[0].code), force_bytes("SPT")
        )
        self.assertEqual(
            force_bytes(inst.accident.type.coding[0].display),
            force_bytes("Sporting Accident"),
        )
        self.assertEqual(
            force_bytes(inst.accident.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/ActIncidentCode"),
        )
        self.assertEqual(inst.billablePeriod.end.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.billablePeriod.end.as_json(), "2014-08-16")
        self.assertEqual(inst.billablePeriod.start.date, FHIRDate("2014-08-15").date)
        self.assertEqual(inst.billablePeriod.start.as_json(), "2014-08-15")
        self.assertEqual(
            force_bytes(inst.careTeam[0].qualification.coding[0].code),
            force_bytes("physician"),
        )
        self.assertEqual(
            force_bytes(inst.careTeam[0].qualification.coding[0].system),
            force_bytes("http://hl7.org/fhir/provider-qualification"),
        )
        self.assertTrue(inst.careTeam[0].responsible)
        self.assertEqual(
            force_bytes(inst.careTeam[0].role.coding[0].code), force_bytes("primary")
        )
        self.assertEqual(
            force_bytes(inst.careTeam[0].role.coding[0].system),
            force_bytes("http://hl7.org/fhir/claim-careteamrole"),
        )
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("654456"),
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[0].packageCode.coding[0].code),
            force_bytes("400"),
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[0].packageCode.coding[0].display),
            force_bytes("Head trauma - concussion"),
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[0].packageCode.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-diagnosisrelatedgroup"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.diagnosis[0].type[0].coding[0].code),
            force_bytes("admitting"),
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[0].type[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-diagnosistype"),
        )
        self.assertEqual(inst.employmentImpacted.end.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.employmentImpacted.end.as_json(), "2014-08-16")
        self.assertEqual(
            inst.employmentImpacted.start.date, FHIRDate("2014-08-16").date
        )
        self.assertEqual(inst.employmentImpacted.start.as_json(), "2014-08-16")
        self.assertEqual(inst.hospitalization.end.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.hospitalization.end.as_json(), "2014-08-16")
        self.assertEqual(inst.hospitalization.start.date, FHIRDate("2014-08-15").date)
        self.assertEqual(inst.hospitalization.start.as_json(), "2014-08-15")
        self.assertEqual(force_bytes(inst.id), force_bytes("960151"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happyhospital.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("96123451"))
        self.assertEqual(
            force_bytes(inst.insurance[0].businessArrangement), force_bytes("BA987123")
        )
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(
            force_bytes(inst.insurance[0].preAuthRef[0]), force_bytes("PA2014G56473")
        )
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 125.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("exam")
        )
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-serviceproduct"),
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].unitPrice.value, 125.0)
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("normal")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Claim</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.total.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.total.value, 125.0)
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("institutional")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("complete"))

    def testClaim2(self):
        inst = self.instantiate_from("claim-example-professional.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim2(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim2(inst2)

    def implClaim2(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("654456"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("860150"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happypdocs.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("8612345"))
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 75.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("exam")
        )
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-serviceproduct"),
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].unitPrice.value, 75.0)
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("normal")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Claim</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("professional")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("complete"))

    def testClaim3(self):
        inst = self.instantiate_from("claim-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim3(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim3(inst2)

    def implClaim3(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("123456"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("100150"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happyvalley.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("1200")
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("normal")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Oral Health Claim</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("complete"))

    def testClaim4(self):
        inst = self.instantiate_from("claim-example-vision.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim4(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim4(inst2)

    def implClaim4(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("654321"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("660150"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happysight.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("6612345"))
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 80.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("exam")
        )
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-visionservice"),
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].unitPrice.value, 80.0)
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("normal")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Vision Claim</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("vision"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("complete"))

    def testClaim5(self):
        inst = self.instantiate_from("claim-example-vision-glasses-3tier.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim5(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim5(inst2)

    def implClaim5(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.contained[0].id), force_bytes("claimresponse-1")
        )
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("device-frame"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("device-lens"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("654321"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("660152"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happysight.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("6612347"))
        self.assertFalse(inst.insurance[0].focal)
        self.assertEqual(
            force_bytes(inst.insurance[0].preAuthRef[0]), force_bytes("PR7652387237")
        )
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertTrue(inst.insurance[1].focal)
        self.assertEqual(
            force_bytes(inst.insurance[1].preAuthRef[0]), force_bytes("AB543GTD7567")
        )
        self.assertEqual(inst.insurance[1].sequence, 2)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(
            force_bytes(inst.item[0].category.coding[0].code), force_bytes("F6")
        )
        self.assertEqual(
            force_bytes(inst.item[0].category.coding[0].display),
            force_bytes("Vision Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].category.coding[0].system),
            force_bytes("http://hl7.org/fhir/benefit-subcategory"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].category.coding[0].code),
            force_bytes("F6"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].category.coding[0].display),
            force_bytes("Vision Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].category.coding[0].system),
            force_bytes("http://hl7.org/fhir/benefit-subcategory"),
        )
        self.assertEqual(inst.item[0].detail[0].factor, 1.1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].modifier[0].coding[0].code),
            force_bytes("rooh"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].modifier[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/modifiers"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[0].net.value, 110.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].revenue.coding[0].code),
            force_bytes("0010"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].revenue.coding[0].display),
            force_bytes("Vision Clinic"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].revenue.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-revenue-center"),
        )
        self.assertEqual(inst.item[0].detail[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].service.coding[0].code),
            force_bytes("frame"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-visionservice"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[0].unitPrice.value, 100.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].category.coding[0].code),
            force_bytes("F6"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].category.coding[0].display),
            force_bytes("Vision Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].category.coding[0].system),
            force_bytes("http://hl7.org/fhir/benefit-subcategory"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].net.value, 110.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].programCode[0].coding[0].code),
            force_bytes("none"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].programCode[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-programcode"),
        )
        self.assertEqual(inst.item[0].detail[1].quantity.value, 2)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].revenue.coding[0].code),
            force_bytes("0010"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].revenue.coding[0].display),
            force_bytes("Vision Clinic"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].revenue.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-revenue-center"),
        )
        self.assertEqual(inst.item[0].detail[1].sequence, 2)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].service.coding[0].code),
            force_bytes("lens"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-visionservice"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].category.coding[0].code),
            force_bytes("F6"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].category.coding[0].display),
            force_bytes("Vision Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].category.coding[0].system),
            force_bytes("http://hl7.org/fhir/benefit-subcategory"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[0].factor, 1.1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].modifier[0].coding[0].code),
            force_bytes("rooh"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[0].modifier[0].coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/modifiers"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].net.code),
            force_bytes("USD"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[0].net.value, 66.0)
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[0].programCode[0].coding[0].code
            ),
            force_bytes("none"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[0].programCode[0].coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/ex-programcode"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[0].quantity.value, 2)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].revenue.coding[0].code),
            force_bytes("0010"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].revenue.coding[0].display),
            force_bytes("Vision Clinic"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].revenue.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-revenue-center"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].service.coding[0].code),
            force_bytes("lens"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-visionservice"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].unitPrice.code),
            force_bytes("USD"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[0].unitPrice.value, 30.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].category.coding[0].code),
            force_bytes("F6"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].category.coding[0].display),
            force_bytes("Vision Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].category.coding[0].system),
            force_bytes("http://hl7.org/fhir/benefit-subcategory"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[1].factor, 1.1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].modifier[0].coding[0].code),
            force_bytes("rooh"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[1].modifier[0].coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/modifiers"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].net.code),
            force_bytes("USD"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[1].net.value, 33.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[1].quantity.value, 2)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].revenue.coding[0].code),
            force_bytes("0010"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].revenue.coding[0].display),
            force_bytes("Vision Clinic"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].revenue.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-revenue-center"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[1].sequence, 2)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].service.coding[0].code),
            force_bytes("hardening"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-visionservice"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].unitPrice.code),
            force_bytes("USD"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[1].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[1].unitPrice.value, 15.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].category.coding[0].code),
            force_bytes("F6"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].category.coding[0].display),
            force_bytes("Vision Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].category.coding[0].system),
            force_bytes("http://hl7.org/fhir/benefit-subcategory"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[2].factor, 1.1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].modifier[0].coding[0].code),
            force_bytes("rooh"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].detail[1].subDetail[2].modifier[0].coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/modifiers"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].net.code),
            force_bytes("USD"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[2].net.value, 11.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[2].quantity.value, 2)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].revenue.coding[0].code),
            force_bytes("0010"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].revenue.coding[0].display),
            force_bytes("Vision Clinic"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].revenue.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-revenue-center"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[2].sequence, 3)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].service.coding[0].code),
            force_bytes("UV coating"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-visionservice"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].unitPrice.code),
            force_bytes("USD"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].subDetail[2].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].subDetail[2].unitPrice.value, 5.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].unitPrice.value, 55.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].category.coding[0].code),
            force_bytes("F6"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].category.coding[0].display),
            force_bytes("Vision Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].category.coding[0].system),
            force_bytes("http://hl7.org/fhir/benefit-subcategory"),
        )
        self.assertEqual(inst.item[0].detail[2].factor, 0.07)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[2].net.value, 15.4)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].revenue.coding[0].code),
            force_bytes("0010"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].revenue.coding[0].display),
            force_bytes("Vision Clinic"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].revenue.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-revenue-center"),
        )
        self.assertEqual(inst.item[0].detail[2].sequence, 3)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].service.coding[0].code),
            force_bytes("fst"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-visionservice"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[2].unitPrice.value, 220.0)
        self.assertEqual(
            force_bytes(inst.item[0].modifier[0].coding[0].code), force_bytes("rooh")
        )
        self.assertEqual(
            force_bytes(inst.item[0].modifier[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/modifiers"),
        )
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 235.4)
        self.assertEqual(
            force_bytes(inst.item[0].programCode[0].coding[0].code), force_bytes("none")
        )
        self.assertEqual(
            force_bytes(inst.item[0].programCode[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-programcode"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].revenue.coding[0].code), force_bytes("0010")
        )
        self.assertEqual(
            force_bytes(inst.item[0].revenue.coding[0].display),
            force_bytes("Vision Clinic"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].revenue.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-revenue-center"),
        )
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("glasses")
        )
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-visionservice"),
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].unitPrice.value, 235.4)
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("normal")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Vision Claim for Glasses</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("vision"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("complete"))

    def testClaim6(self):
        inst = self.instantiate_from("claim-example-institutional.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim6(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim6(inst2)

    def implClaim6(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("654456"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("960150"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happyhospital.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("9612345"))
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 125.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("exam")
        )
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-serviceproduct"),
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].unitPrice.value, 125.0)
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("normal")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].code), force_bytes("emergency")
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimsubtype"),
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Claim</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.total.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.total.value, 125.0)
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("institutional")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("complete"))

    def testClaim7(self):
        inst = self.instantiate_from("claim-example-oral-contained.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim7(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim7(inst2)

    def implClaim7(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("org-insurer"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("org-org"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("provider-1"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("patient-1"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("coverage-1"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("123456"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("100152"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happyvalley.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12347"))
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("1200")
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("normal")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Oral Health Claim</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("complete"))

    def testClaim8(self):
        inst = self.instantiate_from("claim-example-pharmacy-medication.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim8(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim8(inst2)

    def implClaim8(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("654456"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("760151"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happypharma.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("7612345"))
        self.assertEqual(
            force_bytes(inst.information[0].category.coding[0].code),
            force_bytes("pharmacyrefill"),
        )
        self.assertEqual(
            force_bytes(inst.information[0].code.coding[0].code), force_bytes("new")
        )
        self.assertEqual(
            force_bytes(inst.information[0].code.coding[0].system),
            force_bytes("http://hl7.org/fhir/pharmacy-refill"),
        )
        self.assertEqual(inst.information[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.information[1].category.coding[0].code),
            force_bytes("pharmacyinformation"),
        )
        self.assertEqual(
            force_bytes(inst.information[1].code.coding[0].code),
            force_bytes("refillsremaining"),
        )
        self.assertEqual(
            force_bytes(inst.information[1].code.coding[0].system),
            force_bytes("http://hl7.org/fhir/pharmacy-information"),
        )
        self.assertEqual(inst.information[1].sequence, 2)
        self.assertEqual(inst.information[1].valueQuantity.value, 2)
        self.assertEqual(
            force_bytes(inst.information[2].category.coding[0].code),
            force_bytes("pharmacyinformation"),
        )
        self.assertEqual(
            force_bytes(inst.information[2].code.coding[0].code),
            force_bytes("dayssupply"),
        )
        self.assertEqual(
            force_bytes(inst.information[2].code.coding[0].system),
            force_bytes("http://hl7.org/fhir/pharmacy-information"),
        )
        self.assertEqual(inst.information[2].sequence, 3)
        self.assertEqual(inst.information[2].valueQuantity.value, 90)
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[0].net.value, 45.0)
        self.assertEqual(inst.item[0].detail[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].service.coding[0].code),
            force_bytes("drugcost"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-pharmaservice"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].net.value, 9.0)
        self.assertEqual(inst.item[0].detail[1].sequence, 2)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].service.coding[0].code),
            force_bytes("markup"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-pharmaservice"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[2].net.value, 36.0)
        self.assertEqual(inst.item[0].detail[2].sequence, 3)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].service.coding[0].code),
            force_bytes("dispensefee"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-pharmaservice"),
        )
        self.assertEqual(inst.item[0].informationLinkId[0], 1)
        self.assertEqual(inst.item[0].informationLinkId[1], 2)
        self.assertEqual(inst.item[0].informationLinkId[2], 3)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 90.0)
        self.assertEqual(force_bytes(inst.item[0].quantity.code), force_bytes("TAB"))
        self.assertEqual(
            force_bytes(inst.item[0].quantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(force_bytes(inst.item[0].quantity.unit), force_bytes("TAB"))
        self.assertEqual(inst.item[0].quantity.value, 90)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("562721")
        )
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].display),
            force_bytes("Alprazolam 0.25mg (Xanax)"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].system),
            force_bytes("http://hl7.org/fhir/RxNorm"),
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(force_bytes(inst.priority.coding[0].code), force_bytes("stat"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Pharmacy Claim</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.total.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.total.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.total.value, 90.0)
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("pharmacy"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("complete"))

    def testClaim9(self):
        inst = self.instantiate_from("claim-example-oral-orthoplan.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim9(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim9(inst2)

    def implClaim9(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2015-03-16").date)
        self.assertEqual(inst.created.as_json(), "2015-03-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("123457"),
        )
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/icd-10"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.fundsReserve.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("100153"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happyvalley.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12355"))
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[0].net.value, 1000.0)
        self.assertEqual(inst.item[0].detail[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].service.coding[0].code),
            force_bytes("ORTHOEXAM"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[0].unitPrice.value, 1000.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].net.value, 1500.0)
        self.assertEqual(inst.item[0].detail[1].sequence, 2)
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].service.coding[0].code),
            force_bytes("ORTHODIAG"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[1].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[1].unitPrice.value, 1500.0)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[2].net.value, 500.0)
        self.assertEqual(inst.item[0].detail[2].sequence, 3)
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].service.coding[0].code),
            force_bytes("ORTHOINITIAL"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[2].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[2].unitPrice.value, 500.0)
        self.assertEqual(inst.item[0].detail[3].quantity.value, 24)
        self.assertEqual(inst.item[0].detail[3].sequence, 4)
        self.assertEqual(
            force_bytes(inst.item[0].detail[3].service.coding[0].code),
            force_bytes("ORTHOMONTHS"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[3].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[4].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[4].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[4].net.value, 250.0)
        self.assertEqual(inst.item[0].detail[4].quantity.value, 24)
        self.assertEqual(inst.item[0].detail[4].sequence, 5)
        self.assertEqual(
            force_bytes(inst.item[0].detail[4].service.coding[0].code),
            force_bytes("ORTHOPERIODIC"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[4].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[4].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[0].detail[4].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].detail[4].unitPrice.value, 250.0)
        self.assertEqual(inst.item[0].diagnosisLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 9000.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("ORTHPLAN")
        )
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2015-05-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2015-05-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].unitPrice.value, 9000.0)
        self.assertEqual(
            force_bytes(inst.item[1].bodySite.coding[0].code), force_bytes("21")
        )
        self.assertEqual(
            force_bytes(inst.item[1].bodySite.coding[0].system),
            force_bytes("http://fdi.org/fhir/oraltoothcodes"),
        )
        self.assertEqual(inst.item[1].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[1].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[1].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[1].net.value, 105.0)
        self.assertEqual(inst.item[1].sequence, 2)
        self.assertEqual(
            force_bytes(inst.item[1].service.coding[0].code), force_bytes("21211")
        )
        self.assertEqual(
            force_bytes(inst.item[1].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(inst.item[1].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[1].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.item[1].subSite[0].coding[0].code), force_bytes("L")
        )
        self.assertEqual(
            force_bytes(inst.item[1].subSite[0].coding[0].system),
            force_bytes("http://fdi.org/fhir/oralsurfacecodes"),
        )
        self.assertEqual(force_bytes(inst.item[1].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[1].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[1].unitPrice.value, 105.0)
        self.assertEqual(
            force_bytes(inst.item[2].bodySite.coding[0].code), force_bytes("36")
        )
        self.assertEqual(
            force_bytes(inst.item[2].bodySite.coding[0].system),
            force_bytes("http://fdi.org/fhir/oraltoothcodes"),
        )
        self.assertEqual(inst.item[2].careTeamLinkId[0], 1)
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].detail[0].net.value, 750.0)
        self.assertEqual(inst.item[2].detail[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].service.coding[0].code),
            force_bytes("27211"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].detail[0].unitPrice.value, 750.0)
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].detail[1].net.value, 350.0)
        self.assertEqual(inst.item[2].detail[1].sequence, 2)
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].service.coding[0].code),
            force_bytes("lab"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].detail[1].unitPrice.value, 350.0)
        self.assertEqual(force_bytes(inst.item[2].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[2].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[2].net.value, 1100.0)
        self.assertEqual(inst.item[2].sequence, 3)
        self.assertEqual(
            force_bytes(inst.item[2].service.coding[0].code), force_bytes("27211")
        )
        self.assertEqual(
            force_bytes(inst.item[2].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(inst.item[2].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[2].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[2].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[2].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].unitPrice.value, 1100.0)
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("normal")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Oral Health Claim</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("proposed"))

    def testClaim10(self):
        inst = self.instantiate_from("claim-example-oral-average.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim10(inst)

        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim10(inst2)

    def implClaim10(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.diagnosis[0].diagnosisCodeableConcept.coding[0].code),
            force_bytes("123456"),
        )
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("100151"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happyvalley.com/claim"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12346"))
        self.assertEqual(
            force_bytes(inst.information[0].category.coding[0].code),
            force_bytes("missingtooth"),
        )
        self.assertEqual(
            force_bytes(inst.information[0].category.coding[0].system),
            force_bytes("http://hl7.org/fhir/claiminformationcategory"),
        )
        self.assertEqual(
            force_bytes(inst.information[0].code.coding[0].code), force_bytes("15")
        )
        self.assertEqual(
            force_bytes(inst.information[0].code.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-tooth"),
        )
        self.assertEqual(
            force_bytes(inst.information[0].reason.coding[0].code), force_bytes("e")
        )
        self.assertEqual(
            force_bytes(inst.information[0].reason.coding[0].system),
            force_bytes("http://hl7.org/fhir/missingtoothreason"),
        )
        self.assertEqual(inst.information[0].sequence, 1)
        self.assertEqual(
            inst.information[0].timingDate.date, FHIRDate("2012-04-07").date
        )
        self.assertEqual(inst.information[0].timingDate.as_json(), "2012-04-07")
        self.assertEqual(
            force_bytes(inst.information[1].category.coding[0].code),
            force_bytes("exception"),
        )
        self.assertEqual(
            force_bytes(inst.information[1].category.coding[0].system),
            force_bytes("http://hl7.org/fhir/claiminformationcategory"),
        )
        self.assertEqual(
            force_bytes(inst.information[1].code.coding[0].code), force_bytes("student")
        )
        self.assertEqual(
            force_bytes(inst.information[1].code.coding[0].system),
            force_bytes("http://hl7.org/fhir/claim-exception"),
        )
        self.assertEqual(inst.information[1].sequence, 2)
        self.assertEqual(
            force_bytes(inst.information[1].valueString),
            force_bytes("Happy Valley Community College"),
        )
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.item[0].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[0].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].code), force_bytes("1200")
        )
        self.assertEqual(
            force_bytes(inst.item[0].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[0].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(
            force_bytes(inst.item[1].bodySite.coding[0].code), force_bytes("21")
        )
        self.assertEqual(
            force_bytes(inst.item[1].bodySite.coding[0].system),
            force_bytes("http://fdi.org/fhir/oraltoothcodes"),
        )
        self.assertEqual(inst.item[1].careTeamLinkId[0], 1)
        self.assertEqual(force_bytes(inst.item[1].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[1].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[1].net.value, 105.0)
        self.assertEqual(inst.item[1].sequence, 2)
        self.assertEqual(
            force_bytes(inst.item[1].service.coding[0].code), force_bytes("21211")
        )
        self.assertEqual(
            force_bytes(inst.item[1].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(inst.item[1].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[1].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.item[1].subSite[0].coding[0].code), force_bytes("L")
        )
        self.assertEqual(
            force_bytes(inst.item[1].subSite[0].coding[0].system),
            force_bytes("http://fdi.org/fhir/oralsurfacecodes"),
        )
        self.assertEqual(force_bytes(inst.item[1].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[1].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[1].unitPrice.value, 105.0)
        self.assertEqual(
            force_bytes(inst.item[2].bodySite.coding[0].code), force_bytes("36")
        )
        self.assertEqual(
            force_bytes(inst.item[2].bodySite.coding[0].system),
            force_bytes("http://fdi.org/fhir/oraltoothcodes"),
        )
        self.assertEqual(inst.item[2].careTeamLinkId[0], 1)
        self.assertEqual(inst.item[2].detail[0].factor, 0.75)
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].detail[0].net.value, 750.0)
        self.assertEqual(inst.item[2].detail[0].sequence, 1)
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].service.coding[0].code),
            force_bytes("27211"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[0].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].detail[0].unitPrice.value, 1000.0)
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].net.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].net.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].detail[1].net.value, 350.0)
        self.assertEqual(inst.item[2].detail[1].sequence, 2)
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].service.coding[0].code),
            force_bytes("lab"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].unitPrice.code), force_bytes("USD")
        )
        self.assertEqual(
            force_bytes(inst.item[2].detail[1].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].detail[1].unitPrice.value, 350.0)
        self.assertEqual(force_bytes(inst.item[2].net.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[2].net.system), force_bytes("urn:iso:std:iso:4217")
        )
        self.assertEqual(inst.item[2].net.value, 1100.0)
        self.assertEqual(inst.item[2].sequence, 3)
        self.assertEqual(
            force_bytes(inst.item[2].service.coding[0].code), force_bytes("27211")
        )
        self.assertEqual(
            force_bytes(inst.item[2].service.coding[0].system),
            force_bytes("http://example.org/fhir/oralservicecodes"),
        )
        self.assertEqual(inst.item[2].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[2].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.item[2].unitPrice.code), force_bytes("USD"))
        self.assertEqual(
            force_bytes(inst.item[2].unitPrice.system),
            force_bytes("urn:iso:std:iso:4217"),
        )
        self.assertEqual(inst.item[2].unitPrice.value, 1100.0)
        self.assertEqual(
            force_bytes(inst.payee.type.coding[0].code), force_bytes("provider")
        )
        self.assertEqual(
            force_bytes(inst.priority.coding[0].code), force_bytes("normal")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the Oral Health Claim</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/ex-claimtype"),
        )
        self.assertEqual(force_bytes(inst.use), force_bytes("complete"))
