from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Expression
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic import Field

from . import datatype, fhirtypes


class Expression(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An expression that can be used to generate a value.
    A expression that is evaluated in a specified context and returns a value.
    The context of use of the expression must specify the context in which the
    expression is evaluated, and how the result of the expression is used.
    """

    __resource_type__ = "Expression"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Natural language description of the condition",
        description=(
            "A brief, natural language description of the condition that "
            "effectively communicates the intended semantics."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="expression",
        title="Expression in specified language",
        description="An expression in the specified language that returns a value.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_expression", title="Extension field for ``expression``."
    )

    language: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="language",
        title="text/cql | text/fhirpath | application/x-fhir-query | etc.",
        description="The media type of the language for the expression.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "text/cql",
                "text/fhirpath",
                "application/x-fhir-query",
                "etc.",
            ],
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_language", title="Extension field for ``language``."
    )

    name: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Short name assigned to expression for reuse",
        description=(
            "A short name assigned to the expression to allow for multiple reuse of"
            " the expression in the context where it is defined."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    reference: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="reference",
        title="Where the expression is found",
        description="A URI that defines where the expression is found.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_reference", title="Extension field for ``reference``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Expression`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "description",
            "name",
            "language",
            "expression",
            "reference",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Expression`` according to specification,
        with preserving the original sequence order.
        """
        return ["description", "name", "language", "expression", "reference"]
