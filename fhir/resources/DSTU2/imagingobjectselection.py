# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/imagingobjectselection.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class ImagingObjectSelection(DomainResource):
    """Key Object Selection.

    A manifest of a set of DICOM Service-Object Pair Instances (SOP Instances).
    The referenced SOP Instances (images or other content) are for a single
    patient, and may be from one or more studies. The referenced SOP Instances
    have been selected for a purpose, such as quality assurance, conference, or
    consult. Reflecting that range of purposes, typical ImagingObjectSelection
    resources may include all SOP Instances in a study (perhaps for sharing
    through a Health Information Exchange); key images from multiple studies
    (for reference by a referring or treating physician); a multi-frame
    ultrasound instance ("cine" video clip) and a set of measurements taken
    from that instance (for inclusion in a teaching file); and so on.
    """

    resource_type = "ImagingObjectSelection"

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Practitioner, Device, Organization, "
            "Patient, RelatedPerson` (represented as `dict` in JSON)."
        ),
        description="Author (human or machine).",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Device",
            "Organization",
            "Patient",
            "RelatedPerson",
        ],
    )

    authoringTime: fhirtypes.DateTime = Field(
        None,
        alias="authoringTime",
        title="Type `DateTime` (represented as `str` in JSON).",
        description="Authoring time of the selection.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `str`.",
        description="Description text.",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON).",
        description="Patient of the selected objects.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    study: ListType[fhirtypes.ImagingObjectSelectionStudyType] = Field(
        ...,
        alias="study",
        title=(
            "List of `ImagingObjectSelectionStudy` items (represented as `dict` in "
            "JSON)."
        ),
        description="Study identity of the selected instances.",
    )

    title: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="title",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Reason for selection.",
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `Oid`.",
        description="Instance UID.",
    )


class ImagingObjectSelectionStudy(BackboneElement):
    """Study identity of the selected instances.

    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """

    resource_type = "ImagingObjectSelectionStudy"

    imagingStudy: fhirtypes.ReferenceType = Field(
        None,
        alias="imagingStudy",
        title=(
            "Type `Reference` referencing `ImagingStudy` (represented as `dict` in "
            "JSON)."
        ),
        description="Reference to ImagingStudy.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ImagingStudy"],
    )

    series: ListType[fhirtypes.ImagingObjectSelectionStudySeriesType] = Field(
        ...,
        alias="series",
        title=(
            "List of `ImagingObjectSelectionStudySeries` items (represented as `dict` "
            "in JSON)."
        ),
        description="Series identity of the selected instances.",
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `Oid`.",
        description="Study instance UID.",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`.",
        description="Retrieve study URL.",
    )


class ImagingObjectSelectionStudySeries(BackboneElement):
    """Series identity of the selected instances.

    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """

    resource_type = "ImagingObjectSelectionStudySeries"

    instance: ListType[fhirtypes.ImagingObjectSelectionStudySeriesInstanceType] = Field(
        ...,
        alias="instance",
        title=(
            "List of `ImagingObjectSelectionStudySeriesInstance` items (represented as "
            "`dict` in JSON)."
        ),
        description="The selected instance.",
    )

    uid: fhirtypes.Oid = Field(
        None,
        alias="uid",
        title="Type `Oid`.",
        description="Series instance UID.",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`.",
        description="Retrieve series URL.",
    )


class ImagingObjectSelectionStudySeriesInstance(BackboneElement):
    """The selected instance.

    Identity and locating information of the selected DICOM SOP instances.
    """

    resource_type = "ImagingObjectSelectionStudySeriesInstance"

    frames: ListType[
        fhirtypes.ImagingObjectSelectionStudySeriesInstanceFramesType
    ] = Field(
        None,
        alias="frames",
        title=(
            "List of `ImagingObjectSelectionStudySeriesInstanceFrames` items "
            "(represented as `dict` in JSON)."
        ),
        description="The frame set.",
    )

    sopClass: fhirtypes.Oid = Field(
        ...,
        alias="sopClass",
        title="Type `Oid`.",
        description="SOP class UID of instance.",
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Type `Oid`.",
        description="Selected instance UID.",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `str`.",
        description="Retrieve instance URL.",
    )


class ImagingObjectSelectionStudySeriesInstanceFrames(BackboneElement):
    """The frame set.

    Identity and location information of the frames in the selected instance.
    """

    resource_type = "ImagingObjectSelectionStudySeriesInstanceFrames"

    frameNumbers: ListType[fhirtypes.UnsignedInt] = Field(
        ...,
        alias="frameNumbers",
        title="List of `int` items.",
        description="Frame numbers.",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri`.",
        description="Retrieve frame URL.",
    )
