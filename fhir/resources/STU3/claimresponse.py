# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ClaimResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Remittance resource.
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

    communicationRequest: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="communicationRequest",
        title=(
            "List of `Reference` items referencing `CommunicationRequest` "
            "(represented as `dict` in JSON)"
        ),
        description="Request for additional information",
    )

    created: fhirtypes.DateTime = Field(
        None, alias="created", title="Type `DateTime`", description="Creation date"
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String`",
        description="Disposition Message",
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    error: ListType[fhirtypes.ClaimResponseErrorType] = Field(
        None,
        alias="error",
        title="List of `ClaimResponseError` items (represented as `dict` in JSON)",
        description="Processing errors",
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Printed Form Identifier",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Response  number",
    )

    insurance: ListType[fhirtypes.ClaimResponseInsuranceType] = Field(
        None,
        alias="insurance",
        title="List of `ClaimResponseInsurance` items (represented as `dict` in JSON)",
        description="Insurance or medical plan",
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Insurance issuing organization",
    )

    item: ListType[fhirtypes.ClaimResponseItemType] = Field(
        None,
        alias="item",
        title="List of `ClaimResponseItem` items (represented as `dict` in JSON)",
        description="Line items",
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="complete | error | partial",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The subject of the Products and Services",
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
        description="Payment details, if paid",
    )

    processNote: ListType[fhirtypes.ClaimResponseProcessNoteType] = Field(
        None,
        alias="processNote",
        title=(
            "List of `ClaimResponseProcessNote` items (represented as `dict` in "
            "JSON)"
        ),
        description="Processing notes",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Type `Reference` referencing `Claim` (represented as `dict` in JSON)",
        description="Id of resource triggering adjudication",
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible organization",
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible practitioner",
    )

    reserved: fhirtypes.CodingType = Field(
        None,
        alias="reserved",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Funds reserved status",
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

    totalBenefit: fhirtypes.MoneyType = Field(
        None,
        alias="totalBenefit",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total benefit payable for the Claim",
    )

    totalCost: fhirtypes.MoneyType = Field(
        None,
        alias="totalCost",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total Cost of service from the Claim",
    )

    unallocDeductable: fhirtypes.MoneyType = Field(
        None,
        alias="unallocDeductable",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Unallocated deductible",
    )


class ClaimResponseAddItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The first tier service adjudications for payor added services.
    """

    resource_type = Field("ClaimResponseAddItem", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title=(
            "List of `ClaimResponseItemAdjudication` items (represented as `dict` "
            "in JSON)"
        ),
        description="Added items adjudication",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of service or product",
    )

    detail: ListType[fhirtypes.ClaimResponseAddItemDetailType] = Field(
        None,
        alias="detail",
        title=(
            "List of `ClaimResponseAddItemDetail` items (represented as `dict` in "
            "JSON)"
        ),
        description="Added items details",
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Professional fee or Product charge",
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Service/Product billing modifiers",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items",
        description="List of note numbers which apply",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Revenue or cost center code",
    )

    sequenceLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="sequenceLinkId",
        title="List of `PositiveInt` items",
        description="Service instances",
    )
    sequenceLinkId__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Group, Service or Product",
    )


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Added items details.
    The second tier service adjudications for payor added services.
    """

    resource_type = Field("ClaimResponseAddItemDetail", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title=(
            "List of `ClaimResponseItemAdjudication` items (represented as `dict` "
            "in JSON)"
        ),
        description="Added items detail adjudication",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of service or product",
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Professional fee or Product charge",
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Service/Product billing modifiers",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items",
        description="List of note numbers which apply",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Revenue or cost center code",
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Service or Product",
    )


class ClaimResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Mutually exclusive with Services Provided (Item).
    """

    resource_type = Field("ClaimResponseError", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Error code detailing processing issues",
    )

    detailSequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="detailSequenceLinkId",
        title="Type `PositiveInt`",
        description="Detail sequence number",
    )
    detailSequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_detailSequenceLinkId",
        title="Extension field for ``detailSequenceLinkId``.",
    )

    sequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="sequenceLinkId",
        title="Type `PositiveInt`",
        description="Item sequence number",
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    subdetailSequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="subdetailSequenceLinkId",
        title="Type `PositiveInt`",
        description="Subdetail sequence number",
    )
    subdetailSequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_subdetailSequenceLinkId",
        title="Extension field for ``subdetailSequenceLinkId``.",
    )


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan.
    Financial instrument by which payment information for health care.
    """

    resource_type = Field("ClaimResponseInsurance", const=True)

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Type `String`",
        description="Business agreement",
    )
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_businessArrangement",
        title="Extension field for ``businessArrangement``.",
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title=(
            "Type `Reference` referencing `ClaimResponse` (represented as `dict` in"
            " JSON)"
        ),
        description="Adjudication results",
    )

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title=(
            "Type `Reference` referencing `Coverage` (represented as `dict` in " "JSON)"
        ),
        description="Insurance information",
    )

    focal: bool = Field(
        ..., alias="focal", title="Type `bool`", description="Is the focal Coverage"
    )
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_focal", title="Extension field for ``focal``."
    )

    preAuthRef: ListType[fhirtypes.String] = Field(
        None,
        alias="preAuthRef",
        title="List of `String` items",
        description="Pre-Authorization/Determination Reference",
    )
    preAuthRef__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_preAuthRef", title="Extension field for ``preAuthRef``.")

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt`",
        description="Service instance identifier",
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )


class ClaimResponseItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Line items.
    The first tier service adjudications for submitted services.
    """

    resource_type = Field("ClaimResponseItem", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title=(
            "List of `ClaimResponseItemAdjudication` items (represented as `dict` "
            "in JSON)"
        ),
        description="Adjudication details",
    )

    detail: ListType[fhirtypes.ClaimResponseItemDetailType] = Field(
        None,
        alias="detail",
        title=(
            "List of `ClaimResponseItemDetail` items (represented as `dict` in " "JSON)"
        ),
        description="Detail line items",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items",
        description="List of note numbers which apply",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    sequenceLinkId: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequenceLinkId",
        title="Type `PositiveInt`",
        description="Service instance",
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication details.
    The adjudication results.
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
        description="Adjudication category such as co-pay, eligible, benefit, etc.",
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Explanation of Adjudication outcome",
    )

    value: fhirtypes.Decimal = Field(
        None, alias="value", title="Type `Decimal`", description="Non-monetary value"
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Detail line items.
    The second tier service adjudications for submitted services.
    """

    resource_type = Field("ClaimResponseItemDetail", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title=(
            "List of `ClaimResponseItemAdjudication` items (represented as `dict` "
            "in JSON)"
        ),
        description="Detail level adjudication details",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items",
        description="List of note numbers which apply",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    sequenceLinkId: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequenceLinkId",
        title="Type `PositiveInt`",
        description="Service instance",
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    subDetail: ListType[fhirtypes.ClaimResponseItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title=(
            "List of `ClaimResponseItemDetailSubDetail` items (represented as "
            "`dict` in JSON)"
        ),
        description="Subdetail line items",
    )


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Subdetail line items.
    The third tier service adjudications for submitted services.
    """

    resource_type = Field("ClaimResponseItemDetailSubDetail", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title=(
            "List of `ClaimResponseItemAdjudication` items (represented as `dict` "
            "in JSON)"
        ),
        description="Subdetail level adjudication details",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items",
        description="List of note numbers which apply",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    sequenceLinkId: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequenceLinkId",
        title="Type `PositiveInt`",
        description="Service instance",
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )


class ClaimResponsePayment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Payment details, if paid.
    Payment details for the claim if the claim has been paid.
    """

    resource_type = Field("ClaimResponsePayment", const=True)

    adjustment: fhirtypes.MoneyType = Field(
        None,
        alias="adjustment",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Payment adjustment for non-Claim issues",
    )

    adjustmentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="adjustmentReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Explanation for the non-claim adjustment",
    )

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Payable amount after adjustment",
    )

    date: fhirtypes.Date = Field(
        None, alias="date", title="Type `Date`", description="Expected data of Payment"
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier of the payment instrument",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Partial or Complete",
    )


class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing notes.
    Note text.
    """

    resource_type = Field("ClaimResponseProcessNote", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Language if different from the resource",
    )

    number: fhirtypes.PositiveInt = Field(
        None,
        alias="number",
        title="Type `PositiveInt`",
        description="Sequence Number for this note",
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    text: fhirtypes.String = Field(
        None, alias="text", title="Type `String`", description="Note explanatory text"
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="display | print | printoper",
    )
