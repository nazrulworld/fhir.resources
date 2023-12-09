# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic.v1 import Field

from . import fhirtypes
from .resource import Resource


class Binary(Resource):
    """Pure binary content defined by some other format than FHIR.

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
