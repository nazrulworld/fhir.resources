# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/list.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class List(domainresource.DomainResource):
    """A list is a curated collection of resources."""

    resource_type = Field("List", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="What the purpose of this list is",
        description="This code defines the purpose of the list - why it was created.",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the list was prepared",
        description="The date that the list was prepared.",
    )

    emptyReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="emptyReason",
        title="Why list is empty",
        description="If the list is empty, why the list is empty.",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Context in which list created",
        description="The encounter that is the context in which this list was created.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    entry: ListType[fhirtypes.ListEntryType] = Field(
        None,
        alias="entry",
        title="Entries in the list",
        description="Entries in this list.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Identifier for the List assigned for business purposes outside the "
            "context of FHIR."
        ),
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="working | snapshot | changes",
        description=(
            "How this list was prepared - whether it is a working list that is "
            "suitable for being maintained on an ongoing basis, or if it represents"
            " a snapshot of a list of items from another source, or whether it is a"
            " prepared list where items may be marked as added, modified or "
            "deleted."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["working", "snapshot", "changes"],
    )

    note: fhirtypes.String = Field(
        None,
        alias="note",
        title="Comments about the list",
        description="Comments that apply to the overall list.",
    )

    orderedBy: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orderedBy",
        title="What order the list has",
        description="What order applies to the items in the list.",
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Who and/or what defined the list contents (aka Author)",
        description=(
            "The entity responsible for deciding what the contents of the list "
            "were. Where the list was created by a human, this is the same as the "
            "author of the list."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Patient", "Device"],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="current | retired | entered-in-error",
        description="Indicates the current state of this list.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["current", "retired", "entered-in-error"],
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="If all resources have the same subject",
        description=(
            "The common subject (or patient) of the resources that are in the list "
            "if there is one."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Device", "Location"],
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Descriptive name for the list",
        description="A label for the list assigned by the author.",
    )


class ListEntry(backboneelement.BackboneElement):
    """Entries in the list.

    Entries in this list.
    """

    resource_type = Field("ListEntry", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When item added to list",
        description="When this item was added to the list.",
    )

    deleted: fhirtypes.Boolean = Field(
        None,
        alias="deleted",
        title="If this item is actually marked as deleted",
        description="True if this item is marked as deleted in the list.",
    )

    flag: fhirtypes.CodeableConceptType = Field(
        None,
        alias="flag",
        title="Status/Workflow information about this item",
        description=(
            "The flag allows the system constructing the list to indicate the role "
            "and significance of the item in the list."
        ),
    )

    item: fhirtypes.ReferenceType = Field(
        ...,
        alias="item",
        title="Actual entry",
        description="A reference to the actual resource from which data was derived.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
