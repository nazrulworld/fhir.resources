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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related artifacts for a knowledge resource.
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    resource_type = Field("RelatedArtifact", const=True)

    citation: fhirtypes.Markdown = Field(
        None,
        alias="citation",
        title="Type `Markdown`",
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

    label: fhirtypes.String = Field(
        None, alias="label", title="Type `String`", description="Short label"
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    resource: fhirtypes.Canonical = Field(
        None,
        alias="resource",
        title="Type `Canonical` referencing `Resource`",
        description="What resource is being referenced",
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
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

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="Type `Url`",
        description="Where the artifact can be accessed",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )
