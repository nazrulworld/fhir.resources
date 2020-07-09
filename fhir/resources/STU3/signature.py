# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Signature
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import element, fhirtypes


class Signature(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..
    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different signature
    approaches have different utilities.
    """

    resource_type = Field("Signature", const=True)

    blob: fhirtypes.Base64Binary = Field(
        None,
        alias="blob",
        title="The actual signature content (XML DigSig. JWT, picture, etc.)",
        description=(
            "The base64 encoding of the Signature content. When signature is not "
            "recorded electronically this element would be empty."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    blob__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_blob", title="Extension field for ``blob``."
    )

    contentType: fhirtypes.Code = Field(
        None,
        alias="contentType",
        title="The technical format of the signature",
        description=(
            "A mime type that indicates the technical format of the signature. "
            "Important mime types are application/signature+xml for X ML DigSig, "
            "application/jwt for JWT, and image/* for a graphical image of a "
            "signature, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentType", title="Extension field for ``contentType``."
    )

    onBehalfOfReference: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOfReference",
        title="The party represented",
        description=(
            "A reference to an application-usable description of the identity that "
            "is represented by the signature."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onBehalfOf[x]
        one_of_many="onBehalfOf",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "RelatedPerson",
            "Patient",
            "Device",
            "Organization",
        ],
    )

    onBehalfOfUri: fhirtypes.Uri = Field(
        None,
        alias="onBehalfOfUri",
        title="The party represented",
        description=(
            "A reference to an application-usable description of the identity that "
            "is represented by the signature."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onBehalfOf[x]
        one_of_many="onBehalfOf",
        one_of_many_required=False,
    )
    onBehalfOfUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onBehalfOfUri", title="Extension field for ``onBehalfOfUri``."
    )

    type: ListType[fhirtypes.CodingType] = Field(
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
        ...,
        alias="when",
        title="When the signature was created",
        description="When the digital signature was signed.",
        # if property is element of this resource.
        element_property=True,
    )
    when__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_when", title="Extension field for ``when``."
    )

    whoReference: fhirtypes.ReferenceType = Field(
        None,
        alias="whoReference",
        title="Who signed",
        description=(
            "A reference to an application-usable description of the identity that "
            "signed  (e.g. the signature used their private key)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e who[x]
        one_of_many="who",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "RelatedPerson",
            "Patient",
            "Device",
            "Organization",
        ],
    )

    whoUri: fhirtypes.Uri = Field(
        None,
        alias="whoUri",
        title="Who signed",
        description=(
            "A reference to an application-usable description of the identity that "
            "signed  (e.g. the signature used their private key)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e who[x]
        one_of_many="who",
        one_of_many_required=True,
    )
    whoUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whoUri", title="Extension field for ``whoUri``."
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
