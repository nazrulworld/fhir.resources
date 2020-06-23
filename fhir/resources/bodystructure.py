# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodyStructure
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class BodyStructure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specific and identified anatomical structure.
    Record details about an anatomical structure.  This resource may be used
    when a coded concept does not provide the necessary detail needed for the
    use case.
    """

    resource_type = Field("BodyStructure", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this record is in active use",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    description: fhirtypes.String = Field(
        None, alias="description", title="Type `String`", description="Text description"
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Bodystructure identifier",
    )

    image: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="image",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Attached images",
    )

    location: fhirtypes.CodeableConceptType = Field(
        None,
        alias="location",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Body site",
    )

    locationQualifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="locationQualifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Body site modifier",
    )

    morphology: fhirtypes.CodeableConceptType = Field(
        None,
        alias="morphology",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of Structure",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who this is about",
    )
