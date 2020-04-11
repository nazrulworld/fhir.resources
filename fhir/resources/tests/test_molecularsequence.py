# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence
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

from .. import molecularsequence
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MolecularSequenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("MolecularSequence", js["resourceType"])
        return molecularsequence.MolecularSequence(js)

    def testMolecularSequence1(self):
        inst = self.instantiate_from("sequence-genetics-example-breastcancer.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence1(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence1(inst2)

    def implMolecularSequence1(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("breastcancer"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code),
            force_bytes("NM_000059.3"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].display),
            force_bytes("Homo sapiens BRCA2, DNA repair associated (BRCA2), mRNA"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system),
            force_bytes("http://www.ncbi.nlm.nih.gov/nuccore/"),
        )
        self.assertEqual(inst.referenceSeq.windowEnd, 101499444)
        self.assertEqual(inst.referenceSeq.windowStart, 101488058)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("rna"))
        self.assertEqual(inst.variant[0].end, 32316187)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("A"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("C"))
        self.assertEqual(inst.variant[0].start, 32316186)

    def testMolecularSequence2(self):
        inst = self.instantiate_from("sequence-graphic-example-1.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence2(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence2(inst2)

    def implMolecularSequence2(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("graphic-example-1"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code),
            force_bytes("NC_000002.12"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system),
            force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"),
        )
        self.assertEqual(force_bytes(inst.referenceSeq.strand), force_bytes("watson"))
        self.assertEqual(inst.referenceSeq.windowEnd, 128273732)
        self.assertEqual(inst.referenceSeq.windowStart, 128273724)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(force_bytes(inst.variant[0].cigar), force_bytes("1M"))
        self.assertEqual(inst.variant[0].end, 128273726)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("G"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("T"))
        self.assertEqual(inst.variant[0].start, 128273725)

    def testMolecularSequence3(self):
        inst = self.instantiate_from("sequence-example-fda-vcfeval.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence3(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence3(inst2)

    def implMolecularSequence3(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("fda-vcfeval-comparison"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.quality[0].end, 101770080)
        self.assertEqual(inst.quality[0].gtFP, 2186)
        self.assertEqual(
            force_bytes(inst.quality[0].method.coding[0].code),
            force_bytes("app-BxfGF8j02pBZzZxbzZxP725P"),
        )
        self.assertEqual(
            force_bytes(inst.quality[0].method.coding[0].system),
            force_bytes("https://precision.fda.gov/apps/"),
        )
        self.assertEqual(
            force_bytes(inst.quality[0].method.text),
            force_bytes("Vcfeval + Hap.py Comparison"),
        )
        self.assertEqual(inst.quality[0].precision, 0.428005)
        self.assertEqual(inst.quality[0].queryFP, 10670)
        self.assertEqual(inst.quality[0].recall, 0.752111)
        self.assertEqual(
            force_bytes(inst.quality[0].standardSequence.coding[0].code),
            force_bytes("file-BkZxBZ00bpJVk2q6x43b1YBx"),
        )
        self.assertEqual(
            force_bytes(inst.quality[0].standardSequence.coding[0].system),
            force_bytes("https://precision.fda.gov/files/"),
        )
        self.assertEqual(inst.quality[0].start, 10453)
        self.assertEqual(inst.quality[0].truthFN, 2554)
        self.assertEqual(inst.quality[0].truthTP, 7749)
        self.assertEqual(force_bytes(inst.quality[0].type), force_bytes("indel"))
        self.assertEqual(inst.quality[1].end, 101770080)
        self.assertEqual(inst.quality[1].gtFP, 493)
        self.assertEqual(
            force_bytes(inst.quality[1].method.coding[0].code),
            force_bytes("app-BxfGF8j02pBZzZxbzZxP725P"),
        )
        self.assertEqual(
            force_bytes(inst.quality[1].method.coding[0].system),
            force_bytes("https://precision.fda.gov/apps/"),
        )
        self.assertEqual(
            force_bytes(inst.quality[1].method.text),
            force_bytes("Vcfeval + Hap.py Comparison"),
        )
        self.assertEqual(inst.quality[1].precision, 0.808602)
        self.assertEqual(inst.quality[1].queryFP, 21744)
        self.assertEqual(inst.quality[1].recall, 0.986642)
        self.assertEqual(
            force_bytes(inst.quality[1].standardSequence.coding[0].code),
            force_bytes("file-BkZxBZ00bpJVk2q6x43b1YBx"),
        )
        self.assertEqual(
            force_bytes(inst.quality[1].standardSequence.coding[0].system),
            force_bytes("https://precision.fda.gov/files/"),
        )
        self.assertEqual(inst.quality[1].start, 10453)
        self.assertEqual(inst.quality[1].truthFN, 1247)
        self.assertEqual(inst.quality[1].truthTP, 92106)
        self.assertEqual(force_bytes(inst.quality[1].type), force_bytes("snp"))
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code),
            force_bytes("NC_000001.11"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system),
            force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"),
        )
        self.assertEqual(force_bytes(inst.referenceSeq.strand), force_bytes("watson"))
        self.assertEqual(inst.referenceSeq.windowEnd, 101770080)
        self.assertEqual(inst.referenceSeq.windowStart, 10453)
        self.assertEqual(force_bytes(inst.repository[0].name), force_bytes("FDA"))
        self.assertEqual(force_bytes(inst.repository[0].type), force_bytes("login"))
        self.assertEqual(
            force_bytes(inst.repository[0].url),
            force_bytes("https://precision.fda.gov/jobs/job-ByxYPx809jFVy21KJG74Jg3Y"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(inst.variant[0].end, 13117)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("T"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("G"))
        self.assertEqual(inst.variant[0].start, 13116)

    def testMolecularSequence4(self):
        inst = self.instantiate_from("sequence-complex-variant.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence4(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence4(inst2)

    def implMolecularSequence4(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("sequence-complex-variant"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.quantity.value, 25)
        self.assertEqual(inst.readCoverage, 1)
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code),
            force_bytes("NC_000002.12"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system),
            force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"),
        )
        self.assertEqual(force_bytes(inst.referenceSeq.strand), force_bytes("watson"))
        self.assertEqual(inst.referenceSeq.windowEnd, 128273754)
        self.assertEqual(inst.referenceSeq.windowStart, 128273724)
        self.assertEqual(
            force_bytes(inst.repository[0].datasetId), force_bytes("Ensembl")
        )
        self.assertEqual(
            force_bytes(inst.repository[0].readsetId), force_bytes("v1beta2")
        )
        self.assertEqual(force_bytes(inst.repository[0].type), force_bytes("other"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(force_bytes(inst.variant[0].cigar), force_bytes("3M1D4M6N2M"))
        self.assertEqual(inst.variant[0].end, 128273736)
        self.assertEqual(
            force_bytes(inst.variant[0].observedAllele), force_bytes("CTCATTGT")
        )
        self.assertEqual(
            force_bytes(inst.variant[0].referenceAllele),
            force_bytes("CTCCATTGCATGCGTT"),
        )
        self.assertEqual(inst.variant[0].start, 128273724)

    def testMolecularSequence5(self):
        inst = self.instantiate_from("sequence-example-TPMT-one.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence5(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence5(inst2)

    def implMolecularSequence5(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("example-TPMT-one"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.observedSeq), force_bytes("T-C-C-C-A-C-C-C"))
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code),
            force_bytes("NT_007592.15"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system),
            force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"),
        )
        self.assertEqual(force_bytes(inst.referenceSeq.strand), force_bytes("watson"))
        self.assertEqual(inst.referenceSeq.windowEnd, 18143955)
        self.assertEqual(inst.referenceSeq.windowStart, 18130918)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(inst.variant[0].end, 18139214)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("A"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("G"))
        self.assertEqual(inst.variant[0].start, 18139214)

    def testMolecularSequence6(self):
        inst = self.instantiate_from("sequence-example-pgx-2.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence6(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence6(inst2)

    def implMolecularSequence6(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("example-pgx-2"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.orientation), force_bytes("sense")
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code),
            force_bytes("NG_007726.3"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system),
            force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"),
        )
        self.assertEqual(force_bytes(inst.referenceSeq.strand), force_bytes("watson"))
        self.assertEqual(inst.referenceSeq.windowEnd, 55227980)
        self.assertEqual(inst.referenceSeq.windowStart, 55227970)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(inst.variant[0].end, 55227979)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("G"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("T"))
        self.assertEqual(inst.variant[0].start, 55227978)

    def testMolecularSequence7(self):
        inst = self.instantiate_from("molecularsequence-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence7(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence7(inst2)

    def implMolecularSequence7(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code),
            force_bytes("NC_000009.11"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system),
            force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"),
        )
        self.assertEqual(force_bytes(inst.referenceSeq.strand), force_bytes("watson"))
        self.assertEqual(inst.referenceSeq.windowEnd, 22125510)
        self.assertEqual(inst.referenceSeq.windowStart, 22125500)
        self.assertEqual(force_bytes(inst.repository[0].name), force_bytes("GA4GH API"))
        self.assertEqual(force_bytes(inst.repository[0].type), force_bytes("openapi"))
        self.assertEqual(
            force_bytes(inst.repository[0].url),
            force_bytes(
                "http://grch37.rest.ensembl.org/ga4gh/variants/3:rs1333049?content-type=application/json"
            ),
        )
        self.assertEqual(
            force_bytes(inst.repository[0].variantsetId), force_bytes("3:rs1333049")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(inst.variant[0].end, 22125504)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("C"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("G"))
        self.assertEqual(inst.variant[0].start, 22125503)

    def testMolecularSequence8(self):
        inst = self.instantiate_from("sequence-example-fda.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence8(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence8(inst2)

    def implMolecularSequence8(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("fda-example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.quality[0].end, 101770080)
        self.assertEqual(inst.quality[0].fScore, 0.545551)
        self.assertEqual(inst.quality[0].gtFP, 2186)
        self.assertEqual(
            force_bytes(inst.quality[0].method.coding[0].code),
            force_bytes("job-ByxYPx809jFVy21KJG74Jg3Y"),
        )
        self.assertEqual(
            force_bytes(inst.quality[0].method.coding[0].system),
            force_bytes("https://precision.fda.gov/jobs/"),
        )
        self.assertEqual(
            force_bytes(inst.quality[0].method.text),
            force_bytes("Vcfeval + Hap.py Comparison"),
        )
        self.assertEqual(inst.quality[0].precision, 0.428005)
        self.assertEqual(inst.quality[0].queryFP, 10670)
        self.assertEqual(inst.quality[0].queryTP, 7984)
        self.assertEqual(inst.quality[0].recall, 0.752111)
        self.assertEqual(
            force_bytes(inst.quality[0].standardSequence.coding[0].code),
            force_bytes("file-Bk50V4Q0qVb65P0v2VPbfYPZ"),
        )
        self.assertEqual(
            force_bytes(inst.quality[0].standardSequence.coding[0].system),
            force_bytes("https://precision.fda.gov/files/"),
        )
        self.assertEqual(inst.quality[0].start, 10453)
        self.assertEqual(inst.quality[0].truthFN, 2554)
        self.assertEqual(inst.quality[0].truthTP, 7749)
        self.assertEqual(force_bytes(inst.quality[0].type), force_bytes("snp"))
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code),
            force_bytes("NC_000001.11"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system),
            force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"),
        )
        self.assertEqual(force_bytes(inst.referenceSeq.strand), force_bytes("watson"))
        self.assertEqual(inst.referenceSeq.windowEnd, 101770080)
        self.assertEqual(inst.referenceSeq.windowStart, 10453)
        self.assertEqual(force_bytes(inst.repository[0].name), force_bytes("FDA"))
        self.assertEqual(force_bytes(inst.repository[0].type), force_bytes("login"))
        self.assertEqual(
            force_bytes(inst.repository[0].url),
            force_bytes(
                "https://precision.fda.gov/files/file-Bx37ZK009P4bX5g3qjkFZV38"
            ),
        )
        self.assertEqual(
            force_bytes(inst.repository[0].variantsetId),
            force_bytes("file-Bx37ZK009P4bX5g3qjkFZV38"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(inst.variant[0].end, 13117)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("T"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("G"))
        self.assertEqual(inst.variant[0].start, 13116)

    def testMolecularSequence9(self):
        inst = self.instantiate_from("coord-1base-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence9(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence9(inst2)

    def implMolecularSequence9(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("coord-1-base"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.observedSeq), force_bytes("ACATGGTAGC"))
        self.assertEqual(
            force_bytes(inst.referenceSeq.referenceSeqString), force_bytes("ACGTAGTC")
        )
        self.assertEqual(force_bytes(inst.referenceSeq.strand), force_bytes("watson"))
        self.assertEqual(inst.referenceSeq.windowEnd, 8)
        self.assertEqual(inst.referenceSeq.windowStart, 1)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(force_bytes(inst.variant[0].cigar), force_bytes("3I"))
        self.assertEqual(inst.variant[0].end, 3)
        self.assertEqual(
            force_bytes(inst.variant[0].observedAllele), force_bytes("ATG")
        )
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("-"))
        self.assertEqual(inst.variant[0].start, 2)
        self.assertEqual(force_bytes(inst.variant[1].cigar), force_bytes("3I"))
        self.assertEqual(inst.variant[1].end, 5)
        self.assertEqual(force_bytes(inst.variant[1].observedAllele), force_bytes("T"))
        self.assertEqual(force_bytes(inst.variant[1].referenceAllele), force_bytes("A"))
        self.assertEqual(inst.variant[1].start, 5)
        self.assertEqual(force_bytes(inst.variant[2].cigar), force_bytes("1D"))
        self.assertEqual(inst.variant[2].end, 7)
        self.assertEqual(force_bytes(inst.variant[2].observedAllele), force_bytes("-"))
        self.assertEqual(force_bytes(inst.variant[2].referenceAllele), force_bytes("T"))
        self.assertEqual(inst.variant[2].start, 7)

    def testMolecularSequence10(self):
        inst = self.instantiate_from("sequence-graphic-example-4.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a MolecularSequence instance"
        )
        self.implMolecularSequence10(inst)

        js = inst.as_json()
        self.assertEqual("MolecularSequence", js["resourceType"])
        inst2 = molecularsequence.MolecularSequence(js)
        self.implMolecularSequence10(inst2)

    def implMolecularSequence10(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("graphic-example-4"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.chromosome.coding[0].code), force_bytes("2")
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.chromosome.coding[0].display),
            force_bytes("chromosome 2"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.chromosome.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/chromosome-human"),
        )
        self.assertEqual(
            force_bytes(inst.referenceSeq.genomeBuild), force_bytes("GRCh 38")
        )
        self.assertEqual(force_bytes(inst.referenceSeq.strand), force_bytes("watson"))
        self.assertEqual(inst.referenceSeq.windowEnd, 128273740)
        self.assertEqual(inst.referenceSeq.windowStart, 128273736)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
