# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Money
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Money(element.Element):
    """ An amount of economic utility in some recognized currency.
    """

    resource_type = Field("Money", const=True)

    currency: fhirtypes.Code = Field(
        None,
        alias="currency",
        title="Type `Code` (represented as `dict` in JSON)",
        description="ISO 4217 Currency Code",
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Numerical value (with implicit precision)",
    )
