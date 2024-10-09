from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class PaymentNotice(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    PaymentNotice request.
    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """

    __resource_type__ = "PaymentNotice"

    amount: fhirtypes.MoneyType = Field(  # type: ignore
        ...,
        alias="amount",
        title="Monetary amount of the payment",
        description="The amount sent to the payee.",
        json_schema_extra={
            "element_property": True,
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for the payment notice",
        description="A unique identifier assigned to this payment notice.",
        json_schema_extra={
            "element_property": True,
        },
    )

    payee: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="payee",
        title="Party being paid",
        description=(
            "The party who will receive or has received payment that is the subject"
            " of this notification."
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

    payment: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="payment",
        title="Payment reference",
        description="A reference to the payment which is the subject of this notice.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PaymentReconciliation"],
        },
    )

    paymentDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="paymentDate",
        title="Payment or clearing date",
        description="The date when the above payment action occurred.",
        json_schema_extra={
            "element_property": True,
        },
    )
    paymentDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_paymentDate", title="Extension field for ``paymentDate``."
    )

    paymentStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="paymentStatus",
        title="Issued or cleared Status of the payment",
        description="A code indicating whether payment has been sent or cleared.",
        json_schema_extra={
            "element_property": True,
        },
    )

    recipient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="recipient",
        title="Party being notified",
        description="The party who is notified of the payment status.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    reporter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reporter",
        title="Responsible practitioner",
        description="The party who reports the payment notice.",
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

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Request reference",
        description="Reference of resource for which payment is being made.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    response: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="response",
        title="Response reference",
        description="Reference of response to resource for which payment is being made.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
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
        ``PaymentNotice`` according specification,
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
            "request",
            "response",
            "created",
            "reporter",
            "payment",
            "paymentDate",
            "payee",
            "recipient",
            "amount",
            "paymentStatus",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("created", "created__ext"), ("status", "status__ext")]
        return required_fields
