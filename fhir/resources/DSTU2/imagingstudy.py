# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/imagingstudy.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImagingStudy(domainresource.DomainResource):
    """A set of images produced in single study (one or more series of references
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
        title="Type `Identifier` (represented as `dict` in JSON).",
        description='Related workflow identifier ("Accession Number").',
    )

    availability: fhirtypes.Code = Field(
        None,
        alias="availability",
        title="ONLINE | OFFLINE | NEARLINE | UNAVAILABLE (0008,0056)",
        description="Type `str`.",
        enum_values=["ONLINE", "OFFLINE", "NEARLINE", "UNAVAILABLE"],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Institution-generated description",
        description=(
            "The Imaging Manager description of the study. Institution-generated "
            "description or classification of the Study (component) performed."
        ),
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifiers for the whole study",
        description=(
            "Identifiers for the ImagingStudy such as DICOM Study Instance UID, and"
            " Accession Number."
        ),
    )

    interpreter: fhirtypes.ReferenceType = Field(
        None,
        alias="interpreter",
        title="Who interpreted images",
        description="Who read the study and interpreted the images or other content.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    modalityList: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="modalityList",
        title="All series modality if actual acquisition modalities",
        description=(
            "A list of all the series.modality values that are actual acquisition "
            "modalities, i.e. those in the DICOM Context Group 29 (value set OID "
            "1.2.840.10008.6.1.19)."
        ),
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        ...,
        alias="numberOfInstances",
        title="Number of Study Related Instances",
        description=(
            "Number of SOP Instances in Study. This value given may be larger than "
            "the number of instance elements this resource contains due to resource"
            " availability, security, or other factors. This element should be "
            "present if any instance elements are present."
        ),
    )

    numberOfSeries: fhirtypes.UnsignedInt = Field(
        ...,
        alias="numberOfSeries",
        title="Number of Study Related Series",
        description=(
            "Number of Series in the Study. This value given may be larger than the"
            " number of series elements this Resource contains due to resource "
            "availability, security, or other factors. This element should be "
            "present if any series elements are present."
        ),
    )

    order: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="order",
        title=(
            "List of `Reference` items referencing `DiagnosticOrder` (represented as "
            "`dict` in JSON)."
        ),
        description="Order(s) that caused this study to be performed.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DiagnosticOrder"],
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Who the images are of.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    procedure: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="procedure",
        title="The performed Procedure reference",
        description="The procedure which this ImagingStudy was part of.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    referrer: fhirtypes.ReferenceType = Field(
        None,
        alias="referrer",
        title="Referring physician",
        description="The requesting/referring physician.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    series: ListType[fhirtypes.ImagingStudySeriesType] = Field(
        None,
        alias="series",
        title="Each study has one or more series of instances",
        description="Each study has one or more series of images or other content.",
    )

    started: fhirtypes.DateTime = Field(
        None,
        alias="started",
        title="When the study was started",
        description="Date and time the study started.",
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `str`",
        description="Formal identifier for the study.",
    )

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="Type `str`",
        description="Retrieve URI.",
    )


class ImagingStudySeries(backboneelement.BackboneElement):
    """Each study has one or more series of instances.

    Each study has one or more series of images or other content.
    """

    resource_type = Field("ImagingStudySeries", const=True)

    availability: fhirtypes.Code = Field(
        None,
        alias="availability",
        title="ONLINE | OFFLINE | NEARLINE | UNAVAILABLE.",
        description="Type `str`.",
        enum_values=["ONLINE", "OFFLINE", "NEARLINE", "UNAVAILABLE"],
    )

    bodySite: fhirtypes.CodingType = Field(
        None,
        alias="bodySite",
        title="Body part examined",
        description=(
            "The anatomic structures examined. See DICOM Part 16 Annex L (http://di"
            "com.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html)"
            " for DICOM to SNOMED-CT mappings. The bodySite may indicate the "
            "laterality of body part imaged; if so, it shall be consistent with any"
            " content of ImagingStudy.series.laterality."
        ),
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="A short human readable summary of the series",
        description="A description of the series.",
    )

    instance: ListType[fhirtypes.ImagingStudySeriesInstanceType] = Field(
        None,
        alias="instance",
        title="A single SOP instance from the series",
        description=(
            "A single SOP instance within the series, e.g. an image, or "
            "presentation state."
        ),
    )

    laterality: fhirtypes.CodingType = Field(
        None,
        alias="laterality",
        title="Body part laterality",
        description=(
            "The laterality of the (possibly paired) anatomic structures examined. "
            "E.g., the left knee, both lungs, or unpaired abdomen. If present, "
            "shall be consistent with any laterality information indicated in "
            "ImagingStudy.series.bodySite."
        ),
    )

    modality: fhirtypes.CodingType = Field(
        ...,
        alias="modality",
        title="The modality of the instances in the series",
        description="The modality of this series sequence.",
    )

    number: fhirtypes.UnsignedInt = Field(
        None,
        alias="number",
        title="Numeric identifier of this series",
        description="The numeric identifier of this series in the study.",
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        ...,
        alias="numberOfInstances",
        title="Number of Series Related Instances",
        description=(
            "Number of SOP Instances in the Study. The value given may be larger "
            "than the number of instance elements this resource contains due to "
            "resource availability, security, or other factors. This element should"
            " be present if any instance elements are present."
        ),
    )

    started: fhirtypes.DateTime = Field(
        None,
        alias="started",
        title="When the series started",
        description="The date and time the series was started.",
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="DICOM Series Instance UID for the series",
        description="The DICOM Series Instance UID for the series.",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `str`.",
        description="Location of the referenced instance(s).",
    )


class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """A single SOP instance from the series.

    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """

    resource_type = Field("ImagingStudySeriesInstance", const=True)

    content: ListType[fhirtypes.AttachmentType] = Field(
        None,
        alias="content",
        title="List of `Attachment` items (represented as `dict` in JSON).",
        description="Content of the instance.",
    )

    number: fhirtypes.UnsignedInt = Field(
        None,
        alias="number",
        title="The number of this instance in the series",
        description="The number of instance in the series.",
    )

    sopClass: fhirtypes.Oid = Field(
        ...,
        alias="sopClass",
        title="DICOM class type",
        description="DICOM instance  type.",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Description of instance",
        description="The description of the instance.",
    )

    type: fhirtypes.String = Field(
        None,
        alias="type",
        title="Type `str`.",
        description="Type of instance (image etc.).",
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="DICOM SOP Instance UID",
        description="The DICOM SOP Instance UID for this image or other DICOM content.",
    )
