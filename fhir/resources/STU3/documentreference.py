# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentReference
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DocumentReference(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reference to a document.
    """

    resource_type = Field("DocumentReference", const=True)

    authenticator: fhirtypes.ReferenceType = Field(
        None,
        alias="authenticator",
        title=(
            "Type `Reference` referencing `Practitioner, Organization` (represented"
            " as `dict` in JSON)"
        ),
        description="Who/what authenticated the document",
    )

    author: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title=(
            "List of `Reference` items referencing `Practitioner, Organization, "
            "Device, Patient, RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Who and/or what authored the document",
    )

    class_fhir: fhirtypes.CodeableConceptType = Field(
        None,
        alias="class",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
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

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime`",
        description="Document creation time",
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
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

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Human-readable description (title)",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    docStatus: fhirtypes.Code = Field(
        None,
        alias="docStatus",
        title="Type `Code`",
        description="preliminary | final | appended | amended | entered-in-error",
    )
    docStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_docStatus", title="Extension field for ``docStatus``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Other identifiers for the document",
    )

    indexed: fhirtypes.Instant = Field(
        ...,
        alias="indexed",
        title="Type `Instant`",
        description="When this document reference was created",
    )
    indexed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_indexed", title="Extension field for ``indexed``."
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
        description="Who/what is the subject of the document",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of document (LOINC if possible)",
    )


class DocumentReferenceContent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Document referenced.
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Clinical context of document.
    The clinical context in which the document was prepared.
    """

    resource_type = Field("DocumentReferenceContext", const=True)

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
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

    related: ListType[fhirtypes.DocumentReferenceContextRelatedType] = Field(
        None,
        alias="related",
        title=(
            "List of `DocumentReferenceContextRelated` items (represented as `dict`"
            " in JSON)"
        ),
        description="Related identifiers or resources",
    )

    sourcePatientInfo: fhirtypes.ReferenceType = Field(
        None,
        alias="sourcePatientInfo",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Patient demographics from source",
    )


class DocumentReferenceContextRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related identifiers or resources.
    Related identifiers or resources associated with the DocumentReference.
    """

    resource_type = Field("DocumentReferenceContextRelated", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier of related objects or events",
    )

    ref: fhirtypes.ReferenceType = Field(
        None,
        alias="ref",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Related Resource",
    )


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationships to other documents.
    Relationships that this document has with other document references that
    already exist.
    """

    resource_type = Field("DocumentReferenceRelatesTo", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="replaces | transforms | signs | appends",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
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
