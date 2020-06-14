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
    """ An expression that can be used to generate a value.
    A expression that is evaluated in a specified context and returns a value.
    The context of use of the expression must specify the context in which the
    expression is evaluated, and how the result of the expression is used.
    """

    resource_type = Field("Expression", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Natural language description of the condition",
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String` (represented as `dict` in JSON)",
        description="Expression in specified language",
    )

    language: fhirtypes.Code = Field(
        ...,
        alias="language",
        title="Type `Code` (represented as `dict` in JSON)",
        description="text/cql | text/fhirpath | application/x-fhir-query | etc.",
    )

    name: fhirtypes.Id = Field(
        None,
        alias="name",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Short name assigned to expression for reuse",
    )

    reference: fhirtypes.Uri = Field(
        None,
        alias="reference",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Where the expression is found",
    )
