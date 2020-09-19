# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Claim(DomainResource):
    """Claim, Pre-determination or Pre-authorization.

    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    resource_type = Field("Claim", const=True)

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Type",
    )

    accident: fhirtypes.Date = Field(
        None,
        alias="accident",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Accident Date",
    )
    accidentType: fhirtypes.CodingType = Field(
        None,
        alias="accidentType",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Accident Date",
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
    )

    diagnosis: ListType[fhirtypes.ClaimDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of `ClaimDiagnosis` items (represented as `dict` in JSON)",
        description="List of Diagnosis",
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Author",
    )

    facility: fhirtypes.ReferenceType = Field(
        None,
        alias="facility",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Servicing Facility",
    )

    fundsReserve: fhirtypes.CodingType = Field(
        None,
        alias="fundsReserve",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Funds requested to be reserved",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Claim number",
    )

    item: ListType[fhirtypes.ClaimItemType] = Field(
        None,
        alias="item",
        title="List of `ClaimItem` items (represented as `dict` in JSON)",
        description="Goods and Services",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible organization",
    )

    originalPrescription: fhirtypes.ReferenceType = Field(
        None,
        alias="originalPrescription",
        title=(
            "Type `Reference` referencing `MedicationRequest` (represented as "
            "`dict` in JSON)"
        ),
        description="Original prescription if superceded by fulfiller",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The subject of the Products and Services",
    )

    payee: fhirtypes.ClaimPayeeType = Field(
        None,
        alias="payee",
        title="Type `ClaimPayee` (represented as `dict` in JSON)",
        description="Party to be paid any benefits payable",
    )

    prescription: fhirtypes.ReferenceType = Field(
        None,
        alias="prescription",
        title=(
            "Type `Reference` referencing `MedicationRequest, VisionPrescription` "
            "(represented as `dict` in JSON)"
        ),
        description="Prescription authorizing services or products",
    )

    priority: fhirtypes.CodingType = Field(
        None,
        alias="priority",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Desired processing priority",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="Responsible provider",
    )

    referral: fhirtypes.ReferenceType = Field(
        None,
        alias="referral",
        title=(
            "Type `Reference` referencing `ReferralRequest` (represented as `dict` "
            "in JSON)"
        ),
        description="Treatment Referral",
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="complete | proposed | exploratory | other",
    )
    additionalMaterials: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="additionalMaterials",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Additional materials, documents, etc..",
    )

    condition: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="condition",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="List of presenting Conditions.",
    )
    coverage: ListType[fhirtypes.ClaimCoverageType] = Field(
        None,
        alias="coverage",
        title="List of `ClaimCoverage` items (represented as `dict` in JSON).",
        description="Insurance or medical plan.",
    )

    exception: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="exception",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Eligibility exceptions.",
    )

    interventionException: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="interventionException",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Intervention and exception code (Pharma).",
    )

    missingTeeth: ListType[fhirtypes.ClaimMissingTeethType] = Field(
        None,
        alias="missingTeeth",
        title="List of `ClaimMissingTeeth` items (represented as `dict` in JSON).",
        description="Only if type = oral.",
    )

    originalRuleset: fhirtypes.CodingType = Field(
        None,
        alias="originalRuleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Original specification followed.",
    )

    ruleset: fhirtypes.CodingType = Field(
        None,
        alias="ruleset",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Current specification followed.",
    )

    school: fhirtypes.String = Field(
        None, alias="school", title="Type `str`.", description="Name of School."
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Insurer.",
    )


class ClaimCoverage(BackboneElement):
    """Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """

    resource_type = Field("ClaimCoverage", const=True)

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
        title="Type `Reference` referencing `Coverage` (represented as `dict` in JSON).",
        description="Insurance information.",
    )

    focal: fhirtypes.Boolean = Field(
        None, alias="focal", title="Type `bool`.", description="The focal Coverage."
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
        ...,
        alias="sequence",
        title="Type `int`.",
        description="Service instance identifier.",
    )


class ClaimDiagnosis(BackboneElement):
    """Diagnosis.

    Ordered list of patient diagnosis for which care is sought.
    """

    resource_type = Field("ClaimDiagnosis", const=True)

    diagnosis: fhirtypes.CodingType = Field(
        ...,
        alias="diagnosis",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Patient's list of diagnosis.",
    )
    sequence: fhirtypes.PositiveInt = Field(
        ..., alias="sequence", title="Type `int`.", description="Sequence of diagnosis."
    )


class ClaimItem(BackboneElement):
    """Goods and Services.

    First tier of goods and services.
    """

    resource_type = "ClaimItem"

    bodySite: fhirtypes.CodingType = Field(
        None,
        alias="bodySite",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Service Location.",
    )

    detail: ListType[fhirtypes.ClaimItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ClaimItemDetail` items (represented as `dict` in JSON).",
        description="Additional items.",
    )

    diagnosisLinkId: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="diagnosisLinkId",
        title="List of `int` items.",
        description="Diagnosis Link.",
    )

    factor: fhirtypes.Decimal = Field(
        None, alias="factor", title="Type `float`.", description="Price scaling factor."
    )

    modifier: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="modifier",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Service/Product billing modifiers.",
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Total item cost.",
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Type `float`.",
        description="Difficulty scaling factor.",
    )

    prosthesis: fhirtypes.ClaimItemProsthesisType = Field(
        None,
        alias="prosthesis",
        title="Type `ClaimItemProsthesis` (represented as `dict` in JSON).",
        description="Prosthetic details.",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON).",
        description="Responsible practitioner.",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON).",
        description="Count of Products or Services.",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ..., alias="sequence", title="type `int`.", description="Service instance."
    )

    service: fhirtypes.CodingType = Field(
        None,
        alias="service",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Item Code.",
    )

    serviceDate: fhirtypes.Date = Field(
        None,
        alias="serviceDate",
        title="Type `Date` (represented as `str` in JSON).",
        description="Date of Service.",
    )

    subSite: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="subSite",
        title="List of `Coding` items (represented as `dict` in JSON).",
        description="Service Sub-location.",
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Group or type of product or service.",
    )

    udi: fhirtypes.CodingType = Field(
        None,
        alias="udi",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Unique Device Identifier.",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Fee, charge or cost per point.",
    )


class ClaimItemDetail(BackboneElement):
    """Additional items.

    Second tier of goods and services.
    """

    resource_type = Field("ClaimItemDetail", const=True)

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Group or type of product or service.",
    )

    udi: fhirtypes.CodingType = Field(
        None,
        alias="udi",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Unique Device Identifier.",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Fee, charge or cost per point.",
    )
    sequence: fhirtypes.PositiveInt = Field(
        ..., alias="sequence", title="type `int`.", description="Service instance."
    )

    service: fhirtypes.CodingType = Field(
        None,
        alias="service",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Item Code.",
    )
    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON).",
        description="Count of Products or Services.",
    )
    factor: fhirtypes.Decimal = Field(
        None, alias="factor", title="Type `float`.", description="Price scaling factor."
    )
    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Total item cost.",
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Type `float`.",
        description="Difficulty scaling factor.",
    )

    subDetail: ListType[fhirtypes.ClaimItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON).",
        description="Additional items.",
    )


class ClaimItemDetailSubDetail(BackboneElement):
    """Additional items.

    Third tier of goods and services.
    """

    resource_type = Field("ClaimItemDetailSubDetail", const=True)

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Group or type of product or service.",
    )
    udi: fhirtypes.CodingType = Field(
        None,
        alias="udi",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Unique Device Identifier.",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Fee, charge or cost per point.",
    )
    sequence: fhirtypes.PositiveInt = Field(
        ..., alias="sequence", title="type `int`.", description="Service instance."
    )

    service: fhirtypes.CodingType = Field(
        None,
        alias="service",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Item Code.",
    )
    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON).",
        description="Count of Products or Services.",
    )
    factor: fhirtypes.Decimal = Field(
        None, alias="factor", title="Type `float`.", description="Price scaling factor."
    )
    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Type `Quantity` referencing `Money` (represented as `dict` in JSON).",
        description="Total item cost.",
    )

    points: fhirtypes.Decimal = Field(
        None,
        alias="points",
        title="Type `float`.",
        description="Difficulty scaling factor.",
    )


class ClaimItemProsthesis(BackboneElement):
    """Prosthetic details.

    The materials and placement date of prior fixed prosthesis.
    """

    resource_type = Field("ClaimItemProsthesis", const=True)

    initial: fhirtypes.Boolean = Field(
        None,
        alias="initial",
        title="Type `bool`.",
        description="Is this the initial service.",
    )

    priorDate: fhirtypes.Date = Field(
        None,
        alias="priorDate",
        title="Type `Date` (represented as `str` in JSON).",
        description="Initial service Date.",
    )

    priorMaterial: fhirtypes.CodingType = Field(
        None,
        alias="priorMaterial",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Prosthetic Material.",
    )


class ClaimMissingTeeth(BackboneElement):
    """Only if type = oral.

    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """

    resource_type = Field("ClaimMissingTeeth", const=True)

    extractionDate: fhirtypes.Date = Field(
        None,
        alias="extractionDate",
        title="Type `Date` (represented as `str` in JSON).",
        description="Date of Extraction.",
    )

    reason: fhirtypes.CodingType = Field(
        None,
        alias="reason",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Reason for missing.",
    )

    tooth: fhirtypes.CodingType = Field(
        None,
        alias="tooth",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Tooth Code.",
    )


class ClaimPayee(BackboneElement):
    """Payee.

    The party to be reimbursed for the services.
    """

    resource_type = Field("ClaimPayee", const=True)

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Organization who is the payee.",
    )

    person: fhirtypes.ReferenceType = Field(
        None,
        alias="person",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Other person who is the payee.",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON).",
        description="Provider who is the payee.",
    )

    type: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Party to be paid any benefits payable.",
    )
