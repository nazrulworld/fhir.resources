# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Meta
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import element, fhirtypes


class Meta(element.Element):
    """ Metadata about a resource.
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """

    resource_type = Field("Meta", const=True)

    lastUpdated: fhirtypes.Instant = Field(
        None,
        alias="lastUpdated",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When the resource version last changed",
    )

    profile: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="profile",
        title=(
            "List of `Canonical` items referencing `StructureDefinition` "
            "(represented as `dict` in JSON)"
        ),
        description="Profiles this resource claims to conform to",
    )

    security: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="security",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Security Labels applied to this resource",
    )

    source: fhirtypes.Uri = Field(
        None,
        alias="source",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Identifies where the resource comes from",
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
