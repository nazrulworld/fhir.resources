from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class VisionPrescription(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Prescription for vision correction products for a patient.
    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """

    __resource_type__ = "VisionPrescription"

    dateWritten: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="dateWritten",
        title="When prescription was authorized",
        description="The date (and perhaps time) when the prescription was written.",
        json_schema_extra={
            "element_property": True,
        },
    )
    dateWritten__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_dateWritten", title="Extension field for ``dateWritten``."
    )

    dispense: typing.List[fhirtypes.VisionPrescriptionDispenseType] | None = Field(  # type: ignore
        default=None,
        alias="dispense",
        title="Vision supply authorization",
        description="Deals with details of the dispense part of the supply specification.",
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="encounter",
        title="Created during encounter / admission / stay",
        description=(
            "A link to a resource that identifies the particular occurrence of "
            "contact between patient and health care provider."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Business identifier which may be used by other parties to reference or"
            " identify the prescription."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    patient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="patient",
        title="Who prescription is for",
        description=(
            "A link to a resource representing the person to whom the vision "
            "products will be supplied."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    prescriber: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="prescriber",
        title="Who authorizes the vision product",
        description=(
            "The healthcare professional responsible for authorizing the "
            "prescription."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="reasonCodeableConcept",
        title="Reason or indication for writing the prescription",
        description="Can be the reason or the indication for writing the prescription.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e reason[x]
            "one_of_many": "reason",
            "one_of_many_required": False,
        },
    )

    reasonReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="reasonReference",
        title="Reason or indication for writing the prescription",
        description="Can be the reason or the indication for writing the prescription.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e reason[x]
            "one_of_many": "reason",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``VisionPrescription`` according to specification,
        with preserving the original sequence order.
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
            "patient",
            "encounter",
            "dateWritten",
            "prescriber",
            "reasonCodeableConcept",
            "reasonReference",
            "dispense",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``VisionPrescription`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "meta", "implicitRules", "status"]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"reason": ["reasonCodeableConcept", "reasonReference"]}
        return one_of_many_fields


class VisionPrescriptionDispense(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Vision supply authorization.
    Deals with details of the dispense part of the supply specification.
    """

    __resource_type__ = "VisionPrescriptionDispense"

    add: fhirtypes.DecimalType | None = Field(  # type: ignore
        default=None,
        alias="add",
        title="Lens add",
        description=(
            "Power adjustment for multifocal lenses measured in diopters (0.25 "
            "units)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    add__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_add", title="Extension field for ``add``."
    )

    axis: fhirtypes.IntegerType | None = Field(  # type: ignore
        default=None,
        alias="axis",
        title="Lens axis",
        description="Adjustment for astigmatism measured in integer degrees.",
        json_schema_extra={
            "element_property": True,
        },
    )
    axis__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_axis", title="Extension field for ``axis``."
    )

    backCurve: fhirtypes.DecimalType | None = Field(  # type: ignore
        default=None,
        alias="backCurve",
        title="Contact lens back curvature",
        description="Back curvature measured in millimeters.",
        json_schema_extra={
            "element_property": True,
        },
    )
    backCurve__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_backCurve", title="Extension field for ``backCurve``."
    )

    base: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="base",
        title="up | down | in | out",
        description="The relative base, or reference lens edge, for the prism.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["up", "down", "in", "out"],
        },
    )
    base__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_base", title="Extension field for ``base``."
    )

    brand: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="brand",
        title="Brand required",
        description="Brand recommendations or restrictions.",
        json_schema_extra={
            "element_property": True,
        },
    )
    brand__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_brand", title="Extension field for ``brand``."
    )

    color: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="color",
        title="Color required",
        description="Special color or pattern.",
        json_schema_extra={
            "element_property": True,
        },
    )
    color__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_color", title="Extension field for ``color``."
    )

    cylinder: fhirtypes.DecimalType | None = Field(  # type: ignore
        default=None,
        alias="cylinder",
        title="Lens cylinder",
        description="Power adjustment for astigmatism measured in diopters (0.25 units).",
        json_schema_extra={
            "element_property": True,
        },
    )
    cylinder__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_cylinder", title="Extension field for ``cylinder``."
    )

    diameter: fhirtypes.DecimalType | None = Field(  # type: ignore
        default=None,
        alias="diameter",
        title="Contact lens diameter",
        description="Contact lens diameter measured in millimeters.",
        json_schema_extra={
            "element_property": True,
        },
    )
    diameter__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_diameter", title="Extension field for ``diameter``."
    )

    duration: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="duration",
        title="Lens wear duration",
        description="The recommended maximum wear period for the lens.",
        json_schema_extra={
            "element_property": True,
        },
    )

    eye: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="eye",
        title="right | left",
        description="The eye for which the lens applies.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["right", "left"],
        },
    )
    eye__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_eye", title="Extension field for ``eye``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        default=None,
        alias="note",
        title="Notes for coatings",
        description="Notes for special requirements such as coatings and lens materials.",
        json_schema_extra={
            "element_property": True,
        },
    )

    power: fhirtypes.DecimalType | None = Field(  # type: ignore
        default=None,
        alias="power",
        title="Contact lens power",
        description="Contact lens power measured in diopters (0.25 units).",
        json_schema_extra={
            "element_property": True,
        },
    )
    power__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_power", title="Extension field for ``power``."
    )

    prism: fhirtypes.DecimalType | None = Field(  # type: ignore
        default=None,
        alias="prism",
        title="Lens prism",
        description="Amount of prism to compensate for eye alignment in fractional units.",
        json_schema_extra={
            "element_property": True,
        },
    )
    prism__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_prism", title="Extension field for ``prism``."
    )

    product: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
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
        default=None,
        alias="sphere",
        title="Lens sphere",
        description="Lens power measured in diopters (0.25 units).",
        json_schema_extra={
            "element_property": True,
        },
    )
    sphere__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_sphere", title="Extension field for ``sphere``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``VisionPrescriptionDispense`` according to specification,
        with preserving the original sequence order.
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
            "base",
            "add",
            "power",
            "backCurve",
            "diameter",
            "duration",
            "color",
            "brand",
            "note",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``VisionPrescriptionDispense`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]
