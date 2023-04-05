# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/integer64
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic import Field

from . import fhirtypes, primitivetype


class Integer64(primitivetype.PrimitiveType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Primitive Type integer64.
    A very large whole number
    """

    resource_type = Field("integer64", const=True)

    value: fhirtypes.Integer64 = Field(
        None,
        alias="value",
        title="Primitive value for integer64",
        description="Primitive value for integer64",
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Integer64`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value"]
