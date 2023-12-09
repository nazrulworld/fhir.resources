# -*- coding: utf-8 -*-
"""
Profile: None
Release: DSTU2
Version: 1.0.2
Revision: None
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .domainresource import DomainResource


class OrderResponse(DomainResource):
    """
    The response to an order indicates the outcome of processing the order
    itself - whether it was accepted or rejected, or is still in process. The
    order response resource does not itself convey or represent information that
    arises as a result of performing the actual order, but it may have
    references to other resources that do have this information, in order to
    link between the original order and its outcome.
    """

    resource_type = Field("OrderResponse", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Identifiers assigned to this order by the orderer or by the receiver",
        # if property is element of this resource.
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        ...,
        alias="request",
        title="request",
        description="The order that this is a response to.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Order"],
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="date",
        description="When the response was made.",
        # if property is element of this resource.
        element_property=True,
    )

    who: fhirtypes.ReferenceType = Field(
        None,
        alias="who",
        title="who",
        description="Who made the response.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization", "Device"],
    )

    orderStatus: fhirtypes.Code = Field(
        ...,
        alias="orderStatus",
        title="Type `Code`",
        description=(
            "pending | review | rejected | error | accepted "
            "| cancelled | replaced | aborted | completed."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="description",
        description="Additional description of the response",
        # if property is element of this resource.
        element_property=True,
    )

    fulfillment: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="fulfillment",
        title="fulfillment",
        description="Details of the outcome of performing the order.",
        # if property is element of this resource.
        element_property=True,
    )
