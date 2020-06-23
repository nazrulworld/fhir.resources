# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import fhirtypes, resource


class Binary(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Pure binary content defined by a format other than FHIR.
    A binary resource can contain any content, whether text, image, pdf, zip
    archive, etc.
    """

    resource_type = Field("Binary", const=True)

    content: fhirtypes.Base64Binary = Field(
        ...,
        alias="content",
        title="Type `Base64Binary`",
        description="The actual content",
    )
    content__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_content", title="Extension field for ``content``."
    )

    contentType: fhirtypes.Code = Field(
        ...,
        alias="contentType",
        title="Type `Code`",
        description="MimeType of the binary content",
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    securityContext: fhirtypes.ReferenceType = Field(
        None,
        alias="securityContext",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Access Control Management",
    )
