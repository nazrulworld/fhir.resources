# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Reference
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
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

    type: fhirtypes.Uri = Field(
        None,
        alias="type",
        title="Type `Uri` (represented as `dict` in JSON)",
        description='Type the reference refers to (e.g. "Patient")',
    )
