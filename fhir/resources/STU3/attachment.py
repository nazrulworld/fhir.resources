# -*- coding: utf-8 -*-
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Content in a format defined elsewhere.
    For referring to data content defined in other formats.
    """

    resource_type = Field("Attachment", const=True)

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="Type `Code`",
        description="Mime type of the content, with charset etc.",
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    creation: fhirtypes.DateTime = Field(
        None,
        alias="creation",
        title="Type `DateTime`",
        description="Date attachment was first created",
    )
    creation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_creation", title="Extension field for ``creation``."
    )

    data: fhirtypes.Base64Binary = Field(
        None,
        alias="data",
        title="Type `Base64Binary`",
        description="Data inline, base64ed",
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_data", title="Extension field for ``data``."
    )

    hash: fhirtypes.Base64Binary = Field(
        None,
        alias="hash",
        title="Type `Base64Binary`",
        description="Hash of the data (sha-1, base64ed)",
    )
    hash__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_hash", title="Extension field for ``hash``."
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code`",
        description="Human language of the content (BCP-47)",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    size: fhirtypes.UnsignedInt = Field(
        None,
        alias="size",
        title="Type `UnsignedInt`",
        description="Number of bytes of content (if url provided)",
    )
    size__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_size", title="Extension field for ``size``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Label to display in place of the data",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Uri where the data can be found",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )
