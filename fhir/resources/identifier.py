# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Identifier
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Identifier(element.Element):
    """ An identifier intended for computation.
    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """

    resource_type = Field("Identifier", const=True)

    assigner: fhirtypes.ReferenceType = Field(
        None,
        alias="assigner",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization that issued id (may be just text)",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period when id is/was valid for use",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="The namespace for the identifier value",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Description of identifier",
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="usual | official | temp | secondary | old (If known)",
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="The value that is unique",
    )
