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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of images produced in single study (one or more series of references
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
        title=(
            "List of `Reference` items referencing `CarePlan, ServiceRequest, "
            "Appointment, AppointmentResponse, Task` (represented as `dict` in "
            "JSON)"
        ),
        description="Request fulfilled",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Institution-generated description",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Encounter with which this imaging study is associated",
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "List of `Reference` items referencing `Endpoint` (represented as "
            "`dict` in JSON)"
        ),
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
        title=(
            "List of `Reference` items referencing `Practitioner, PractitionerRole`"
            " (represented as `dict` in JSON)"
        ),
        description="Who interpreted images",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
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
        title="Type `UnsignedInt`",
        description="Number of Study Related Instances",
    )
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfInstances",
        title="Extension field for ``numberOfInstances``.",
    )

    numberOfSeries: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfSeries",
        title="Type `UnsignedInt`",
        description="Number of Study Related Series",
    )
    numberOfSeries__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfSeries", title="Extension field for ``numberOfSeries``."
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
        title=(
            "Type `Reference` referencing `Procedure` (represented as `dict` in "
            "JSON)"
        ),
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
        title=(
            "List of `Reference` items referencing `Condition, Observation, Media, "
            "DiagnosticReport, DocumentReference` (represented as `dict` in JSON)"
        ),
        description="Why was study performed",
    )

    referrer: fhirtypes.ReferenceType = Field(
        None,
        alias="referrer",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
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
        title="Type `DateTime`",
        description="When the study was started",
    )
    started__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_started", title="Extension field for ``started``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="registered | available | cancelled | entered-in-error | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Device, Group` (represented as "
            "`dict` in JSON)"
        ),
        description="Who or what is the subject of the study",
    )


class ImagingStudySeries(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each study has one or more series of instances.
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
        title="Type `String`",
        description="A short human readable summary of the series",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "List of `Reference` items referencing `Endpoint` (represented as "
            "`dict` in JSON)"
        ),
        description="Series access endpoint",
    )

    instance: ListType[fhirtypes.ImagingStudySeriesInstanceType] = Field(
        None,
        alias="instance",
        title=(
            "List of `ImagingStudySeriesInstance` items (represented as `dict` in "
            "JSON)"
        ),
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
        title="Type `UnsignedInt`",
        description="Numeric identifier of this series",
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfInstances",
        title="Type `UnsignedInt`",
        description="Number of Series Related Instances",
    )
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfInstances",
        title="Extension field for ``numberOfInstances``.",
    )

    performer: ListType[fhirtypes.ImagingStudySeriesPerformerType] = Field(
        None,
        alias="performer",
        title=(
            "List of `ImagingStudySeriesPerformer` items (represented as `dict` in "
            "JSON)"
        ),
        description="Who performed the series",
    )

    specimen: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="specimen",
        title=(
            "List of `Reference` items referencing `Specimen` (represented as "
            "`dict` in JSON)"
        ),
        description="Specimen imaged",
    )

    started: fhirtypes.DateTime = Field(
        None,
        alias="started",
        title="Type `DateTime`",
        description="When the series started",
    )
    started__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_started", title="Extension field for ``started``."
    )

    uid: fhirtypes.Id = Field(
        ...,
        alias="uid",
        title="Type `Id`",
        description="DICOM Series Instance UID for the series",
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )


class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single SOP instance from the series.
    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """

    resource_type = Field("ImagingStudySeriesInstance", const=True)

    number: fhirtypes.UnsignedInt = Field(
        None,
        alias="number",
        title="Type `UnsignedInt`",
        description="The number of this instance in the series",
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
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
        title="Type `String`",
        description="Description of instance",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    uid: fhirtypes.Id = Field(
        ..., alias="uid", title="Type `Id`", description="DICOM SOP Instance UID"
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )


class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed the series.
    Indicates who or what performed the series and how they were involved.
    """

    resource_type = Field("ImagingStudySeriesPerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "Organization, CareTeam, Patient, Device, RelatedPerson` (represented "
            "as `dict` in JSON)"
        ),
        description="Who performed the series",
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of performance",
    )
