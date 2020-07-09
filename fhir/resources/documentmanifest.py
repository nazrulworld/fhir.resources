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
        title="Who and/or what authored the DocumentManifest",
        description=(
            "Identifies who is the author of the manifest. Manifest author is not "
            "necessarly the author of the references included."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Device",
            "Patient",
            "RelatedPerson",
        ],
    )

    content: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="content",
        title="Items in manifest",
        description="The list of Resources that consist of the parts of this manifest.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="When this document manifest created",
        description=(
            "When the document manifest was created for submission to the server "
            "(not necessarily the same thing as the actual resource last modified "
            "time, since it may be modified, replicated, etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Human-readable description (title)",
        description=(
            "Human-readable description of the source document. This is sometimes "
            'known as the "title".'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Other identifiers for the manifest",
        description=(
            "Other identifiers associated with the document manifest, including "
            "version independent  identifiers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    masterIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="masterIdentifier",
        title="Unique Identifier for the set of documents",
        description=(
            "A single identifier that uniquely identifies this manifest. "
            "Principally used to refer to the manifest in non-FHIR contexts."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title="Intended to get notified about this set of documents",
        description=(
            "A patient, practitioner, or organization for which this set of "
            "documents is intended."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Organization",
        ],
    )

    related: ListType[fhirtypes.DocumentManifestRelatedType] = Field(
        None,
        alias="related",
        title="Related things",
        description="Related identifiers or resources associated with the DocumentManifest.",
        # if property is element of this resource.
        element_property=True,
    )

    source: fhirtypes.Uri = Field(
        None,
        alias="source",
        title="The source system/application/software",
        description=(
            "Identifies the source system, application, or software that produced "
            "the document manifest."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="current | superseded | entered-in-error",
        description="The status of this document manifest.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["current", "superseded", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="The subject of the set of documents",
        description=(
            "Who or what the set of documents is about. The documents can be about "
            "a person, (patient or healthcare practitioner), a device (i.e. "
            "machine) or even a group of subjects (such as a document about a herd "
            "of farm animals, or a set of patients that share a common exposure). "
            "If the documents cross more than one subject, then more than one "
            "subject is allowed here (unusual use case)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "Group", "Device"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of document set",
        description=(
            "The code specifying the type of clinical activity that resulted in "
            "placing the associated content into the DocumentManifest."
        ),
        # if property is element of this resource.
        element_property=True,
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
        title="Identifiers of things that are related",
        description=(
            "Related identifier to this DocumentManifest.  For example, Order "
            "numbers, accession numbers, XDW workflow numbers."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    ref: fhirtypes.ReferenceType = Field(
        None,
        alias="ref",
        title="Related Resource",
        description=(
            "Related Resource to this DocumentManifest. For example, Order, "
            "ServiceRequest,  Procedure, EligibilityRequest, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
