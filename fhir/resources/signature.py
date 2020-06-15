# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Signature
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import element, fhirtypes


class Signature(element.Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..
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
        title="Type `Base64Binary` (represented as `dict` in JSON)",
        description="The actual signature content (XML DigSig. JWS, picture, etc.)",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "RelatedPerson, Patient, Device, Organization` (represented as `dict` "
            "in JSON)"
        ),
        description="The party represented",
    )

    sigFormat: fhirtypes.Code = Field(
        None,
        alias="sigFormat",
        title="Type `Code` (represented as `dict` in JSON)",
        description="The technical format of the signature",
    )

    targetFormat: fhirtypes.Code = Field(
        None,
        alias="targetFormat",
        title="Type `Code` (represented as `dict` in JSON)",
        description="The technical format of the signed resources",
    )

    type: ListType[fhirtypes.CodingType] = Field(
        ...,
        alias="type",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Indication of the reason the entity signed the object(s)",
    )

    when: fhirtypes.Instant = Field(
        ...,
        alias="when",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When the signature was created",
    )

    who: fhirtypes.ReferenceType = Field(
        ...,
        alias="who",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "RelatedPerson, Patient, Device, Organization` (represented as `dict` "
            "in JSON)"
        ),
        description="Who signed",
    )
