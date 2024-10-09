from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeableConcept
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class CodeableConcept(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Concept - reference to a terminology or just  text.
    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    """

    __resource_type__ = "CodeableConcept"

    coding: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="coding",
        title="Code defined by a terminology system",
        description="A reference to a code defined by a terminology system.",
        json_schema_extra={
            "element_property": True,
        },
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Plain text representation of the concept",
        description=(
            "A human language representation of the concept as "
            "seen/selected/uttered by the user who entered the data and/or which "
            "represents the intended meaning of the user."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CodeableConcept`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "coding", "text"]
