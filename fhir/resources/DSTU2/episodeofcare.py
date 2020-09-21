# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/episodeofcare.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class EpisodeOfCare(domainresource.DomainResource):
    """An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.

    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """

    resource_type = Field("EpisodeOfCare", const=True)

    careManager: fhirtypes.ReferenceType = Field(
        None,
        alias="careManager",
        title="Care manager/care coordinator for the patient",
        description=(
            "The practitioner that is the care manager/care coordinator for this "
            "patient."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    careTeam: ListType[fhirtypes.EpisodeOfCareCareTeamType] = Field(
        None,
        alias="careTeam",
        title="Other practitioners facilitating this episode of care",
        description=(
            "The list of practitioners that may be facilitating this episode of "
            "care for specific purposes."
        ),
    )

    condition: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="condition",
        title=(
            "List of `Reference` items referencing `Condition` (represented as `dict` "
            "in JSON)."
        ),
        description="Conditions/problems/diagnoses this episode of care is for.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier(s) relevant for this EpisodeOfCare",
        description=(
            "The EpisodeOfCare may be known by different identifiers for different "
            "contexts of use, such as when an external agency is tracking the "
            "Episode for funding purposes."
        ),
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Organization that assumes care",
        description=(
            "The organization that has assumed the specific responsibilities for "
            "the specified duration."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="The patient who is the focus of this episode of care",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Interval during responsibility is assumed",
        description=(
            "The interval during which the managing organization assumes the "
            "defined responsibility."
        ),
    )

    referralRequest: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="referralRequest",
        title="Originating Referral Request(s)",
        description=(
            "Referral Request(s) that are fulfilled by this EpisodeOfCare, incoming"
            " referrals."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ReferralRequest"],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="planned | waitlist | active | onhold | finished | cancelled",
        description="planned | waitlist | active | onhold | finished | cancelled.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "waitlist",
            "active",
            "onhold",
            "finished",
            "cancelled",
        ],
    )

    statusHistory: ListType[fhirtypes.EpisodeOfCareStatusHistoryType] = Field(
        None,
        alias="statusHistory",
        title=(
            "Past list of status codes (the current status may be included to cover"
            " the start date of the status)"
        ),
        description=(
            "The history of statuses that the EpisodeOfCare has been through "
            "(without requiring processing the history of the resource)."
        ),
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Type/class  - e.g. specialist referral, disease management",
        description=(
            "A classification of the type of episode of care; e.g. specialist "
            "referral, disease management, type of funded care."
        ),
    )


class EpisodeOfCareCareTeam(backboneelement.BackboneElement):
    """Other practitioners facilitating this episode of care."""

    resource_type = Field("EpisodeOfCareCareTeam", const=True)

    member: fhirtypes.ReferenceType = Field(
        None,
        alias="member",
        title=(
            "Type `Reference` referencing `Practitioner, Organization` (represented as "
            "`dict` in JSON)."
        ),
        description="The practitioner (or Organization) within the team.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Period of time for this role.",
    )

    role: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Role taken by this team member.",
    )


class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """Past list of status codes (the current status may be included to cover the
    start date of the status).

    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """

    resource_type = Field("EpisodeOfCareStatusHistory", const=True)

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Duration the EpisodeOfCare was in the specified status",
        description="The period during this EpisodeOfCare that the specific status applied.",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="planned | waitlist | active | onhold | finished | cancelled",
        description="planned | waitlist | active | onhold | finished | cancelled.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "waitlist",
            "active",
            "onhold",
            "finished",
            "cancelled",
        ],
    )
