# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Identifier
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Identifier(element.Element):
    """ An identifier intended for computation.
    A technical identifier - identifies some entity uniquely and unambiguously.
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
        description="usual | official | temp | secondary (If known)",
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="The value that is unique",
    )
