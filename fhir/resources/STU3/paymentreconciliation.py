from __future__ import annotations as _annotations

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

    __resource_type__ = "PaymentReconciliation"

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    detail: typing.List[fhirtypes.PaymentReconciliationDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="List of settlements",
        description=(
            "List of individual settlement amounts and the corresponding "
            "transaction."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    disposition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    form: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="organization",
        title="Insurer",
        description="The Insurer who produced this adjudicated response.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    outcome: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Transaction status: error, complete.",
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Period covered",
        description=(
            "The period of time for which payments have been gathered into this "
            "bulk payment for settlement."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    processNote: typing.List[fhirtypes.PaymentReconciliationProcessNoteType] | None = Field(  # type: ignore
        None,
        alias="processNote",
        title="Processing comments",
        description="Suite of notes.",
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Claim reference",
        description="Original request resource reference.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ProcessRequest"],
        },
    )

    requestOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestOrganization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    requestProvider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestProvider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    total: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="total",
        title="Total amount of Payment",
        description="Total payment amount.",
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "PaymentReconciliationDetail"

    amount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Amount being paid",
        description="Amount paid for this detail.",
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Invoice date",
        description="The date of the invoice or financial resource.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    payee: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="payee",
        title="Organization which is receiving the payment",
        description="The organization which is receiving the payment.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Claim",
        description="The claim or financial resource.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    response: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="response",
        title="Claim Response",
        description="The claim response resource.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    submitter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="submitter",
        title="Organization which submitted the claim",
        description="The Organization which submitted the claim or financial transaction.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type code",
        description=(
            "Code to indicate the nature of the payment, adjustment, funds advance,"
            " etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "PaymentReconciliationProcessNote"

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Comment on the processing",
        description="The note text.",
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="display | print | printoper",
        description="The note purpose: Print/Display.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PaymentReconciliationProcessNote`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "text"]
