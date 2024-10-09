from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/InsurancePlan
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class InsurancePlan(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of a Health Insurance product/plan provided by an organization.
    """

    __resource_type__ = "InsurancePlan"

    administeredBy: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="administeredBy",
        title="Product administrator",
        description=(
            "An organization which administer other services such as underwriting, "
            "customer service and/or claims processing on behalf of the health "
            "insurance product owner."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    alias: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="alias",
        title="Alternate names",
        description=(
            "A list of alternate names that the product is known as, or was known "
            "as in the past."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    alias__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_alias", title="Extension field for ``alias``."
    )

    contact: typing.List[fhirtypes.ExtendedContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Official contact details relevant to the health insurance plan/product",
        description=(
            "The contact details of communication devices available relevant to the"
            " specific Insurance Plan/Product. This can include addresses, phone "
            "numbers, fax numbers, mobile numbers, email addresses and web sites."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    coverage: typing.List[fhirtypes.InsurancePlanCoverageType] | None = Field(  # type: ignore
        None,
        alias="coverage",
        title="Coverage details",
        description="Details about the coverage offered by the insurance product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    coverageArea: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="coverageArea",
        title="Where product applies",
        description=(
            "The geographic region in which a health insurance product's benefits "
            "apply."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    endpoint: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="endpoint",
        title="Technical endpoint",
        description=(
            "The technical endpoints providing access to services operated for the "
            "health insurance product."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Endpoint"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for Product",
        description=(
            "Business identifiers assigned to this health insurance product which "
            "remain constant as the resource is updated and propagates from server "
            "to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Official name",
        description=(
            "Official name of the health insurance product as designated by the "
            "owner."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    network: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="network",
        title="What networks are Included",
        description="Reference to the network included in the health insurance product.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    ownedBy: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="ownedBy",
        title="Product issuer",
        description=(
            "The entity that is providing  the health insurance product and "
            "underwriting the risk.  This is typically an insurance carriers, other"
            " third-party payers, or health plan sponsors comonly referred to as "
            "'payers'."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="When the product is available",
        description="The period of time that the health insurance product is available.",
        json_schema_extra={
            "element_property": True,
        },
    )

    plan: typing.List[fhirtypes.InsurancePlanPlanType] | None = Field(  # type: ignore
        None,
        alias="plan",
        title="Plan details",
        description="Details about an insurance plan.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of the health insurance product.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Kind of product",
        description="The kind of health insurance product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlan`` according specification,
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
            "name",
            "alias",
            "period",
            "ownedBy",
            "administeredBy",
            "coverageArea",
            "contact",
            "endpoint",
            "network",
            "coverage",
            "plan",
        ]


class InsurancePlanCoverage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Coverage details.
    Details about the coverage offered by the insurance product.
    """

    __resource_type__ = "InsurancePlanCoverage"

    benefit: typing.List[fhirtypes.InsurancePlanCoverageBenefitType] = Field(  # type: ignore
        ...,
        alias="benefit",
        title="List of benefits",
        description="Specific benefits under this type of coverage.",
        json_schema_extra={
            "element_property": True,
        },
    )

    network: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="network",
        title="What networks provide coverage",
        description="Reference to the network that providing the type of coverage.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type of coverage",
        description=(
            "Type of coverage  (Medical; Dental; Mental Health; Substance Abuse; "
            "Vision; Drug; Short Term; Long Term Care; Hospice; Home Health)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlanCoverage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "network", "benefit"]


class InsurancePlanCoverageBenefit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of benefits.
    Specific benefits under this type of coverage.
    """

    __resource_type__ = "InsurancePlanCoverageBenefit"

    limit: typing.List[fhirtypes.InsurancePlanCoverageBenefitLimitType] | None = Field(  # type: ignore
        None,
        alias="limit",
        title="Benefit limits",
        description="The specific limits on the benefit.",
        json_schema_extra={
            "element_property": True,
        },
    )

    requirement: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="requirement",
        title="Referral requirements",
        description="The referral requirements to have access/coverage for this benefit.",
        json_schema_extra={
            "element_property": True,
        },
    )
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_requirement", title="Extension field for ``requirement``."
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type of benefit",
        description=(
            "Type of benefit (primary care; speciality care; inpatient; " "outpatient)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlanCoverageBenefit`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "requirement", "limit"]


class InsurancePlanCoverageBenefitLimit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefit limits.
    The specific limits on the benefit.
    """

    __resource_type__ = "InsurancePlanCoverageBenefitLimit"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Benefit limit details",
        description="The specific limit on the benefit.",
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Maximum value allowed",
        description=(
            "The maximum amount of a service item a plan will pay for a covered "
            "benefit.  For examples. wellness visits, or eyeglasses."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlanCoverageBenefitLimit`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "value", "code"]


class InsurancePlanPlan(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Plan details.
    Details about an insurance plan.
    """

    __resource_type__ = "InsurancePlanPlan"

    coverageArea: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="coverageArea",
        title="Where product applies",
        description=(
            "The geographic region in which a health insurance plan's benefits "
            "apply."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    generalCost: typing.List[fhirtypes.InsurancePlanPlanGeneralCostType] | None = Field(  # type: ignore
        None,
        alias="generalCost",
        title="Overall costs",
        description="Overall costs associated with the plan.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for Product",
        description=(
            "Business identifiers assigned to this health insurance plan which "
            "remain constant as the resource is updated and propagates from server "
            "to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    network: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="network",
        title="What networks provide coverage",
        description="Reference to the network that providing the type of coverage.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    specificCost: typing.List[fhirtypes.InsurancePlanPlanSpecificCostType] | None = Field(  # type: ignore
        None,
        alias="specificCost",
        title="Specific costs",
        description="Costs associated with the coverage provided by the product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type of plan",
        description='Type of plan. For example, "Platinum" or "High Deductable".',
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlanPlan`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "type",
            "coverageArea",
            "network",
            "generalCost",
            "specificCost",
        ]


class InsurancePlanPlanGeneralCost(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Overall costs.
    Overall costs associated with the plan.
    """

    __resource_type__ = "InsurancePlanPlanGeneralCost"

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Additional cost information",
        description=(
            "Additional information about the general costs associated with this "
            "plan."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    cost: fhirtypes.MoneyType | None = Field(  # type: ignore
        None,
        alias="cost",
        title="Cost value",
        description="Value of the cost.",
        json_schema_extra={
            "element_property": True,
        },
    )

    groupSize: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="groupSize",
        title="Number of enrollees",
        description="Number of participants enrolled in the plan.",
        json_schema_extra={
            "element_property": True,
        },
    )
    groupSize__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_groupSize", title="Extension field for ``groupSize``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type of cost",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlanPlanGeneralCost`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "groupSize",
            "cost",
            "comment",
        ]


class InsurancePlanPlanSpecificCost(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specific costs.
    Costs associated with the coverage provided by the product.
    """

    __resource_type__ = "InsurancePlanPlanSpecificCost"

    benefit: typing.List[fhirtypes.InsurancePlanPlanSpecificCostBenefitType] | None = Field(  # type: ignore
        None,
        alias="benefit",
        title="Benefits list",
        description="List of the specific benefits under this category of benefit.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="category",
        title="General category of benefit",
        description=(
            "General category of benefit (Medical; Dental; Vision; Drug; Mental "
            "Health; Substance Abuse; Hospice, Home Health)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlanPlanSpecificCost`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "category", "benefit"]


class InsurancePlanPlanSpecificCostBenefit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefits list.
    List of the specific benefits under this category of benefit.
    """

    __resource_type__ = "InsurancePlanPlanSpecificCostBenefit"

    cost: typing.List[fhirtypes.InsurancePlanPlanSpecificCostBenefitCostType] | None = Field(  # type: ignore
        None,
        alias="cost",
        title="List of the costs",
        description="List of the costs associated with a specific benefit.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type of specific benefit",
        description=(
            "Type of specific benefit (preventative; primary care office visit; "
            "speciality office visit; hospitalization; emergency room; urgent "
            "care)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlanPlanSpecificCostBenefit`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "cost"]


class InsurancePlanPlanSpecificCostBenefitCost(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of the costs.
    List of the costs associated with a specific benefit.
    """

    __resource_type__ = "InsurancePlanPlanSpecificCostBenefitCost"

    applicability: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="applicability",
        title="in-network | out-of-network | other",
        description=(
            "Whether the cost applies to in-network or out-of-network providers "
            "(in-network; out-of-network; other)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    qualifiers: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="qualifiers",
        title="Additional information about the cost",
        description=(
            "Additional information about the cost, such as information about "
            "funding sources (e.g. HSA, HRA, FSA, RRA)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Type of cost",
        description=(
            "Type of cost (copay; individual cap; family cap; coinsurance; "
            "deductible)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="value",
        title="The actual cost value",
        description=(
            "The actual cost value. (some of the costs may be represented as "
            "percentages rather than currency, e.g. 10% coinsurance)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlanPlanSpecificCostBenefitCost`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "applicability",
            "qualifiers",
            "value",
        ]
