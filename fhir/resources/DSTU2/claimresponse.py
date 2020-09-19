# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class ClaimResponse(DomainResource):
    """Remittance resource.

    This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    addItem: ListType[fhirtypes.ClaimResponseAddItemType] = Field(
        None,
        alias="addItem",
        title="List of `ClaimResponseAddItem` items (represented as `dict` in JSON)",
        description="Insurer added line items",
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
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

    form: fhirtypes.CodingType = Field(
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

    item: ListType[fhirtypes.ClaimResponseItemType] = Field(
        None,
        alias="item",
        title="List of `ClaimResponseItem` items (represented as `dict` in JSON)",
        description="Line items",
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="Type `Code` (represented as `dict` in JSON)",
        description="complete | error | partial",
    )

    payeeType: fhirtypes.CodingType = Field(
        None,
        alias="payeeType",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Party to be paid any benefits payable",
    )

    paymentAdjustment: fhirtypes.MoneyType = Field(
        None,
        alias="paymentAdjustment",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Payment adjustment for non-Claim issues.",
    )

    paymentAdjustmentReason: fhirtypes.CodingType = Field(
        None,
        alias="paymentAdjustmentReason",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Reason for Payment adjustment.",
    )

    paymentAmount: fhirtypes.MoneyType = Field(
        None,
        alias="paymentAmount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Payment amount.",
    )

    paymentDate: fhirtypes.Date = Field(
        None,
        alias="paymentDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Expected data of Payment.",
    )

    paymentRef: fhirtypes.ReferenceType = Field(
        None,
        alias="paymentDate",
        title="Type `Identifier` (represented as `dict` in JSON).",
        description="Payment identifier.",
    )

    note: ListType[fhirtypes.ClaimResponseNoteType] = Field(
        None,
        alias="note",
        title=("List of `ClaimResponseNote` items (represented as `dict` in " "JSON)"),
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

    ruleset: fhirtypes.CodingType = Field(
        None,
        alias="ruleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Resource version.",
    )
    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Insurer.",
    )

    originalRuleset: fhirtypes.CodingType = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original version.",
    )

    coverage: ListType[fhirtypes.ClaimResponseCoverageType] = Field(
        None,
        alias="originalRuleset",
        title="List of `ClaimResponseCoverage` items (represented as `dict` in JSON).",
        description="Insurance or medical plan.",
    )


class ClaimResponseAddItem(BackboneElement):
    """Insurer added line items.

    The first tier service adjudications for payor added services.
    """

    resource_type = Field("ClaimResponseAddItem", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseAddItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title=(
            "List of `ClaimResponseAddItemAdjudication` "
            "items (represented as `dict` in JSON)."
        ),
        description="Added items adjudication.",
    )

    detail: ListType[fhirtypes.ClaimResponseAddItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ClaimResponseAddItemDetail` items (represented as `dict` in JSON).",
        description="Added items details.",
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Professional fee or Product charge.",
    )

    noteNumberLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumberLinkId",
        title="List of note numbers which apply.",
        description="List of `int` items.",
    )
    sequenceLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="sequenceLinkId",
        title="List of `int` items.",
        description="Service instances.",
    )
    service: fhirtypes.CodingType = Field(
        ...,
        alias="service",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Group, Service or Product.",
    )


class ClaimResponseAddItemAdjudication(BackboneElement):
    """Added items adjudication.

    The adjudications results.
    """

    resource_type = Field("ClaimResponseAddItemAdjudication", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Monetary amount.",
    )

    code: fhirtypes.CodingType = Field(
        None,
        alias="code",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Adjudication category such as co-pay, eligible, benefit, etc..",
    )

    value: fhirtypes.CodingType = Field(
        None, alias="value", title="Type `float`.", description="Non-monetary value."
    )


class ClaimResponseAddItemDetail(BackboneElement):
    """Added items details.

    The second tier service adjudications for payor added services.
    """

    resource_type = Field("ClaimResponseAddItemDetail", const=True)

    adjudication: ListType[
        fhirtypes.ClaimResponseAddItemDetailAdjudicationType
    ] = Field(
        None,
        alias="adjudication",
        title=(
            "List of `ClaimResponseAddItemDetailAdjudication` "
            "items (represented as `dict` in JSON)."
        ),
        description="Added items detail adjudication.",
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Professional fee or Product charge.",
    )
    service: fhirtypes.CodingType = Field(
        None,
        alias="service",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Service or Product.",
    )


class ClaimResponseAddItemDetailAdjudication(BackboneElement):
    """Added items detail adjudication.

    The adjudications results.
    """

    resource_type = Field("ClaimResponseAddItemDetailAdjudication", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Monetary amount.",
    )

    code: fhirtypes.CodingType = Field(
        None,
        alias="code",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Adjudication category such as co-pay, eligible, benefit, etc..",
    )
    value: fhirtypes.Decimal = Field(
        None, alias="value", title="Type `float`.", description="Non-monetary value."
    )


class ClaimResponseCoverage(BackboneElement):
    """Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """

    resource_type = Field("ClaimResponseCoverage", const=True)

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Type `str`.",
        description="Business agreement.",
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title="Type `Reference` referencing `ClaimResponse` (represented as `dict` in JSON).",
        description="Adjudication results.",
    )

    coverage: fhirtypes.ReferenceType = Field(
        None,
        alias="coverage",
        title="Type `Reference` referencing `ClaimResponse` (represented as `dict` in JSON).",
        description="Insurance information.",
    )

    focal: fhirtypes.Boolean = Field(
        None, alias="focal", title="Type `bool`.", description="Is the focal Coverage."
    )

    originalRuleset: fhirtypes.CodingType = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original version.",
    )
    preAuthRef: ListType[fhirtypes.String] = Field(
        None,
        alias="preAuthRef",
        title="List of `str` items.",
        description="Pre-Authorization/Determination Reference.",
    )

    relationship: fhirtypes.CodingType = Field(
        None,
        alias="relationship",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Patient relationship to subscriber.",
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Type `int`.",
        description="Service instance identifier.",
    )


class ClaimResponseError(BackboneElement):
    """Processing errors.

    Mutually exclusive with Services Provided (Item).
    """

    resource_type = Field("ClaimResponseError", const=True)

    code: fhirtypes.CodingType = Field(
        None,
        alias="code",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Error code detailing processing issues.",
    )
    detailSequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="detailSequenceLinkId",
        title="Type `int`.",
        description="Detail sequence number.",
    )
    sequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="sequenceLinkId",
        title="Type `int`.",
        description="Item sequence number.",
    )

    subdetailSequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="subdetailSequenceLinkId",
        title="Type `int`.",
        description="Subdetail sequence number.",
    )


class ClaimResponseItem(BackboneElement):
    """Line items.

    The first tier service adjudications for submitted services.
    """

    resource_type = Field("ClaimResponseItem", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON).",
        description="Adjudication details.",
    )
    detail: ListType[fhirtypes.ClaimResponseItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ClaimResponseItemDetail` items (represented as `dict` in JSON).",
        description="Detail line items.",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `int` items.",
        description="List of note numbers which apply.",
    )
    sequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="sequenceLinkId",
        title="Type `int`.",
        description="Service instance.",
    )


class ClaimResponseItemAdjudication(BackboneElement):
    """Adjudication details.

    The adjudications results.
    """

    resource_type = Field("ClaimResponseItemAdjudication", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Monetary amount.",
    )

    code: fhirtypes.CodingType = Field(
        None,
        alias="code",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Adjudication category such as co-pay, eligible, benefit, etc..",
    )
    value: fhirtypes.Decimal = Field(
        None, alias="value", title="Type `float`.", description="Non-monetary value."
    )


class ClaimResponseItemDetail(BackboneElement):
    """Detail line items.

    The second tier service adjudications for submitted services.
    """

    resource_type = Field("ClaimResponseItemDetail", const=True)

    adjudication: ListType[fhirtypes.ClaimResponseItemDetailAdjudicationType] = Field(
        None,
        alias="adjudication",
        title=(
            "List of `ClaimResponseItemDetailAdjudication` "
            "items (represented as `dict` in JSON)."
        ),
        description="Detail adjudication.",
    )

    sequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="sequenceLinkId",
        title="Type `int`.",
        description="Service instance.",
    )

    subDetail: ListType[fhirtypes.ClaimResponseItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title=(
            "List of `ClaimResponseItemDetailSubDetail` "
            "items (represented as `dict` in JSON)."
        ),
        description="Subdetail line items.",
    )


class ClaimResponseItemDetailAdjudication(BackboneElement):
    """Detail adjudication.

    The adjudications results.
    """

    resource_type = Field("ClaimResponseItemDetailAdjudication", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Monetary amount.",
    )
    code: fhirtypes.CodingType = Field(
        None,
        alias="code",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Adjudication category such as co-pay, eligible, benefit, etc..",
    )

    value: fhirtypes.Decimal = Field(
        None, alias="value", title="Type `float`.", description="Non-monetary value."
    )


class ClaimResponseItemDetailSubDetail(BackboneElement):
    """Subdetail line items.

    The third tier service adjudications for submitted services.
    """

    resource_type = Field("ClaimResponseItemDetailSubDetail", const=True)

    adjudication: ListType[
        fhirtypes.ClaimResponseItemDetailSubDetailAdjudicationType
    ] = Field(
        None,
        alias="adjudication",
        title=(
            "List of `ClaimResponseItemDetailSubDetailAdjudication` "
            "items (represented as `dict` in JSON)."
        ),
        description="Subdetail adjudication.",
    )

    sequenceLinkId: fhirtypes.PositiveInt = Field(
        None,
        alias="sequenceLinkId",
        title="Type `int`.",
        description="Service instance.",
    )


class ClaimResponseItemDetailSubDetailAdjudication(BackboneElement):
    """Subdetail adjudication.

    The adjudications results.
    """

    resource_type = Field("ClaimResponseItemDetailSubDetailAdjudication", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Monetary amount.",
    )
    code: fhirtypes.CodingType = Field(
        None,
        alias="code",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Adjudication category such as co-pay, eligible, benefit, etc..",
    )

    value: fhirtypes.Decimal = Field(
        None, alias="value", title="Type `float`.", description="Non-monetary value."
    )


class ClaimResponseNote(BackboneElement):
    """Processing notes.

    Note text.
    """

    resource_type = Field("ClaimResponseNote", const=True)

    number: fhirtypes.PositiveInt = Field(
        None,
        alias="number",
        title="Type `int`.",
        description="Note Number for this note.",
    )
    text: fhirtypes.String = Field(
        None, alias="text", title="Type `str`.", description="Note explanatory text."
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="display | print | printoper.",
    )
