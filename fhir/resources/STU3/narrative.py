# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Narrative
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Narrative(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A human-readable formatted text, including images.
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
