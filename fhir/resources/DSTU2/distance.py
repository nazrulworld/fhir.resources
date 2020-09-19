# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Distance
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic import Field

from .quantity import Quantity


class Distance(Quantity):
    """A measure of distance.

    There SHALL be a code if there is a value and it SHALL be an expression of
    length.  If system is present, it SHALL be UCUM.
    """

    resource_type = Field("Distance", const=True)
