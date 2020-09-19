# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Meta
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .element import Element


class Meta(Element):
    """Metadata about a resource.

    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not always be
    associated with version changes to the resource.
    """

    resource_type = Field("Meta", const=True)

    lastUpdated: fhirtypes.Instant = Field(
        None,
        alias="lastUpdated",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When the resource version last changed",
    )

    profile: ListType[fhirtypes.Uri] = Field(
        None,
        alias="profile",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Profiles this resource claims to conform to",
    )

    security: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="security",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Security Labels applied to this resource",
    )

    tag: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="tag",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Tags applied to this resource",
    )

    versionId: fhirtypes.Id = Field(
        None,
        alias="versionId",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Version specific identifier",
    )
