# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImagingStudy(domainresource.DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).
    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """

    resource_type = Field("ImagingStudy", const=True)

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="List of `Reference` items referencing `CarePlan, ServiceRequest, Appointment, AppointmentResponse, Task` (represented as `dict` in JSON)",
        description="Request fulfilled",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Institution-generated description",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON)",
        description="Encounter with which this imaging study is associated",
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="List of `Reference` items referencing `Endpoint` (represented as `dict` in JSON)",
        description="Study access endpoint",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifiers for the whole study",
    )

    interpreter: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="interpreter",
        title="List of `Reference` items referencing `Practitioner, PractitionerRole` (represented as `dict` in JSON)",
        description="Who interpreted images",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Type `Reference` referencing `Location` (represented as `dict` in JSON)",
        description="Where ImagingStudy occurred",
    )

    modality: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="modality",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="All series modality if actual acquisition modalities",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="User-defined comments",
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfInstances",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Number of Study Related Instances",
    )

    numberOfSeries: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfSeries",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Number of Study Related Series",
    )

    procedureCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="procedureCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The performed procedure code",
    )

    procedureReference: fhirtypes.ReferenceType = Field(
        None,
        alias="procedureReference",
        title="Type `Reference` referencing `Procedure` (represented as `dict` in JSON)",
        description="The performed Procedure reference",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why the study was requested",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="List of `Reference` items referencing `Condition, Observation, Media, DiagnosticReport, DocumentReference` (represented as `dict` in JSON)",
        description="Why was study performed",
    )

    referrer: fhirtypes.ReferenceType = Field(
        None,
        alias="referrer",
        title="Type `Reference` referencing `Practitioner, PractitionerRole` (represented as `dict` in JSON)",
        description="Referring physician",
    )

    series: ListType[fhirtypes.ImagingStudySeriesType] = Field(
        None,
        alias="series",
        title="List of `ImagingStudySeries` items (represented as `dict` in JSON)",
        description="Each study has one or more series of instances",
    )

    started: fhirtypes.DateTime = Field(
        None,
        alias="started",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the study was started",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="registered | available | cancelled | entered-in-error | unknown",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Type `Reference` referencing `Patient, Device, Group` (represented as `dict` in JSON)",
        description="Who or what is the subject of the study",
    )


class ImagingStudySeries(backboneelement.BackboneElement):
    """ Each study has one or more series of instances.
    Each study has one or more series of images or other content.
    """

    resource_type = Field("ImagingStudySeries", const=True)

    bodySite: fhirtypes.CodingType = Field(
        None,
        alias="bodySite",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Body part examined",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="A short human readable summary of the series",
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="List of `Reference` items referencing `Endpoint` (represented as `dict` in JSON)",
        description="Series access endpoint",
    )

    instance: ListType[fhirtypes.ImagingStudySeriesInstanceType] = Field(
        None,
        alias="instance",
        title="List of `ImagingStudySeriesInstance` items (represented as `dict` in JSON)",
        description="A single SOP instance from the series",
    )

    laterality: fhirtypes.CodingType = Field(
        None,
        alias="laterality",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Body part laterality",
    )

    modality: fhirtypes.CodingType = Field(
        ...,
        alias="modality",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="The modality of the instances in the series",
    )

    number: fhirtypes.UnsignedInt = Field(
        None,
        alias="number",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Numeric identifier of this series",
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfInstances",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Number of Series Related Instances",
    )

    performer: ListType[fhirtypes.ImagingStudySeriesPerformerType] = Field(
        None,
        alias="performer",
        title="List of `ImagingStudySeriesPerformer` items (represented as `dict` in JSON)",
        description="Who performed the series",
    )

    specimen: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="specimen",
        title="List of `Reference` items referencing `Specimen` (represented as `dict` in JSON)",
        description="Specimen imaged",
    )

    started: fhirtypes.DateTime = Field(
        None,
        alias="started",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the series started",
    )

    uid: fhirtypes.Id = Field(
        ...,
        alias="uid",
        title="Type `Id` (represented as `dict` in JSON)",
        description="DICOM Series Instance UID for the series",
    )


class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """ A single SOP instance from the series.
    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """

    resource_type = Field("ImagingStudySeriesInstance", const=True)

    number: fhirtypes.UnsignedInt = Field(
        None,
        alias="number",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="The number of this instance in the series",
    )

    sopClass: fhirtypes.CodingType = Field(
        ...,
        alias="sopClass",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="DICOM class type",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of instance",
    )

    uid: fhirtypes.Id = Field(
        ...,
        alias="uid",
        title="Type `Id` (represented as `dict` in JSON)",
        description="DICOM SOP Instance UID",
    )


class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    """ Who performed the series.
    Indicates who or what performed the series and how they were involved.
    """

    resource_type = Field("ImagingStudySeriesPerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Organization, CareTeam, Patient, Device, RelatedPerson` (represented as `dict` in JSON)",
        description="Who performed the series",
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of performance",
    )
