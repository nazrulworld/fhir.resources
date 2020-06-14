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

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ExplanationOfBenefit(domainresource.DomainResource):
    """ Explanation of Benefit resource.
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    resource_type = Field("ExplanationOfBenefit", const=True)

    accident: fhirtypes.ExplanationOfBenefitAccidentType = Field(
        None,
        alias="accident",
        title="Type `ExplanationOfBenefitAccident` (represented as `dict` in JSON)",
        description="Details of an accident",
    )

    addItem: ListType[fhirtypes.ExplanationOfBenefitAddItemType] = Field(
        None,
        alias="addItem",
        title="List of `ExplanationOfBenefitAddItem` items (represented as `dict` in JSON)",
        description="Insurer added line items",
    )

    benefitBalance: ListType[fhirtypes.ExplanationOfBenefitBenefitBalanceType] = Field(
        None,
        alias="benefitBalance",
        title="List of `ExplanationOfBenefitBenefitBalance` items (represented as `dict` in JSON)",
        description="Balance by Benefit Category",
    )

    billablePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="billablePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period for charge submission",
    )

    careTeam: ListType[fhirtypes.ExplanationOfBenefitCareTeamType] = Field(
        None,
        alias="careTeam",
        title="List of `ExplanationOfBenefitCareTeam` items (represented as `dict` in JSON)",
        description="Care Team members",
    )

    claim: fhirtypes.ReferenceType = Field(
        None,
        alias="claim",
        title="Type `Reference` referencing `Claim` (represented as `dict` in JSON)",
        description="Claim reference",
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title="Type `Reference` referencing `ClaimResponse` (represented as `dict` in JSON)",
        description="Claim response reference",
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
    )

    diagnosis: ListType[fhirtypes.ExplanationOfBenefitDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of `ExplanationOfBenefitDiagnosis` items (represented as `dict` in JSON)",
        description="List of Diagnosis",
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Disposition Message",
    )

    employmentImpacted: fhirtypes.PeriodType = Field(
        None,
        alias="employmentImpacted",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period unable to work",
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON)",
        description="Author",
    )

    facility: fhirtypes.ReferenceType = Field(
        None,
        alias="facility",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Servicing Facility",
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Printed Form Identifier",
    )

    hospitalization: fhirtypes.PeriodType = Field(
        None,
        alias="hospitalization",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period in hospital",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier",
    )

    information: ListType[fhirtypes.ExplanationOfBenefitInformationType] = Field(
        None,
        alias="information",
        title="List of `ExplanationOfBenefitInformation` items (represented as `dict` in JSON)",
        description="Exceptions, special considerations, the condition, situation, prior or concurrent issues",
    )

    insurance: fhirtypes.ExplanationOfBenefitInsuranceType = Field(
        None,
        alias="insurance",
        title="Type `ExplanationOfBenefitInsurance` (represented as `dict` in JSON)",
        description="Insurance or medical plan",
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Insurer responsible for the EOB",
    )

    item: ListType[fhirtypes.ExplanationOfBenefitItemType] = Field(
        None,
        alias="item",
        title="List of `ExplanationOfBenefitItem` items (represented as `dict` in JSON)",
        description="Goods and Services",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Responsible organization for the claim",
    )

    originalPrescription: fhirtypes.ReferenceType = Field(
        None,
        alias="originalPrescription",
        title="Type `Reference` referencing `MedicationRequest` (represented as `dict` in JSON)",
        description="Original prescription if superceded by fulfiller",
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

    payee: fhirtypes.ExplanationOfBenefitPayeeType = Field(
        None,
        alias="payee",
        title="Type `ExplanationOfBenefitPayee` (represented as `dict` in JSON)",
        description="Party to be paid any benefits payable",
    )

    payment: fhirtypes.ExplanationOfBenefitPaymentType = Field(
        None,
        alias="payment",
        title="Type `ExplanationOfBenefitPayment` (represented as `dict` in JSON)",
        description="Payment (if paid)",
    )

    precedence: fhirtypes.PositiveInt = Field(
        None,
        alias="precedence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Precedence (primary, secondary, etc.)",
    )

    prescription: fhirtypes.ReferenceType = Field(
        None,
        alias="prescription",
        title="Type `Reference` referencing `MedicationRequest, VisionPrescription` (represented as `dict` in JSON)",
        description="Prescription authorizing services or products",
    )

    procedure: ListType[fhirtypes.ExplanationOfBenefitProcedureType] = Field(
        None,
        alias="procedure",
        title="List of `ExplanationOfBenefitProcedure` items (represented as `dict` in JSON)",
        description="Procedures performed",
    )

    processNote: ListType[fhirtypes.ExplanationOfBenefitProcessNoteType] = Field(
        None,
        alias="processNote",
        title="List of `ExplanationOfBenefitProcessNote` items (represented as `dict` in JSON)",
        description="Processing notes",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON)",
        description="Responsible provider for the claim",
    )

    referral: fhirtypes.ReferenceType = Field(
        None,
        alias="referral",
        title="Type `Reference` referencing `ReferralRequest` (represented as `dict` in JSON)",
        description="Treatment Referral",
    )

    related: ListType[fhirtypes.ExplanationOfBenefitRelatedType] = Field(
        None,
        alias="related",
        title="List of `ExplanationOfBenefitRelated` items (represented as `dict` in JSON)",
        description="Related Claims which may be revelant to processing this claim",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )

    subType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Finer grained claim type information",
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

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type or discipline",
    )

    unallocDeductable: fhirtypes.MoneyType = Field(
        None,
        alias="unallocDeductable",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Unallocated deductable",
    )


class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """ Details of an accident.
    An accident which resulted in the need for healthcare services.
    """

    resource_type = Field("ExplanationOfBenefitAccident", const=True)

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the accident occurred",
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Accident Place",
        one_of_many="location",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Accident Place",
        one_of_many="location",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The nature of the accident",
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
            "location": ["locationAddress", "locationReference",],
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


class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    The first tier service adjudications for payor added services.
    """

    resource_type = Field("ExplanationOfBenefitAddItem", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
        description="Added items adjudication",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of service or product",
    )

    detail: ListType[fhirtypes.ExplanationOfBenefitAddItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ExplanationOfBenefitAddItemDetail` items (represented as `dict` in JSON)",
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
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="List of note numbers which apply",
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Revenue or cost center code",
    )

    sequenceLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="sequenceLinkId",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Service instances",
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing Code",
    )


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """ Added items details.
    The second tier service adjudications for payor added services.
    """

    resource_type = Field("ExplanationOfBenefitAddItemDetail", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
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
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="List of note numbers which apply",
    )

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
        description="Billing Code",
    )


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """ Balance by Benefit Category.
    """

    resource_type = Field("ExplanationOfBenefitBenefitBalance", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of services covered",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of the benefit or services covered",
    )

    excluded: bool = Field(
        None,
        alias="excluded",
        title="Type `bool`",
        description="Excluded from the plan",
    )

    financial: ListType[
        fhirtypes.ExplanationOfBenefitBenefitBalanceFinancialType
    ] = Field(
        None,
        alias="financial",
        title="List of `ExplanationOfBenefitBenefitBalanceFinancial` items (represented as `dict` in JSON)",
        description="Benefit Summary",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Short name for the benefit",
    )

    network: fhirtypes.CodeableConceptType = Field(
        None,
        alias="network",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="In or out of network",
    )

    subCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subCategory",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Detailed services covered within the type",
    )

    term: fhirtypes.CodeableConceptType = Field(
        None,
        alias="term",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Annual or lifetime",
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Individual or family",
    )


class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.
    Benefits Used to date.
    """

    resource_type = Field("ExplanationOfBenefitBenefitBalanceFinancial", const=True)

    allowedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="allowedMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Benefits allowed",
        one_of_many="allowed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    allowedString: fhirtypes.String = Field(
        None,
        alias="allowedString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Benefits allowed",
        one_of_many="allowed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    allowedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="allowedUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Benefits allowed",
        one_of_many="allowed",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Deductable, visits, benefit amount",
    )

    usedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="usedMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Benefits used",
        one_of_many="used",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    usedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="usedUnsignedInt",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Benefits used",
        one_of_many="used",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
            "allowed": ["allowedMoney", "allowedString", "allowedUnsignedInt",],
            "used": ["usedMoney", "usedUnsignedInt",],
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
    """ Care Team members.
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """

    resource_type = Field("ExplanationOfBenefitCareTeam", const=True)

    provider: fhirtypes.ReferenceType = Field(
        ...,
        alias="provider",
        title="Type `Reference` referencing `Practitioner, Organization` (represented as `dict` in JSON)",
        description="Member of the Care Team",
    )

    qualification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="qualification",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type, classification or Specialization",
    )

    responsible: bool = Field(
        None,
        alias="responsible",
        title="Type `bool`",
        description="Billing practitioner",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Role on the team",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Number to covey order of careteam",
    )


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """ List of Diagnosis.
    Ordered list of patient diagnosis for which care is sought.
    """

    resource_type = Field("ExplanationOfBenefitDiagnosis", const=True)

    diagnosisCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="diagnosisCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Patient\u0027s diagnosis",
        one_of_many="diagnosis",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    diagnosisReference: fhirtypes.ReferenceType = Field(
        None,
        alias="diagnosisReference",
        title="Type `Reference` referencing `Condition` (represented as `dict` in JSON)",
        description="Patient\u0027s diagnosis",
        one_of_many="diagnosis",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    packageCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="packageCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Package billing code",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Number to covey order of diagnosis",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Timing or nature of the diagnosis",
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
            "diagnosis": ["diagnosisCodeableConcept", "diagnosisReference",],
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
    """ Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """

    resource_type = Field("ExplanationOfBenefitInformation", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="General class of information",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of information",
    )

    reason: fhirtypes.CodingType = Field(
        None,
        alias="reason",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Reason associated with the information",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Information instance identifier",
    )

    timingDate: fhirtypes.Date = Field(
        None,
        alias="timingDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When it occurred",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When it occurred",
        one_of_many="timing",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Additional Data or supporting information",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Additional Data or supporting information",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Additional Data or supporting information",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional Data or supporting information",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
            "timing": ["timingDate", "timingPeriod",],
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
    """ Insurance or medical plan.
    Financial instrument by which payment information for health care.
    """

    resource_type = Field("ExplanationOfBenefitInsurance", const=True)

    coverage: fhirtypes.ReferenceType = Field(
        None,
        alias="coverage",
        title="Type `Reference` referencing `Coverage` (represented as `dict` in JSON)",
        description="Insurance information",
    )

    preAuthRef: ListType[fhirtypes.String] = Field(
        None,
        alias="preAuthRef",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pre-Authorization/Determination Reference",
    )


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """ Goods and Services.
    First tier of goods and services.
    """

    resource_type = Field("ExplanationOfBenefitItem", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
        description="Adjudication details",
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Service Location",
    )

    careTeamLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="careTeamLinkId",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable careteam members",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of service or product",
    )

    detail: ListType[fhirtypes.ExplanationOfBenefitItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ExplanationOfBenefitItemDetail` items (represented as `dict` in JSON)",
        description="Additional items",
    )

    diagnosisLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="diagnosisLinkId",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable diagnoses",
    )

    encounter: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="encounter",
        title="List of `Reference` items referencing `Encounter` (represented as `dict` in JSON)",
        description="Encounters related to this billed item",
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Price scaling factor",
    )

    informationLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="informationLinkId",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable exception and supporting information",
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Place of service",
        one_of_many="location",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    locationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="locationCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Place of service",
        one_of_many="location",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Place of service",
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
        description="List of note numbers which apply",
    )

    procedureLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="procedureLinkId",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable procedures",
    )

    programCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Program specific reason for item inclusion",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of Products or Services",
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Revenue or cost center code",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Service instance",
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing Code",
    )

    servicedDate: fhirtypes.Date = Field(
        None,
        alias="servicedDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Date or dates of Service",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    servicedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Date or dates of Service",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    subSite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subSite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Service Sub-location",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="List of `Reference` items referencing `Device` (represented as `dict` in JSON)",
        description="Unique Device Identifier",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per point",
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


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    The adjudications results.
    """

    resource_type = Field("ExplanationOfBenefitItemAdjudication", const=True)

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
        None,
        alias="value",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Non-monitory value",
    )


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    Second tier of goods and services.
    """

    resource_type = Field("ExplanationOfBenefitItemDetail", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
        description="Detail level adjudication details",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of service or product",
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
        description="Total additional item cost",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="List of note numbers which apply",
    )

    programCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Program specific reason for item inclusion",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of Products or Services",
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Revenue or cost center code",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Service instance",
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing Code",
    )

    subDetail: ListType[fhirtypes.ExplanationOfBenefitItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="List of `ExplanationOfBenefitItemDetailSubDetail` items (represented as `dict` in JSON)",
        description="Additional items",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Group or type of product or service",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="List of `Reference` items referencing `Device` (represented as `dict` in JSON)",
        description="Unique Device Identifier",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per point",
    )


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    Third tier of goods and services.
    """

    resource_type = Field("ExplanationOfBenefitItemDetailSubDetail", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
        description="Language if different from the resource",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of service or product",
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
        description="Net additional item cost",
    )

    noteNumber: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="noteNumber",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="List of note numbers which apply",
    )

    programCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Program specific reason for item inclusion",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of Products or Services",
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Revenue or cost center code",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Service instance",
    )

    service: fhirtypes.CodeableConceptType = Field(
        None,
        alias="service",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing Code",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of product or service",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="List of `Reference` items referencing `Device` (represented as `dict` in JSON)",
        description="Unique Device Identifier",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per point",
    )


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """ Party to be paid any benefits payable.
    The party to be reimbursed for the services.
    """

    resource_type = Field("ExplanationOfBenefitPayee", const=True)

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title="Type `Reference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON)",
        description="Party to receive the payable",
    )

    resourceType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="resourceType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="organization | patient | practitioner | relatedperson",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of party: Subscriber, Provider, other",
    )


class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """ Payment (if paid).
    Payment details for the claim if the claim has been paid.
    """

    resource_type = Field("ExplanationOfBenefitPayment", const=True)

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
        None,
        alias="date",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Expected date of Payment",
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


class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """ Procedures performed.
    Ordered list of patient procedures performed to support the adjudication.
    """

    resource_type = Field("ExplanationOfBenefitProcedure", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the procedure was performed",
    )

    procedureCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="procedureCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Patient\u0027s list of procedures performed",
        one_of_many="procedure",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    procedureReference: fhirtypes.ReferenceType = Field(
        None,
        alias="procedureReference",
        title="Type `Reference` referencing `Procedure` (represented as `dict` in JSON)",
        description="Patient\u0027s list of procedures performed",
        one_of_many="procedure",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Procedure sequence for reference",
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
            "procedure": ["procedureCodeableConcept", "procedureReference",],
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
    """ Processing notes.
    Note text.
    """

    resource_type = Field("ExplanationOfBenefitProcessNote", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Language if different from the resource",
    )

    number: fhirtypes.PositiveInt = Field(
        None,
        alias="number",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Sequence number for this note",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Note explanitory text",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="display | print | printoper",
    )


class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """ Related Claims which may be revelant to processing this claim.
    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """

    resource_type = Field("ExplanationOfBenefitRelated", const=True)

    claim: fhirtypes.ReferenceType = Field(
        None,
        alias="claim",
        title="Type `Reference` referencing `Claim` (represented as `dict` in JSON)",
        description="Reference to the related claim",
    )

    reference: fhirtypes.IdentifierType = Field(
        None,
        alias="reference",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Related file or case reference",
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the reference claim is related",
    )
