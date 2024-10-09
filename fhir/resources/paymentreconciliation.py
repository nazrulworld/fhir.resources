from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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

    accountNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="accountNumber",
        title="Digits for verification",
        description=(
            "A portion of the account number, often the last 4 digits, used for "
            "verification not charging purposes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    accountNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_accountNumber", title="Extension field for ``accountNumber``."
    )

    allocation: typing.List[fhirtypes.PaymentReconciliationAllocationType] | None = Field(  # type: ignore
        None,
        alias="allocation",
        title="Settlement particulars",
        description=(
            "Distribution of the payment amount for a previously acknowledged "
            "payable."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    amount: fhirtypes.MoneyType = Field(  # type: ignore
        ...,
        alias="amount",
        title="Total amount of Payment",
        description="Total payment amount as indicated on the financial instrument.",
        json_schema_extra={
            "element_property": True,
        },
    )

    authorization: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="authorization",
        title="Authorization number",
        description=(
            "An alphanumeric issued by the processor to confirm the successful "
            "issuance of payment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    authorization__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_authorization", title="Extension field for ``authorization``."
    )

    cardBrand: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="cardBrand",
        title="Type of card",
        description=(
            "The card brand such as debit, Visa, Amex etc. used if a card is the "
            "method of payment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    cardBrand__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_cardBrand", title="Extension field for ``cardBrand``."
    )

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

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When payment issued",
        description="The date of payment as indicated on the financial instrument.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
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

    enterer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="enterer",
        title="Who entered the payment",
        description="Payment enterer if not the actual payment issuer.",
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

    expirationDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="expirationDate",
        title="Expiration year-month",
        description=(
            "The year and month (YYYY-MM) when the instrument, typically card, "
            "expires."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_expirationDate", title="Extension field for ``expirationDate``."
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

    issuerType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="issuerType",
        title="Nature of the source",
        description="The type of the source such as patient or insurance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    kind: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="kind",
        title="Workflow originating payment",
        description=(
            "The workflow or activity which gave rise to or during which the "
            "payment ocurred such as a kiosk, deposit on account, periodic payment "
            "etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where payment collected",
        description=(
            "The location of the site or device for electronic transfers or "
            "physical location for cash payments."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    method: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="method",
        title="Payment instrument",
        description=(
            "The means of payment such as check, card cash, or electronic funds "
            "transfer."
        ),
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
            "enum_reference_types": ["Organization", "Patient", "RelatedPerson"],
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

    processor: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="processor",
        title="Processor name",
        description="The name of the card processor, etf processor, bank for checks.",
        json_schema_extra={
            "element_property": True,
        },
    )
    processor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_processor", title="Extension field for ``processor``."
    )

    referenceNumber: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="referenceNumber",
        title="Check number or payment reference",
        description="The check number, eft reference, car processor reference.",
        json_schema_extra={
            "element_property": True,
        },
    )
    referenceNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_referenceNumber", title="Extension field for ``referenceNumber``."
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

    returnedAmount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="returnedAmount",
        title="Amount returned by the receiver",
        description=(
            "The amount returned by the receiver which is excess to the amount "
            "payable, often referred to as 'change'."
        ),
        json_schema_extra={
            "element_property": True,
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

    tenderedAmount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="tenderedAmount",
        title="Amount offered by the issuer",
        description=(
            "The amount offered by the issuer, typically applies to cash when the "
            "issuer provides an amount in bank note denominations equal to or "
            "excess of the amount actually being paid."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Category of payment",
        description=(
            "Code to indicate the nature of the payment such as payment, " "adjustment."
        ),
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
            "type",
            "status",
            "kind",
            "period",
            "created",
            "enterer",
            "issuerType",
            "paymentIssuer",
            "request",
            "requestor",
            "outcome",
            "disposition",
            "date",
            "location",
            "method",
            "cardBrand",
            "accountNumber",
            "expirationDate",
            "processor",
            "referenceNumber",
            "authorization",
            "tenderedAmount",
            "returnedAmount",
            "amount",
            "paymentIdentifier",
            "allocation",
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
            ("date", "date__ext"),
            ("status", "status__ext"),
        ]
        return required_fields


class PaymentReconciliationAllocation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Settlement particulars.
    Distribution of the payment amount for a previously acknowledged payable.
    """

    __resource_type__ = "PaymentReconciliationAllocation"

    account: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="account",
        title="Applied-to account",
        description=(
            "The Account to which this payment applies, may be completed by the "
            "receiver, used for search."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Account"],
        },
    )

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

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Applied-to encounter",
        description=(
            "The Encounter to which this payment applies, may be completed by the "
            "receiver, used for search."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
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
            "enum_reference_types": ["ClaimResponse"],
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

    target: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="target",
        title="Subject of the payment",
        description="Specific resource to which the payment/adjustment/advance applies.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Claim",
                "Account",
                "Invoice",
                "ChargeItem",
                "Encounter",
                "Contract",
            ],
        },
    )

    targetItemIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="targetItemIdentifier",
        title="Sub-element of the subject",
        description=(
            " Identifies the claim line item, encounter or other sub-element being "
            "paid. Note payment may be partial, that is not match the then "
            "outstanding balance or amount incurred."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e targetItem[x]
            "one_of_many": "targetItem",
            "one_of_many_required": False,
        },
    )

    targetItemPositiveInt: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="targetItemPositiveInt",
        title="Sub-element of the subject",
        description=(
            " Identifies the claim line item, encounter or other sub-element being "
            "paid. Note payment may be partial, that is not match the then "
            "outstanding balance or amount incurred."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e targetItem[x]
            "one_of_many": "targetItem",
            "one_of_many_required": False,
        },
    )
    targetItemPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_targetItemPositiveInt",
        title="Extension field for ``targetItemPositiveInt``.",
    )

    targetItemString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="targetItemString",
        title="Sub-element of the subject",
        description=(
            " Identifies the claim line item, encounter or other sub-element being "
            "paid. Note payment may be partial, that is not match the then "
            "outstanding balance or amount incurred."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e targetItem[x]
            "one_of_many": "targetItem",
            "one_of_many_required": False,
        },
    )
    targetItemString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_targetItemString",
        title="Extension field for ``targetItemString``.",
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
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
        ``PaymentReconciliationAllocation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "predecessor",
            "target",
            "targetItemString",
            "targetItemIdentifier",
            "targetItemPositiveInt",
            "encounter",
            "account",
            "type",
            "submitter",
            "response",
            "date",
            "responsible",
            "payee",
            "amount",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "targetItem": [
                "targetItemIdentifier",
                "targetItemPositiveInt",
                "targetItemString",
            ]
        }
        return one_of_many_fields


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
