# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Immunization(DomainResource):
    """Immunization event information.

    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    resource_type = Field("Immunization", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="Vaccination administration date.",
    )
    doseQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="doseQuantity",
        title="Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON).",
        description="Amount of vaccine administered.",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON).",
        description="Encounter administered as part of.",
    )

    expirationDate: fhirtypes.Date = Field(
        None,
        alias="expirationDate",
        title="Type `Date`",
        description="Vaccine expiration date.",
    )

    explanation: fhirtypes.ImmunizationExplanationType = Field(
        None,
        alias="explanation",
        title="Type `ImmunizationExplanation` (represented as `dict` in JSON).",
        description="Administration/non-administration reasons.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Business identifier.",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON).",
        description="Where vaccination occurred.",
    )
    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Vaccine manufacturer.",
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Who was immunized.",
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON).",
        description="Who administered vaccine.",
    )

    requester: fhirtypes.ReferenceType = Field(
        None,
        alias="requester",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON).",
        description="Who ordered vaccination.",
    )

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="Type `String`.",
        description="Vaccine lot number.",
    )

    reported: fhirtypes.Boolean = Field(
        None,
        alias="reported",
        title="Type `Boolean`.",
        description="Indicates a self-reported record.",
    )

    wasNotGiven: fhirtypes.Boolean = Field(
        None,
        alias="wasNotGiven",
        title="Type `Boolean`.",
        description="Flag for whether immunization was given.",
    )
    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`.",
        description="in-progress | on-hold | completed | entered-in-error | stopped.",
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="How vaccine entered body.",
    )

    site: fhirtypes.CodeableConceptType = Field(
        None,
        alias="site",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Body site vaccine  was administered.",
    )

    vaccineCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="vaccineCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Vaccine product administered.",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON).",
        description="Vaccination notes.",
    )
    reaction: ListType[fhirtypes.ImmunizationReactionType] = Field(
        None,
        alias="reaction",
        title="List of `ImmunizationReaction` items (represented as `dict` in JSON).",
        description="Details of a reaction that follows immunization.",
    )

    vaccinationProtocol: ListType[
        fhirtypes.ImmunizationVaccinationProtocolType
    ] = Field(
        None,
        alias="vaccinationProtocol",
        title=(
            "List of `ImmunizationVaccinationProtocol` "
            "items (represented as `dict` in JSON)."
        ),
        description="What protocol was followed.",
    )


class ImmunizationExplanation(BackboneElement):
    """Administration/non-administration reasons.

    Reasons why a vaccine was or was not administered.
    """

    resource_type = Field("ImmunizationExplanation", const=True)

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Why immunization occurred.",
    )

    reasonNotGiven: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonNotGiven",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Why immunization did not occur.",
    )


class ImmunizationReaction(BackboneElement):
    """Details of a reaction that follows immunization.

    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """

    resource_type = Field("ImmunizationReaction", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="When reaction started.",
    )
    detail: fhirtypes.ReferenceType = Field(
        None,
        alias="detail",
        title="Type `Reference` referencing `Observation` (represented as `dict` in JSON).",
        description="Additional information on reaction.",
    )

    reported: fhirtypes.Boolean = Field(
        None,
        alias="reported",
        title="Type `Boolean`",
        description="Indicates self-reported reaction.",
    )


class ImmunizationVaccinationProtocol(BackboneElement):
    """What protocol was followed.

    Contains information about the protocol(s) under which the vaccine was
    administered.
    """

    resource_type = Field("ImmunizationVaccinationProtocol", const=True)

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON).",
        description="Who is responsible for protocol.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`.",
        description="Details of vaccine protocol.",
    )

    doseSequence: fhirtypes.PositiveInt = Field(
        None,
        alias="doseSequence",
        title="Type `Interger`.",
        description="Dose number within series.",
    )
    doseStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="doseStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Indicates if dose counts towards immunity.",
    )

    doseStatusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="doseStatusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Why dose does (not) count.",
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Type `String`.",
        description="Name of vaccine series.",
    )
    seriesDoses: fhirtypes.PositiveInt = Field(
        None,
        alias="seriesDoses",
        title="Type `Integer`.",
        description="Recommended number of doses for immunity.",
    )

    targetDisease: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="targetDisease",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Disease immunized against.",
    )
