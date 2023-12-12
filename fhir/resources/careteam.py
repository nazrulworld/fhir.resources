# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CareTeam
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class CareTeam(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Planned participants in the coordination and delivery of care.
    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care.
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

    reason: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="reason",
        title="Why the care team exists",
        description="Describes why the care team exists.",
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
            "period",
            "participant",
            "reason",
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

    coveragePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="coveragePeriod",
        title="When the member is generally available within this care team",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e coverage[x]
        one_of_many="coverage",
        one_of_many_required=False,
    )

    coverageTiming: fhirtypes.TimingType = Field(
        None,
        alias="coverageTiming",
        title="When the member is generally available within this care team",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e coverage[x]
        one_of_many="coverage",
        one_of_many_required=False,
    )

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

    role: fhirtypes.CodeableConceptType = Field(
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
            "coveragePeriod",
            "coverageTiming",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2104(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"coverage": ["coveragePeriod", "coverageTiming"]}
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
