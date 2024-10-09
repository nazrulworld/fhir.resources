from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Encounter
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Encounter(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An interaction during which services are provided to the patient.
    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """

    __resource_type__ = "Encounter"

    account: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="account",
        title="The set of accounts that may be used for billing for this Encounter",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Account"],
        },
    )

    appointment: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="appointment",
        title="The appointment that scheduled this encounter",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Appointment"],
        },
    )

    classHistory: typing.List[fhirtypes.EncounterClassHistoryType] | None = Field(  # type: ignore
        None,
        alias="classHistory",
        title="List of past encounter classes",
        description=(
            "The class history permits the tracking of the encounters transitions "
            "without needing to go  through the resource history.  This would be "
            "used for a case where an admission starts of as an emergency "
            "encounter, then transisions into an inpatient scenario. Doing this and"
            " not restarting a new encounter ensures that any lab/diagnostic "
            "results can more easily follow the patient and not require re-"
            "processing and not get lost or cancelled during a kindof discharge "
            "from emergency to inpatient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    class_fhir: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="class",
        title="inpatient | outpatient | ambulatory | emergency +",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    diagnosis: typing.List[fhirtypes.EncounterDiagnosisType] | None = Field(  # type: ignore
        None,
        alias="diagnosis",
        title="The list of diagnosis relevant to this encounter",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    episodeOfCare: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="episodeOfCare",
        title="Episode(s) of care that this encounter should be recorded against",
        description=(
            "Where a specific encounter should be classified as a part of a "
            "specific episode(s) of care this field should be used. This "
            "association can facilitate grouping of related encounters together for"
            " a specific purpose, such as government reporting, issue tracking, "
            "association via a common problem.  The association is recorded on the "
            "encounter as these are typically created after the episode of care, "
            "and grouped on entry rather than editing the episode of care to append"
            " another encounter to it (the episode of care could span years)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["EpisodeOfCare"],
        },
    )

    hospitalization: fhirtypes.EncounterHospitalizationType | None = Field(  # type: ignore
        None,
        alias="hospitalization",
        title="Details about the admission to a healthcare service",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifier(s) by which this encounter is known",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    incomingReferral: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="incomingReferral",
        title="The ReferralRequest that initiated this encounter",
        description="The referral request this encounter satisfies (incoming referral).",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ReferralRequest"],
        },
    )

    length: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="length",
        title="Quantity of time the encounter lasted (less time absent)",
        description=(
            "Quantity of time the encounter lasted. This excludes the time during "
            "leaves of absence."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    location: typing.List[fhirtypes.EncounterLocationType] | None = Field(  # type: ignore
        None,
        alias="location",
        title="List of locations where the patient has been",
        description="List of locations where  the patient has been during this encounter.",
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Another Encounter this encounter is part of",
        description=(
            "Another Encounter of which this encounter is a part of "
            "(administratively or in time)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    participant: typing.List[fhirtypes.EncounterParticipantType] | None = Field(  # type: ignore
        None,
        alias="participant",
        title="List of participants involved in the encounter",
        description="The\u00a0list of\u00a0people\u00a0responsible for providing the service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="The start and end time of the encounter",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    priority: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="Indicates the urgency of the encounter",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Reason the encounter takes place (code)",
        description=(
            "Reason the encounter takes place, expressed as a code. For admissions,"
            " this can be used for a coded admission diagnosis."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    serviceProvider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="serviceProvider",
        title="The custodian organization of this Encounter record",
        description=(
            "An organization that is in charge of maintaining the information of "
            "this Encounter (e.g. who maintains the report or the master service "
            "catalog item, etc.). This MAY be the same as the organization on the "
            "Patient record, however it could be different. This MAY not be not the"
            " Service Delivery Location's Organization."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "planned | arrived | triaged | in-progress | onleave | finished | "
            "cancelled +"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "planned",
                "arrived",
                "triaged",
                "in-progress",
                "onleave",
                "finished",
                "cancelled",
                "+",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    statusHistory: typing.List[fhirtypes.EncounterStatusHistoryType] | None = Field(  # type: ignore
        None,
        alias="statusHistory",
        title="List of past encounter statuses",
        description=(
            "The status history permits the encounter resource to contain the "
            "status history without needing to read through the historical versions"
            " of the resource, or even have the server store them."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="The patient ro group present at the encounter",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Specific type of encounter",
        description=(
            "Specific type of encounter (e.g. e-mail consultation, surgical day-"
            "care, skilled nursing, rehabilitation)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Encounter`` according specification,
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
            "statusHistory",
            "class",
            "classHistory",
            "type",
            "priority",
            "subject",
            "episodeOfCare",
            "incomingReferral",
            "participant",
            "appointment",
            "period",
            "length",
            "reason",
            "diagnosis",
            "account",
            "hospitalization",
            "location",
            "serviceProvider",
            "partOf",
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


class EncounterClassHistory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of past encounter classes.
    The class history permits the tracking of the encounters transitions
    without needing to go  through the resource history.

    This would be used for a case where an admission starts of as an emergency
    encounter, then transisions into an inpatient scenario. Doing this and not
    restarting a new encounter ensures that any lab/diagnostic results can more
    easily follow the patient and not require re-processing and not get lost or
    cancelled during a kindof discharge from emergency to inpatient.
    """

    __resource_type__ = "EncounterClassHistory"

    class_fhir: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="class",
        title="inpatient | outpatient | ambulatory | emergency +",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType = Field(  # type: ignore
        ...,
        alias="period",
        title="The time that the episode was in the specified class",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterClassHistory`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "class", "period"]


class EncounterDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The list of diagnosis relevant to this encounter.
    """

    __resource_type__ = "EncounterDiagnosis"

    condition: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="condition",
        title="Reason the encounter takes place (resource)",
        description=(
            "Reason the encounter takes place, as specified using information from "
            "another resource. For admissions, this is the admission diagnosis. The"
            " indication will typically be a Condition (with other resources "
            "referenced in the evidence.detail), or a Procedure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Procedure"],
        },
    )

    rank: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="rank",
        title="Ranking of the diagnosis (for each role type)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_rank", title="Extension field for ``rank``."
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="role",
        title=(
            "Role that this diagnosis has within the encounter (e.g. admission, "
            "billing, discharge \u2026)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterDiagnosis`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "condition", "role", "rank"]


class EncounterHospitalization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details about the admission to a healthcare service.
    """

    __resource_type__ = "EncounterHospitalization"

    admitSource: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="admitSource",
        title="From where patient was admitted (physician referral, transfer)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    destination: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="destination",
        title="Location to which the patient is discharged",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    dietPreference: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="dietPreference",
        title="Diet preferences reported by the patient",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    dischargeDisposition: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="dischargeDisposition",
        title="Category or kind of location after discharge",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    origin: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="origin",
        title="The location from which the patient came before admission",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    preAdmissionIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="preAdmissionIdentifier",
        title="Pre-admission identifier",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    reAdmission: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="reAdmission",
        title=(
            "The type of hospital re-admission that has occurred (if any). If the "
            "value is absent, then this is not identified as a readmission"
        ),
        description="Whether this hospitalization is a readmission and why if known.",
        json_schema_extra={
            "element_property": True,
        },
    )

    specialArrangement: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="specialArrangement",
        title="Wheelchair, translator, stretcher, etc.",
        description=(
            "Any special requests that have been made for this hospitalization "
            "encounter, such as the provision of specific equipment or other "
            "things."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    specialCourtesy: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="specialCourtesy",
        title="Special courtesies (VIP, board member)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterHospitalization`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "preAdmissionIdentifier",
            "origin",
            "admitSource",
            "reAdmission",
            "dietPreference",
            "specialCourtesy",
            "specialArrangement",
            "destination",
            "dischargeDisposition",
        ]


class EncounterLocation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of locations where the patient has been.
    List of locations where  the patient has been during this encounter.
    """

    __resource_type__ = "EncounterLocation"

    location: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="location",
        title="Location the encounter takes place",
        description="The location where the encounter takes place.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Time period during which the patient was present at the location",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="planned | active | reserved | completed",
        description=(
            "The status of the participants' presence at the specified location "
            "during the period specified. If the participant is is no longer at the"
            " location, then the period will have an end date/time."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["planned", "active", "reserved", "completed"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterLocation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "location", "status", "period"]


class EncounterParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of participants involved in the encounter.
    The list of people responsible for providing the service.
    """

    __resource_type__ = "EncounterParticipant"

    individual: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="individual",
        title="Persons involved in the encounter other than the patient",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "RelatedPerson"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Period of time during the encounter that the participant participated",
        description=(
            "The period of time that the specified participant participated in the "
            "encounter. These can overlap or be sub-sets of the overall encounter's"
            " period."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Role of participant in encounter",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "period", "individual"]


class EncounterStatusHistory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of past encounter statuses.
    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """

    __resource_type__ = "EncounterStatusHistory"

    period: fhirtypes.PeriodType = Field(  # type: ignore
        ...,
        alias="period",
        title="The time that the episode was in the specified status",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title=(
            "planned | arrived | triaged | in-progress | onleave | finished | "
            "cancelled +"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "planned",
                "arrived",
                "triaged",
                "in-progress",
                "onleave",
                "finished",
                "cancelled",
                "+",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EncounterStatusHistory`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "status", "period"]

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
