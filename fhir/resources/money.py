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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An amount of economic utility in some recognized currency.
    """

    resource_type = Field("Money", const=True)

    currency: fhirtypes.Code = Field(
        None,
        alias="currency",
        title="ISO 4217 Currency Code",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    currency__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_currency", title="Extension field for ``currency``."
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Numerical value (with implicit precision)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )
