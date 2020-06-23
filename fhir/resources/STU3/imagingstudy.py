# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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

    accession: fhirtypes.IdentifierType = Field(
        None,
        alias="accession",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description='Related workflow identifier ("Accession Number")',
    )

    availability: fhirtypes.Code = Field(
        None,
        alias="availability",
        title="Type `Code`",
        description="ONLINE | OFFLINE | NEARLINE | UNAVAILABLE",
    )
    availability__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_availability", title="Extension field for ``availability``."
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `ReferralRequest, CarePlan, "
            "ProcedureRequest` (represented as `dict` in JSON)"
        ),
        description="Request fulfilled",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title=(
            "Type `Reference` referencing `Encounter, EpisodeOfCare` (represented "
            "as `dict` in JSON)"
        ),
        description="Originating context",
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
        description="Other identifiers for the study",
    )

    interpreter: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="interpreter",
        title=(
            "List of `Reference` items referencing `Practitioner` (represented as "
            "`dict` in JSON)"
        ),
        description="Who interpreted images",
    )

    modalityList: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="modalityList",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="All series modality if actual acquisition modalities",
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

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who the images are of",
    )

    procedureCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="procedureCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The performed procedure code",
    )

    procedureReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="procedureReference",
        title=(
            "List of `Reference` items referencing `Procedure` (represented as "
            "`dict` in JSON)"
        ),
        description="The performed Procedure reference",
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why the study was requested",
    )

    referrer: fhirtypes.ReferenceType = Field(
        None,
        alias="referrer",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
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

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `Oid`",
        description="Formal DICOM identifier for the study",
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )


class ImagingStudySeries(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each study has one or more series of instances.
    Each study has one or more series of images or other content.
    """

    resource_type = Field("ImagingStudySeries", const=True)

    availability: fhirtypes.Code = Field(
        None,
        alias="availability",
        title="Type `Code`",
        description="ONLINE | OFFLINE | NEARLINE | UNAVAILABLE",
    )
    availability__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_availability", title="Extension field for ``availability``."
    )

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

    performer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="performer",
        title=(
            "List of `Reference` items referencing `Practitioner` (represented as "
            "`dict` in JSON)"
        ),
        description="Who performed the series",
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

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `Oid`",
        description="Formal DICOM identifier for this series",
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

    sopClass: fhirtypes.Oid = Field(
        ..., alias="sopClass", title="Type `Oid`", description="DICOM class type"
    )
    sopClass__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sopClass", title="Extension field for ``sopClass``."
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

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `Oid`",
        description="Formal DICOM identifier for this instance",
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )
