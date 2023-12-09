# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentReference
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class DocumentReference(domainresource.DomainResource):
    """
    A reference to a document.
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
        title="Who/what authenticated the document",
        description=(
            "Which person or organization authenticates that this document is " "valid."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    author: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title="Who and/or what authored the document",
        description=(
            "Identifies who is responsible for adding the information to the "
            "document."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Device",
            "Patient",
            "RelatedPerson",
        ],
    )

    class_fhir: fhirtypes.CodeableConceptType = Field(
        None,
        alias="class",
        title="Categorization of document",
        description=(
            "A categorization for the type of document referenced - "
            "helps for indexing and searching. This may be implied by or derived "
            "from the code specified in the DocumentReference.type."
        ),
    )

    content: ListType[fhirtypes.DocumentReferenceContentType] = Field(
        ...,
        alias="content",
        title="Document referenced",
        description=(
            "The document and format referenced. There may be multiple content "
            "element repetitions, each with a different format."
        ),
    )

    context: fhirtypes.DocumentReferenceContextType = Field(
        None,
        alias="context",
        title="Clinical context of document",
        description="The clinical context in which the document was prepared.",
    )

    custodian: fhirtypes.ReferenceType = Field(
        None,
        alias="custodian",
        title="Organization which maintains the document",
        description=(
            "Identifies the organization or group who is responsible for ongoing "
            "maintenance of and access to the document."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Document creation time",
        description="When the document was created.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Human-readable description",
        description="Human-readable description of the source document.",
    )

    docStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="docStatus",
        title="preliminary | final | appended | amended | entered-in-error",
        description="The status of the underlying document.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["preliminary", "final", "appended", "amended", "entered-in-error"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Other identifiers for the document",
        description=(
            "Other identifiers associated with the document, including version "
            "independent identifiers."
        ),
    )

    indexed: fhirtypes.Instant = Field(
        ...,
        alias="indexed",
        title="When this document reference was created",
        description="When the document reference was created.",
    )

    masterIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="masterIdentifier",
        title="Master Version Specific Identifier",
        description=(
            "Document identifier as assigned by the source of the document. This "
            "identifier is specific to this version of the document. This unique "
            "identifier may be used elsewhere to identify this version of the "
            "document."
        ),
    )

    relatesTo: ListType[fhirtypes.DocumentReferenceRelatesToType] = Field(
        None,
        alias="relatesTo",
        title="Relationships to other documents",
        description=(
            "Relationships that this document has with other document references "
            "that already exist."
        ),
    )

    securityLabel: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="securityLabel",
        title="Document security-tags",
        description=(
            "A set of Security-Tag codes specifying the level of privacy/security "
            "of the Document. Note that DocumentReference.meta.security contains "
            'the security labels of the "reference" to the document, while '
            "DocumentReference.securityLabel contains a snapshot of the security "
            "labels on the document the reference refers to."
        ),
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="current | superseded | entered-in-error",
        description="The status of this document reference.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["current", "superseded", "entered-in-error"],
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who/what is the subject of the document",
        description=(
            "Who or what the document is about. The document can be about a person,"
            " (patient or healthcare practitioner), a device (e.g. a machine) or "
            "even a group of subjects (such as a document about a herd of farm "
            "animals, or a set of patients that share a common exposure)."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "Group", "Device"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Kind of document (LOINC if possible)",
        description=(
            "Specifies the particular kind of document referenced  (e.g. History "
            "and Physical, Discharge Summary, Progress Note). This usually equates "
            "to the purpose of making the document referenced."
        ),
    )


class DocumentReferenceContent(backboneelement.BackboneElement):
    """
    Document referenced.
    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """

    resource_type = Field("DocumentReferenceContent", const=True)

    attachment: fhirtypes.AttachmentType = Field(
        ...,
        alias="attachment",
        title="Where to access the document",
        description=(
            "The document or URL of the document along with critical metadata to "
            "prove content has integrity."
        ),
    )

    format: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="format",
        title="Format/content rules for the document",
        description=(
            "An identifier of the document encoding, structure, and template that "
            "the document conforms to beyond the base format indicated in the "
            "mimeType."
        ),
    )


class DocumentReferenceContext(backboneelement.BackboneElement):
    """
    Clinical context of document.
    The clinical context in which the document was prepared.
    """

    resource_type = Field("DocumentReferenceContext", const=True)

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Context of the document content",
        description=(
            "Describes the clinical encounter or type of care that the document "
            "content is associated with."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    event: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="event",
        title="Main clinical acts documented",
        description=(
            "This list of codes represents the main clinical acts, such as a "
            "colonoscopy or an appendectomy, being documented. In some cases, the "
            'event is inherent in the type Code, such as a "History and Physical '
            'Report" in which the procedure being documented is necessarily a '
            '"History and Physical" act.'
        ),
    )

    facilityType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="facilityType",
        title="Kind of facility where patient was seen",
        description="The kind of facility where the patient was seen.",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time of service that is being documented",
        description=(
            "The time period over which the service that is described by the "
            "document was provided."
        ),
    )

    practiceSetting: fhirtypes.CodeableConceptType = Field(
        None,
        alias="practiceSetting",
        title=(
            "Additional details about where the content was created (e.g. clinical "
            "specialty)"
        ),
        description=(
            "This property may convey specifics about the practice setting where "
            "the content was created, often reflecting the clinical specialty."
        ),
    )

    related: ListType[fhirtypes.DocumentReferenceContextRelatedType] = Field(
        None,
        alias="related",
        title="Related identifiers or resources",
        description=(
            "Related identifiers or resources associated with the " "DocumentReference."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    sourcePatientInfo: fhirtypes.ReferenceType = Field(
        None,
        alias="sourcePatientInfo",
        title="Patient demographics from source",
        description=(
            "The Patient Information as known when the document was published. May "
            "be a reference to a version specific, or contained."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """
    Relationships to other documents.
    Relationships that this document has with other document references that
    already exist.
    """

    resource_type = Field("DocumentReferenceRelatesTo", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="replaces | transforms | signs | appends",
        description="The type of relationship that this document has with anther document.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["replaces", "transforms", "signs", "appends"],
    )

    target: fhirtypes.ReferenceType = Field(
        ...,
        alias="target",
        title="Target of the relationship",
        description="The target document of this relationship.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )


class DocumentReferenceContextRelated(backboneelement.BackboneElement):
    resource_type = Field("DocumentReferenceContextRelated", const=True)

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier of related objects or events",
        description=(
            "This property may convey specifics about the practice setting"
            "where the content was created, often reflecting the clinical specialty."
        ),
    )

    ref: fhirtypes.ReferenceType = Field(
        None,
        alias="related",
        title="Related identifiers or resources",
        description=(
            "Related identifiers or resources associated with the " "DocumentReference."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
