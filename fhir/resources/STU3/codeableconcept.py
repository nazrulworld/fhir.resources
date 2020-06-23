# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeableConcept
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import element, fhirtypes


class CodeableConcept(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Concept - reference to a terminology or just  text.
    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    """

    resource_type = Field("CodeableConcept", const=True)

    coding: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="coding",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Code defined by a terminology system",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String`",
        description="Plain text representation of the concept",
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )
