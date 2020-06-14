# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.
    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """

    resource_type = Field("PaymentReconciliation", const=True)

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
    )

    detail: ListType[fhirtypes.PaymentReconciliationDetailType] = Field(
        None,
        alias="detail",
        title="List of `PaymentReconciliationDetail` items (represented as `dict` in JSON)",
        description="Settlement particulars",
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Disposition message",
    )

    formCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="formCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Printed form identifier",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for a payment reconciliation",
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="Type `Code` (represented as `dict` in JSON)",
        description="queued | complete | error | partial",
    )

    paymentAmount: fhirtypes.MoneyType = Field(
        ...,
        alias="paymentAmount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total amount of Payment",
    )

    paymentDate: fhirtypes.Date = Field(
        ...,
        alias="paymentDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When payment issued",
    )

    paymentIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="paymentIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Business identifier for the payment",
    )

    paymentIssuer: fhirtypes.ReferenceType = Field(
        None,
        alias="paymentIssuer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Party generating payment",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period covered",
    )

    processNote: ListType[fhirtypes.PaymentReconciliationProcessNoteType] = Field(
        None,
        alias="processNote",
        title="List of `PaymentReconciliationProcessNote` items (represented as `dict` in JSON)",
        description="Note concerning processing",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type `Reference` referencing `Task` (represented as `dict` in JSON)",
        description="Reference to requesting resource",
    )

    requestor: fhirtypes.ReferenceType = Field(
        None,
        alias="requestor",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Responsible practitioner",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )


class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ Settlement particulars.
    Distribution of the payment amount for a previously acknowledged payable.
    """

    resource_type = Field("PaymentReconciliationDetail", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Amount allocated to this payable",
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Date of commitment to pay",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Business identifier of the payment detail",
    )

    payee: fhirtypes.ReferenceType = Field(
        None,
        alias="payee",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Recipient of the payment",
    )

    predecessor: fhirtypes.IdentifierType = Field(
        None,
        alias="predecessor",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Business identifier of the prior payment detail",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Request giving rise to the payment",
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Response committing to a payment",
    )

    responsible: fhirtypes.ReferenceType = Field(
        None,
        alias="responsible",
        title="Type `Reference` referencing `PractitionerRole` (represented as `dict` in JSON)",
        description="Contact for the response",
    )

    submitter: fhirtypes.ReferenceType = Field(
        None,
        alias="submitter",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Submitter of the request",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Category of payment",
    )


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """ Note concerning processing.
    A note that describes or explains the processing in a human readable form.
    """

    resource_type = Field("PaymentReconciliationProcessNote", const=True)

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Note explanatory text",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="display | print | printoper",
    )
