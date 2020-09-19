# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Quantity
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic import Field

from . import fhirtypes
from .element import Element


class Quantity(Element):
    """A measured or measurable amount.

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
        description="< | <= | >= | > - how to understand the value.",
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
