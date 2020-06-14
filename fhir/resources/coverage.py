# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.
    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """

    resource_type = Field("Coverage", const=True)

    beneficiary: fhirtypes.ReferenceType = Field(
        ...,
        alias="beneficiary",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Plan beneficiary",
    )

    class_fhir: ListType[fhirtypes.CoverageClassType] = Field(
        None,
        alias="class",
        title="List of `CoverageClass` items (represented as `dict` in JSON)",
        description="Additional coverage classifications",
    )

    contract: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="contract",
        title="List of `Reference` items referencing `Contract` (represented as `dict` in JSON)",
        description="Contract details",
    )

    costToBeneficiary: ListType[fhirtypes.CoverageCostToBeneficiaryType] = Field(
        None,
        alias="costToBeneficiary",
        title="List of `CoverageCostToBeneficiary` items (represented as `dict` in JSON)",
        description="Patient payments for services/products",
    )

    dependent: fhirtypes.String = Field(
        None,
        alias="dependent",
        title="Type `String` (represented as `dict` in JSON)",
        description="Dependent number",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for the coverage",
    )

    network: fhirtypes.String = Field(
        None,
        alias="network",
        title="Type `String` (represented as `dict` in JSON)",
        description="Insurer network",
    )

    order: fhirtypes.PositiveInt = Field(
        None,
        alias="order",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Relative order of the coverage",
    )

    payor: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="payor",
        title="List of `Reference` items referencing `Organization, Patient, RelatedPerson` (represented as `dict` in JSON)",
        description="Issuer of the policy",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Coverage start and end dates",
    )

    policyHolder: fhirtypes.ReferenceType = Field(
        None,
        alias="policyHolder",
        title="Type `Reference` referencing `Patient, RelatedPerson, Organization` (represented as `dict` in JSON)",
        description="Owner of the policy",
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Beneficiary relationship to the subscriber",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | cancelled | draft | entered-in-error",
    )

    subrogation: bool = Field(
        None,
        alias="subrogation",
        title="Type `bool`",
        description="Reimbursement to insurer",
    )

    subscriber: fhirtypes.ReferenceType = Field(
        None,
        alias="subscriber",
        title="Type `Reference` referencing `Patient, RelatedPerson` (represented as `dict` in JSON)",
        description="Subscriber to the policy",
    )

    subscriberId: fhirtypes.String = Field(
        None,
        alias="subscriberId",
        title="Type `String` (represented as `dict` in JSON)",
        description="ID assigned to the subscriber",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Coverage category such as medical or accident",
    )


class CoverageClass(backboneelement.BackboneElement):
    """ Additional coverage classifications.
    A suite of underwriter specific classifiers.
    """

    resource_type = Field("CoverageClass", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human readable description of the type and value",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of class such as \u0027group\u0027 or \u0027plan\u0027",
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="Value associated with the type",
    )


class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    """ Patient payments for services/products.
    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """

    resource_type = Field("CoverageCostToBeneficiary", const=True)

    exception: ListType[fhirtypes.CoverageCostToBeneficiaryExceptionType] = Field(
        None,
        alias="exception",
        title="List of `CoverageCostToBeneficiaryException` items (represented as `dict` in JSON)",
        description="Exceptions for patient payments",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Cost category",
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="Type `Money` (represented as `dict` in JSON)",
        description="The amount or percentage due from the beneficiary",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The amount or percentage due from the beneficiary",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
            "value": ["valueMoney", "valueQuantity",],
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


class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    """ Exceptions for patient payments.
    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """

    resource_type = Field("CoverageCostToBeneficiaryException", const=True)

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The effective period of the exception",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Exception category",
    )
