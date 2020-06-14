# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class CoverageEligibilityRequest(domainresource.DomainResource):
    """ CoverageEligibilityRequest resource.
    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """

    resource_type = Field("CoverageEligibilityRequest", const=True)

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Creation date",
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title="Type `Reference` referencing `Practitioner, PractitionerRole` (represented as `dict` in JSON)",
        description="Author",
    )

    facility: fhirtypes.ReferenceType = Field(
        None,
        alias="facility",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Servicing facility",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for coverage eligiblity request",
    )

    insurance: ListType[fhirtypes.CoverageEligibilityRequestInsuranceType] = Field(
        None,
        alias="insurance",
        title="List of `CoverageEligibilityRequestInsurance` items (represented as `dict` in JSON)",
        description="Patient insurance information",
    )

    insurer: fhirtypes.ReferenceType = Field(
        ...,
        alias="insurer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Coverage issuer",
    )

    item: ListType[fhirtypes.CoverageEligibilityRequestItemType] = Field(
        None,
        alias="item",
        title="List of `CoverageEligibilityRequestItem` items (represented as `dict` in JSON)",
        description="Item to be evaluated for eligibiity",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Intended recipient of products and services",
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Desired processing priority",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization` (represented as `dict` in JSON)",
        description="Party responsible for the request",
    )

    purpose: ListType[fhirtypes.Code] = Field(
        ...,
        alias="purpose",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="auth-requirements | benefits | discovery | validation",
    )

    servicedDate: fhirtypes.Date = Field(
        None,
        alias="servicedDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Estimated date or dates of service",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    servicedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicedPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Estimated date or dates of service",
        one_of_many="serviced",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )

    supportingInfo: ListType[
        fhirtypes.CoverageEligibilityRequestSupportingInfoType
    ] = Field(
        None,
        alias="supportingInfo",
        title="List of `CoverageEligibilityRequestSupportingInfo` items (represented as `dict` in JSON)",
        description="Supporting information",
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


class CoverageEligibilityRequestInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services.
    """

    resource_type = Field("CoverageEligibilityRequestInsurance", const=True)

    businessArrangement: fhirtypes.String = Field(
        None,
        alias="businessArrangement",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional provider contract number",
    )

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title="Type `Reference` referencing `Coverage` (represented as `dict` in JSON)",
        description="Insurance information",
    )

    focal: bool = Field(
        None, alias="focal", title="Type `bool`", description="Applicable coverage",
    )


class CoverageEligibilityRequestItem(backboneelement.BackboneElement):
    """ Item to be evaluated for eligibiity.
    Service categories or billable services for which benefit details and/or an
    authorization prior to service delivery may be required by the payor.
    """

    resource_type = Field("CoverageEligibilityRequestItem", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Benefit classification",
    )

    detail: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="detail",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Product or service details",
    )

    diagnosis: ListType[fhirtypes.CoverageEligibilityRequestItemDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of `CoverageEligibilityRequestItemDiagnosis` items (represented as `dict` in JSON)",
        description="Applicable diagnosis",
    )

    facility: fhirtypes.ReferenceType = Field(
        None,
        alias="facility",
        title="Type `Reference` referencing `Location, Organization` (represented as `dict` in JSON)",
        description="Servicing facility",
    )

    modifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Product or service billing modifiers",
    )

    productOrService: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productOrService",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing, service, product, or drug code",
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Type `Reference` referencing `Practitioner, PractitionerRole` (represented as `dict` in JSON)",
        description="Perfoming practitioner",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Count of products or services",
    )

    supportingInfoSequence: ListType[fhirtypes.PositiveInt] = Field(
        None,
        alias="supportingInfoSequence",
        title="List of `PositiveInt` items (represented as `dict` in JSON)",
        description="Applicable exception or supporting information",
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Fee, charge or cost per item",
    )


class CoverageEligibilityRequestItemDiagnosis(backboneelement.BackboneElement):
    """ Applicable diagnosis.
    Patient diagnosis for which care is sought.
    """

    resource_type = Field("CoverageEligibilityRequestItemDiagnosis", const=True)

    diagnosisCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="diagnosisCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Nature of illness or problem",
        one_of_many="diagnosis",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    diagnosisReference: fhirtypes.ReferenceType = Field(
        None,
        alias="diagnosisReference",
        title="Type `Reference` referencing `Condition` (represented as `dict` in JSON)",
        description="Nature of illness or problem",
        one_of_many="diagnosis",  # Choice of Data Types. i.e value[x]
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


class CoverageEligibilityRequestSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """

    resource_type = Field("CoverageEligibilityRequestSupportingInfo", const=True)

    appliesToAll: bool = Field(
        None,
        alias="appliesToAll",
        title="Type `bool`",
        description="Applies to all items",
    )

    information: fhirtypes.ReferenceType = Field(
        ...,
        alias="information",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Data to be provided",
    )

    sequence: fhirtypes.PositiveInt = Field(
        ...,
        alias="sequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Information instance identifier",
    )
