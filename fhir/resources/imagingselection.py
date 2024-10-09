from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingSelection
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImagingSelection(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A selection of DICOM SOP instances and/or frames.
    A selection of DICOM SOP instances and/or frames within a single Study and
    Series. This might include additional specifics such as an image region, an
    Observation UID or a Segmentation Number, allowing linkage to an
    Observation Resource or transferring this information along with the
    ImagingStudy Resource.
    """

    __resource_type__ = "ImagingSelection"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Associated request",
        description=(
            "A list of the diagnostic requests that resulted in this imaging "
            "selection being performed."
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

    bodySite: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Body part examined",
        description=(
            "The anatomic structures examined. See DICOM Part 16 Annex L (http://di"
            "com.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html)"
            " for DICOM to SNOMED-CT mappings."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BodyStructure"],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Classifies the imaging selection",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Imaging Selection purpose text or code",
        description="Reason for referencing the selected content.",
        json_schema_extra={
            "element_property": True,
        },
    )

    derivedFrom: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="derivedFrom",
        title="The imaging study from which the imaging selection is derived",
        description="The imaging study from which the imaging selection is made.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ImagingStudy", "DocumentReference"],
        },
    )

    endpoint: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="endpoint",
        title=(
            "The network service providing retrieval for the images referenced in "
            "the imaging selection"
        ),
        description=(
            "The network service providing retrieval access to the selected images,"
            " frames, etc. See implementation notes for information about using "
            "DICOM endpoints."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Endpoint"],
        },
    )

    focus: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="focus",
        title="Related resource that is the focus for the imaging selection",
        description=(
            "The actual focus of an observation when it is not the patient of "
            "record representing something or someone associated with the patient "
            "such as a spouse, parent, fetus, or donor. For example, fetus "
            "observations in a mother's record.  The focus of an observation could "
            "also be an existing condition,  an intervention, the subject's diet,  "
            "another observation of the subject,  or a body structure such as tumor"
            " or implanted device.   An example use case would be using the "
            "Observation resource to capture whether the mother is trained to "
            "change her child's tracheostomy tube. In this example, the child is "
            "the patient of record and the mother is the focus."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ImagingSelection"],
        },
    )

    frameOfReferenceUid: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="frameOfReferenceUid",
        title="The Frame of Reference UID for the selected images",
        description=(
            "The Frame of Reference UID identifying the coordinate system that "
            "conveys spatial and/or temporal information for the selected images or"
            " frames."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    frameOfReferenceUid__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_frameOfReferenceUid",
        title="Extension field for ``frameOfReferenceUid``.",
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for Imaging Selection",
        description="A unique identifier assigned to this imaging selection.",
        json_schema_extra={
            "element_property": True,
        },
    )

    instance: typing.List[fhirtypes.ImagingSelectionInstanceType] | None = Field(  # type: ignore
        None,
        alias="instance",
        title="The selected instances",
        description=(
            "Each imaging selection includes one or more selected DICOM SOP "
            "instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    issued: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="issued",
        title="Date / Time when this imaging selection was created",
        description="The date and time this imaging selection was created.",
        json_schema_extra={
            "element_property": True,
        },
    )
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_issued", title="Extension field for ``issued``."
    )

    performer: typing.List[fhirtypes.ImagingSelectionPerformerType] | None = Field(  # type: ignore
        None,
        alias="performer",
        title="Selector of the instances (human or machine)",
        description="Selector of the instances \u2013 human or machine.",
        json_schema_extra={
            "element_property": True,
        },
    )

    seriesNumber: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="seriesNumber",
        title="DICOM Series Number",
        description=(
            "The Series Number for the DICOM Series from which the images were "
            "selected."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    seriesNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_seriesNumber", title="Extension field for ``seriesNumber``."
    )

    seriesUid: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="seriesUid",
        title="DICOM Series Instance UID",
        description=(
            "The Series Instance UID for the DICOM Series from which the images "
            "were selected."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    seriesUid__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_seriesUid", title="Extension field for ``seriesUid``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="available | entered-in-error | unknown",
        description=(
            "The current state of the ImagingSelection resource. This is not the "
            "status of any ImagingStudy, ServiceRequest, or Task resources "
            "associated with the ImagingSelection."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["available", "entered-in-error", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    studyUid: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="studyUid",
        title="DICOM Study Instance UID",
        description=(
            "The Study Instance UID for the DICOM Study from which the images were "
            "selected."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    studyUid__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_studyUid", title="Extension field for ``studyUid``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="Subject of the selected instances",
        description=(
            "The patient, or group of patients, location, device, organization, "
            "procedure or practitioner this imaging selection is about and into "
            "whose or what record the imaging selection is placed."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Group",
                "Device",
                "Location",
                "Organization",
                "Procedure",
                "Practitioner",
                "Medication",
                "Substance",
                "Specimen",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingSelection`` according specification,
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
            "subject",
            "issued",
            "performer",
            "basedOn",
            "category",
            "code",
            "studyUid",
            "derivedFrom",
            "endpoint",
            "seriesUid",
            "seriesNumber",
            "frameOfReferenceUid",
            "bodySite",
            "focus",
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
        required_fields = [("status", "status__ext")]
        return required_fields


class ImagingSelectionInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The selected instances.
    Each imaging selection includes one or more selected DICOM SOP instances.
    """

    __resource_type__ = "ImagingSelectionInstance"

    imageRegion2D: typing.List[fhirtypes.ImagingSelectionInstanceImageRegion2DType] | None = Field(  # type: ignore
        None,
        alias="imageRegion2D",
        title="A specific 2D region in a DICOM image / frame",
        description=(
            "Each imaging selection instance or frame list might includes an image "
            "region, specified by a region type and a set of 2D coordinates."
            "        If the parent imagingSelection.instance contains a subset "
            "element of type frame, the image region applies to all frames in the "
            "subset list."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    imageRegion3D: typing.List[fhirtypes.ImagingSelectionInstanceImageRegion3DType] | None = Field(  # type: ignore
        None,
        alias="imageRegion3D",
        title="A specific 3D region in a DICOM frame of reference",
        description=(
            "Each imaging selection might includes a 3D image region, specified by "
            "a region type and a set of 3D coordinates."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    number: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="number",
        title="DICOM Instance Number",
        description="The Instance Number for the selected DICOM instance.",
        json_schema_extra={
            "element_property": True,
        },
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_number", title="Extension field for ``number``."
    )

    sopClass: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="sopClass",
        title="DICOM SOP Class UID",
        description="The SOP Class UID for the selected DICOM instance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subset: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="subset",
        title="The selected subset of the SOP Instance",
        description=(
            "Selected subset of the SOP Instance. The content and format of the "
            "subset item is determined by the SOP Class of the selected instance."
            "        May be one of:        - A list of frame numbers selected from "
            "a multiframe SOP Instance.        - A list of Content Item Observation"
            " UID values selected from a DICOM SR or other structured document SOP "
            "Instance.        - A list of segment numbers selected from a "
            "segmentation SOP Instance.        - A list of Region of Interest (ROI)"
            " numbers selected from a radiotherapy structure set SOP Instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subset__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_subset", title="Extension field for ``subset``."
    )

    uid: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="uid",
        title="DICOM SOP Instance UID",
        description="The SOP Instance UID for the selected DICOM instance.",
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
        ``ImagingSelectionInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uid",
            "number",
            "sopClass",
            "subset",
            "imageRegion2D",
            "imageRegion3D",
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


class ImagingSelectionInstanceImageRegion2D(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A specific 2D region in a DICOM image / frame.
    Each imaging selection instance or frame list might includes an image
    region, specified by a region type and a set of 2D coordinates.
           If the parent imagingSelection.instance contains a subset element of
    type frame, the image region applies to all frames in the subset list.
    """

    __resource_type__ = "ImagingSelectionInstanceImageRegion2D"

    coordinate: typing.List[fhirtypes.DecimalType | None] | None = Field(  # type: ignore
        None,
        alias="coordinate",
        title="Specifies the coordinates that define the image region",
        description=(
            "The coordinates describing the image region. Encoded as a set of "
            "(column, row) pairs that denote positions in the selected image / "
            "frames specified with sub-pixel resolution.        The origin at the "
            "TLHC of the TLHC pixel is 0.0\\0.0, the BRHC of the TLHC pixel is "
            "1.0\\1.0, and the BRHC of the BRHC pixel is the number of columns\\rows "
            "in the image / frames. The values must be within the range 0\\0 to the "
            "number of columns\\rows in the image / frames."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    coordinate__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_coordinate", title="Extension field for ``coordinate``."
    )

    regionType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="regionType",
        title="point | polyline | interpolated | circle | ellipse",
        description="Specifies the type of image region.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["point", "polyline", "interpolated", "circle", "ellipse"],
        },
    )
    regionType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_regionType", title="Extension field for ``regionType``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingSelectionInstanceImageRegion2D`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "regionType", "coordinate"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("coordinate", "coordinate__ext"),
            ("regionType", "regionType__ext"),
        ]
        return required_fields


class ImagingSelectionInstanceImageRegion3D(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A specific 3D region in a DICOM frame of reference.
    Each imaging selection might includes a 3D image region, specified by a
    region type and a set of 3D coordinates.
    """

    __resource_type__ = "ImagingSelectionInstanceImageRegion3D"

    coordinate: typing.List[fhirtypes.DecimalType | None] | None = Field(  # type: ignore
        None,
        alias="coordinate",
        title="Specifies the coordinates that define the image region",
        description=(
            "The coordinates describing the image region. Encoded as an ordered set"
            " of (x,y,z) triplets (in mm and may be negative) that define a region "
            "of interest in the patient-relative Reference Coordinate System "
            "defined by ImagingSelection.frameOfReferenceUid element."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    coordinate__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_coordinate", title="Extension field for ``coordinate``."
    )

    regionType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="regionType",
        title="point | multipoint | polyline | polygon | ellipse | ellipsoid",
        description="Specifies the type of image region.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "point",
                "multipoint",
                "polyline",
                "polygon",
                "ellipse",
                "ellipsoid",
            ],
        },
    )
    regionType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_regionType", title="Extension field for ``regionType``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingSelectionInstanceImageRegion3D`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "regionType", "coordinate"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("coordinate", "coordinate__ext"),
            ("regionType", "regionType__ext"),
        ]
        return required_fields


class ImagingSelectionPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Selector of the instances (human or machine).
    Selector of the instances – human or machine.
    """

    __resource_type__ = "ImagingSelectionPerformer"

    actor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="actor",
        title="Author (human or machine)",
        description="Author \u2013 human or machine.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Device",
                "Organization",
                "CareTeam",
                "Patient",
                "RelatedPerson",
                "HealthcareService",
            ],
        },
    )

    function: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="function",
        title="Type of performer",
        description="Distinguishes the type of involvement of the performer.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingSelectionPerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]
