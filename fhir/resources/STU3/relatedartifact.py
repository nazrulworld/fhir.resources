# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedArtifact
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class RelatedArtifact(element.Element):
    """ Related artifacts for a knowledge resource.
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    resource_type = Field("RelatedArtifact", const=True)

    citation: fhirtypes.String = Field(
        None,
        alias="citation",
        title="Type `String` (represented as `dict` in JSON)",
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

    resource: fhirtypes.ReferenceType = Field(
        None,
        alias="resource",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
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

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Where the artifact can be accessed",
    )
