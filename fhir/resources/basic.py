# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Basic
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

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

    __resource_type__ = "Basic"

    author: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="author",
        title="Who created",
        description="Indicates who was responsible for creating the resource instance.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Patient",
                "RelatedPerson",
                "Organization",
                "Device",
                "CareTeam",
            ],
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Kind of Resource",
        description=(
            "Identifies the 'type' of resource - equivalent to the resource name "
            "for other resources."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    created: fhirtypes.DateTimeType = Field(  # type: ignore
        None,
        alias="created",
        title="When created",
        description="Identifies when the resource was first created.",
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Identifier assigned to the resource for business purposes, outside the"
            " context of FHIR."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="subject",
        title="Identifies the focus of this resource",
        description=(
            "Identifies the patient, practitioner, device or any other resource "
            'that is the "focus" of this resource.'
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
