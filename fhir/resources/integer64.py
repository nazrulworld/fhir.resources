from __future__ import annotations as _annotations

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

    __resource_type__ = "integer64"

    value: fhirtypes.Integer64Type | None = Field(  # type: ignore
        default=None,
        alias="value",
        title="Primitive value for integer64",
        description="Primitive value for integer64",
        json_schema_extra={
            "element_property": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Integer64`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "value"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Integer64`` according to specification,
        with preserving the original sequence order.
        """
        return []
