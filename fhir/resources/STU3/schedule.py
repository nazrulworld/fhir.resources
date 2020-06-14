# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Schedule
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class Schedule(domainresource.DomainResource):
    """ A container for slots of time that may be available for booking
    appointments.
    """

    resource_type = Field("Schedule", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this schedule is in active use",
    )

    actor: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="actor",
        title="List of `Reference` items referencing `Patient, Practitioner, PractitionerRole, RelatedPerson, Device, HealthcareService, Location` (represented as `dict` in JSON)",
        description="The resource this Schedule resource is providing availability information for. These are expected to usually be one of HealthcareService, Location, Practitioner, PractitionerRole, Device, Patient or RelatedPerson",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Comments on the availability to describe any extended information. Such as custom constraints on the slots that may be associated",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Ids for this item",
    )

    planningHorizon: fhirtypes.PeriodType = Field(
        None,
        alias="planningHorizon",
        title="Type `Period` (represented as `dict` in JSON)",
        description='The period of time that the slots that are attached to this Schedule resource cover (even if none exist). These  cover the amount of time that an organization\u0027s planning horizon; the interval for which they are currently accepting appointments. This does not define a "template" for planning outside these dates',
    )

    serviceCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="serviceCategory",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="A broad categorisation of the service that is to be performed during this appointment",
    )

    serviceType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The specific service that is to be performed during this appointment",
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The specialty of a practitioner that would be required to perform the service requested in this appointment",
    )
