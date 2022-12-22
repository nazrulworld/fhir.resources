# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Money
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import element, fhirtypes


class Money(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Money`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "currency"]
