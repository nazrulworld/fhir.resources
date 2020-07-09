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
        title="Request fulfilled",
        description=(
            "A list of the diagnostic requests that resulted in this imaging study "
            "being performed."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "CarePlan",
            "ServiceRequest",
            "Appointment",
            "AppointmentResponse",
            "Task",
        ],
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Institution-generated description",
        description=(
            "The Imaging Manager description of the study. Institution-generated "
            "description or classification of the Study (component) performed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter with which this imaging study is associated",
        description=(
            "The healthcare event (e.g. a patient and healthcare provider "
            "interaction) during which this ImagingStudy is made."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Study access endpoint",
        description=(
            "The network service providing access (e.g., query, view, or retrieval)"
            " for the study. See implementation notes for information about using "
            "DICOM endpoints. A study-level endpoint applies to each series in the "
            "study, unless overridden by a series-level endpoint with the same "
            "Endpoint.connectionType."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifiers for the whole study",
        description=(
            "Identifiers for the ImagingStudy such as DICOM Study Instance UID, and"
            " Accession Number."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    interpreter: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="interpreter",
        title="Who interpreted images",
        description="Who read the study and interpreted the images or other content.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where ImagingStudy occurred",
        description="The principal physical location where the ImagingStudy was performed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    modality: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="modality",
        title="All series modality if actual acquisition modalities",
        description=(
            "A list of all the series.modality values that are actual acquisition "
            "modalities, i.e. those in the DICOM Context Group 29 (value set OID "
            "1.2.840.10008.6.1.19)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="User-defined comments",
        description=(
            "Per the recommended DICOM mapping, this element is derived from the "
            "Study Description attribute (0008,1030). Observations or findings "
            "about the imaging study should be recorded in another resource, e.g. "
            "Observation, and not in this element."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfInstances",
        title="Number of Study Related Instances",
        description=(
            "Number of SOP Instances in Study. This value given may be larger than "
            "the number of instance elements this resource contains due to resource"
            " availability, security, or other factors. This element should be "
            "present if any instance elements are present."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfInstances",
        title="Extension field for ``numberOfInstances``.",
    )

    numberOfSeries: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfSeries",
        title="Number of Study Related Series",
        description=(
            "Number of Series in the Study. This value given may be larger than the"
            " number of series elements this Resource contains due to resource "
            "availability, security, or other factors. This element should be "
            "present if any series elements are present."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfSeries__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_numberOfSeries", title="Extension field for ``numberOfSeries``."
    )

    procedureCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="procedureCode",
        title="The performed procedure code",
        description="The code for the performed procedure type.",
        # if property is element of this resource.
        element_property=True,
    )

    procedureReference: fhirtypes.ReferenceType = Field(
        None,
        alias="procedureReference",
        title="The performed Procedure reference",
        description="The procedure which this ImagingStudy was part of.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why the study was requested",
        description=(
            "Description of clinical condition indicating why the ImagingStudy was "
            "requested."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why was study performed",
        description="Indicates another resource whose existence justifies this Study.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "Media",
            "DiagnosticReport",
            "DocumentReference",
        ],
    )

    referrer: fhirtypes.ReferenceType = Field(
        None,
        alias="referrer",
        title="Referring physician",
        description="The requesting/referring physician.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    series: ListType[fhirtypes.ImagingStudySeriesType] = Field(
        None,
        alias="series",
        title="Each study has one or more series of instances",
        description="Each study has one or more series of images or other content.",
        # if property is element of this resource.
        element_property=True,
    )

    started: fhirtypes.DateTime = Field(
        None,
        alias="started",
        title="When the study was started",
        description="Date and time the study started.",
        # if property is element of this resource.
        element_property=True,
    )
    started__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_started", title="Extension field for ``started``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="registered | available | cancelled | entered-in-error | unknown",
        description="The current state of the ImagingStudy.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "registered",
            "available",
            "cancelled",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who or what is the subject of the study",
        description="The subject, typically a patient, of the imaging study.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Device", "Group"],
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
        title="Body part examined",
        description=(
            "The anatomic structures examined. See DICOM Part 16 Annex L (http://di"
            "com.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html)"
            " for DICOM to SNOMED-CT mappings. The bodySite may indicate the "
            "laterality of body part imaged; if so, it shall be consistent with any"
            " content of ImagingStudy.series.laterality."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="A short human readable summary of the series",
        description="A description of the series.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Series access endpoint",
        description=(
            "The network service providing access (e.g., query, view, or retrieval)"
            " for this series. See implementation notes for information about using"
            " DICOM endpoints. A series-level endpoint, if present, has precedence "
            "over a study-level endpoint with the same Endpoint.connectionType."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    instance: ListType[fhirtypes.ImagingStudySeriesInstanceType] = Field(
        None,
        alias="instance",
        title="A single SOP instance from the series",
        description=(
            "A single SOP instance within the series, e.g. an image, or "
            "presentation state."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
    )

    modality: fhirtypes.CodingType = Field(
        ...,
        alias="modality",
        title="The modality of the instances in the series",
        description="The modality of this series sequence.",
        # if property is element of this resource.
        element_property=True,
    )

    number: fhirtypes.UnsignedInt = Field(
        None,
        alias="number",
        title="Numeric identifier of this series",
        description="The numeric identifier of this series in the study.",
        # if property is element of this resource.
        element_property=True,
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    numberOfInstances: fhirtypes.UnsignedInt = Field(
        None,
        alias="numberOfInstances",
        title="Number of Series Related Instances",
        description=(
            "Number of SOP Instances in the Study. The value given may be larger "
            "than the number of instance elements this resource contains due to "
            "resource availability, security, or other factors. This element should"
            " be present if any instance elements are present."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_numberOfInstances",
        title="Extension field for ``numberOfInstances``.",
    )

    performer: ListType[fhirtypes.ImagingStudySeriesPerformerType] = Field(
        None,
        alias="performer",
        title="Who performed the series",
        description="Indicates who or what performed the series and how they were involved.",
        # if property is element of this resource.
        element_property=True,
    )

    specimen: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="specimen",
        title="Specimen imaged",
        description="The specimen imaged, e.g., for whole slide imaging of a biopsy.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    started: fhirtypes.DateTime = Field(
        None,
        alias="started",
        title="When the series started",
        description="The date and time the series was started.",
        # if property is element of this resource.
        element_property=True,
    )
    started__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_started", title="Extension field for ``started``."
    )

    uid: fhirtypes.Id = Field(
        ...,
        alias="uid",
        title="DICOM Series Instance UID for the series",
        description="The DICOM Series Instance UID for the series.",
        # if property is element of this resource.
        element_property=True,
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
        title="The number of this instance in the series",
        description="The number of instance in the series.",
        # if property is element of this resource.
        element_property=True,
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    sopClass: fhirtypes.CodingType = Field(
        ...,
        alias="sopClass",
        title="DICOM class type",
        description="DICOM instance  type.",
        # if property is element of this resource.
        element_property=True,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Description of instance",
        description="The description of the instance.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    uid: fhirtypes.Id = Field(
        ...,
        alias="uid",
        title="DICOM SOP Instance UID",
        description="The DICOM SOP Instance UID for this image or other DICOM content.",
        # if property is element of this resource.
        element_property=True,
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
        title="Who performed the series",
        description="Indicates who or what performed the series.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type of performance",
        description="Distinguishes the type of involvement of the performer in the series.",
        # if property is element of this resource.
        element_property=True,
    )
