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
