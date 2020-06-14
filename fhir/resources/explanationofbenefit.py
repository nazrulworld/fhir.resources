# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
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
        description="Details of the event",
    )

    addItem: ListType[fhirtypes.ExplanationOfBenefitAddItemType] = Field(
        None,
        alias="addItem",
        title="List of `ExplanationOfBenefitAddItem` items (represented as `dict` in JSON)",
        description="Insurer added line items",
    )

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
        description="Header-level adjudication",
    )

    benefitBalance: ListType[fhirtypes.ExplanationOfBenefitBenefitBalanceType] = Field(
        None,
        alias="benefitBalance",
        title="List of `ExplanationOfBenefitBenefitBalance` items (represented as `dict` in JSON)",
        description="Balance by Benefit Category",
    )

    benefitPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="benefitPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the benefits are applicable",
    )

    billablePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="billablePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Relevant time frame for the claim",
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
        ...,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Response creation date",
    )

    diagnosis: ListType[fhirtypes.ExplanationOfBenefitDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of `ExplanationOfBenefitDiagnosis` items (represented as `dict` in JSON)",
        description="Pertinent diagnosis information",
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Disposition Message",
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title="Type `Reference` referencing `Practitioner, PractitionerRole` (represented as `dict` in JSON)",
        description="Author of the claim",
    )

    facility: fhirtypes.ReferenceType = Field(
        None,
        alias="facility",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Servicing Facility",
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

    fundsReserveRequested: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fundsReserveRequested",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="For whom to reserve funds",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for the resource",
    )

    insurance: ListType[fhirtypes.ExplanationOfBenefitInsuranceType] = Field(
        ...,
        alias="insurance",
        title="List of `ExplanationOfBenefitInsurance` items (represented as `dict` in JSON)",
        description="Patient insurance information",
    )

    insurer: fhirtypes.ReferenceType = Field(
        ...,
        alias="insurer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Party responsible for reimbursement",
    )

    item: ListType[fhirtypes.ExplanationOfBenefitItemType] = Field(
        None,
        alias="item",
        title="List of `ExplanationOfBenefitItem` items (represented as `dict` in JSON)",
        description="Product or service provided",
    )

    originalPrescription: fhirtypes.ReferenceType = Field(
        None,
        alias="originalPrescription",
        title="Type `Reference` referencing `MedicationRequest` (represented as `dict` in JSON)",
        description="Original prescription if superceded by fulfiller",
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

    payee: fhirtypes.ExplanationOfBenefitPayeeType = Field(
        None,
        alias="payee",
        title="Type `ExplanationOfBenefitPayee` (represented as `dict` in JSON)",
        description="Recipient of benefits payable",
    )

    payment: fhirtypes.ExplanationOfBenefitPaymentType = Field(
        None,
        alias="payment",
        title="Type `ExplanationOfBenefitPayment` (represented as `dict` in JSON)",
        description="Payment Details",
    )

    preAuthRef: ListType[fhirtypes.String] = Field(
        None,
        alias="preAuthRef",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Preauthorization reference",
    )

    preAuthRefPeriod: ListType[fhirtypes.PeriodType] = Field(
        None,
        alias="preAuthRefPeriod",
        title="List of `Period` items (represented as `dict` in JSON)",
        description="Preauthorization in-effect period",
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

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Desired processing urgency",
    )

    procedure: ListType[fhirtypes.ExplanationOfBenefitProcedureType] = Field(
        None,
        alias="procedure",
        title="List of `ExplanationOfBenefitProcedure` items (represented as `dict` in JSON)",
        description="Clinical procedures performed",
    )

    processNote: ListType[fhirtypes.ExplanationOfBenefitProcessNoteType] = Field(
        None,
        alias="processNote",
        title="List of `ExplanationOfBenefitProcessNote` items (represented as `dict` in JSON)",
        description="Note concerning adjudication",
    )

    provider: fhirtypes.ReferenceType = Field(
        ...,
        alias="provider",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Party responsible for the claim",
    )

    referral: fhirtypes.ReferenceType = Field(
        None,
        alias="referral",
        title="Type `Reference` referencing `ServiceRequest` (represented as `dict` in JSON)",
        description="Treatment Referral",
    )

    related: ListType[fhirtypes.ExplanationOfBenefitRelatedType] = Field(
        None,
        alias="related",
        title="List of `ExplanationOfBenefitRelated` items (represented as `dict` in JSON)",
        description="Prior or corollary claims",
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

    supportingInfo: ListType[fhirtypes.ExplanationOfBenefitSupportingInfoType] = Field(
        None,
        alias="supportingInfo",
        title="List of `ExplanationOfBenefitSupportingInfo` items (represented as `dict` in JSON)",
        description="Supporting information",
    )

    total: ListType[fhirtypes.ExplanationOfBenefitTotalType] = Field(
        None,
        alias="total",
        title="List of `ExplanationOfBenefitTotal` items (represented as `dict` in JSON)",
        description="Adjudication totals",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Category or discipline",
    )

    use: fhirtypes.Code = Field(
        ...,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="claim | preauthorization | predetermination",
    )


class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """ Details of the event.
    Details of a accident which resulted in injuries which required the
    products and services listed in the claim.
    """

    resource_type = Field("ExplanationOfBenefitAccident", const=True)

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the incident occurred",
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Where the event occurred",
        one_of_many="location",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Where the event occurred",
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
    The first-tier service adjudications for payor added product or service
    lines.
    """

    resource_type = Field("ExplanationOfBenefitAddItem", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
        description="Added items adjudication",
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Anatomical location",
    )

    detail: ListType[fhirtypes.ExplanationOfBenefitAddItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ExplanationOfBenefitAddItemDetail` items (represented as `dict` in JSON)",
        description="Insurer added line items",
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

    subDetailSequence: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="subDetailSequence",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Subdetail sequence number",
    )

    subSite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subSite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Anatomical sub-location",
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


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    The second-tier service adjudications for payor added services.
    """

    resource_type = Field("ExplanationOfBenefitAddItemDetail", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
        description="Added items adjudication",
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

    subDetail: ListType[
        fhirtypes.ExplanationOfBenefitAddItemDetailSubDetailType
    ] = Field(
        None,
        alias="subDetail",
        title="List of `ExplanationOfBenefitAddItemDetailSubDetail` items (represented as `dict` in JSON)",
        description="Insurer added line items",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per item",
    )


class ExplanationOfBenefitAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    The third-tier service adjudications for payor added services.
    """

    resource_type = Field("ExplanationOfBenefitAddItemDetailSubDetail", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
        description="Added items adjudication",
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


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """ Balance by Benefit Category.
    """

    resource_type = Field("ExplanationOfBenefitBenefitBalance", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Benefit classification",
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
        description="Benefit classification",
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
    The members of the team who provided the products and services.
    """

    resource_type = Field("ExplanationOfBenefitCareTeam", const=True)

    provider: fhirtypes.ReferenceType = Field(
        ...,
        alias="provider",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Practitioner or organization",
    )

    qualification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="qualification",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Practitioner credential or specialization",
    )

    responsible: bool = Field(
        None,
        alias="responsible",
        title="Type `bool`",
        description="Indicator of the lead practitioner",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Function within the team",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Order of care team",
    )


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.
    Information about diagnoses relevant to the claim items.
    """

    resource_type = Field("ExplanationOfBenefitDiagnosis", const=True)

    diagnosisCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="diagnosisCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Nature of illness or problem",
        one_of_many="diagnosis",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    diagnosisReference: fhirtypes.ReferenceType = Field(
        None,
        alias="diagnosisReference",
        title="Type `Reference` referencing `Condition` (represented as `dict` in JSON)",
        description="Nature of illness or problem",
        one_of_many="diagnosis",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    onAdmission: fhirtypes.CodeableConceptType = Field(
        None,
        alias="onAdmission",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Present on admission",
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
        description="Diagnosis instance identifier",
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


class ExplanationOfBenefitInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """

    resource_type = Field("ExplanationOfBenefitInsurance", const=True)

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

    preAuthRef: ListType[fhirtypes.String] = Field(
        None,
        alias="preAuthRef",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Prior authorization reference number",
    )


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """ Product or service provided.
    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
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
        description="Anatomical location",
    )

    careTeamSequence: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="careTeamSequence",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable care team members",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Benefit classification",
    )

    detail: ListType[fhirtypes.ExplanationOfBenefitItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ExplanationOfBenefitItemDetail` items (represented as `dict` in JSON)",
        description="Additional items",
    )

    diagnosisSequence: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="diagnosisSequence",
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

    informationSequence: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="informationSequence",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable exception and supporting information",
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
        description="Product or service billing modifiers",
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

    procedureSequence: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="procedureSequence",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable procedures",
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

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of products or services",
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
        description="Item instance identifier",
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

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="List of `Reference` items referencing `Device` (represented as `dict` in JSON)",
        description="Unique device identifier",
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


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
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
        description="Non-monitary value",
    )


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    Second-tier of goods and services.
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
        description="Benefit classification",
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

    programCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Program the product or service is provided under",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of products or services",
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
        description="Product or service provided",
    )

    subDetail: ListType[fhirtypes.ExplanationOfBenefitItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="List of `ExplanationOfBenefitItemDetailSubDetail` items (represented as `dict` in JSON)",
        description="Additional items",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="List of `Reference` items referencing `Device` (represented as `dict` in JSON)",
        description="Unique device identifier",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per item",
    )


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    Third-tier of goods and services.
    """

    resource_type = Field("ExplanationOfBenefitItemDetailSubDetail", const=True)

    adjudication: ListType[fhirtypes.ExplanationOfBenefitItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON)",
        description="Subdetail level adjudication details",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Benefit classification",
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

    programCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Program the product or service is provided under",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of products or services",
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
        description="Product or service provided",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="List of `Reference` items referencing `Device` (represented as `dict` in JSON)",
        description="Unique device identifier",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per item",
    )


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.
    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """

    resource_type = Field("ExplanationOfBenefitPayee", const=True)

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization, Patient, RelatedPerson` (represented as `dict` in JSON)",
        description="Recipient reference",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Category of recipient",
    )


class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """ Payment Details.
    Payment details for the adjudication of the claim.
    """

    resource_type = Field("ExplanationOfBenefitPayment", const=True)

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
        description="Explanation for the variance",
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
        description="Expected date of payment",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Business identifier for the payment",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Partial or complete payment",
    )


class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.
    Procedures performed on the patient relevant to the billing items with the
    claim.
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
        description="Specific clinical procedure",
        one_of_many="procedure",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    procedureReference: fhirtypes.ReferenceType = Field(
        None,
        alias="procedureReference",
        title="Type `Reference` referencing `Procedure` (represented as `dict` in JSON)",
        description="Specific clinical procedure",
        one_of_many="procedure",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Procedure instance identifier",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Category of Procedure",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title="List of `Reference` items referencing `Device` (represented as `dict` in JSON)",
        description="Unique device identifier",
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
    """ Note concerning adjudication.
    A note that describes or explains adjudication results in a human readable
    form.
    """

    resource_type = Field("ExplanationOfBenefitProcessNote", const=True)

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
        None,
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


class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.
    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
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
        description="File or case reference",
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the reference claim is related",
    )


class ExplanationOfBenefitSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """

    resource_type = Field("ExplanationOfBenefitSupportingInfo", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Classification of the supplied information",
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
        description="Explanation for the information",
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
        description="Data to be provided",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`",
        description="Data to be provided",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Data to be provided",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Data to be provided",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Data to be provided",
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
                "valueBoolean",
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


class ExplanationOfBenefitTotal(backboneelement.BackboneElement):
    """ Adjudication totals.
    Categorized monetary totals for the adjudication.
    """

    resource_type = Field("ExplanationOfBenefitTotal", const=True)

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
