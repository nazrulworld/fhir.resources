# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeableReference
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic import Field

from . import datatype, fhirtypes


class CodeableReference(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Reference to a resource or a concept.
    A reference to a resource (by instance), or instead, a reference to a
    concept defined in a terminology or ontology (by class).
    """

    resource_type = Field("CodeableReference", const=True)

    concept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="concept",
        title="Reference to a concept (by class)",
        description=(
            "A reference to a concept - e.g. the information is identified by its "
            "general class to the degree of precision found in the terminology."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reference: fhirtypes.ReferenceType = Field(
        None,
        alias="reference",
        title="Reference to a resource (by instance)",
        description=(
            "A reference to a resource the provides exact details about the "
            "information being referenced."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CodeableReference`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "concept", "reference"]
