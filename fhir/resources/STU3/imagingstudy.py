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
    """ A set of images produced in single study (one or more series of references
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="ONLINE | OFFLINE | NEARLINE | UNAVAILABLE",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Institution-generated description",
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
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Number of Study Related Instances",
    )

    numberOfSeries: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfSeries",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Number of Study Related Series",
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
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the study was started",
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `Oid` (represented as `dict` in JSON)",
        description="Formal DICOM identifier for the study",
    )


class ImagingStudySeries(backboneelement.BackboneElement):
    """ Each study has one or more series of instances.
    Each study has one or more series of images or other content.
    """

    resource_type = Field("ImagingStudySeries", const=True)

    availability: fhirtypes.Code = Field(
        None,
        alias="availability",
        title="Type `Code` (represented as `dict` in JSON)",
        description="ONLINE | OFFLINE | NEARLINE | UNAVAILABLE",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="A short human readable summary of the series",
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
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Numeric identifier of this series",
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfInstances",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Number of Series Related Instances",
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
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the series started",
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `Oid` (represented as `dict` in JSON)",
        description="Formal DICOM identifier for this series",
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

    sopClass: fhirtypes.Oid = Field(
        ...,
        alias="sopClass",
        title="Type `Oid` (represented as `dict` in JSON)",
        description="DICOM class type",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of instance",
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `Oid` (represented as `dict` in JSON)",
        description="Formal DICOM identifier for this instance",
    )
