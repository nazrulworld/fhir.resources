# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Account
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Account(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Tracks balance, charges, for patient or cost center.
    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """

    resource_type = Field("Account", const=True)

    active: fhirtypes.PeriodType = Field(
        None,
        alias="active",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time window that transactions may be posted to this account",
    )

    balance: fhirtypes.MoneyType = Field(
        None,
        alias="balance",
        title="Type `Money` (represented as `dict` in JSON)",
        description="How much is in account?",
    )

    coverage: ListType[fhirtypes.AccountCoverageType] = Field(
        None,
        alias="coverage",
        title="List of `AccountCoverage` items (represented as `dict` in JSON)",
        description=(
            "The party(s) that are responsible for covering the payment of this "
            "account, and what order should they be applied to the account"
        ),
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Explanation of purpose/use",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    guarantor: ListType[fhirtypes.AccountGuarantorType] = Field(
        None,
        alias="guarantor",
        title="List of `AccountGuarantor` items (represented as `dict` in JSON)",
        description="Responsible for the account",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Account number",
    )

    name: fhirtypes.String = Field(
        None, alias="name", title="Type `String`", description="Human-readable label"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    owner: fhirtypes.ReferenceType = Field(
        None,
        alias="owner",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Who is responsible?",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Transaction window",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description="active | inactive | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Device, Practitioner, Location,"
            " HealthcareService, Organization` (represented as `dict` in JSON)"
        ),
        description="What is account tied to?",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="E.g. patient, expense, depreciation",
    )


class AccountCoverage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """

    resource_type = Field("AccountCoverage", const=True)

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title=(
            "Type `Reference` referencing `Coverage` (represented as `dict` in " "JSON)"
        ),
        description=(
            "The party(s) that are responsible for covering the payment of this "
            "account"
        ),
    )

    priority: fhirtypes.PositiveInt = Field(
        None,
        alias="priority",
        title="Type `PositiveInt`",
        description="The priority of the coverage in the context of this account",
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )


class AccountGuarantor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Responsible for the account.
    Parties financially responsible for the account.
    """

    resource_type = Field("AccountGuarantor", const=True)

    onHold: bool = Field(
        None,
        alias="onHold",
        title="Type `bool`",
        description="Credit or other hold applied",
    )
    onHold__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onHold", title="Extension field for ``onHold``."
    )

    party: fhirtypes.ReferenceType = Field(
        ...,
        alias="party",
        title=(
            "Type `Reference` referencing `Patient, RelatedPerson, Organization` "
            "(represented as `dict` in JSON)"
        ),
        description="Responsible entity",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Guarrantee account during",
    )
