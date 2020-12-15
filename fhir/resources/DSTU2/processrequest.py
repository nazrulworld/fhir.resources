# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/processrequest.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class ProcessRequest(domainresource.DomainResource):
    """Process request


    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """

    resource_type = Field("ProcessRequest", const=True)

    action: fhirtypes.Code = Field(
        None,
        alias="action",
        title="Type `Code` (represented as `dict` in JSON).",
        description="cancel | poll | reprocess | status",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["cancel", "poll", "reprocess", "status"],
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="The ProcessRequest business identifier.",
        element_property=True,
    )

    ruleset: fhirtypes.CodingType = Field(
        None,
        alias="ruleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Resource version",
        element_property=True,
    )

    originalRuleset: fhirtypes.CodingType = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original version",
        element_property=True,
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        element_property=True,
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title="Type 'Reference' referencing 'Organization'  (represented as 'dict' in JSON).",
        description="Target of the request",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        element_property=True,
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Type 'Reference' referencing 'Practitioner'  (represented as 'dict' in JSON).",
        description="Responsible organization",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Request reference",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Response reference",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    nullify: bool = Field(
        None,
        alias="nullify",
        title="Nullify",
        description="If true remove all history excluding audit.",
        # if property is element of this resource.
        element_property=True,
    )

    reference: fhirtypes.String = Field(
        None,
        alias="reference",
        title="Type `String` (represented as `dict` in JSON)",
        description="Reference number/string",
        element_property=True,
    )

    item: ListType[fhirtypes.ProcessRequestItemType] = Field(
        None,
        alias="item",
        title="Items to re-adjudicate",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    include: ListType[fhirtypes.String] = Field(
        None,
        alias="include",
        title="Type `String` (represented as `dict` in JSON)",
        description="Resource type(s) to include",
        element_property=True,
    )

    exclude: ListType[fhirtypes.String] = Field(
        None,
        alias="exclude",
        title="Type `String` (represented as `dict` in JSON)",
        description="Resource type(s) to exclude",
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period",
        description=(
            "A period of time during which the fulfilling "
            "resources would have been created."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class ProcessRequestItem(BackboneElement):
    """Items to re-adjudicate


    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated..
    """

    resource_type = Field("ProcessRequestItem", const=True)

    sequenceLinkId: fhirtypes.Integer = Field(
        None,
        alias="sequenceLinkId",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Service instance",
    )
