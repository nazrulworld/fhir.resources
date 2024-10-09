from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Signature
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class Signature(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A Signature - XML DigSig, JWS, Graphical image of signature, etc..
    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """

    __resource_type__ = "Signature"

    data: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="data",
        title="The actual signature content (XML DigSig. JWS, picture, etc.)",
        description=(
            "The base64 encoding of the Signature content. When signature is not "
            "recorded electronically this element would be empty."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_data", title="Extension field for ``data``."
    )

    onBehalfOf: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="onBehalfOf",
        title="The party represented",
        description=(
            "A reference to an application-usable description of the identity that "
            "is represented by the signature."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
                "Patient",
                "Device",
                "Organization",
            ],
        },
    )

    sigFormat: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="sigFormat",
        title="The technical format of the signature",
        description=(
            "A mime type that indicates the technical format of the signature. "
            "Important mime types are application/signature+xml for X ML DigSig, "
            "application/jose for JWS, and image/* for a graphical image of a "
            "signature, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    sigFormat__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sigFormat", title="Extension field for ``sigFormat``."
    )

    targetFormat: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="targetFormat",
        title="The technical format of the signed resources",
        description=(
            "A mime type that indicates the technical format of the target "
            "resources signed by the signature."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    targetFormat__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_targetFormat", title="Extension field for ``targetFormat``."
    )

    type: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Indication of the reason the entity signed the object(s)",
        description=(
            "An indication of the reason that the entity signed this document. This"
            " may be explicitly included as part of the signature information and "
            "can be used when determining accountability for various actions "
            "concerning the document."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    when: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="when",
        title="When the signature was created",
        description="When the digital signature was signed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    when__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_when", title="Extension field for ``when``."
    )

    who: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="who",
        title="Who signed",
        description=(
            "A reference to an application-usable description of the identity that "
            "signed  (e.g. the signature used their private key)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
                "Patient",
                "Device",
                "Organization",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Signature`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "type",
            "when",
            "who",
            "onBehalfOf",
            "targetFormat",
            "sigFormat",
            "data",
        ]
