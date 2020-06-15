# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ChargeItemDefinition(domainresource.DomainResource):
    """ Definition of properties and rules about how the price and the
    applicability of a ChargeItem can be determined.
    The ChargeItemDefinition resource provides the properties that apply to the
    (billing) codes necessary to calculate costs and prices. The properties may
    differ largely depending on type and realm, therefore this resource gives
    only a rough structure and requires profiling for each type of billing code
    system.
    """

    resource_type = Field("ChargeItemDefinition", const=True)

    applicability: ListType[fhirtypes.ChargeItemDefinitionApplicabilityType] = Field(
        None,
        alias="applicability",
        title=(
            "List of `ChargeItemDefinitionApplicability` items (represented as "
            "`dict` in JSON)"
        ),
        description="Whether or not the billing code is applicable",
    )

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the charge item definition was approved by publisher",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Billing codes or product types this definition applies to",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date last changed",
    )

    derivedFromUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="derivedFromUri",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Underlying externally-defined charge item definition",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the charge item definition",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the charge item definition is expected to be used",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the charge item definition",
    )

    instance: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="instance",
        title=(
            "List of `Reference` items referencing `Medication, Substance, Device` "
            "(represented as `dict` in JSON)"
        ),
        description="Instances this definition applies to",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for charge item definition (if applicable)",
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When the charge item definition was last reviewed",
    )

    partOf: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="partOf",
        title=(
            "List of `Canonical` items referencing `ChargeItemDefinition` "
            "(represented as `dict` in JSON)"
        ),
        description=(
            "A larger definition of which this particular definition is a component"
            " or step"
        ),
    )

    propertyGroup: ListType[fhirtypes.ChargeItemDefinitionPropertyGroupType] = Field(
        None,
        alias="propertyGroup",
        title=(
            "List of `ChargeItemDefinitionPropertyGroup` items (represented as "
            "`dict` in JSON)"
        ),
        description="Group of properties which are applicable under the same conditions",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    replaces: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="replaces",
        title=(
            "List of `Canonical` items referencing `ChargeItemDefinition` "
            "(represented as `dict` in JSON)"
        ),
        description=(
            "Completed or terminated request(s) whose function is taken by this new"
            " request"
        ),
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this charge item definition (human friendly)",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this charge item definition, represented as a"
            " URI (globally unique)"
        ),
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the charge item definition",
    )


class ChargeItemDefinitionApplicability(backboneelement.BackboneElement):
    """ Whether or not the billing code is applicable.
    Expressions that describe applicability criteria for the billing code.
    """

    resource_type = Field("ChargeItemDefinitionApplicability", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Natural language description of the condition",
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String` (represented as `dict` in JSON)",
        description="Boolean-valued expression",
    )

    language: fhirtypes.String = Field(
        None,
        alias="language",
        title="Type `String` (represented as `dict` in JSON)",
        description="Language of the expression",
    )


class ChargeItemDefinitionPropertyGroup(backboneelement.BackboneElement):
    """ Group of properties which are applicable under the same conditions.
    Group of properties which are applicable under the same conditions. If no
    applicability rules are established for the group, then all properties
    always apply.
    """

    resource_type = Field("ChargeItemDefinitionPropertyGroup", const=True)

    applicability: ListType[fhirtypes.ChargeItemDefinitionApplicabilityType] = Field(
        None,
        alias="applicability",
        title=(
            "List of `ChargeItemDefinitionApplicability` items (represented as "
            "`dict` in JSON)"
        ),
        description="Conditions under which the priceComponent is applicable",
    )

    priceComponent: ListType[
        fhirtypes.ChargeItemDefinitionPropertyGroupPriceComponentType
    ] = Field(
        None,
        alias="priceComponent",
        title=(
            "List of `ChargeItemDefinitionPropertyGroupPriceComponent` items "
            "(represented as `dict` in JSON)"
        ),
        description="Components of total line item price",
    )


class ChargeItemDefinitionPropertyGroupPriceComponent(backboneelement.BackboneElement):
    """ Components of total line item price.
    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice of how the prices have been calculated.
    """

    resource_type = Field("ChargeItemDefinitionPropertyGroupPriceComponent", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Type `Money` (represented as `dict` in JSON)",
        description="Monetary amount associated with this component",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Code identifying the specific component",
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="Factor used for calculating this component",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="base | surcharge | deduction | discount | tax | informational",
    )
