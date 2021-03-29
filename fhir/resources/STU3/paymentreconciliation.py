# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class PaymentReconciliation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    PaymentReconciliation resource.
    This resource provides payment details and claim references supporting a
    bulk payment.
    """

    resource_type = Field("PaymentReconciliation", const=True)

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    detail: typing.List[fhirtypes.PaymentReconciliationDetailType] = Field(
        None,
        alias="detail",
        title="List of settlements",
        description=(
            "List of individual settlement amounts and the corresponding "
            "transaction."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
        # if property is element of this resource.
        element_property=True,
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Insurer",
        description="The Insurer who produced this adjudicated response.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Transaction status: error, complete.",
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period covered",
        description=(
            "The period of time for which payments have been gathered into this "
            "bulk payment for settlement."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    processNote: typing.List[fhirtypes.PaymentReconciliationProcessNoteType] = Field(
        None,
        alias="processNote",
        title="Processing comments",
        description="Suite of notes.",
        # if property is element of this resource.
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Claim reference",
        description="Original request resource reference.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ProcessRequest"],
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
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

    total: fhirtypes.MoneyType = Field(
        None,
        alias="total",
        title="Total amount of Payment",
        description="Total payment amount.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PaymentReconciliation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "status",
            "period",
            "created",
            "organization",
            "request",
            "outcome",
            "disposition",
            "requestProvider",
            "requestOrganization",
            "detail",
            "form",
            "total",
            "processNote",
        ]


class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of settlements.
    List of individual settlement amounts and the corresponding transaction.
    """

    resource_type = Field("PaymentReconciliationDetail", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Amount being paid",
        description="Amount paid for this detail.",
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Invoice date",
        description="The date of the invoice or financial resource.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    payee: fhirtypes.ReferenceType = Field(
        None,
        alias="payee",
        title="Organization which is receiving the payment",
        description="The organization which is receiving the payment.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Claim",
        description="The claim or financial resource.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title="Claim Response",
        description="The claim response resource.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    submitter: fhirtypes.ReferenceType = Field(
        None,
        alias="submitter",
        title="Organization which submitted the claim",
        description="The Organization which submitted the claim or financial transaction.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type code",
        description=(
            "Code to indicate the nature of the payment, adjustment, funds advance,"
            " etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PaymentReconciliationDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "request",
            "response",
            "submitter",
            "payee",
            "date",
            "amount",
        ]


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing comments.
    Suite of notes.
    """

    resource_type = Field("PaymentReconciliationProcessNote", const=True)

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Comment on the processing",
        description="The note text.",
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="display | print | printoper",
        description="The note purpose: Print/Display.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PaymentReconciliationProcessNote`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "text"]
