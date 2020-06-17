# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Narrative
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from pydantic import Field

from . import fhirtypes
from .element import Element


class Narrative(Element):
    """ A human-readable formatted text, including images.
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
