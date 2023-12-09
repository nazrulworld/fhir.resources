# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Account
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class Account(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Time window that transactions may be posted to this account",
        description=(
            "Indicates the period of time over which the account is allowed to have"
            " transactions posted to it. This period may be different to the "
            "coveragePeriod which is the duration of time that services may occur."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    balance: fhirtypes.MoneyType = Field(
        None,
        alias="balance",
        title="How much is in account?",
        description=(
            "Represents the sum of all credits less all debits associated with the "
            "account.  Might be positive, zero or negative."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    coverage: typing.List[fhirtypes.AccountCoverageType] = Field(
        None,
        alias="coverage",
        title=(
            "The party(s) that are responsible for covering the payment of this "
            "account, and what order should they be applied to the account"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Explanation of purpose/use",
        description=(
            "Provides additional information about what the account tracks and how "
            "it is used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    guarantor: typing.List[fhirtypes.AccountGuarantorType] = Field(
        None,
        alias="guarantor",
        title="Responsible for the account",
        description="Parties financially responsible for the account.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Account number",
        description=(
            "Unique identifier used to reference the account.  May or may not be "
            "intended for human use (e.g. credit card number)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Human-readable label",
        description=(
            "Name used for the account when displaying it to humans in reports, " "etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    owner: fhirtypes.ReferenceType = Field(
        None,
        alias="owner",
        title="Who is responsible?",
        description=(
            "Indicates the organization, department, etc. with responsibility for "
            "the account."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Transaction window",
        description=(
            "Identifies the period of time the account applies to; e.g. accounts "
            "created per fiscal year, quarter, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="Indicates whether the account is presently used/usable or not.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="What is account tied to?",
        description=(
            "Identifies the patient, device, practitioner, location or other object"
            " the account is associated with."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Device",
            "Practitioner",
            "Location",
            "HealthcareService",
            "Organization",
        ],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="E.g. patient, expense, depreciation",
        description="Categorizes the account for reporting and searching purposes.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Account`` according specification,
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
            "subject",
            "period",
            "active",
            "balance",
            "coverage",
            "owner",
            "description",
            "guarantor",
        ]


class AccountCoverage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
            "The party(s) that are responsible for covering the payment of this "
            "account"
        ),
        description=(
            "The party(s) that are responsible for payment (or part of) of charges "
            "applied to this account (including self-pay).  A coverage may only be "
            "resposible for specific types of charges, and the sequence of the "
            "coverages in the account could be important when processing billing."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Coverage"],
    )

    priority: fhirtypes.PositiveInt = Field(
        None,
        alias="priority",
        title="The priority of the coverage in the context of this account",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AccountCoverage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "coverage", "priority"]


class AccountGuarantor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Responsible for the account.
    Parties financially responsible for the account.
    """

    resource_type = Field("AccountGuarantor", const=True)

    onHold: bool = Field(
        None,
        alias="onHold",
        title="Credit or other hold applied",
        description=(
            "A guarantor may be placed on credit hold or otherwise have their role "
            "temporarily suspended."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    onHold__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onHold", title="Extension field for ``onHold``."
    )

    party: fhirtypes.ReferenceType = Field(
        ...,
        alias="party",
        title="Responsible entity",
        description="The entity who is responsible.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "RelatedPerson", "Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Guarrantee account during",
        description=(
            "The timeframe during which the guarantor accepts responsibility for "
            "the account."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AccountGuarantor`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "party", "onHold", "period"]
