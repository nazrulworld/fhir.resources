from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImagingStudy(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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

    __resource_type__ = "ImagingStudy"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Request fulfilled",
        description=(
            "A list of the diagnostic requests that resulted in this imaging study "
            "being performed."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "ServiceRequest",
                "Appointment",
                "AppointmentResponse",
                "Task",
            ],
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Institution-generated description",
        description=(
            "The Imaging Manager description of the study. Institution-generated "
            "description or classification of the Study (component) performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter with which this imaging study is associated",
        description=(
            "The healthcare event (e.g. a patient and healthcare provider "
            "interaction) during which this ImagingStudy is made."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    endpoint: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Endpoint"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifiers for the whole study",
        description=(
            "Identifiers for the ImagingStudy such as DICOM Study Instance UID, and"
            " Accession Number."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    interpreter: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="interpreter",
        title="Who interpreted images",
        description="Who read the study and interpreted the images or other content.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Where ImagingStudy occurred",
        description="The principal physical location where the ImagingStudy was performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    modality: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="modality",
        title="All series modality if actual acquisition modalities",
        description=(
            "A list of all the series.modality values that are actual acquisition "
            "modalities, i.e. those in the DICOM Context Group 29 (value set OID "
            "1.2.840.10008.6.1.19)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="User-defined comments",
        description=(
            "Per the recommended DICOM mapping, this element is derived from the "
            "Study Description attribute (0008,1030). Observations or findings "
            "about the imaging study should be recorded in another resource, e.g. "
            "Observation, and not in this element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    numberOfInstances: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="numberOfInstances",
        title="Number of Study Related Instances",
        description=(
            "Number of SOP Instances in Study. This value given may be larger than "
            "the number of instance elements this resource contains due to resource"
            " availability, security, or other factors. This element should be "
            "present if any instance elements are present."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_numberOfInstances",
        title="Extension field for ``numberOfInstances``.",
    )

    numberOfSeries: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="numberOfSeries",
        title="Number of Study Related Series",
        description=(
            "Number of Series in the Study. This value given may be larger than the"
            " number of series elements this Resource contains due to resource "
            "availability, security, or other factors. This element should be "
            "present if any series elements are present."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    numberOfSeries__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_numberOfSeries", title="Extension field for ``numberOfSeries``."
    )

    procedureCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="procedureCode",
        title="The performed procedure code",
        description="The code for the performed procedure type.",
        json_schema_extra={
            "element_property": True,
        },
    )

    procedureReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="procedureReference",
        title="The performed Procedure reference",
        description="The procedure which this ImagingStudy was part of.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Procedure"],
        },
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Why the study was requested",
        description=(
            "Description of clinical condition indicating why the ImagingStudy was "
            "requested."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="Why was study performed",
        description="Indicates another resource whose existence justifies this Study.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Condition",
                "Observation",
                "Media",
                "DiagnosticReport",
                "DocumentReference",
            ],
        },
    )

    referrer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="referrer",
        title="Referring physician",
        description="The requesting/referring physician.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    series: typing.List[fhirtypes.ImagingStudySeriesType] | None = Field(  # type: ignore
        None,
        alias="series",
        title="Each study has one or more series of instances",
        description="Each study has one or more series of images or other content.",
        json_schema_extra={
            "element_property": True,
        },
    )

    started: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="started",
        title="When the study was started",
        description="Date and time the study started.",
        json_schema_extra={
            "element_property": True,
        },
    )
    started__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_started", title="Extension field for ``started``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="registered | available | cancelled | entered-in-error | unknown",
        description="The current state of the ImagingStudy.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "registered",
                "available",
                "cancelled",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who or what is the subject of the study",
        description="The subject, typically a patient, of the imaging study.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Device", "Group"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingStudy`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "status",
            "modality",
            "subject",
            "encounter",
            "started",
            "basedOn",
            "referrer",
            "interpreter",
            "endpoint",
            "numberOfSeries",
            "numberOfInstances",
            "procedureReference",
            "procedureCode",
            "location",
            "reasonCode",
            "reasonReference",
            "note",
            "description",
            "series",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class ImagingStudySeries(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Each study has one or more series of instances.
    Each study has one or more series of images or other content.
    """

    __resource_type__ = "ImagingStudySeries"

    bodySite: fhirtypes.CodingType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="A short human readable summary of the series",
        description="A description of the series.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    endpoint: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="endpoint",
        title="Series access endpoint",
        description=(
            "The network service providing access (e.g., query, view, or retrieval)"
            " for this series. See implementation notes for information about using"
            " DICOM endpoints. A series-level endpoint, if present, has precedence "
            "over a study-level endpoint with the same Endpoint.connectionType."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Endpoint"],
        },
    )

    instance: typing.List[fhirtypes.ImagingStudySeriesInstanceType] | None = Field(  # type: ignore
        None,
        alias="instance",
        title="A single SOP instance from the series",
        description=(
            "A single SOP instance within the series, e.g. an image, or "
            "presentation state."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    laterality: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="laterality",
        title="Body part laterality",
        description=(
            "The laterality of the (possibly paired) anatomic structures examined. "
            "E.g., the left knee, both lungs, or unpaired abdomen. If present, "
            "shall be consistent with any laterality information indicated in "
            "ImagingStudy.series.bodySite."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    modality: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="modality",
        title="The modality of the instances in the series",
        description="The modality of this series sequence.",
        json_schema_extra={
            "element_property": True,
        },
    )

    number: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="number",
        title="Numeric identifier of this series",
        description="The numeric identifier of this series in the study.",
        json_schema_extra={
            "element_property": True,
        },
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_number", title="Extension field for ``number``."
    )

    numberOfInstances: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="numberOfInstances",
        title="Number of Series Related Instances",
        description=(
            "Number of SOP Instances in the Study. The value given may be larger "
            "than the number of instance elements this resource contains due to "
            "resource availability, security, or other factors. This element should"
            " be present if any instance elements are present."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_numberOfInstances",
        title="Extension field for ``numberOfInstances``.",
    )

    performer: typing.List[fhirtypes.ImagingStudySeriesPerformerType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Who performed the series",
        description="Indicates who or what performed the series and how they were involved.",
        json_schema_extra={
            "element_property": True,
        },
    )

    specimen: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="specimen",
        title="Specimen imaged",
        description="The specimen imaged, e.g., for whole slide imaging of a biopsy.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Specimen"],
        },
    )

    started: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="started",
        title="When the series started",
        description="The date and time the series was started.",
        json_schema_extra={
            "element_property": True,
        },
    )
    started__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_started", title="Extension field for ``started``."
    )

    uid: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="uid",
        title="DICOM Series Instance UID for the series",
        description="The DICOM Series Instance UID for the series.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uid", title="Extension field for ``uid``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingStudySeries`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uid",
            "number",
            "modality",
            "description",
            "numberOfInstances",
            "endpoint",
            "bodySite",
            "laterality",
            "specimen",
            "started",
            "performer",
            "instance",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("uid", "uid__ext")]
        return required_fields


class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single SOP instance from the series.
    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """

    __resource_type__ = "ImagingStudySeriesInstance"

    number: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="number",
        title="The number of this instance in the series",
        description="The number of instance in the series.",
        json_schema_extra={
            "element_property": True,
        },
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_number", title="Extension field for ``number``."
    )

    sopClass: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="sopClass",
        title="DICOM class type",
        description="DICOM instance  type.",
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Description of instance",
        description="The description of the instance.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    uid: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="uid",
        title="DICOM SOP Instance UID",
        description="The DICOM SOP Instance UID for this image or other DICOM content.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uid", title="Extension field for ``uid``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingStudySeriesInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uid",
            "sopClass",
            "number",
            "title",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("uid", "uid__ext")]
        return required_fields


class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed the series.
    Indicates who or what performed the series and how they were involved.
    """

    __resource_type__ = "ImagingStudySeriesPerformer"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="actor",
        title="Who performed the series",
        description="Indicates who or what performed the series.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "CareTeam",
                "Patient",
                "Device",
                "RelatedPerson",
            ],
        },
    )

    function: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="function",
        title="Type of performance",
        description="Distinguishes the type of involvement of the performer in the series.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingStudySeriesPerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]
