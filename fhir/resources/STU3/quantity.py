# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SimpleQuantity
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Quantity(element.Element):
    """ A measured or measurable amount.
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """

    resource_type = Field("Quantity", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Coded form of the unit",
    )

    comparator: fhirtypes.Code = Field(
        None,
        alias="comparator",
        title="Type `Code` (represented as `dict` in JSON)",
        description="\u003c | \u003c= | \u003e= | \u003e - how to understand the value",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="System that defines coded unit form",
    )

    unit: fhirtypes.String = Field(
        None,
        alias="unit",
        title="Type `String` (represented as `dict` in JSON)",
        description="Unit representation",
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Numerical value (with implicit precision)",
    )
