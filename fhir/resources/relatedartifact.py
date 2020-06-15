# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedArtifact
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class RelatedArtifact(element.Element):
    """ Related artifacts for a knowledge resource.
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    resource_type = Field("RelatedArtifact", const=True)

    citation: fhirtypes.Markdown = Field(
        None,
        alias="citation",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Bibliographic citation for the artifact",
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String` (represented as `dict` in JSON)",
        description="Brief description of the related artifact",
    )

    document: fhirtypes.AttachmentType = Field(
        None,
        alias="document",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="What document is being referenced",
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short label",
    )

    resource: fhirtypes.Canonical = Field(
        None,
        alias="resource",
        title=(
            "Type `Canonical` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="What resource is being referenced",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "documentation | justification | citation | predecessor | successor | "
            "derived-from | depends-on | composed-of"
        ),
    )

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="Type `Url` (represented as `dict` in JSON)",
        description="Where the artifact can be accessed",
    )
