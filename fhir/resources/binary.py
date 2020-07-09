# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import fhirtypes, resource


class Binary(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Pure binary content defined by a format other than FHIR.
    A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
    """

    resource_type = Field("Binary", const=True)

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

    data: fhirtypes.Base64Binary = Field(
        None,
        alias="data",
        title="The actual content",
        description="The actual content, base64 encoded.",
        # if property is element of this resource.
        element_property=True,
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_data", title="Extension field for ``data``."
    )

    securityContext: fhirtypes.ReferenceType = Field(
        None,
        alias="securityContext",
        title=(
            "Identifies another resource to use as proxy when enforcing access "
            "control"
        ),
        description=(
            "This element identifies another resource that can be used as a proxy "
            "of the security sensitivity to use when deciding and enforcing access "
            "control rules for the Binary resource. Given that the Binary resource "
            "contains very few elements that can be used to determine the "
            "sensitivity of the data and relationships to individuals, the "
            "referenced resource stands in as a proxy equivalent for this purpose. "
            "This referenced resource may be related to the Binary (e.g. Media, "
            "DocumentReference), or may be some non-related Resource purely as a "
            "security proxy. E.g. to identify that the binary resource relates to a"
            " patient, and access should only be granted to applications that have "
            "access to the patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
