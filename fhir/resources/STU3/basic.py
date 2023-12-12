# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Basic
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field

from . import domainresource, fhirtypes


class Basic(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource for non-supported content.
    Basic is used for handling concepts not yet defined in FHIR, narrative-only
    resources that don't map to an existing resource, and custom resources not
    appropriate for inclusion in the FHIR specification.
    """

    resource_type = Field("Basic", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Who created",
        description="Indicates who was responsible for creating the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Patient", "RelatedPerson"],
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Kind of Resource",
        description=(
            "Identifies the 'type' of resource - equivalent to the resource name "
            "for other resources."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    created: fhirtypes.Date = Field(
        None,
        alias="created",
        title="When created",
        description="Identifies when the resource was first created.",
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Identifier assigned to the resource for business purposes, outside the"
            " context of FHIR."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Identifies the focus of this resource",
        description=(
            "Identifies the patient, practitioner, device or any other resource "
            'that is the "focus" of this resource.'
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Basic`` according specification,
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
            "code",
            "subject",
            "created",
            "author",
        ]
