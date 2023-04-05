# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Account
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

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

    balance: typing.List[fhirtypes.AccountBalanceType] = Field(
        None,
        alias="balance",
        title="Calculated account balance(s)",
        description=(
            "The calculated account balances - these are calculated and processed "
            "by the finance system.  The balances with a `term` that is not current"
            " are usually generated/updated by an invoicing or similar process."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    billingStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="billingStatus",
        title="Tracks the lifecycle of the account through the billing process",
        description=(
            "The BillingStatus tracks the lifecycle of the account through the "
            "billing process. It indicates how transactions are treated when they "
            "are allocated to the account."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    calculatedAt: fhirtypes.Instant = Field(
        None,
        alias="calculatedAt",
        title="Time the balance amount was calculated",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    calculatedAt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_calculatedAt", title="Extension field for ``calculatedAt``."
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

    currency: fhirtypes.CodeableConceptType = Field(
        None,
        alias="currency",
        title="The base or default currency",
        description="The default currency for the account.",
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
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

    diagnosis: typing.List[fhirtypes.AccountDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="The list of diagnoses relevant to this account",
        description=(
            "When using an account for billing a specific Encounter the set of "
            "diagnoses that are relevant for billing are stored here on the account"
            " where they are able to be sequenced appropriately prior to processing"
            " to produce claim(s)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    guarantor: typing.List[fhirtypes.AccountGuarantorType] = Field(
        None,
        alias="guarantor",
        title="The parties ultimately responsible for balancing the Account",
        description=(
            "The parties responsible for balancing the account if other payment "
            "options fall short."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Account number",
        description=(
            "Unique identifier used to reference the account.  Might or might not "
            "be intended for human use (e.g. credit card number)."
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
        title="Entity managing the Account",
        description=(
            "Indicates the service area, hospital, department, etc. with "
            "responsibility for managing the Account."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    procedure: typing.List[fhirtypes.AccountProcedureType] = Field(
        None,
        alias="procedure",
        title="The list of procedures relevant to this account",
        description=(
            "When using an account for billing a specific Encounter the set of "
            "procedures that are relevant for billing are stored here on the "
            "account where they are able to be sequenced appropriately prior to "
            "processing to produce claim(s)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relatedAccount: typing.List[fhirtypes.AccountRelatedAccountType] = Field(
        None,
        alias="relatedAccount",
        title="Other associated accounts related to this account",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    servicePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicePeriod",
        title="Transaction window",
        description="The date range of services associated with this account.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | inactive | entered-in-error | on-hold | unknown",
        description="Indicates whether the account is presently used/usable or not.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error", "on-hold", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title="The entity that caused the expenses",
        description=(
            "Identifies the entity which incurs the expenses. While the immediate "
            "recipients of services or goods might be entities related to the "
            "subject, the expenses were ultimately incurred by the subject of the "
            "Account."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Device",
            "Practitioner",
            "PractitionerRole",
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
            "billingStatus",
            "type",
            "name",
            "subject",
            "servicePeriod",
            "coverage",
            "owner",
            "description",
            "guarantor",
            "diagnosis",
            "procedure",
            "relatedAccount",
            "currency",
            "balance",
            "calculatedAt",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_898(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class AccountBalance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Calculated account balance(s).
    The calculated account balances - these are calculated and processed by the
    finance system.

    The balances with a `term` that is not current are usually
    generated/updated by an invoicing or similar process.
    """

    resource_type = Field("AccountBalance", const=True)

    aggregate: fhirtypes.CodeableConceptType = Field(
        None,
        alias="aggregate",
        title="Who is expected to pay this part of the balance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    amount: fhirtypes.MoneyType = Field(
        ...,
        alias="amount",
        title="Calculated amount",
        description=(
            "The actual balance value calculated for the age defined in the term "
            "property."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    estimate: bool = Field(
        None,
        alias="estimate",
        title="Estimated balance",
        description=(
            "The amount is only an estimated value - this is likely common for "
            "`current` term balances, but not with known terms (that were generated"
            " by a backend process)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    estimate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_estimate", title="Extension field for ``estimate``."
    )

    term: fhirtypes.CodeableConceptType = Field(
        None,
        alias="term",
        title="current | 30 | 60 | 90 | 120",
        description=(
            "The term of the account balances - The balance value is the amount "
            "that was outstanding for this age."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AccountBalance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "aggregate",
            "term",
            "estimate",
            "amount",
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
            "The party(s), such as insurances, that may contribute to the payment "
            "of this account"
        ),
        description=(
            "The party(s) that contribute to payment (or part of) of the charges "
            "applied to this account (including self-pay).  A coverage may only be "
            "responsible for specific types of charges, and the sequence of the "
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


class AccountDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The list of diagnoses relevant to this account.
    When using an account for billing a specific Encounter the set of diagnoses
    that are relevant for billing are stored here on the account where they are
    able to be sequenced appropriately prior to processing to produce claim(s).
    """

    resource_type = Field("AccountDiagnosis", const=True)

    condition: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="condition",
        title="The diagnosis relevant to the account",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    dateOfDiagnosis: fhirtypes.DateTime = Field(
        None,
        alias="dateOfDiagnosis",
        title="Date of the diagnosis (when coded diagnosis)",
        description="Ranking of the diagnosis (for each type).",
        # if property is element of this resource.
        element_property=True,
    )
    dateOfDiagnosis__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateOfDiagnosis", title="Extension field for ``dateOfDiagnosis``."
    )

    onAdmission: bool = Field(
        None,
        alias="onAdmission",
        title="Diagnosis present on Admission",
        description="Was the Diagnosis present on Admission in the related Encounter.",
        # if property is element of this resource.
        element_property=True,
    )
    onAdmission__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onAdmission", title="Extension field for ``onAdmission``."
    )

    packageCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="packageCode",
        title="Package Code specific for billing",
        description=(
            "The package code can be used to group diagnoses that may be priced or "
            "delivered as a single product. Such as DRGs."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Ranking of the diagnosis (for each type)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title=(
            "Type that this diagnosis has relevant to the account (e.g. admission, "
            "billing, discharge \u2026)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AccountDiagnosis`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "condition",
            "dateOfDiagnosis",
            "type",
            "onAdmission",
            "packageCode",
        ]


class AccountGuarantor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The parties ultimately responsible for balancing the Account.
    The parties responsible for balancing the account if other payment options
    fall short.
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
        title="Guarantee account during",
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


class AccountProcedure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The list of procedures relevant to this account.
    When using an account for billing a specific Encounter the set of
    procedures that are relevant for billing are stored here on the account
    where they are able to be sequenced appropriately prior to processing to
    produce claim(s).
    """

    resource_type = Field("AccountProcedure", const=True)

    code: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="code",
        title="The procedure relevant to the account",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    dateOfService: fhirtypes.DateTime = Field(
        None,
        alias="dateOfService",
        title="Date of the procedure (when coded procedure)",
        description=(
            "Date of the procedure when using a coded procedure. If using a "
            "reference to a procedure, then the date on the procedure should be "
            "used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    dateOfService__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateOfService", title="Extension field for ``dateOfService``."
    )

    device: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="device",
        title="Any devices that were associated with the procedure",
        description=(
            "Any devices that were associated with the procedure relevant to the "
            "account."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    packageCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="packageCode",
        title="Package Code specific for billing",
        description=(
            "The package code can be used to group procedures that may be priced or"
            " delivered as a single product. Such as DRGs."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sequence: fhirtypes.PositiveInt = Field(
        None,
        alias="sequence",
        title="Ranking of the procedure (for each type)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="How this procedure value should be used in charging the account",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AccountProcedure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "code",
            "dateOfService",
            "type",
            "packageCode",
            "device",
        ]


class AccountRelatedAccount(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Other associated accounts related to this account.
    """

    resource_type = Field("AccountRelatedAccount", const=True)

    account: fhirtypes.ReferenceType = Field(
        ...,
        alias="account",
        title="Reference to an associated Account",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Account"],
    )

    relationship: fhirtypes.CodeableConceptType = Field(
        None,
        alias="relationship",
        title="Relationship of the associated Account",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AccountRelatedAccount`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "relationship", "account"]
