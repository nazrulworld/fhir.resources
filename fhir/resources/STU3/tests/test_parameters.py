# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Parameters
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

from .. import parameters
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ParametersTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
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
