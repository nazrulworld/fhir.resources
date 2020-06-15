# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Claim
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    resource_type = Field("Claim", const=True)

    accident: fhirtypes.ClaimAccidentType = Field(
        None,
        alias="accident",
        title="Type `ClaimAccident` (represented as `dict` in JSON)",
        description="Details about an accident",
    )

    billablePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="billablePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period for charge submission",
    )

    careTeam: ListType[fhirtypes.ClaimCareTeamType] = Field(
        None,
        alias="careTeam",
        title="List of `ClaimCareTeam` items (represented as `dict` in JSON)",
        description="Members of the care team",
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

    employmentImpacted: fhirtypes.PeriodType = Field(
        None,
        alias="employmentImpacted",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period unable to work",
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

    fundsReserve: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fundsReserve",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Funds requested to be reserved",
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
        description="Claim number",
    )

    information: ListType[fhirtypes.ClaimInformationType] = Field(
        None,
        alias="information",
        title="List of `ClaimInformation` items (represented as `dict` in JSON)",
        description=(
            "Exceptions, special considerations, the condition, situation, prior or"
            " concurrent issues"
        ),
    )

    insurance: ListType[fhirtypes.ClaimInsuranceType] = Field(
        None,
        alias="insurance",
        title="List of `ClaimInsurance` items (represented as `dict` in JSON)",
        description="Insurance or medical plan",
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Target",
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
        None,
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

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Desired processing priority",
    )

    procedure: ListType[fhirtypes.ClaimProcedureType] = Field(
        None,
        alias="procedure",
        title="List of `ClaimProcedure` items (represented as `dict` in JSON)",
        description="Procedures performed",
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

    related: ListType[fhirtypes.ClaimRelatedType] = Field(
        None,
        alias="related",
        title="List of `ClaimRelated` items (represented as `dict` in JSON)",
        description="Related Claims which may be revelant to processing this claimn",
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

    total: fhirtypes.MoneyType = Field(
        None,
        alias="total",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Total claim cost",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type or discipline",
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="complete | proposed | exploratory | other",
    )


class ClaimAccident(backboneelement.BackboneElement):
    """ Details about an accident.
    An accident which resulted in the need for healthcare services.
    """

    resource_type = Field("ClaimAccident", const=True)

    date: fhirtypes.Date = Field(
        ...,
        alias="date",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the accident occurred see information codes see information codes",
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
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
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


class ClaimCareTeam(backboneelement.BackboneElement):
    """ Members of the care team.
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """

    resource_type = Field("ClaimCareTeam", const=True)

    provider: fhirtypes.ReferenceType = Field(
        ...,
        alias="provider",
        title=(
            "Type `Reference` referencing `Practitioner, Organization` (represented"
            " as `dict` in JSON)"
        ),
        description="Provider individual or organization",
    )

    qualification: fhirtypes.CodeableConceptType = Field(
        None,
        alias="qualification",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type, classification or Specialization",
    )

    responsible: bool = Field(
        None, alias="responsible", title="Type `bool`", description="Billing provider"
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
        description="Number to covey order of careTeam",
    )


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ List of Diagnosis.
    List of patient diagnosis for which care is sought.
    """

    resource_type = Field("ClaimDiagnosis", const=True)

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
        title=(
            "Type `Reference` referencing `Condition` (represented as `dict` in "
            "JSON)"
        ),
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


class ClaimInformation(backboneelement.BackboneElement):
    """ Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """

    resource_type = Field("ClaimInformation", const=True)

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

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
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
        title=(
            "Type `Reference` referencing `Resource` (represented as `dict` in " "JSON)"
        ),
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


class ClaimInsurance(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    Financial instrument by which payment information for health care.
    """

    resource_type = Field("ClaimInsurance", const=True)

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business agreement",
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title=(
            "Type `Reference` referencing `ClaimResponse` (represented as `dict` in"
            " JSON)"
        ),
        description="Adjudication results",
    )

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title=(
            "Type `Reference` referencing `Coverage` (represented as `dict` in " "JSON)"
        ),
        description="Insurance information",
    )

    focal: bool = Field(
        ..., alias="focal", title="Type `bool`", description="Is the focal Coverage"
    )

    preAuthRef: ListType[fhirtypes.String] = Field(
        None,
        alias="preAuthRef",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Pre-Authorization/Determination Reference",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Service instance identifier",
    )


class ClaimItem(backboneelement.BackboneElement):
    """ Goods and Services.
    First tier of goods and services.
    """

    resource_type = Field("ClaimItem", const=True)

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
        description="Applicable careTeam members",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of service or product",
    )

    detail: ListType[fhirtypes.ClaimItemDetailType] = Field(
        None,
        alias="detail",
        title="List of `ClaimItemDetail` items (represented as `dict` in JSON)",
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
        title=(
            "List of `Reference` items referencing `Encounter` (represented as "
            "`dict` in JSON)"
        ),
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
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
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
        title=(
            "List of `Reference` items referencing `Device` (represented as `dict` "
            "in JSON)"
        ),
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


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    Second tier of goods and services.
    """

    resource_type = Field("ClaimItemDetail", const=True)

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

    subDetail: ListType[fhirtypes.ClaimItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title=(
            "List of `ClaimItemDetailSubDetail` items (represented as `dict` in "
            "JSON)"
        ),
        description="Additional items",
    )

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title=(
            "List of `Reference` items referencing `Device` (represented as `dict` "
            "in JSON)"
        ),
        description="Unique Device Identifier",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per point",
    )


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    Third tier of goods and services.
    """

    resource_type = Field("ClaimItemDetailSubDetail", const=True)

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

    udi: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="udi",
        title=(
            "List of `Reference` items referencing `Device` (represented as `dict` "
            "in JSON)"
        ),
        description="Unique Device Identifier",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per point",
    )


class ClaimPayee(backboneelement.BackboneElement):
    """ Party to be paid any benefits payable.
    The party to be reimbursed for the services.
    """

    resource_type = Field("ClaimPayee", const=True)

    party: fhirtypes.ReferenceType = Field(
        None,
        alias="party",
        title=(
            "Type `Reference` referencing `Practitioner, Organization, Patient, "
            "RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Party to receive the payable",
    )

    resourceType: fhirtypes.CodingType = Field(
        None,
        alias="resourceType",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="organization | patient | practitioner | relatedperson",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of party: Subscriber, Provider, other",
    )


class ClaimProcedure(backboneelement.BackboneElement):
    """ Procedures performed.
    Ordered list of patient procedures performed to support the adjudication.
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
        description="Patient\u0027s list of procedures performed",
        one_of_many="procedure",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    procedureReference: fhirtypes.ReferenceType = Field(
        None,
        alias="procedureReference",
        title=(
            "Type `Reference` referencing `Procedure` (represented as `dict` in "
            "JSON)"
        ),
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


class ClaimRelated(backboneelement.BackboneElement):
    """ Related Claims which may be revelant to processing this claimn.
    Other claims which are related to this claim such as prior claim versions
    or for related services.
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
        description="Related file or case reference",
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the reference claim is related",
    )
