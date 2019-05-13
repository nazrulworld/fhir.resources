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
from .. import parameters
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ParametersTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Parameters", js["resourceType"])
        return parameters.Parameters(js)
    
    def testParameters1(self):
        inst = self.instantiate_from("parameters-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Parameters instance")
        self.implParameters1(inst)
        
        js = inst.as_json()
        self.assertEqual("Parameters", js["resourceType"])
        inst2 = parameters.Parameters(js)
        self.implParameters1(inst2)
    
    def implParameters1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.parameter[0].name), force_bytes("start"))
        self.assertEqual(inst.parameter[0].valueDate.date, FHIRDate("2010-01-01").date)
        self.assertEqual(inst.parameter[0].valueDate.as_json(), "2010-01-01")
        self.assertEqual(force_bytes(inst.parameter[1].name), force_bytes("end"))

