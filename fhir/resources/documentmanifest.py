# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DocumentManifest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A list that defines a set of documents.
    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """

    resource_type = Field("DocumentManifest", const=True)

    author: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title=(
            "List of `Reference` items referencing `Practitioner, PractitionerRole,"
            " Organization, Device, Patient, RelatedPerson` (represented as `dict` "
            "in JSON)"
        ),
        description="Who and/or what authored the DocumentManifest",
    )

    content: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="content",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Items in manifest",
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime`",
        description="When this document manifest created",
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Human-readable description (title)",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Other identifiers for the manifest",
    )

    masterIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="masterIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique Identifier for the set of documents",
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title=(
            "List of `Reference` items referencing `Patient, Practitioner, "
            "PractitionerRole, RelatedPerson, Organization` (represented as `dict` "
            "in JSON)"
        ),
        description="Intended to get notified about this set of documents",
    )

    related: ListType[fhirtypes.DocumentManifestRelatedType] = Field(
        None,
        alias="related",
        title=(
            "List of `DocumentManifestRelated` items (represented as `dict` in " "JSON)"
        ),
        description="Related things",
    )

    source: fhirtypes.Uri = Field(
        None,
        alias="source",
        title="Type `Uri`",
        description="The source system/application/software",
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="current | superseded | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, Group, Device` "
            "(represented as `dict` in JSON)"
        ),
        description="The subject of the set of documents",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of document set",
    )


class DocumentManifestRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related things.
    Related identifiers or resources associated with the DocumentManifest.
    """

    resource_type = Field("DocumentManifestRelated", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifiers of things that are related",
    )

    ref: fhirtypes.ReferenceType = Field(
        None,
        alias="ref",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Related Resource",
    )
