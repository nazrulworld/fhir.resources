# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Encounter
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Encounter(DomainResource):
    """An interaction during which services are provided to the patient.

    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """

    resource_type = Field("Encounter", const=True)

    class_fhir: fhirtypes.Code = Field(
        None,
        alias="class",
        title="Type `Code`.",
        description="inpatient | outpatient | ambulatory | emergency +.",
    )
    length: fhirtypes.DurationType = Field(
        None,
        alias="length",
        title="length",
        description="Duration of time the encounter lasted (less time absent).",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description="The start and end time of the encounter.",
    )
    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON).",
        description="Another Encounter this encounter is part of.",
    )
    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="The patient present at the encounter.",
    )
    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Indicates the urgency of the encounter.",
    )
    serviceProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="serviceProvider",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="The custodian organization of this Encounter record.",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`.",
        description="planned | arrived | in-progress | onleave | finished | cancelled.",
    )

    appointment: fhirtypes.ReferenceType = Field(
        None,
        alias="appointment",
        title="Type `Reference` referencing `Appointment` (represented as `dict` in JSON).",
        description="The appointment that scheduled this encounter.",
    )

    episodeOfCare: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="episodeOfCare",
        title=(
            "List of `Reference` items referencing `EpisodeOfCare`"
            " (represented as `dict` in JSON)."
        ),
        description="Episode(s) of care that this encounter should be recorded against.",
    )

    hospitalization: fhirtypes.EncounterHospitalizationType = Field(
        None,
        alias="hospitalization",
        title="Type `EncounterHospitalization` (represented as `dict` in JSON).",
        description="Details about the admission to a healthcare service.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Identifier(s) by which this encounter is known.",
    )

    incomingReferral: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="incomingReferral",
        title=(
            "List of `Reference` items referencing `ReferralRequest`"
            " (represented as `dict` in JSON)."
        ),
        description="The ReferralRequest that initiated this encounter.",
    )

    indication: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="indication",
        title=(
            "List of `Reference` items referencing `Condition, "
            "Procedure` (represented as `dict` in JSON)."
        ),
        description="Reason the encounter takes place (resource).",
    )

    location: ListType[fhirtypes.EncounterLocationType] = Field(
        None,
        alias="location",
        title="List of `EncounterLocation` items  (represented as `dict` in JSON).",
        description="List of locations where the patient has been.",
    )

    participant: ListType[fhirtypes.EncounterParticipantType] = Field(
        None,
        alias="participant",
        title="List of `EncounterParticipant` items  (represented as `dict` in JSON).",
        description="List of participants involved in the encounter.",
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items  (represented as `dict` in JSON).",
        description="Reason the encounter takes place (code).",
    )

    statusHistory: ListType[fhirtypes.EncounterStatusHistoryType] = Field(
        None,
        alias="statusHistory",
        title="List of `EncounterStatusHistory` items  (represented as `dict` in JSON).",
        description="List of past encounter statuses.",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items  (represented as `dict` in JSON).",
        description="Specific type of encounter.",
    )


class EncounterHospitalization(BackboneElement):
    """Details about the admission to a healthcare service."""

    resource_type = Field("EncounterHospitalization", const=True)

    admitSource: fhirtypes.CodeableConceptType = Field(
        None,
        alias="admitSource",
        title="Type `CodeableConcept`  (represented as `dict` in JSON).",
        description="Specific type of encounter.",
    )

    admittingDiagnosis: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="admittingDiagnosis",
        title=(
            "List of `Reference` items referencing "
            "`Condition` (represented as `dict` in JSON)."
        ),
        description="The admitting diagnosis as reported by admitting practitioner.",
    )
    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON).",
        description="Location to which the patient is discharged.",
    )

    dietPreference: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="dietPreference",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Diet preferences reported by the patient.",
    )

    dischargeDiagnosis: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="dischargeDiagnosis",
        title=(
            "List of `Reference` items referencing "
            "`Condition` (represented as `dict` in JSON)."
        ),
        description=(
            "The final diagnosis given a patient before "
            "release from the hospital after all testing, "
            "surgery, and workup are complete."
        ),
    )

    dischargeDisposition: fhirtypes.CodeableConceptType = Field(
        None,
        alias="dischargeDisposition",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Category or kind of location after discharge.",
    )
    origin: fhirtypes.ReferenceType = Field(
        None,
        alias="origin",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON).",
        description="The location from which the patient came before admission",
    )
    preAdmissionIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="preAdmissionIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON).",
        description="Pre-admission identifier.",
    )

    reAdmission: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reAdmission",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description=(
            "The type of hospital re-admission that has occurred (if any). If"
            "the value is absent, then this is not identified as a readmission."
        ),
    )
    specialArrangement: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialArrangement",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Wheelchair, translator, stretcher, etc.",
    )
    specialCourtesy: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialCourtesy",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Special courtesies (VIP, board member).",
    )


class EncounterLocation(BackboneElement):
    """List of locations where the patient has been.

    List of locations where  the patient has been during this encounter.
    """

    resource_type = Field("EncounterLocation", const=True)

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON).",
        description="Location the encounter takes place.",
    )
    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Time period during which the patient was present at the location.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`.",
        description="planned | active | reserved | completed.",
    )


class EncounterParticipant(BackboneElement):
    """List of participants involved in the encounter.

    The list of people responsible for providing the service.
    """

    resource_type = Field("EncounterParticipant", const=True)

    individual: fhirtypes.ReferenceType = Field(
        None,
        alias="individual",
        title=(
            "Type `Reference` referencing `Practitioner, "
            "RelatedPerson` (represented as `dict` in JSON)."
        ),
        description="Persons involved in the encounter other than the patient.",
    )
    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Period of time during the encounter participant was present.",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Role of participant in encounter.",
    )


class EncounterStatusHistory(BackboneElement):
    """List of past encounter statuses.

    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """

    resource_type = Field("EncounterStatusHistory", const=True)

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description="The time that the episode was in the specified status.",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`.",
        description="planned | arrived | in-progress | onleave | finished | cancelled.",
    )
