from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Account
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

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

    __resource_type__ = "Account"

    coverage: typing.List[fhirtypes.AccountCoverageType] | None = Field(  # type: ignore
        None,
        alias="coverage",
        title=(
            "The party(s) that are responsible for covering the payment of this "
            "account, and what order should they be applied to the account"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Explanation of purpose/use",
        description=(
            "Provides additional information about what the account tracks and how "
            "it is used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    guarantor: typing.List[fhirtypes.AccountGuarantorType] | None = Field(  # type: ignore
        None,
        alias="guarantor",
        title="The parties ultimately responsible for balancing the Account",
        description=(
            "The parties responsible for balancing the account if other payment "
            "options fall short."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Account number",
        description=(
            "Unique identifier used to reference the account.  Might or might not "
            "be intended for human use (e.g. credit card number)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Human-readable label",
        description=(
            "Name used for the account when displaying it to humans in reports, " "etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    owner: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="owner",
        title="Entity managing the Account",
        description=(
            "Indicates the service area, hospital, department, etc. with "
            "responsibility for managing the Account."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    partOf: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Reference to a parent Account",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Account"],
        },
    )

    servicePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="servicePeriod",
        title="Transaction window",
        description="The date range of services associated with this account.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | inactive | entered-in-error | on-hold | unknown",
        description="Indicates whether the account is presently used/usable or not.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "active",
                "inactive",
                "entered-in-error",
                "on-hold",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="subject",
        title="The entity that caused the expenses",
        description=(
            "Identifies the entity which incurs the expenses. While the immediate "
            "recipients of services or goods might be entities related to the "
            "subject, the expenses were ultimately incurred by the subject of the "
            "Account."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Device",
                "Practitioner",
                "PractitionerRole",
                "Location",
                "HealthcareService",
                "Organization",
            ],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="E.g. patient, expense, depreciation",
        description="Categorizes the account for reporting and searching purposes.",
        json_schema_extra={
            "element_property": True,
        },
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
            "servicePeriod",
            "coverage",
            "owner",
            "description",
            "guarantor",
            "partOf",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class AccountCoverage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """

    __resource_type__ = "AccountCoverage"

    coverage: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="coverage",
        title=(
            "The party(s), such as insurances, that may contribute to the payment "
            "of this account"
        ),
        description=(
            "The party(s) that contribute to payment (or part of) of the charges "
            "applied to this account (including self-pay).  A coverage may only be "
            "responsible for specific types of charges, and the sequence of the "
            "coverages in the account could be important when processing billing."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
    )

    priority: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="The priority of the coverage in the context of this account",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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

    The parties ultimately responsible for balancing the Account.
    The parties responsible for balancing the account if other payment options
    fall short.
    """

    __resource_type__ = "AccountGuarantor"

    onHold: bool | None = Field(  # type: ignore
        None,
        alias="onHold",
        title="Credit or other hold applied",
        description=(
            "A guarantor may be placed on credit hold or otherwise have their role "
            "temporarily suspended."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    onHold__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_onHold", title="Extension field for ``onHold``."
    )

    party: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="party",
        title="Responsible entity",
        description="The entity who is responsible.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "RelatedPerson", "Organization"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Guarantee account during",
        description=(
            "The timeframe during which the guarantor accepts responsibility for "
            "the account."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AccountGuarantor`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "party", "onHold", "period"]
