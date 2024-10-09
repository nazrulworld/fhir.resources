from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import fhirtypes, resource


class Binary(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Pure binary content defined by a format other than FHIR.
    A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
    """

    __resource_type__ = "Binary"

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

    data: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="data",
        title="The actual content",
        description="The actual content, base64 encoded.",
        json_schema_extra={
            "element_property": True,
        },
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_data", title="Extension field for ``data``."
    )

    securityContext: fhirtypes.ReferenceType | None = Field(  # type: ignore
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
            "data",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("contentType", "contentType__ext")]
        return required_fields
