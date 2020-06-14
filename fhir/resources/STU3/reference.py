# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Reference
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Reference(element.Element):
    """ A reference from one resource to another.
    """

    resource_type = Field("Reference", const=True)

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String` (represented as `dict` in JSON)",
        description="Text alternative for the resource",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Logical reference, when literal reference is not known",
    )

    reference: fhirtypes.String = Field(
        None,
        alias="reference",
        title="Type `String` (represented as `dict` in JSON)",
        description="Literal reference, Relative, internal or absolute URL",
    )
