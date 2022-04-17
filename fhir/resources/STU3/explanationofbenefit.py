# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

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

    resource_type = Field("ExplanationOfBenefit", const=True)

    accident: fhirtypes.ExplanationOfBenefitAccidentType = Field(
        None,
        alias="accident",
        title="Details of an accident",
        description="An accident which resulted in the need for healthcare services.",
        # if property is element of this resource.
        element_property=True,
    )

    addItem: typing.List[fhirtypes.ExplanationOfBenefitAddItemType] = Field(
        None,
        alias="addItem",
        title="Insurer added line items",
        description="The first tier service adjudications for payor added services.",
        # if property is element of this resource.
        element_property=True,
    )

    benefitBalance: typing.List[
        fhirtypes.ExplanationOfBenefitBenefitBalanceType
    ] = Field(
        None,
        alias="benefitBalance",
        title="Balance by Benefit Category",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    billablePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="billablePeriod",
        title="Period for charge submission",
        description="The billable period for which charges are being submitted.",
        # if property is element of this resource.
        element_property=True,
    )

    careTeam: typing.List[fhirtypes.ExplanationOfBenefitCareTeamType] = Field(
        None,
        alias="careTeam",
        title="Care Team members",
        description=(
            "The members of the team who provided the overall service as well as "
            "their role and whether responsible and qualifications."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    claim: fhirtypes.ReferenceType = Field(
        None,
        alias="claim",
        title="Claim reference",
        description=(
            "The business identifier for the instance: invoice number, claim "
            "number, pre-determination or pre-authorization number."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Claim"],
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title="Claim response reference",
        description=(
            "The business identifier for the instance: invoice number, claim "
            "number, pre-determination or pre-authorization number."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClaimResponse"],
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description="The date when the EOB was created.",
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    diagnosis: typing.List[fhirtypes.ExplanationOfBenefitDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of Diagnosis",
        description="Ordered list of patient diagnosis for which care is sought.",
        # if property is element of this resource.
        element_property=True,
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
        # if property is element of this resource.
        element_property=True,
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    employmentImpacted: fhirtypes.PeriodType = Field(
        None,
        alias="employmentImpacted",
        title="Period unable to work",
        description=(
            "The start and optional end dates of when the patient was precluded "
            "from working due to the treatable condition(s)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title="Author",
        description="The person who created the explanation of benefit.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    facility: fhirtypes.ReferenceType = Field(
        None,
        alias="facility",
        title="Servicing Facility",
        description="Facility where the services were provided.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
        # if property is element of this resource.
        element_property=True,
    )

    hospitalization: fhirtypes.PeriodType = Field(
        None,
        alias="hospitalization",
        title="Period in hospital",
        description=(
            "The start and optional end dates of when the patient was confined to a"
            " treatment center."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The EOB Business Identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    information: typing.List[fhirtypes.ExplanationOfBenefitInformationType] = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    insurance: fhirtypes.ExplanationOfBenefitInsuranceType = Field(
        None,
        alias="insurance",
        title="Insurance or medical plan",
        description="Financial instrument by which payment information for health care.",
        # if property is element of this resource.
        element_property=True,
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Insurer responsible for the EOB",
        description="The insurer which is responsible for the explanation of benefit.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    item: typing.List[fhirtypes.ExplanationOfBenefitItemType] = Field(
        None,
        alias="item",
        title="Goods and Services",
        description="First tier of goods and services.",
        # if property is element of this resource.
        element_property=True,
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Responsible organization for the claim",
        description="The provider which is responsible for the claim.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    originalPrescription: fhirtypes.ReferenceType = Field(
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest"],
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Processing outcome errror, partial or complete processing.",
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="The subject of the Products and Services",
        description="Patient Resource.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    payee: fhirtypes.ExplanationOfBenefitPayeeType = Field(
        None,
        alias="payee",
        title="Party to be paid any benefits payable",
        description="The party to be reimbursed for the services.",
        # if property is element of this resource.
        element_property=True,
    )

    payment: fhirtypes.ExplanationOfBenefitPaymentType = Field(
        None,
        alias="payment",
        title="Payment (if paid)",
        description="Payment details for the claim if the claim has been paid.",
        # if property is element of this resource.
        element_property=True,
    )

    precedence: fhirtypes.PositiveInt = Field(
        None,
        alias="precedence",
        title="Precedence (primary, secondary, etc.)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    precedence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_precedence", title="Extension field for ``precedence``."
    )

    prescription: fhirtypes.ReferenceType = Field(
        None,
        alias="prescription",
        title="Prescription authorizing services or products",
        description="Prescription to support the dispensing of Pharmacy or Vision products.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest", "VisionPrescription"],
    )

    procedure: typing.List[fhirtypes.ExplanationOfBenefitProcedureType] = Field(
        None,
        alias="procedure",
        title="Procedures performed",
        description=(
            "Ordered list of patient procedures performed to support the "
            "adjudication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    processNote: typing.List[fhirtypes.ExplanationOfBenefitProcessNoteType] = Field(
        None,
        alias="processNote",
        title="Processing notes",
        description="Note text.",
        # if property is element of this resource.
        element_property=True,
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Responsible provider for the claim",
        description="The provider which is responsible for the claim.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    referral: fhirtypes.ReferenceType = Field(
        None,
        alias="referral",
        title="Treatment Referral",
        description=(
            "The referral resource which lists the date, practitioner, reason and "
            "other supporting information."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ReferralRequest"],
    )

    related: typing.List[fhirtypes.ExplanationOfBenefitRelatedType] = Field(
        None,
        alias="related",
        title="Related Claims which may be revelant to processing this claim",
        description=(
            "Other claims which are related to this claim such as prior claim "
            "versions or for related services."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
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

    subType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subType",
        title="Finer grained claim type information",
        description=(
            "A finer grained suite of claim subtype codes which may convey "
            "Inpatient vs Outpatient and/or a specialty service. In the US the "
            "BillType."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    totalBenefit: fhirtypes.MoneyType = Field(
        None,
        alias="totalBenefit",
        title="Total benefit payable for the Claim",
        description=(
            "Total amount of benefit payable (Equal to sum of the Benefit amounts "
            "from all detail lines and additions less the Unallocated Deductable)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    totalCost: fhirtypes.MoneyType = Field(
        None,
        alias="totalCost",
        title="Total Cost of service from the Claim",
        description="The total cost of the services reported.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type or discipline",
        description=(
            "The category of claim, eg, oral, pharmacy, vision, insitutional, "
            "professional."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    unallocDeductable: fhirtypes.MoneyType = Field(
        None,
        alias="unallocDeductable",
        title="Unallocated deductable",
        description=(
            "The amount of deductable applied which was not allocated to any "
            "particular service line."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExplanationOfBenefitAccident", const=True)

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="When the accident occurred",
        description="Date of an accident which these services are addressing.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Accident Place",
        description="Where the accident occurred.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Accident Place",
        description="Where the accident occurred.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The nature of the accident",
        description="Type of accident: work, auto, etc.",
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3017(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The first tier service adjudications for payor added services.
    """

    resource_type = Field("ExplanationOfBenefitAddItem", const=True)

    adjudication: typing.List[
        fhirtypes.ExplanationOfBenefitItemAdjudicationType
    ] = Field(
        None,
        alias="adjudication",
        title="Added items adjudication",
        description="The adjudications results.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    detail: typing.List[fhirtypes.ExplanationOfBenefitAddItemDetailType] = Field(
        None,
        alias="detail",
        title="Added items details",
        description="The second tier service adjudications for payor added services.",
        # if property is element of this resource.
        element_property=True,
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Professional fee or Product charge",
        description="The fee charged for the professional service or product.",
        # if property is element of this resource.
        element_property=True,
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequenceLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="sequenceLinkId",
        title="Service instances",
        description=(
            "List of input service items which this service line is intended to "
            "replace."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    sequenceLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_sequenceLinkId", title="Extension field for ``sequenceLinkId``."
    )

    service: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExplanationOfBenefitAddItemDetail", const=True)

    adjudication: typing.List[
        fhirtypes.ExplanationOfBenefitItemAdjudicationType
    ] = Field(
        None,
        alias="adjudication",
        title="Added items detail adjudication",
        description="The adjudications results.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Professional fee or Product charge",
        description="The fee charged for the professional service or product.",
        # if property is element of this resource.
        element_property=True,
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Billing Code",
        description=(
            "A code to indicate the Professional Service or Product supplied (eg. "
            "CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI)."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExplanationOfBenefitBenefitBalance", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type of services covered",
        description="Dental, Vision, Medical, Pharmacy, Rehab etc.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Description of the benefit or services covered",
        description=(
            "A richer description of the benefit, for example 'DENT2 covers 100% of"
            " basic, 50% of major but exclused Ortho, Implants and Costmetic "
            "services'."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    excluded: bool = Field(
        None,
        alias="excluded",
        title="Excluded from the plan",
        description=(
            "True if the indicated class of service is excluded from the plan, "
            "missing or False indicated the service is included in the coverage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_excluded", title="Extension field for ``excluded``."
    )

    financial: typing.List[
        fhirtypes.ExplanationOfBenefitBenefitBalanceFinancialType
    ] = Field(
        None,
        alias="financial",
        title="Benefit Summary",
        description="Benefits Used to date.",
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Short name for the benefit",
        description="A short name or tag for the benefit, for example MED01, or DENT2.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.CodeableConceptType = Field(
        None,
        alias="network",
        title="In or out of network",
        description="Network designation.",
        # if property is element of this resource.
        element_property=True,
    )

    subCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subCategory",
        title="Detailed services covered within the type",
        description="Dental: basic, major, ortho; Vision exam, glasses, contacts; etc.",
        # if property is element of this resource.
        element_property=True,
    )

    term: fhirtypes.CodeableConceptType = Field(
        None,
        alias="term",
        title="Annual or lifetime",
        description=(
            "The term or period of the values such as 'maximum lifetime benefit' or"
            " 'maximum annual vistis'."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Individual or family",
        description="Unit designation: individual or family.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExplanationOfBenefitBenefitBalanceFinancial", const=True)

    allowedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="allowedMoney",
        title="Benefits allowed",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )

    allowedString: fhirtypes.String = Field(
        None,
        alias="allowedString",
        title="Benefits allowed",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )
    allowedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allowedString", title="Extension field for ``allowedString``."
    )

    allowedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="allowedUnsignedInt",
        title="Benefits allowed",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )
    allowedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allowedUnsignedInt",
        title="Extension field for ``allowedUnsignedInt``.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Deductable, visits, benefit amount",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    usedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="usedMoney",
        title="Benefits used",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e used[x]
        one_of_many="used",
        one_of_many_required=False,
    )

    usedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="usedUnsignedInt",
        title="Benefits used",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e used[x]
        one_of_many="used",
        one_of_many_required=False,
    )
    usedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4494(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ExplanationOfBenefitCareTeam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Care Team members.
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """

    resource_type = Field("ExplanationOfBenefitCareTeam", const=True)

    provider: fhirtypes.ReferenceType = Field(
        ...,
        alias="provider",
        title="Member of the Care Team",
        description="The members of the team who provided the overall service.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    qualification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="qualification",
        title="Type, classification or Specialization",
        description="The qualification which is applicable for this service.",
        # if property is element of this resource.
        element_property=True,
    )

    responsible: bool = Field(
        None,
        alias="responsible",
        title="Billing practitioner",
        description=(
            "The practitioner who is billing and responsible for the claimed "
            "services rendered to the patient."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    responsible__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_responsible", title="Extension field for ``responsible``."
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Role on the team",
        description=(
            "The lead, assisting or supervising practitioner and their discipline "
            "if a multidisiplinary team."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Number to covey order of careteam",
        description="Sequence of careteam which serves to order and provide a link.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2985(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of Diagnosis.
    Ordered list of patient diagnosis for which care is sought.
    """

    resource_type = Field("ExplanationOfBenefitDiagnosis", const=True)

    diagnosisCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="diagnosisCodeableConcept",
        title="Patient's diagnosis",
        description="The diagnosis.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e diagnosis[x]
        one_of_many="diagnosis",
        one_of_many_required=True,
    )

    diagnosisReference: fhirtypes.ReferenceType = Field(
        None,
        alias="diagnosisReference",
        title="Patient's diagnosis",
        description="The diagnosis.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e diagnosis[x]
        one_of_many="diagnosis",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    packageCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="packageCode",
        title="Package billing code",
        description=(
            "The package billing code, for example DRG, based on the assigned "
            "grouping code system."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Number to covey order of diagnosis",
        description="Sequence of diagnosis which serves to provide a link.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Timing or nature of the diagnosis",
        description=(
            "The type of the Diagnosis, for example: admitting, primary, secondary,"
            " discharge."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3150(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3150(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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

    resource_type = Field("ExplanationOfBenefitInformation", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="General class of information",
        description=(
            "The general class of the information supplied: information; exception;"
            " accident, employment; onset, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type of information",
        description=(
            "System and code pertaining to the specific information regarding "
            "special conditions relating to the setting, treatment or patient  for "
            "which care is sought which may influence the adjudication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reason: fhirtypes.CodingType = Field(
        None,
        alias="reason",
        title="Reason associated with the information",
        description=(
            "For example, provides the reason for: the additional stay, or missing "
            "tooth or any other situation where a reason code is required in "
            "addition to the content."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Information instance identifier",
        description="Sequence of the information element which serves to provide a link.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    timingDate: fhirtypes.Date = Field(
        None,
        alias="timingDate",
        title="When it occurred",
        description="The date when or period to which this information refers.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )
    timingDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timingDate", title="Extension field for ``timingDate``."
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="When it occurred",
        description="The date when or period to which this information refers.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Additional Data or supporting information",
        description=(
            "Additional data or information such as resources, documents, images "
            "etc. including references to the data or the actual inclusion of the "
            "data."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3374(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3374(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ExplanationOfBenefitInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurance or medical plan.
    Financial instrument by which payment information for health care.
    """

    resource_type = Field("ExplanationOfBenefitInsurance", const=True)

    coverage: fhirtypes.ReferenceType = Field(
        None,
        alias="coverage",
        title="Insurance information",
        description="Reference to the program or plan identification, underwriter or payor.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Coverage"],
    )

    preAuthRef: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="preAuthRef",
        title="Pre-Authorization/Determination Reference",
        description="A list of references from the Insurer to which these services pertain.",
        # if property is element of this resource.
        element_property=True,
    )
    preAuthRef__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_preAuthRef", title="Extension field for ``preAuthRef``.")

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

    resource_type = Field("ExplanationOfBenefitItem", const=True)

    adjudication: typing.List[
        fhirtypes.ExplanationOfBenefitItemAdjudicationType
    ] = Field(
        None,
        alias="adjudication",
        title="Adjudication details",
        description="The adjudications results.",
        # if property is element of this resource.
        element_property=True,
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Service Location",
        description="Physical service site on the patient (limb, tooth, etc).",
        # if property is element of this resource.
        element_property=True,
    )

    careTeamLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="careTeamLinkId",
        title="Applicable careteam members",
        description="Careteam applicable for this service or product line.",
        # if property is element of this resource.
        element_property=True,
    )
    careTeamLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_careTeamLinkId", title="Extension field for ``careTeamLinkId``."
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    detail: typing.List[fhirtypes.ExplanationOfBenefitItemDetailType] = Field(
        None,
        alias="detail",
        title="Additional items",
        description="Second tier of goods and services.",
        # if property is element of this resource.
        element_property=True,
    )

    diagnosisLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="diagnosisLinkId",
        title="Applicable diagnoses",
        description="Diagnosis applicable for this service or product line.",
        # if property is element of this resource.
        element_property=True,
    )
    diagnosisLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_diagnosisLinkId", title="Extension field for ``diagnosisLinkId``."
    )

    encounter: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="encounter",
        title="Encounters related to this billed item",
        description=(
            "A billed item may include goods or services provided in multiple "
            "encounters."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    informationLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="informationLinkId",
        title="Applicable exception and supporting information",
        description=(
            "Exceptions, special conditions and supporting information pplicable "
            "for this service or product line."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    informationLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_informationLinkId",
        title="Extension field for ``informationLinkId``.",
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Place of service",
        description="Where the service was provided.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
    )

    locationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="locationCodeableConcept",
        title="Place of service",
        description="Where the service was provided.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Place of service",
        description="Where the service was provided.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    procedureLinkId: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="procedureLinkId",
        title="Applicable procedures",
        description="Procedures applicable for this service or product line.",
        # if property is element of this resource.
        element_property=True,
    )
    procedureLinkId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_procedureLinkId", title="Extension field for ``procedureLinkId``."
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
        # if property is element of this resource.
        element_property=True,
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    servicedDate: fhirtypes.Date = Field(
        None,
        alias="servicedDate",
        title="Date or dates of Service",
        description=(
            "The date or dates when the enclosed suite of services were performed "
            "or completed."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e serviced[x]
        one_of_many="serviced",
        one_of_many_required=False,
    )
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_servicedDate", title="Extension field for ``servicedDate``."
    )

    servicedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicedPeriod",
        title="Date or dates of Service",
        description=(
            "The date or dates when the enclosed suite of services were performed "
            "or completed."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e serviced[x]
        one_of_many="serviced",
        one_of_many_required=False,
    )

    subSite: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subSite",
        title="Service Sub-location",
        description="A region or surface of the site, eg. limb region or tooth surface(s).",
        # if property is element of this resource.
        element_property=True,
    )

    udi: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description=(
            "If the item is a node then this is the fee for the product or service,"
            " otherwise this is the total of the fees for the children of the "
            "group."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2614(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2614(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication details.
    The adjudications results.
    """

    resource_type = Field("ExplanationOfBenefitItemAdjudication", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Monetary amount",
        description="Monitory amount associated with the code.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Adjudication category such as co-pay, eligible, benefit, etc.",
        description="Code indicating: Co-Pay, deductable, elegible, benefit, tax, etc.",
        # if property is element of this resource.
        element_property=True,
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Explanation of Adjudication outcome",
        description="Adjudication reason such as limit reached.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Non-monitory value",
        description=(
            "A non-monetary value for example a percentage. Mutually exclusive to "
            "the amount element above."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field("ExplanationOfBenefitItemDetail", const=True)

    adjudication: typing.List[
        fhirtypes.ExplanationOfBenefitItemAdjudicationType
    ] = Field(
        None,
        alias="adjudication",
        title="Detail level adjudication details",
        description="The adjudications results.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Total additional item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    programCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
        # if property is element of this resource.
        element_property=True,
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    subDetail: typing.List[
        fhirtypes.ExplanationOfBenefitItemDetailSubDetailType
    ] = Field(
        None,
        alias="subDetail",
        title="Additional items",
        description="Third tier of goods and services.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Group or type of product or service",
        description="The type of product or service.",
        # if property is element of this resource.
        element_property=True,
    )

    udi: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description=(
            "If the item is a node then this is the fee for the product or service,"
            " otherwise this is the total of the fees for the children of the "
            "group."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3208(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Third tier of goods and services.
    """

    resource_type = Field("ExplanationOfBenefitItemDetailSubDetail", const=True)

    adjudication: typing.List[
        fhirtypes.ExplanationOfBenefitItemAdjudicationType
    ] = Field(
        None,
        alias="adjudication",
        title="Language if different from the resource",
        description="The adjudications results.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Net additional item cost",
        description=(
            "The quantity times the unit price for an addittional service or "
            "product or charge. For example, the formula: unit Quantity * unit "
            "Price (Cost per Point) * factor Number  * points = net Amount. "
            "Quantity, factor and points are assumed to be 1 if not supplied."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    noteNumber: typing.List[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
        # if property is element of this resource.
        element_property=True,
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    programCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
        # if property is element of this resource.
        element_property=True,
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Billing Code",
        description=(
            "A code to indicate the Professional Service or Product supplied (eg. "
            "CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of product or service",
        description="The type of product or service.",
        # if property is element of this resource.
        element_property=True,
    )

    udi: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description="The fee for an addittional service or product or charge.",
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4101(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Party to be paid any benefits payable.
    The party to be reimbursed for the services.
    """

    resource_type = Field("ExplanationOfBenefitPayee", const=True)

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title="Party to receive the payable",
        description="Party to be reimbursed: Subscriber, provider, other.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Patient",
            "RelatedPerson",
        ],
    )

    resourceType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="resourceType",
        title="organization | patient | practitioner | relatedperson",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of party: Subscriber, Provider, other",
        description="Type of Party to be reimbursed: Subscriber, provider, other.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExplanationOfBenefitPayment", const=True)

    adjustment: fhirtypes.MoneyType = Field(
        None,
        alias="adjustment",
        title="Payment adjustment for non-Claim issues",
        description=(
            "Adjustment to the payment of this transaction which is not related to "
            "adjudication of this transaction."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    adjustmentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="adjustmentReason",
        title="Explanation for the non-claim adjustment",
        description="Reason for the payment adjustment.",
        # if property is element of this resource.
        element_property=True,
    )

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Payable amount after adjustment",
        description="Payable less any payment adjustment.",
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Expected date of Payment",
        description="Estimated payment date.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier of the payment instrument",
        description="Payment identifer.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Partial or Complete",
        description="Whether this represents partial or complete payment of the claim.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExplanationOfBenefitProcedure", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the procedure was performed",
        description="Date and optionally time the procedure was performed .",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    procedureCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="procedureCodeableConcept",
        title="Patient's list of procedures performed",
        description="The procedure code.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e procedure[x]
        one_of_many="procedure",
        one_of_many_required=True,
    )

    procedureReference: fhirtypes.ReferenceType = Field(
        None,
        alias="procedureReference",
        title="Patient's list of procedures performed",
        description="The procedure code.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e procedure[x]
        one_of_many="procedure",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Procedure sequence for reference",
        description="Sequence of procedures which serves to order and provide a link.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3144(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("sequence", "sequence__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3144(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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


class ExplanationOfBenefitProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing notes.
    Note text.
    """

    resource_type = Field("ExplanationOfBenefitProcessNote", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="Language if different from the resource",
        description=(
            "The ISO-639-1 alpha 2 code in lower case for the language, optionally "
            "followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in"
            ' upper case; e.g. "en" for English, or "en-US" for American English '
            'versus "en-EN" for England English.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    number: fhirtypes.PositiveInt = Field(
        None,
        alias="number",
        title="Sequence number for this note",
        description=(
            "An integer associated with each note which may be referred to from "
            "each service line item."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Note explanitory text",
        description="The note text.",
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="display | print | printoper",
        description="The note purpose: Print/Display.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExplanationOfBenefitRelated", const=True)

    claim: fhirtypes.ReferenceType = Field(
        None,
        alias="claim",
        title="Reference to the related claim",
        description=(
            "Other claims which are related to this claim such as prior claim "
            "versions or for related services."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Claim"],
    )

    reference: fhirtypes.IdentifierType = Field(
        None,
        alias="reference",
        title="Related file or case reference",
        description=(
            "An alternate organizational reference to the case or file to which "
            "this particular claim pertains - eg Property/Casualy insurer claim # "
            "or Workers Compensation case # ."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="How the reference claim is related",
        description="For example prior or umbrella.",
        # if property is element of this resource.
        element_property=True,
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
