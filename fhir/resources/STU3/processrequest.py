# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ProcessRequest(domainresource.DomainResource):
    """ Request to perform some action on or in regards to an existing resource.
    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """

    resource_type = Field("ProcessRequest", const=True)

    action: fhirtypes.Code = Field(
        None,
        alias="action",
        title="Type `Code` (represented as `dict` in JSON)",
        description="cancel | poll | reprocess | status",
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
    )

    exclude: ListType[fhirtypes.String] = Field(
        None,
        alias="exclude",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Resource type(s) to exclude",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier",
    )

    include: ListType[fhirtypes.String] = Field(
        None,
        alias="include",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Resource type(s) to include",
    )

    item: ListType[fhirtypes.ProcessRequestItemType] = Field(
        None,
        alias="item",
        title="List of `ProcessRequestItem` items (represented as `dict` in JSON)",
        description="Items to re-adjudicate",
    )

    nullify: bool = Field(
        None, alias="nullify", title="Type `bool`", description="Remove history"
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible organization",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Selection period",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible practitioner",
    )

    reference: fhirtypes.String = Field(
        None,
        alias="reference",
        title="Type `String` (represented as `dict` in JSON)",
        description="Reference number/string",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Reference to the Request resource",
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Reference to the Response resource",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Party which is the target of the request",
    )


class ProcessRequestItem(backboneelement.BackboneElement):
    """ Items to re-adjudicate.
    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """

    resource_type = Field("ProcessRequestItem", const=True)

    sequenceLinkId: fhirtypes.Integer = Field(
        ...,
        alias="sequenceLinkId",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Service instance",
    )
