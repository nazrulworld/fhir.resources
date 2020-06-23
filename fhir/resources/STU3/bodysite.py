# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodySite
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class BodySite(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        title="Type `bool`",
        description="Whether this body site record is in active use",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Named anatomical location",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Anatomical location description",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Bodysite identifier",
    )

    image: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="image",
        title="List of `Attachment` items (represented as `dict` in JSON)",
        description="Attached images",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who this is about",
    )

    qualifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="qualifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Modification to location code",
    )
