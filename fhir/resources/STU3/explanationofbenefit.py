from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ExplanationOfBenefit(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Explanation of Benefit resource.
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    __resource_type__ = "ExplanationOfBenefit"

    accident: fhirtypes.ExplanationOfBenefitAccidentType | None = Field(  # type: ignore
        None,
        alias="accident",
        title="Details of an accident",
        description="An accident which resulted in the need for healthcare services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    addItem: typing.List[fhirtypes.ExplanationOfBenefitAddItemType] | None = Field(  # type: ignore
        None,
        alias="addItem",
        title="Insurer added line items",
        description="The first tier service adjudications for payor added services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    benefitBalance: typing.List[fhirtypes.ExplanationOfBenefitBenefitBalanceType] | None = Field(  # type: ignore
        None,
        alias="benefitBalance",
        title="Balance by Benefit Category",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    billablePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="billablePeriod",
        title="Period for charge submission",
        description="The billable period for which charges are being submitted.",
        json_schema_extra={
            "element_property": True,
        },
    )

    careTeam: typing.List[fhirtypes.ExplanationOfBenefitCareTeamType] | None = Field(  # type: ignore
        None,
        alias="careTeam",
        title="Care Team members",
        description=(
            "The members of the team who provided the overall service as well as "
            "their role and whether responsible and qualifications."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    claim: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="claim",
        title="Claim reference",
        description=(
            "The business identifier for the instance: invoice number, claim "
            "number, pre-determination or pre-authorization number."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Claim"],
        },
    )

    claimResponse: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="claimResponse",
        title="Claim response reference",
        description=(
            "The business identifier for the instance: invoice number, claim "
            "number, pre-determination or pre-authorization number."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ClaimResponse"],
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Creation date",
        description="The date when the EOB was created.",
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    diagnosis: typing.List[fhirtypes.ExplanationOfBenefitDiagnosisType] | None = Field(  # type: ignore
        None,
        alias="diagnosis",
        title="List of Diagnosis",
        description="Ordered list of patient diagnosis for which care is sought.",
        json_schema_extra={
            "element_property": True,
        },
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

    employmentImpacted: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="employmentImpacted",
        title="Period unable to work",
        description=(
            "The start and optional end dates of when the patient was precluded "
            "from working due to the treatable condition(s)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    enterer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="enterer",
        title="Author",
        description="The person who created the explanation of benefit.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    facility: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="facility",
        title="Servicing Facility",
        description="Facility where the services were provided.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
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

    hospitalization: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="hospitalization",
        title="Period in hospital",
        description=(
            "The start and optional end dates of when the patient was confined to a"
            " treatment center."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier",
        description="The EOB Business Identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    information: typing.List[fhirtypes.ExplanationOfBenefitInformationType] | None = Field(  # type: ignore
        None,
        alias="information",
        title=(
            "Exceptions, special considerations, the condition, situation, prior or"
            " concurrent issues"
        ),
        description=(
            "Additional information codes regarding exceptions, special "
            "considerations, the condition, situation, prior or concurrent issues. "
            "Often there are mutiple jurisdiction specific valuesets which are "
            "required."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    insurance: fhirtypes.ExplanationOfBenefitInsuranceType | None = Field(  # type: ignore
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
        title="Insurer responsible for the EOB",
        description="The insurer which is responsible for the explanation of benefit.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    item: typing.List[fhirtypes.ExplanationOfBenefitItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Goods and Services",
        description="First tier of goods and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="organization",
        title="Responsible organization for the claim",
        description="The provider which is responsible for the claim.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    originalPrescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="originalPrescription",
        title="Original prescription if superceded by fulfiller",
        description=(
            "Original prescription which has been superceded by this prescription "
            "to support the dispensing of pharmacy services, medications or "
            "products. For example, a physician may prescribe a medication which "
            "the pharmacy determines is contraindicated, or for which the patient "
            "has an intolerance, and therefor issues a new precription for an "
            "alternate medication which has the same theraputic intent. The "
            "prescription from the pharmacy becomes the 'prescription' and that "
            "from the physician becomes the 'original prescription'."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest"],
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

    payee: fhirtypes.ExplanationOfBenefitPayeeType | None = Field(  # type: ignore
        None,
        alias="payee",
        title="Party to be paid any benefits payable",
        description="The party to be reimbursed for the services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    payment: fhirtypes.ExplanationOfBenefitPaymentType | None = Field(  # type: ignore
        None,
        alias="payment",
        title="Payment (if paid)",
        description="Payment details for the claim if the claim has been paid.",
        json_schema_extra={
            "element_property": True,
        },
    )

    precedence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="precedence",
        title="Precedence (primary, secondary, etc.)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    precedence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_precedence", title="Extension field for ``precedence``."
    )

    prescription: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="prescription",
        title="Prescription authorizing services or products",
        description="Prescription to support the dispensing of Pharmacy or Vision products.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest", "VisionPrescription"],
        },
    )

    procedure: typing.List[fhirtypes.ExplanationOfBenefitProcedureType] | None = Field(  # type: ignore
        None,
        alias="procedure",
        title="Procedures performed",
        description=(
            "Ordered list of patient procedures performed to support the "
            "adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    processNote: typing.List[fhirtypes.ExplanationOfBenefitProcessNoteType] | None = Field(  # type: ignore
        None,
        alias="processNote",
        title="Processing notes",
        description="Note text.",
        json_schema_extra={
            "element_property": True,
        },
    )

    provider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="provider",
        title="Responsible provider for the claim",
        description="The provider which is responsible for the claim.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    referral: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="referral",
        title="Treatment Referral",
        description=(
            "The referral resource which lists the date, practitioner, reason and "
            "other supporting information."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ReferralRequest"],
        },
    )

    related: typing.List[fhirtypes.ExplanationOfBenefitRelatedType] | None = Field(  # type: ignore
        None,
        alias="related",
        title="Related Claims which may be revelant to processing this claim",
        description=(
            "Other claims which are related to this claim such as prior claim "
            "versions or for related services."
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
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="subType",
        title="Finer grained claim type information",
        description=(
            "A finer grained suite of claim subtype codes which may convey "
            "Inpatient vs Outpatient and/or a specialty service. In the US the "
            "BillType."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    totalBenefit: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="totalBenefit",
        title="Total benefit payable for the Claim",
        description=(
            "Total amount of benefit payable (Equal to sum of the Benefit amounts "
            "from all detail lines and additions less the Unallocated Deductable)."
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

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type or discipline",
        description=(
            "The category of claim, eg, oral, pharmacy, vision, insitutional, "
            "professional."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unallocDeductable: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unallocDeductable",
        title="Unallocated deductable",
        description=(
            "The amount of deductable applied which was not allocated to any "
            "particular service line."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefit`` according specification,
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
            "patient",
            "billablePeriod",
            "created",
            "enterer",
            "insurer",
            "provider",
            "organization",
            "referral",
            "facility",
            "claim",
            "claimResponse",
            "outcome",
            "disposition",
            "related",
            "prescription",
            "originalPrescription",
            "payee",
            "information",
            "careTeam",
            "diagnosis",
            "procedure",
            "precedence",
            "insurance",
            "accident",
            "employmentImpacted",
            "hospitalization",
            "item",
            "addItem",
            "totalCost",
            "unallocDeductable",
            "totalBenefit",
            "payment",
            "form",
            "processNote",
            "benefitBalance",
        ]


class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of an accident.
    An accident which resulted in the need for healthcare services.
    """

    __resource_type__ = "ExplanationOfBenefitAccident"

    date: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When the accident occurred",
        description="Date of an accident which these services are addressing.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    locationAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="locationAddress",
        title="Accident Place",
        description="Where the accident occurred.",
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
        title="Accident Place",
        description="Where the accident occurred.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="The nature of the accident",
        description="Type of accident: work, auto, etc.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitAccident`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "date",
            "type",
            "locationAddress",
            "locationReference",
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
        one_of_many_fields = {"location": ["locationAddress", "locationReference"]}
        return one_of_many_fields


class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The first tier service adjudications for payor added services.
    """

    __resource_type__ = "ExplanationOfBenefitAddItem"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
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

    detail: typing.List[fhirtypes.ExplanationOfBenefitAddItemDetailType] | None = Field(  # type: ignore
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
        description="The fee charged for the professional service or product.",
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
        title="Billing Code",
        description=(
            "If this is an actual service or product line, ie. not a Group, then "
            "use code to indicate the Professional Service or Product supplied (eg."
            " CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI). If a grouping item then "
            "use a group code to indicate the type of thing being grouped eg. "
            "'glasses' or 'compound'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitAddItem`` according specification,
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


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Added items details.
    The second tier service adjudications for payor added services.
    """

    __resource_type__ = "ExplanationOfBenefitAddItemDetail"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
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
        description="The fee charged for the professional service or product.",
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
        title="Billing Code",
        description=(
            "A code to indicate the Professional Service or Product supplied (eg. "
            "CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitAddItemDetail`` according specification,
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


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Balance by Benefit Category.
    """

    __resource_type__ = "ExplanationOfBenefitBenefitBalance"

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Type of services covered",
        description="Dental, Vision, Medical, Pharmacy, Rehab etc.",
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Description of the benefit or services covered",
        description=(
            "A richer description of the benefit, for example 'DENT2 covers 100% of"
            " basic, 50% of major but exclused Ortho, Implants and Costmetic "
            "services'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    excluded: bool | None = Field(  # type: ignore
        None,
        alias="excluded",
        title="Excluded from the plan",
        description=(
            "True if the indicated class of service is excluded from the plan, "
            "missing or False indicated the service is included in the coverage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_excluded", title="Extension field for ``excluded``."
    )

    financial: typing.List[fhirtypes.ExplanationOfBenefitBenefitBalanceFinancialType] | None = Field(  # type: ignore
        None,
        alias="financial",
        title="Benefit Summary",
        description="Benefits Used to date.",
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Short name for the benefit",
        description="A short name or tag for the benefit, for example MED01, or DENT2.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="network",
        title="In or out of network",
        description="Network designation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subCategory: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subCategory",
        title="Detailed services covered within the type",
        description="Dental: basic, major, ortho; Vision exam, glasses, contacts; etc.",
        json_schema_extra={
            "element_property": True,
        },
    )

    term: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="term",
        title="Annual or lifetime",
        description=(
            "The term or period of the values such as 'maximum lifetime benefit' or"
            " 'maximum annual vistis'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unit: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="unit",
        title="Individual or family",
        description="Unit designation: individual or family.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitBenefitBalance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "subCategory",
            "excluded",
            "name",
            "description",
            "network",
            "unit",
            "term",
            "financial",
        ]


class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefit Summary.
    Benefits Used to date.
    """

    __resource_type__ = "ExplanationOfBenefitBenefitBalanceFinancial"

    allowedMoney: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="allowedMoney",
        title="Benefits allowed",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": False,
        },
    )

    allowedString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="allowedString",
        title="Benefits allowed",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": False,
        },
    )
    allowedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_allowedString", title="Extension field for ``allowedString``."
    )

    allowedUnsignedInt: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="allowedUnsignedInt",
        title="Benefits allowed",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e allowed[x]
            "one_of_many": "allowed",
            "one_of_many_required": False,
        },
    )
    allowedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_allowedUnsignedInt",
        title="Extension field for ``allowedUnsignedInt``.",
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Deductable, visits, benefit amount",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    usedMoney: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="usedMoney",
        title="Benefits used",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e used[x]
            "one_of_many": "used",
            "one_of_many_required": False,
        },
    )

    usedUnsignedInt: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="usedUnsignedInt",
        title="Benefits used",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e used[x]
            "one_of_many": "used",
            "one_of_many_required": False,
        },
    )
    usedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_usedUnsignedInt", title="Extension field for ``usedUnsignedInt``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitBenefitBalanceFinancial`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "allowedUnsignedInt",
            "allowedString",
            "allowedMoney",
            "usedUnsignedInt",
            "usedMoney",
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
            "allowed": ["allowedMoney", "allowedString", "allowedUnsignedInt"],
            "used": ["usedMoney", "usedUnsignedInt"],
        }
        return one_of_many_fields


class ExplanationOfBenefitCareTeam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Care Team members.
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """

    __resource_type__ = "ExplanationOfBenefitCareTeam"

    provider: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="provider",
        title="Member of the Care Team",
        description="The members of the team who provided the overall service.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "Organization"],
        },
    )

    qualification: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="qualification",
        title="Type, classification or Specialization",
        description="The qualification which is applicable for this service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    responsible: bool | None = Field(  # type: ignore
        None,
        alias="responsible",
        title="Billing practitioner",
        description=(
            "The practitioner who is billing and responsible for the claimed "
            "services rendered to the patient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    responsible__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_responsible", title="Extension field for ``responsible``."
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title="Role on the team",
        description=(
            "The lead, assisting or supervising practitioner and their discipline "
            "if a multidisiplinary team."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Number to covey order of careteam",
        description="Sequence of careteam which serves to order and provide a link.",
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
        ``ExplanationOfBenefitCareTeam`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "provider",
            "responsible",
            "role",
            "qualification",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        return required_fields


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of Diagnosis.
    Ordered list of patient diagnosis for which care is sought.
    """

    __resource_type__ = "ExplanationOfBenefitDiagnosis"

    diagnosisCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="diagnosisCodeableConcept",
        title="Patient's diagnosis",
        description="The diagnosis.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e diagnosis[x]
            "one_of_many": "diagnosis",
            "one_of_many_required": True,
        },
    )

    diagnosisReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="diagnosisReference",
        title="Patient's diagnosis",
        description="The diagnosis.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e diagnosis[x]
            "one_of_many": "diagnosis",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition"],
        },
    )

    packageCode: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="packageCode",
        title="Package billing code",
        description=(
            "The package billing code, for example DRG, based on the assigned "
            "grouping code system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Number to covey order of diagnosis",
        description="Sequence of diagnosis which serves to provide a link.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Timing or nature of the diagnosis",
        description=(
            "The type of the Diagnosis, for example: admitting, primary, secondary,"
            " discharge."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitDiagnosis`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "diagnosisCodeableConcept",
            "diagnosisReference",
            "type",
            "packageCode",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        return required_fields

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
            "diagnosis": ["diagnosisCodeableConcept", "diagnosisReference"]
        }
        return one_of_many_fields


class ExplanationOfBenefitInformation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """

    __resource_type__ = "ExplanationOfBenefitInformation"

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="General class of information",
        description=(
            "The general class of the information supplied: information; exception;"
            " accident, employment; onset, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Type of information",
        description=(
            "System and code pertaining to the specific information regarding "
            "special conditions relating to the setting, treatment or patient  for "
            "which care is sought which may influence the adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Reason associated with the information",
        description=(
            "For example, provides the reason for: the additional stay, or missing "
            "tooth or any other situation where a reason code is required in "
            "addition to the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Information instance identifier",
        description="Sequence of the information element which serves to provide a link.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    timingDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="timingDate",
        title="When it occurred",
        description="The date when or period to which this information refers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )
    timingDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_timingDate", title="Extension field for ``timingDate``."
    )

    timingPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="timingPeriod",
        title="When it occurred",
        description="The date when or period to which this information refers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="valueReference",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="valueString",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitInformation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "category",
            "code",
            "timingDate",
            "timingPeriod",
            "valueString",
            "valueQuantity",
            "valueAttachment",
            "valueReference",
            "reason",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        return required_fields

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
            "timing": ["timingDate", "timingPeriod"],
            "value": [
                "valueAttachment",
                "valueQuantity",
                "valueReference",
                "valueString",
            ],
        }
        return one_of_many_fields


class ExplanationOfBenefitInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan.
    Financial instrument by which payment information for health care.
    """

    __resource_type__ = "ExplanationOfBenefitInsurance"

    coverage: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="coverage",
        title="Insurance information",
        description="Reference to the program or plan identification, underwriter or payor.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitInsurance`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "coverage", "preAuthRef"]


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Goods and Services.
    First tier of goods and services.
    """

    __resource_type__ = "ExplanationOfBenefitItem"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Adjudication details",
        description="The adjudications results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    bodySite: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Service Location",
        description="Physical service site on the patient (limb, tooth, etc).",
        json_schema_extra={
            "element_property": True,
        },
    )

    careTeamLinkId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="careTeamLinkId",
        title="Applicable careteam members",
        description="Careteam applicable for this service or product line.",
        json_schema_extra={
            "element_property": True,
        },
    )
    careTeamLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_careTeamLinkId", title="Extension field for ``careTeamLinkId``."
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

    detail: typing.List[fhirtypes.ExplanationOfBenefitItemDetailType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Additional items",
        description="Second tier of goods and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    diagnosisLinkId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="diagnosisLinkId",
        title="Applicable diagnoses",
        description="Diagnosis applicable for this service or product line.",
        json_schema_extra={
            "element_property": True,
        },
    )
    diagnosisLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_diagnosisLinkId", title="Extension field for ``diagnosisLinkId``."
    )

    encounter: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounters related to this billed item",
        description=(
            "A billed item may include goods or services provided in multiple "
            "encounters."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
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

    informationLinkId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="informationLinkId",
        title="Applicable exception and supporting information",
        description=(
            "Exceptions, special conditions and supporting information pplicable "
            "for this service or product line."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    informationLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_informationLinkId",
        title="Extension field for ``informationLinkId``.",
    )

    locationAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        None,
        alias="locationAddress",
        title="Place of service",
        description="Where the service was provided.",
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
        title="Place of service",
        description="Where the service was provided.",
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
        title="Place of service",
        description="Where the service was provided.",
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
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
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
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
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

    procedureLinkId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="procedureLinkId",
        title="Applicable procedures",
        description="Procedures applicable for this service or product line.",
        json_schema_extra={
            "element_property": True,
        },
    )
    procedureLinkId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_procedureLinkId", title="Extension field for ``procedureLinkId``."
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
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

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="service",
        title="Billing Code",
        description=(
            "If this is an actual service or product line, ie. not a Group, then "
            "use code to indicate the Professional Service or Product supplied (eg."
            " CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI). If a grouping item then "
            "use a group code to indicate the type of thing being grouped eg. "
            "'glasses' or 'compound'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    servicedDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="servicedDate",
        title="Date or dates of Service",
        description=(
            "The date or dates when the enclosed suite of services were performed "
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
        title="Date or dates of Service",
        description=(
            "The date or dates when the enclosed suite of services were performed "
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
        title="Service Sub-location",
        description="A region or surface of the site, eg. limb region or tooth surface(s).",
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description=(
            "If the item is a node then this is the fee for the product or service,"
            " otherwise this is the total of the fees for the children of the "
            "group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "careTeamLinkId",
            "diagnosisLinkId",
            "procedureLinkId",
            "informationLinkId",
            "revenue",
            "category",
            "service",
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
            "udi",
            "bodySite",
            "subSite",
            "encounter",
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
        required_fields = [("sequence", "sequence__ext")]
        return required_fields

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


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication details.
    The adjudications results.
    """

    __resource_type__ = "ExplanationOfBenefitItemAdjudication"

    amount: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Monetary amount",
        description="Monitory amount associated with the code.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="Adjudication category such as co-pay, eligible, benefit, etc.",
        description="Code indicating: Co-Pay, deductable, elegible, benefit, tax, etc.",
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
        title="Non-monitory value",
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
        ``ExplanationOfBenefitItemAdjudication`` according specification,
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


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Second tier of goods and services.
    """

    __resource_type__ = "ExplanationOfBenefitItemDetail"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Detail level adjudication details",
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
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Total additional item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
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

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
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

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="service",
        title="Billing Code",
        description=(
            "If this is an actual service or product line, ie. not a Group, then "
            "use code to indicate the Professional Service or Product supplied (eg."
            " CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI). If a grouping item then "
            "use a group code to indicate the type of thing being grouped eg. "
            "'glasses' or 'compound'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subDetail: typing.List[fhirtypes.ExplanationOfBenefitItemDetailSubDetailType] | None = Field(  # type: ignore
        None,
        alias="subDetail",
        title="Additional items",
        description="Third tier of goods and services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Group or type of product or service",
        description="The type of product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description=(
            "If the item is a node then this is the fee for the product or service,"
            " otherwise this is the total of the fees for the children of the "
            "group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "type",
            "revenue",
            "category",
            "service",
            "modifier",
            "programCode",
            "quantity",
            "unitPrice",
            "factor",
            "net",
            "udi",
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
        required_fields = [("sequence", "sequence__ext")]
        return required_fields


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Third tier of goods and services.
    """

    __resource_type__ = "ExplanationOfBenefitItemDetailSubDetail"

    adjudication: typing.List[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None = Field(  # type: ignore
        None,
        alias="adjudication",
        title="Language if different from the resource",
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
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="net",
        title="Net additional item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
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

    programCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
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

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="service",
        title="Billing Code",
        description=(
            "A code to indicate the Professional Service or Product supplied (eg. "
            "CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type of product or service",
        description="The type of product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    udi: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    unitPrice: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description="The fee for an addittional service or product or charge.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitItemDetailSubDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "type",
            "revenue",
            "category",
            "service",
            "modifier",
            "programCode",
            "quantity",
            "unitPrice",
            "factor",
            "net",
            "udi",
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
        required_fields = [("sequence", "sequence__ext")]
        return required_fields


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Party to be paid any benefits payable.
    The party to be reimbursed for the services.
    """

    __resource_type__ = "ExplanationOfBenefitPayee"

    party: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="party",
        title="Party to receive the payable",
        description="Party to be reimbursed: Subscriber, provider, other.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    resourceType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="resourceType",
        title="organization | patient | practitioner | relatedperson",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type of party: Subscriber, Provider, other",
        description="Type of Party to be reimbursed: Subscriber, provider, other.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitPayee`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "resourceType", "party"]


class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Payment (if paid).
    Payment details for the claim if the claim has been paid.
    """

    __resource_type__ = "ExplanationOfBenefitPayment"

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
        title="Expected date of Payment",
        description="Estimated payment date.",
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
        description="Payment identifer.",
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
        ``ExplanationOfBenefitPayment`` according specification,
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


class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Procedures performed.
    Ordered list of patient procedures performed to support the adjudication.
    """

    __resource_type__ = "ExplanationOfBenefitProcedure"

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When the procedure was performed",
        description="Date and optionally time the procedure was performed .",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    procedureCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="procedureCodeableConcept",
        title="Patient's list of procedures performed",
        description="The procedure code.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e procedure[x]
            "one_of_many": "procedure",
            "one_of_many_required": True,
        },
    )

    procedureReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="procedureReference",
        title="Patient's list of procedures performed",
        description="The procedure code.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e procedure[x]
            "one_of_many": "procedure",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Procedure"],
        },
    )

    sequence: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="sequence",
        title="Procedure sequence for reference",
        description="Sequence of procedures which serves to order and provide a link.",
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
        ``ExplanationOfBenefitProcedure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "date",
            "procedureCodeableConcept",
            "procedureReference",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        return required_fields

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
            "procedure": ["procedureCodeableConcept", "procedureReference"]
        }
        return one_of_many_fields


class ExplanationOfBenefitProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing notes.
    Note text.
    """

    __resource_type__ = "ExplanationOfBenefitProcessNote"

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
        title="Sequence number for this note",
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
        title="Note explanitory text",
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
        ``ExplanationOfBenefitProcessNote`` according specification,
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


class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Related Claims which may be revelant to processing this claim.
    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """

    __resource_type__ = "ExplanationOfBenefitRelated"

    claim: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="claim",
        title="Reference to the related claim",
        description=(
            "Other claims which are related to this claim such as prior claim "
            "versions or for related services."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Claim"],
        },
    )

    reference: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Related file or case reference",
        description=(
            "An alternate organizational reference to the case or file to which "
            "this particular claim pertains - eg Property/Casualy insurer claim # "
            "or Workers Compensation case # ."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relationship: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="relationship",
        title="How the reference claim is related",
        description="For example prior or umbrella.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExplanationOfBenefitRelated`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "claim",
            "relationship",
            "reference",
        ]
