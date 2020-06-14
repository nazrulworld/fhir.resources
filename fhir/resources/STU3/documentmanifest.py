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
    """ A list that defines a set of documents.
    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """

    resource_type = Field("DocumentManifest", const=True)

    author: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="author",
        title="List of `Reference` items referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON)",
        description="Who and/or what authored the manifest",
    )

    content: ListType[fhirtypes.DocumentManifestContentType] = Field(
        ...,
        alias="content",
        title="List of `DocumentManifestContent` items (represented as `dict` in JSON)",
        description="The items included",
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When this document manifest created",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human-readable description (title)",
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
        title="List of `Reference` items referencing `Patient, Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON)",
        description="Intended to get notified about this set of documents",
    )

    related: ListType[fhirtypes.DocumentManifestRelatedType] = Field(
        None,
        alias="related",
        title="List of `DocumentManifestRelated` items (represented as `dict` in JSON)",
        description="Related things",
    )

    source: fhirtypes.Uri = Field(
        None,
        alias="source",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="The source system/application/software",
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
        title="Type `Reference` referencing `Patient, Practitioner, Group, Device` (represented as `dict` in JSON)",
        description="The subject of the set of documents",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of document set",
    )


class DocumentManifestContent(backboneelement.BackboneElement):
    """ The items included.
    The list of Documents included in the manifest.
    """

    resource_type = Field("DocumentManifestContent", const=True)

    pAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="pAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Contents of this set of documents",
        one_of_many="p",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    pReference: fhirtypes.ReferenceType = Field(
        None,
        alias="pReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Contents of this set of documents",
        one_of_many="p",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
        one_of_many_fields = {
            "p": ["pAttachment", "pReference",],
        }
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
    """ Related things.
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
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Related Resource",
    )
