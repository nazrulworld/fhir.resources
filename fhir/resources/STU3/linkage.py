# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Linkage
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Linkage(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links records for 'same' item.
    Identifies two or more records (resource instances) that are referring to
    the same real-world "occurrence".
    """

    resource_type = Field("Linkage", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this linkage assertion is active or not",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Practitioner, Organization` (represented"
            " as `dict` in JSON)"
        ),
        description="Who is responsible for linkages",
    )

    item: ListType[fhirtypes.LinkageItemType] = Field(
        ...,
        alias="item",
        title="List of `LinkageItem` items (represented as `dict` in JSON)",
        description="Item to be linked",
    )


class LinkageItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item to be linked.
    Identifies one of the records that is considered to refer to the same real-
    world occurrence as well as how the items hould be evaluated within the
    collection of linked items.
    """

    resource_type = Field("LinkageItem", const=True)

    resource: fhirtypes.ReferenceType = Field(
        ...,
        alias="resource",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="Resource being linked",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="source | alternate | historical",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
