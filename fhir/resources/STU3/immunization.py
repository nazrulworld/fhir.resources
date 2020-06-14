# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Immunization(domainresource.DomainResource):
    """ Immunization event information.
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    resource_type = Field("Immunization", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Vaccination administration date",
    )

    doseQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="doseQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of vaccine administered",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON)",
        description="Encounter administered as part of",
    )

    expirationDate: fhirtypes.Date = Field(
        None,
        alias="expirationDate",
        title="Type `Date` (represented as `dict` in JSON)",
        description="Vaccine expiration date",
    )

    explanation: fhirtypes.ImmunizationExplanationType = Field(
        None,
        alias="explanation",
        title="Type `ImmunizationExplanation` (represented as `dict` in JSON)",
        description="Administration/non-administration reasons",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Where vaccination occurred",
    )

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="Type `String` (represented as `dict` in JSON)",
        description="Vaccine lot number",
    )

    manufacturer: fhirtypes.ReferenceType = Field(
        None,
        alias="manufacturer",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Vaccine manufacturer",
    )

    notGiven: bool = Field(
        ...,
        alias="notGiven",
        title="Type `bool`",
        description="Flag for whether immunization was given",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Vaccination notes",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who was immunized",
    )

    practitioner: ListType[fhirtypes.ImmunizationPractitionerType] = Field(
        None,
        alias="practitioner",
        title="List of `ImmunizationPractitioner` items (represented as `dict` in JSON)",
        description="Who performed event",
    )

    primarySource: bool = Field(
        ...,
        alias="primarySource",
        title="Type `bool`",
        description="Indicates context the data was recorded in",
    )

    reaction: ListType[fhirtypes.ImmunizationReactionType] = Field(
        None,
        alias="reaction",
        title="List of `ImmunizationReaction` items (represented as `dict` in JSON)",
        description="Details of a reaction that follows immunization",
    )

    reportOrigin: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reportOrigin",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Indicates the source of a secondarily reported record",
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How vaccine entered body",
    )

    site: fhirtypes.CodeableConceptType = Field(
        None,
        alias="site",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Body site vaccine  was administered",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="completed | entered-in-error",
    )

    vaccinationProtocol: ListType[
        fhirtypes.ImmunizationVaccinationProtocolType
    ] = Field(
        None,
        alias="vaccinationProtocol",
        title="List of `ImmunizationVaccinationProtocol` items (represented as `dict` in JSON)",
        description="What protocol was followed",
    )

    vaccineCode: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="vaccineCode",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Vaccine product administered",
    )


class ImmunizationExplanation(backboneelement.BackboneElement):
    """ Administration/non-administration reasons.
    Reasons why a vaccine was or was not administered.
    """

    resource_type = Field("ImmunizationExplanation", const=True)

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why immunization occurred",
    )

    reasonNotGiven: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonNotGiven",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why immunization did not occur",
    )


class ImmunizationPractitioner(backboneelement.BackboneElement):
    """ Who performed event.
    Indicates who or what performed the event.
    """

    resource_type = Field("ImmunizationPractitioner", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON)",
        description="Individual who was performing",
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What type of performance was done",
    )


class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """

    resource_type = Field("ImmunizationReaction", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When reaction started",
    )

    detail: fhirtypes.ReferenceType = Field(
        None,
        alias="detail",
        title="Type `Reference` referencing `Observation` (represented as `dict` in JSON)",
        description="Additional information on reaction",
    )

    reported: bool = Field(
        None,
        alias="reported",
        title="Type `bool`",
        description="Indicates self-reported reaction",
    )


class ImmunizationVaccinationProtocol(backboneelement.BackboneElement):
    """ What protocol was followed.
    Contains information about the protocol(s) under which the vaccine was
    administered.
    """

    resource_type = Field("ImmunizationVaccinationProtocol", const=True)

    authority: fhirtypes.ReferenceType = Field(
        None,
        alias="authority",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Who is responsible for protocol",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Details of vaccine protocol",
    )

    doseSequence: fhirtypes.PositiveInt = Field(
        None,
        alias="doseSequence",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Dose number within series",
    )

    doseStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="doseStatus",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Indicates if dose counts towards immunity",
    )

    doseStatusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="doseStatusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why dose does (not) count",
    )

    series: fhirtypes.String = Field(
        None,
        alias="series",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of vaccine series",
    )

    seriesDoses: fhirtypes.PositiveInt = Field(
        None,
        alias="seriesDoses",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Recommended number of doses for immunity",
    )

    targetDisease: ListType[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="targetDisease",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Disease immunized against",
    )
