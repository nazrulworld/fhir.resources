from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Expression
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class Expression(element.Element):
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
        None,
        alias="description",
        title="Natural language description of the condition",
        description=(
            "A brief, natural language description of the condition that "
            "effectively communicates the intended semantics."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="expression",
        title="Expression in specified language",
        description="An expression in the specified language that returns a value.",
        json_schema_extra={
            "element_property": True,
        },
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_expression", title="Extension field for ``expression``."
    )

    language: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="language",
        title=(
            "text/cql | text/fhirpath | application/x-fhir-query | text/cql-"
            "identifier | text/cql-expression | etc."
        ),
        description="The media type of the language for the expression.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "text/cql",
                "text/fhirpath",
                "application/x-fhir-query",
                "text/cql-identifier",
                "text/cql-expression",
                "etc.",
            ],
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_language", title="Extension field for ``language``."
    )

    name: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Short name assigned to expression for reuse",
        description=(
            "A short name assigned to the expression to allow for multiple reuse of"
            " the expression in the context where it is defined."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    reference: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Where the expression is found",
        description="A URI that defines where the expression is found.",
        json_schema_extra={
            "element_property": True,
        },
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_reference", title="Extension field for ``reference``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Expression`` according specification,
        with preserving original sequence order.
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("language", "language__ext")]
        return required_fields
