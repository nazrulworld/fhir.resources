from __future__ import annotations as _annotations

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
