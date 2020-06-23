# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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

    created: fhirtypes.DateTime = Field(
        None, alias="created", title="Type `DateTime`", description="Creation date"
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
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
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible organization",
    )

    paymentStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="paymentStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Whether payment has been sent or cleared",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible practitioner",
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
        None,
        alias="status",
        title="Type `Code`",
        description="active | cancelled | draft | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusDate: fhirtypes.Date = Field(
        None,
        alias="statusDate",
        title="Type `Date`",
        description="Payment or clearing date",
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Insurer or Regulatory body",
    )
