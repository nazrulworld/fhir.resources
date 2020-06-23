# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingManifest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImagingManifest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key Object Selection.
    A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.
    """

    resource_type = Field("ImagingManifest", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Practitioner, Device, Organization, "
            "Patient, RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Author (human or machine)",
    )

    authoringTime: fhirtypes.DateTime = Field(
        None,
        alias="authoringTime",
        title="Type `DateTime`",
        description="Time when the selection of instances was made",
    )
    authoringTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoringTime", title="Extension field for ``authoringTime``."
    )

    description: fhirtypes.String = Field(
        None, alias="description", title="Type `String`", description="Description text"
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="SOP Instance UID",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Patient of the selected objects",
    )

    study: ListType[fhirtypes.ImagingManifestStudyType] = Field(
        ...,
        alias="study",
        title="List of `ImagingManifestStudy` items (represented as `dict` in JSON)",
        description="Study identity of the selected instances",
    )


class ImagingManifestStudy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Study identity of the selected instances.
    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """

    resource_type = Field("ImagingManifestStudy", const=True)

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "List of `Reference` items referencing `Endpoint` (represented as "
            "`dict` in JSON)"
        ),
        description="Study access service endpoint",
    )

    imagingStudy: fhirtypes.ReferenceType = Field(
        None,
        alias="imagingStudy",
        title=(
            "Type `Reference` referencing `ImagingStudy` (represented as `dict` in "
            "JSON)"
        ),
        description="Reference to ImagingStudy",
    )

    series: ListType[fhirtypes.ImagingManifestStudySeriesType] = Field(
        ...,
        alias="series",
        title=(
            "List of `ImagingManifestStudySeries` items (represented as `dict` in "
            "JSON)"
        ),
        description="Series identity of the selected instances",
    )

    uid: fhirtypes.Oid = Field(
        ..., alias="uid", title="Type `Oid`", description="Study instance UID"
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )


class ImagingManifestStudySeries(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Series identity of the selected instances.
    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """

    resource_type = Field("ImagingManifestStudySeries", const=True)

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "List of `Reference` items referencing `Endpoint` (represented as "
            "`dict` in JSON)"
        ),
        description="Series access endpoint",
    )

    instance: ListType[fhirtypes.ImagingManifestStudySeriesInstanceType] = Field(
        ...,
        alias="instance",
        title=(
            "List of `ImagingManifestStudySeriesInstance` items (represented as "
            "`dict` in JSON)"
        ),
        description="The selected instance",
    )

    uid: fhirtypes.Oid = Field(
        ..., alias="uid", title="Type `Oid`", description="Series instance UID"
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )


class ImagingManifestStudySeriesInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The selected instance.
    Identity and locating information of the selected DICOM SOP instances.
    """

    resource_type = Field("ImagingManifestStudySeriesInstance", const=True)

    sopClass: fhirtypes.Oid = Field(
        ...,
        alias="sopClass",
        title="Type `Oid`",
        description="SOP class UID of instance",
    )
    sopClass__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sopClass", title="Extension field for ``sopClass``."
    )

    uid: fhirtypes.Oid = Field(
        ..., alias="uid", title="Type `Oid`", description="Selected instance UID"
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )
