# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Account
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

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

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="Reference to a parent Account",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Account"],
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
