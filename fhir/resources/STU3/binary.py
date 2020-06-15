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
    """ Pure binary content defined by a format other than FHIR.
    A binary resource can contain any content, whether text, image, pdf, zip
    archive, etc.
    """

    resource_type = Field("Binary", const=True)

    content: fhirtypes.Base64Binary = Field(
        ...,
        alias="content",
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="The actual content",
    )

    contentType: fhirtypes.Code = Field(
        ...,
        alias="contentType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="MimeType of the binary content",
    )

    securityContext: fhirtypes.ReferenceType = Field(
        None,
        alias="securityContext",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Access Control Management",
    )
