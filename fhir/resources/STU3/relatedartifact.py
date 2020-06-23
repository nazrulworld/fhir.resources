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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related artifacts for a knowledge resource.
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    resource_type = Field("RelatedArtifact", const=True)

    citation: fhirtypes.String = Field(
        None,
        alias="citation",
        title="Type `String`",
        description="Bibliographic citation for the artifact",
    )
    citation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_citation", title="Extension field for ``citation``."
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Type `String`",
        description="Brief description of the related artifact",
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
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
        title="Type `Code`",
        description=(
            "documentation | justification | citation | predecessor | successor | "
            "derived-from | depends-on | composed-of"
        ),
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Where the artifact can be accessed",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )
