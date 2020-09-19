# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Count
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic import Field

from .quantity import Quantity


class Count(Quantity):
    """A count of a discrete element (no unit).

    There SHALL be a code with a value of "1" if there is a value and it SHALL
    be an expression of length.  If system is present, it SHALL be UCUM.  If
    present, the value SHALL a whole number.
    """

    resource_type = Field("Count", const=True)
