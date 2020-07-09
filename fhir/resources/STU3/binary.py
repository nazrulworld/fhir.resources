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
        title="The actual content",
        description="The actual content, base64 encoded.",
        # if property is element of this resource.
        element_property=True,
    )
    content__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_content", title="Extension field for ``content``."
    )

    contentType: fhirtypes.Code = Field(
        ...,
        alias="contentType",
        title="MimeType of the binary content",
        description=(
            "MimeType of the binary content represented as a standard MimeType (BCP"
            " 13)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    securityContext: fhirtypes.ReferenceType = Field(
        None,
        alias="securityContext",
        title="Access Control Management",
        description=(
            "Treat this binary as if it was this other resource for access control "
            "purposes."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
