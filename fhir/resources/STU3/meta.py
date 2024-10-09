from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Meta
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class Meta(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Metadata about a resource.
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not always be
    associated with version changes to the resource.
    """

    __resource_type__ = "Meta"

    lastUpdated: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="lastUpdated",
        title="When the resource version last changed",
        description="When the resource last changed - e.g. when the version changed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    lastUpdated__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lastUpdated", title="Extension field for ``lastUpdated``."
    )

    profile: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="profile",
        title="Profiles this resource claims to conform to",
        description=(
            "A list of profiles (references to "
            "[StructureDefinition](structuredefinition.html#) resources) that this "
            "resource claims to conform to. The URL is a reference to "
            "[StructureDefinition.url]()."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    profile__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_profile", title="Extension field for ``profile``."
    )

    security: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="security",
        title="Security Labels applied to this resource",
        description=(
            "Security labels applied to this resource. These tags connect specific "
            "resources to the overall security policy and infrastructure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    tag: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="tag",
        title="Tags applied to this resource",
        description=(
            "Tags applied to this resource. Tags are intended to be used to "
            "identify and relate resources to process and workflow, and "
            "applications are not required to consider the tags when interpreting "
            "the meaning of a resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    versionId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="versionId",
        title="Version specific identifier",
        description=(
            "The version specific identifier, as it appears in the version portion "
            "of the URL. This values changes when the resource is created, updated,"
            " or deleted."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_versionId", title="Extension field for ``versionId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Meta`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "versionId",
            "lastUpdated",
            "profile",
            "security",
            "tag",
        ]
