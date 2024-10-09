from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class PaymentReconciliation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    PaymentReconciliation resource.
    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """

    __resource_type__ = "PaymentReconciliation"

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Creation date",
        description="The date when the resource was created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    detail: typing.List[fhirtypes.PaymentReconciliationDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Settlement particulars",
        description=(
            "Distribution of the payment amount for a previously acknowledged "
            "payable."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    disposition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="disposition",
        title="Disposition message",
        description=(
            "A human readable description of the status of the request for the "
            "reconciliation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    formCode: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="formCode",
        title="Printed form identifier",
        description="A code for the form to be used for printing the content.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for a payment reconciliation",
        description="A unique identifier assigned to this payment reconciliation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    outcome: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="queued | complete | error | partial",
        description="The outcome of a request for a reconciliation.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["queued", "complete", "error", "partial"],
        },
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    paymentAmount: fhirtypes.MoneyType = Field(  # type: ignore
        ...,
        alias="paymentAmount",
        title="Total amount of Payment",
        description="Total payment amount as indicated on the financial instrument.",
        json_schema_extra={
            "element_property": True,
        },
    )

    paymentDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="paymentDate",
        title="When payment issued",
        description="The date of payment as indicated on the financial instrument.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    paymentDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_paymentDate", title="Extension field for ``paymentDate``."
    )

    paymentIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="paymentIdentifier",
        title="Business identifier for the payment",
        description="Issuer's unique identifier for the payment instrument.",
        json_schema_extra={
            "element_property": True,
        },
    )

    paymentIssuer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="paymentIssuer",
        title="Party generating payment",
        description="The party who generated the payment.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
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
        title="Note concerning processing",
        description=(
            "A note that describes or explains the processing in a human readable "
            "form."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Reference to requesting resource",
        description="Original request resource reference.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Task"],
        },
    )

    requestor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestor",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
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
            "paymentIssuer",
            "request",
            "requestor",
            "outcome",
            "disposition",
            "paymentDate",
            "paymentAmount",
            "paymentIdentifier",
            "detail",
            "formCode",
            "processNote",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("created", "created__ext"),
            ("paymentDate", "paymentDate__ext"),
            ("status", "status__ext"),
        ]
        return required_fields


class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Settlement particulars.
    Distribution of the payment amount for a previously acknowledged payable.
    """

    __resource_type__ = "PaymentReconciliationDetail"

    amount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Amount allocated to this payable",
        description="The monetary amount allocated from the total payment to the payable.",
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date of commitment to pay",
        description="The date from the response resource containing a commitment to pay.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier of the payment detail",
        description=(
            "Unique identifier for the current payment item for the referenced "
            "payable."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    payee: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="payee",
        title="Recipient of the payment",
        description="The party which is receiving the payment.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    predecessor: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="predecessor",
        title="Business identifier of the prior payment detail",
        description=(
            "Unique identifier for the prior payment item for the referenced "
            "payable."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Request giving rise to the payment",
        description=(
            "A resource, such as a Claim, the evaluation of which could lead to "
            "payment."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    response: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="response",
        title="Response committing to a payment",
        description=(
            "A resource, such as a ClaimResponse, which contains a commitment to "
            "payment."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    responsible: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="responsible",
        title="Contact for the response",
        description=(
            "A reference to the individual who is responsible for inquiries "
            "regarding the response and its payment."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PractitionerRole"],
        },
    )

    submitter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="submitter",
        title="Submitter of the request",
        description="The party which submitted the claim or financial transaction.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Category of payment",
        description="Code to indicate the nature of the payment.",
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
            "identifier",
            "predecessor",
            "type",
            "request",
            "submitter",
            "response",
            "date",
            "responsible",
            "payee",
            "amount",
        ]


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Note concerning processing.
    A note that describes or explains the processing in a human readable form.
    """

    __resource_type__ = "PaymentReconciliationProcessNote"

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Note explanatory text",
        description="The explanation or description associated with the processing.",
        json_schema_extra={
            "element_property": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="display | print | printoper",
        description="The business purpose of the note text.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["display", "print", "printoper"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PaymentReconciliationProcessNote`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "text"]
