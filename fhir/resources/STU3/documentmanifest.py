# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

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
        title="Who and/or what authored the manifest",
        description=(
            "Identifies who is responsible for creating the manifest, and adding  "
            "documents to it."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Device",
            "Patient",
            "RelatedPerson",
        ],
    )

    content: ListType[fhirtypes.DocumentManifestContentType] = Field(
        ...,
        alias="content",
        title="The items included",
        description="The list of Documents included in the manifest.",
        # if property is element of this resource.
        element_property=True,
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
            "Specifies the kind of this set of documents (e.g. Patient Summary, "
            "Discharge Summary, Prescription, etc.). The type of a set of documents"
            " may be the same as one of the documents in it - especially if there "
            "is only one - but it may be wider."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class DocumentManifestContent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The items included.
    The list of Documents included in the manifest.
    """

    resource_type = Field("DocumentManifestContent", const=True)

    pAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="pAttachment",
        title="Contents of this set of documents",
        description=(
            "The list of references to document content, or Attachment that consist"
            " of the parts of this document manifest. Usually, these would be "
            "document references, but direct references to Media or Attachments are"
            " also allowed."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e p[x]
        one_of_many="p",
        one_of_many_required=True,
    )

    pReference: fhirtypes.ReferenceType = Field(
        None,
        alias="pReference",
        title="Contents of this set of documents",
        description=(
            "The list of references to document content, or Attachment that consist"
            " of the parts of this document manifest. Usually, these would be "
            "document references, but direct references to Media or Attachments are"
            " also allowed."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e p[x]
        one_of_many="p",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


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
            "ProcedureRequest,  Procedure, EligibilityRequest, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
