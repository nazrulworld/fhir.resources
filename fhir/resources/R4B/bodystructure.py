from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/BodyStructure
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class BodyStructure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specific and identified anatomical structure.
    Record details about an anatomical structure.  This resource may be used
    when a coded concept does not provide the necessary detail needed for the
    use case.
    """

    __resource_type__ = "BodyStructure"

    active: bool | None = Field(  # type: ignore
        None,
        alias="active",
        title="Whether this record is in active use",
        description="Whether this body site is in active use.",
        json_schema_extra={
            "element_property": True,
        },
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_active", title="Extension field for ``active``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Text description",
        description="A summary, characterization or explanation of the body structure.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Bodystructure identifier",
        description="Identifier for this instance of the anatomical structure.",
        json_schema_extra={
            "element_property": True,
        },
    )

    image: typing.List[fhirtypes.AttachmentType] | None = Field(  # type: ignore
        None,
        alias="image",
        title="Attached images",
        description="Image or images used to identify a location.",
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Body site",
        description=(
            "The anatomical location or region of the specimen, lesion, or body "
            "structure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    locationQualifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="locationQualifier",
        title="Body site modifier",
        description=(
            "Qualifier to refine the anatomical location.  These include qualifiers"
            " for laterality, relative location, directionality, number, and plane."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    morphology: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="morphology",
        title="Kind of Structure",
        description=(
            "The kind of structure being represented by the body structure at "
            "`BodyStructure.location`.  This can define both normal and abnormal "
            "morphologies."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="Who this is about",
        description="The person to which the body site belongs.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BodyStructure`` according specification,
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
            "morphology",
            "location",
            "locationQualifier",
            "description",
            "image",
            "patient",
        ]
