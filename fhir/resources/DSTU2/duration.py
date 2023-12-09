# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Duration
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic.v1 import Field

from .quantity import Quantity


class Duration(Quantity):
    """A length of time.
    There SHALL be a code if there is a value and it SHALL be an expression of
    time.  If system is present, it SHALL be UCUM.
    """

    resource_type = Field("Duration", const=True)
