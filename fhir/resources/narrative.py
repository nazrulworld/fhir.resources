# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Narrative
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Narrative(element.Element):
    """ Human-readable summary of the resource (essential clinical and business
    information).
    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """

    resource_type = Field("Narrative", const=True)

    div: fhirtypes.Xhtml = Field(
        ...,
        alias="div",
        title="Type `Xhtml` (represented as `dict` in JSON)",
        description="Limited xhtml content",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="generated | extensions | additional | empty",
    )
