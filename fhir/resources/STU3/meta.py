# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Meta
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import element, fhirtypes


class Meta(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Metadata about a resource.
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not always be
    associated with version changes to the resource.
    """

    resource_type = Field("Meta", const=True)

    lastUpdated: fhirtypes.Instant = Field(
        None,
        alias="lastUpdated",
        title="Type `Instant`",
        description="When the resource version last changed",
    )
    lastUpdated__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastUpdated", title="Extension field for ``lastUpdated``."
    )

    profile: ListType[fhirtypes.Uri] = Field(
        None,
        alias="profile",
        title="List of `Uri` items",
        description="Profiles this resource claims to conform to",
    )
    profile__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_profile", title="Extension field for ``profile``."
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
        title="Type `Id`",
        description="Version specific identifier",
    )
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versionId", title="Extension field for ``versionId``."
    )
