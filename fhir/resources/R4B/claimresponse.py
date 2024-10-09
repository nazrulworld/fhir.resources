from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ClaimResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Response to a claim predetermination or preauthorization.
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    __resource_type__ = "ClaimResponse"

    addItem: typing.List[fhirtypes.ClaimResponseAddItemType] | None = Field(  # type: ignore
        None,
        alias="addItem",
        title="Insurer added line items",
        description=(
            "The first-tier service adjudications for payor added product or "
            "service lines."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Header-level adjudication",
        description=(
            "The adjudication results which are presented at the header level "
            "rather than at the line-item or add-item levels."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    communicationRequest: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="communicationRequest",
        title="Request for additional information",
        description="Request for additional supporting or authorizing information.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CommunicationRequest"],
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Response creation date",
        description="The date this resource was created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="disposition",
        title="Disposition Message",
        description="A human readable description of the status of the adjudication.",
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
        description="Errors encountered during the processing of the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    form: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="form",
        title="Printed reference or actual form",
        description=(
            "The actual form, by reference or inclusion, for printing the content "
            "or an EOB."
        ),
        json_schema_extra={
            "element_property": True,
        },
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

    fundsReserve: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="fundsReserve",
        title="Funds reserved status",
        description=(
            "A code, used only on a response to a preauthorization, to indicate "
            "whether the benefits payable have been reserved and for whom."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for a claim response",
        description="A unique identifier assigned to this claim response.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurance: typing.List[fhirtypes.ClaimResponseInsuranceType] | None = Field(  # type: ignore
        None,
        alias="insurance",
        title="Patient insurance information",
        description=(
            "Financial instruments for reimbursement for the health care products "
            "and services specified on the claim."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    insurer: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="insurer",
        title="Party responsible for reimbursement",
        description=(
            "The party responsible for authorization, adjudication and "
            "reimbursement."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    item: typing.List[fhirtypes.ClaimResponseItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Adjudication for claim line items",
        description=(
            "A claim line. Either a simple (a product or service) or a 'group' of "
            "details which can also be a simple items or groups of sub-details."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    outcome: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="outcome",
        title="queued | complete | error | partial",
        description=(
            "The outcome of the claim, predetermination, or preauthorization "
            "processing."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["queued", "complete", "error", "partial"],
        },
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="The recipient of the products and services",
        description=(
            "The party to whom the professional services and/or products have been "
            "supplied or are being considered and for whom actual for facast "
            "reimbursement is sought."
        ),
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
        description="Type of Party to be reimbursed: subscriber, provider, other.",
        json_schema_extra={
            "element_property": True,
        },
    )

    payment: fhirtypes.ClaimResponsePaymentType | None = Field(  # type: ignore
        None,
        alias="payment",
        title="Payment Details",
        description="Payment details for the adjudication of the claim.",
        json_schema_extra={
            "element_property": True,
        },
    )

    preAuthPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="preAuthPeriod",
        title="Preauthorization reference effective period",
        description="The time frame during which this authorization is effective.",
        json_schema_extra={
            "element_property": True,
        },
    )

    preAuthRef: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="preAuthRef",
        title="Preauthorization reference",
        description=(
            "Reference from the Insurer which is used in later communications which"
            " refers to this adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preAuthRef__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_preAuthRef", title="Extension field for ``preAuthRef``."
    )

    processNote: typing.List[fhirtypes.ClaimResponseProcessNoteType] | None = Field(  # type: ignore
        None,
        alias="processNote",
        title="Note concerning adjudication",
        description=(
            "A note that describes or explains adjudication results in a human "
            "readable form."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="request",
        title="Id of resource triggering adjudication",
        description="Original request resource reference.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Claim"],
        },
    )

    requestor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requestor",
        title="Party responsible for the claim",
        description=(
            "The provider which is responsible for the claim, predetermination or "
            "preauthorization."
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

    subType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subType",
        title="More granular claim type",
        description=(
            "A finer grained suite of claim type codes which may convey additional "
            "information such as Inpatient vs Outpatient and/or a specialty "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    total: typing.List[fhirtypes.ClaimResponseTotalType] | None = Field(  # type: ignore
        None,
        alias="total",
        title="Adjudication totals",
        description="Categorized monetary totals for the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="More granular claim type",
        description=(
            "A finer grained suite of claim type codes which may convey additional "
            "information such as Inpatient vs Outpatient and/or a specialty "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    use: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="use",
        title="claim | preauthorization | predetermination",
        description=(
            "A code to indicate whether the nature of the request is: to request "
            "adjudication of products and services previously rendered; or "
            "requesting authorization and adjudication for provision in the future;"
            " or requesting the non-binding adjudication of the listed products and"
            " services which could be provided in the future."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["claim", "preauthorization", "predetermination"],
        },
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_use", title="Extension field for ``use``."
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
            "type",
            "subType",
            "use",
            "patient",
            "created",
            "insurer",
            "requestor",
            "request",
            "outcome",
            "disposition",
            "preAuthRef",
            "preAuthPeriod",
            "payeeType",
            "item",
            "addItem",
            "adjudication",
            "total",
            "payment",
            "fundsReserve",
            "formCode",
            "form",
            "processNote",
            "communicationRequest",
            "insurance",
            "error",
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
            ("outcome", "outcome__ext"),
            ("status", "status__ext"),
            ("use", "use__ext"),
        ]
        return required_fields


class ClaimResponseAddItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The first-tier service adjudications for payor added product or service
    lines.
    """

    __resource_type__ = "ClaimResponseAddItem"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(  # type: ignore
        ...,
        alias="adjudication",
        title="Added items adjudication",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    bodySite: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Anatomical location",
        description="Physical service site on the patient (limb, tooth, etc.).",
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ClaimResponseAddItemDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Insurer added line details",
        description="The second-tier service adjudications for payor added services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detailSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="detailSequence",
        title="Detail sequence number",
        description=(
            "The sequence number of the details within the claim item which this "
            "line is intended to replace."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    detailSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_detailSequence", title="Extension field for ``detailSequence``."
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    itemSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="itemSequence",
        title="Item sequence number",
        description="Claim items which this service line is intended to replace.",
        json_schema_extra={
            "element_property": True,
        },
    )
    itemSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_itemSequence", title="Extension field for ``itemSequence``."
    )

    locationAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="locationAddress",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
        },
    )

    locationCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="locationCodeableConcept",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
        },
    )

    locationReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="locationReference",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The quantity times the unit price for an additional service or product"
            " or charge."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    productOrService: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related claim details, otherwise this contains the product, service, "
            "drug or other billing code for the item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program the product or service is provided under",
        description="Identifies the program under which this may be recovered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    provider: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="provider",
        title="Authorized providers",
        description=(
            "The providers who are authorized for the services rendered to the "
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

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    servicedDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="servicedDate",
        title="Date or dates of service or product delivery",
        description=(
            "The date or dates when the service or product was supplied, performed "
            "or completed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e serviced[x]
            "one_of_many": "serviced",
            "one_of_many_required": False,
        },
    )
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_servicedDate", title="Extension field for ``servicedDate``."
    )

    servicedPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="servicedPeriod",
        title="Date or dates of service or product delivery",
        description=(
            "The date or dates when the service or product was supplied, performed "
            "or completed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e serviced[x]
            "one_of_many": "serviced",
            "one_of_many_required": False,
        },
    )

    subSite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subSite",
        title="Anatomical sub-location",
        description=(
            "A region or surface of the bodySite, e.g. limb region or tooth "
            "surface(s)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subdetailSequence: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="subdetailSequence",
        title="Subdetail sequence number",
        description=(
            "The sequence number of the sub-details within the details within the "
            "claim item which this line is intended to replace."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subdetailSequence__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_subdetailSequence",
        title="Extension field for ``subdetailSequence``.",
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
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
            "itemSequence",
            "detailSequence",
            "subdetailSequence",
            "provider",
            "productOrService",
            "modifier",
            "programCode",
            "servicedDate",
            "servicedPeriod",
            "locationCodeableConcept",
            "locationAddress",
            "locationReference",
            "quantity",
            "unitPrice",
            "factor",
            "net",
            "bodySite",
            "subSite",
            "noteNumber",
            "adjudication",
            "detail",
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
            "location": [
                "locationAddress",
                "locationCodeableConcept",
                "locationReference",
            ],
            "serviced": ["servicedDate", "servicedPeriod"],
        }
        return one_of_many_fields


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line details.
    The second-tier service adjudications for payor added services.
    """

    __resource_type__ = "ClaimResponseAddItemDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(  # type: ignore
        ...,
        alias="adjudication",
        title="Added items detail adjudication",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The quantity times the unit price for an additional service or product"
            " or charge."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    productOrService: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related claim details, otherwise this contains the product, service, "
            "drug or other billing code for the item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subDetail: typing.List[fhirtypes.ClaimResponseAddItemDetailSubDetailType] | None = Field(  # type: ignore
        None,
        alias="subDetail",
        title="Insurer added line items",
        description="The third-tier service adjudications for payor added services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
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
            "productOrService",
            "modifier",
            "quantity",
            "unitPrice",
            "factor",
            "net",
            "noteNumber",
            "adjudication",
            "subDetail",
        ]


class ClaimResponseAddItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The third-tier service adjudications for payor added services.
    """

    __resource_type__ = "ClaimResponseAddItemDetailSubDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(  # type: ignore
        ...,
        alias="adjudication",
        title="Added items detail adjudication",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    factor: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The quantity times the unit price for an additional service or product"
            " or charge."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    productOrService: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related claim details, otherwise this contains the product, service, "
            "drug or other billing code for the item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseAddItemDetailSubDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "productOrService",
            "modifier",
            "quantity",
            "unitPrice",
            "factor",
            "net",
            "noteNumber",
            "adjudication",
        ]


class ClaimResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Errors encountered during the processing of the adjudication.
    """

    __resource_type__ = "ClaimResponseError"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Error code detailing processing issues",
        description=(
            "An error code, from a specified code system, which details why the "
            "claim could not be adjudicated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detailSequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="detailSequence",
        title="Detail sequence number",
        description=(
            "The sequence number of the detail within the line item submitted which"
            " contains the error. This value is omitted when the error occurs "
            "outside of the item structure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    detailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_detailSequence", title="Extension field for ``detailSequence``."
    )

    itemSequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="itemSequence",
        title="Item sequence number",
        description=(
            "The sequence number of the line item submitted which contains the "
            "error. This value is omitted when the error occurs outside of the item"
            " structure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    itemSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_itemSequence", title="Extension field for ``itemSequence``."
    )

    subDetailSequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="subDetailSequence",
        title="Subdetail sequence number",
        description=(
            "The sequence number of the sub-detail within the detail within the "
            "line item submitted which contains the error. This value is omitted "
            "when the error occurs outside of the item structure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subDetailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_subDetailSequence",
        title="Extension field for ``subDetailSequence``.",
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
            "itemSequence",
            "detailSequence",
            "subDetailSequence",
            "code",
        ]


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """

    __resource_type__ = "ClaimResponseInsurance"

    businessArrangement: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="businessArrangement",
        title="Additional provider contract number",
        description=(
            "A business agreement number established between the provider and the "
            "insurer for special business processing purposes."
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
        description=(
            "The result of the adjudication of the line items for the Coverage "
            "specified in this insurance."
        ),
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
        description=(
            "Reference to the insurance card level information contained in the "
            "Coverage resource. The coverage issuing insurer will use these details"
            " to locate the patient's actual coverage within the insurer's "
            "information system."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
    )

    focal: bool | None = Field(  # type: ignore
        None,
        alias="focal",
        title="Coverage to be used for adjudication",
        description=(
            "A flag to indicate that this Coverage is to be used for adjudication "
            "of this claim when set to true."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_focal", title="Extension field for ``focal``."
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Insurance instance identifier",
        description=(
            "A number to uniquely identify insurance entries and provide a sequence"
            " of coverages to convey coordination of benefit order."
        ),
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

    Adjudication for claim line items.
    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """

    __resource_type__ = "ClaimResponseItem"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(  # type: ignore
        ...,
        alias="adjudication",
        title="Adjudication details",
        description=(
            "If this item is a group then the values here are a summary of the "
            "adjudication of the detail items. If this item is a simple product or "
            "service then this is the result of the adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ClaimResponseItemDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Adjudication for claim details",
        description=(
            "A claim detail. Either a simple (a product or service) or a 'group' of"
            " sub-details which are simple items."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    itemSequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="itemSequence",
        title="Claim item instance identifier",
        description="A number to uniquely reference the claim item entries.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    itemSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_itemSequence", title="Extension field for ``itemSequence``."
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
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
            "itemSequence",
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
        required_fields = [("itemSequence", "itemSequence__ext")]
        return required_fields


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication details.
    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """

    __resource_type__ = "ClaimResponseItemAdjudication"

    amount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Monetary amount",
        description="Monetary amount associated with the category.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Type of adjudication information",
        description=(
            "A code to indicate the information type of this adjudication record. "
            "Information types may include the value submitted, maximum values or "
            "percentages allowed or payable under the plan, amounts that: the "
            "patient is responsible for in aggregate or pertaining to this item; "
            "amounts paid by other coverages; and, the benefit payable for this "
            "item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Explanation of adjudication outcome",
        description=(
            "A code supporting the understanding of the adjudication result and "
            "explaining variance from expected amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Non-monetary value",
        description=(
            "A non-monetary value associated with the category. Mutually exclusive "
            "to the amount element above."
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

    Adjudication for claim details.
    A claim detail. Either a simple (a product or service) or a 'group' of sub-
    details which are simple items.
    """

    __resource_type__ = "ClaimResponseItemDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(  # type: ignore
        ...,
        alias="adjudication",
        title="Detail level adjudication details",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detailSequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="detailSequence",
        title="Claim detail instance identifier",
        description="A number to uniquely reference the claim detail entry.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    detailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_detailSequence", title="Extension field for ``detailSequence``."
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    subDetail: typing.List[fhirtypes.ClaimResponseItemDetailSubDetailType] | None = Field(  # type: ignore
        None,
        alias="subDetail",
        title="Adjudication for claim sub-details",
        description="A sub-detail adjudication of a simple product or service.",
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
            "detailSequence",
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
        required_fields = [("detailSequence", "detailSequence__ext")]
        return required_fields


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication for claim sub-details.
    A sub-detail adjudication of a simple product or service.
    """

    __resource_type__ = "ClaimResponseItemDetailSubDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Subdetail level adjudication details",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_noteNumber", title="Extension field for ``noteNumber``."
    )

    subDetailSequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="subDetailSequence",
        title="Claim sub-detail instance identifier",
        description="A number to uniquely reference the claim sub-detail entry.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    subDetailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_subDetailSequence",
        title="Extension field for ``subDetailSequence``.",
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
            "subDetailSequence",
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
        required_fields = [("subDetailSequence", "subDetailSequence__ext")]
        return required_fields


class ClaimResponsePayment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Payment Details.
    Payment details for the adjudication of the claim.
    """

    __resource_type__ = "ClaimResponsePayment"

    adjustment: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="adjustment",
        title="Payment adjustment for non-claim issues",
        description=(
            "Total amount of all adjustments to this payment included in this "
            "transaction which are not related to this claim's adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    adjustmentReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="adjustmentReason",
        title="Explanation for the adjustment",
        description="Reason for the payment adjustment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    amount: fhirtypes.MoneyType = Field(  # type: ignore
        ...,
        alias="amount",
        title="Payable amount after adjustment",
        description="Benefits payable less any payment adjustment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Expected date of payment",
        description=(
            "Estimated date the payment will be issued or the actual issue date of "
            "payment."
        ),
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
        title="Business identifier for the payment",
        description="Issuer's unique identifier for the payment instrument.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Partial or complete payment",
        description=(
            "Whether this represents partial or complete payment of the benefits "
            "payable."
        ),
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

    Note concerning adjudication.
    A note that describes or explains adjudication results in a human readable
    form.
    """

    __resource_type__ = "ClaimResponseProcessNote"

    language: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="language",
        title="Language of the text",
        description="A code to define the language used in the text of the note.",
        json_schema_extra={
            "element_property": True,
        },
    )

    number: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="number",
        title="Note instance identifier",
        description="A number to uniquely identify a note entry.",
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
        description="The explanation or description associated with the processing.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("text", "text__ext")]
        return required_fields


class ClaimResponseTotal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication totals.
    Categorized monetary totals for the adjudication.
    """

    __resource_type__ = "ClaimResponseTotal"

    amount: fhirtypes.MoneyType = Field(  # type: ignore
        ...,
        alias="amount",
        title="Financial total for the category",
        description="Monetary total amount associated with the category.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Type of adjudication information",
        description=(
            "A code to indicate the information type of this adjudication record. "
            "Information types may include: the value submitted, maximum values or "
            "percentages allowed or payable under the plan, amounts that the "
            "patient is responsible for in aggregate or pertaining to this item, "
            "amounts paid by other coverages, and the benefit payable for this "
            "item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseTotal`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "category", "amount"]
