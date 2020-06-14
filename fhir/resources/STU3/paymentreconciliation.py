# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.
    This resource provides payment details and claim references supporting a
    bulk payment.
    """

    resource_type = Field("PaymentReconciliation", const=True)

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
    )

    detail: ListType[fhirtypes.PaymentReconciliationDetailType] = Field(
        None,
        alias="detail",
        title="List of `PaymentReconciliationDetail` items (represented as `dict` in JSON)",
        description="List of settlements",
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Disposition Message",
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Printed Form Identifier",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Insurer",
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="complete | error | partial",
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
        description="Processing comments",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type `Reference` referencing `ProcessRequest` (represented as `dict` in JSON)",
        description="Claim reference",
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Responsible organization",
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON)",
        description="Responsible practitioner",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )

    total: fhirtypes.MoneyType = Field(
        None,
        alias="total",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total amount of Payment",
    )


class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ List of settlements.
    List of individual settlement amounts and the corresponding transaction.
    """

    resource_type = Field("PaymentReconciliationDetail", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Amount being paid",
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Invoice date",
    )

    payee: fhirtypes.ReferenceType = Field(
        None,
        alias="payee",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization which is receiving the payment",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Claim",
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Claim Response",
    )

    submitter: fhirtypes.ReferenceType = Field(
        None,
        alias="submitter",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization which submitted the claim",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type code",
    )


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """ Processing comments.
    Suite of notes.
    """

    resource_type = Field("PaymentReconciliationProcessNote", const=True)

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Comment on the processing",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="display | print | printoper",
    )
