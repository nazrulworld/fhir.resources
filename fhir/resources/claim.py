# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """

    resource_type = Field("Claim", const=True)

    accident: fhirtypes.ClaimAccidentType = Field(
        None,
        alias="accident",
        title="Type `ClaimAccident` (represented as `dict` in JSON)",
        description="Details of the event",
    )

    billablePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="billablePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Relevant time frame for the claim",
    )

    careTeam: ListType[fhirtypes.ClaimCareTeamType] = Field(
        None,
        alias="careTeam",
        title="List of `ClaimCareTeam` items (represented as `dict` in JSON)",
        description="Members of the care team",
    )

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Resource creation date",
    )

    diagnosis: ListType[fhirtypes.ClaimDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of `ClaimDiagnosis` items (represented as `dict` in JSON)",
        description="Pertinent diagnosis information",
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
        description="Servicing facility",
    )

    fundsReserve: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fundsReserve",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="For whom to reserve funds",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for claim",
    )

    insurance: ListType[fhirtypes.ClaimInsuranceType] = Field(
        ...,
        alias="insurance",
        title="List of `ClaimInsurance` items (represented as `dict` in JSON)",
        description="Patient insurance information",
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Target",
    )

    item: ListType[fhirtypes.ClaimItemType] = Field(
        None,
        alias="item",
        title="List of `ClaimItem` items (represented as `dict` in JSON)",
        description="Product or service provided",
    )

    originalPrescription: fhirtypes.ReferenceType = Field(
        None,
        alias="originalPrescription",
        title="Type `Reference` referencing `DeviceRequest, MedicationRequest, VisionPrescription` (represented as `dict` in JSON)",
        description="Original prescription if superseded by fulfiller",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The recipient of the products and services",
    )

    payee: fhirtypes.ClaimPayeeType = Field(
        None,
        alias="payee",
        title="Type `ClaimPayee` (represented as `dict` in JSON)",
        description="Recipient of benefits payable",
    )

    prescription: fhirtypes.ReferenceType = Field(
        None,
        alias="prescription",
        title="Type `Reference` referencing `DeviceRequest, MedicationRequest, VisionPrescription` (represented as `dict` in JSON)",
        description="Prescription authorizing services and products",
    )

    priority: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Desired processing ugency",
    )

    procedure: ListType[fhirtypes.ClaimProcedureType] = Field(
        None,
        alias="procedure",
        title="List of `ClaimProcedure` items (represented as `dict` in JSON)",
        description="Clinical procedures performed",
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
        description="Treatment referral",
    )

    related: ListType[fhirtypes.ClaimRelatedType] = Field(
        None,
        alias="related",
        title="List of `ClaimRelated` items (represented as `dict` in JSON)",
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

    supportingInfo: ListType[fhirtypes.ClaimSupportingInfoType] = Field(
        None,
        alias="supportingInfo",
        title="List of `ClaimSupportingInfo` items (represented as `dict` in JSON)",
        description="Supporting information",
    )

    total: fhirtypes.MoneyType = Field(
        None,
        alias="total",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total claim cost",
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


class ClaimAccident(backboneelement.BackboneElement):
    """ Details of the event.
    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """

    resource_type = Field("ClaimAccident", const=True)

    date: fhirtypes.Date = Field(
        ...,
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


class ClaimCareTeam(backboneelement.BackboneElement):
    """ Members of the care team.
    The members of the team who provided the products and services.
    """

    resource_type = Field("ClaimCareTeam", const=True)

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


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.
    Information about diagnoses relevant to the claim items.
    """

    resource_type = Field("ClaimDiagnosis", const=True)

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


class ClaimInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """

    resource_type = Field("ClaimInsurance", const=True)

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional provider contract number",
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title="Type `Reference` referencing `ClaimResponse` (represented as `dict` in JSON)",
        description="Adjudication results",
    )

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

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Pre-assigned Claim number",
    )

    preAuthRef: ListType[fhirtypes.String] = Field(
        None,
        alias="preAuthRef",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Prior authorization reference number",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Insurance instance identifier",
    )


class ClaimItem(backboneelement.BackboneElement):
    """ Product or service provided.
    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """

    resource_type = Field("ClaimItem", const=True)

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
        description="Applicable careTeam members",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Benefit classification",
    )

    detail: ListType[fhirtypes.ClaimItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ClaimItemDetail` items (represented as `dict` in JSON)",
        description="Product or service provided",
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


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Product or service provided.
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """

    resource_type = Field("ClaimItemDetail", const=True)

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

    subDetail: ListType[fhirtypes.ClaimItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON)",
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


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Product or service provided.
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """

    resource_type = Field("ClaimItemDetailSubDetail", const=True)

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


class ClaimPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.
    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """

    resource_type = Field("ClaimPayee", const=True)

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization, Patient, RelatedPerson` (represented as `dict` in JSON)",
        description="Recipient reference",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Category of recipient",
    )


class ClaimProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.
    Procedures performed on the patient relevant to the billing items with the
    claim.
    """

    resource_type = Field("ClaimProcedure", const=True)

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


class ClaimRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.
    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """

    resource_type = Field("ClaimRelated", const=True)

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


class ClaimSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """

    resource_type = Field("ClaimSupportingInfo", const=True)

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

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
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
