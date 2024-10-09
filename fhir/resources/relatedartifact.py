from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedArtifact
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class RelatedArtifact(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related artifacts for a knowledge resource.
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    __resource_type__ = "RelatedArtifact"

    citation: fhirtypes.MarkdownType | None = Field(  # type: ignore
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

    classifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="classifier",
        title="Additional classifiers",
        description="Provides additional classifiers of the related artifact.",
        json_schema_extra={
            "element_property": True,
        },
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

    label: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="label",
        title="Short label",
        description=(
            "A short label that can be used to reference the citation from "
            "elsewhere in the containing artifact, such as a footnote index."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_label", title="Extension field for ``label``."
    )

    publicationDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="publicationDate",
        title="Date of publication of the artifact being referred to",
        description="The date of publication of the artifact being referred to.",
        json_schema_extra={
            "element_property": True,
        },
    )
    publicationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publicationDate", title="Extension field for ``publicationDate``."
    )

    publicationStatus: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="publicationStatus",
        title="draft | active | retired | unknown",
        description="The publication status of the artifact being referred to.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    publicationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_publicationStatus",
        title="Extension field for ``publicationStatus``.",
    )

    resource: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="resource",
        title="What artifact is being referenced",
        description=(
            "The related artifact, such as a library, value set, profile, or other "
            "knowledge resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_resource", title="Extension field for ``resource``."
    )

    resourceReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="resourceReference",
        title="What artifact, if not a conformance resource",
        description=(
            "The related artifact, if the artifact is not a canonical resource, or "
            "a resource reference to a canonical resource."
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
            "derived-from | depends-on | composed-of | part-of | amends | amended-"
            "with | appends | appended-with | cites | cited-by | comments-on | "
            "comment-in | contains | contained-in | corrects | correction-in | "
            "replaces | replaced-with | retracts | retracted-by | signs | similar-"
            "to | supports | supported-with | transforms | transformed-into | "
            "transformed-with | documents | specification-of | created-with | cite-"
            "as"
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
                "part-of",
                "amends",
                "amended-with",
                "appends",
                "appended-with",
                "cites",
                "cited-by",
                "comments-on",
                "comment-in",
                "contains",
                "contained-in",
                "corrects",
                "correction-in",
                "replaces",
                "replaced-with",
                "retracts",
                "retracted-by",
                "signs",
                "similar-to",
                "supports",
                "supported-with",
                "transforms",
                "transformed-into",
                "transformed-with",
                "documents",
                "specification-of",
                "created-with",
                "cite-as",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
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
            "classifier",
            "label",
            "display",
            "citation",
            "document",
            "resource",
            "resourceReference",
            "publicationStatus",
            "publicationDate",
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
