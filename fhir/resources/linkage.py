# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Linkage
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Linkage(domainresource.DomainResource):
    """ Links records for 'same' item.
    Identifies two or more records (resource instances) that refer to the same
    real-world "occurrence".
    """

    resource_type = Field("Linkage", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this linkage assertion is active or not",
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Who is responsible for linkages",
    )

    item: ListType[fhirtypes.LinkageItemType] = Field(
        ...,
        alias="item",
        title="List of `LinkageItem` items (represented as `dict` in JSON)",
        description="Item to be linked",
    )


class LinkageItem(backboneelement.BackboneElement):
    """ Item to be linked.
    Identifies which record considered as the reference to the same real-world
    occurrence as well as how the items should be evaluated within the
    collection of linked items.
    """

    resource_type = Field("LinkageItem", const=True)

    resource: fhirtypes.ReferenceType = Field(
        ...,
        alias="resource",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Resource being linked",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="source | alternate | historical",
    )
