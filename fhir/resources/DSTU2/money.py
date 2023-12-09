# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Money
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic.v1 import Field

from .quantity import Quantity


class Money(Quantity):
    """An amount of money. With regard to precision, see [Decimal
    Precision](datatypes.html#precision).

    There SHALL be a code if there is a value and it SHALL be an expression of
    currency.  If system is present, it SHALL be ISO 4217 (system =
    "urn:iso:std:iso:4217" - currency).
    """

    resource_type = Field("Money", const=True)
