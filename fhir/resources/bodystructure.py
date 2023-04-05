# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodyStructure
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class BodyStructure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specific and identified anatomical structure.
    Record details about an anatomical structure.  This resource may be used
    when a coded concept does not provide the necessary detail needed for the
    use case.
    """

    resource_type = Field("BodyStructure", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this record is in active use",
        description="Whether this body site is in active use.",
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Text description",
        description="A summary, characterization or explanation of the body structure.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    excludedStructure: typing.List[
        fhirtypes.BodyStructureIncludedStructureType
    ] = Field(
        None,
        alias="excludedStructure",
        title="Excluded anatomic locations(s)",
        description=(
            "The anatomical location(s) or region(s) not occupied or represented by"
            " the specimen, lesion, or body structure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Bodystructure identifier",
        description="Identifier for this instance of the anatomical structure.",
        # if property is element of this resource.
        element_property=True,
    )

    image: typing.List[fhirtypes.AttachmentType] = Field(
        None,
        alias="image",
        title="Attached images",
        description="Image or images used to identify a location.",
        # if property is element of this resource.
        element_property=True,
    )

    includedStructure: typing.List[
        fhirtypes.BodyStructureIncludedStructureType
    ] = Field(
        ...,
        alias="includedStructure",
        title="Included anatomic location(s)",
        description=(
            "The anatomical location(s) or region(s) of the specimen, lesion, or "
            "body structure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    morphology: fhirtypes.CodeableConceptType = Field(
        None,
        alias="morphology",
        title="Kind of Structure",
        description=(
            "The kind of structure being represented by the body structure at "
            "`BodyStructure.location`.  This can define both normal and abnormal "
            "morphologies."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who this is about",
        description="The person to which the body site belongs.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BodyStructure`` according specification,
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
            "active",
            "morphology",
            "includedStructure",
            "excludedStructure",
            "description",
            "image",
            "patient",
        ]


class BodyStructureIncludedStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Included anatomic location(s).
    The anatomical location(s) or region(s) of the specimen, lesion, or body
    structure.
    """

    resource_type = Field("BodyStructureIncludedStructure", const=True)

    bodyLandmarkOrientation: typing.List[
        fhirtypes.BodyStructureIncludedStructureBodyLandmarkOrientationType
    ] = Field(
        None,
        alias="bodyLandmarkOrientation",
        title="Landmark relative location",
        description=(
            "Body locations in relation to a specific body landmark (tatoo, scar, "
            "other body structure)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    laterality: fhirtypes.CodeableConceptType = Field(
        None,
        alias="laterality",
        title="Code that represents the included structure laterality",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    qualifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="qualifier",
        title="Code that represents the included structure qualifier",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    spatialReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="spatialReference",
        title="Cartesian reference for structure",
        description="XY or XYZ-coordinate orientation for structure.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ImagingSelection"],
    )

    structure: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="structure",
        title="Code that represents the included structure",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BodyStructureIncludedStructure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "structure",
            "laterality",
            "bodyLandmarkOrientation",
            "spatialReference",
            "qualifier",
        ]


class BodyStructureIncludedStructureBodyLandmarkOrientation(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Landmark relative location.
    Body locations in relation to a specific body landmark (tatoo, scar, other
    body structure).
    """

    resource_type = Field(
        "BodyStructureIncludedStructureBodyLandmarkOrientation", const=True
    )

    clockFacePosition: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="clockFacePosition",
        title="Clockface orientation",
        description=(
            "An description of the direction away from a landmark something is "
            "located based on a radial clock dial."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    distanceFromLandmark: typing.List[
        fhirtypes.BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmarkType
    ] = Field(
        None,
        alias="distanceFromLandmark",
        title="Landmark relative location",
        description=(
            "The distance in centimeters a certain observation is made from a body "
            "landmark."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    landmarkDescription: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="landmarkDescription",
        title="Body ]andmark description",
        description=(
            "A description of a landmark on the body used as a reference to locate "
            "something else."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    surfaceOrientation: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="surfaceOrientation",
        title="Relative landmark surface orientation",
        description="The surface area a body location is in relation to a landmark.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BodyStructureIncludedStructureBodyLandmarkOrientation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "landmarkDescription",
            "clockFacePosition",
            "distanceFromLandmark",
            "surfaceOrientation",
        ]


class BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmark(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Landmark relative location.
    The distance in centimeters a certain observation is made from a body
    landmark.
    """

    resource_type = Field(
        "BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmark",
        const=True,
    )

    device: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="device",
        title="Measurement device",
        description="An instrument, tool, analyzer, etc. used in the measurement.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    value: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="value",
        title="Measured distance from body landmark",
        description="The measured distance (e.g., in cm) from a body landmark.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BodyStructureIncludedStructureBodyLandmark
        OrientationDistanceFromLandmark``
        according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "device", "value"]
