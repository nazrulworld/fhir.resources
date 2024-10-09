from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Signature
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class Signature(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..
    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different signature
    approaches have different utilities.
    """

    __resource_type__ = "Signature"

    blob: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        None,
        alias="blob",
        title="The actual signature content (XML DigSig. JWT, picture, etc.)",
        description=(
            "The base64 encoding of the Signature content. When signature is not "
            "recorded electronically this element would be empty."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    blob__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_blob", title="Extension field for ``blob``."
    )

    contentType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="contentType",
        title="The technical format of the signature",
        description=(
            "A mime type that indicates the technical format of the signature. "
            "Important mime types are application/signature+xml for X ML DigSig, "
            "application/jwt for JWT, and image/* for a graphical image of a "
            "signature, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    onBehalfOfReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="onBehalfOfReference",
        title="The party represented",
        description=(
            "A reference to an application-usable description of the identity that "
            "is represented by the signature."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onBehalfOf[x]
            "one_of_many": "onBehalfOf",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "RelatedPerson",
                "Patient",
                "Device",
                "Organization",
            ],
        },
    )

    onBehalfOfUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="onBehalfOfUri",
        title="The party represented",
        description=(
            "A reference to an application-usable description of the identity that "
            "is represented by the signature."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onBehalfOf[x]
            "one_of_many": "onBehalfOf",
            "one_of_many_required": False,
        },
    )
    onBehalfOfUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_onBehalfOfUri", title="Extension field for ``onBehalfOfUri``."
    )

    type: typing.List[fhirtypes.CodingType] = Field(  # type: ignore
        ...,
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
            "element_required": True,
        },
    )
    when__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_when", title="Extension field for ``when``."
    )

    whoReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="whoReference",
        title="Who signed",
        description=(
            "A reference to an application-usable description of the identity that "
            "signed  (e.g. the signature used their private key)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e who[x]
            "one_of_many": "who",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "RelatedPerson",
                "Patient",
                "Device",
                "Organization",
            ],
        },
    )

    whoUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="whoUri",
        title="Who signed",
        description=(
            "A reference to an application-usable description of the identity that "
            "signed  (e.g. the signature used their private key)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e who[x]
            "one_of_many": "who",
            "one_of_many_required": True,
        },
    )
    whoUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_whoUri", title="Extension field for ``whoUri``."
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
            "whoUri",
            "whoReference",
            "whoReference",
            "whoReference",
            "whoReference",
            "whoReference",
            "onBehalfOfUri",
            "onBehalfOfReference",
            "onBehalfOfReference",
            "onBehalfOfReference",
            "onBehalfOfReference",
            "onBehalfOfReference",
            "contentType",
            "blob",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("when", "when__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "onBehalfOf": ["onBehalfOfReference", "onBehalfOfUri"],
            "who": ["whoReference", "whoUri"],
        }
        return one_of_many_fields
