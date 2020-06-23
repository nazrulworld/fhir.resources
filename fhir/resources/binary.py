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
        title="Type `Code`",
        description="MimeType of the binary content",
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    data: fhirtypes.Base64Binary = Field(
        None,
        alias="data",
        title="Type `Base64Binary`",
        description="The actual content",
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_data", title="Extension field for ``data``."
    )

    securityContext: fhirtypes.ReferenceType = Field(
        None,
        alias="securityContext",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description=(
            "Identifies another resource to use as proxy when enforcing access "
            "control"
        ),
    )
