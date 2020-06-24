# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ExplanationOfBenefit(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )

    addItem: ListType[fhirtypes.ExplanationOfBenefitAddItemType] = Field(
        None,
        alias="addItem",
        title="Insurer added line items",
        description="The first tier service adjudications for payor added services.",
    )

    benefitBalance: ListType[fhirtypes.ExplanationOfBenefitBenefitBalanceType] = Field(
        None,
        alias="benefitBalance",
        title="Balance by Benefit Category",
        description=None,
    )

    billablePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="billablePeriod",
        title="Period for charge submission",
        description="The billable period for which charges are being submitted.",
    )

    careTeam: ListType[fhirtypes.ExplanationOfBenefitCareTeamType] = Field(
        None,
        alias="careTeam",
        title="Care Team members",
        description=(
            "The members of the team who provided the overall service as well as "
            "their role and whether responsible and qualifications."
        ),
    )

    claim: fhirtypes.ReferenceType = Field(
        None,
        alias="claim",
        title="Claim reference",
        description=(
            "The business identifier for the instance: invoice number, claim "
            "number, pre-determination or pre-authorization number."
        ),
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
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClaimResponse"],
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description="The date when the EOB was created.",
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    diagnosis: ListType[fhirtypes.ExplanationOfBenefitDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of Diagnosis",
        description="Ordered list of patient diagnosis for which care is sought.",
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
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
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title="Author",
        description="The person who created the explanation of benefit.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    facility: fhirtypes.ReferenceType = Field(
        None,
        alias="facility",
        title="Servicing Facility",
        description="Facility where the services were provided.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
    )

    hospitalization: fhirtypes.PeriodType = Field(
        None,
        alias="hospitalization",
        title="Period in hospital",
        description=(
            "The start and optional end dates of when the patient was confined to a"
            " treatment center."
        ),
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The EOB Business Identifier.",
    )

    information: ListType[fhirtypes.ExplanationOfBenefitInformationType] = Field(
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
    )

    insurance: fhirtypes.ExplanationOfBenefitInsuranceType = Field(
        None,
        alias="insurance",
        title="Insurance or medical plan",
        description="Financial instrument by which payment information for health care.",
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Insurer responsible for the EOB",
        description="The insurer which is responsible for the explanation of benefit.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    item: ListType[fhirtypes.ExplanationOfBenefitItemType] = Field(
        None,
        alias="item",
        title="Goods and Services",
        description="First tier of goods and services.",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Responsible organization for the claim",
        description="The provider which is responsible for the claim.",
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
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest"],
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Processing outcome errror, partial or complete processing.",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="The subject of the Products and Services",
        description="Patient Resource.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    payee: fhirtypes.ExplanationOfBenefitPayeeType = Field(
        None,
        alias="payee",
        title="Party to be paid any benefits payable",
        description="The party to be reimbursed for the services.",
    )

    payment: fhirtypes.ExplanationOfBenefitPaymentType = Field(
        None,
        alias="payment",
        title="Payment (if paid)",
        description="Payment details for the claim if the claim has been paid.",
    )

    precedence: fhirtypes.PositiveInt = Field(
        None,
        alias="precedence",
        title="Precedence (primary, secondary, etc.)",
        description=None,
    )
    precedence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_precedence", title="Extension field for ``precedence``."
    )

    prescription: fhirtypes.ReferenceType = Field(
        None,
        alias="prescription",
        title="Prescription authorizing services or products",
        description="Prescription to support the dispensing of Pharmacy or Vision products.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest", "VisionPrescription"],
    )

    procedure: ListType[fhirtypes.ExplanationOfBenefitProcedureType] = Field(
        None,
        alias="procedure",
        title="Procedures performed",
        description=(
            "Ordered list of patient procedures performed to support the "
            "adjudication."
        ),
    )

    processNote: ListType[fhirtypes.ExplanationOfBenefitProcessNoteType] = Field(
        None, alias="processNote", title="Processing notes", description="Note text.",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Responsible provider for the claim",
        description="The provider which is responsible for the claim.",
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
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ReferralRequest"],
    )

    related: ListType[fhirtypes.ExplanationOfBenefitRelatedType] = Field(
        None,
        alias="related",
        title="Related Claims which may be revelant to processing this claim",
        description=(
            "Other claims which are related to this claim such as prior claim "
            "versions or for related services."
        ),
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subType",
        title="Finer grained claim type information",
        description=(
            "A finer grained suite of claim subtype codes which may convey "
            "Inpatient vs Outpatient and/or a specialty service. In the US the "
            "BillType."
        ),
    )

    totalBenefit: fhirtypes.MoneyType = Field(
        None,
        alias="totalBenefit",
        title="Total benefit payable for the Claim",
        description=(
            "Total amount of benefit payable (Equal to sum of the Benefit amounts "
            "from all detail lines and additions less the Unallocated Deductable)."
        ),
    )

    totalCost: fhirtypes.MoneyType = Field(
        None,
        alias="totalCost",
        title="Total Cost of service from the Claim",
        description="The total cost of the services reported.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type or discipline",
        description=(
            "The category of claim, eg, oral, pharmacy, vision, insitutional, "
            "professional."
        ),
    )

    unallocDeductable: fhirtypes.MoneyType = Field(
        None,
        alias="unallocDeductable",
        title="Unallocated deductable",
        description=(
            "The amount of deductable applied which was not allocated to any "
            "particular service line."
        ),
    )


