from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/EpisodeOfCare
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class EpisodeOfCare(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """

    __resource_type__ = "EpisodeOfCare"

    account: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="account",
        title=(
            "The set of accounts that may be used for billing for this " "EpisodeOfCare"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Account"],
        },
    )

    careManager: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="careManager",
        title="Care manager/care co-ordinator for the patient",
        description=(
            "The practitioner that is the care manager/care co-ordinator for this "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    diagnosis: typing.List[fhirtypes.EpisodeOfCareDiagnosisType] | None = Field(  # type: ignore
        default=None,
        alias="diagnosis",
        title="The list of diagnosis relevant to this episode of care",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Business Identifier(s) relevant for this EpisodeOfCare",
        description=(
            "The EpisodeOfCare may be known by different identifiers for different "
            "contexts of use, such as when an external agency is tracking the "
            "Episode for funding purposes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    managingOrganization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="managingOrganization",
        title="Organization that assumes care",
        description=(
            "The organization that has assumed the specific responsibilities for "
            "the specified duration."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="patient",
        title="The patient who is the focus of this episode of care",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="period",
        title="Interval during responsibility is assumed",
        description=(
            "The interval during which the managing organization assumes the "
            "defined responsibility."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    referralRequest: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="referralRequest",
        title="Originating Referral Request(s)",
        description=(
            "Referral Request(s) that are fulfilled by this EpisodeOfCare, incoming"
            " referrals."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ReferralRequest"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title=(
            "planned | waitlist | active | onhold | finished | cancelled | entered-"
            "in-error"
        ),
        description="planned | waitlist | active | onhold | finished | cancelled.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "planned",
                "waitlist",
                "active",
                "onhold",
                "finished",
                "cancelled",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    statusHistory: typing.List[fhirtypes.EpisodeOfCareStatusHistoryType] | None = Field(  # type: ignore
        default=None,
        alias="statusHistory",
        title=(
            "Past list of status codes (the current status may be included to cover"
            " the start date of the status)"
        ),
        description=(
            "The history of statuses that the EpisodeOfCare has been through "
            "(without requiring processing the history of the resource)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    team: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="team",
        title="Other practitioners facilitating this episode of care",
        description=(
            "The list of practitioners that may be facilitating this episode of "
            "care for specific purposes."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CareTeam"],
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Type/class  - e.g. specialist referral, disease management",
        description=(
            "A classification of the type of episode of care; e.g. specialist "
            "referral, disease management, type of funded care."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``EpisodeOfCare`` according to specification,
        with preserving the original sequence order.
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
            "statusHistory",
            "type",
            "diagnosis",
            "patient",
            "managingOrganization",
            "period",
            "referralRequest",
            "careManager",
            "team",
            "account",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``EpisodeOfCare`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "status",
            "type",
            "diagnosis",
            "patient",
            "managingOrganization",
            "period",
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


class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The list of diagnosis relevant to this episode of care.
    """

    __resource_type__ = "EpisodeOfCareDiagnosis"

    condition: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="condition",
        title="Conditions/problems/diagnoses this episode of care is for",
        description=(
            "A list of conditions/problems/diagnoses that this episode of care is "
            "intended to be providing care for."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition"],
        },
    )

    rank: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        default=None,
        alias="rank",
        title="Ranking of the diagnosis (for each role type)",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_rank", title="Extension field for ``rank``."
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="role",
        title=(
            "Role that this diagnosis has within the episode of care (e.g. "
            "admission, billing, discharge \u2026)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``EpisodeOfCareDiagnosis`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "condition", "role", "rank"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``EpisodeOfCareDiagnosis`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "condition", "role", "rank"]


class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Past list of status codes (the current status may be included to cover the
    start date of the status).
    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """

    __resource_type__ = "EpisodeOfCareStatusHistory"

    period: fhirtypes.PeriodType = Field(  # type: ignore
        default=...,
        alias="period",
        title="Duration the EpisodeOfCare was in the specified status",
        description="The period during this EpisodeOfCare that the specific status applied.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title=(
            "planned | waitlist | active | onhold | finished | cancelled | entered-"
            "in-error"
        ),
        description="planned | waitlist | active | onhold | finished | cancelled.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "planned",
                "waitlist",
                "active",
                "onhold",
                "finished",
                "cancelled",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``EpisodeOfCareStatusHistory`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "status", "period"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``EpisodeOfCareStatusHistory`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

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
