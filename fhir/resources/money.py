from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Money
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic import Field

from . import datatype, fhirtypes


class Money(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An amount of economic utility in some recognized currency.
    """

    __resource_type__ = "Money"

    currency: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="currency",
        title="ISO 4217 Currency Code",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    currency__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_currency", title="Extension field for ``currency``."
    )

    value: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Numerical value (with implicit precision)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Money`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "currency"]
