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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Human-readable summary of the resource (essential clinical and business
    information).
    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """

    resource_type = Field("Narrative", const=True)

    div: fhirtypes.Xhtml = Field(
        ..., alias="div", title="Type `Xhtml`", description="Limited xhtml content"
    )
    div__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_div", title="Extension field for ``div``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="generated | extensions | additional | empty",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )
