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
from .. import sequence
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class SequenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Sequence", js["resourceType"])
        return sequence.Sequence(js)
    
    def testSequence1(self):
        inst = self.instantiate_from("coord-1base-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence1(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence1(inst2)
    
    def implSequence1(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("coord-1-base"))
        self.assertEqual(force_bytes(inst.observedSeq), force_bytes("ACATGGTAGC"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqString), force_bytes("ACGTAGTC"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 8)
        self.assertEqual(inst.referenceSeq.windowStart, 1)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(force_bytes(inst.variant[0].cigar), force_bytes("3I"))
        self.assertEqual(inst.variant[0].end, 3)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("ATG"))
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
    
    def testSequence2(self):
        inst = self.instantiate_from("sequence-graphic-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence2(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence2(inst2)
    
    def implSequence2(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("graphic-example-2"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqString), force_bytes("CGCCATTG"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 8)
        self.assertEqual(inst.referenceSeq.windowStart, 0)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
    
    def testSequence3(self):
        inst = self.instantiate_from("sequence-graphic-example-4.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence3(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence3(inst2)
    
    def implSequence3(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("graphic-example-4"))
        self.assertEqual(force_bytes(inst.referenceSeq.chromosome.coding[0].code), force_bytes("2"))
        self.assertEqual(force_bytes(inst.referenceSeq.chromosome.coding[0].display), force_bytes("chromosome 2"))
        self.assertEqual(force_bytes(inst.referenceSeq.chromosome.coding[0].system), force_bytes("http://hl7.org/fhir/chromosome-human"))
        self.assertEqual(force_bytes(inst.referenceSeq.genomeBuild), force_bytes("GRCh 38"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 128273740)
        self.assertEqual(inst.referenceSeq.windowStart, 128273736)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
    
    def testSequence4(self):
        inst = self.instantiate_from("sequence-graphic-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence4(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence4(inst2)
    
    def implSequence4(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("graphic-example-1"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code), force_bytes("NC_000002.12"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system), force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 128273732)
        self.assertEqual(inst.referenceSeq.windowStart, 128273724)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(force_bytes(inst.variant[0].cigar), force_bytes("1M"))
        self.assertEqual(inst.variant[0].end, 128273726)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("G"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("T"))
        self.assertEqual(inst.variant[0].start, 128273725)
    
    def testSequence5(self):
        inst = self.instantiate_from("sequence-example-TPMT-one.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence5(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence5(inst2)
    
    def implSequence5(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("example-TPMT-one"))
        self.assertEqual(force_bytes(inst.observedSeq), force_bytes("T-C-C-C-A-C-C-C"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code), force_bytes("NT_007592.15"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system), force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 18143955)
        self.assertEqual(inst.referenceSeq.windowStart, 18130918)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(inst.variant[0].end, 18139214)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("A"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("G"))
        self.assertEqual(inst.variant[0].start, 18139214)
    
    def testSequence6(self):
        inst = self.instantiate_from("sequence-graphic-example-3.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence6(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence6(inst2)
    
    def implSequence6(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("graphic-example-3"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 128273736)
        self.assertEqual(inst.referenceSeq.windowStart, 128273732)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(force_bytes(inst.variant[0].cigar), force_bytes("2M"))
        self.assertEqual(inst.variant[0].end, 128273736)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("GA"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("AT"))
        self.assertEqual(inst.variant[0].start, 1282737234)
    
    def testSequence7(self):
        inst = self.instantiate_from("sequence-graphic-example-5.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence7(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence7(inst2)
    
    def implSequence7(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("graphic-example-5"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code), force_bytes("NC_000002.12"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system), force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 128273736)
        self.assertEqual(inst.referenceSeq.windowStart, 128273732)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
    
    def testSequence8(self):
        inst = self.instantiate_from("sequence-example-fda-comparisons.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence8(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence8(inst2)
    
    def implSequence8(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("fda-vcf-comparison"))
        self.assertEqual(inst.quality[0].end, 101770080)
        self.assertEqual(inst.quality[0].fScore, 0.9823)
        self.assertEqual(inst.quality[0].gtFP, 2186)
        self.assertEqual(force_bytes(inst.quality[0].method.coding[0].code), force_bytes("app-BqB9XZ8006ZZ2g5KzGXP3fpq"))
        self.assertEqual(force_bytes(inst.quality[0].method.coding[0].system), force_bytes("https://precision.fda.gov/apps/"))
        self.assertEqual(force_bytes(inst.quality[0].method.text), force_bytes("VCF Comparison"))
        self.assertEqual(inst.quality[0].precision, 0.9885)
        self.assertEqual(inst.quality[0].queryFP, 1507)
        self.assertEqual(inst.quality[0].score.value, 5.0)
        self.assertEqual(force_bytes(inst.quality[0].standardSequence.coding[0].code), force_bytes("file-BkZxBZ00bpJVk2q6x43b1YBx"))
        self.assertEqual(force_bytes(inst.quality[0].standardSequence.coding[0].system), force_bytes("https://precision.fda.gov/files/"))
        self.assertEqual(inst.quality[0].start, 10453)
        self.assertEqual(inst.quality[0].truthFN, 3168)
        self.assertEqual(inst.quality[0].truthTP, 129481)
        self.assertEqual(force_bytes(inst.quality[0].type), force_bytes("unknown"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code), force_bytes("NC_000001.11"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system), force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 101770080)
        self.assertEqual(inst.referenceSeq.windowStart, 10453)
        self.assertEqual(force_bytes(inst.repository[0].name), force_bytes("FDA"))
        self.assertEqual(force_bytes(inst.repository[0].type), force_bytes("login"))
        self.assertEqual(force_bytes(inst.repository[0].url), force_bytes("https://precision.fda.gov/comparisons/1850"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(inst.variant[0].end, 13117)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("T"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("G"))
        self.assertEqual(inst.variant[0].start, 13116)
    
    def testSequence9(self):
        inst = self.instantiate_from("sequence-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence9(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence9(inst2)
    
    def implSequence9(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code), force_bytes("NC_000009.11"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system), force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 22125510)
        self.assertEqual(inst.referenceSeq.windowStart, 22125500)
        self.assertEqual(force_bytes(inst.repository[0].name), force_bytes("GA4GH API"))
        self.assertEqual(force_bytes(inst.repository[0].type), force_bytes("openapi"))
        self.assertEqual(force_bytes(inst.repository[0].url), force_bytes("http://grch37.rest.ensembl.org/ga4gh/variants/3:rs1333049?content-type=application/json"))
        self.assertEqual(force_bytes(inst.repository[0].variantsetId), force_bytes("3:rs1333049"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(inst.variant[0].end, 22125504)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("C"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("G"))
        self.assertEqual(inst.variant[0].start, 22125503)
    
    def testSequence10(self):
        inst = self.instantiate_from("sequence-example-pgx-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence10(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence10(inst2)
    
    def implSequence10(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("example-pgx-1"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].code), force_bytes("NG_007726.3"))
        self.assertEqual(force_bytes(inst.referenceSeq.referenceSeqId.coding[0].system), force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"))
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 55227980)
        self.assertEqual(inst.referenceSeq.windowStart, 55227970)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("dna"))
        self.assertEqual(inst.variant[0].end, 55227977)
        self.assertEqual(force_bytes(inst.variant[0].observedAllele), force_bytes("G"))
        self.assertEqual(force_bytes(inst.variant[0].referenceAllele), force_bytes("T"))
        self.assertEqual(inst.variant[0].start, 55227976)

