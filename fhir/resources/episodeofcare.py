# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EpisodeOfCare
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class EpisodeOfCare(domainresource.DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """

    resource_type = Field("EpisodeOfCare", const=True)

    account: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="account",
        title=(
            "List of `Reference` items referencing `Account` (represented as `dict`"
            " in JSON)"
        ),
        description=(
            "The set of accounts that may be used for billing for this " "EpisodeOfCare"
        ),
    )

    careManager: fhirtypes.ReferenceType = Field(
        None,
        alias="careManager",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="Care manager/care coordinator for the patient",
    )

    diagnosis: ListType[fhirtypes.EpisodeOfCareDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of `EpisodeOfCareDiagnosis` items (represented as `dict` in JSON)",
        description="The list of diagnosis relevant to this episode of care",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifier(s) relevant for this EpisodeOfCare",
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization that assumes care",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The patient who is the focus of this episode of care",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Interval during responsibility is assumed",
    )

    referralRequest: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="referralRequest",
        title=(
            "List of `Reference` items referencing `ServiceRequest` (represented as"
            " `dict` in JSON)"
        ),
        description="Originating Referral Request(s)",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "planned | waitlist | active | onhold | finished | cancelled | entered-"
            "in-error"
        ),
    )

    statusHistory: ListType[fhirtypes.EpisodeOfCareStatusHistoryType] = Field(
        None,
        alias="statusHistory",
        title=(
            "List of `EpisodeOfCareStatusHistory` items (represented as `dict` in "
            "JSON)"
        ),
        description=(
            "Past list of status codes (the current status may be included to cover"
            " the start date of the status)"
        ),
    )

    team: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="team",
        title=(
            "List of `Reference` items referencing `CareTeam` (represented as "
            "`dict` in JSON)"
        ),
        description="Other practitioners facilitating this episode of care",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type/class  - e.g. specialist referral, disease management",
    )


class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    """ The list of diagnosis relevant to this episode of care.
    """

    resource_type = Field("EpisodeOfCareDiagnosis", const=True)

    condition: fhirtypes.ReferenceType = Field(
        ...,
        alias="condition",
        title=(
            "Type `Reference` referencing `Condition` (represented as `dict` in "
            "JSON)"
        ),
        description="Conditions/problems/diagnoses this episode of care is for",
    )

    rank: fhirtypes.PositiveInt = Field(
        None,
        alias="rank",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Ranking of the diagnosis (for each role type)",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Role that this diagnosis has within the episode of care (e.g. "
            "admission, billing, discharge \u2026)"
        ),
    )


class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """ Past list of status codes (the current status may be included to cover the
    start date of the status).
    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """

    resource_type = Field("EpisodeOfCareStatusHistory", const=True)

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Duration the EpisodeOfCare was in the specified status",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "planned | waitlist | active | onhold | finished | cancelled | entered-"
            "in-error"
        ),
    )
