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
    """ Information summarized from a list of other resources.
    A set of information summarized from a list of other resources.
    """

    resource_type = Field("List", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What the purpose of this list is",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the list was prepared",
    )

    emptyReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="emptyReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why list is empty",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON)",
        description="Context in which list created",
    )

    entry: ListType[fhirtypes.ListEntryType] = Field(
        None,
        alias="entry",
        title="List of `ListEntry` items (represented as `dict` in JSON)",
        description="Entries in the list",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier",
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="Type `Code` (represented as `dict` in JSON)",
        description="working | snapshot | changes",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments about the list",
    )

    orderedBy: fhirtypes.CodeableConceptType = Field(
        None,
        alias="orderedBy",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What order the list has",
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="Type `Reference` referencing `Practitioner, Patient, Device` (represented as `dict` in JSON)",
        description="Who and/or what defined the list contents (aka Author)",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="current | retired | entered-in-error",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON)",
        description="If all resources have the same subject",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Descriptive name for the list",
    )


class ListEntry(backboneelement.BackboneElement):
    """ Entries in the list.
    Entries in this list.
    """

    resource_type = Field("ListEntry", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When item added to list",
    )

    deleted: bool = Field(
        None,
        alias="deleted",
        title="Type `bool`",
        description="If this item is actually marked as deleted",
    )

    flag: fhirtypes.CodeableConceptType = Field(
        None,
        alias="flag",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Status/Workflow information about this item",
    )

    item: fhirtypes.ReferenceType = Field(
        ...,
        alias="item",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Actual entry",
    )
