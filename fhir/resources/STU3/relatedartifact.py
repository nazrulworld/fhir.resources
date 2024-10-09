from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedArtifact
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class RelatedArtifact(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related artifacts for a knowledge resource.
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    __resource_type__ = "RelatedArtifact"

    citation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="citation",
        title="Bibliographic citation for the artifact",
        description=(
            "A bibliographic citation for the related artifact. This text SHOULD be"
            " formatted according to an accepted citation format."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    citation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_citation", title="Extension field for ``citation``."
    )

    display: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="display",
        title="Brief description of the related artifact",
        description=(
            "A brief description of the document or knowledge resource being "
            "referenced, suitable for display to a consumer."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_display", title="Extension field for ``display``."
    )

    document: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="document",
        title="What document is being referenced",
        description=(
            "The document being referenced, represented as an attachment. This is "
            "exclusive with the resource element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    resource: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="resource",
        title="What resource is being referenced",
        description=(
            "The related resource, such as a library, value set, profile, or other "
            "knowledge resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "documentation | justification | citation | predecessor | successor | "
            "derived-from | depends-on | composed-of"
        ),
        description="The type of relationship to the related artifact.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "documentation",
                "justification",
                "citation",
                "predecessor",
                "successor",
                "derived-from",
                "depends-on",
                "composed-of",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Where the artifact can be accessed",
        description=(
            "A url for the artifact that can be followed to access the actual "
            "content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RelatedArtifact`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "type",
            "display",
            "citation",
            "url",
            "document",
            "resource",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields
