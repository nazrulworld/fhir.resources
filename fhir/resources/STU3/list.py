# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/List
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class List(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information summarized from a list of other resources.
    A set of information summarized from a list of other resources.
    """

    resource_type = Field("List", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="What the purpose of this list is",
        description="This code defines the purpose of the list - why it was created.",
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the list was prepared",
        description="The date that the list was prepared.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    emptyReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="emptyReason",
        title="Why list is empty",
        description="If the list is empty, why the list is empty.",
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Context in which list created",
        description="The encounter that is the context in which this list was created.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    entry: ListType[fhirtypes.ListEntryType] = Field(
        None,
        alias="entry",
        title="Entries in the list",
        description="Entries in this list.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Identifier for the List assigned for business purposes outside the "
            "context of FHIR."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["working", "snapshot", "changes"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments about the list",
        description="Comments that apply to the overall list.",
        # if property is element of this resource.
        element_property=True,
    )

    orderedBy: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orderedBy",
        title="What order the list has",
        description="What order applies to the items in the list.",
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Patient", "Device"],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="current | retired | entered-in-error",
        description="Indicates the current state of this list.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["current", "retired", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="If all resources have the same subject",
        description=(
            "The common subject (or patient) of the resources that are in the list,"
            " if there is one."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Device", "Location"],
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Descriptive name for the list",
        description="A label for the list assigned by the author.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )


class ListEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Entries in the list.
    Entries in this list.
    """

    resource_type = Field("ListEntry", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When item added to list",
        description="When this item was added to the list.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    deleted: bool = Field(
        None,
        alias="deleted",
        title="If this item is actually marked as deleted",
        description="True if this item is marked as deleted in the list.",
        # if property is element of this resource.
        element_property=True,
    )
    deleted__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deleted", title="Extension field for ``deleted``."
    )

    flag: fhirtypes.CodeableConceptType = Field(
        None,
        alias="flag",
        title="Status/Workflow information about this item",
        description=(
            "The flag allows the system constructing the list to indicate the role "
            "and significance of the item in the list."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    item: fhirtypes.ReferenceType = Field(
        ...,
        alias="item",
        title="Actual entry",
        description="A reference to the actual resource from which data was derived.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
