# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Meta
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class Meta(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Metadata about a resource.
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
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

    profile: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="profile",
        title="Profiles this resource claims to conform to",
        description=(
            "A list of profiles (references to "
            "[StructureDefinition](structuredefinition.html#) resources) that this "
            "resource claims to conform to. The URL is a reference to "
            "[StructureDefinition.url](structuredefinition-"
            "definitions.html#StructureDefinition.url)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
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

    source: fhirtypes.Uri = Field(
        None,
        alias="source",
        title="Identifies where the resource comes from",
        description=(
            "A uri that identifies the source system of the resource. This provides"
            " a minimal amount of [Provenance](provenance.html#) information that "
            "can be used to track or differentiate the source of information in the"
            " resource. The source may identify another FHIR server, document, "
            "message, database, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
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
            "of the URL. This value changes when the resource is created, updated, "
            "or deleted."
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
            "source",
            "profile",
            "security",
            "tag",
        ]
