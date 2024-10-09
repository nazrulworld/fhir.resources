from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ClaimResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Remittance resource.
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    __resource_type__ = "ClaimResponse"

    addItem: typing.List[fhirtypes.ClaimResponseAddItemType] | None = Field(  # type: ignore
        None,
        alias="addItem",
        title="Insurer added line items",
        description="The first tier service adjudications for payor added services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    communicationRequest: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="communicationRequest",
        title="Request for additional information",
        description=(
            "Request for additional supporting or authorizing information, such as:"
            " documents, images or resources."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CommunicationRequest"],
        },
    )

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

    error: typing.List[fhirtypes.ClaimResponseErrorType] | None = Field(  # type: ignore
        None,
        alias="error",
        title="Processing errors",
        description="Mutually exclusive with Services Provided (Item).",
        json_schema_extra={
            "element_property": True,
        },
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
        title="Response  number",
        description="The Response business identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurance: typing.List[fhirtypes.ClaimResponseInsuranceType] | None = Field(  # type: ignore
        None,
        alias="insurance",
        title="Insurance or medical plan",
        description="Financial instrument by which payment information for health care.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="insurer",
        title="Insurance issuing organization",
        description="The Insurer who produced this adjudicated response.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    item: typing.List[fhirtypes.ClaimResponseItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Line items",
        description="The first tier service adjudications for submitted services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    outcome: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Processing outcome errror, partial or complete processing.",
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="patient",
        title="The subject of the Products and Services",
        description="Patient Resource.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    payeeType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="payeeType",
        title="Party to be paid any benefits payable",
        description="Party to be reimbursed: Subscriber, provider, other.",
        json_schema_extra={
            "element_property": True,
        },
    )

    payment: fhirtypes.ClaimResponsePaymentType | None = Field(  # type: ignore
        None,
        alias="payment",
        title="Payment details, if paid",
        description="Payment details for the claim if the claim has been paid.",
        json_schema_extra={
            "element_property": True,
        },
    )

    processNote: typing.List[fhirtypes.ClaimResponseProcessNoteType] | None = Field(  # type: ignore
        None,
        alias="processNote",
        title="Processing notes",
        description="Note text.",
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Id of resource triggering adjudication",
        description="Original request resource referrence.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Claim"],
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

    reserved: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="reserved",
        title="Funds reserved status",
        description="Status of funds reservation (For provider, for Patient, None).",
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
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    totalBenefit: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="totalBenefit",
        title="Total benefit payable for the Claim",
        description=(
            "Total amount of benefit payable (Equal to sum of the Benefit amounts "
            "from all detail lines and additions less the Unallocated Deductible)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    totalCost: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="totalCost",
        title="Total Cost of service from the Claim",
        description="The total cost of the services reported.",
        json_schema_extra={
            "element_property": True,
        },
    )

    unallocDeductable: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unallocDeductable",
        title="Unallocated deductible",
        description=(
            "The amount of deductible applied which was not allocated to any "
            "particular service line."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponse`` according specification,
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
            "patient",
            "created",
            "insurer",
            "requestProvider",
            "requestOrganization",
            "request",
            "outcome",
            "disposition",
            "payeeType",
            "item",
            "addItem",
            "error",
            "totalCost",
            "unallocDeductable",
            "totalBenefit",
            "payment",
            "reserved",
            "form",
            "processNote",
            "communicationRequest",
            "insurance",
        ]


class ClaimResponseAddItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The first tier service adjudications for payor added services.
    """

    __resource_type__ = "ClaimResponseAddItem"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Added items adjudication",
        description="The adjudications results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ClaimResponseAddItemDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Added items details",
        description="The second tier service adjudications for payor added services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    fee: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="fee",
        title="Professional fee or Product charge",
        description="The fee charged for the professional service or product..",
        json_schema_extra={
            "element_property": True,
        },
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    revenue: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequenceLinkId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="sequenceLinkId",
        title="Service instances",
        description=(
            "List of input service items which this service line is intended to "
            "replace."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    sequenceLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    service: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="service",
        title="Group, Service or Product",
        description="A code to indicate the Professional Service or Product supplied.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseAddItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "revenue",
            "category",
            "service",
            "modifier",
            "fee",
            "noteNumber",
            "adjudication",
            "detail",
        ]


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Added items details.
    The second tier service adjudications for payor added services.
    """

    __resource_type__ = "ClaimResponseAddItemDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Added items detail adjudication",
        description="The adjudications results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    fee: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="fee",
        title="Professional fee or Product charge",
        description="The fee charged for the professional service or product..",
        json_schema_extra={
            "element_property": True,
        },
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    revenue: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    service: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="service",
        title="Service or Product",
        description="A code to indicate the Professional Service or Product supplied.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseAddItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "revenue",
            "category",
            "service",
            "modifier",
            "fee",
            "noteNumber",
            "adjudication",
        ]


class ClaimResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Mutually exclusive with Services Provided (Item).
    """

    __resource_type__ = "ClaimResponseError"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Error code detailing processing issues",
        description=(
            "An error code,from a specified code system, which details why the "
            "claim could not be adjudicated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detailSequenceLinkId: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="detailSequenceLinkId",
        title="Detail sequence number",
        description=(
            "The sequence number of the addition within the line item submitted "
            "which contains the error. This value is omitted when the error is not "
            "related to an Addition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    detailSequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_detailSequenceLinkId",
        title="Extension field for ``detailSequenceLinkId``.",
    )

    sequenceLinkId: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequenceLinkId",
        title="Item sequence number",
        description=(
            "The sequence number of the line item submitted which contains the "
            "error. This value is omitted when the error is elsewhere."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    subdetailSequenceLinkId: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="subdetailSequenceLinkId",
        title="Subdetail sequence number",
        description=(
            "The sequence number of the addition within the line item submitted "
            "which contains the error. This value is omitted when the error is not "
            "related to an Addition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subdetailSequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_subdetailSequenceLinkId",
        title="Extension field for ``subdetailSequenceLinkId``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseError`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "detailSequenceLinkId",
            "subdetailSequenceLinkId",
            "code",
        ]


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan.
    Financial instrument by which payment information for health care.
    """

    __resource_type__ = "ClaimResponseInsurance"

    businessArrangement: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="businessArrangement",
        title="Business agreement",
        description=(
            "The contract number of a business agreement which describes the terms "
            "and conditions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_businessArrangement",
        title="Extension field for ``businessArrangement``.",
    )

    claimResponse: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="claimResponse",
        title="Adjudication results",
        description="The Coverages adjudication details.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ClaimResponse"],
        },
    )

    coverage: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="coverage",
        title="Insurance information",
        description="Reference to the program or plan identification, underwriter or payor.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
    )

    focal: bool | None = Field(  # type: ignore
        None,
        alias="focal",
        title="Is the focal Coverage",
        description=(
            "The instance number of the Coverage which is the focus for "
            "adjudication. The Coverage against which the claim is to be "
            "adjudicated."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_focal", title="Extension field for ``focal``."
    )

    preAuthRef: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="preAuthRef",
        title="Pre-Authorization/Determination Reference",
        description="A list of references from the Insurer to which these services pertain.",
        json_schema_extra={
            "element_property": True,
        },
    )
    preAuthRef__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_preAuthRef", title="Extension field for ``preAuthRef``."
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Service instance identifier",
        description="A service line item.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseInsurance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "focal",
            "coverage",
            "businessArrangement",
            "preAuthRef",
            "claimResponse",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("focal", "focal__ext"), ("sequence", "sequence__ext")]
        return required_fields


class ClaimResponseItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Line items.
    The first tier service adjudications for submitted services.
    """

    __resource_type__ = "ClaimResponseItem"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Adjudication details",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ClaimResponseItemDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Detail line items",
        description="The second tier service adjudications for submitted services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    sequenceLinkId: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequenceLinkId",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "noteNumber",
            "adjudication",
            "detail",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequenceLinkId", "sequenceLinkId__ext")]
        return required_fields


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication details.
    The adjudication results.
    """

    __resource_type__ = "ClaimResponseItemAdjudication"

    amount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Monetary amount",
        description="Monetary amount associated with the code.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Adjudication category such as co-pay, eligible, benefit, etc.",
        description="Code indicating: Co-Pay, deductible, eligible, benefit, tax, etc.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Explanation of Adjudication outcome",
        description="Adjudication reason such as limit reached.",
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Non-monetary value",
        description=(
            "A non-monetary value for example a percentage. Mutually exclusive to "
            "the amount element above."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItemAdjudication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "reason",
            "amount",
            "value",
        ]


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Detail line items.
    The second tier service adjudications for submitted services.
    """

    __resource_type__ = "ClaimResponseItemDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Detail level adjudication details",
        description="The adjudications results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    sequenceLinkId: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequenceLinkId",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    subDetail: typing.List[fhirtypes.ClaimResponseItemDetailSubDetailType] | None = Field(  # type: ignore
        None,
        alias="subDetail",
        title="Subdetail line items",
        description="The third tier service adjudications for submitted services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "noteNumber",
            "adjudication",
            "subDetail",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequenceLinkId", "sequenceLinkId__ext")]
        return required_fields


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Subdetail line items.
    The third tier service adjudications for submitted services.
    """

    __resource_type__ = "ClaimResponseItemDetailSubDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Subdetail level adjudication details",
        description="The adjudications results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    sequenceLinkId: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequenceLinkId",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItemDetailSubDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLinkId",
            "noteNumber",
            "adjudication",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequenceLinkId", "sequenceLinkId__ext")]
        return required_fields


class ClaimResponsePayment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Payment details, if paid.
    Payment details for the claim if the claim has been paid.
    """

    __resource_type__ = "ClaimResponsePayment"

    adjustment: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="adjustment",
        title="Payment adjustment for non-Claim issues",
        description=(
            "Adjustment to the payment of this transaction which is not related to "
            "adjudication of this transaction."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    adjustmentReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="adjustmentReason",
        title="Explanation for the non-claim adjustment",
        description="Reason for the payment adjustment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    amount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Payable amount after adjustment",
        description="Payable less any payment adjustment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Expected data of Payment",
        description="Estimated payment data.",
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
        title="Identifier of the payment instrument",
        description="Payment identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Partial or Complete",
        description="Whether this represents partial or complete payment of the claim.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponsePayment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "adjustment",
            "adjustmentReason",
            "date",
            "amount",
            "identifier",
        ]


class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing notes.
    Note text.
    """

    __resource_type__ = "ClaimResponseProcessNote"

    language: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="language",
        title="Language if different from the resource",
        description=(
            "The ISO-639-1 alpha 2 code in lower case for the language, optionally "
            "followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in"
            ' upper case; e.g. "en" for English, or "en-US" for American English '
            'versus "en-EN" for England English.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    number: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="number",
        title="Sequence Number for this note",
        description=(
            "An integer associated with each note which may be referred to from "
            "each service line item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_number", title="Extension field for ``number``."
    )

    text: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="text",
        title="Note explanatory text",
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
        ``ClaimResponseProcessNote`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "number",
            "type",
            "text",
            "language",
        ]
