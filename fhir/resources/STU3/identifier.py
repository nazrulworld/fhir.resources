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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An identifier intended for computation.
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
        title="Type `Uri`",
        description="The namespace for the identifier value",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
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
        title="Type `Code`",
        description="usual | official | temp | secondary (If known)",
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String`",
        description="The value that is unique",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )
