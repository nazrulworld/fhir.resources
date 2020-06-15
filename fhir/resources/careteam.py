# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CareTeam
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CareTeam(domainresource.DomainResource):
    """ Planned participants in the coordination and delivery of care for a patient
    or group.
    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """

    resource_type = Field("CareTeam", const=True)

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of team",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Encounter created as part of",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Ids for this team",
    )

    managingOrganization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="managingOrganization",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="Organization responsible for the care team",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the team, such as crisis assessment team",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about the CareTeam",
    )

    participant: ListType[fhirtypes.CareTeamParticipantType] = Field(
        None,
        alias="participant",
        title="List of `CareTeamParticipant` items (represented as `dict` in JSON)",
        description="Members of the team",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period team covers",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why the care team exists",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition` (represented as "
            "`dict` in JSON)"
        ),
        description="Why the care team exists",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="proposed | active | suspended | inactive | entered-in-error",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Who care team is for",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="A contact detail for the care team (that applies to all members)",
    )


class CareTeamParticipant(backboneelement.BackboneElement):
    """ Members of the team.
    Identifies all people and organizations who are expected to be involved in
    the care team.
    """

    resource_type = Field("CareTeamParticipant", const=True)

    member: fhirtypes.ReferenceType = Field(
        None,
        alias="member",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "RelatedPerson, Patient, Organization, CareTeam` (represented as `dict`"
            " in JSON)"
        ),
        description="Who is involved",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization of the practitioner",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period of participant",
    )

    role: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of involvement",
    )
