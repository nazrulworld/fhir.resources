from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import fhirtypes, resource


class Binary(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Pure binary content defined by a format other than FHIR.
    A binary resource can contain any content, whether text, image, pdf, zip
    archive, etc.
    """

    __resource_type__ = "Binary"

    content: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="content",
        title="The actual content",
        description="The actual content, base64 encoded.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    content__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_content", title="Extension field for ``content``."
    )

    contentType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="contentType",
        title="MimeType of the binary content",
        description=(
            "MimeType of the binary content represented as a standard MimeType (BCP"
            " 13)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    securityContext: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="securityContext",
        title="Access Control Management",
        description=(
            "Treat this binary as if it was this other resource for access control "
            "purposes."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Binary`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "contentType",
            "securityContext",
            "content",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("content", "content__ext"),
            ("contentType", "contentType__ext"),
        ]
        return required_fields
