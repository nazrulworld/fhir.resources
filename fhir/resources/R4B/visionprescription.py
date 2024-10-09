from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class VisionPrescription(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Prescription for vision correction products for a patient.
    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """

    __resource_type__ = "VisionPrescription"

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="Response creation date",
        description="The date this resource was created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    dateWritten: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="dateWritten",
        title="When prescription was authorized",
        description="The date (and perhaps time) when the prescription was written.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    dateWritten__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_dateWritten", title="Extension field for ``dateWritten``."
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Created during encounter / admission / stay",
        description=(
            "A reference to a resource that identifies the particular occurrence of"
            " contact between patient and health care provider during which the "
            "prescription was issued."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for vision prescription",
        description="A unique identifier assigned to this vision prescription.",
        json_schema_extra={
            "element_property": True,
        },
    )

    lensSpecification: typing.List[fhirtypes.VisionPrescriptionLensSpecificationType] = Field(  # type: ignore
        ...,
        alias="lensSpecification",
        title="Vision lens authorization",
        description=(
            "Contain the details of  the individual lens specifications and serves "
            "as the authorization for the fullfillment by certified professionals."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="patient",
        title="Who prescription is for",
        description=(
            "A resource reference to the person to whom the vision prescription "
            "applies."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    prescriber: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="prescriber",
        title="Who authorized the vision prescription",
        description=(
            "The healthcare professional responsible for authorizing the "
            "prescription."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VisionPrescription`` according specification,
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
            "created",
            "patient",
            "encounter",
            "dateWritten",
            "prescriber",
            "lensSpecification",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("created", "created__ext"),
            ("dateWritten", "dateWritten__ext"),
            ("status", "status__ext"),
        ]
        return required_fields


class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Vision lens authorization.
    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """

    __resource_type__ = "VisionPrescriptionLensSpecification"

    add: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="add",
        title="Added power for multifocal levels",
        description=(
            "Power adjustment for multifocal lenses measured in dioptres (0.25 "
            "units)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    add__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_add", title="Extension field for ``add``."
    )

    axis: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="axis",
        title="Lens meridian which contain no power for astigmatism",
        description="Adjustment for astigmatism measured in integer degrees.",
        json_schema_extra={
            "element_property": True,
        },
    )
    axis__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_axis", title="Extension field for ``axis``."
    )

    backCurve: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="backCurve",
        title="Contact lens back curvature",
        description="Back curvature measured in millimetres.",
        json_schema_extra={
            "element_property": True,
        },
    )
    backCurve__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_backCurve", title="Extension field for ``backCurve``."
    )

    brand: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="brand",
        title="Brand required",
        description="Brand recommendations or restrictions.",
        json_schema_extra={
            "element_property": True,
        },
    )
    brand__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_brand", title="Extension field for ``brand``."
    )

    color: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="color",
        title="Color required",
        description="Special color or pattern.",
        json_schema_extra={
            "element_property": True,
        },
    )
    color__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_color", title="Extension field for ``color``."
    )

    cylinder: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="cylinder",
        title="Lens power for astigmatism",
        description="Power adjustment for astigmatism measured in dioptres (0.25 units).",
        json_schema_extra={
            "element_property": True,
        },
    )
    cylinder__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_cylinder", title="Extension field for ``cylinder``."
    )

    diameter: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="diameter",
        title="Contact lens diameter",
        description="Contact lens diameter measured in millimetres.",
        json_schema_extra={
            "element_property": True,
        },
    )
    diameter__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_diameter", title="Extension field for ``diameter``."
    )

    duration: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="duration",
        title="Lens wear duration",
        description="The recommended maximum wear period for the lens.",
        json_schema_extra={
            "element_property": True,
        },
    )

    eye: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="eye",
        title="right | left",
        description="The eye for which the lens specification applies.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["right", "left"],
        },
    )
    eye__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_eye", title="Extension field for ``eye``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Notes for coatings",
        description="Notes for special requirements such as coatings and lens materials.",
        json_schema_extra={
            "element_property": True,
        },
    )

    power: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="power",
        title="Contact lens power",
        description="Contact lens power measured in dioptres (0.25 units).",
        json_schema_extra={
            "element_property": True,
        },
    )
    power__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_power", title="Extension field for ``power``."
    )

    prism: typing.List[fhirtypes.VisionPrescriptionLensSpecificationPrismType] | None = Field(  # type: ignore
        None,
        alias="prism",
        title="Eye alignment compensation",
        description="Allows for adjustment on two axis.",
        json_schema_extra={
            "element_property": True,
        },
    )

    product: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="product",
        title="Product to be supplied",
        description=(
            "Identifies the type of vision correction product which is required for"
            " the patient."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    sphere: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="sphere",
        title="Power of the lens",
        description="Lens power measured in dioptres (0.25 units).",
        json_schema_extra={
            "element_property": True,
        },
    )
    sphere__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sphere", title="Extension field for ``sphere``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VisionPrescriptionLensSpecification`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "product",
            "eye",
            "sphere",
            "cylinder",
            "axis",
            "prism",
            "add",
            "power",
            "backCurve",
            "diameter",
            "duration",
            "color",
            "brand",
            "note",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("eye", "eye__ext")]
        return required_fields


class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Eye alignment compensation.
    Allows for adjustment on two axis.
    """

    __resource_type__ = "VisionPrescriptionLensSpecificationPrism"

    amount: fhirtypes.DecimalType | None = Field(  # type: ignore
        None,
        alias="amount",
        title="Amount of adjustment",
        description="Amount of prism to compensate for eye alignment in fractional units.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    amount__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_amount", title="Extension field for ``amount``."
    )

    base: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="base",
        title="up | down | in | out",
        description="The relative base, or reference lens edge, for the prism.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["up", "down", "in", "out"],
        },
    )
    base__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_base", title="Extension field for ``base``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VisionPrescriptionLensSpecificationPrism`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "amount", "base"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("amount", "amount__ext"), ("base", "base__ext")]
        return required_fields
