# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Invoice
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Invoice(domainresource.DomainResource):
    """ Invoice containing ChargeItems from an Account.
    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """

    resource_type = Field("Invoice", const=True)

    account: fhirtypes.ReferenceType = Field(
        None,
        alias="account",
        title="Type `Reference` referencing `Account` (represented as `dict` in JSON)",
        description="Account that is being balanced",
    )

    cancelledReason: fhirtypes.String = Field(
        None,
        alias="cancelledReason",
        title="Type `String` (represented as `dict` in JSON)",
        description="Reason for cancellation of this Invoice",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Invoice date / posting date",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for item",
    )

    issuer: fhirtypes.ReferenceType = Field(
        None,
        alias="issuer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Issuing Organization of Invoice",
    )

    lineItem: ListType[fhirtypes.InvoiceLineItemType] = Field(
        None,
        alias="lineItem",
        title="List of `InvoiceLineItem` items (represented as `dict` in JSON)",
        description="Line items of this Invoice",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about the invoice",
    )

    participant: ListType[fhirtypes.InvoiceParticipantType] = Field(
        None,
        alias="participant",
        title="List of `InvoiceParticipant` items (represented as `dict` in JSON)",
        description="Participant in creation of this Invoice",
    )

    paymentTerms: fhirtypes.Markdown = Field(
        None,
        alias="paymentTerms",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Payment details",
    )

    recipient: fhirtypes.ReferenceType = Field(
        None,
        alias="recipient",
        title="Type `Reference` referencing `Organization, Patient, RelatedPerson` (represented as `dict` in JSON)",
        description="Recipient of this invoice",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | issued | balanced | cancelled | entered-in-error",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Recipient(s) of goods and services",
    )

    totalGross: fhirtypes.MoneyType = Field(
        None,
        alias="totalGross",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Gross total of this Invoice",
    )

    totalNet: fhirtypes.MoneyType = Field(
        None,
        alias="totalNet",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Net total of this Invoice",
    )

    totalPriceComponent: ListType[fhirtypes.InvoiceLineItemPriceComponentType] = Field(
        None,
        alias="totalPriceComponent",
        title="List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON)",
        description="Components of Invoice total",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of Invoice",
    )


class InvoiceLineItem(backboneelement.BackboneElement):
    """ Line items of this Invoice.
    Each line item represents one charge for goods and services rendered.
    Details such as date, code and amount are found in the referenced
    ChargeItem resource.
    """

    resource_type = Field("InvoiceLineItem", const=True)

    chargeItemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="chargeItemCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reference to ChargeItem containing details of this line item or an inline billing code",
        one_of_many="chargeItem",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    chargeItemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="chargeItemReference",
        title="Type `Reference` referencing `ChargeItem` (represented as `dict` in JSON)",
        description="Reference to ChargeItem containing details of this line item or an inline billing code",
        one_of_many="chargeItem",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    priceComponent: ListType[fhirtypes.InvoiceLineItemPriceComponentType] = Field(
        None,
        alias="priceComponent",
        title="List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON)",
        description="Components of total line item price",
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Sequence number of line item",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
            "chargeItem": ["chargeItemCodeableConcept", "chargeItemReference",],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class InvoiceLineItemPriceComponent(backboneelement.BackboneElement):
    """ Components of total line item price.
    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice as to how the prices have been calculated.
    """

    resource_type = Field("InvoiceLineItemPriceComponent", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Monetary amount associated with this component",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Code identifying the specific component",
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Factor used for calculating this component",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="base | surcharge | deduction | discount | tax | informational",
    )


class InvoiceParticipant(backboneelement.BackboneElement):
    """ Participant in creation of this Invoice.
    Indicates who or what performed or participated in the charged service.
    """

    resource_type = Field("InvoiceParticipant", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Type `Reference` referencing `Practitioner, Organization, Patient, PractitionerRole, Device, RelatedPerson` (represented as `dict` in JSON)",
        description="Individual who was involved",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of involvement in creation of this Invoice",
    )
