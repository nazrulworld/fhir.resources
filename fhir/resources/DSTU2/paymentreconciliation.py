# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/paymentreconciliation.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class PaymentReconciliation(domainresource.DomainResource):
    """PaymentReconciliation resource


    This resource provides payment details and claim references
    supporting a bulk payment.
    """

    resource_type = Field("PaymentReconciliation", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description="The Response business identifier.",
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type 'Reference' referencing 'ProcessRequest'  (represented as 'dict' in JSON).",
        description="Claim reference",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ProcessRequest"],
        element_property=True,
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="Type `Code` (represented as `dict` in JSON).",
        description="complete | error",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["complete", "error"],
        element_property=True,
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Disposition Message",
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
        description="The date when the enclosed suite of services were performed or completed.",
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period covered",
        description=(
            "The period of time for which payments have been "
            "gathered into this bulk payment for settlement."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Type 'Reference' referencing 'Organization'  (represented as 'dict' in JSON).",
        description="Insurer",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        element_property=True,
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Type 'Reference' referencing 'Practitioner'  (represented as 'dict' in JSON).",
        description="Responsible practitioner",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
        element_property=True,
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Type 'Reference' referencing 'Organization'  (represented as 'dict' in JSON).",
        description="Responsible organization",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        element_property=True,
    )

    detail: ListType[fhirtypes.PaymentReconciliationDetailType] = Field(
        None,
        alias="detail",
        title="Details",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    form: fhirtypes.CodingType = Field(
        None,
        alias="form",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Printed Form Identifier",
        element_property=True,
    )

    total: fhirtypes.MoneyType = Field(
        None,
        alias="total",
        title="Total amount of Payment",
        description="Type `Money` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )

    note: ListType[fhirtypes.PaymentReconciliationNoteType] = Field(
        None,
        alias="detail",
        title="Details",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class PaymentReconciliationDetail(BackboneElement):
    """Details


    List of individual settlement amounts and the corresponding transaction.
    """

    resource_type = Field("PaymentReconciliationDetail", const=True)

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Type code",
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Claim",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title="Type 'Reference' referencing 'Any'  (represented as 'dict' in JSON).",
        description="Claim Response",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Any"],
        element_property=True,
    )

    submitter: fhirtypes.ReferenceType = Field(
        None,
        alias="submitter",
        title="Type 'Reference' referencing 'Organization'  (represented as 'dict' in JSON).",
        description="Submitter",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        element_property=True,
    )

    payee: fhirtypes.ReferenceType = Field(
        None,
        alias="payee",
        title="Type 'Reference' referencing 'Organization'  (represented as 'dict' in JSON).",
        description="Payee",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        element_property=True,
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Type `Date`.",
        description="Invoice date",
        element_property=True,
    )

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Detail amount",
        description="Type `Money` (represented as `dict` in JSON).",
        # if property is element of this resource.
        element_property=True,
    )


class PaymentReconciliationNote(BackboneElement):
    """Note text


    Suite of notes.
    """

    resource_type = Field("PaymentReconciliationNote", const=True)

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="display | print | printoper",
        element_property=True,
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Notes text",
        element_property=True,
    )
