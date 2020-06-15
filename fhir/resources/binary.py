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
    """ Pure binary content defined by a format other than FHIR.
    A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
    """

    resource_type = Field("Binary", const=True)

    contentType: fhirtypes.Code = Field(
        ...,
        alias="contentType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="MimeType of the binary content",
    )

    data: fhirtypes.Base64Binary = Field(
        None,
        alias="data",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="The actual content",
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
