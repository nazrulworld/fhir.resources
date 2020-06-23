# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Expression
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Expression(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An expression that can be used to generate a value.
    A expression that is evaluated in a specified context and returns a value.
    The context of use of the expression must specify the context in which the
    expression is evaluated, and how the result of the expression is used.
    """

    resource_type = Field("Expression", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Natural language description of the condition",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String`",
        description="Expression in specified language",
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    language: fhirtypes.Code = Field(
        ...,
        alias="language",
        title="Type `Code`",
        description="text/cql | text/fhirpath | application/x-fhir-query | etc.",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    name: fhirtypes.Id = Field(
        None,
        alias="name",
        title="Type `Id`",
        description="Short name assigned to expression for reuse",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    reference: fhirtypes.Uri = Field(
        None,
        alias="reference",
        title="Type `Uri`",
        description="Where the expression is found",
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reference", title="Extension field for ``reference``."
    )
