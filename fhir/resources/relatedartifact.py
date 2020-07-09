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
        title="Bibliographic citation for the artifact",
        description=(
            "A bibliographic citation for the related artifact. This text SHOULD be"
            " formatted according to an accepted citation format."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    citation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_citation", title="Extension field for ``citation``."
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Brief description of the related artifact",
        description=(
            "A brief description of the document or knowledge resource being "
            "referenced, suitable for display to a consumer."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    document: fhirtypes.AttachmentType = Field(
        None,
        alias="document",
        title="What document is being referenced",
        description=(
            "The document being referenced, represented as an attachment. This is "
            "exclusive with the resource element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    label: fhirtypes.String = Field(
        None,
        alias="label",
        title="Short label",
        description=(
            "A short label that can be used to reference the citation from "
            "elsewhere in the containing artifact, such as a footnote index."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_label", title="Extension field for ``label``."
    )

    resource: fhirtypes.Canonical = Field(
        None,
        alias="resource",
        title="What resource is being referenced",
        description=(
            "The related resource, such as a library, value set, profile, or other "
            "knowledge resource."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title=(
            "documentation | justification | citation | predecessor | successor | "
            "derived-from | depends-on | composed-of"
        ),
        description="The type of relationship to the related artifact.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "documentation",
            "justification",
            "citation",
            "predecessor",
            "successor",
            "derived-from",
            "depends-on",
            "composed-of",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="Where the artifact can be accessed",
        description=(
            "A url for the artifact that can be followed to access the actual "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )
