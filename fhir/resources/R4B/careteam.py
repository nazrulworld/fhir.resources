# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CareTeam
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class CareTeam(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Planned participants in the coordination and delivery of care for a patient
    or group.
    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """

    resource_type = Field("CareTeam", const=True)

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Type of team",
        description=(
            "Identifies what kind of team.  This is to support differentiation "
            "between multiple co-existing teams, such as care plan team, episode of"
            " care team, longitudinal care team."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter created as part of",
        description=(
            "The Encounter during which this CareTeam was created or to which the "
            "creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Ids for this team",
        description=(
            "Business identifiers assigned to this care team by the performer or "
            "other systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    managingOrganization: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="managingOrganization",
        title="Organization responsible for the care team",
        description="The organization responsible for the care team.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of the team, such as crisis assessment team",
        description=(
            "A label for human use intended to distinguish like teams.  E.g. the "
            '"red" vs. "green" trauma teams.'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the CareTeam",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    participant: typing.List[fhirtypes.CareTeamParticipantType] = Field(
        None,
        alias="participant",
        title="Members of the team",
        description=(
            "Identifies all people and organizations who are expected to be "
            "involved in the care team."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period team covers",
        description=(
            "Indicates when the team did (or is intended to) come into effect and "
            "end."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why the care team exists",
        description="Describes why the care team exists.",
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why the care team exists",
        description="Condition(s) that this care team addresses.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="proposed | active | suspended | inactive | entered-in-error",
        description="Indicates the current state of the care team.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["proposed", "active", "suspended", "inactive", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who care team is for",
        description=(
            "Identifies the patient or group whose intended care is handled by the "
            "team."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="A contact detail for the care team (that applies to all members)",
        description=(
            "A central contact detail for the care team (that applies to all "
            "members)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CareTeam`` according specification,
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
            "category",
            "name",
            "subject",
            "encounter",
            "period",
            "participant",
            "reasonCode",
            "reasonReference",
            "managingOrganization",
            "telecom",
            "note",
        ]


class CareTeamParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Members of the team.
    Identifies all people and organizations who are expected to be involved in
    the care team.
    """

    resource_type = Field("CareTeamParticipant", const=True)

    member: fhirtypes.ReferenceType = Field(
        None,
        alias="member",
        title="Who is involved",
        description=(
            "The specific person or organization who is participating/expected to "
            "participate in the care team."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Patient",
            "Organization",
            "CareTeam",
        ],
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Organization of the practitioner",
        description="The organization of the practitioner.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period of participant",
        description=(
            "Indicates when the specific member or organization did (or is intended"
            " to) come into effect and end."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    role: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="role",
        title="Type of involvement",
        description=(
            "Indicates specific responsibility of an individual within the care "
            'team, such as "Primary care physician", "Trained social worker '
            'counselor", "Caregiver", etc.'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CareTeamParticipant`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "role",
            "member",
            "onBehalfOf",
            "period",
        ]
