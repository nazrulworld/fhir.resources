from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Narrative
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class Narrative(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Human-readable summary of the resource (essential clinical and business
    information).
    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """

    __resource_type__ = "Narrative"

    div: fhirtypes.XhtmlType | None = Field(  # type: ignore
        None,
        alias="div",
        title="Limited xhtml content",
        description="The actual narrative content, a stripped down version of XHTML.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    div__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_div", title="Extension field for ``div``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="generated | extensions | additional | empty",
        description=(
            "The status of the narrative - whether it's entirely generated (from "
            "just the defined data or the extensions too), or whether a human "
            "authored it and it may contain additional data."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["generated", "extensions", "additional", "empty"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Narrative`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "status", "div"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("div", "div__ext"), ("status", "status__ext")]
        return required_fields
