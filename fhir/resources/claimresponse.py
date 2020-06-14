# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ClaimResponse(domainresource.DomainResource):
    """ Response to a claim predetermination or preauthorization.
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    resource_type = Field("ClaimResponse", const=True)

    addItem: ListType[fhirtypes.ClaimResponseAddItemType] = Field(
        None,
        alias="addItem",
        title="List of `ClaimResponseAddItem` items (represented as `dict` in JSON)",
        description="Insurer added line items",
    )

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON)",
        description="Header-level adjudication",
    )

    communicationRequest: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="communicationRequest",
        title="List of `Reference` items referencing `CommunicationRequest` (represented as `dict` in JSON)",
        description="Request for additional information",
    )

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Response creation date",
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Disposition Message",
    )

    error: ListType[fhirtypes.ClaimResponseErrorType] = Field(
        None,
        alias="error",
        title="List of `ClaimResponseError` items (represented as `dict` in JSON)",
        description="Processing errors",
    )

    form: fhirtypes.AttachmentType = Field(
        None,
        alias="form",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Printed reference or actual form",
    )

    formCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="formCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Printed form identifier",
    )

    fundsReserve: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fundsReserve",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Funds reserved status",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for a claim response",
    )

    insurance: ListType[fhirtypes.ClaimResponseInsuranceType] = Field(
        None,
        alias="insurance",
        title="List of `ClaimResponseInsurance` items (represented as `dict` in JSON)",
        description="Patient insurance information",
    )

    insurer: fhirtypes.ReferenceType = Field(
        ...,
        alias="insurer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Party responsible for reimbursement",
    )

    item: ListType[fhirtypes.ClaimResponseItemType] = Field(
        None,
        alias="item",
        title="List of `ClaimResponseItem` items (represented as `dict` in JSON)",
        description="Adjudication for claim line items",
    )

    outcome: fhirtypes.Code = Field(
        ...,
        alias="outcome",
        title="Type `Code` (represented as `dict` in JSON)",
        description="queued | complete | error | partial",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The recipient of the products and services",
    )

    payeeType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="payeeType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Party to be paid any benefits payable",
    )

    payment: fhirtypes.ClaimResponsePaymentType = Field(
        None,
        alias="payment",
        title="Type `ClaimResponsePayment` (represented as `dict` in JSON)",
        description="Payment Details",
    )

    preAuthPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="preAuthPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Preauthorization reference effective period",
    )

    preAuthRef: fhirtypes.String = Field(
        None,
        alias="preAuthRef",
        title="Type `String` (represented as `dict` in JSON)",
        description="Preauthorization reference",
    )

    processNote: ListType[fhirtypes.ClaimResponseProcessNoteType] = Field(
        None,
        alias="processNote",
        title="List of `ClaimResponseProcessNote` items (represented as `dict` in JSON)",
        description="Note concerning adjudication",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type `Reference` referencing `Claim` (represented as `dict` in JSON)",
        description="Id of resource triggering adjudication",
    )

    requestor: fhirtypes.ReferenceType = Field(
        None,
        alias="requestor",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Party responsible for the claim",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )

    subType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="More granular claim type",
    )

    total: ListType[fhirtypes.ClaimResponseTotalType] = Field(
        None,
        alias="total",
        title="List of `ClaimResponseTotal` items (represented as `dict` in JSON)",
        description="Adjudication totals",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="More granular claim type",
    )

    use: fhirtypes.Code = Field(
        ...,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="claim | preauthorization | predetermination",
    )


class ClaimResponseAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    The first-tier service adjudications for payor added product or service
    lines.
    """

    resource_type = Field("ClaimResponseAddItem", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        ...,
        alias="adjudication",
        title="List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON)",
        description="Added items adjudication",
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Anatomical location",
    )

    detail: ListType[fhirtypes.ClaimResponseAddItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ClaimResponseAddItemDetail` items (represented as `dict` in JSON)",
        description="Insurer added line details",
    )

    detailSequence: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="detailSequence",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Detail sequence number",
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Price scaling factor",
    )

    itemSequence: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="itemSequence",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Item sequence number",
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Place of service or where product was supplied",
        one_of_many="location",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    locationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="locationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Place of service or where product was supplied",
        one_of_many="location",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Place of service or where product was supplied",
        one_of_many="location",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Service/Product billing modifiers",
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total item cost",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable note numbers",
    )

    productOrService: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="productOrService",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing, service, product, or drug code",
    )

    programCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Program the product or service is provided under",
    )

    provider: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="provider",
        title="List of `Reference` items referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Authorized providers",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of products or services",
    )

    servicedDate: fhirtypes.Date = Field(
        None,
        alias="servicedDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Date or dates of service or product delivery",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    servicedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Date or dates of service or product delivery",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subSite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subSite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Anatomical sub-location",
    )

    subdetailSequence: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="subdetailSequence",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Subdetail sequence number",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per item",
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
            "location": [
                "locationAddress",
                "locationCodeableConcept",
                "locationReference",
            ],
            "serviced": ["servicedDate", "servicedPeriod",],
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


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """ Insurer added line details.
    The second-tier service adjudications for payor added services.
    """

    resource_type = Field("ClaimResponseAddItemDetail", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        ...,
        alias="adjudication",
        title="List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON)",
        description="Added items detail adjudication",
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Price scaling factor",
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Service/Product billing modifiers",
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total item cost",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable note numbers",
    )

    productOrService: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="productOrService",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing, service, product, or drug code",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of products or services",
    )

    subDetail: ListType[fhirtypes.ClaimResponseAddItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="List of `ClaimResponseAddItemDetailSubDetail` items (represented as `dict` in JSON)",
        description="Insurer added line items",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per item",
    )


class ClaimResponseAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    The third-tier service adjudications for payor added services.
    """

    resource_type = Field("ClaimResponseAddItemDetailSubDetail", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        ...,
        alias="adjudication",
        title="List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON)",
        description="Added items detail adjudication",
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Price scaling factor",
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Service/Product billing modifiers",
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total item cost",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable note numbers",
    )

    productOrService: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="productOrService",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing, service, product, or drug code",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of products or services",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per item",
    )


class ClaimResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    Errors encountered during the processing of the adjudication.
    """

    resource_type = Field("ClaimResponseError", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Error code detailing processing issues",
    )

    detailSequence: fhirtypes.PositiveInt = Field(
        None,
        alias="detailSequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Detail sequence number",
    )

    itemSequence: fhirtypes.PositiveInt = Field(
        None,
        alias="itemSequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Item sequence number",
    )

    subDetailSequence: fhirtypes.PositiveInt = Field(
        None,
        alias="subDetailSequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Subdetail sequence number",
    )


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """

    resource_type = Field("ClaimResponseInsurance", const=True)

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional provider contract number",
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title="Type `Reference` referencing `ClaimResponse` (represented as `dict` in JSON)",
        description="Adjudication results",
    )

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title="Type `Reference` referencing `Coverage` (represented as `dict` in JSON)",
        description="Insurance information",
    )

    focal: bool = Field(
        ...,
        alias="focal",
        title="Type `bool`",
        description="Coverage to be used for adjudication",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Insurance instance identifier",
    )


class ClaimResponseItem(backboneelement.BackboneElement):
    """ Adjudication for claim line items.
    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """

    resource_type = Field("ClaimResponseItem", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        ...,
        alias="adjudication",
        title="List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON)",
        description="Adjudication details",
    )

    detail: ListType[fhirtypes.ClaimResponseItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ClaimResponseItemDetail` items (represented as `dict` in JSON)",
        description="Adjudication for claim details",
    )

    itemSequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="itemSequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Claim item instance identifier",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable note numbers",
    )


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """

    resource_type = Field("ClaimResponseItemAdjudication", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Monetary amount",
    )

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of adjudication information",
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Explanation of adjudication outcome",
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Non-monetary value",
    )


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """ Adjudication for claim details.
    A claim detail. Either a simple (a product or service) or a 'group' of sub-
    details which are simple items.
    """

    resource_type = Field("ClaimResponseItemDetail", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        ...,
        alias="adjudication",
        title="List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON)",
        description="Detail level adjudication details",
    )

    detailSequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="detailSequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Claim detail instance identifier",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable note numbers",
    )

    subDetail: ListType[fhirtypes.ClaimResponseItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="List of `ClaimResponseItemDetailSubDetail` items (represented as `dict` in JSON)",
        description="Adjudication for claim sub-details",
    )


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """ Adjudication for claim sub-details.
    A sub-detail adjudication of a simple product or service.
    """

    resource_type = Field("ClaimResponseItemDetailSubDetail", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON)",
        description="Subdetail level adjudication details",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable note numbers",
    )

    subDetailSequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="subDetailSequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Claim sub-detail instance identifier",
    )


class ClaimResponsePayment(backboneelement.BackboneElement):
    """ Payment Details.
    Payment details for the adjudication of the claim.
    """

    resource_type = Field("ClaimResponsePayment", const=True)

    adjustment: fhirtypes.MoneyType = Field(
        None,
        alias="adjustment",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Payment adjustment for non-claim issues",
    )

    adjustmentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="adjustmentReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Explanation for the adjustment",
    )

    amount: fhirtypes.MoneyType = Field(
        ...,
        alias="amount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Payable amount after adjustment",
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Expected date of payment",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Business identifier for the payment",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Partial or complete payment",
    )


class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """ Note concerning adjudication.
    A note that describes or explains adjudication results in a human readable
    form.
    """

    resource_type = Field("ClaimResponseProcessNote", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Language of the text",
    )

    number: fhirtypes.PositiveInt = Field(
        None,
        alias="number",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Note instance identifier",
    )

    text: fhirtypes.String = Field(
        ...,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Note explanatory text",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="display | print | printoper",
    )


class ClaimResponseTotal(backboneelement.BackboneElement):
    """ Adjudication totals.
    Categorized monetary totals for the adjudication.
    """

    resource_type = Field("ClaimResponseTotal", const=True)

    amount: fhirtypes.MoneyType = Field(
        ...,
        alias="amount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Financial total for the category",
    )

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of adjudication information",
    )