class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Accident Place",
        description="Where the accident occurred.",
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Accident Place",
        description="Where the accident occurred.",
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The first tier service adjudications for payor added services.
    """

    resource_type = Field("ExplanationOfBenefitAddItem", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Added items adjudication",
        description="The adjudications results.",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
    )

    detail: ListType[fhirtypes.ExplanationOfBenefitAddItemDetailType] = Field(
        None,
        alias="detail",
        title="Added items details",
        description="The second tier service adjudications for payor added services.",
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Professional fee or Product charge",
        description="The fee charged for the professional service or product.",
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
    )

    sequenceLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="sequenceLinkId",
        title="Service instances",
        description=(
            "List of input service items which this service line is intended to "
            "replace."
        ),
    )
    sequenceLinkId__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
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
    )


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Added items details.
    The second tier service adjudications for payor added services.
    """

    resource_type = Field("ExplanationOfBenefitAddItemDetail", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Added items detail adjudication",
        description="The adjudications results.",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
    )

    fee: fhirtypes.MoneyType = Field(
        None,
        alias="fee",
        title="Professional fee or Product charge",
        description="The fee charged for the professional service or product.",
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Billing Code",
        description=(
            "A code to indicate the Professional Service or Product supplied (eg. "
            "CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI)."
        ),
    )


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_excluded", title="Extension field for ``excluded``."
    )

    financial: ListType[
        fhirtypes.ExplanationOfBenefitBenefitBalanceFinancialType
    ] = Field(
        None,
        alias="financial",
        title="Benefit Summary",
        description="Benefits Used to date.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Short name for the benefit",
        description="A short name or tag for the benefit, for example MED01, or DENT2.",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.CodeableConceptType = Field(
        None,
        alias="network",
        title="In or out of network",
        description="Network designation.",
    )

    subCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subCategory",
        title="Detailed services covered within the type",
        description="Dental: basic, major, ortho; Vision exam, glasses, contacts; etc.",
    )

    term: fhirtypes.CodeableConceptType = Field(
        None,
        alias="term",
        title="Annual or lifetime",
        description=(
            "The term or period of the values such as 'maximum lifetime benefit' or"
            " 'maximum annual vistis'."
        ),
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Individual or family",
        description="Unit designation: individual or family.",
    )


