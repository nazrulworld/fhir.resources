# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class OrganizationAffiliation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines an affiliation/assotiation/relationship between 2 distinct
    oganizations, that is not a part-of relationship/sub-division relationship.
    """

    resource_type = Field("OrganizationAffiliation", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this organization affiliation record is in active use",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Definition of the role the participatingOrganization plays",
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "List of `Reference` items referencing `Endpoint` (represented as "
            "`dict` in JSON)"
        ),
        description=(
            "Technical endpoints providing access to services operated for this " "role"
        ),
    )

    healthcareService: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="healthcareService",
        title=(
            "List of `Reference` items referencing `HealthcareService` (represented"
            " as `dict` in JSON)"
        ),
        description="Healthcare services provided through the role",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifiers that are specific to this role",
    )

    location: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="location",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="The location(s) at which the role occurs",
    )

    network: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="network",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description=(
            "Health insurance provider network in which the "
            "participatingOrganization provides the role\u0027s services (if defined) at"
            " the indicated locations (if defined)"
        ),
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization where the role is available",
    )

    participatingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="participatingOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description=(
            "Organization that provides/performs the role (e.g. providing services "
            "or is a member of)"
        ),
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description=(
            "The period during which the participatingOrganization is affiliated "
            "with the primary organization"
        ),
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "Specific specialty of the participatingOrganization in the context of "
            "the role"
        ),
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description=(
            "Contact details at the participatingOrganization relevant to this "
            "Affiliation"
        ),
    )
