from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DocumentManifest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A list that defines a set of documents.
    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """

    __resource_type__ = "DocumentManifest"

    author: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="author",
        title="Who and/or what authored the manifest",
        description=(
            "Identifies who is responsible for creating the manifest, and adding  "
            "documents to it."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Device",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    content: typing.List[fhirtypes.DocumentManifestContentType] = Field(  # type: ignore
        ...,
        alias="content",
        title="The items included",
        description="The list of Documents included in the manifest.",
        json_schema_extra={
            "element_property": True,
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="When this document manifest created",
        description=(
            "When the document manifest was created for submission to the server "
            "(not necessarily the same thing as the actual resource last modified "
            "time, since it may be modified, replicated, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Human-readable description (title)",
        description=(
            "Human-readable description of the source document. This is sometimes "
            'known as the "title".'
        ),
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
        title="Other identifiers for the manifest",
        description=(
            "Other identifiers associated with the document manifest, including "
            "version independent  identifiers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    masterIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="masterIdentifier",
        title="Unique Identifier for the set of documents",
        description=(
            "A single identifier that uniquely identifies this manifest. "
            "Principally used to refer to the manifest in non-FHIR contexts."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    recipient: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="recipient",
        title="Intended to get notified about this set of documents",
        description=(
            "A patient, practitioner, or organization for which this set of "
            "documents is intended."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "Organization",
            ],
        },
    )

    related: typing.List[fhirtypes.DocumentManifestRelatedType] | None = Field(  # type: ignore
        None,
        alias="related",
        title="Related things",
        description="Related identifiers or resources associated with the DocumentManifest.",
        json_schema_extra={
            "element_property": True,
        },
    )

    source: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="source",
        title="The source system/application/software",
        description=(
            "Identifies the source system, application, or software that produced "
            "the document manifest."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_source", title="Extension field for ``source``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="current | superseded | entered-in-error",
        description="The status of this document manifest.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["current", "superseded", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Practitioner", "Group", "Device"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Kind of document set",
        description=(
            "Specifies the kind of this set of documents (e.g. Patient Summary, "
            "Discharge Summary, Prescription, etc.). The type of a set of documents"
            " may be the same as one of the documents in it - especially if there "
            "is only one - but it may be wider."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentManifest`` according specification,
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
            "masterIdentifier",
            "identifier",
            "status",
            "type",
            "subject",
            "created",
            "author",
            "recipient",
            "source",
            "description",
            "content",
            "related",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class DocumentManifestContent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The items included.
    The list of Documents included in the manifest.
    """

    __resource_type__ = "DocumentManifestContent"

    pAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="pAttachment",
        title="Contents of this set of documents",
        description=(
            "The list of references to document content, or Attachment that consist"
            " of the parts of this document manifest. Usually, these would be "
            "document references, but direct references to Media or Attachments are"
            " also allowed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e p[x]
            "one_of_many": "p",
            "one_of_many_required": True,
        },
    )

    pReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="pReference",
        title="Contents of this set of documents",
        description=(
            "The list of references to document content, or Attachment that consist"
            " of the parts of this document manifest. Usually, these would be "
            "document references, but direct references to Media or Attachments are"
            " also allowed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e p[x]
            "one_of_many": "p",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DocumentManifestContent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "pAttachment", "pReference"]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"p": ["pAttachment", "pReference"]}
        return one_of_many_fields


class DocumentManifestRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related things.
    Related identifiers or resources associated with the DocumentManifest.
    """

    __resource_type__ = "DocumentManifestRelated"

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifiers of things that are related",
        description=(
            "Related identifier to this DocumentManifest.  For example, Order "
            "numbers, accession numbers, XDW workflow numbers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    ref: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="ref",
        title="Related Resource",
        description=(
            "Related Resource to this DocumentManifest. For example, Order, "
            "ProcedureRequest,  Procedure, EligibilityRequest, etc."
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
        ``DocumentManifestRelated`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "identifier", "ref"]
