# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/InsurancePlan
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class InsurancePlan(domainresource.DomainResource):
    """ Details of a Health Insurance product/plan provided by an organization.
    """

    resource_type = Field("InsurancePlan", const=True)

    administeredBy: fhirtypes.ReferenceType = Field(
        None,
        alias="administeredBy",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Product administrator",
    )

    alias: ListType[fhirtypes.String] = Field(
        None,
        alias="alias",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Alternate names",
    )

    contact: ListType[fhirtypes.InsurancePlanContactType] = Field(
        None,
        alias="contact",
        title="List of `InsurancePlanContact` items (represented as `dict` in JSON)",
        description="Contact for the product",
    )

    coverage: ListType[fhirtypes.InsurancePlanCoverageType] = Field(
        None,
        alias="coverage",
        title="List of `InsurancePlanCoverage` items (represented as `dict` in JSON)",
        description="Coverage details",
    )

    coverageArea: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="coverageArea",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="Where product applies",
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "List of `Reference` items referencing `Endpoint` (represented as "
            "`dict` in JSON)"
        ),
        description="Technical endpoint",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for Product",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Official name",
    )

    network: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="network",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="What networks are Included",
    )

    ownedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="ownedBy",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Plan issuer",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the product is available",
    )

    plan: ListType[fhirtypes.InsurancePlanPlanType] = Field(
        None,
        alias="plan",
        title="List of `InsurancePlanPlan` items (represented as `dict` in JSON)",
        description="Plan details",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Kind of product",
    )


class InsurancePlanContact(backboneelement.BackboneElement):
    """ Contact for the product.
    The contact for the health insurance product for a certain purpose.
    """

    resource_type = Field("InsurancePlanContact", const=True)

    address: fhirtypes.AddressType = Field(
        None,
        alias="address",
        title="Type `Address` (represented as `dict` in JSON)",
        description="Visiting or postal addresses for the contact",
    )

    name: fhirtypes.HumanNameType = Field(
        None,
        alias="name",
        title="Type `HumanName` (represented as `dict` in JSON)",
        description="A name associated with the contact",
    )

    purpose: fhirtypes.CodeableConceptType = Field(
        None,
        alias="purpose",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The type of contact",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Contact details (telephone, email, etc.)  for a contact",
    )


class InsurancePlanCoverage(backboneelement.BackboneElement):
    """ Coverage details.
    Details about the coverage offered by the insurance product.
    """

    resource_type = Field("InsurancePlanCoverage", const=True)

    benefit: ListType[fhirtypes.InsurancePlanCoverageBenefitType] = Field(
        ...,
        alias="benefit",
        title=(
            "List of `InsurancePlanCoverageBenefit` items (represented as `dict` in"
            " JSON)"
        ),
        description="List of benefits",
    )

    network: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="network",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="What networks provide coverage",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of coverage",
    )


class InsurancePlanCoverageBenefit(backboneelement.BackboneElement):
    """ List of benefits.
    Specific benefits under this type of coverage.
    """

    resource_type = Field("InsurancePlanCoverageBenefit", const=True)

    limit: ListType[fhirtypes.InsurancePlanCoverageBenefitLimitType] = Field(
        None,
        alias="limit",
        title=(
            "List of `InsurancePlanCoverageBenefitLimit` items (represented as "
            "`dict` in JSON)"
        ),
        description="Benefit limits",
    )

    requirement: fhirtypes.String = Field(
        None,
        alias="requirement",
        title="Type `String` (represented as `dict` in JSON)",
        description="Referral requirements",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of benefit",
    )


class InsurancePlanCoverageBenefitLimit(backboneelement.BackboneElement):
    """ Benefit limits.
    The specific limits on the benefit.
    """

    resource_type = Field("InsurancePlanCoverageBenefitLimit", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Benefit limit details",
    )

    value: fhirtypes.QuantityType = Field(
        None,
        alias="value",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Maximum value allowed",
    )


class InsurancePlanPlan(backboneelement.BackboneElement):
    """ Plan details.
    Details about an insurance plan.
    """

    resource_type = Field("InsurancePlanPlan", const=True)

    coverageArea: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="coverageArea",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="Where product applies",
    )

    generalCost: ListType[fhirtypes.InsurancePlanPlanGeneralCostType] = Field(
        None,
        alias="generalCost",
        title=(
            "List of `InsurancePlanPlanGeneralCost` items (represented as `dict` in"
            " JSON)"
        ),
        description="Overall costs",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier for Product",
    )

    network: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="network",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="What networks provide coverage",
    )

    specificCost: ListType[fhirtypes.InsurancePlanPlanSpecificCostType] = Field(
        None,
        alias="specificCost",
        title=(
            "List of `InsurancePlanPlanSpecificCost` items (represented as `dict` "
            "in JSON)"
        ),
        description="Specific costs",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of plan",
    )


class InsurancePlanPlanGeneralCost(backboneelement.BackboneElement):
    """ Overall costs.
    Overall costs associated with the plan.
    """

    resource_type = Field("InsurancePlanPlanGeneralCost", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional cost information",
    )

    cost: fhirtypes.MoneyType = Field(
        None,
        alias="cost",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Cost value",
    )

    groupSize: fhirtypes.PositiveInt = Field(
        None,
        alias="groupSize",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Number of enrollees",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of cost",
    )


class InsurancePlanPlanSpecificCost(backboneelement.BackboneElement):
    """ Specific costs.
    Costs associated with the coverage provided by the product.
    """

    resource_type = Field("InsurancePlanPlanSpecificCost", const=True)

    benefit: ListType[fhirtypes.InsurancePlanPlanSpecificCostBenefitType] = Field(
        None,
        alias="benefit",
        title=(
            "List of `InsurancePlanPlanSpecificCostBenefit` items (represented as "
            "`dict` in JSON)"
        ),
        description="Benefits list",
    )

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="General category of benefit",
    )


class InsurancePlanPlanSpecificCostBenefit(backboneelement.BackboneElement):
    """ Benefits list.
    List of the specific benefits under this category of benefit.
    """

    resource_type = Field("InsurancePlanPlanSpecificCostBenefit", const=True)

    cost: ListType[fhirtypes.InsurancePlanPlanSpecificCostBenefitCostType] = Field(
        None,
        alias="cost",
        title=(
            "List of `InsurancePlanPlanSpecificCostBenefitCost` items (represented "
            "as `dict` in JSON)"
        ),
        description="List of the costs",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of specific benefit",
    )


class InsurancePlanPlanSpecificCostBenefitCost(backboneelement.BackboneElement):
    """ List of the costs.
    List of the costs associated with a specific benefit.
    """

    resource_type = Field("InsurancePlanPlanSpecificCostBenefitCost", const=True)

    applicability: fhirtypes.CodeableConceptType = Field(
        None,
        alias="applicability",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="in-network | out-of-network | other",
    )

    qualifiers: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="qualifiers",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Additional information about the cost",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of cost",
    )

    value: fhirtypes.QuantityType = Field(
        None,
        alias="value",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The actual cost value",
    )
