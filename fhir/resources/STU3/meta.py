# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Meta
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field

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

    resource_type = Field("Meta", const=True)

    lastUpdated: fhirtypes.Instant = Field(
        None,
        alias="lastUpdated",
        title="When the resource version last changed",
        description="When the resource last changed - e.g. when the version changed.",
        # if property is element of this resource.
        element_property=True,
    )
    lastUpdated__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastUpdated", title="Extension field for ``lastUpdated``."
    )

    profile: typing.List[fhirtypes.Uri] = Field(
        None,
        alias="profile",
        title="Profiles this resource claims to conform to",
        description=(
            "A list of profiles (references to "
            "[StructureDefinition](structuredefinition.html#) resources) that this "
            "resource claims to conform to. The URL is a reference to "
            "[StructureDefinition.url]()."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    profile__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_profile", title="Extension field for ``profile``.")

    security: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="security",
        title="Security Labels applied to this resource",
        description=(
            "Security labels applied to this resource. These tags connect specific "
            "resources to the overall security policy and infrastructure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    tag: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="tag",
        title="Tags applied to this resource",
        description=(
            "Tags applied to this resource. Tags are intended to be used to "
            "identify and relate resources to process and workflow, and "
            "applications are not required to consider the tags when interpreting "
            "the meaning of a resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    versionId: fhirtypes.Id = Field(
        None,
        alias="versionId",
        title="Version specific identifier",
        description=(
            "The version specific identifier, as it appears in the version portion "
            "of the URL. This values changes when the resource is created, updated,"
            " or deleted."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