class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )

    allowedString: fhirtypes.String = Field(
        None,
        alias="allowedString",
        title="Benefits allowed",
        description=None,
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
        ..., alias="type", title="Deductable, visits, benefit amount", description=None,
    )

    usedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="usedMoney",
        title="Benefits used",
        description=None,
        # Choice of Data Types. i.e used[x]
        one_of_many="used",
        one_of_many_required=False,
    )

    usedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="usedUnsignedInt",
        title="Benefits used",
        description=None,
        # Choice of Data Types. i.e used[x]
        one_of_many="used",
        one_of_many_required=False,
    )
    usedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_usedUnsignedInt", title="Extension field for ``usedUnsignedInt``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    qualification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="qualification",
        title="Type, classification or Specialization",
        description="The qualification which is applicable for this service.",
    )

    responsible: bool = Field(
        None,
        alias="responsible",
        title="Billing practitioner",
        description=(
            "The practitioner who is billing and responsible for the claimed "
            "services rendered to the patient."
        ),
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
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Number to covey order of careteam",
        description="Sequence of careteam which serves to order and provide a link.",
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        # Choice of Data Types. i.e diagnosis[x]
        one_of_many="diagnosis",
        one_of_many_required=True,
    )

    diagnosisReference: fhirtypes.ReferenceType = Field(
        None,
        alias="diagnosisReference",
        title="Patient's diagnosis",
        description="The diagnosis.",
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
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Number to covey order of diagnosis",
        description="Sequence of diagnosis which serves to provide a link.",
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Timing or nature of the diagnosis",
        description=(
            "The type of the Diagnosis, for example: admitting, primary, secondary,"
            " discharge."
        ),
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Information instance identifier",
        description="Sequence of the information element which serves to provide a link.",
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    timingDate: fhirtypes.Date = Field(
        None,
        alias="timingDate",
        title="When it occurred",
        description="The date when or period to which this information refers.",
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
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Coverage"],
    )

    preAuthRef: ListType[fhirtypes.String] = Field(
        None,
        alias="preAuthRef",
        title="Pre-Authorization/Determination Reference",
        description="A list of references from the Insurer to which these services pertain.",
    )
    preAuthRef__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_preAuthRef", title="Extension field for ``preAuthRef``.")


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Goods and Services.
    First tier of goods and services.
    """

    resource_type = Field("ExplanationOfBenefitItem", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Adjudication details",
        description="The adjudications results.",
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Service Location",
        description="Physical service site on the patient (limb, tooth, etc).",
    )

    careTeamLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="careTeamLinkId",
        title="Applicable careteam members",
        description="Careteam applicable for this service or product line.",
    )
    careTeamLinkId__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
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
    )

    detail: ListType[fhirtypes.ExplanationOfBenefitItemDetailType] = Field(
        None,
        alias="detail",
        title="Additional items",
        description="Second tier of goods and services.",
    )

    diagnosisLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="diagnosisLinkId",
        title="Applicable diagnoses",
        description="Diagnosis applicable for this service or product line.",
    )
    diagnosisLinkId__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_diagnosisLinkId", title="Extension field for ``diagnosisLinkId``."
    )

    encounter: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="encounter",
        title="Encounters related to this billed item",
        description=(
            "A billed item may include goods or services provided in multiple "
            "encounters."
        ),
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
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    informationLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="informationLinkId",
        title="Applicable exception and supporting information",
        description=(
            "Exceptions, special conditions and supporting information pplicable "
            "for this service or product line."
        ),
    )
    informationLinkId__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
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
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
    )

    locationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="locationCodeableConcept",
        title="Place of service",
        description="Where the service was provided.",
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Place of service",
        description="Where the service was provided.",
        # Choice of Data Types. i.e location[x]
        one_of_many="location",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
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
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    procedureLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="procedureLinkId",
        title="Applicable procedures",
        description="Procedures applicable for this service or product line.",
    )
    procedureLinkId__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_procedureLinkId", title="Extension field for ``procedureLinkId``."
    )

    programCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
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
    )

    servicedDate: fhirtypes.Date = Field(
        None,
        alias="servicedDate",
        title="Date or dates of Service",
        description=(
            "The date or dates when the enclosed suite of services were performed "
            "or completed."
        ),
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
        # Choice of Data Types. i.e serviced[x]
        one_of_many="serviced",
        one_of_many_required=False,
    )

    subSite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subSite",
        title="Service Sub-location",
        description="A region or surface of the site, eg. limb region or tooth surface(s).",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Adjudication category such as co-pay, eligible, benefit, etc.",
        description="Code indicating: Co-Pay, deductable, elegible, benefit, tax, etc.",
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Explanation of Adjudication outcome",
        description="Adjudication reason such as limit reached.",
    )

    value: fhirtypes.Decimal = Field(
        None,
        alias="value",
        title="Non-monitory value",
        description=(
            "A non-monetary value for example a percentage. Mutually exclusive to "
            "the amount element above."
        ),
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Second tier of goods and services.
    """

    resource_type = Field("ExplanationOfBenefitItemDetail", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Detail level adjudication details",
        description="The adjudications results.",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
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
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
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
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    programCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
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
    )

    subDetail: ListType[fhirtypes.ExplanationOfBenefitItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="Additional items",
        description="Third tier of goods and services.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Group or type of product or service",
        description="The type of product or service.",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
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
    )


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional items.
    Third tier of goods and services.
    """

    resource_type = Field("ExplanationOfBenefitItemDetailSubDetail", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Language if different from the resource",
        description="The adjudications results.",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of service or product",
        description=(
            "Health Care Service Type Codes  to identify the classification of "
            "service or benefits."
        ),
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
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes, eg for Oral whether the "
            "treatment is cosmetic or associated with TMJ, or for medical whether "
            "the treatment was outside the clinic or out of office hours."
        ),
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
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of note numbers which apply",
        description="A list of note references to the notes provided below.",
    )
    noteNumber__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    programCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program specific reason for item inclusion",
        description=(
            "For programs which require reson codes for the inclusion, covering, of"
            " this billed item under the program or sub-program."
        ),
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of Products or Services",
        description="The number of repetitions of a service or product.",
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of reveneu or cost center providing the product and/or "
            "service."
        ),
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Service instance",
        description="A service line number.",
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
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of product or service",
        description="The type of product or service.",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="Unique Device Identifier",
        description="List of Unique Device Identifiers associated with this line item.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per point",
        description="The fee for an addittional service or product or charge.",
    )


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of party: Subscriber, Provider, other",
        description="Type of Party to be reimbursed: Subscriber, provider, other.",
    )


class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )

    adjustmentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="adjustmentReason",
        title="Explanation for the non-claim adjustment",
        description="Reason for the payment adjustment.",
    )

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Payable amount after adjustment",
        description="Payable less any payment adjustment.",
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Expected date of Payment",
        description="Estimated payment date.",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier of the payment instrument",
        description="Payment identifer.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Partial or Complete",
        description="Whether this represents partial or complete payment of the claim.",
    )


class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    procedureCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="procedureCodeableConcept",
        title="Patient's list of procedures performed",
        description="The procedure code.",
        # Choice of Data Types. i.e procedure[x]
        one_of_many="procedure",
        one_of_many_required=True,
    )

    procedureReference: fhirtypes.ReferenceType = Field(
        None,
        alias="procedureReference",
        title="Patient's list of procedures performed",
        description="The procedure code.",
        # Choice of Data Types. i.e procedure[x]
        one_of_many="procedure",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Procedure sequence for reference",
        description="Sequence of procedures which serves to order and provide a link.",
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )

    number: fhirtypes.PositiveInt = Field(
        None,
        alias="number",
        title="Sequence number for this note",
        description=(
            "An integer associated with each note which may be referred to from "
            "each service line item."
        ),
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    text: fhirtypes.String = Field(
        None, alias="text", title="Note explanitory text", description="The note text.",
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="display | print | printoper",
        description="The note purpose: Print/Display.",
    )


class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="How the reference claim is related",
        description="For example prior or umbrella.",
    )
