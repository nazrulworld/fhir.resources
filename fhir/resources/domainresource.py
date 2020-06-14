# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DomainResource
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes, resource


class DomainResource(resource.Resource):
    """ A resource with narrative, extensions, and contained resources.
    A resource that includes narrative, extensions, and contained resources.
    """

    resource_type = Field("DomainResource", const=True)

    contained: ListType[fhirtypes.ResourceType] = Field(
        None,
        alias="contained",
        title="List of `Resource` items (represented as `dict` in JSON)",
        description="Contained, inline Resources",
    )

    extension: ListType[fhirtypes.ExtensionType] = Field(
        None,
        alias="extension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Additional content defined by implementations",
    )

    modifierExtension: ListType[fhirtypes.ExtensionType] = Field(
        None,
        alias="modifierExtension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Extensions that cannot be ignored",
    )

    text: fhirtypes.NarrativeType = Field(
        None,
        alias="text",
        title="Type `Narrative` (represented as `dict` in JSON)",
        description="Text summary of the resource, for human interpretation",
    )
