# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/InsurancePlan
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class InsurancePlan(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of a Health Insurance product/plan provided by an organization.
    """

    resource_type = Field("InsurancePlan", const=True)

    administeredBy: fhirtypes.ReferenceType = Field(
        None,
        alias="administeredBy",
        title="Product administrator",
        description=(
            "An organization which administer other services such as underwriting, "
            "customer service and/or claims processing on behalf of the health "
            "insurance product owner."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    alias: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="alias",
        title="Alternate names",
        description=(
            "A list of alternate names that the product is known as, or was known "
            "as in the past."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    alias__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_alias", title="Extension field for ``alias``.")

    contact: typing.List[fhirtypes.InsurancePlanContactType] = Field(
        None,
        alias="contact",
        title="Contact for the product",
        description="The contact for the health insurance product for a certain purpose.",
        # if property is element of this resource.
        element_property=True,
    )

    coverage: typing.List[fhirtypes.InsurancePlanCoverageType] = Field(
        None,
        alias="coverage",
        title="Coverage details",
        description="Details about the coverage offered by the insurance product.",
        # if property is element of this resource.
        element_property=True,
    )

    coverageArea: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="coverageArea",
        title="Where product applies",
        description=(
            "The geographic region in which a health insurance product's benefits "
            "apply."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Technical endpoint",
        description=(
            "The technical endpoints providing access to services operated for the "
            "health insurance product."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for Product",
        description=(
            "Business identifiers assigned to this health insurance product which "
            "remain constant as the resource is updated and propagates from server "
            "to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Official name",
        description=(
            "Official name of the health insurance product as designated by the "
            "owner."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    network: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="network",
        title="What networks are Included",
        description="Reference to the network included in the health insurance product.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    ownedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="ownedBy",
        title="Plan issuer",
        description=(
            "The entity that is providing  the health insurance product and "
            "underwriting the risk.  This is typically an insurance carriers, other"
            " third-party payers, or health plan sponsors comonly referred to as "
            "'payers'."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When the product is available",
        description="The period of time that the health insurance product is available.",
        # if property is element of this resource.
        element_property=True,
    )

    plan: typing.List[fhirtypes.InsurancePlanPlanType] = Field(
        None,
        alias="plan",
        title="Plan details",
        description="Details about an insurance plan.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of the health insurance product.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Kind of product",
        description="The kind of health insurance product.",
        # if property is element of this resource.
        element_property=True,
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


class InsurancePlanContact(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contact for the product.
    The contact for the health insurance product for a certain purpose.
    """

    resource_type = Field("InsurancePlanContact", const=True)

    address: fhirtypes.AddressType = Field(
        None,
        alias="address",
        title="Visiting or postal addresses for the contact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.HumanNameType = Field(
        None,
        alias="name",
        title="A name associated with the contact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    purpose: fhirtypes.CodeableConceptType = Field(
        None,
        alias="purpose",
        title="The type of contact",
        description="Indicates a purpose for which the contact can be reached.",
        # if property is element of this resource.
        element_property=True,
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact details (telephone, email, etc.)  for a contact",
        description=(
            "A contact detail (e.g. a telephone number or an email address) by "
            "which the party may be contacted."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InsurancePlanContact`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "purpose",
            "name",
            "telecom",
            "address",
        ]


class InsurancePlanCoverage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Coverage details.
    Details about the coverage offered by the insurance product.
    """

    resource_type = Field("InsurancePlanCoverage", const=True)

    benefit: typing.List[fhirtypes.InsurancePlanCoverageBenefitType] = Field(
        ...,
        alias="benefit",
        title="List of benefits",
        description="Specific benefits under this type of coverage.",
        # if property is element of this resource.
        element_property=True,
    )

    network: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="network",
        title="What networks provide coverage",
        description="Reference to the network that providing the type of coverage.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of coverage",
        description=(
            "Type of coverage  (Medical; Dental; Mental Health; Substance Abuse; "
            "Vision; Drug; Short Term; Long Term Care; Hospice; Home Health)."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("InsurancePlanCoverageBenefit", const=True)

    limit: typing.List[fhirtypes.InsurancePlanCoverageBenefitLimitType] = Field(
        None,
        alias="limit",
        title="Benefit limits",
        description="The specific limits on the benefit.",
        # if property is element of this resource.
        element_property=True,
    )

    requirement: fhirtypes.String = Field(
        None,
        alias="requirement",
        title="Referral requirements",
        description="The referral requirements to have access/coverage for this benefit.",
        # if property is element of this resource.
        element_property=True,
    )
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requirement", title="Extension field for ``requirement``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of benefit",
        description=(
            "Type of benefit (primary care; speciality care; inpatient; " "outpatient)."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("InsurancePlanCoverageBenefitLimit", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Benefit limit details",
        description="The specific limit on the benefit.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.QuantityType = Field(
        None,
        alias="value",
        title="Maximum value allowed",
        description=(
            "The maximum amount of a service item a plan will pay for a covered "
            "benefit.  For examples. wellness visits, or eyeglasses."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("InsurancePlanPlan", const=True)

    coverageArea: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="coverageArea",
        title="Where product applies",
        description=(
            "The geographic region in which a health insurance plan's benefits "
            "apply."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    generalCost: typing.List[fhirtypes.InsurancePlanPlanGeneralCostType] = Field(
        None,
        alias="generalCost",
        title="Overall costs",
        description="Overall costs associated with the plan.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for Product",
        description=(
            "Business identifiers assigned to this health insurance plan which "
            "remain constant as the resource is updated and propagates from server "
            "to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    network: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="network",
        title="What networks provide coverage",
        description="Reference to the network that providing the type of coverage.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    specificCost: typing.List[fhirtypes.InsurancePlanPlanSpecificCostType] = Field(
        None,
        alias="specificCost",
        title="Specific costs",
        description="Costs associated with the coverage provided by the product.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of plan",
        description='Type of plan. For example, "Platinum" or "High Deductable".',
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("InsurancePlanPlanGeneralCost", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Additional cost information",
        description=(
            "Additional information about the general costs associated with this "
            "plan."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    cost: fhirtypes.MoneyType = Field(
        None,
        alias="cost",
        title="Cost value",
        description="Value of the cost.",
        # if property is element of this resource.
        element_property=True,
    )

    groupSize: fhirtypes.PositiveInt = Field(
        None,
        alias="groupSize",
        title="Number of enrollees",
        description="Number of participants enrolled in the plan.",
        # if property is element of this resource.
        element_property=True,
    )
    groupSize__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_groupSize", title="Extension field for ``groupSize``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of cost",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("InsurancePlanPlanSpecificCost", const=True)

    benefit: typing.List[fhirtypes.InsurancePlanPlanSpecificCostBenefitType] = Field(
        None,
        alias="benefit",
        title="Benefits list",
        description="List of the specific benefits under this category of benefit.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="General category of benefit",
        description=(
            "General category of benefit (Medical; Dental; Vision; Drug; Mental "
            "Health; Substance Abuse; Hospice, Home Health)."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("InsurancePlanPlanSpecificCostBenefit", const=True)

    cost: typing.List[fhirtypes.InsurancePlanPlanSpecificCostBenefitCostType] = Field(
        None,
        alias="cost",
        title="List of the costs",
        description="List of the costs associated with a specific benefit.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of specific benefit",
        description=(
            "Type of specific benefit (preventative; primary care office visit; "
            "speciality office visit; hospitalization; emergency room; urgent "
            "care)."
        ),
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("InsurancePlanPlanSpecificCostBenefitCost", const=True)

    applicability: fhirtypes.CodeableConceptType = Field(
        None,
        alias="applicability",
        title="in-network | out-of-network | other",
        description=(
            "Whether the cost applies to in-network or out-of-network providers "
            "(in-network; out-of-network; other)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    qualifiers: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="qualifiers",
        title="Additional information about the cost",
        description=(
            "Additional information about the cost, such as information about "
            "funding sources (e.g. HSA, HRA, FSA, RRA)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type of cost",
        description=(
            "Type of cost (copay; individual cap; family cap; coinsurance; "
            "deductible)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.QuantityType = Field(
        None,
        alias="value",
        title="The actual cost value",
        description=(
            "The actual cost value. (some of the costs may be represented as "
            "percentages rather than currency, e.g. 10% coinsurance)."
        ),
        # if property is element of this resource.
        element_property=True,
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
