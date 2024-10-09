from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Attachment
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Attachment(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Content in a format defined elsewhere.
    For referring to data content defined in other formats.
    """

    __resource_type__ = "Attachment"

    contentType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="contentType",
        title="Mime type of the content, with charset etc.",
        description=(
            "Identifies the type of the data in the attachment and allows a method "
            "to be chosen to interpret or render the data. Includes mime type "
            "parameters such as charset where appropriate."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    creation: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="creation",
        title="Date attachment was first created",
        description="The date that the attachment was first created.",
        json_schema_extra={
            "element_property": True,
        },
    )
    creation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_creation", title="Extension field for ``creation``."
    )

    data: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="data",
        title="Data inline, base64ed",
        description=(
            "The actual data of the attachment - a sequence of bytes. In XML, "
            "represented using base64."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_data", title="Extension field for ``data``."
    )

    hash: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="hash",
        title="Hash of the data (sha-1, base64ed)",
        description="The calculated hash of the data using SHA-1. Represented using base64.",
        json_schema_extra={
            "element_property": True,
        },
    )
    hash__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_hash", title="Extension field for ``hash``."
    )

    language: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="language",
        title="Human language of the content (BCP-47)",
        description=(
            "The human language of the content. The value can be any valid value "
            "according to BCP 47."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_language", title="Extension field for ``language``."
    )

    size: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="size",
        title="Number of bytes of content (if url provided)",
        description=(
            "The number of bytes of data that make up this attachment (before "
            "base64 encoding, if that is done)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    size__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_size", title="Extension field for ``size``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Label to display in place of the data",
        description="A label or set of text to display in place of the data.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Uri where the data can be found",
        description="An alternative location where the data can be accessed.",
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
        ``Attachment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "contentType",
            "language",
            "data",
            "url",
            "size",
            "hash",
            "title",
            "creation",
        ]
