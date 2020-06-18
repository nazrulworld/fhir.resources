# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Account
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .domainresource import DomainResource


class Account(DomainResource):
    """A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centres,
    etc.
    """

    resource_type = Field("Account", const=True)

    balance: fhirtypes.MoneyType = Field(
        None,
        alias="balance",
        title="Type `Money` (represented as `dict` in JSON)",
        description="How much is in account?",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Explanation of purpose/use",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Account number",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human-readable label",
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

    coveragePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="coveragePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Transaction window",
    )

    activePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="activePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Transaction window",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | inactive | entered-in-error",
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
    currency: fhirtypes.CodingType = Field(
        None,
        alias="type",
        title="Type `Coding` (represented as `dict` in JSON).",
        description="Base currency in which balance is tracked.",
    )
