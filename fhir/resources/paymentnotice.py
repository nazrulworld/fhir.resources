# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.
    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """

    resource_type = Field("PaymentNotice", const=True)

    amount: fhirtypes.MoneyType = Field(
        ...,
        alias="amount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Monetary amount of the payment",
    )

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for the payment noctice",
    )

    payee: fhirtypes.ReferenceType = Field(
        None,
        alias="payee",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description="Party being paid",
    )

    payment: fhirtypes.ReferenceType = Field(
        ...,
        alias="payment",
        title=(
            "Type `Reference` referencing `PaymentReconciliation` (represented as "
            "`dict` in JSON)"
        ),
        description="Payment reference",
    )

    paymentDate: fhirtypes.Date = Field(
        None,
        alias="paymentDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Payment or clearing date",
    )

    paymentStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="paymentStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Issued or cleared Status of the payment",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization` (represented as `dict` in JSON)"
        ),
        description="Responsible practitioner",
    )

    recipient: fhirtypes.ReferenceType = Field(
        ...,
        alias="recipient",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Party being notified",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Request reference",
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
        description="Response reference",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )
