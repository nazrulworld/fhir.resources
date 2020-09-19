# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Attachment
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic import Field

from . import fhirtypes
from .element import Element


class Attachment(Element):
    """Content in a format defined elsewhere.

    For referring to data content defined in other formats.
    """

    resource_type = Field("Attachment", const=True)

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Mime type of the content, with charset etc.",
    )

    creation: fhirtypes.DateTime = Field(
        None,
        alias="creation",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date attachment was first created",
    )

    data: fhirtypes.Base64Binary = Field(
        None,
        alias="data",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="Data inline, base64ed",
    )

    hash: fhirtypes.Base64Binary = Field(
        None,
        alias="hash",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="Hash of the data (sha-1, base64ed)",
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Human language of the content (BCP-47)",
    )

    size: fhirtypes.UnsignedInt = Field(
        None,
        alias="size",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Number of bytes of content (if url provided)",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Label to display in place of the data",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Uri where the data can be found",
    )
