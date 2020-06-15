# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentReference
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DocumentReference(domainresource.DomainResource):
    """ A reference to a document.
    A reference to a document of any kind for any purpose. Provides metadata
    about the document so that the document can be discovered and managed. The
    scope of a document is any seralized object with a mime-type, so includes
    formal patient centric documents (CDA), cliical notes, scanned paper, and
    non-patient specific documents like policy text.
    """

    resource_type = Field("DocumentReference", const=True)

    authenticator: fhirtypes.ReferenceType = Field(
        None,
        alias="authenticator",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description="Who/what authenticated the document",
    )

    author: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title=(
            "List of `Reference` items referencing `Practitioner, PractitionerRole,"
            " Organization, Device, Patient, RelatedPerson` (represented as `dict` "
            "in JSON)"
        ),
        description="Who and/or what authored the document",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Categorization of document",
    )

    content: ListType[fhirtypes.DocumentReferenceContentType] = Field(
        ...,
        alias="content",
        title=(
            "List of `DocumentReferenceContent` items (represented as `dict` in "
            "JSON)"
        ),
        description="Document referenced",
    )

    context: fhirtypes.DocumentReferenceContextType = Field(
        None,
        alias="context",
        title="Type `DocumentReferenceContext` (represented as `dict` in JSON)",
        description="Clinical context of document",
    )

    custodian: fhirtypes.ReferenceType = Field(
        None,
        alias="custodian",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization which maintains the document",
    )

    date: fhirtypes.Instant = Field(
        None,
        alias="date",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When this document reference was created",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human-readable description",
    )

    docStatus: fhirtypes.Code = Field(
        None,
        alias="docStatus",
        title="Type `Code` (represented as `dict` in JSON)",
        description="preliminary | final | amended | entered-in-error",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Other identifiers for the document",
    )

    masterIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="masterIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Master Version Specific Identifier",
    )

    relatesTo: ListType[fhirtypes.DocumentReferenceRelatesToType] = Field(
        None,
        alias="relatesTo",
        title=(
            "List of `DocumentReferenceRelatesTo` items (represented as `dict` in "
            "JSON)"
        ),
        description="Relationships to other documents",
    )

    securityLabel: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="securityLabel",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Document security-tags",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="current | superseded | entered-in-error",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, Group, Device` "
            "(represented as `dict` in JSON)"
        ),
        description="Who/what is the subject of the document",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of document (LOINC if possible)",
    )


class DocumentReferenceContent(backboneelement.BackboneElement):
    """ Document referenced.
    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """

    resource_type = Field("DocumentReferenceContent", const=True)

    attachment: fhirtypes.AttachmentType = Field(
        ...,
        alias="attachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Where to access the document",
    )

    format: fhirtypes.CodingType = Field(
        None,
        alias="format",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Format/content rules for the document",
    )


class DocumentReferenceContext(backboneelement.BackboneElement):
    """ Clinical context of document.
    The clinical context in which the document was prepared.
    """

    resource_type = Field("DocumentReferenceContext", const=True)

    encounter: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="encounter",
        title=(
            "List of `Reference` items referencing `Encounter, EpisodeOfCare` "
            "(represented as `dict` in JSON)"
        ),
        description="Context of the document  content",
    )

    event: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="event",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Main clinical acts documented",
    )

    facilityType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="facilityType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of facility where patient was seen",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time of service that is being documented",
    )

    practiceSetting: fhirtypes.CodeableConceptType = Field(
        None,
        alias="practiceSetting",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Additional details about where the content was created (e.g. clinical "
            "specialty)"
        ),
    )

    related: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="related",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Related identifiers or resources",
    )

    sourcePatientInfo: fhirtypes.ReferenceType = Field(
        None,
        alias="sourcePatientInfo",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Patient demographics from source",
    )


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other documents.
    Relationships that this document has with other document references that
    already exist.
    """

    resource_type = Field("DocumentReferenceRelatesTo", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="replaces | transforms | signs | appends",
    )

    target: fhirtypes.ReferenceType = Field(
        ...,
        alias="target",
        title=(
            "Type `Reference` referencing `DocumentReference` (represented as "
            "`dict` in JSON)"
        ),
        description="Target of the relationship",
    )
