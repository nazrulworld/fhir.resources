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
        title="cancel | poll | reprocess | status",
        description=(
            "The type of processing action being requested, for example Reversal, "
            "Readjudication, StatusRequest,PendedRequest."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["cancel", "poll", "reprocess", "status"],
    )
    action__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_action", title="Extension field for ``action``."
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    exclude: ListType[fhirtypes.String] = Field(
        None,
        alias="exclude",
        title="Resource type(s) to exclude",
        description="Names of resource types to exclude.",
        # if property is element of this resource.
        element_property=True,
    )
    exclude__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The ProcessRequest business identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    include: ListType[fhirtypes.String] = Field(
        None,
        alias="include",
        title="Resource type(s) to include",
        description="Names of resource types to include.",
        # if property is element of this resource.
        element_property=True,
    )
    include__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_include", title="Extension field for ``include``."
    )

    item: ListType[fhirtypes.ProcessRequestItemType] = Field(
        None,
        alias="item",
        title="Items to re-adjudicate",
        description=(
            "List of top level items to be re-adjudicated, if none specified then "
            "the entire submission is re-adjudicated."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    nullify: bool = Field(
        None,
        alias="nullify",
        title="Remove history",
        description="If true remove all history excluding audit.",
        # if property is element of this resource.
        element_property=True,
    )
    nullify__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_nullify", title="Extension field for ``nullify``."
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the action speccified in "
            "this request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Selection period",
        description=(
            "A period of time during which the fulfilling resources would have been"
            " created."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the action specified in this "
            "request."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    reference: fhirtypes.String = Field(
        None,
        alias="reference",
        title="Reference number/string",
        description="A reference to supply which authenticates the process.",
        # if property is element of this resource.
        element_property=True,
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reference", title="Extension field for ``reference``."
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Reference to the Request resource",
        description="Reference of resource which is the target or subject of this action.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title="Reference to the Response resource",
        description=(
            "Reference of a prior response to resource which is the target or "
            "subject of this action."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title="Party which is the target of the request",
        description="The organization which is the target of the request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
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
        title="Service instance",
        description="A service line number.",
        # if property is element of this resource.
        element_property=True,
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )
