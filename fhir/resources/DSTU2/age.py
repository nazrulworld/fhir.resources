# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Age
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from pydantic.v1 import Field

from .quantity import Quantity


class Age(Quantity):
    """A duration (length of time) with a UCUM code.

    There SHALL be a code if there is a value and it SHALL be an expression of
    time.  If system is present, it SHALL be UCUM.  If value is present, it
    SHALL be positive.
    """

    resource_type = Field("Age", const=True)
