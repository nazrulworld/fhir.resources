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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    PaymentNotice request.
    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """

    resource_type = Field("PaymentNotice", const=True)

    amount: fhirtypes.MoneyType = Field(
        ...,
        alias="amount",
        title="Monetary amount of the payment",
        description="The amount sent to the payee.",
        # if property is element of this resource.
        element_property=True,
    )

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for the payment noctice",
        description="A unique identifier assigned to this payment notice.",
        # if property is element of this resource.
        element_property=True,
    )

    payee: fhirtypes.ReferenceType = Field(
        None,
        alias="payee",
        title="Party being paid",
        description=(
            "The party who will receive or has received payment that is the subject"
            " of this notification."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    payment: fhirtypes.ReferenceType = Field(
        ...,
        alias="payment",
        title="Payment reference",
        description="A reference to the payment which is the subject of this notice.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PaymentReconciliation"],
    )

    paymentDate: fhirtypes.Date = Field(
        None,
        alias="paymentDate",
        title="Payment or clearing date",
        description="The date when the above payment action occurred.",
        # if property is element of this resource.
        element_property=True,
    )
    paymentDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_paymentDate", title="Extension field for ``paymentDate``."
    )

    paymentStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="paymentStatus",
        title="Issued or cleared Status of the payment",
        description="A code indicating whether payment has been sent or cleared.",
        # if property is element of this resource.
        element_property=True,
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    recipient: fhirtypes.ReferenceType = Field(
        ...,
        alias="recipient",
        title="Party being notified",
        description="The party who is notified of the payment status.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Request reference",
        description="Reference of resource for which payment is being made.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title="Response reference",
        description="Reference of response to resource for which payment is being made.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    status: fhirtypes.Code = Field(
        ...,
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
