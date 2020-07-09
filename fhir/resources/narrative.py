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
        ...,
        alias="div",
        title="Limited xhtml content",
        description="The actual narrative content, a stripped down version of XHTML.",
        # if property is element of this resource.
        element_property=True,
    )
    div__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_div", title="Extension field for ``div``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="generated | extensions | additional | empty",
        description=(
            "The status of the narrative - whether it's entirely generated (from "
            "just the defined data or the extensions too), or whether a human "
            "authored it and it may contain additional data."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["generated", "extensions", "additional", "empty"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )
