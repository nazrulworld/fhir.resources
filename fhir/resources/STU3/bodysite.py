# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodySite
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class BodySite(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specific and identified anatomical location.
    Record details about the anatomical location of a specimen or body part.
    This resource may be used when a coded concept does not provide the
    necessary detail needed for the use case.
    """

    resource_type = Field("BodySite", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this body site record is in active use",
        description="Whether this body site is in active use.",
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Named anatomical location",
        description="Named anatomical location - ideally coded where possible.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Anatomical location description",
        description="A summary, charactarization or explanation of the anatomic location.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Bodysite identifier",
        description="Identifier for this instance of the anatomical location.",
        # if property is element of this resource.
        element_property=True,
    )

    image: typing.List[fhirtypes.AttachmentType] = Field(
        None,
        alias="image",
        title="Attached images",
        description="Image or images used to identify a location.",
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who this is about",
        description="The person to which the body site belongs.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    qualifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="qualifier",
        title="Modification to location code",
        description=(
            "Qualifier to refine the anatomical location.  These include qualifiers"
            " for laterality, relative location, directionality, number, and plane."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BodySite`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "active",
            "code",
            "qualifier",
            "description",
            "image",
            "patient",
        ]
