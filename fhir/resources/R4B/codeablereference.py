from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeableReference
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import element, fhirtypes


class CodeableReference(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Reference to a resource or a concept.
    A reference to a resource (by instance), or instead, a reference to a
    concept defined in a terminology or ontology (by class).
    """

    __resource_type__ = "CodeableReference"

    concept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="concept",
        title="Reference to a concept (by class)",
        description=(
            "A reference to a concept - e.g. the information is identified by its "
            "general class to the degree of precision found in the terminology."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Reference to a resource (by instance)",
        description=(
            "A reference to a resource the provides exact details about the "
            "information being referenced."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CodeableReference`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "concept", "reference"]
