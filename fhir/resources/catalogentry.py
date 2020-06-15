# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CatalogEntry
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CatalogEntry(domainresource.DomainResource):
    """ An entry in a catalog.
    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """

    resource_type = Field("CatalogEntry", const=True)

    additionalCharacteristic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="additionalCharacteristic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Additional characteristics of the catalog entry",
    )

    additionalClassification: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="additionalClassification",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Additional classification of the catalog entry",
    )

    additionalIdentifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="additionalIdentifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description=(
            "Any additional identifier(s) for the catalog item, in the same "
            "granularity or concept"
        ),
    )

    classification: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classification",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Classification (category or class) of the item entry",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Unique identifier of the catalog item",
    )

    lastUpdated: fhirtypes.DateTime = Field(
        None,
        alias="lastUpdated",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When was this catalog last updated",
    )

    orderable: bool = Field(
        ...,
        alias="orderable",
        title="Type `bool`",
        description="Whether the entry represents an orderable item",
    )

    referencedItem: fhirtypes.ReferenceType = Field(
        ...,
        alias="referencedItem",
        title=(
            "Type `Reference` referencing `Medication, Device, Organization, "
            "Practitioner, PractitionerRole, HealthcareService, ActivityDefinition,"
            " PlanDefinition, SpecimenDefinition, ObservationDefinition, Binary` "
            "(represented as `dict` in JSON)"
        ),
        description="The item that is being defined",
    )

    relatedEntry: ListType[fhirtypes.CatalogEntryRelatedEntryType] = Field(
        None,
        alias="relatedEntry",
        title=(
            "List of `CatalogEntryRelatedEntry` items (represented as `dict` in "
            "JSON)"
        ),
        description="An item that this catalog entry is related to",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of item - medication, device, service, protocol or other",
    )

    validTo: fhirtypes.DateTime = Field(
        None,
        alias="validTo",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="The date until which this catalog entry is expected to be active",
    )

    validityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="validityPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The time period in which this catalog entry is expected to be active",
    )


class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """ An item that this catalog entry is related to.
    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """

    resource_type = Field("CatalogEntryRelatedEntry", const=True)

    item: fhirtypes.ReferenceType = Field(
        ...,
        alias="item",
        title=(
            "Type `Reference` referencing `CatalogEntry` (represented as `dict` in "
            "JSON)"
        ),
        description="The reference to the related item",
    )

    relationtype: fhirtypes.Code = Field(
        ...,
        alias="relationtype",
        title="Type `Code` (represented as `dict` in JSON)",
        description="triggers | is-replaced-by",
    )
