# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Signature
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import element, fhirtypes


class Signature(element.Element):
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

    resource_type = Field("Signature", const=True)

    data: fhirtypes.Base64Binary = Field(
        None,
        alias="data",
        title="The actual signature content (XML DigSig. JWS, picture, etc.)",
        description=(
            "The base64 encoding of the Signature content. When signature is not "
            "recorded electronically this element would be empty."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    data__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_data", title="Extension field for ``data``."
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="The party represented",
        description=(
            "A reference to an application-usable description of the identity that "
            "is represented by the signature."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Patient",
            "Device",
            "Organization",
        ],
    )

    sigFormat: fhirtypes.Code = Field(
        None,
        alias="sigFormat",
        title="The technical format of the signature",
        description=(
            "A mime type that indicates the technical format of the signature. "
            "Important mime types are application/signature+xml for X ML DigSig, "
            "application/jose for JWS, and image/* for a graphical image of a "
            "signature, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sigFormat__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sigFormat", title="Extension field for ``sigFormat``."
    )

    targetFormat: fhirtypes.Code = Field(
        None,
        alias="targetFormat",
        title="The technical format of the signed resources",
        description=(
            "A mime type that indicates the technical format of the target "
            "resources signed by the signature."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    targetFormat__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_targetFormat", title="Extension field for ``targetFormat``."
    )

    type: typing.List[fhirtypes.CodingType] = Field(
        ...,
        alias="type",
        title="Indication of the reason the entity signed the object(s)",
        description=(
            "An indication of the reason that the entity signed this document. This"
            " may be explicitly included as part of the signature information and "
            "can be used when determining accountability for various actions "
            "concerning the document."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    when: fhirtypes.Instant = Field(
        None,
        alias="when",
        title="When the signature was created",
        description="When the digital signature was signed.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    when__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_when", title="Extension field for ``when``."
    )

    who: fhirtypes.ReferenceType = Field(
        ...,
        alias="who",
        title="Who signed",
        description=(
            "A reference to an application-usable description of the identity that "
            "signed  (e.g. the signature used their private key)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Patient",
            "Device",
            "Organization",
        ],
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1130(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("when", "when__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
