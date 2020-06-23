# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ProcessRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Request to perform some action on or in regards to an existing resource.
    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """

    resource_type = Field("ProcessRequest", const=True)

    action: fhirtypes.Code = Field(
        None,
        alias="action",
        title="Type `Code`",
        description="cancel | poll | reprocess | status",
    )
    action__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_action", title="Extension field for ``action``."
    )

    created: fhirtypes.DateTime = Field(
        None, alias="created", title="Type `DateTime`", description="Creation date"
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    exclude: ListType[fhirtypes.String] = Field(
        None,
        alias="exclude",
        title="List of `String` items",
        description="Resource type(s) to exclude",
    )
    exclude__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_exclude", title="Extension field for ``exclude``."
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
        title="List of `String` items",
        description="Resource type(s) to include",
    )
    include__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_include", title="Extension field for ``include``."
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
    nullify__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_nullify", title="Extension field for ``nullify``."
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
        title="Type `String`",
        description="Reference number/string",
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reference", title="Extension field for ``reference``."
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
        title="Type `Code`",
        description="active | cancelled | draft | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Items to re-adjudicate.
    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """

    resource_type = Field("ProcessRequestItem", const=True)

    sequenceLinkId: fhirtypes.Integer = Field(
        ...,
        alias="sequenceLinkId",
        title="Type `Integer`",
        description="Service instance",
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )
