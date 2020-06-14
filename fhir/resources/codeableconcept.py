# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeableConcept
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import element, fhirtypes


class CodeableConcept(element.Element):
    """ Concept - reference to a terminology or just  text.
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Plain text representation of the concept",
    )
