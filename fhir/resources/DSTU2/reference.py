# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Reference
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic import Field

from . import fhirtypes
from .element import Element


class Reference(Element):
    """A reference from one resource to another."""

    resource_type = Field("Reference", const=True)

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String` (represented as `dict` in JSON)",
        description="Text alternative for the resource",
    )
    reference: fhirtypes.String = Field(
        None,
        alias="reference",
        title="Type `String` (represented as `dict` in JSON)",
        description="Literal reference, Relative, internal or absolute URL",
    )
