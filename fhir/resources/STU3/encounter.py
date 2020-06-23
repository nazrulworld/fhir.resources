# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Encounter
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Encounter(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An interaction during which services are provided to the patient.
    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """

    resource_type = Field("Encounter", const=True)

    account: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="account",
        title=(
            "List of `Reference` items referencing `Account` (represented as `dict`"
            " in JSON)"
        ),
        description="The set of accounts that may be used for billing for this Encounter",
    )

    appointment: fhirtypes.ReferenceType = Field(
        None,
        alias="appointment",
        title=(
            "Type `Reference` referencing `Appointment` (represented as `dict` in "
            "JSON)"
        ),
        description="The appointment that scheduled this encounter",
    )

    classHistory: ListType[fhirtypes.EncounterClassHistoryType] = Field(
        None,
        alias="classHistory",
        title="List of `EncounterClassHistory` items (represented as `dict` in JSON)",
        description="List of past encounter classes",
    )

    class_fhir: fhirtypes.CodingType = Field(
        None,
        alias="class",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="inpatient | outpatient | ambulatory | emergency +",
    )

    diagnosis: ListType[fhirtypes.EncounterDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of `EncounterDiagnosis` items (represented as `dict` in JSON)",
        description="The list of diagnosis relevant to this encounter",
    )

    episodeOfCare: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="episodeOfCare",
        title=(
            "List of `Reference` items referencing `EpisodeOfCare` (represented as "
            "`dict` in JSON)"
        ),
        description="Episode(s) of care that this encounter should be recorded against",
    )

    hospitalization: fhirtypes.EncounterHospitalizationType = Field(
        None,
        alias="hospitalization",
        title="Type `EncounterHospitalization` (represented as `dict` in JSON)",
        description="Details about the admission to a healthcare service",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifier(s) by which this encounter is known",
    )

    incomingReferral: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="incomingReferral",
        title=(
            "List of `Reference` items referencing `ReferralRequest` (represented "
            "as `dict` in JSON)"
        ),
        description="The ReferralRequest that initiated this encounter",
    )

    length: fhirtypes.DurationType = Field(
        None,
        alias="length",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Quantity of time the encounter lasted (less time absent)",
    )

    location: ListType[fhirtypes.EncounterLocationType] = Field(
        None,
        alias="location",
        title="List of `EncounterLocation` items (represented as `dict` in JSON)",
        description="List of locations where the patient has been",
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Another Encounter this encounter is part of",
    )

    participant: ListType[fhirtypes.EncounterParticipantType] = Field(
        None,
        alias="participant",
        title="List of `EncounterParticipant` items (represented as `dict` in JSON)",
        description="List of participants involved in the encounter",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The start and end time of the encounter",
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Indicates the urgency of the encounter",
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason the encounter takes place (code)",
    )

    serviceProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="serviceProvider",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="The custodian organization of this Encounter record",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description=(
            "planned | arrived | triaged | in-progress | onleave | finished | "
            "cancelled +"
        ),
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusHistory: ListType[fhirtypes.EncounterStatusHistoryType] = Field(
        None,
        alias="statusHistory",
        title="List of `EncounterStatusHistory` items (represented as `dict` in JSON)",
        description="List of past encounter statuses",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="The patient ro group present at the encounter",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Specific type of encounter",
    )


class EncounterClassHistory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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

    resource_type = Field("EncounterClassHistory", const=True)

    class_fhir: fhirtypes.CodingType = Field(
        ...,
        alias="class",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="inpatient | outpatient | ambulatory | emergency +",
    )

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The time that the episode was in the specified class",
    )


class EncounterDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The list of diagnosis relevant to this encounter.
    """

    resource_type = Field("EncounterDiagnosis", const=True)

    condition: fhirtypes.ReferenceType = Field(
        ...,
        alias="condition",
        title=(
            "Type `Reference` referencing `Condition, Procedure` (represented as "
            "`dict` in JSON)"
        ),
        description="Reason the encounter takes place (resource)",
    )

    rank: fhirtypes.PositiveInt = Field(
        None,
        alias="rank",
        title="Type `PositiveInt`",
        description="Ranking of the diagnosis (for each role type)",
    )
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rank", title="Extension field for ``rank``."
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Role that this diagnosis has within the encounter (e.g. admission, "
            "billing, discharge \u2026)"
        ),
    )


class EncounterHospitalization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details about the admission to a healthcare service.
    """

    resource_type = Field("EncounterHospitalization", const=True)

    admitSource: fhirtypes.CodeableConceptType = Field(
        None,
        alias="admitSource",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="From where patient was admitted (physician referral, transfer)",
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Location to which the patient is discharged",
    )

    dietPreference: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="dietPreference",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Diet preferences reported by the patient",
    )

    dischargeDisposition: fhirtypes.CodeableConceptType = Field(
        None,
        alias="dischargeDisposition",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Category or kind of location after discharge",
    )

    origin: fhirtypes.ReferenceType = Field(
        None,
        alias="origin",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="The location from which the patient came before admission",
    )

    preAdmissionIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="preAdmissionIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Pre-admission identifier",
    )

    reAdmission: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reAdmission",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The type of hospital re-admission that has occurred (if any). If the "
            "value is absent, then this is not identified as a readmission"
        ),
    )

    specialArrangement: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialArrangement",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Wheelchair, translator, stretcher, etc.",
    )

    specialCourtesy: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialCourtesy",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Special courtesies (VIP, board member)",
    )


class EncounterLocation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of locations where the patient has been.
    List of locations where  the patient has been during this encounter.
    """

    resource_type = Field("EncounterLocation", const=True)

    location: fhirtypes.ReferenceType = Field(
        ...,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Location the encounter takes place",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period during which the patient was present at the location",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description="planned | active | reserved | completed",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )


class EncounterParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of participants involved in the encounter.
    The list of people responsible for providing the service.
    """

    resource_type = Field("EncounterParticipant", const=True)

    individual: fhirtypes.ReferenceType = Field(
        None,
        alias="individual",
        title=(
            "Type `Reference` referencing `Practitioner, RelatedPerson` "
            "(represented as `dict` in JSON)"
        ),
        description="Persons involved in the encounter other than the patient",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period of time during the encounter that the participant participated",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Role of participant in encounter",
    )


class EncounterStatusHistory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    List of past encounter statuses.
    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """

    resource_type = Field("EncounterStatusHistory", const=True)

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The time that the episode was in the specified status",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description=(
            "planned | arrived | triaged | in-progress | onleave | finished | "
            "cancelled +"
        ),
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )
